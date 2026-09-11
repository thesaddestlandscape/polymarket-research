#!/usr/bin/env python3
"""vigia_candidata9_executor_progreso_diario.py — 08-Sep, informe DIARIO
explícito (petición Javi, 08-Sep: "ve informandome dia a dia de como va
evolucionando para cuando podamos sacarla a live") del progreso del
ejecutor DRY_RUN de CANDIDATA9_BOT_CONSENSO (candidata9_bot_consenso_
executor.py, hilo dentro de la screen `ejeclive`) hacia una posible
promoción real.

Mismo patrón que vigia_dispersed_bot_progreso_diario.py (07-Sep): cruza
el gate ESTADÍSTICO retrospectivo (candidata9_10_gate_bucket.json,
regenerado por analisis_candidata9_10_gate_bucket_26ago.py / vigia_
candidata9_10_gate_bucket_26ago.py) con la fill-ability REAL medida por
el propio ejecutor (columnas sigue_fillable_en_decision/en_zona_
confirmada de candidata9_bot_consenso_executor.csv) -- un bucket puede
estar "bueno_confirmado" en el histórico y aun así no ser operable si
el libro real nunca deja fillable la señal en el instante de decisión
(mismo hueco que ya demostró ser real en dispersed_bot/wallet_mirror).

SIEMPRE envía un mensaje (no solo si hay cambios) -- mismo criterio que
CLAUDE.md pt.20 para resolution_sniper_precierre_depth_fase0.csv y
dispersed_bot_executor_dryrun.py: "no basta con revisarlo, hay que
reportarlo aunque no haya cambios". Puramente informativo -- no toca
prob_yes/stake/pares_permitidos_live, candidata9_bot_consenso_
executor.py sigue DRY_RUN=True.
"""
import csv
import json
import math
import sys
import time
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DRYRUN_CSV = REPO / "data/shadow/candidata9_bot_consenso_executor.csv"
GATE_JSON = REPO / "data/shadow/candidata9_10_gate_bucket.json"
LATCH = REPO / "data/live/vigia_candidata9_executor_progreso_latch.json"
BOTS_FASE0_CSV = REPO / "data/shadow/bot_wallets_gate_bucket_fase0.csv"

N_MIN_GATE = 40   # umbral estándar del proyecto para "concluyente" (no el N_MIN=15 del gate en sí)
FILLABILITY_MIN = 0.30  # mismo umbral que gate_bucket_propio._veto_fillable
FEE = 0.07
N_MIN_FORWARD_PNL = 10  # piso mínimo para que el pnl forward cuente como evidencia, no ruido de 1-2 filas
STEP = 0.05


def _bucket(p: float) -> str:
    return f"{math.floor(p / STEP + 1e-9) * STEP:.2f}"


def _pnl_neto(ask: float, acierto: int) -> float:
    gross_win = (1 - ask) / ask
    return gross_win * (1 - FEE) if acierto else -1.0


def _cargar_outcomes() -> dict:
    """condition_id -> outcome_real, desde bot_wallets_gate_bucket_fase0.csv
    (misma fuente que analisis_candidata9_10_gate_bucket_26ago.py usa para
    construir el gate). Fail-open a {} si falta: el caller trata "sin
    outcome" como "sin evidencia forward todavía", nunca como confirmación."""
    outcomes = {}
    if not BOTS_FASE0_CSV.exists():
        return outcomes
    with open(BOTS_FASE0_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            o = row.get("outcome_real")
            if o and row.get("condition_id") not in outcomes:
                outcomes[row["condition_id"]] = o
    return outcomes


def _leer_dryrun():
    """10-Sep (hallazgo real, ver feedback_gate_debe_usar_precio_decision_
    no_deteccion_10sep en memoria nativa): además de contar fillability,
    calcula el PnL forward del subconjunto que de verdad sería ejecutable
    (en_zona_confirmada=1 Y sigue_fillable_en_decision=1) usando ask_
    decision (el precio real, ~3s después del trigger) + outcome_real
    resuelto. Antes este vigía solo medía liquidez -- promocionó
    CANDIDATA9#ETH#5min[0.30,0.35) con fill-ability 87,5% sin comprobar
    que ese subconjunto ejecutable ganara dinero de verdad; resultó
    negativo (n=16, hit=25%, pnl-0,255€) pese al gate retrospectivo
    positivo (n=65, +0,645€) -- el gate se construye sobre el ask de
    DETECCIÓN, no el de decisión, sesgo optimista real."""
    total = 0
    # [n_total, n_en_zona, n_fillable_en_zona, n_pnl, suma_pnl, n_acierto]
    por_bucket = defaultdict(lambda: [0, 0, 0, 0, 0.0, 0])
    if not DRYRUN_CSV.exists():
        return 0, por_bucket, None, None
    outcomes = _cargar_outcomes()
    ts_min = ts_max = None
    with open(DRYRUN_CSV, encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            total += 1
            ts = row.get("timestamp_utc", "")
            if ts:
                ts_min = ts if ts_min is None else min(ts_min, ts)
                ts_max = ts if ts_max is None else max(ts_max, ts)
            try:
                ask = float(row.get("ask_decision") or "nan")
            except (TypeError, ValueError):
                continue
            if not (0.0 < ask < 1.0):
                continue
            clave = (row["activo"], row["marco"], _bucket(ask))
            por_bucket[clave][0] += 1
            if row.get("en_zona_confirmada") != "1":
                continue
            por_bucket[clave][1] += 1
            if row.get("sigue_fillable_en_decision") != "1":
                continue
            por_bucket[clave][2] += 1
            outcome = outcomes.get(row.get("condition_id", ""))
            if not outcome:
                continue  # aún no resuelto -- no cuenta como evidencia todavía
            acierto = 1 if row.get("lado_mayoria") == outcome else 0
            por_bucket[clave][3] += 1
            por_bucket[clave][4] += _pnl_neto(ask, acierto)
            por_bucket[clave][5] += acierto
    return total, por_bucket, ts_min, ts_max


def main() -> int:
    from shadow_digest import enviar_telegram

    t0 = time.time()
    gate = json.loads(GATE_JSON.read_text(encoding="utf-8")) if GATE_JSON.exists() else {}
    total_filas, por_bucket, ts_min, ts_max = _leer_dryrun()
    dt = time.time() - t0

    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}
    filas_antes = previo.get("total_filas", 0)

    candidatos = []
    cerca = []
    for (act, mar, buc_str), (n_tot, n_zona, n_fill, n_pnl, suma_pnl, n_acierto) in por_bucket.items():
        gate_key = f"CANDIDATA9_BOT_CONSENSO#{act}#{mar}"
        gate_info = gate.get(gate_key, {}).get(buc_str, {})
        if gate_info.get("veredicto") != "bueno_confirmado":
            continue
        n_gate = gate_info.get("n", 0)
        fillability = (n_fill / n_zona) if n_zona else 0.0
        pnl_forward = (suma_pnl / n_pnl) if n_pnl else None
        hit_forward = (n_acierto / n_pnl) if n_pnl else None
        item = {
            "tupla": f"{act}#{mar}[{buc_str},{float(buc_str)+STEP:.2f})",
            "n_gate": n_gate, "pnl_medio_gate": gate_info.get("pnl_medio"),
            "shuffle_p": gate_info.get("shuffle_p"),
            "n_dryrun_en_zona": n_zona, "n_fillable": n_fill,
            "fillability": round(100 * fillability, 1),
            "n_pnl_forward": n_pnl, "pnl_forward": pnl_forward, "hit_forward": hit_forward,
        }
        # 10-Sep: además de liquidez, exige que el subconjunto REALMENTE
        # ejecutable (ask de decisión + outcome resuelto) no salga
        # negativo con evidencia suficiente -- ver docstring de
        # _leer_dryrun(). Sin esto, un gate retrospectivo positivo con
        # buena liquidez podía promocionar un subconjunto forward
        # negativo (pasó de verdad con ETH#5min[0.30,0.35) el 10-Sep).
        pnl_forward_ok = pnl_forward is None or n_pnl < N_MIN_FORWARD_PNL or pnl_forward >= 0
        if n_gate < N_MIN_GATE:
            cerca.append(item)
        elif fillability >= FILLABILITY_MIN and n_zona >= 15 and pnl_forward_ok:
            candidatos.append(item)
        else:
            cerca.append(item)

    candidatos.sort(key=lambda x: -x["n_dryrun_en_zona"])
    cerca.sort(key=lambda x: -x["n_dryrun_en_zona"])

    rango = f" [{ts_min} → {ts_max}]" if ts_min else ""
    lineas = [f"🐣 candidata9_bot_consenso_executor: {total_filas:,} señales evaluadas"
              f" (+{total_filas - filas_antes:,} desde el último informe){rango}, leído en {dt:.1f}s"]

    def _fwd(c):
        if not c["n_pnl_forward"]:
            return "sin outcomes resueltos todavía"
        return f"pnl_forward={c['pnl_forward']:+.3f} hit_forward={c['hit_forward']:.1%} (n={c['n_pnl_forward']})"

    if candidatos:
        lineas.append(f"\n✅ CANDIDATOS A REAL ({len(candidatos)}, gate n≥{N_MIN_GATE}, "
                       f"fill-ability≥{FILLABILITY_MIN:.0%}, n_en_zona≥15, pnl_forward≥0 con n≥{N_MIN_FORWARD_PNL}):")
        for c in candidatos[:10]:
            lineas.append(
                f"  {c['tupla']}: gate n={c['n_gate']} pnl/tr={c['pnl_medio_gate']:+.3f} p={c['shuffle_p']} "
                f"| dry-run n_en_zona={c['n_dryrun_en_zona']} fillable={c['n_fillable']} ({c['fillability']}%) "
                f"| {_fwd(c)}"
            )
    else:
        lineas.append(f"\n✅ CANDIDATOS A REAL: ninguno todavía "
                       f"(gate n<{N_MIN_GATE}, o fill-ability<{FILLABILITY_MIN:.0%}, o n_en_zona<15, "
                       f"o pnl_forward<0 con n≥{N_MIN_FORWARD_PNL})")

    if cerca:
        lineas.append("\n⏳ Zonas bueno_confirmado en el gate retrospectivo, aún sin evidencia "
                       "propia suficiente del ejecutor, top 5 por volumen:")
        for c in cerca[:5]:
            lineas.append(
                f"  {c['tupla']}: gate n={c['n_gate']} pnl/tr={c['pnl_medio_gate']:+.3f} "
                f"| dry-run n_en_zona={c['n_dryrun_en_zona']} fillable={c['n_fillable']} ({c['fillability']}%) "
                f"| {_fwd(c)}"
            )

    msg = "\n".join(lineas)
    print(msg)
    enviar_telegram(msg, bot="cripto")

    LATCH.write_text(json.dumps({
        "total_filas": total_filas,
        "candidatos": [c["tupla"] for c in candidatos],
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_candidata9_executor_progreso_diario] ERROR {type(e).__name__}: {e}")
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram(f"🔴 vigia_candidata9_executor_progreso_diario.py falló: {type(e).__name__}: {e}")
        except Exception:
            pass
        sys.exit(1)
