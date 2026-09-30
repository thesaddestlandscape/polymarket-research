#!/usr/bin/env python3
"""vigia_valor_tras_salto_forward.py -- validación FORWARD de "valor tras salto de Binance".

Origen (30-Sep): las tomadoras que ganan de forma persistente sacan el 61 % de su PnL de compras
en las que la probabilidad justa según el subyacente supera al precio en >=10 puntos, y el 81 %
de su PnL de compras alineadas con un movimiento reciente de Binance. Cruzado con el observador
de ASK REAL tras saltos de Binance (binance_jump_leadlag_fase0, que lee el libro a +0/0,3/0,6/1 s):
comprar TODOS los saltos pierde (-6 % por € en 5 min), pero hay dosis-respuesta monótona en
    valor = Phi(z) - ask real,   z = signo * ln(S_t / S_apertura) / (sigma_1s * sqrt(segundos restantes))
(S = mid de Binance, sigma de los últimos 300 s, lado = el del salto):
    5 min, libro a +0,6 s, 25-30 Sep: valor < -0,10 -> -11 % (IC90 <0) ... valor >= 0,20 -> +14 % (IC90 >0).

Eso se vio mirando 48 celdas a posteriori, así que NO se da por bueno: aquí se CONGELAN tres
hipótesis (CORTE) y solo cuenta lo que ocurra después. Nada se reajusta.
    H1  5m   valor >= 0,10   entrada con el libro leído a +0,6 s
    H2  5m   valor >= 0,20   entrada a +0,6 s
    H3  15m  valor >= 0,03   entrada a +0,6 s
+0,6 s porque nuestra orden tarda ~250 ms y Polymarket añade 150 ms de taker delay.
Confirmada = n>=40, >=5 días, EV>=+0,10 por € (fee 7 %), IC90 por días >0, ningún activo >60 % de las entradas.
Solo lectura; Telegram diario con --telegram. Si se confirma: dry-run con ejecutor propio,
checklist de 6 categorías, /code-review y OK de Javi. No antes.
"""
import bisect
import csv
import gzip
import json
import math
import random
import statistics as st
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import analisis_binance_jump_leadlag as J

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
OUT = REPO / "data" / "shadow" / "vigia_valor_tras_salto_forward.json"
CORTE = "2026-09-30T10:00:00"
OFFSET = 0.6
FEE = 0.07
HIPOTESIS = {"H1 5m valor>=0,10": ("5m", 0.10), "H2 5m valor>=0,20": ("5m", 0.20), "H3 15m valor>=0,03": ("15m", 0.03),
             "H4 5m valor>=0,10 solo en RAFAGA": ("5m", 0.10)}
# H4 (30-Sep 18:05Z, programa cripto10): mismo H1 pero solo si en los 600 s ANTERIORES al salto el observador registró
# >= RAFAGA_MIN saltos entre TODAS las monedas (régimen medido antes de operar). Antes de su corte: TRAIN/VAL/holdout
# +0,119/+0,160/+0,319 (n=267/357/178), sin las 2 mejores horas +0,086; fuera de ráfaga negativo en los tres. Pocas horas
# independientes: solo cuenta el forward desde CORTE_POR_HIPOTESIS. Datalogs analisis_persistente_30sep/cripto10_30sep/.
RAFAGA_MIN, RAFAGA_S = 40, 600
CORTE_POR_HIPOTESIS = {"H4 5m valor>=0,10 solo en RAFAGA": "2026-09-30T18:10:00"}


def _phi(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def _cargar_binance(dias: set) -> dict:
    B = defaultdict(lambda: ([], []))
    for d in sorted(dias):
        for p in (DATALOGS / f"binance_bookticker_{d}.csv", DATALOGS / f"binance_bookticker_{d}.csv.gz"):
            if not p.exists():
                continue
            f = gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")
            with f:
                for r in csv.DictReader(f):
                    try:
                        B[r["activo"]][0].append(int(r["ts_recepcion_ms"]) / 1000)
                        B[r["activo"]][1].append(float(r["mid"]))
                    except (ValueError, TypeError):
                        continue
            break
    return B


def main() -> int:
    filas, todos_t = [], set()
    with open(J.CSV, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                todos_t.add(datetime.fromisoformat(r["ts_evento"]).timestamp())
            except (ValueError, TypeError, KeyError):
                pass
            if r.get("error") or not r.get("ask"):
                continue
            try:
                if abs(float(r["offset_s"]) - OFFSET) > 0.01:
                    continue
                a, ratio, resto = float(r["ask"]), float(r["ratio_vs_stake"] or 0), float(r["resto_s"])
                t = datetime.fromisoformat(r["ts_evento"]).timestamp()
            except (ValueError, TypeError):
                continue
            if not 0.03 <= a < 0.97 or ratio < 5 or resto < 5:
                continue
            filas.append((r["ts_evento"], t, r["activo"], r["marco"], r["market_id"], r["direccion"], a, resto))
    if not filas:
        print("sin filas")
        return 1
    dias = {x[0][:10] for x in filas} | {(datetime.fromisoformat(x[0]) - timedelta(days=1)).strftime("%Y-%m-%d") for x in filas}
    B = _cargar_binance(dias)
    ganador = J._resolver(sorted({x[4] for x in filas}))

    def mid(act, t, tol=20.0):
        bt, bm = B[act]
        i = bisect.bisect_right(bt, t) - 1
        return bm[i] if i >= 0 and t - bt[i] < tol else None

    sig = {}

    def sigma(act, t):
        k = (act, int(t) // 60)
        if k not in sig:
            xs = [mid(act, t - 300 + 5 * j) for j in range(61)]
            xs = [x for x in xs if x]
            rs = [math.log(y / x) for x, y in zip(xs, xs[1:])]
            sig[k] = (st.pstdev(rs) / math.sqrt(5)) if len(rs) >= 30 else None
        return sig[k]

    todos_l = sorted(todos_t)
    res = {h: {"antes": defaultdict(list), "forward": defaultdict(list)} for h in HIPOTESIS}
    activos = {h: defaultdict(int) for h in HIPOTESIS}
    for ts_ev, t, act, marco, mkt, dr, a, resto in filas:
        o = ganador.get(str(mkt))
        if o not in ("Up", "Down"):
            continue
        dur = 300 if marco == "5m" else 900
        m0, mo, s1 = mid(act, t), mid(act, t + resto - dur, 60.0), sigma(act, t)
        if not (m0 and mo and s1):
            continue
        z = (1 if dr == "Up" else -1) * math.log(m0 / mo) / (s1 * math.sqrt(resto))
        valor = _phi(z) - a
        pnl = (1 if dr == o else 0) / a - 1 - FEE * (1 - a)
        n_rafaga = bisect.bisect_left(todos_l, t) - bisect.bisect_left(todos_l, t - RAFAGA_S)
        for h, (mc, umbral) in HIPOTESIS.items():
            tramo = "forward" if ts_ev[:19] >= CORTE_POR_HIPOTESIS.get(h, CORTE) else "antes"
            if "RAFAGA" in h and n_rafaga < RAFAGA_MIN:
                continue
            if marco == mc and valor >= umbral:
                res[h][tramo][ts_ev[:10]].append(pnl)
                if tramo == "forward":
                    activos[h][act] += 1

    def resumen(vd: dict):
        x = [v for d in vd.values() for v in d]
        if not x:
            return {"n": 0}
        ks = [k for k in vd if vd[k]]
        ic = None
        if len(ks) >= 3:
            rng = random.Random(9)
            ms = []
            for _ in range(2000):
                s = [v for k in (rng.choice(ks) for _ in ks) for v in vd[k]]
                ms.append(sum(s) / len(s))
            ms.sort()
            ic = [round(ms[100], 4), round(ms[1900], 4)]
        return {"n": len(x), "dias": len(ks), "ev": round(sum(x) / len(x), 4), "ic90": ic,
                "dias_positivos": sum(1 for k in ks if sum(vd[k]) > 0)}

    informe, lineas = {}, [f"🧪 Valor tras salto de Binance — forward desde {CORTE}Z (ask real a +{OFFSET} s, fee 7 %)"]
    for h in HIPOTESIS:
        a, fw = resumen(res[h]["antes"]), resumen(res[h]["forward"])
        top = (max(activos[h].values()) / sum(activos[h].values())) if activos[h] else 0
        conf = bool(fw["n"] >= 40 and fw.get("dias", 0) >= 5 and fw["ev"] >= 0.10 and fw.get("ic90") and fw["ic90"][0] > 0 and top <= 0.60)
        informe[h] = {"antes_del_corte": a, "forward": fw, "activo_top_pct": round(top * 100), "confirmada": conf}
        lineas.append(f"{h}: forward n={fw['n']}" + (f" días={fw['dias']} EV {fw['ev']:+.3f}" + (f" IC90 {fw['ic90']}" if fw.get("ic90") else "") if fw["n"] else "")
                      + (f" | antes del corte n={a['n']} EV {a['ev']:+.3f}" if a["n"] else "") + (" ✅ CONFIRMADA" if conf else ""))
    lineas.append("Gate: n≥40, ≥5 días, EV≥+0,10, IC90 por días >0, ningún activo >60 %. Hasta entonces, nada con dinero.")
    OUT.write_text(json.dumps({"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "corte": CORTE,
                               "offset_s": OFFSET, "hipotesis": informe}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n".join(lineas))
    if "--telegram" in sys.argv:
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram("\n".join(lineas))
        except Exception as e:
            print(f"(no se pudo avisar por Telegram: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
