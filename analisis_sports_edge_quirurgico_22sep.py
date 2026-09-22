#!/usr/bin/env python3
"""
analisis_sports_edge_quirurgico_22sep.py -- 22-Sep, petición explícita
Javi ("con todo lo que hay de soccer, futbol, tennis, nfl, formula 1...
no hay NADA?"). Extiende a sports el MISMO motor robusto que ya corre en
cripto (analisis_edge_quirurgico_21sep.py::_evaluar_tupla -- multi-ancho
0.01-0.05, corrección max-estadístico, robustez por días independientes,
concentración de wallet, forward rodante), reusado tal cual (import, no
reimplementar), solo cambia el loader.

Origen del hallazgo (mismo día): el gate "_fino" de sports (analisis_
sports_wallet_mirror_gate_bucket_fino.py) tiene la MISMA debilidad ya
documentada y corregida en cripto -- busca cada día la ÚNICA ventana con
mayor diferencia, que puede no ser la misma de ayer (Tennis#SEGUIR: 3
días consecutivos bueno_confirmado, hoy la ventana con mayor diff salió
[0.16,0.21) con split_half_diff=[+2.06,-0.70], inconsistente, veredicto
cae a sin_concluir aunque el historial diga 3/3 -- NO es un bug de
gate_confirmacion_historial.py, verificado en código). Además, el gate
"_fino"/"grid" de sports solo evalúa un subconjunto pequeño de categorías
(CS/LoL/Dota/Valorant/Tennis/epl-ganador/fl1-ganador) pese a que
wallet_edge_score_por_categoria.json tiene 4.294 wallets validadas (BH-
FDR) en NFL/MLB/UFC/decenas de ligas de fútbol -- datos reales y
fillable (NFL n=203, MLB n=398, UFC n=69 tras el filtro ratio>=5x) que
nunca llegan a evaluarse.

Cubre TODO (categoria,tipo) presente en wallet_mirror_sniper_dry_run.csv
(sin lista hardcodeada -- mismo criterio "descubre solo" que el resto
del proyecto), con identidad de wallet real (a diferencia de la familia
"clásica" de cripto) -- el check de concentración de _evaluar_tupla()
SÍ aplica aquí, tal cual.

MODO LECTURA. No toca gates, config ni ejecutores.
"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_edge_quirurgico_21sep import (  # noqa: E402 -- mismo motor, no reimplementar
    _evaluar_tupla, N_MIN_TUPLA, ANCHOS, PISO_EUR, P_MAX,
)

DRY_RUN = REPO / "data/sports/wallet_mirror_sniper_dry_run.csv"
CONFIG_LIVE_SPORTS = REPO / "data/sports/config_live_sports.json"
OUT = REPO / "data/sports/edge_quirurgico_sports.json"

RATIO_MIN = 5.0
FEE = 0.05    # verificado 26-Ago contra gamma-api (sports_fees_v3), NO 0.07 de cripto
STAKE = 1.0


def payout_win(ask: float) -> float:
    return STAKE * (1 - ask) / ask - STAKE * FEE * (1 - ask)


def cargar_filas() -> dict:
    """{(categoria, tipo): [(ts, ask, pnl, wallet), ...]} -- TODO el
    universo presente en el dry-run, sin lista hardcodeada."""
    grupos = defaultdict(list)
    with open(DRY_RUN, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") not in ("0", "1"):
                continue
            try:
                ratio = float(row["ratio_vs_stake_mirror"])
                ask = float(row["mejor_ask_mirror"])
            except (TypeError, ValueError, KeyError):
                continue
            if ratio < RATIO_MIN or not (0.01 < ask < 0.99):
                continue
            acierto = int(row["acierto"])
            pnl = payout_win(ask) if acierto == 1 else -STAKE
            ts = row.get("resolved_ts") or row.get("timestamp_utc", "")
            key = (row["categoria"], row["tipo"])
            grupos[key].append((ts, ask, pnl, row.get("wallet", "")))
    return grupos


def _estado_config() -> dict:
    try:
        c = json.loads(CONFIG_LIVE_SPORTS.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {p: "LIVE" for p in c.get("pares_permitidos_live", [])}


def main():
    est = _estado_config()
    resultados = []
    grupos = cargar_filas()
    print(f"Combos (categoria,tipo): {len(grupos)} | con n>={N_MIN_TUPLA}: "
          f"{sum(1 for f in grupos.values() if len(f) >= N_MIN_TUPLA)}")
    for (categoria, tipo), filas in grupos.items():
        for w in _evaluar_tupla(filas, f"{categoria}#{tipo}"):
            resultados.append({"categoria": categoria, "tipo": tipo, **w})
    for r in resultados:
        r["estado"] = est.get(f"{r['categoria']}#{r['tipo']}", "candidata/dormida")
    por_categoria = defaultdict(list)
    for i, r in enumerate(resultados):
        por_categoria[r["categoria"]].append(i)
    for cat, idx in por_categoria.items():
        ps = [resultados[i]["p_max"] for i in idx]
        orden = sorted(range(len(ps)), key=lambda k: ps[k]); corte = -1
        for rank, k in enumerate(orden, 1):
            if ps[k] <= rank / len(ps) * P_MAX: corte = rank
        ok = set(orden[:corte]) if corte > 0 else set()
        for k, i in enumerate(idx):
            resultados[i]["bh_ok"] = k in ok
    resultados.sort(key=lambda r: (not r["bh_ok"], -r["pnl_sin_2_mejores_dias"]))
    OUT.write_text(json.dumps(resultados, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"tuplas con >=1 ventana calificada: "
          f"{len({(r['categoria'],r['tipo']) for r in resultados})} | "
          f"ventanas: {len(resultados)} | pasan BH-FDR: {sum(r['bh_ok'] for r in resultados)}")
    print(f"{'BH':2} {'estado':10} {'tupla':28} {'anch':5} {'ventana':12} {'n':>4} {'pnl':>6} {'dias':>4} {'sin2':>6} {'wal':>3} {'top1':>5} {'p':>6}")
    for r in resultados:
        tup = f"{r['categoria']}#{r['tipo']}"
        print(f"{'OK' if r['bh_ok'] else '--':2} {r['estado']:10} {tup:28} {r['ancho']:<5} [{r['lo']:.2f},{r['hi']:.2f}) {r['n']:>4} {r['pnl_medio']:+.3f} {r['n_dias']:>4} {r['pnl_sin_2_mejores_dias']:+.3f} {r['wallets']:>3} {r['top1_wallet']:>5.2f} {r['p_max']:>6.3f}")


if __name__ == "__main__":
    main()
