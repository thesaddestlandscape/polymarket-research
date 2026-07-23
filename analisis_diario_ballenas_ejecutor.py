#!/usr/bin/env python3
"""
analisis_diario_ballenas_ejecutor.py -- mecanismo diario (petición explícita
Javi, 23-Jul: "quiero que hagas este análisis diariamente... este tiene que
ser el mecanismo para ir en la dirección correcta") que reproduce, para cada
activo con ejecutor de ballenas propio, el cruce que se hizo a mano en la
sesión de franja milimétrica de ballenas_executor_5min:

  1. Franja fina (bucket 0.05) por activo, cruzando 4 fuentes: histórico
     completo (ballenas_timing_history.csv), observer LIVE fino con timing
     (ballenas_timing_state_fino.json), y nuestro propio ejecutor
     (ballenas_5min_dry_run.csv) -- mismo patrón que
     analisis_franja_milimetrica_ballenas.py pero centrado en el propio
     ejecutor en vez de en resultados de results.csv/shadow_predict.
  2. Timing: relación entre restante_s (segundos antes del cierre al
     disparar) y acierto/pnl de nuestras propias señales -- el ángulo que
     motivó el fix de calibración dinámica en ballenas_executor_5min.py
     (cargar_calibracion/MARGEN_CONFIRM_S, 23-Jul).
  3. Wallets top por (activo,5m) desde wallet_edge_score_por_activo_marco.json
     (wallet_edge_tracker.py, extendido 23-Jul) -- candidatas con edge_pp
     validado (shuffle+BH-FDR) para vigilar si se consolidan.
  4. Sanity check de calibración: compara banda_lo/hi y n de la banda
     operativa de HOY contra la de la última corrida guardada -- alerta
     (solo en el log, no Telegram) si una banda se ha movido, para que la
     desalineación tipo "XRP prob_bucket congelado en 0.83 desde 18-Jul"
     nunca vuelva a pasar desapercibida (aunque ahora sea dinámica, sirve
     de auditoría de que sigue moviéndose de forma razonable).

Solo lectura, no decide ni ejecuta nada. Salida:
  data/shadow/analisis_diario_ballenas_ejecutor.json (snapshot del día)
  log a stdout (cron lo redirige a logs/analisis_diario_ballenas_ejecutor.log)

Cron sugerido: una vez al día (ver crontab -- 6:40 UTC, después de que
ballenas_observer.py y wallet_edge_tracker.py hayan corrido varias veces).
"""
import csv
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_franja_milimetrica_ballenas import bucket  # noqa: E402 -- misma función bucket(), no reimplementar

DIR = Path(__file__).resolve().parent
DIR_SHADOW = DIR / "data" / "shadow"
TIMING_HIST = DIR_SHADOW / "ballenas_timing_history.csv"
STATE_FINO = DIR_SHADOW / "ballenas_timing_state_fino.json"
STATE_MACRO = DIR_SHADOW / "ballenas_timing_state.json"
DRY_RUN_5M = DIR_SHADOW / "ballenas_5min_dry_run.csv"
WALLET_EDGE_ACTIVO_MARCO = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
OUT = DIR_SHADOW / "analisis_diario_ballenas_ejecutor.json"

STAKE_REF = 1.05
FEE_RATE = 0.07
ACTIVOS_5MIN = ("ETH", "SOL", "XRP", "DOGE")  # BTC#5m no tiene ejecutor propio (excluido 18-Jul, n insuficiente)


def _pnl(py: float, acierto: int) -> float:
    fee = STAKE_REF * FEE_RATE * (1 - py)
    return (STAKE_REF * (1.0 / py - 1.0) - fee) if acierto else (-STAKE_REF - fee)


def cargar_ballenas_historico_5m():
    """(activo) -> bucket -> [aciertos, n]. Solo marco=5m."""
    out = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    with open(TIMING_HIST, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("marco") != "5m" or row.get("activo") not in ACTIVOS_5MIN:
                continue
            try:
                p = float(row["precio"])
                acierto = int(row["acierto"])
            except (TypeError, ValueError):
                continue
            d = out[row["activo"]][bucket(p)]
            d[0] += acierto
            d[1] += 1
    return out


def cargar_dry_run():
    filas = defaultdict(list)
    if not DRY_RUN_5M.exists():
        return filas
    with open(DRY_RUN_5M, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") in (None, ""):
                continue
            try:
                py = float(row["py"])
                acierto = int(row["acierto"])
                restante_s = float(row["restante_s"])
            except (TypeError, ValueError):
                continue
            row["_py"] = py
            row["_acierto"] = acierto
            row["_restante_s"] = restante_s
            row["_pnl"] = _pnl(py, acierto)
            row["_bucket"] = bucket(py)
            filas[row["activo"]].append(row)
    return filas


def franja_fina_por_activo(activo, ballenas_hist, state_fino, dry_run_filas):
    fino = state_fino.get(f"{activo}#5m", {}).get("bandas_significativas", [])
    fino_by_bucket = {round(b["banda_lo"], 2): b for b in fino}
    hist_by_bucket = ballenas_hist.get(activo, {})
    propio_by_bucket = defaultdict(list)
    for row in dry_run_filas.get(activo, []):
        propio_by_bucket[row["_bucket"]].append(row)

    todos_buckets = sorted(set(hist_by_bucket) | set(fino_by_bucket) | set(propio_by_bucket))
    filas = []
    for bk in todos_buckets:
        hd = hist_by_bucket.get(bk, [0, 0])
        fb = fino_by_bucket.get(bk)
        pf = propio_by_bucket.get(bk, [])
        fila = {
            "bucket_lo": bk, "bucket_hi": round(bk + 0.05, 2),
            "hist_n": hd[1], "hist_hit": round(hd[0] / hd[1], 4) if hd[1] else None,
            "live_fino_n": fb["n"] if fb else 0,
            "live_fino_hit": round(fb["hit"], 4) if fb else None,
            "live_fino_rest_mediana_min": round(fb["rest_mediana_min"], 3) if fb else None,
            "live_fino_top1_share": round(fb["top1_share"], 4) if fb else None,
            "propio_n": len(pf),
            "propio_hit": round(sum(r["_acierto"] for r in pf) / len(pf), 4) if pf else None,
            "propio_pnl_trade": round(sum(r["_pnl"] for r in pf) / len(pf), 4) if pf else None,
        }
        filas.append(fila)
    return filas


def timing_por_activo(dry_run_filas_activo):
    """restante_s (segundos antes del cierre al disparar) vs acierto/pnl --
    NO decide nada aquí (ballenas_executor_5min.py ya usa confirm_ceiling_s
    dinámico, ver cargar_calibracion), esto es solo vigilancia de que la
    relación sigue el patrón esperado (disparar más tarde = mejor) conforme
    crece la n propia."""
    cortes = [(0, 30), (30, 60), (60, 90), (90, 999999)]
    filas = []
    for lo, hi in cortes:
        sub = [r for r in dry_run_filas_activo if lo <= r["_restante_s"] < hi]
        n = len(sub)
        filas.append({
            "restante_s_lo": lo, "restante_s_hi": (hi if hi < 999999 else None),
            "n": n,
            "hit": round(sum(r["_acierto"] for r in sub) / n, 4) if n else None,
            "pnl_trade": round(sum(r["_pnl"] for r in sub) / n, 4) if n else None,
        })
    return filas


def top_wallets_por_activo(activo, wallet_edge_db, top_n=10):
    candidatas = [v for v in wallet_edge_db.values()
                  if v.get("activo") == activo and v.get("marco") == "5m" and v.get("sig_bhfdr")]
    candidatas.sort(key=lambda v: v["edge_pp"], reverse=True)
    return candidatas[:top_n]


def calibracion_actual(activo):
    """Snapshot de la banda operativa actual -- para detectar movimientos
    día a día en el log (auditoría, no alerta Telegram)."""
    try:
        estado = json.loads(STATE_MACRO.read_text())
    except Exception:
        return None
    e = estado.get(f"{activo}#5m", {})
    if not e.get("significativo"):
        return None
    return {"banda_lo": e.get("banda_lo"), "banda_hi": e.get("banda_hi"),
            "n": e.get("n"), "hit": None if e.get("n_ganadoras") is None or not e.get("n")
            else round(e["n_ganadoras"] / e["n"], 4),
            "rest_hi_min": e.get("rest_hi_min")}


def main():
    ahora = datetime.now(timezone.utc)
    print(f"[analisis_diario_ballenas_ejecutor] {ahora.isoformat(timespec='seconds')}")

    anterior = {}
    if OUT.exists():
        try:
            anterior = json.loads(OUT.read_text())
        except Exception:
            anterior = {}

    ballenas_hist = cargar_ballenas_historico_5m()
    try:
        state_fino = json.loads(STATE_FINO.read_text())
    except Exception:
        state_fino = {}
    dry_run_filas = cargar_dry_run()
    try:
        wallet_edge_db = json.loads(WALLET_EDGE_ACTIVO_MARCO.read_text())
    except Exception:
        wallet_edge_db = {}

    salida = {"actualizado": ahora.isoformat(timespec="seconds"), "activos": {}}

    for activo in ACTIVOS_5MIN:
        franja = franja_fina_por_activo(activo, ballenas_hist, state_fino, dry_run_filas)
        timing = timing_por_activo(dry_run_filas.get(activo, []))
        top_wallets = top_wallets_por_activo(activo, wallet_edge_db)
        calib = calibracion_actual(activo)

        n_propio_total = sum(f["propio_n"] for f in franja)
        hit_propio_total = None
        if n_propio_total:
            aciertos = sum((f["propio_hit"] or 0) * f["propio_n"] for f in franja)
            hit_propio_total = round(aciertos / n_propio_total, 4)

        salida["activos"][activo] = {
            "franja_fina": franja,
            "timing": timing,
            "top_wallets_validadas": top_wallets,
            "calibracion_actual": calib,
            "n_propio_total": n_propio_total,
            "hit_propio_total": hit_propio_total,
        }

        print(f"\n=== {activo}#5min ===")
        if calib:
            print(f"  banda operativa: [{calib['banda_lo']:.2f},{calib['banda_hi']:.2f}) "
                  f"n={calib['n']} hit={calib['hit']}")
            calib_prev = (anterior.get("activos", {}).get(activo, {}) or {}).get("calibracion_actual")
            if calib_prev and (calib_prev.get("banda_lo") != calib["banda_lo"]
                                or calib_prev.get("banda_hi") != calib["banda_hi"]):
                print(f"  ⚠️  la banda operativa CAMBIÓ desde la corrida anterior: "
                      f"[{calib_prev.get('banda_lo')},{calib_prev.get('banda_hi')}) -> "
                      f"[{calib['banda_lo']},{calib['banda_hi']})")
        else:
            print("  banda operativa: NO significativa hoy")
        print(f"  nuestro ejecutor: n_total={n_propio_total} hit_total={hit_propio_total}")
        for t in timing:
            if t["n"]:
                hi_txt = t['restante_s_hi'] if t['restante_s_hi'] is not None else '+'
                print(f"    restante[{t['restante_s_lo']}-{hi_txt}s): n={t['n']} hit={t['hit']} pnl/trade={t['pnl_trade']}")
        if top_wallets:
            print(f"  top wallets validadas (sig_bhfdr): {len(top_wallets)}")
            for w in top_wallets[:3]:
                print(f"    {w['wallet'][:12]}... n={w['n']} hit={w['hit']} edge_pp={w['edge_pp']:+.1f} precio_medio={w['precio_medio']}")

    OUT.write_text(json.dumps(salida, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nescrito {OUT}")


if __name__ == "__main__":
    main()
