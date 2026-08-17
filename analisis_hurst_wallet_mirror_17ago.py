#!/usr/bin/env python3
"""
analisis_hurst_wallet_mirror_17ago.py — extensión del hallazgo de régimen
de Hurst a WALLET_MIRROR (petición Javi 17-Ago: probar Hurst en una
familia con fill-ability REAL, no en GBM_LATE/arquetipo A donde ya se
refutó por selección adversa, ver
idea_hurst_regimen_gbmlate_reversion_gana_17ago).

WALLET_MIRROR (P24) espeja wallets reales con edge ya validado -- su
cuello de botella nunca fue "¿va a haber profundidad?" (el fade/P2 no le
aplican, es un mecanismo distinto), sino precio de entrada (ver
idea_walletmirror_eth15min_zona_ask050_065_17ago). Si el régimen de
mercado (tendencia/reversión) correlaciona con cuándo las wallets
mirroreadas tienen más edge, sería una pieza nueva, no una repetición del
patrón ya refutado.

Reusa EXACTAMENTE el join validado en analisis_wallet_mirror_gate_bucket_10ago.py:
ask real (wallet_mirror_executor_dryrun.csv, filtrado a
sigue_fillable_en_decision=1) + outcome real (wallet_mirror_sniper_dry_run.csv)
+ filtro TWAP (shadow_postmortem.es_pre_twap). Solo lectura.
"""
import csv
import glob
import math
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(DIR))
import shadow_postmortem as sp  # noqa: E402

PRICES_GLOB = str(DIR / "data" / "prices" / "2026-*.csv")
EXECUTOR = DIR / "data" / "shadow" / "wallet_mirror_executor_dryrun.csv"
SNIPER = DIR / "data" / "shadow" / "wallet_mirror_sniper_dry_run.csv"
OUT_PATH = DIR / "data" / "shadow" / "hurst_wallet_mirror_analisis.json"

ACTIVOS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")
VENTANA_MIN = 60
PASO_MIN = 15
FEE = 0.07


def _hurst_rs(rets):
    n = len(rets)
    if n < 20:
        return None
    media = sum(rets) / n
    acc = 0.0
    desv_acum = []
    for r in rets:
        acc += (r - media)
        desv_acum.append(acc)
    rango = max(desv_acum) - min(desv_acum)
    var = sum((r - media) ** 2 for r in rets) / n
    s = math.sqrt(var)
    if s <= 0 or rango <= 0:
        return None
    try:
        return math.log(rango / s) / math.log(n)
    except (ValueError, ZeroDivisionError):
        return None


def _cargar_klines():
    series = defaultdict(list)
    for fp in sorted(glob.glob(PRICES_GLOB)):
        if "chainlink" in fp:
            continue
        with open(fp, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                activo = row.get("asset")
                if activo not in ACTIVOS:
                    continue
                try:
                    ts = datetime.fromisoformat(row["timestamp_utc"]).timestamp()
                    price = float(row["price_usd"])
                except (ValueError, KeyError, TypeError):
                    continue
                if price > 0:
                    series[activo].append((ts, price))
    for a in series:
        series[a].sort(key=lambda x: x[0])
    return series


def _hurst_rodante(serie, ventana_min):
    if not serie:
        return []
    ts0, ts_fin = serie[0][0], serie[-1][0]
    out = []
    j = 0
    t = ts0 + ventana_min * 60
    while t <= ts_fin:
        t_lo = t - ventana_min * 60
        while j < len(serie) and serie[j][0] < t_lo:
            j += 1
        i_fin = j
        while i_fin < len(serie) and serie[i_fin][0] <= t:
            i_fin += 1
        sub = serie[j:i_fin]
        rets = []
        for k in range(1, len(sub)):
            p0, p1 = sub[k - 1][1], sub[k][1]
            if p0 > 0 and p1 > 0:
                rets.append(math.log(p1 / p0))
        h = _hurst_rs(rets)
        if h is not None:
            out.append((t, h))
        t += PASO_MIN * 60
    return out


def _bucket_h(h):
    if h >= 0.58:
        return "alto_tendencial"
    if h <= 0.42:
        return "bajo_reversion"
    return "medio_paseo_aleatorio"


def _lookup_h(h_rodante, ts, tol_s=1800):
    if not h_rodante:
        return None
    lo, hi = 0, len(h_rodante) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if h_rodante[mid][0] < ts:
            lo = mid + 1
        else:
            hi = mid - 1
    best = None
    for idx in (hi, lo):
        if 0 <= idx < len(h_rodante) and abs(h_rodante[idx][0] - ts) <= tol_s:
            if best is None or abs(h_rodante[idx][0] - ts) < abs(best[0] - ts):
                best = h_rodante[idx]
    return best[1] if best else None


def _pnl_neto(ask, acierto):
    gross_win = (1 - ask) / ask
    return gross_win * (1 - FEE) if acierto else -1.0


def _cargar_outcomes():
    out = {}
    with open(SNIPER, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("acierto") not in ("0", "1"):
                continue
            out[(r["wallet"], r["market_slug"], r["trade_timestamp"])] = int(r["acierto"])
    return out


def _shuffle_test_medias(a, b, n_shuffle=2000):
    import random
    if len(a) < 5 or len(b) < 5:
        return None
    obs = (sum(a) / len(a)) - (sum(b) / len(b))
    todo = list(a) + list(b)
    na = len(a)
    rnd = random.Random(17)
    cnt = 0
    for _ in range(n_shuffle):
        rnd.shuffle(todo)
        aa, bb = todo[:na], todo[na:]
        diff = (sum(aa) / len(aa)) - (sum(bb) / len(bb))
        if abs(diff) >= abs(obs):
            cnt += 1
    return cnt / n_shuffle


def main():
    print("Cargando klines y Hurst rodante...")
    series = _cargar_klines()
    h_rodante = {a: _hurst_rodante(series.get(a, []), VENTANA_MIN) for a in ACTIVOS}

    print("Cargando outcomes reales (wallet_mirror_sniper_dry_run.csv)...")
    outcomes = _cargar_outcomes()
    print(f"  {len(outcomes)} outcomes")

    print("Cargando executor (ask real, filtrado sigue_fillable_en_decision=1, post-TWAP)...")
    filas = []
    with open(EXECUTOR, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("sigue_fillable_en_decision") != "1":
                continue
            activo = r.get("activo")
            if activo not in ACTIVOS:
                continue
            marco = r.get("marco", "?")
            if sp.es_pre_twap(marco, r.get("timestamp_utc", "")):
                continue
            clave_out = (r["wallet"], r["market_slug"], r["trade_timestamp"])
            ac = outcomes.get(clave_out)
            if ac is None:
                continue
            try:
                ask = float(r["ask_decision"])
                ts = datetime.fromisoformat(r["trade_timestamp"]).timestamp()
            except (TypeError, ValueError, KeyError):
                continue
            if not (0.0 < ask < 1.0):
                continue
            pnl = _pnl_neto(ask, ac)
            grande = r.get("es_jugada_grande") == "1"
            filas.append({"ts": ts, "activo": activo, "marco": marco,
                           "acierto": ac, "pnl": pnl, "grande": grande, "ask": ask})

    print(f"  {len(filas)} filas fillable+resueltas post-TWAP")

    cruzadas = []
    for f in filas:
        h = _lookup_h(h_rodante.get(f["activo"], []), f["ts"])
        if h is None:
            continue
        cruzadas.append({**f, "h": h, "h_bucket": _bucket_h(h)})

    print(f"  {len(cruzadas)} filas con H asignado")

    def _resumen(subset):
        por_bucket = defaultdict(list)
        for c in subset:
            por_bucket[c["h_bucket"]].append(c)
        out = {}
        for b, items in por_bucket.items():
            n = len(items)
            hits = sum(c["acierto"] for c in items)
            pnls = [c["pnl"] for c in items]
            out[b] = {"n": n, "hit": round(hits / n, 4), "pnl_medio": round(sum(pnls) / n, 4)}
        return out

    resumen_global = _resumen(cruzadas)

    # desagregado por (activo, marco) -- CLAUDE.md pt.17, nunca solo agregado
    por_activo_marco = defaultdict(list)
    for c in cruzadas:
        por_activo_marco[(c["activo"], c["marco"])].append(c)
    resumen_por_activo_marco = {f"{a}#{m}": _resumen(items) for (a, m), items in por_activo_marco.items()
                                  if len(items) >= 15}

    # shuffle test global bajo vs medio (pnl)
    por_bucket_global = defaultdict(list)
    for c in cruzadas:
        por_bucket_global[c["h_bucket"]].append(c["pnl"])
    a = por_bucket_global.get("bajo_reversion", [])
    b = por_bucket_global.get("medio_paseo_aleatorio", [])
    p_shuffle = _shuffle_test_medias(a, b)

    # split-half del bucket con mejor pnl (estabilidad antes de creer nada)
    mejor_bucket = max(resumen_global, key=lambda k: resumen_global[k]["pnl_medio"]) if resumen_global else None
    split_half = None
    if mejor_bucket:
        items_mejor = sorted([c for c in cruzadas if c["h_bucket"] == mejor_bucket], key=lambda c: c["ts"])
        mitad = len(items_mejor) // 2
        if mitad >= 5:
            m1, m2 = items_mejor[:mitad], items_mejor[mitad:]
            split_half = {
                "bucket": mejor_bucket,
                "1a_mitad": {"n": len(m1), "hit": round(sum(c["acierto"] for c in m1) / len(m1), 4),
                             "pnl_medio": round(sum(c["pnl"] for c in m1) / len(m1), 4)},
                "2a_mitad": {"n": len(m2), "hit": round(sum(c["acierto"] for c in m2) / len(m2), 4),
                             "pnl_medio": round(sum(c["pnl"] for c in m2) / len(m2), 4)},
            }

    out = {
        "generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "n_total_cruzado": len(cruzadas),
        "resumen_global_por_bucket_h": resumen_global,
        "p_shuffle_pnl_bajo_vs_medio_global": p_shuffle,
        "split_half_mejor_bucket": split_half,
        "resumen_por_activo_marco_bucket_h": resumen_por_activo_marco,
    }
    OUT_PATH.write_text(__import__("json").dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGuardado en {OUT_PATH}")
    print(__import__("json").dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
