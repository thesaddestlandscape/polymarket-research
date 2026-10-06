#!/usr/bin/env python3
"""analisis_valor_relativo_llegada.py -- ¿el ask rancio del tramo CORTO sigue disponible cuando llegaría nuestra orden?
(06-Oct). Eventos = primer evento por ventana con inv_margen >= --margen en valor_relativo_anidado_v2 (asks reales);
con el registro ms (maker_ms, filas q con hora de RECEPCIÓN) se mira el ask del token comprado a t+L (L = 0..1000 ms):
'disponible' = ask(t+L) <= ask detectado y tamaño >= 5 acciones; y el EV por € comprando al ask(t+L) si sigue por
debajo de inv_bid15 detectado. Solo eventos cubiertos por el registro (desde 05-Oct 16:06Z)."""
import argparse, bisect, collections, csv, glob, gzip, sys
from datetime import datetime
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
LATS = [0, 100, 150, 215, 250, 300, 400, 600, 1000]
fee = lambda p: 0.07 * p * (1 - p)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--margen", type=float, default=0.03); a = ap.parse_args()
    F = []
    for f in sorted(glob.glob("/root/polymarket-research-datalogs/valor_relativo_anidado_v2_*.csv*")):
        F += list(csv.DictReader(gzip.open(f, "rt") if f.endswith(".gz") else open(f)))
    vis, ev = set(), []
    for r in sorted(F, key=lambda r: int(r["ts_ms"])):
        if r["par"] != "5m>15m" or int(r["ts_ms"]) < 1791223560000:      # 05-Oct 16:06Z
            continue
        try:
            if float(r["inv_margen"]) < a.margen:
                continue
        except ValueError:
            continue
        k = (r["activo"], r["fin"])
        if k not in vis:
            vis.add(k); ev.append(r)
    mids = {r["market5"] for r in ev}
    tok, q = {}, collections.defaultdict(list)
    for f in sorted(glob.glob("/root/polymarket-research-datalogs/maker_ms_*.csv.gz"), key=lambda f: Path(f).stat().st_mtime):
        try:
            for ln in gzip.open(f, "rt"):
                c = ln.rstrip("\n").split(",")
                if c[0] == "k" and c[5] in mids:
                    tok[(c[5], c[7])] = c[2]
                elif c[0] == "q" and c[2] in tok.values():
                    q[c[2]].append((int(c[7]) if len(c) > 7 and c[7] else int(c[1]), None if c[4] in ("", "None") else float(c[4]),
                                    0.0 if c[6] in ("", "None") else float(c[6])))
        except (EOFError, OSError):
            pass
    for k in q:
        q[k].sort(key=lambda x: x[0])
    des = desenlaces(mids)
    disp = collections.Counter(); evs = collections.defaultdict(list); n = 0
    for r in ev:
        lado = "NO" if r["lado"] == "Up" else "YES"          # inverso: comprar el lado contrario en el 5m
        t = tok.get((r["market5"], lado))
        if not t or not q[t] or r["market5"] not in des:
            continue
        n += 1
        ts = [x[0] for x in q[t]]; t0 = int(r["ts_ms"]); a0 = float(r["inv_ask5"]); b15 = float(r["inv_bid15"])
        gana = des[r["market5"]] == lado
        for L in LATS:
            i = bisect.bisect_right(ts, t0 + L) - 1
            if i < 0:
                continue
            ask, sz = q[t][i][1], q[t][i][2]
            if ask is not None and ask <= a0 + 1e-9 and sz >= 5:
                disp[L] += 1
            if ask is not None and ask < b15 and sz >= 5:
                evs[L].append(((1 - ask) / ask if gana else -1) - fee(ask) / ask)
    print(f"eventos cubiertos por el registro ms (margen >= {a.margen}): {n}")
    for L in LATS:
        v = evs[L]
        print(f"  +{L:4} ms: ask detectado aún disponible (>=5 acc.) {disp[L]}/{n} | comprable bajo bid15: {len(v)} "
              f"EV/€ {(sum(v) / len(v)) if v else 0:+.3f}")
main()
