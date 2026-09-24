#!/usr/bin/env python3
"""ask_real_por_senal.py -- FUENTE ÚNICA del ASK REAL por señal del shadow (24-Sep, Javi: "que cuente
el ask real... dale a las tres y soluciónalo").

Problema (auditoría 24-Sep, analisis_auditoria_twap_estrategias_24sep.py): todo lo que se mide sobre
results.csv usa precio_yes_mercado, el precio de la SEÑAL, que va desfasado: cuando llega la señal
el mercado ya se ha movido. De 49 bueno_confirmado de gate_bucket_propio solo 4 sobreviven al ask
real. Este proceso mide, para cada señal, el ask REAL de nuestro token justo DESPUÉS de la señal y
lo publica para que lo consuman gate_bucket_propio (veto), analisis_kelly_precio_gate_29jul.py y
analisis_log_growth.py (misma base de precio, nunca reimplementada aparte).

Método (idéntico a la auditoría, orden temporal estricto, sin look-ahead):
  - señales = PRIMERA predicción por (strategy, market_id, decision) de results.csv, marcos 5/15/60min,
    6 monedas, últimos DIAS días (la que ejecutaría live; las repeticiones del ciclo no añaden info).
  - ask = best_ask del token propio en libro_book_ws (datalogs, log agregado del websocket) en la
    primera fila con ts >= t_señal y <= t+ASK_MAX_S. Token YES deducido por el bid final + outcome_real.
    Sin profundidad (el log no la trae): cota OPTIMISTA de fill -- un bucket que pierde aquí pierde más.
Salidas:
  data/shadow/ask_real_por_senal.csv   strategy,market_id,decision,prediction_timestamp,py,ask,acierto
  data/shadow/gate_bucket_ask_real.json {tupla: {bucket: {n_ask, eur_ask, ic90_dias, dias, dias_pos}}}
    (tupla = STRATEGY#ACTIVO#MARCO#DECISION, bucket = gate_bucket_propio.bucket(py), clave "%.2f")
Cron diario (05:40 UTC, antes de los gates de las 06:5x). ~20 min con nice.
"""
import csv
import json
import os
import random
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import analisis_auditoria_twap_estrategias_24sep as A
from analisis_gate_bucket_propio_28jul import ESTRATEGIAS_FIX_PRECIO_CANDIDATA9_10, FECHA_FIX_PRECIO_CANDIDATA9_10
from gate_bucket_propio import bucket

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data/shadow/results.csv"
OUT_CSV = REPO / "data/shadow/ask_real_por_senal.csv"
OUT_JSON = REPO / "data/shadow/gate_bucket_ask_real.json"
DIAS = int(os.environ.get("DIAS", "21"))
DUR = {"5min": 300, "15min": 900, "60min": 3600}
ACTIVOS = {"BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"}
FEE = 0.07
csv.field_size_limit(10_000_000)


def pnl(entry, ac):
    return (1 - entry) / entry * (1 - FEE) if ac else -1.0


def cargar_senales(desde):
    vistos, sen = set(), []
    with open(RESULTS, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            pt = r.get("prediction_timestamp") or ""
            if pt < desde:
                continue
            sub = r.get("subtype") or ""
            if "#" not in sub:
                continue
            act, marco = sub.split("#")[0], sub.split("#")[-1]
            dec = r.get("decision")
            if marco not in DUR or act not in ACTIVOS or dec not in ("BUY_YES", "BUY_NO") \
                    or r.get("acierto") not in ("0", "1"):
                continue
            k = (r["strategy"], r["market_id"], dec)
            if k in vistos:
                continue
            try:
                py = float(r["precio_yes_mercado"])
                t = A.ts(pt)
            except (ValueError, KeyError):
                continue          # /code-review: se marca como vista SOLO una fila válida
            # /code-review: mismo filtro que analisis_gate_bucket_propio_28jul.py -- BUY_NO de
            # CANDIDATA9/10 antes del fix de precio invertido cae en el bucket espejo.
            if (r["strategy"] in ESTRATEGIAS_FIX_PRECIO_CANDIDATA9_10 and dec == "BUY_NO"
                    and datetime.fromtimestamp(t, timezone.utc) < FECHA_FIX_PRECIO_CANDIDATA9_10):
                continue
            vistos.add(k)
            sen.append({"st": r["strategy"], "act": act, "marco": marco, "mid": r["market_id"], "dec": dec,
                        "pt": pt, "t": t, "py": py, "ac": int(r["acierto"]),
                        "outc": (r.get("outcome_real") or "").upper()})
    return sen


def ic90_dias(xs):
    dias = defaultdict(list)
    for dia, v in xs:
        dias[dia].append(v)
    ds = list(dias.values())
    if len(ds) < 2:
        return None, len(ds), sum(1 for v in ds if sum(v) > 0)
    rng, med = random.Random(3), []
    for _ in range(1000):
        m = [v for _ in ds for v in rng.choice(ds)]
        med.append(sum(m) / len(m))
    med.sort()
    return [round(med[50], 4), round(med[949], 4)], len(ds), sum(1 for v in ds if sum(v) > 0)


def main() -> int:
    ahora = datetime.now(timezone.utc)
    desde = (ahora - timedelta(days=DIAS)).strftime("%Y-%m-%d")
    sen = cargar_senales(desde)
    print(f"[{ahora.isoformat(timespec='seconds')}] señales {len(sen)} desde {desde}", flush=True)
    por_dia = defaultdict(list)
    for s in sen:
        por_dia[datetime.fromtimestamp(s["t"], timezone.utc).date().isoformat()].append(s)
    tmp = OUT_CSV.with_suffix(".csv.tmp")
    agg = defaultdict(list)
    n_ask = 0
    with open(tmp, "w", newline="", encoding="utf-8") as fo:
        w = csv.writer(fo)
        w.writerow(["strategy", "market_id", "decision", "prediction_timestamp", "py", "ask", "acierto"])
        for dia in sorted(por_dia):
            L = A.libro(dia, {s["mid"] for s in por_dia[dia]})
            for s in por_dia[dia]:
                ask = None
                ty = A.token_yes(L.get(s["mid"], {}), s["outc"])
                if ty:
                    tn = next((a for a in L[s["mid"]] if a != ty), None)
                    tok = ty if s["dec"] == "BUY_YES" else tn
                    ask = A.ask_tras(L[s["mid"]][tok], s["t"]) if tok else None
                w.writerow([s["st"], s["mid"], s["dec"], s["pt"], s["py"], "" if ask is None else ask, s["ac"]])
                if ask is not None:
                    n_ask += 1
                    tupla = f"{s['st']}#{s['act']}#{s['marco']}#{s['dec']}"
                    agg[(tupla, f"{bucket(s['py']):.2f}")].append((dia, pnl(ask, s["ac"])))
            print(f"  {dia}: {len(por_dia[dia])} señales, mercados libro {len(L)}", flush=True)
            del L
    tmp.replace(OUT_CSV)
    buckets = defaultdict(dict)
    for (tupla, b), xs in agg.items():
        ic, nd, dp = ic90_dias(xs)
        buckets[tupla][b] = {"n_ask": len(xs), "eur_ask": round(sum(v for _, v in xs) / len(xs), 4),
                             "ic90_dias": ic, "dias": nd, "dias_pos": dp}
    salida = {"generado_utc": ahora.isoformat(timespec="seconds"), "desde": desde, "dias": DIAS,
              "n_senales": len(sen), "n_con_ask": n_ask, "marcos": sorted(DUR), "buckets": buckets}
    tj = OUT_JSON.with_suffix(".json.tmp")
    tj.write_text(json.dumps(salida, ensure_ascii=False), encoding="utf-8")
    tj.replace(OUT_JSON)
    print(f"señales {len(sen)}, con ask {n_ask} -> {OUT_CSV.name}, {OUT_JSON.name} ({len(agg)} buckets)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
