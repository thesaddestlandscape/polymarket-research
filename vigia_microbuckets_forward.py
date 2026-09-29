#!/usr/bin/env python3
"""vigia_microbuckets_forward.py -- validación FORWARD (out-of-sample real) de
los micro-buckets con edge sostenido al ASK REAL (29-Sep, Javi: "hay
micro-buckets en gbm que dan positivo y llevan días sostenidos, revísalo").

Los 15 buckets que cumplen todo salvo BH-FDR en
analisis_microbuckets_ask_real_sostenidos.py se CONGELAN aquí
(data/shadow/microbuckets_watchlist.json, cutoff = momento de creación, NO se
reescribe sola). Se miran de 1066 buckets: por azar salen ~50 con p<0.05, así
que el histórico no basta -- solo cuentan señales POSTERIORES al cutoff
(ask real de ask_real_por_senal.csv, fee 7 %).
Veredicto por bucket (forward): confirmado si n>=20, >=5 días, EV>=+0.10 e IC90
por días lo>0; refutado si n>=20 y EV<=0; si no, sin_concluir.
Telegram SIEMPRE (informe de estado). Cron 08:50 UTC (tras ask_real 05:40).
"""
import json
import random
import statistics as st
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
WATCH = REPO / "data/shadow/microbuckets_watchlist.json"
FUENTE = REPO / "data/shadow/microbuckets_ask_real_sostenidos.json"
OUT = REPO / "data/shadow/microbuckets_forward.json"


def _congelar():
    d = json.loads(FUENTE.read_text(encoding="utf-8"))
    items = [{"tupla": c["tupla"], "bucket": c["bucket"], "n_hist": c["n"], "ev_hist": c["ev_eur"],
              "fill_libro_real": c.get("fill_libro_real")} for c in d["candidatas"] if c.get("base_sin_bh")]
    w = {"cutoff_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "items": items,
         "nota": "congelada, NO se reescribe; solo señales con prediction_timestamp > cutoff"}
    WATCH.write_text(json.dumps(w, ensure_ascii=False, indent=1), encoding="utf-8")
    return w


def _enviar(msg):
    print(msg)
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg, bot="cripto")
    except Exception as e:
        print(f"[vigia_microbuckets_forward] error Telegram: {e}")


def main():
    if WATCH.exists():
        w = json.loads(WATCH.read_text(encoding="utf-8"))
    elif FUENTE.exists():
        w = _congelar()
    else:
        _enviar("🧪 *Micro-buckets forward*: falta microbuckets ask real sostenidos (aún sin generar).")
        return
    cutoff = w["cutoff_utc"]
    import analisis_microbuckets_ask_real_sostenidos as M
    import csv
    import ask_real_por_senal as ARS
    from gate_bucket_propio import bucket
    sen = ARS.cargar_senales(cutoff[:10])
    idx = {(s["st"], s["mid"], s["dec"]): s for s in sen if s["pt"] > cutoff}
    want = {(i["tupla"], i["bucket"]) for i in w["items"]}
    por = defaultdict(lambda: defaultdict(list))
    with open(M.CSV_ASK, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if not r["ask"]:
                continue
            s = idx.get((r["strategy"], r["market_id"], r["decision"]))
            if not s:
                continue
            ask = float(r["ask"])
            if not 0.02 <= ask <= 0.98:
                continue
            t = f"{s['st']}#{s['act']}#{s['marco']}#{s['dec']}"
            b = f"{bucket(s['py']):.2f}"
            if (t, b) in want:
                dia = datetime.fromtimestamp(s["t"], timezone.utc).date().isoformat()
                por[(t, b)][dia].append(ARS.pnl(ask, s["ac"]))
    res, lin = [], []
    conf = ref = 0
    for i in w["items"]:
        d = por.get((i["tupla"], i["bucket"]), {})
        vals = [v for vs in d.values() for v in vs]
        n = len(vals)
        v = "sin_concluir"
        ev = st.mean(vals) if n else None
        lo = None
        if n >= 3 and len(d) >= 2:
            ds = list(d.values()); rng = random.Random(5)
            m = sorted(st.mean([x for _ in ds for x in rng.choice(ds)]) for _ in range(1000))
            lo = m[50]
        if n >= 20 and len(d) >= 5 and ev >= 0.10 and lo is not None and lo > 0:
            v = "confirmado_forward"; conf += 1
        elif n >= 20 and ev is not None and ev <= 0:
            v = "refutado_forward"; ref += 1
        res.append({**i, "n_fwd": n, "dias_fwd": len(d), "ev_fwd": None if ev is None else round(ev, 4),
                    "ic_lo_fwd": None if lo is None else round(lo, 4), "veredicto": v})
    OUT.write_text(json.dumps({"cutoff_utc": cutoff, "generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                               "items": res}, ensure_ascii=False, indent=1), encoding="utf-8")
    lin.append(f"🧪 *Micro-buckets sostenidos: validación FORWARD (ask real)* — desde {cutoff[:16]}Z")
    lin.append(f"Watchlist congelada: {len(res)} buckets (9 GBM). Confirmados {conf}, refutados {ref}, "
               f"sin concluir {len(res) - conf - ref}. Regla: n>=20, >=5 días, EV>=+0,10, IC90 lo>0.")
    for r in sorted(res, key=lambda x: -(x["n_fwd"] or 0))[:12]:
        ev = "n/d" if r["ev_fwd"] is None else f"{r['ev_fwd']:+.2f}"
        lin.append(f"· {r['tupla'].replace('GBM_LATE_15M_', 'GL15_').replace('_', ' ')} [{r['bucket']}] "
                   f"fwd n={r['n_fwd']} d={r['dias_fwd']} EV {ev} (hist {r['ev_hist']:+.2f}, fill {r['fill_libro_real']}) → {r['veredicto']}")
    _enviar("\n".join(lin))


if __name__ == "__main__":
    main()
