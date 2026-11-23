"""Roda dentro do editor SEM janela (via lote_executar do MCP): aplica uma lista de passos numa cópia do projeto.

    AnastacioEngine -b <copia.range> --python lote_editor.py -- <passos.json> <resultado.json>

Usa as mesmas regras do editor ao vivo (nucleo_editor.py): operadores de código, `definir` fora do projeto e `py`
continuam bloqueados sem ANASTACIO_CRIADOR_PY=1. Se algum passo falhar, nada é gravado. Se todos passarem, grava a cópia
e escreve em <resultado.json> o resumo do que mudou (objetos criados, removidos e alterados).
"""
import json, os, sys, traceback
import bpy

_pasta = os.path.dirname(os.path.abspath(sys.argv[sys.argv.index('--python') + 1]))
sys.path.insert(0, _pasta)
import nucleo_editor as nucleo  # noqa: E402

ARGS = sys.argv[sys.argv.index('--') + 1:]
PASSOS, RESULTADO = ARGS[0], ARGS[1]
IDENT = ARGS[2] if len(ARGS) > 2 else ''
# Módulos de operadores que mexem com arquivos, janelas, render, texto ou preferências: não cabem num lote
# (que roda sem janela, numa cópia). Para esses, use a edição ao vivo.
MODULOS_FORA_DO_LOTE = {'wm', 'file', 'render', 'image', 'sound', 'screen', 'script', 'console', 'text', 'ui', 'buttons',
                        'outliner', 'info', 'nla', 'sequencer', 'clip', 'cachefile'}
PERMITIDOS = {'op', 'definir', 'script_gravar', 'script_ligar', 'ler', 'py'}
LIMITE_PASSOS = 500


def _arred(valores):
    return tuple(round(v, 4) for v in valores)


def foto_extra():
    """Scripts (nome -> conteúdo), materiais (nome -> aparência) e cenas (nome -> ajustes): o que a foto dos objetos não mostra."""
    return {'scripts': {t.name: t.as_string() for t in bpy.data.texts},
            'materiais': {m.name: (_arred(m.diffuse_color), _arred(m.specular_color), round(m.alpha, 4), m.use_shadeless,
                                   tuple(s.texture.name for s in m.texture_slots if s and s.texture))
                          for m in bpy.data.materials},
            'cenas': {c.name: (c.frame_start, c.frame_end, c.render.fps, _arred(c.gravity), c.camera.name if c.camera else None)
                      for c in bpy.data.scenes}}


def foto():
    return {o.name: (tuple(round(v, 5) for v in o.location), tuple(round(v, 5) for v in o.rotation_euler),
                     tuple(round(v, 5) for v in o.scale), o.parent.name if o.parent else None,
                     o.data.name if getattr(o, 'data', None) else None,
                     tuple(s.material.name for s in o.material_slots if s.material),
                     (len(o.data.vertices), round(sum(v.co.x + v.co.y + v.co.z for v in o.data.vertices), 3))
                     if o.type == 'MESH' else None,
                     tuple((p.name, str(p.value)) for p in o.game.properties))
            for o in bpy.data.objects}


def diferenca(antes, depois, extra_antes, extra_depois):
    ea, ed = extra_antes['scripts'], extra_depois['scripts']
    return {'criados': sorted(set(depois) - set(antes)), 'removidos': sorted(set(antes) - set(depois)),
            'alterados': sorted(n for n in set(antes) & set(depois) if antes[n] != depois[n]),
            'scripts_criados': sorted(set(ed) - set(ea)), 'scripts_removidos': sorted(set(ea) - set(ed)),
            'scripts_alterados': sorted(n for n in set(ea) & set(ed) if ea[n] != ed[n]),
            'materiais_criados': sorted(set(extra_depois['materiais']) - set(extra_antes['materiais'])),
            'materiais_removidos': sorted(set(extra_antes['materiais']) - set(extra_depois['materiais'])),
            'materiais_alterados': sorted(n for n in set(extra_antes['materiais']) & set(extra_depois['materiais'])
                                          if extra_antes['materiais'][n] != extra_depois['materiais'][n]),
            'cenas_criadas': sorted(set(extra_depois['cenas']) - set(extra_antes['cenas'])),
            'cenas_removidas': sorted(set(extra_antes['cenas']) - set(extra_depois['cenas'])),
            'cenas_alteradas': sorted(n for n in set(extra_antes['cenas']) & set(extra_depois['cenas'])
                                      if extra_antes['cenas'][n] != extra_depois['cenas'][n]),
            'nao_coberto_pelo_resumo': 'forma das malhas, propriedades de jogo, logic bricks, texturas e outros ajustes finos'}


def passo_op(p):
    if p['nome'] in nucleo.OPS_TEXTO_ATIVO:
        raise PermissionError('%s edita o texto ativo: use script_gravar' % p['nome'])
    modulo = p['nome'].split('.', 1)[0]
    if modulo in MODULOS_FORA_DO_LOTE or modulo.startswith(('export_', 'import_')):
        raise PermissionError('%s (módulo %s) mexe com arquivos, janelas ou preferências: não cabe num lote; '
                              'faça ao vivo no editor' % (p['nome'], modulo))
    if nucleo.grava_arquivo(p['nome']) and not nucleo.PY_LIBERADO:
        raise PermissionError('%s grava arquivos em caminhos livres: só com ANASTACIO_CRIADOR_PY=1' % p['nome'])
    if p['nome'] in nucleo.OPS_DE_CODIGO and not nucleo.PY_LIBERADO:
        raise PermissionError('%s executa código: só com ANASTACIO_CRIADOR_PY=1' % p['nome'])
    if p['nome'] in nucleo.CARREGAM_ARQUIVO:
        raise PermissionError('%s troca o arquivo aberto: não cabe num lote' % p['nome'])
    try:
        estado = sorted(nucleo.operador(p['nome'])('EXEC_DEFAULT', **(p.get('args') or {})))
    except RuntimeError as erro:  # poll falhou: sem contexto de janela
        raise RuntimeError('%s não roda sem janela (%s); faça esse passo ao vivo no editor' % (p['nome'], erro))
    if 'FINISHED' not in estado:
        raise RuntimeError('%s terminou como %s (não fez nada); faça esse passo ao vivo no editor' % (p['nome'], estado))
    return {'estado': estado}


def executar(passo):
    cmd = passo.get('cmd')
    if cmd not in PERMITIDOS:
        raise PermissionError('passo "%s" não permitido num lote (permitidos: %s)' % (cmd, ', '.join(sorted(PERMITIDOS))))
    if cmd == 'op':
        return passo_op(passo)
    return nucleo.COMANDOS[cmd](passo)


def principal():
    passos = json.loads(open(PASSOS, encoding='utf-8').read())
    saida = {'ok': False, 'executados': 0, 'ident': IDENT}
    try:
        if not isinstance(passos, list) or len(passos) > LIMITE_PASSOS:
            raise ValueError('passos deve ser uma lista de até %d itens' % LIMITE_PASSOS)
        antes, extra_antes = foto(), foto_extra()
        resultados = []
        for i, passo in enumerate(passos):
            try:
                resultados.append(executar(passo))
            except Exception as erro:
                saida.update(erro='passo %d (%s): %s' % (i + 1, passo.get('cmd'), erro),
                             detalhe=traceback.format_exc()[-600:])
                raise
            saida['executados'] = i + 1
        mudou = diferenca(antes, foto(), extra_antes, foto_extra())
        if 'FINISHED' not in bpy.ops.wm.save_mainfile(filepath=bpy.data.filepath):  # só depois de gravar o lote vale
            raise RuntimeError('não consegui gravar a cópia')
        saida.update(ok=True, resultados=[nucleo.texto(r) for r in resultados], mudou=mudou)
    except Exception as erro:
        saida.setdefault('erro', str(erro))
    open(RESULTADO, 'w', encoding='utf-8').write(json.dumps(saida, ensure_ascii=False))


principal()
