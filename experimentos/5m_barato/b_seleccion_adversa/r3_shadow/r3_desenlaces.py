#!/usr/bin/env python3
"""r3_desenlaces.py -- RESOLVEDOR (cron, cada 20 min) del brazo shadow R2/R3: anade el desenlace OFICIAL (gamma-api, closed=true) de cada mercado 5m cerrado.
Un solo escritor por fichero: r3_shadow.py escribe r3_shadow_D.jsonl.gz; este escribe r3_desenlaces_D.jsonl.gz (D = dia UTC del cierre). Idempotente (clave des|slug) y con
flock (dos cron simultaneos no duplican). Solo lectura de la API publica; sin ordenes ni claves.
Cobertura: imprime mercados cerrados / con relleno / resueltos / pendientes / abandonados (>6 h sin cerrar en gamma = `ganador: null`, motivo sin_resolver_6h; NUNCA se trata como 0).
Uso: .venv/bin/python -I r3_desenlaces.py [--dir DIR] [--dias 3]      (sale con 0 aunque haya pendientes; con 1 si gamma falla en TODOS los lotes)"""
import argparse
import fcntl
import json
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import r3_shadow as S  # noqa: E402

GAMMA = "https://gamma-api.polymarket.com/markets"
ESPERA_CIERRE_S, ABANDONO_S = 90, 6 * 3600


def desenlaces_gamma(slugs):
    """{slug: 'YES'|'NO'} de los mercados YA cerrados con desenlace inequivoco (Up gana => YES). Un slug ausente = pendiente (no es 0)."""
    import requests
    res, errores, lotes = {}, 0, 0
    for k in range(0, len(slugs), 40):
        lotes += 1
        try:
            r = requests.get(GAMMA, timeout=25, params=[("slug", s) for s in slugs[k:k + 40]] + [("closed", "true"), ("limit", "40")])
            r.raise_for_status()
            datos = r.json() or []
        except Exception as e:
            errores += 1
            print(f"{datetime.now(timezone.utc).isoformat()} gamma lote {k}: {type(e).__name__}: {str(e)[:80]}", file=sys.stderr, flush=True)
            continue
        for m in datos:
            out = m.get("outcomes")
            out = json.loads(out) if isinstance(out, str) else out
            pr = m.get("outcomePrices")
            pr = json.loads(pr) if isinstance(pr, str) else pr
            if not m.get("closed") or not out or [o.lower() for o in out] != ["up", "down"] or not pr or len(pr) != 2:
                continue
            if float(pr[0]) >= 0.999:
                res[m["slug"]] = "YES"
            elif float(pr[1]) >= 0.999:
                res[m["slug"]] = "NO"
    return res, errores, lotes


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=S.SALIDA_DEFECTO)
    ap.add_argument("--dias", type=int, default=3)
    a = ap.parse_args(argv)
    d = Path(a.dir)
    d.mkdir(parents=True, exist_ok=True)
    lock = open(d / ".desenlaces.lock", "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        print("otro resolvedor activo (lock): salgo")
        return 0
    ahora = time.time()
    hoy = datetime.fromtimestamp(ahora, timezone.utc).date()
    cerrados, con_fill, ya = {}, set(), set()
    for i in range(a.dias, -1, -1):
        dia = (hoy - timedelta(days=i)).isoformat()
        for row in S.leer_gz_tolerante(d / f"r3_shadow_{dia}.jsonl.gz"):
            t = row.get("tipo")
            if t == "mkt_fin":
                cerrados[row["slug"]] = row["cierre"]
            elif t == "fill":
                con_fill.add(row["slug"])
        for row in S.leer_gz_tolerante(d / f"r3_desenlaces_{dia}.jsonl.gz"):
            if row.get("tipo") == "des":
                ya.add(row["slug"])
    pend = [s for s, c in cerrados.items() if s not in ya and c + ESPERA_CIERRE_S < ahora]
    pend.sort(key=lambda s: (s not in con_fill, cerrados[s]))        # primero los que tienen rellenos
    res, errores, lotes = desenlaces_gamma(pend) if pend else ({}, 0, 0)
    out = S.Salida(d, prefijo="r3_desenlaces")
    nuevos = abandonados = 0
    for s in pend:
        c = cerrados[s]
        if s in res:
            out.put({"k": f"des|{s}", "tipo": "des", "r": c * 1000, "slug": s, "cierre": c, "ganador": res[s], "resuelto_ms": int(ahora * 1000)})
            nuevos += 1
        elif c + ABANDONO_S < ahora:
            out.put({"k": f"des|{s}", "tipo": "des", "r": c * 1000, "slug": s, "cierre": c, "ganador": None, "motivo": "sin_resolver_6h", "resuelto_ms": int(ahora * 1000)})
            abandonados += 1
    out.cerrar()
    quedan = len(pend) - nuevos - abandonados
    print(f"{datetime.now(timezone.utc).isoformat()} desenlaces: cerrados={len(cerrados)} con_fill={len(con_fill)} ya={len(ya)} candidatos={len(pend)} "
          f"nuevos={nuevos} abandonados={abandonados} pendientes={quedan} lotes={lotes} errores_gamma={errores}", flush=True)
    return 1 if lotes and errores == lotes else 0


if __name__ == "__main__":
    sys.exit(main())
