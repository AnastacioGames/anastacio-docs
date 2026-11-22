"""Roda dentro do editor da Anastacio Engine e deixa o MCP do criador controlá-lo por TCP local.

Carregado com: AnastacioEngine <projeto> --python servidor_editor.py -- <arquivo_de_sessao>
É o modo em que o MCP abre o editor. O núcleo está em nucleo_editor.py (o mesmo do complemento
"Controle por IA", que serve para o editor que o usuário já abriu). Aqui o controle já nasce liberado.
"""
import os, sys
import bpy

_pasta = os.path.dirname(os.path.abspath(sys.argv[sys.argv.index('--python') + 1])) if '--python' in sys.argv else os.getcwd()
sys.path.insert(0, _pasta)
import nucleo_editor as nucleo  # noqa: E402

argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
quadros = [0]


def iniciar(_cena):
    quadros[0] += 1
    if quadros[0] < 3:
        return
    bpy.app.handlers.scene_update_post.remove(iniciar)
    nucleo.ligar(argv[0], observar=False)
    nucleo.iniciar_modal()


@bpy.app.handlers.persistent
def religar(_arquivo):
    quadros[0] = 0
    if iniciar not in bpy.app.handlers.scene_update_post:
        bpy.app.handlers.scene_update_post.append(iniciar)


nucleo.registrar()
bpy.app.handlers.scene_update_post.append(iniciar)
bpy.app.handlers.load_post.append(religar)
