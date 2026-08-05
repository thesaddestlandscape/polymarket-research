#!/usr/bin/env python3
"""
analisis_cruce_live_ready_ballenas_04ago.py — Cruza las 46 candidatas
"LIVE READY" que salió el /inicio (script legacy, solo IC agregado n>=40)
contra TODA la infraestructura ya construida del proyecto, antes de
tratar cualquiera como oportunidad nueva (CLAUDE.md pt.8: "ballenas es la
lente por defecto, cruzar SIEMPRE").

Para cada candidata (strategy#activo#marco):
  1. Dirección real -- se calcula IC por BUY_YES/BUY_NO por separado
     (results.csv) y se toma la de mejor IC con n>=15.
  2. ¿Ya está en pares_permitidos_live? (ya vive, no es "nueva")
  3. ¿Ya está en candidatos_evaluacion_live? (ya se vigila fill-ability)
  4. gate_bucket_propio.json -- veredicto agregado de sus buckets
     (malo_confirmado/bueno_confirmado/sin_concluir/sin_datos)
  5. ballenas_timing_state.json -- ¿hay banda significativa calibrada
     para este (activo,marco)?
  6. veto_ballenas.combos_validados -- ¿esta combinación activo#marco
     está protegida por el veto de concentración?
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data" / "shadow" / "results.csv"
CONFIG_LIVE = REPO / "data" / "live" / "config_live.json"
GATE_BUCKET = REPO / "data" / "shadow" / "gate_bucket_propio.json"
BALLENAS_TIMING = REPO / "data" / "shadow" / "ballenas_timing_state.json"

CANDIDATOS = [
    "WEEKLY_PRICE#ETH", "WEEKLY_PRICE#BTC", "WEEKLY_PRICE#SOL",
    "GBM_LATE_15M#XRP#15min", "STREAK_FADE_15M#SOL#15min",
    "GBM_LATE_15M_TARDIO#XRP#15min", "GBM_LATE_15M_ESPACIO_ATR#XRP#15min",
    "FAVORITO_CONFIRMADO#BTC#15min", "FAVORITO_CONFIRMADO#ETH#15min",
    "FAVORITO_CONFIRMADO#SOL#15min", "FAVORITO_CONFIRMADO#ETH#5min",
    "FAVORITO_CONFIRMADO#SOL#240min", "FAVORITO_CONFIRMADO#ETH#60min",
    "FAVORITO_CONFIRMADO#SOL#60min", "FAVORITO_CONFIRMADO#BTC#60min",
    "GBM_LATE_15M_PYCONFIRMADO#XRP#15min", "UPDOWN_GBM_15M_TARDIO#BTC#15min",
    "FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min",
    "UPDOWN_GBM_15M_TARDIO#ETH#15min",
    "UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min",
    "UPDOWN_GBM_15M_TARDIO#XRP#15min",
    "UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min",
    "UPDOWN_GBM_15M_TARDIO#BNB#15min", "UPDOWN_GBM_15M_TARDIO#DOGE#15min",
    "BALLENAS_TARDIAS#BTC#15min", "GBM_LATE_15M#DOGE#15min",
    "GBM_LATE_15M_TARDIO#DOGE#15min", "GBM_LATE_15M_ESPACIO_ATR#DOGE#15min",
    "GBM_LATE_15M#BNB#15min", "GBM_LATE_15M_TARDIO#BNB#15min",
    "GBM_LATE_15M_ESPACIO_ATR#BNB#15min",
    "FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min",
    "FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min",
    "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min",
    "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min",
    "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min",
    "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min",
    "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min",
    "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min",
    "BALLENAS_TARDIAS#DOGE#5min",
    "FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min",
    "FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min",
    "FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min",
    "FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min",
    "FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min",
    "FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min",
]

MARCO_A_BALLENAS = {"5min": "5m", "15min": "15m", "60min": "60m", "240min": "240m"}


def ic(w, n):
    return ((w + 1) / (n + 2) - 0.5) * min(1.0, n / 20)


def main():
    rows = list(csv.DictReader(open(RESULTS, encoding="utf-8")))
    config = json.loads(CONFIG_LIVE.read_text())
    pares_live = set(config.get("pares_permitidos_live", []))
    candidatos_eval = set(config.get("candidatos_evaluacion_live", []))
    veto_combos = set(config.get("riesgo", {}).get("veto_ballenas", {}).get("combos_validados", []))
    gate_bucket = json.loads(GATE_BUCKET.read_text()) if GATE_BUCKET.exists() else {}
    ballenas_timing = json.loads(BALLENAS_TIMING.read_text()) if BALLENAS_TIMING.exists() else {}

    for clave in CANDIDATOS:
        partes = clave.split("#")
        strategy = partes[0]
        activo = partes[1] if len(partes) > 1 else None
        marco = partes[2] if len(partes) > 2 else None

        # dirección: mejor IC por BUY_YES/BUY_NO con n>=15
        por_dir = defaultdict(list)
        for r in rows:
            k = r["strategy"] + ("#" + r["subtype"] if r.get("subtype") else "")
            if k == clave:
                por_dir[r["decision"]].append(int(r["acierto"]))
        mejor_dir, mejor_ic, mejor_n = None, -999, 0
        for d, hits in por_dir.items():
            if len(hits) >= 15:
                icd = ic(sum(hits), len(hits))
                if icd > mejor_ic:
                    mejor_dir, mejor_ic, mejor_n = d, icd, len(hits)

        tupla_str = f"{clave}#{mejor_dir}" if mejor_dir else None
        ya_live = any(p.startswith(clave + "#") for p in pares_live)
        ya_candidato = any(p.startswith(clave + "#") for p in candidatos_eval) or clave in candidatos_eval

        # gate_bucket_propio: veredicto agregado
        gb_tabla = gate_bucket.get(tupla_str, {}) if tupla_str else {}
        veredictos = [v.get("veredicto") for v in gb_tabla.values()] if isinstance(gb_tabla, dict) else []
        n_malo = veredictos.count("malo_confirmado")
        n_bueno = veredictos.count("bueno_confirmado")

        # ballenas_timing_state: banda significativa para (activo, marco)
        marco_b = MARCO_A_BALLENAS.get(marco, marco)
        combo_ballenas = f"{activo}#{marco_b}" if activo and marco_b else None
        banda_sig = ballenas_timing.get(combo_ballenas, {}).get("significativo") if combo_ballenas else None

        veto_activo = combo_ballenas in veto_combos if combo_ballenas else False

        flags = []
        if ya_live:
            flags.append("YA LIVE")
        if ya_candidato:
            flags.append("ya en candidatos_evaluacion")
        if n_malo:
            flags.append(f"gate_bucket: {n_malo} malo_confirmado")
        if n_bueno:
            flags.append(f"gate_bucket: {n_bueno} bueno_confirmado")
        if banda_sig:
            flags.append("ballenas: banda significativa")
        if veto_activo:
            flags.append("veto_ballenas activo")

        print(f"{clave:55s} dir={mejor_dir or '?':8s} IC={mejor_ic:+.3f} n={mejor_n:4d}  "
              f"{' | '.join(flags) if flags else '(sin conexión encontrada)'}")


if __name__ == "__main__":
    main()
