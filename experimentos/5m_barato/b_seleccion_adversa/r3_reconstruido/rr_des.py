#!/usr/bin/env python3
"""rr_des.py -- desenlaces OFICIALES (gamma-api publica, solo lectura) de los mercados CON FILL de un dia reconstruido -> r3_desenlaces_reconstruido_D.jsonl.gz (misma forma que r3_desenlaces).
Idempotente (clave des|slug). Un slug sin desenlace queda ausente (pendiente != 0). Uso: .venv/bin/python -I rr_des.py --dia D [--sub puerta]"""
import argparse
import gzip
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, "/root/polymarket-research/experimentos/5m_barato/b_seleccion_adversa/r3_shadow")
import r3_desenlaces as DS  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/r3_reconstruido")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dia", required=True)
    ap.add_argument("--sub", default="")
    a = ap.parse_args()
    d = OUT / a.sub if a.sub else OUT
    fr, fd = d / f"r3_reconstruido_{a.dia}.jsonl.gz", d / f"r3_desenlaces_reconstruido_{a.dia}.jsonl.gz"
    cierre, fills, ya = {}, set(), {}
    for ln in gzip.open(fr, "rt"):
        if '"tipo":"mkt_fin"' in ln or '"tipo":"fill"' in ln:
            r = json.loads(ln)
            if r["tipo"] == "mkt_fin":
                cierre[r["slug"]] = r["cierre"]
            else:
                fills.add(r["slug"])
    if fd.exists():
        ya = {json.loads(l)["slug"]: json.loads(l) for l in gzip.open(fd, "rt")}
    pend = sorted(s for s in fills if s not in ya or ya[s].get("ganador") is None)
    res, err, lotes = DS.desenlaces_gamma(pend) if pend else ({}, 0, 0)
    ahora = int(time.time() * 1000)
    for s in pend:
        if s in res:
            ya[s] = {"k": f"des|{s}", "tipo": "des", "r": cierre[s] * 1000, "slug": s, "cierre": cierre[s], "ganador": res[s], "resuelto_ms": ahora, "fuente": "reconstruido"}
    tmp = fd.with_suffix(".tmp")
    with gzip.open(tmp, "wt") as f:
        f.write("\n".join(json.dumps(v, separators=(",", ":")) for v in ya.values()) + "\n")
    os.replace(tmp, fd)
    sin = [s for s in fills if s not in ya or ya[s].get("ganador") is None]
    print(f"{a.dia}: mercados con fill={len(fills)} resueltos={len(fills) - len(sin)} pendientes={len(sin)} errores_gamma={err}/{lotes}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
