"""Aplica vários lotes de uma vez, a partir de um arquivo combinado.

O arquivo tem seções "===== <pagina>" seguidas de uma tradução por linha,
na ordem de traducao/pendente.json. Uma linha "=" mantém o texto original
(útil para trechos que já estão em português). Cada seção também é gravada
em traducao/lotes/<pagina>.txt.

Uso: python tools/aplicar_varios.py traducao/lotes/combinado.txt
"""
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parents[1]
PT = AQUI / "traducao" / "pt.json"
PENDENTE = AQUI / "traducao" / "pendente.json"
LOTES = AQUI / "traducao" / "lotes"

pendente = json.loads(PENDENTE.read_text(encoding="utf-8"))
secoes, atual = {}, None
for l in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    if l.startswith("===== "):
        atual = l[6:].strip()
        secoes[atual] = []
    elif l.strip() and atual:
        secoes[atual].append(l.strip())

pt = json.loads(PT.read_text(encoding="utf-8")) if PT.exists() else {}
erros = 0
for pagina, linhas in secoes.items():
    chaves = list(pendente.get(pagina, {}))
    if len(chaves) != len(linhas):
        print(f"ERRO {pagina}: {len(chaves)} trechos pendentes, lote tem {len(linhas)}")
        erros += 1
        continue
    linhas = [c.replace("\n", " ") if t == "=" else t for c, t in zip(chaves, linhas)]
    (LOTES / f"{pagina}.txt").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    pt.update(zip(chaves, linhas))
    print(f"{pagina}: {len(linhas)}")
PT.write_text(json.dumps(pt, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
print(f"pt.json tem {len(pt)}; {erros} seções com erro")
