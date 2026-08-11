#!/usr/bin/env python3
"""vigia_p31_wallets_forward.py — Validación FORWARD (out-of-sample real)
de la watchlist de wallets P31 (idea_p31_fade_wallets_sistematicamente_
malas_11ago): fade/follow sistemático de wallets con edge probado,
ampliado a las 6 monedas y 5 marcos.

Por qué existe: el gate "pooled" del 11-Ago (analisis_p31_gate_pooled_
todos_combos_11ago.py) es PARCIALMENTE CIRCULAR -- las wallets se
seleccionaron por tener edge significativo + split-half consistente
sobre datos hasta el 11-Ago, y el pooled-test corre sobre esos MISMOS
datos. La única prueba real es forward: ¿siguen prediciendo con los
trades que hagan ESTAS MISMAS wallets a partir de AHORA?

`data/shadow/p31_wallets_watchlist.json` (generado UNA VEZ por
generar_p31_watchlist_11ago.py, NO se reescribe solo -- ampliar la lista
de wallets es decisión explícita nueva, para no mover la portería) fija
`cutoff_utc` y la lista de wallets por combo (activo,marco,lado). Este
vigía:
1. Lee SOLO filas de ballenas_timing_history.csv con ts_trade > cutoff_utc
   (la fuente ya se captura sola vía ballenas_observer.py, cron horario --
   no hace falta ningún capturador nuevo).
2. Excluye régimen pre-TWAP igual que el resto del pipeline (defensivo --
   el cutoff ya es post-TWAP, pero si el mecanismo de resolución cambia
   otra vez en el futuro, esta guardia sigue protegiendo sin tocar código).
3. Aplica el mismo gate riguroso (Wilson90lo + breakeven fee 7% +
   shuffle) en cuanto el combo cruza n>=15 forward -- mismo suelo de
   rigor que el resto del proyecto.
4. Persiste veredicto en data/shadow/p31_forward_validacion.json y avisa
   por Telegram SOLO veredictos NUEVOS (latch, mismo patrón que
   vigia_gate_bucket_propio.py) -- confirmado o refutado, no cada corrida.

Puramente observacional: no ejecuta nada, no toca dinero, no escribe en
config_live.json ni pares_permitidos_live. Cron horario (mismo cadencia
que wallet_edge_tracker.py, que ya lee el mismo CSV cada hora -- no añade
categoría nueva de carga).
"""
import csv
import json
import math
import sys
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from shadow_digest import enviar_telegram
from shadow_postmortem import es_pre_twap

WATCHLIST = REPO / "data/shadow/p31_wallets_watchlist.json"
HIST = REPO / "data/shadow/ballenas_timing_history.csv"
OUT = REPO / "data/shadow/p31_forward_validacion.json"
LATCH = REPO / "data/live/vigia_p31_wallets_forward_latch.json"

FEE = 0.07
Z_90 = 1.645
N_MIN = 15
MARCO_LARGO = {"5m": "5min", "15m": "15min", "60m": "60min", "240m": "240min"}


def wilson_lower(hits: int, n: int, z: float = Z_90) -> float:
    if n == 0:
        return 0.0
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - margen) / denom


def breakeven(p_held: float) -> float:
    p_held = min(max(p_held, 1e-6), 1 - 1e-6)
    gross_win = (1 - p_held) / p_held
    return 1 / (1 + gross_win * (1 - FEE))


def cargar_forward(watchlist: dict) -> dict:
    """Una pasada por el CSV -- acumula filas forward por combo."""
    cutoff = watchlist["cutoff_utc"]
    wallet_a_combos = {}
    for combo_id, info in watchlist["combos"].items():
        for w in info["wallets"]:
            wallet_a_combos.setdefault(w, []).append(combo_id)

    filas_por_combo = {k: [] for k in watchlist["combos"]}
    with open(HIST, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            w = row.get("wallet")
            combos_wallet = wallet_a_combos.get(w)
            if not combos_wallet:
                continue
            ts = row.get("ts_trade", "")
            if ts <= cutoff:
                continue  # solo forward, out-of-sample real
            try:
                precio_chk = float(row.get("precio", ""))
            except (TypeError, ValueError):
                continue
            if not (0.0 < precio_chk < 1.0):
                continue  # mismo guard que wallet_edge_tracker.py -- precio 0/1 rompe breakeven/shuffle
            activo = row.get("activo")
            marco = row.get("marco")
            marco_largo = MARCO_LARGO.get(marco, marco)
            if es_pre_twap(marco_largo, ts):
                continue  # defensivo, ver docstring
            for combo_id in combos_wallet:
                info = watchlist["combos"][combo_id]
                if info["activo"] == activo and info["marco"] == marco:
                    filas_por_combo[combo_id].append(row)
    return filas_por_combo


def evaluar_combo(lado: str, rows: list) -> dict:
    n = len(rows)
    if n == 0:
        return {"n": 0, "veredicto": "sin_datos"}
    if lado == "fade":
        hits = sum(1 for r in rows if r.get("acierto") not in ("1", "True", "true"))
        p_sum = sum(1 - float(r["precio"]) for r in rows)
    else:
        hits = sum(1 for r in rows if r.get("acierto") in ("1", "True", "true"))
        p_sum = sum(float(r["precio"]) for r in rows)
    hit = hits / n
    p_medio = p_sum / n
    resultado = {
        "n": n, "hit": round(hit, 4), "precio_medio": round(p_medio, 4),
    }
    if n < N_MIN:
        resultado["veredicto"] = "sin_concluir"
        return resultado

    be = breakeven(p_medio)
    wl = wilson_lower(hits, n)
    rng = np.random.default_rng(hits * 1000003 + n)
    sim = rng.binomial(n, p_medio, size=10000) / n
    p_shuffle = float(np.mean(np.abs(sim - p_medio) >= abs(hit - p_medio)))
    margen = (wl - be) * 100

    resultado.update({
        "breakeven": round(be, 4), "wilson90lo": round(wl, 4),
        "margen_pp": round(margen, 2), "p_shuffle": p_shuffle,
    })
    if margen > 0 and p_shuffle < 0.05:
        resultado["veredicto"] = "confirmado_forward"
    elif margen < 0 and p_shuffle < 0.05:
        resultado["veredicto"] = "refutado_forward"
    else:
        resultado["veredicto"] = "sin_concluir"
    return resultado


def main() -> int:
    if not WATCHLIST.exists():
        print("No hay watchlist P31 -- nada que vigilar.")
        return 0
    watchlist = json.loads(WATCHLIST.read_text(encoding="utf-8"))

    try:
        previo = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    except Exception:
        previo = {}

    filas_por_combo = cargar_forward(watchlist)

    nuevo = {}
    avisos = []
    for combo_id, info in watchlist["combos"].items():
        rows = filas_por_combo[combo_id]
        r = evaluar_combo(info["lado"], rows)
        r["activo"] = info["activo"]
        r["marco"] = info["marco"]
        r["lado"] = info["lado"]
        r["n_wallets"] = info["n_wallets"]
        nuevo[combo_id] = r

        veredicto_antes = previo.get(combo_id, {}).get("veredicto", "sin_concluir")
        veredicto_ahora = r["veredicto"]
        if veredicto_ahora in ("confirmado_forward", "refutado_forward") and veredicto_ahora != veredicto_antes:
            emoji = "✅🟢" if veredicto_ahora == "confirmado_forward" else "❌🔴"
            avisos.append(
                f"{emoji} P31 {combo_id}: {veredicto_ahora} forward "
                f"(n={r['n']} hit={r['hit']:.3f} margen={r.get('margen_pp', 0):+.2f}pp "
                f"p={r.get('p_shuffle', 1):.4f})"
            )

    OUT.write_text(json.dumps(nuevo, indent=1))

    n_con_datos = sum(1 for r in nuevo.values() if r["n"] > 0)
    n_concluidos = sum(1 for r in nuevo.values() if r["veredicto"] in ("confirmado_forward", "refutado_forward"))
    print(f"[vigia_p31] {n_con_datos}/{len(nuevo)} combos con datos forward, "
          f"{n_concluidos} concluidos (confirmado/refutado)")
    for combo_id, r in sorted(nuevo.items(), key=lambda kv: -kv[1]["n"]):
        print(f"  {combo_id}: n={r['n']} veredicto={r['veredicto']}")

    if avisos:
        try:
            latch = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
        except Exception:
            latch = {}
        texto = "🔬 *P31 -- validación forward de wallets (fade/follow)*\n\n" + "\n".join(avisos)
        ok = enviar_telegram(texto)
        latch.update({combo_id: nuevo[combo_id]["veredicto"]
                      for combo_id in watchlist["combos"]
                      if nuevo[combo_id]["veredicto"] in ("confirmado_forward", "refutado_forward")})
        latch["_telegram_ok"] = ok
        LATCH.write_text(json.dumps(latch, indent=1))

    return 0


if __name__ == "__main__":
    sys.exit(main())
