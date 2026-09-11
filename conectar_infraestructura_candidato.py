"""
conectar_infraestructura_candidato.py — cruza una tupla live (o cualquier
candidata) contra TODA la infraestructura de ballenas/micro-bucket/timing
que ya existe, en vez de mirarla ad-hoc cada vez (petición Javi 02-Ago,
ver memoria project_conectar_infraestructura_todas_candidatas_cementerio_02ago).

Uso:
    python3 conectar_infraestructura_candidato.py "STRATEGY#SUBTYPE#DIRECTION" [...]

Para cada trade REAL (dinero real, trades.csv) de la tupla:
  1. Localiza la predicción original (predictions_YYYY-MM-DD.csv, por
     market_id+strategy+subtype+decision) para recuperar sus features
     (py_entrada, n_total_lado, restante_min, banda_fina_vetaria_fase1,
     banda_fina_motivo, hora_utc).
  2. Imprime una tabla por trade, ordenada por pnl_neto_eur (peor primero)
     — el objetivo es ver si las PÉRDIDAS GRANDES comparten alguna
     condición (poco volumen de ballenas, timing concreto, fuera de banda
     fina) que las pérdidas pequeñas/ganancias no tienen.

n típicamente bajo (15-25) en tuplas recién promocionadas — esto es
EXPLORATORIO, no un gate riguroso (CLAUDE.md: n<15 no concluye nada).
"""
import csv
import glob
import json
import sys
from pathlib import Path

TRADES_PATH = Path("data/live/trades.csv")
PRED_GLOB = "data/shadow/predictions_*.csv"

FEATURE_KEYS = [
    "py_entrada", "n_total_lado", "restante_min",
    "banda_fina_vetaria_fase1", "banda_fina_motivo", "hora_utc",
]


def _split_tupla(tupla_clave: str) -> tuple[str, str, str]:
    partes = tupla_clave.split("#")
    return partes[0], "#".join(partes[1:-1]), partes[-1]


def cargar_trades(tupla_clave: str) -> list[dict]:
    strategy, subtype, direction = _split_tupla(tupla_clave)
    out = []
    with open(TRADES_PATH, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if (row.get("strategy") == strategy and row.get("subtype") == subtype
                    and row.get("direction") == direction and row.get("status") == "CLOSED"):
                out.append(row)
    return out


def indice_predicciones(strategy: str, subtype: str, decision: str) -> dict:
    """market_id -> features dict, escaneando todos los predictions_*.csv."""
    idx = {}
    for path in sorted(glob.glob(PRED_GLOB)):
        try:
            with open(path, encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    if (row.get("strategy") == strategy and row.get("subtype") == subtype
                            and row.get("decision") == decision):
                        mid = row.get("market_id")
                        if mid and mid not in idx:
                            try:
                                idx[mid] = json.loads(row.get("features") or "{}")
                            except json.JSONDecodeError:
                                idx[mid] = {}
        except FileNotFoundError:
            continue
    return idx


def main(tuplas: list[str]):
    for tupla_clave in tuplas:
        strategy, subtype, direction = _split_tupla(tupla_clave)
        trades = cargar_trades(tupla_clave)
        if not trades:
            print(f"\n=== {tupla_clave}: 0 trades reales cerrados ===")
            continue
        pred_idx = indice_predicciones(strategy, subtype, direction)

        filas = []
        for t in trades:
            feats = pred_idx.get(t["market_id"], {})
            pnl = float(t["pnl_neto_eur"]) if t.get("pnl_neto_eur") not in (None, "") else 0.0
            filas.append({
                "market_id": t["market_id"],
                "entry_price": t.get("entry_price"),
                "pnl_neto_eur": pnl,
                "stake_eur": t.get("stake_eur"),
                **{k: feats.get(k) for k in FEATURE_KEYS},
            })

        filas.sort(key=lambda r: r["pnl_neto_eur"])

        n = len(filas)
        n_win = sum(1 for r in filas if r["pnl_neto_eur"] > 0)
        pnl_total = sum(r["pnl_neto_eur"] for r in filas)
        print(f"\n=== {tupla_clave}: n={n} trades reales, {n_win} ganadores "
              f"({n_win/n*100:.0f}%), pnl_total={pnl_total:+.2f}€ ===")
        if n < 15:
            print("  ⚠️  n<15 — EXPLORATORIO, no concluir nada, solo mirar patrones a vigilar.")

        hdr = f"{'pnl€':>7} {'stake€':>7} {'entry':>6} {'n_wlado':>8} {'rest_min':>9} {'banda_fina':>11} {'hora':>5}  motivo"
        print(hdr)
        print("-" * len(hdr))
        for r in filas:
            nw = r.get("n_total_lado")
            rm = r.get("restante_min")
            bf = r.get("banda_fina_vetaria_fase1")
            print(f"{r['pnl_neto_eur']:>7.2f} {float(r['stake_eur'] or 0):>7.2f} "
                  f"{float(r['entry_price'] or 0):>6.3f} "
                  f"{('—' if nw is None else str(nw)):>8} "
                  f"{('—' if rm is None else f'{rm:.1f}'):>9} "
                  f"{('—' if bf is None else str(bf)):>11} "
                  f"{('—' if r.get('hora_utc') is None else str(r.get('hora_utc'))):>5}  "
                  f"{r.get('banda_fina_motivo') or ''}")

        # Resumen pérdidas grandes vs resto
        perdidas = [r for r in filas if r["pnl_neto_eur"] < 0]
        if perdidas:
            peor_mediana = sorted(r["pnl_neto_eur"] for r in perdidas)[len(perdidas)//2]
            grandes = [r for r in perdidas if r["pnl_neto_eur"] <= peor_mediana]
            pequenas = [r for r in perdidas if r["pnl_neto_eur"] > peor_mediana]

            def resumen(grupo, etiqueta):
                if not grupo:
                    return
                con_dato = [r for r in grupo if r.get("n_total_lado") is not None]
                nw_medio = (sum(r["n_total_lado"] for r in con_dato) / len(con_dato)
                            if con_dato else None)
                fuera_banda = sum(1 for r in grupo if r.get("banda_fina_vetaria_fase1") is False)
                print(f"  {etiqueta}: n={len(grupo)}, n_total_lado medio="
                      f"{'—' if nw_medio is None else f'{nw_medio:.1f}'} "
                      f"({len(con_dato)}/{len(grupo)} con dato), "
                      f"fuera_banda_fina={fuera_banda}/{len(grupo)}")

            print("  --- pérdidas grandes vs pequeñas ---")
            resumen(grandes, "PÉRDIDAS GRANDES")
            resumen(pequenas, "pérdidas pequeñas")


if __name__ == "__main__":
    tuplas = sys.argv[1:] or [
        "BALLENAS_TARDIAS#BTC#15min#BUY_YES",
        "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min#BUY_YES",
        "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min#BUY_YES",
    ]
    main(tuplas)
