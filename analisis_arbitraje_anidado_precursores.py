#!/usr/bin/env python3
"""analisis_arbitraje_anidado_precursores.py -- B1 nueva fase, paso 1 (06-Oct, Javi: "explicar y predecir el nacimiento
del arbitraje"; estudiar el REPRICING del ask del 15m, no el arbitraje).

Universo: todas las ventanas 5m>15m del registro ms con referencia conocible (mismo par garantizado que
analisis_arbitraje_anidado_ms_scanner.py: A = pata del 15m, B = pata del 5m), solo con t >= inicio del 5m + 1,5 s.
Dos tablas (todo con hora de RECEPCIÓN y SOLO datos con recepción <= instante de decisión: sin look-ahead):
  EVENTOS: cada BAJADA del ask de A (pata 15m). Etiquetas (posteriores, solo para evaluar): baja en céntimos, si deja
    neto >= 0,0005 (crea arbitraje) y el neto resultante. Rasgos en td = t_evento - X para X en LEADS.
  REJILLA: cada 100 ms dentro de la ventana, rasgos en td y etiquetas: ¿bajada de A en los próximos H ms?, ¿arbitraje
    nace en los próximos H ms?, ¿con neto >= 1c / 5c?
Rasgos en td: Binance (precio de aggTrade, recepción) retorno en [td-w, td] para w = 100/250/500/1000/3000 ms con SIGNO "a favor de que
A se abarate" (A = Up -> Binance baja = +); |ret| y nº de cambios del mid en 1 s; edad de la última cotización de A y de
B; ask A, ask B, suma, neto en td; tamaño del top de A; operaciones en A y en B en los 1.000 ms previos; resto al cierre.
Salida: dos CSV en --dir. Uso: --desde 2026-10-05T16:06 --dir <carpeta>
"""
import argparse
import bisect
import collections
import csv
import glob
import gzip
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_arbitraje_anidado_ms_scanner import cargar_twap60, fee, SIM, GAP_MIN_BPS, REF_CONOCIBLE_MS  # noqa: E402

DL = "/root/polymarket-research-datalogs"
LEADS = [0, 10, 25, 50, 100, 150, 250, 500]
WS = [100, 250, 500, 1000, 3000]
HS = [25, 50, 100, 150, 250]
GRID_MS = 100


def ultimo(ts, vs, t):
    i = bisect.bisect_right(ts, t) - 1
    return (ts[i], vs[i]) if i >= 0 else (None, None)


def rasgos(td, w, binance, signo):
    qa_t, qa_v = w["qa"]
    qb_t, qb_v = w["qb"]
    f = {}
    ta, va = ultimo(qa_t, qa_v, td)
    tb, vb = ultimo(qb_t, qb_v, td)
    f["edad_A_ms"] = None if ta is None else td - ta
    f["edad_B_ms"] = None if tb is None else td - tb
    aA = va[0] if va else None
    aB = vb[0] if vb else None
    f["ask_A"], f["ask_B"] = aA, aB
    f["size_A"] = va[1] if va else None
    f["neto"] = (1 - aA - aB - fee(aA) - fee(aB)) if (aA and aB) else None
    bt, bm = binance
    _, m1 = ultimo(bt, bm, td)
    for ww in WS:
        _, m0 = ultimo(bt, bm, td - ww)
        f[f"bin_{ww}"] = None if (m0 is None or m1 is None) else signo * (m1 / m0 - 1) * 1e4
    i1, i0 = bisect.bisect_right(bt, td), bisect.bisect_right(bt, td - 1000)
    f["bin_cambios_1s"] = i1 - i0
    for lado, tr in (("A", w["ta"]), ("B", w["tb"])):
        f[f"trades_{lado}_1s"] = bisect.bisect_right(tr, td) - bisect.bisect_right(tr, td - 1000)
    f["resto_s"] = w["cierre"] - td / 1000
    return f


def procesar_ventana(w, binance_all, ev_out, grid_out):
    sym = SIM[w["moneda"]]
    if sym not in binance_all:
        return
    binance = binance_all[sym]
    signo = 1.0 if w["pata_A"].startswith("Up") else -1.0
    signo = -signo        # A = Up: Binance BAJA abarata A -> ret negativo * -1 = +
    qa_t, qa_v = w["qa"]
    qb_t, qb_v = w["qb"]
    t_ini = (w["cierre"] - 300) * 1000 + REF_CONOCIBLE_MS
    t_fin = w["cierre"] * 1000
    # eventos: bajadas del ask de A
    bajadas = []
    for i in range(1, len(qa_t)):
        t = qa_t[i]
        if not (t_ini <= t < t_fin):
            continue
        a0, a1 = qa_v[i - 1][0], qa_v[i][0]
        if a0 is None or a1 is None or a1 >= a0 - 1e-9:
            continue
        _, vb = ultimo(qb_t, qb_v, t)
        aB = vb[0] if vb else None
        neto_post = (1 - a1 - aB - fee(a1) - fee(aB)) if aB else None
        _, vb0 = ultimo(qb_t, qb_v, t - 1)
        neto_pre = (1 - a0 - vb0[0] - fee(a0) - fee(vb0[0])) if (vb0 and vb0[0]) else None
        bajadas.append(t)
        base = {"moneda": w["moneda"], "cierre": w["cierre"], "pata_A": w["pata_A"], "t_evento": t,
                "baja_c": round((a0 - a1) * 100, 2), "ask_antes": a0, "ask_despues": a1,
                "neto_post": neto_post, "crea_arb": int(neto_post is not None and neto_post >= 0.0005 and
                                                           (neto_pre is None or neto_pre < 0.0005))}
        for X in LEADS:
            r = rasgos(t - X, w, binance, signo)
            ev_out.writerow({**base, "lead_ms": X, **r})
    # rejilla
    bajadas.sort()
    arbs = []
    for i in range(1, len(qa_t)):
        t = qa_t[i]
        if t_ini <= t < t_fin and qa_v[i][0] is not None:
            _, vb = ultimo(qb_t, qb_v, t)
            if vb and vb[0]:
                n = 1 - qa_v[i][0] - vb[0] - fee(qa_v[i][0]) - fee(vb[0])
                if n >= 0.0005:
                    arbs.append((t, n))
    for j in range(1, len(qb_t)):       # el arbitraje también puede nacer por un cambio de B
        t = qb_t[j]
        if t_ini <= t < t_fin and qb_v[j][0] is not None:
            _, va = ultimo(qa_t, qa_v, t)
            if va and va[0]:
                n = 1 - va[0] - qb_v[j][0] - fee(va[0]) - fee(qb_v[j][0])
                if n >= 0.0005:
                    arbs.append((t, n))
    arbs.sort()
    at = [x[0] for x in arbs]
    for td in range(t_ini, t_fin - 250, GRID_MS):
        r = rasgos(td, w, binance, signo)
        if r["neto"] is not None and r["neto"] >= 0.0005:
            continue                     # ya hay arbitraje: no es "antes"
        lab = {}
        for H in HS:
            k0, k1 = bisect.bisect_right(bajadas, td), bisect.bisect_right(bajadas, td + H)
            lab[f"baja_{H}"] = int(k1 > k0)
            a0, a1 = bisect.bisect_right(at, td), bisect.bisect_right(at, td + H)
            mx = max((arbs[i][1] for i in range(a0, a1)), default=None)
            lab[f"arb_{H}"] = int(mx is not None)
            lab[f"arb1c_{H}"] = int(mx is not None and mx >= 0.01)
            lab[f"arb5c_{H}"] = int(mx is not None and mx >= 0.05)
            lab[f"arbneto_{H}"] = mx
        grid_out.writerow({"moneda": w["moneda"], "cierre": w["cierre"], "pata_A": w["pata_A"], "td": td, **r, **lab})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-05T16:06")
    ap.add_argument("--dir", required=True)
    a = ap.parse_args()
    t_desde = int(datetime.fromisoformat(a.desde).replace(tzinfo=timezone.utc).timestamp() * 1000)
    fich = sorted(glob.glob(f"{DL}/maker_ms_*.csv.gz"), key=lambda f: Path(f).stat().st_mtime)
    dias = sorted({Path(f).name[9:19] for f in fich})
    tw = cargar_twap60(dias)
    meta, idx, pares = {}, collections.defaultdict(dict), {}
    tok2w = {}
    binance = collections.defaultdict(lambda: ([], []))
    ventanas = {}
    rf = ["moneda", "cierre", "pata_A"]
    rasg = ["edad_A_ms", "edad_B_ms", "ask_A", "ask_B", "size_A", "neto"] + [f"bin_{x}" for x in WS] + \
        ["bin_cambios_1s", "trades_A_1s", "trades_B_1s", "resto_s"]
    Path(a.dir).mkdir(parents=True, exist_ok=True)
    fe = open(Path(a.dir) / "eventos_baja_15m.csv", "w", newline="")
    fg = open(Path(a.dir) / "rejilla_100ms.csv", "w", newline="")
    ev_out = csv.DictWriter(fe, fieldnames=rf + ["t_evento", "baja_c", "ask_antes", "ask_despues", "neto_post",
                                                  "crea_arb", "lead_ms"] + rasg)
    grid_out = csv.DictWriter(fg, fieldnames=rf + ["td"] + rasg + [f"{p}_{H}" for H in HS for p in
                                                                  ("baja", "arb", "arb1c", "arb5c", "arbneto")])
    ev_out.writeheader()
    grid_out.writeheader()
    n_ok = 0
    for f in fich:
        try:
            fh = gzip.open(f, "rt")
            for ln in fh:
                c = ln.rstrip("\n").split(",")
                tp = c[0]
                if tp == "x":
                    # 06-Oct: aggTrades (precio de cada operación, hora de RECEPCIÓN c[6]); las filas b (bookTicker) del
                    # registro son escasas (97 % de retornos 0 en 250 ms) y no sirven como precursor
                    if len(c) > 7 and c[7]:
                        t = int(c[7])      # x = T, símbolo, precio, cantidad, m, E, RECEPCIÓN (c[7])
                        if t >= t_desde - 10_000:
                            bb = binance[c[2]]
                            bb[0].append(t)
                            bb[1].append(float(c[3]))
                    continue
                if tp == "k":
                    if c[4] in ("5min", "15min"):
                        cierre = int(datetime.fromisoformat(c[6]).timestamp())
                        meta[c[2]] = (c[3], c[4], c[5], cierre, c[7])
                        idx[(c[3], cierre)][(c[4], c[7])] = c[2]
                        k = (c[3], cierre)
                        toks = idx[k]
                        if k not in pares and all(x in toks for x in (("5min", "YES"), ("5min", "NO"),
                                                                       ("15min", "YES"), ("15min", "NO"))):
                            rl, rc = tw.get(c[3], {}).get(cierre - 900), tw.get(c[3], {}).get(cierre - 300)
                            if rl is None or rc is None or abs((rc / rl - 1) * 1e4) < GAP_MIN_BPS:
                                pares[k] = None
                            else:
                                if rl < rc:
                                    A, B, pa = toks[("15min", "YES")], toks[("5min", "NO")], "Up_largo"
                                else:
                                    A, B, pa = toks[("15min", "NO")], toks[("5min", "YES")], "Down_largo"
                                pares[k] = True
                                ventanas[k] = {"moneda": c[3], "cierre": cierre, "pata_A": pa, "A": A, "B": B,
                                               "qa": ([], []), "qb": ([], []), "ta": [], "tb": []}
                                tok2w[A] = (k, "a")
                                tok2w[B] = (k, "b")
                    continue
                if tp in ("q", "t"):
                    m = tok2w.get(c[2])
                    if not m:
                        continue
                    w = ventanas.get(m[0])
                    if w is None:
                        continue
                    if tp == "q":
                        tr = int(c[7]) if len(c) > 7 and c[7] else int(c[1])
                        ask = None if c[4] in ("", "None") else float(c[4])
                        asz = 0.0 if c[6] in ("", "None") else float(c[6])
                        w["q" + m[1]][0].append(tr)
                        w["q" + m[1]][1].append((ask, asz))
                    else:
                        tr = int(c[6]) if len(c) > 6 and c[6] else int(c[1])
                        w["t" + m[1]].append(tr)
                    # cerrar ventanas vencidas
                    if tr > (w["cierre"] + 5) * 1000 and not w.get("hecha"):
                        pass
            fh.close()
        except (EOFError, OSError) as ex:
            print(f"  aviso: {Path(f).name} truncado ({type(ex).__name__})", file=sys.stderr)
    for s in binance:
        o = sorted(range(len(binance[s][0])), key=binance[s][0].__getitem__)
        binance[s] = ([binance[s][0][i] for i in o], [binance[s][1][i] for i in o])
    for k, w in sorted(ventanas.items(), key=lambda kv: kv[1]["cierre"]):
        if w["cierre"] * 1000 < t_desde + 300_000:
            continue
        for lado in ("qa", "qb"):
            o = sorted(range(len(w[lado][0])), key=w[lado][0].__getitem__)
            w[lado] = ([w[lado][0][i] for i in o], [w[lado][1][i] for i in o])
        w["ta"].sort()
        w["tb"].sort()
        procesar_ventana(w, binance, ev_out, grid_out)
        n_ok += 1
        w["qa"], w["qb"] = ([], []), ([], [])
    fe.close()
    fg.close()
    print(f"ventanas procesadas: {n_ok} -> {a.dir}")


if __name__ == "__main__":
    main()
