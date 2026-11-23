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
PERMITIDOS = {'op', 'definir', 'script_gravar', 'script_ligar', 'ler', 'py'}
LIMITE_PASSOS = 500


def foto():
    return {o.name: (tuple(round(v, 5) for v in o.location), tuple(round(v, 5) for v in o.rotation_euler),
                     tuple(round(v, 5) for v in o.scale), o.parent.name if o.parent else None,
                     o.data.name if getattr(o, 'data', None) else None,
                     tuple(s.material.name for s in o.material_slots if s.material))
            for o in bpy.data.objects}


def diferenca(antes, depois):
    return {'criados': sorted(set(depois) - set(antes)), 'removidos': sorted(set(antes) - set(depois)),
            'alterados': sorted(n for n in set(antes) & set(depois) if antes[n] != depois[n])}


def passo_op(p):
    if p['nome'] in nucleo.OPS_TEXTO_ATIVO:
        raise PermissionError('%s edita o texto ativo: use script_gravar' % p['nome'])
    if p['nome'] in nucleo.OPS_DE_CODIGO and not nucleo.PY_LIBERADO:
        raise PermissionError('%s executa código: só com ANASTACIO_CRIADOR_PY=1' % p['nome'])
    if p['nome'] in nucleo.CARREGAM_ARQUIVO:
        raise PermissionError('%s troca o arquivo aberto: não cabe num lote' % p['nome'])
    try:
        return {'estado': sorted(nucleo.operador(p['nome'])('EXEC_DEFAULT', **(p.get('args') or {})))}
    except RuntimeError as erro:  # poll falhou: sem contexto de janela
        raise RuntimeError('%s não roda sem janela (%s); faça esse passo ao vivo no editor' % (p['nome'], erro))


def executar(passo):
    cmd = passo.get('cmd')
    if cmd not in PERMITIDOS:
        raise PermissionError('passo "%s" não permitido num lote (permitidos: %s)' % (cmd, ', '.join(sorted(PERMITIDOS))))
    if cmd == 'op':
        return passo_op(passo)
    return nucleo.COMANDOS[cmd](passo)


def principal():
    passos = json.loads(open(PASSOS, encoding='utf-8').read())
    saida = {'ok': False, 'executados': 0}
    try:
        if not isinstance(passos, list) or len(passos) > LIMITE_PASSOS:
            raise ValueError('passos deve ser uma lista de até %d itens' % LIMITE_PASSOS)
        antes = foto()
        resultados = []
        for i, passo in enumerate(passos):
            try:
                resultados.append(executar(passo))
            except Exception as erro:
                saida.update(erro='passo %d (%s): %s' % (i + 1, passo.get('cmd'), erro),
                             detalhe=traceback.format_exc()[-600:])
                raise
            saida['executados'] = i + 1
        saida.update(ok=True, resultados=[nucleo.texto(r) for r in resultados], mudou=diferenca(antes, foto()))
        bpy.ops.wm.save_mainfile(filepath=bpy.data.filepath)
    except Exception as erro:
        saida.setdefault('erro', str(erro))
    open(RESULTADO, 'w', encoding='utf-8').write(json.dumps(saida, ensure_ascii=False))


principal()
