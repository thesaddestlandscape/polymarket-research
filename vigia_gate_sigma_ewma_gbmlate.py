#!/usr/bin/env python3
"""vigia_gate_sigma_ewma_gbmlate.py — Vigía del gate por zona de
sigma_ewma_delta_pct que vetea GBM_LATE_15M#{activo}#15min#BUY_YES
(ver GBM_LATE_15M_SIGMA_EWMA_ZONAS_BUENAS_BUY_YES en shadow_predict.py).

Origen (05-Ago, decisión explícita Javi): tras una racha real en
GBM_LATE_15M#{ETH,SOL}#15min#BUY_YES (n=6 hoy 0% hit, n=13 7d 23.1% hit vs
44% en 30d), se investigó sigma_ewma_delta_pct como causa raíz. El motor
causal (shadow_postmortem.py -> filtros_causales) NO capturaba el patrón
de forma fiable: para ETH encontró 11 umbrales distintos a lo largo de
semanas (bucket móvil que entra/sale del gate n>=15/IC<-0.12) y para SOL
encontró el filtro en la dirección BUY_NO, pasando por alto la zona mala
de BUY_YES. Un análisis ad-hoc con rigor completo (Wilson+shuffle+
bootstrap+split-half, n>=40) sobre resultados.csv encontró un patrón
CONSISTENTE en las 6 monedas: el edge de BUY_YES solo se confirma cuando
la volatilidad ACELERA (sigma_ewma_delta_pct alto), nunca cuando decelera.
Ese hallazgo se cableó como veto real en _s_gbm_late (fail-closed: fuera
de zona confirmada -> no apostar).

Este vigía existe porque esa tabla es una foto fija del 05-Ago -- según
crezca results.csv el mapa de zonas confirmadas puede cambiar (una zona
vetada hoy puede confirmarse buena mañana, o una permitida hoy puede dejar
de pasar el gate). Recorre el MISMO cálculo cada vez que se ejecuta
(cron diario, mismo patrón que vigia_gate_bucket_propio.py) y avisa por
Telegram SOLO si el veredicto de alguna (moneda, bucket) cambia respecto
al último aviso (latch) -- no cambia el código de shadow_predict.py solo,
eso requiere revisión explícita (decisión de Javi + /code-review si toca
una tupla que vaya a re-promocionarse a pares_permitidos_live).
"""
import csv
import json
import math
import random
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
csv.field_size_limit(10_000_000)

RESULTS_CSV = REPO / "data/shadow/results.csv"
LATCH = REPO / "data/live/vigia_gate_sigma_ewma_gbmlate_latch.json"

MONEDAS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
EDGES = [-999, -9, -6, -3, 0, 3, 6, 9, 12, 999]
N_MIN_GATE = 40
N_MIN_EXPLORA = 15

# Tabla ACTUALMENTE cableada en shadow_predict.py -- si este vigía diverge
# de esto, es la señal de que hay que revisar el código, no solo el aviso.
ZONAS_ACTIVAS = {
    "BTC": [(12.0, None)],
    "ETH": [],
    "SOL": [(6.0, 9.0), (12.0, None)],
    "XRP": [(9.0, None)],
    "DOGE": [(6.0, 9.0), (12.0, None)],
    "BNB": [(6.0, 9.0)],
}


def _wilson_lo(k, n, z=1.645):
    if n == 0:
        return 0.0
    p = k / n
    denom = 1 + z * z / n
    center = p + z * z / (2 * n)
    margin = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (center - margin) / denom


def _bootstrap_ci(pnls, iters=2000, seed=42):
    rnd = random.Random(seed)
    n = len(pnls)
    means = []
    for _ in range(iters):
        s = [pnls[rnd.randrange(n)] for _ in range(n)]
        means.append(sum(s) / n)
    means.sort()
    return means[int(0.05 * iters)], means[int(0.95 * iters)]


def _shuffle_p(data, lo, hi, iters=1500, seed=7):
    rnd = random.Random(seed)
    labels = [1 if lo <= d[0] < hi else 0 for d in data]
    pnls = [d[1] for d in data]
    obs_in = [p for p, l in zip(pnls, labels) if l == 1]
    obs_out = [p for p, l in zip(pnls, labels) if l == 0]
    if not obs_in or not obs_out:
        return None
    obs_diff = sum(obs_in) / len(obs_in) - sum(obs_out) / len(obs_out)
    n_in = len(obs_in)
    idxs = list(range(len(pnls)))
    cnt = 0
    for _ in range(iters):
        rnd.shuffle(idxs)
        sel, rest = idxs[:n_in], idxs[n_in:]
        m_in = sum(pnls[i] for i in sel) / len(sel)
        m_out = sum(pnls[i] for i in rest) / len(rest)
        diff = m_in - m_out
        if obs_diff >= 0 and diff >= obs_diff:
            cnt += 1
        elif obs_diff < 0 and diff <= obs_diff:
            cnt += 1
    return cnt / iters


def _cargar_datos():
    buckets = {m: [] for m in MONEDAS}
    if not RESULTS_CSV.exists():
        return buckets
    with open(RESULTS_CSV, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("strategy") != "GBM_LATE_15M" or r.get("decision") != "BUY_YES":
                continue
            sub = r.get("subtype", "")
            activo = sub.split("#")[0] if "#" in sub else None
            if activo not in buckets or not sub.endswith("#15min"):
                continue
            feats_raw = r.get("features")
            if not feats_raw:
                continue
            try:
                feats = json.loads(feats_raw)
            except Exception:
                continue
            sew = feats.get("sigma_ewma_delta_pct")
            if sew is None:
                continue
            try:
                pnl = float(r.get("pnl_neto"))
                acierto = int(r.get("acierto"))
            except Exception:
                continue
            buckets[activo].append((sew, pnl, acierto))
    return buckets


def _evaluar(buckets):
    """Devuelve {activo: {(lo,hi): veredicto_dict}}"""
    resultado = {}
    for activo, data in buckets.items():
        resultado[activo] = {}
        for lo, hi in zip(EDGES, EDGES[1:]):
            sub_d = [d for d in data if lo <= d[0] < hi]
            n = len(sub_d)
            if n < N_MIN_EXPLORA:
                continue
            pnls = [d[1] for d in sub_d]
            hits = [d[2] for d in sub_d]
            hit_rate = sum(hits) / n
            pnl_trade = sum(pnls) / n
            wlo = _wilson_lo(sum(hits), n)
            boot_lo, boot_hi = _bootstrap_ci(pnls)
            pval = _shuffle_p(data, lo, hi)
            half = n // 2
            first = sum(pnls[:half]) / half if half else None
            second = sum(pnls[half:]) / (n - half) if (n - half) else None
            consistente = (
                first is not None and second is not None
                and ((first >= 0 and second >= 0) or (first < 0 and second < 0))
            )
            gate_ok = (
                n >= N_MIN_GATE
                and (boot_lo > 0 or boot_hi < 0)
                and pval is not None and pval < 0.05
                and consistente
            )
            veredicto = "GATE_OK_BUENO" if (gate_ok and pnl_trade > 0) else (
                "GATE_OK_MALO" if (gate_ok and pnl_trade < 0) else "sin_concluir"
            )
            resultado[activo][f"{lo},{hi}"] = {
                "n": n, "hit_rate": round(hit_rate, 4), "pnl_trade": round(pnl_trade, 4),
                "wilson_lo": round(wlo, 4), "boot90": [round(boot_lo, 4), round(boot_hi, 4)],
                "p_shuffle": round(pval, 4) if pval is not None else None,
                "veredicto": veredicto,
            }
    return resultado


def _en_zona_activa(activo, lo, hi):
    # comparación simple por solape con el bucket evaluado
    for zlo, zhi in ZONAS_ACTIVAS.get(activo, []):
        zhi_v = zhi if zhi is not None else 999
        if lo >= zlo and hi <= zhi_v:
            return True
        if lo < zlo < hi or lo < zhi_v < hi:
            return True
    return False


def main() -> int:
    from shadow_digest import enviar_telegram

    buckets = _cargar_datos()
    resultado = _evaluar(buckets)

    try:
        vistos = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        vistos = {}

    cambios = []
    for activo, zonas in resultado.items():
        for zona, info in zonas.items():
            lo_s, hi_s = zona.split(",")
            lo, hi = float(lo_s), float(hi_s)
            activa = _en_zona_activa(activo, lo, hi)
            clave = f"{activo}#{zona}"
            veredicto_actual = info["veredicto"]
            visto_prev = vistos.get(clave, {}).get("veredicto")
            if veredicto_actual != visto_prev:
                riesgo = None
                if activa and veredicto_actual == "GATE_OK_MALO":
                    riesgo = "⚠️ ZONA ACTIVA (permitida hoy) YA NO PASA EL GATE / da negativo"
                elif not activa and veredicto_actual == "GATE_OK_BUENO":
                    riesgo = "💡 ZONA VETADA hoy pasa el gate en positivo -- candidata a ampliar"
                elif activa and veredicto_actual == "sin_concluir":
                    riesgo = "zona activa dejó de tener gate limpio (ahora sin_concluir)"
                cambios.append((clave, visto_prev, veredicto_actual, info, activa, riesgo))
            vistos[clave] = {"veredicto": veredicto_actual, "n": info["n"], "pnl_trade": info["pnl_trade"]}

    print(f"[vigia_gate_sigma_ewma_gbmlate] monedas={len(resultado)} cambios={len(cambios)}")
    for clave, prev, actual, info, activa, riesgo in cambios:
        print(f"  {clave}: {prev} -> {actual} n={info['n']} pnl/trade={info['pnl_trade']} activa_hoy={activa} {riesgo or ''}")

    relevantes = [c for c in cambios if c[5]]  # solo avisar de los que tienen riesgo/oportunidad real
    if relevantes:
        detalle = "\n".join(
            f"  {clave}: {prev}->{actual} n={info['n']} pnl/trade={info['pnl_trade']:+.3f} — {riesgo}"
            for clave, prev, actual, info, activa, riesgo in relevantes
        )
        msg = (
            "🔎 VIGÍA gate sigma_ewma_delta_pct (GBM_LATE_15M#BUY_YES) — cambio de veredicto:\n"
            f"{detalle}\n"
            "La tabla activa vive en shadow_predict.py::GBM_LATE_15M_SIGMA_EWMA_ZONAS_BUENAS_BUY_YES "
            "(cableada 05-Ago) -- este aviso NO cambia el código solo, revisar si conviene actualizar la tabla."
        )
        ok = enviar_telegram(msg)
        print(f"[vigia_gate_sigma_ewma_gbmlate] aviso enviado (telegram={ok})")

    LATCH.write_text(json.dumps(vistos, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_gate_sigma_ewma_gbmlate] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
