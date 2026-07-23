#!/usr/bin/env python3
"""
analisis_diario_franja_15min.py -- mecanismo diario (petición explícita
Javi, 23-Jul: "conviértelo") del cruce por moneda + franja milimétrica +
timing + TODO lo que tenemos de ballenas para el marco 15min, mismo
espíritu que analisis_diario_ballenas_ejecutor.py (5min) pero sin
ejecutor propio -- aquí "nuestro propio" es el agregado de TODAS las
estrategias BUY_YES #15min en results.csv, no un dry_run.csv dedicado
(no existe un ballenas_executor_15min genérico, solo BTC15m que ya opera
con dinero real).

Por cada (activo, bucket 0.05), TODOS los buckets (no solo los
"significativos" -- Javi pidió verlo desagregado del todo, incluidos los
huecos):
  1. BALLENAS histórico completo (ballenas_timing_history.csv vía
     cargar_ballenas(), mismo import que analisis_franja_milimetrica_
     ballenas.py -- no reimplementar).
  2. BALLENAS live-fino con timing (ballenas_timing_state_fino.json) --
     rest_mediana_min, top1_share.
  3. NUESTRO propio (results.csv, agregado de todas las estrategias
     BUY_YES #15min de esa moneda) -- n, hit, pnl/trade.

Además, franja MACRO (bandas anchas de ballenas_timing_state.json) por
moneda -- para vigilar si aparece edge temprano (antes de la banda
operativa) que hoy no existe, y snapshot de wallets especialistas
marco=15m (wallet_edge_score_por_activo_marco.json).

Solo lectura/reporte. No decide ni conecta nada a ejecutores.
Cron sugerido: diario, después de wallet_edge_tracker.py.
"""
import csv
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_franja_milimetrica_ballenas import cargar_ballenas, bucket, STEP  # noqa: E402

DIR = Path(__file__).resolve().parent
DIR_SHADOW = DIR / "data" / "shadow"
RESULTS = DIR_SHADOW / "results.csv"
STATE_MACRO = DIR_SHADOW / "ballenas_timing_state.json"
STATE_FINO = DIR_SHADOW / "ballenas_timing_state_fino.json"
WALLET_EDGE_ACTIVO_MARCO = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
OUT = DIR_SHADOW / "analisis_diario_franja_15min.json"

ACTIVOS = ("BTC", "ETH", "SOL", "XRP", "DOGE")
MARCO_R = "15min"
MARCO_B = "15m"


def cargar_propio():
    propio = defaultdict(lambda: defaultdict(lambda: [0, 0, 0.0]))
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["decision"] != "BUY_YES":
                continue
            sub = row.get("subtype") or ""
            if "#" not in sub:
                continue
            activo, marco = sub.split("#", 1)
            if activo not in ACTIVOS or marco != MARCO_R:
                continue
            if row.get("acierto") not in ("0", "1"):
                continue
            try:
                p = float(row["precio_yes_mercado"])
                pnl = float(row.get("pnl_neto") or 0)
            except (TypeError, ValueError):
                continue
            d = propio[activo][bucket(p)]
            d[0] += 1
            d[1] += int(row["acierto"])
            d[2] += pnl
    return propio


def top_wallets_por_activo(activo, wallet_edge_db, top_n=10):
    candidatas = [v for v in wallet_edge_db.values()
                  if v.get("activo") == activo and v.get("marco") == MARCO_B and v.get("sig_bhfdr")]
    candidatas.sort(key=lambda v: v["edge_pp"], reverse=True)
    return candidatas[:top_n]


def main():
    ahora = datetime.now(timezone.utc)
    print(f"[analisis_diario_franja_15min] {ahora.isoformat(timespec='seconds')}")

    ballenas_hist = cargar_ballenas()
    try:
        state_macro = json.loads(STATE_MACRO.read_text())
    except Exception:
        state_macro = {}
    try:
        state_fino = json.loads(STATE_FINO.read_text())
    except Exception:
        state_fino = {}
    propio = cargar_propio()
    try:
        wallet_edge_db = json.loads(WALLET_EDGE_ACTIVO_MARCO.read_text())
    except Exception:
        wallet_edge_db = {}

    salida = {"actualizado": ahora.isoformat(timespec="seconds"), "activos": {}}

    for act in ACTIVOS:
        macro_info = state_macro.get(f"{act}#{MARCO_B}", {})
        banda_lo, banda_hi = macro_info.get("banda_lo"), macro_info.get("banda_hi")
        top_wallets = top_wallets_por_activo(act, wallet_edge_db)

        hist_b = ballenas_hist.get((act, MARCO_B), {})
        fino_b = {round(b["banda_lo"], 2): b for b in state_fino.get(f"{act}#{MARCO_B}", {}).get("bandas_significativas", [])}
        propio_b = propio.get(act, {})
        todos_buckets = sorted(set(round(k, 2) for k in hist_b) | set(fino_b) | set(propio_b))

        filas = []
        for bk in todos_buckets:
            hd = hist_b.get(bk, [0, 0, None])
            fb = fino_b.get(bk)
            pd_ = propio_b.get(bk, [0, 0, 0.0])
            filas.append({
                "bucket_lo": bk, "bucket_hi": round(bk + STEP, 2),
                "hist_n": hd[1], "hist_hit": round(hd[0] / hd[1], 4) if hd[1] else None,
                "live_fino_n": fb["n"] if fb else 0,
                "live_fino_hit": round(fb["hit"], 4) if fb else None,
                "live_fino_rest_mediana_min": round(fb["rest_mediana_min"], 3) if fb else None,
                "live_fino_top1_share": round(fb["top1_share"], 4) if fb else None,
                "propio_n": pd_[0],
                "propio_hit": round(pd_[1] / pd_[0], 4) if pd_[0] else None,
                "propio_pnl_trade": round(pd_[2] / pd_[0], 4) if pd_[0] else None,
            })

        salida["activos"][act] = {
            "banda_operativa": [banda_lo, banda_hi] if banda_lo is not None else None,
            "franja_fina": filas,
            "top_wallets_validadas": top_wallets,
        }

        print(f"\n=== {act}#15min === banda_operativa=[{banda_lo},{banda_hi})")
        n_propio_total = sum(f["propio_n"] for f in filas)
        print(f"  nuestro n_total 15min: {n_propio_total}")
        if top_wallets:
            print(f"  top wallets validadas: {len(top_wallets)}")
            for w in top_wallets[:3]:
                print(f"    {w['wallet'][:12]}... n={w['n']} hit={w['hit']} edge_pp={w['edge_pp']:+.1f}")

    OUT.write_text(json.dumps(salida, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nescrito {OUT}")


if __name__ == "__main__":
    main()
