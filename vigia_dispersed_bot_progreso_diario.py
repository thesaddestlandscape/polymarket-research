#!/usr/bin/env python3
"""vigia_dispersed_bot_progreso_diario.py — Informe DIARIO explícito
(petición Javi, 07-Sep, mismo patrón que resolution_sniper_precierre_
depth_fase0.csv: "avísame diariamente... para ver qué podemos sacar a
live") del progreso del ejecutor DRY_RUN de la familia P-GALLINA
(dispersed_bot_executor_dryrun.py, hilo dentro de la screen
`ejecdryrun`) hacia una posible promoción real.

Distinto de vigia_bot_wallets_gate_bucket.py (que solo vigila el gate
ESTADÍSTICO, bot_wallets_gate_bucket.json, y avisa solo veredictos
NUEVOS): este vigía cruza ESE gate con la fill-ability REAL medida por
el propio ejecutor DRY_RUN (columnas sigue_fillable/decision_dry_run
de dispersed_bot_executor_dryrun.csv) -- el mismo cruce hecho a mano
07-Sep que confirmó SNIPER#BTC#5min[0.25,0.30) (n=301, shuffle_p=0.0,
split-half OK, PnL bootstrap CI90%=[0.098,0.411], g(f=10%)=+0.0177,
fill-ability real 56.7%, cruce ballenas +10.3pp sobre baseline,
concentración sana) como la candidata más sólida de la sesión.

SIEMPRE envía un mensaje (no solo si hay cambios) -- mismo criterio que
CLAUDE.md pt.20 para resolution_sniper_precierre_depth_fase0.csv:
"no basta con revisarlo, hay que reportarlo aunque no haya cambios".
Puramente informativo -- no toca prob_yes/stake/pares_permitidos_live,
dispersed_bot_executor_dryrun.py sigue DRY_RUN=True.
"""
import csv
import json
import math
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import shadow_postmortem as sp  # noqa: E402 -- reusa es_pre_twap

DRYRUN_CSV = REPO / "data/shadow/dispersed_bot_executor_dryrun.csv"
GATE_JSON = REPO / "data/shadow/bot_wallets_gate_bucket.json"
LATCH = REPO / "data/live/vigia_dispersed_bot_progreso_latch.json"

N_MIN_LIVE = 40          # mismo umbral que el resto del proyecto
FILLABILITY_MIN = 0.30   # mismo umbral que gate_bucket_propio._veto_fillable
RATIO_MIN = 5.0
FEE = 0.07
STEP = 0.05


def _bucket(p: float) -> float:
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def _leer_dryrun():
    """Cuenta filas y dispararia/total por (arquetipo,activo,marco,bucket).
    Single-pass, sin DictReader completo en memoria (284MB+ y creciendo)."""
    total = 0
    por_bucket = defaultdict(lambda: [0, 0])  # [n_total, n_dispararia]
    with open(DRYRUN_CSV, encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split(",")
        idx = {h: i for i, h in enumerate(header)}
        i_arq, i_act, i_mar, i_buc, i_dec = (
            idx["arquetipo"], idx["activo"], idx["marco"],
            idx["bucket_precio"], idx["decision_dry_run"],
        )
        i_ver = idx.get("gate_veredicto")
        for line in f:
            total += 1
            parts = line.rstrip("\n").split(",")
            if len(parts) <= max(i_arq, i_act, i_mar, i_buc, i_dec, i_ver or 0):
                continue
            if i_ver is not None and parts[i_ver] != "bueno_confirmado":
                continue
            clave = (parts[i_arq], parts[i_act], parts[i_mar], parts[i_buc])
            por_bucket[clave][0] += 1
            if parts[i_dec] == "DISPARARIA":
                por_bucket[clave][1] += 1
    return total, por_bucket


def _pnl_real_bucket(arquetipo, activo, marco, bucket_precio):
    """Recalcula n/hit/pnl real (results independiente del JSON, misma
    fuente que analisis_bot_wallets_gate_bucket_25ago.py) para el bucket
    exacto -- confirmación de segunda fuente antes de listar como
    candidato, no fiarse solo del veredicto ya cacheado en el JSON."""
    IN = REPO / "data/shadow/bot_wallets_gate_bucket_fase0.csv"
    if not IN.exists():
        return None
    pnls = []
    with open(IN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("arquetipo") != arquetipo or r.get("activo") != activo or r.get("marco") != marco:
                continue
            if not r.get("outcome_real"):
                continue
            ask_raw = r.get("mejor_ask_deteccion", "")
            if not ask_raw:
                continue
            try:
                ask = float(ask_raw)
            except (TypeError, ValueError):
                continue
            if not (0.0 < ask < 1.0):
                continue
            try:
                ratio = float(r.get("ratio_vs_stake_deteccion") or "nan")
            except (TypeError, ValueError):
                continue
            if ratio < RATIO_MIN:
                continue
            if sp.es_pre_twap(marco, r.get("timestamp_utc", "")):
                continue
            if _bucket(ask) != bucket_precio:
                continue
            acierto = 1 if r.get("outcome_real") == r.get("lado_wallet") else 0
            gross_win = (1 - ask) / ask
            pnls.append(gross_win * (1 - FEE) if acierto else -1.0)
    n = len(pnls)
    if n == 0:
        return None
    ev = sum(pnls) / n
    g = sum(math.log(1 + 0.10 * x) for x in pnls) / n
    return {"n": n, "ev": round(ev, 4), "g": round(g, 5)}


def main() -> int:
    from shadow_digest import enviar_telegram

    t0 = time.time()
    gate = json.loads(GATE_JSON.read_text(encoding="utf-8")) if GATE_JSON.exists() else {}
    total_filas, por_bucket = _leer_dryrun()
    dt = time.time() - t0

    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}
    filas_antes = previo.get("total_filas", 0)

    candidatos = []
    cerca = []
    for (arq, act, mar, buc_str), (n_tot, n_disp) in por_bucket.items():
        if n_tot < 30:
            continue
        fillability = n_disp / n_tot if n_tot else 0.0
        try:
            buc = float(buc_str)
        except ValueError:
            continue
        gate_key = f"{arq}#{act}#{mar}"
        gate_info = gate.get(gate_key, {}).get(buc_str, {})
        n_gate = gate_info.get("n", 0)
        if n_gate < N_MIN_LIVE:
            continue
        # 11-Sep (bug real encontrado al revisar SNIPER#BTC#15min[0.10,0.15)
        # a petición de Javi): faltaba exigir que el veredicto ACTUAL del
        # gate sea bueno_confirmado -- antes solo se exigía n_gate>=40, así
        # que un bucket que HOY es sin_concluir (split-half inconsistente,
        # veredicto en flip-flop día a día) seguía apareciendo en
        # "CANDIDATOS A REAL" mientras al menos una fila vieja del CSV
        # llevara la etiqueta bueno_confirmado histórica (gate_veredicto
        # por fila, congelada en el momento del log, usada solo para
        # aproximar fill-ability bajo gate activo). Esto rompía la
        # confianza del informe -- un candidato listado aquí debe estar
        # confirmado HOY, no solo haberlo estado alguna vez.
        if gate_info.get("veredicto") != "bueno_confirmado":
            continue
        item = {
            "tupla": f"{arq}#{act}#{mar}[{buc:.2f},{buc+STEP:.2f})",
            "n_gate": n_gate, "pnl_medio_gate": gate_info.get("pnl_medio"),
            "shuffle_p": gate_info.get("shuffle_p"),
            "n_dryrun": n_tot, "n_dispararia": n_disp, "fillability": round(100 * fillability, 1),
        }
        if fillability >= FILLABILITY_MIN and n_disp >= 30:
            real = _pnl_real_bucket(arq, act, mar, buc)
            item["verificacion_real"] = real
            candidatos.append(item)
        else:
            cerca.append(item)

    candidatos.sort(key=lambda x: -x["n_dispararia"])
    cerca.sort(key=lambda x: -x["n_dispararia"])

    lineas = [f"🎯 dispersed_bot_executor_dryrun: {total_filas:,} filas totales "
              f"(+{total_filas - filas_antes:,} desde el último informe), "
              f"leído en {dt:.1f}s"]
    if candidatos:
        lineas.append(f"\n✅ CANDIDATOS A REAL ({len(candidatos)}, fill-ability≥{FILLABILITY_MIN:.0%}, n_dispararia≥30):")
        for c in candidatos[:10]:
            v = c.get("verificacion_real")
            v_txt = (f" | verif.independiente: n={v['n']} EV/$={v['ev']:+.3f} g(f=10%)={v['g']:+.5f}"
                     if v else " | ⚠️ sin verificación independiente (n insuficiente en fuente 2)")
            lineas.append(
                f"  {c['tupla']}: gate n={c['n_gate']} pnl/tr={c['pnl_medio_gate']:+.3f} p={c['shuffle_p']} "
                f"| dry-run n={c['n_dryrun']} dispararia={c['n_dispararia']} ({c['fillability']}% fillable){v_txt}"
            )
    else:
        lineas.append("\n✅ CANDIDATOS A REAL: ninguno todavía (fill-ability<30% o n_dispararia<30 en todos)")

    if cerca:
        lineas.append(f"\n⏳ Cerca (bueno_confirmado pero fill-ability<{FILLABILITY_MIN:.0%} o n_dispararia<30), top 5 por volumen:")
        for c in cerca[:5]:
            lineas.append(f"  {c['tupla']}: n_dryrun={c['n_dryrun']} dispararia={c['n_dispararia']} ({c['fillability']}% fillable)")

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
        print(f"[vigia_dispersed_bot_progreso_diario] ERROR {type(e).__name__}: {e}")
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram(f"🔴 vigia_dispersed_bot_progreso_diario.py falló: {type(e).__name__}: {e}")
        except Exception:
            pass
        sys.exit(1)
