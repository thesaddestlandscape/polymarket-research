#!/usr/bin/env python3
"""analisis_ref_twap_modelos_shadow_24sep.py -- impacto de corregir la referencia de
los modelos de precio de shadow_predict (s_updown_gbm / _s_gbm_late) a la regla
real de resolución (24-Sep, OK Javi: "atácalo ahora").

Compara la DIRECCIÓN implícita (signo de pct = spot/ref - 1) contra el outcome
real de gamma en mercados 5/15min, a varios segundos del cierre:
  VIEJA: spot = TWAP últimos 60 s de Chainlink (BTC/ETH/SOL/XRP) o consenso
         (DOGE/BNB); ref = precio de consenso más cercano a la apertura (±3 min).
  NUEVA: ref = TWAP Chainlink en [apertura-60, apertura] (hora del oráculo);
         actual = spot Chainlink si quedan >60 s, si no TWAP proyectado.
Solo lectura. Reusa los cargadores de analisis_precierre_twap_multidia_24sep.py.
"""
import bisect
import csv
import glob
import gzip
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import analisis_precierre_twap_multidia_24sep as m  # noqa: E402

OFFSETS = [-240, -120, -60, -30]
OFICIALES_VIEJO = {"BTC", "ETH", "SOL", "XRP"}


def consenso_dia(dias):
    s = defaultdict(lambda: ([], []))
    for d in dias:
        for p in glob.glob(str(REPO / f"data/prices/{d}.csv*")):
            f = gzip.open(p, "rt") if p.endswith(".gz") else open(p)
            for r in csv.DictReader(f):
                try:
                    t = datetime.fromisoformat(r["timestamp_utc"]).timestamp(); v = float(r["price_usd"])
                except (ValueError, KeyError):
                    continue
                s[r["asset"]][0].append(t); s[r["asset"]][1].append(v)
    for a in s:
        o = sorted(zip(*s[a])); s[a] = ([x for x, _ in o], [y for _, y in o])
    return s


def cercano(ser, t, tol):
    xs, ys = ser
    i = bisect.bisect_left(xs, t)
    cands = [j for j in (i - 1, i) if 0 <= j < len(xs)]
    if not cands:
        return None
    j = min(cands, key=lambda j: abs(xs[j] - t))
    return ys[j] if abs(xs[j] - t) <= tol else None


def main():
    n_dias = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    hoy = datetime.now(timezone.utc).date()
    dias = [(hoy - timedelta(days=k)).isoformat() for k in range(n_dias, 0, -1)]
    acc = defaultdict(lambda: [0, 0, 0])  # n, ok_vieja, ok_nueva
    for d in dias:
        prev = (datetime.fromisoformat(d) - timedelta(days=1)).date().isoformat()
        cl = m.chainlink_dias([prev, d]); cons = consenso_dia([prev, d])
        L = m.libros_dia(d); res = m.outcomes(L.keys())
        print(f"{d}: {len(res)} mercados", flush=True)
        for mid, (gan, _toks, fin) in res.items():
            act, marco = L[mid]["meta"]; s = cl.get(act); c = cons.get(act)
            if not s or not c:
                continue
            ini = fin - m.DUR[marco]
            ref_new, n_i = m.media(s, ini - 60, ini)
            ref_old = cercano(c, ini, 180)
            if ref_new is None or n_i < 20 or ref_old is None:
                continue
            for off in OFFSETS:
                t = fin + off
                # VIEJA
                if act in OFICIALES_VIEJO:
                    sp_old, n60 = m.media(s, t - 60, t)
                    if not sp_old or n60 < 2:
                        sp_old = cercano(c, t, 60)
                else:
                    sp_old = cercano(c, t, 60)
                # NUEVA
                spot = m.valor_en(s, t)
                if spot is None or sp_old is None:
                    continue
                if -off > 60:
                    sp_new = spot
                else:
                    mc, nc = m.media(s, fin - 60, t)
                    resto = -off
                    sp_new = (mc * nc + spot * resto) / (nc + resto) if mc else spot
                a = acc[(marco, off, act)]
                a[0] += 1
                a[1] += int((0 if sp_old > ref_old else 1) == gan)
                a[2] += int((0 if sp_new > ref_new else 1) == gan)
    print("\nacierto de dirección (VIEJA -> NUEVA) por marco/offset/moneda:")
    for marco in ("5min", "15min"):
        for off in OFFSETS:
            tot = [0, 0, 0]
            fila = []
            for act in ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"):
                a = acc.get((marco, off, act))
                if not a or not a[0]:
                    continue
                tot = [x + y for x, y in zip(tot, a)]
                fila.append(f"{act} {a[1]/a[0]:.3f}->{a[2]/a[0]:.3f}")
            if tot[0]:
                print(f"  {marco} T{off:+d}s n={tot[0]} TOTAL {tot[1]/tot[0]:.4f} -> {tot[2]/tot[0]:.4f} | " + "  ".join(fila))


if __name__ == "__main__":
    main()
