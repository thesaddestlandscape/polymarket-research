#!/usr/bin/env python3
"""reconstruir_wallet_mirror_executor_08_22sep.py -- (24-Sep, A2, Javi: "no admito que pierdas
datos... busca la manera"). Reconstruye las filas de wallet_mirror_executor_dryrun.csv perdidas
por el OOM del 23-Sep 06:01 (08-Sep .. 23-Sep 06:01) a partir de los backups del sniper.

Por qué es posible (medido 24-Sep sobre 262.106 filas reales del ejecutor):
  - detección ~ decisión en WM: 98,7 % de lo fillable en detección sigue fillable en decisión,
    ask idéntico (±0,005) en el 86,3 %, PnL a 1 EUR −0,027 vs −0,033 -> ask/ratio de detección
    del sniper sustituyen a los de decisión con error pequeño (marcado reconstruido=1).
  - qué filas escribía el ejecutor: todas las SEGUIR de las (wallet,activo,marco) que estaban en
    su roster EN ESE MOMENTO (cobertura por combo×hora bimodal 0 %/100 %). El roster se replica
    punto a punto con la MISMA lógica de wallet_mirror_tracker.wallets_operativas_recientes():
    últimas N_RECIENTE_OPERAR resoluciones ANTES de t (trade + duración del marco + 1 h de
    retraso de ballenas_observer) -> no degradada (Wilson hi >= hit_hist − margen) y Wilson lo > 50 %.
Lista validada = la versión horaria en git vigente en t (desde 11-Sep); antes, la más temprana
(columna lista_validada_aprox=1).
Modo --validar: compara la réplica con el ejecutor real en el solape 23-Sep 07:00 -> ahora.
Salida (modo normal): data/shadow/wallet_mirror_executor_dryrun_reconstruido_08_22sep.csv
(fichero APARTE, nunca se mezcla en el original sin decisión de Javi).
"""
import bisect
import csv
import glob
import gzip
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import wallet_mirror_tracker as T

REPO = Path(__file__).resolve().parent
BACKUPS = Path("/mnt/HC_Volume_106538179/backups_wallet_mirror_sniper_dry_run")
SNIPER_VIVO = REPO / "data/shadow/wallet_mirror_sniper_dry_run.csv"
EXEC = REPO / "data/shadow/wallet_mirror_executor_dryrun.csv"
OUT = REPO / "data/shadow/wallet_mirror_executor_dryrun_reconstruido_08_22sep.csv"
DESDE, HASTA = "2026-09-08", "2026-09-23T06:01:52"
DUR_S = {"5min": 300, "15min": 900, "60min": 3600, "240min": 14400, "weekly": 7 * 86400}
RETRASO_S = int(__import__("os").environ.get("RETRASO_S", "0"))   # validado 24-Sep contra el ejecutor real
csv.field_size_limit(10_000_000)


def ts(s):
    d = datetime.fromisoformat(s.replace("Z", "+00:00"))
    return (d if d.tzinfo else d.replace(tzinfo=timezone.utc)).timestamp()


def filas_sniper(desde, hasta):
    """Filas SEGUIR del sniper en [desde, hasta), dedup (wallet, tx_hash) sobre todas las fuentes."""
    fuentes = sorted(glob.glob(str(BACKUPS / "wallet_mirror_sniper_dry_run_*.csv.gz"))) + [str(SNIPER_VIVO)]
    vistos = set()
    for p in fuentes:
        with (gzip.open(p, "rt") if p.endswith(".gz") else open(p)) as f:
            for r in csv.DictReader(f):
                t = r.get("timestamp_utc") or ""
                if not (desde <= t < hasta) or r.get("tipo") != "SEGUIR":
                    continue
                k = ((r.get("wallet") or "").lower(), r.get("transaction_hash") or r.get("trade_timestamp"))
                if k in vistos:
                    continue
                vistos.add(k)
                yield r


def roster_en(t, clave, info, hist_ts, hist_ac):
    """Réplica punto a punto de wallets_operativas_recientes() para una clave."""
    w, activo, marco = clave
    xs = hist_ts.get((w, activo, marco, info["tipo"]))
    if not xs or info.get("hit") is None:
        return False
    corte = t - DUR_S.get(marco, 900) - RETRASO_S
    i = bisect.bisect_left(xs, corte)
    if i < T.N_RECIENTE_OPERAR:
        return False
    rec = hist_ac[(w, activo, marco, info["tipo"])][i - T.N_RECIENTE_OPERAR:i]
    k, n = sum(rec), len(rec)
    lo, hi = T.wilson_ci(k, n)
    if hi * 100 < info["hit"] * 100 - T.MARGEN_DEGRADACION_PP_OPERAR:
        return False
    kp = k if info["tipo"] == "SEGUIR" else n - k
    return T.wilson_ci(kp, n)[0] > 0.50


SCORES_REL = "data/shadow/wallet_edge_score_por_activo_marco.json"
TMP_SCORES = Path("/tmp") / "wm_scores_version.json"


def listas_validadas():
    """[(epoch, {clave: info})] -- una por versión horaria en git de la lista validada
    (desde 11-Sep; antes, squash del historial -> se usa la más temprana, marcado aprox)."""
    import subprocess
    vers = subprocess.run(["git", "-C", str(REPO), "log", "--format=%H %cI", "--", SCORES_REL],
                          capture_output=True, text=True, check=True).stdout.split("\n")
    out = []
    original = T.WALLET_SCORES
    try:
        for linea in reversed([v for v in vers if v.strip()]):
            h, fecha = linea.split()
            TMP_SCORES.write_bytes(subprocess.run(["git", "-C", str(REPO), "show", f"{h}:{SCORES_REL}"],
                                                  capture_output=True, check=True).stdout)
            T.WALLET_SCORES = TMP_SCORES
            out.append((ts(fecha), T.cargar_wallets_validadas()))
    finally:
        T.WALLET_SCORES = original
        TMP_SCORES.unlink(missing_ok=True)
    return out


def cand_en(t, listas, xs_listas):
    i = bisect.bisect_right(xs_listas, t) - 1
    return listas[max(i, 0)][1], i < 0


def preparar():
    listas = listas_validadas()
    wallets = {w for _, c in listas for w, _, _ in c}
    hist = T._historial_reciente_wallet_mirror(wallets)
    hist_ts, hist_ac = {}, {}
    for k, v in hist.items():
        v = sorted((ts(a), b) for a, b in v if a)
        hist_ts[k] = [a for a, _ in v]
        hist_ac[k] = [b for _, b in v]
    return listas, hist_ts, hist_ac


def validar():
    listas, hist_ts, hist_ac = preparar()
    xl = [x for x, _ in listas]
    desde = "2026-09-23T07:00"
    real = set()
    for r in csv.DictReader(open(EXEC)):
        if r["timestamp_utc"] >= desde:
            real.add(((r["wallet"] or "").lower(), r["trade_timestamp"][:19], r["market_slug"]))
    tp = fp = fn = 0
    vistos = set()
    for r in filas_sniper(desde, "2099"):
        w = (r["wallet"] or "").lower()
        clave = (w, r["activo"], r["marco"])
        k = (w, r["trade_timestamp"][:19], r["market_slug"])
        if k in vistos:
            continue
        vistos.add(k)
        info = cand_en(ts(r["timestamp_utc"]), listas, xl)[0].get(clave)
        pred = bool(info and info["tipo"] == "SEGUIR" and roster_en(ts(r["timestamp_utc"]), clave, info, hist_ts, hist_ac))
        esta = k in real
        tp += pred and esta
        fp += pred and not esta
        fn += (not pred) and esta
    print(f"validación solape {desde}->: réplica incluye {tp + fp}, real {len(real)}, "
          f"acierto (TP) {tp}, sobran (FP) {fp}, faltan (FN) {fn} | "
          f"precisión {tp / max(tp + fp, 1):.3f} cobertura {tp / max(tp + fn, 1):.3f}")


def generar():
    listas, hist_ts, hist_ac = preparar()
    xl = [x for x, _ in listas]
    campos = list(csv.DictReader(open(EXEC)).fieldnames) + ["reconstruido", "fuente_reconstruccion",
                                                            "lista_validada_aprox"]
    n = 0
    tmp = OUT.with_suffix(".csv.tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=campos)
        wr.writeheader()
        for r in filas_sniper(DESDE, HASTA):
            w = (r["wallet"] or "").lower()
            clave = (w, r["activo"], r["marco"])
            cand, aprox = cand_en(ts(r["timestamp_utc"]), listas, xl)
            info = cand.get(clave)
            if not info or info["tipo"] != "SEGUIR" or not roster_en(ts(r["timestamp_utc"]), clave, info, hist_ts, hist_ac):
                continue
            try:
                ratio = float(r["ratio_vs_stake_deteccion"])
            except (ValueError, TypeError):
                continue          # el ejecutor no escribía fila sin libro en detección
            ask = r.get("mejor_ask_deteccion", "")
            wr.writerow({
                "timestamp_utc": r["timestamp_utc"], "trade_timestamp": r["trade_timestamp"], "wallet": w,
                "tipo": "SEGUIR", "edge_pp_validado": r.get("edge_pp_validado", ""),
                "n_validado": r.get("n_validado", ""), "activo": r["activo"], "marco": r["marco"],
                "mirror_lado": r.get("mirror_lado", ""), "market_slug": r.get("market_slug", ""),
                "ratio_deteccion": ratio, "ask_deteccion": ask, "ratio_decision": ratio, "ask_decision": ask,
                "degradacion_ask_pct": 0.0, "sigue_fillable_en_decision": int(ratio >= 5),
                "outcome_real": r.get("outcome_real", ""), "acierto": r.get("acierto", ""),
                "resolved_ts": r.get("resolved_ts", ""),
                "tupla_sintetica": f"WALLET_MIRROR#{r['activo']}#{r['marco']}#BUY_{r.get('mirror_lado', '')}",
                "usd_trade": r.get("usd_trade", ""), "size_mediana_wallet": r.get("size_mediana_wallet", ""),
                "ratio_vs_mediana_propia": r.get("ratio_vs_mediana_propia", ""),
                "es_jugada_grande": r.get("es_jugada_grande", ""),
                "reconstruido": 1, "fuente_reconstruccion": "sniper_deteccion+roster_replicado",
                "lista_validada_aprox": int(aprox)})
            n += 1
    tmp.replace(OUT)
    print(f"{n} filas reconstruidas -> {OUT}")


if __name__ == "__main__":
    validar() if "--validar" in sys.argv else generar()
