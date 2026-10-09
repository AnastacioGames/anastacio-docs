"""Junta um lote de tradução em traducao/pt.json.

O lote é um .txt com uma tradução por linha, na mesma ordem dos trechos da
página em traducao/pendente.json (rode gerar_paginas.py antes).

Uso: python tools/aplicar_lote.py KX_Scene traducao/lotes/KX_Scene.txt
"""
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parents[1]
PT = AQUI / "traducao" / "pt.json"
PENDENTE = AQUI / "traducao" / "pendente.json"

pagina, lote = sys.argv[1], Path(sys.argv[2])
chaves = list(json.loads(PENDENTE.read_text(encoding="utf-8")).get(pagina, {}))
linhas = [l for l in lote.read_text(encoding="utf-8").splitlines() if l.strip()]
if len(chaves) != len(linhas):
    sys.exit(f"{pagina}: {len(chaves)} trechos pendentes, mas o lote tem {len(linhas)} linhas")
pt = json.loads(PT.read_text(encoding="utf-8")) if PT.exists() else {}
pt.update(zip(chaves, linhas))
PT.write_text(json.dumps(pt, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
print(f"{pagina}: {len(linhas)} trechos adicionados; pt.json tem {len(pt)}")
