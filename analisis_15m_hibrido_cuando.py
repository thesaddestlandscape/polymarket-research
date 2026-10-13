#!/usr/bin/env python3
"""analisis_15m_hibrido_cuando.py -- 13-Oct (Javi: "ponte con 2 a ver si nos serviría"). Vía HÍBRIDA de la misión 15m:
¿CUÁNDO y a qué coste completa/refuerza la híbrida 0xb970fb5c (maker + tomador en el mismo mercado) y se sostiene fuera de
muestra? Pregunta útil para los pares 15m: ¿hay una forma de convertir una pata suelta en par, o de usar el relleno maker
como señal, que no sea "completar al instante" (refutado: bid+ask+fee >= 1; cubrir tras el relleno −6,7c/acc)?

Datos: rellenos on-chain 15m del archivo del volumen (m15_onchain, 05-12 Oct) filtrados por la wallet; mapa token ->
(moneda, mercado, cierre, lado) de las filas k del registro (m15_registro) + tokens.json de la caché 05-06; desenlace
oficial (desenlaces(), gamma closed=true). Rol: la fila cuyo `taker` es el contrato del exchange es la orden TOMADORA de
`maker`; el resto, rellenos MAKER de `maker`. side 0 = compra de `maker`.
Periodos: EXTRACCIÓN 05-07 (ya mirada el 08-Oct en analisis_15m_v4_hibridos.py) y VALIDACIÓN 08-12 (no mirada).
Cada compra TOMADORA se clasifica frente a la posición neta (acciones YES − NO) justo antes: CUBRE (compra el lado
contrario a su posición), REFUERZA (el mismo), ABRE (posición 0). Coste del par de una CUBRE = precio medio de compra del
lado que tenía + precio pagado + comisión por acción.
Uso: nice -n 19 python3 analisis_15m_hibrido_cuando.py [wallet]
"""
import collections
import gzip
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

VOL = Path("/mnt/HC_Volume_106538179")
DL = Path("/root/polymarket-research-datalogs")
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
WALLET = (sys.argv[1] if len(sys.argv) > 1 else "0xb970fb5c743b22e9c3df143f81075ad3c79c0000").lower()
EXT = ["2026-10-05", "2026-10-06", "2026-10-07"]
VAL = ["2026-10-08", "2026-10-09", "2026-10-10", "2026-10-11", "2026-10-12"]
INF = Path(__file__).resolve().parent / "informes" / f"m15_hibrido_cuando_{WALLET[:10]}_13oct.txt"


def mapa_tokens():
    m = {}
    f = DL / "m15_ms_cache" / "tokens.json"
    if f.exists():
        for tok, act, mid, fin, lado in json.load(open(f)):
            m[str(tok)] = (act, str(mid), int(fin), lado)
    for f in sorted((VOL / "m15_registro").glob("m15_registro_2026-10-*.csv.gz")):
        out = subprocess.run(f"zcat {f} 2>/dev/null | grep -a '^k,'", shell=True, capture_output=True).stdout.decode()
        for ln in out.splitlines():
            c = ln.split(",")
            if len(c) >= 8 and c[4] == "15min":
                m[c[2]] = (c[3], c[5], int(datetime.fromisoformat(c[6]).timestamp()), c[7])
    return m


def cargar(dias, tok):
    filas = []
    for d in dias:
        f = VOL / "m15_onchain" / f"m15_onchain_{d}.csv.gz"
        out = subprocess.run(f"zcat {f} | grep -F {WALLET}", shell=True, capture_output=True).stdout.decode()
        for ln in out.splitlines():
            c = ln.split(",")
            # tipo,bloque,ts_est,tx,log_index,order_hash,maker,taker,side,token_id,maker_amt,taker_amt,fee
            if c[0] != "F" or c[6].lower() != WALLET or c[9] not in tok:
                continue
            act, mkt, fin, lado = tok[c[9]]
            compra = c[8] == "0"
            mamt, tamt = float(c[10]), float(c[11])
            acc, usdc = (tamt, mamt) if compra else (mamt, tamt)
            if acc <= 0:
                continue
            filas.append(dict(dia=d, ts=float(c[2]), tx=c[3], li=int(c[4]), act=act, mkt=mkt, fin=fin, lado=lado,
                              compra=compra, acc=acc, usdc=usdc, p=usdc / acc, fee=float(c[12] or 0),
                              rol="tomador" if c[7].lower() == EXCH else "maker"))
    return filas


def ic90(x, n_boot=2000, seed=7):
    x = np.asarray(x, float)
    if len(x) < 2:
        return (float("nan"), float("nan"))
    r = np.random.default_rng(seed)
    m = x[r.integers(0, len(x), (n_boot, len(x)))].mean(1)
    return float(np.quantile(m, 0.05)), float(np.quantile(m, 0.95))


def analizar(filas, des, L, titulo):
    por_m = collections.defaultdict(list)
    for f in filas:
        if des.get(f["mkt"]) is not None:
            por_m[f["mkt"]].append(f)
    cob = len(por_m) / max(1, len({f["mkt"] for f in filas}))
    cat = collections.defaultdict(list)          # categoría -> [(pnl/€, acc, p, coste_par, dt_maker, dia, act)]
    mk_pnl, tk_pnl, merc_pnl, merc_dia = [], [], [], collections.defaultdict(float)
    for mkt, fs in por_m.items():
        fs.sort(key=lambda f: (f["ts"], f["li"]))
        gana = des[mkt]
        pos = {"YES": [0.0, 0.0], "NO": [0.0, 0.0]}   # [acciones, coste]
        ult_maker = {"YES": None, "NO": None}
        pm = 0.0
        for f in fs:
            w = 1.0 if f["lado"] == gana else 0.0
            pnl = (f["acc"] * w - f["usdc"] if f["compra"] else f["usdc"] - f["acc"] * w) - (f["fee"] if f["rol"] == "tomador" else 0.0)
            pm += pnl
            (tk_pnl if f["rol"] == "tomador" else mk_pnl).append(pnl)
            otro = "NO" if f["lado"] == "YES" else "YES"
            neto = pos["YES"][0] - pos["NO"][0]
            if f["rol"] == "tomador" and f["compra"]:
                lado_pos = "YES" if neto > 0 else ("NO" if neto < 0 else None)
                c = "ABRE" if lado_pos is None else ("REFUERZA" if lado_pos == f["lado"] else "CUBRE")
                coste_par = None
                if c == "CUBRE" and pos[otro][0] > 0:
                    coste_par = pos[otro][1] / pos[otro][0] + f["p"] + f["fee"] / f["acc"]
                um = ult_maker[f["lado"]] if c == "REFUERZA" else ult_maker[otro]
                dt = f["ts"] - um if um is not None else None
                cat[c].append((pnl / f["usdc"], f["usdc"], f["p"], coste_par, dt, f["dia"], f["act"], pnl))
            elif f["rol"] == "tomador":
                cat["VENDE"].append((pnl / max(f["usdc"], 1e-9), f["usdc"], f["p"], None, None, f["dia"], f["act"], pnl))
            if f["compra"]:
                pos[f["lado"]][0] += f["acc"]; pos[f["lado"]][1] += f["usdc"]
            else:
                k = min(f["acc"], pos[f["lado"]][0])
                if pos[f["lado"]][0] > 0:
                    pos[f["lado"]][1] *= 1 - k / pos[f["lado"]][0]
                pos[f["lado"]][0] -= k
            if f["rol"] == "maker" and f["compra"]:
                ult_maker[f["lado"]] = f["ts"]
        merc_pnl.append(pm)
        merc_dia[fs[0]["dia"]] += pm
    L(f"\n===== {titulo}: {len(por_m)} mercados (cobertura desenlace {cob:.0%}), rellenos {sum(map(len, por_m.values()))}")
    lo, hi = ic90(merc_pnl)
    L(f"PnL total {sum(merc_pnl):+.0f} $ (maker {sum(mk_pnl):+.0f}, tomador {sum(tk_pnl):+.0f}); por mercado "
      f"{np.mean(merc_pnl):+.2f} $ IC90 ({lo:+.2f},{hi:+.2f}); por día: " +
      ", ".join(f"{d[5:]} {v:+.0f}" for d, v in sorted(merc_dia.items())))
    for c in ["CUBRE", "REFUERZA", "ABRE", "VENDE"]:
        xs = cat.get(c, [])
        if not xs:
            continue
        r = np.array([x[0] for x in xs]); vol = sum(x[1] for x in xs); pnl = sum(x[7] for x in xs)
        lo, hi = ic90(r)
        L(f"  tomador {c:8s} n={len(xs):4d} vol {vol:7.0f} $ PnL {pnl:+7.0f} $ PnL/$ {pnl / max(vol, 1e-9):+.3f} "
          f"(media por orden {r.mean():+.3f} IC90 {lo:+.3f},{hi:+.3f}) precio P50 {np.median([x[2] for x in xs]):.2f}")
        if c == "CUBRE":
            cp = [x[3] for x in xs if x[3] is not None]
            if cp:
                cp = np.array(cp)
                L(f"     coste del par al cubrir: P25/50/75 {np.quantile(cp, .25):.3f}/{np.median(cp):.3f}/{np.quantile(cp, .75):.3f}"
                  f" | <1,00: {np.mean(cp < 1):.0%} | <0,97: {np.mean(cp < .97):.0%}")
        dts = [(x[4], x[0], x[1], x[7]) for x in xs if x[4] is not None]
        for a, b in [(0, 30), (30, 120), (120, 300), (300, 10**6)]:
            g = [t for t in dts if a <= t[0] < b]
            if len(g) >= 5:
                v = sum(t[2] for t in g); p = sum(t[3] for t in g)
                L(f"     {a}-{b if b < 10**6 else '∞'} s tras su relleno maker {'del mismo lado' if c == 'REFUERZA' else 'del otro lado'}:"
                  f" n={len(g)} PnL/$ {p / v:+.3f}")
    por_act = collections.defaultdict(lambda: [0.0, 0])
    for fs in por_m.values():
        pass
    return merc_pnl


def main():
    tok = mapa_tokens()
    lines = []

    def L(s=""):
        print(s, flush=True)
        lines.append(s)
    L(f"Híbrida {WALLET} — ¿cuándo cubre/refuerza y a qué coste? (tokens 15m mapeados: {len(tok)})")
    ext, val = cargar(EXT, tok), cargar(VAL, tok)
    des = desenlaces({f["mkt"] for f in ext + val})
    analizar(ext, des, L, "EXTRACCIÓN 05-07 (ya vista el 08-Oct)")
    analizar(val, des, L, "VALIDACIÓN 08-12 (no vista)")
    INF.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n-> {INF}")


if __name__ == "__main__":
    main()
