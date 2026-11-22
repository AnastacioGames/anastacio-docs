"""Copia a fonte única (nucleo_editor, caminhos, sessao) para o complemento "Controle por IA" da engine.

Uso: python sincronizar_addon.py <raiz da engine> [--verificar]
--verificar só compara e sai com 1 se houver diferença (para teste/CI).
"""
import shutil, sys
from pathlib import Path

ARQUIVOS = ('nucleo_editor.py', 'caminhos.py', 'sessao.py')
aqui = Path(__file__).resolve().parent
raiz = Path(sys.argv[1])
destino = raiz / 'source' / 'release' / 'scripts' / 'addons' / 'anastacio_controle_ia'
diferentes = [n for n in ARQUIVOS if not (destino / n).exists() or (destino / n).read_bytes() != (aqui / n).read_bytes()]
if '--verificar' in sys.argv:
    print('diferentes:', diferentes or 'nenhum')
    sys.exit(1 if diferentes else 0)
for n in diferentes:
    shutil.copyfile(aqui / n, destino / n)
print('copiados:', diferentes or 'nenhum')
