"""
analisis_wallets_crossdominio_01sep.py — Propuesta #9 del backlog cross-repo
(27-Ago, ver idea_10_propuestas_cross_repo_27ago / idea_ronda2_propuestas_
profundas_27ago_actualizacion_01sep): wallets "humanas" de baja frecuencia
que operan en MÚLTIPLES dominios (cripto + sports) -- hipótesis de que su
edge/hit-rate podría ser mayor que el de wallets especialistas de un solo
dominio (información generalista vs bots de alta frecuencia especializados,
ya cubiertos por bot_wallets_gate_bucket_fase0.py / wallet_especialistas_
observer.py).

Weather (repo aparte, /root/polymarket-weather) queda FUERA de este cruce a
propósito -- CLAUDE.md prohíbe mezclar código/datos entre repos, y no hay
overlap de wallets accesible sin tocarlo.

Fuentes (solo lectura, ventana de 6 días, 27-Ago a 01-Sep, la disponible en
ambos dominios):
  - data/sports/activity_ws_YYYY-MM-DD.csv        (firehose sports)
  - /root/polymarket-research-datalogs/polymarket_activity_YYYY-MM-DD.csv
    (firehose cripto, movido fuera del repo 29-Jul, ver fetch_polymarket_
    activity_ws.py)
  - data/shadow/wallet_edge_score_por_activo_marco.json (score validado
    cripto, por wallet#activo#marco)
  - data/sports/wallet_edge_score_por_categoria.json::wallets_validadas
    (score validado sports, por wallet+categoria)

Salida: data/shadow/wallets_crossdominio_analisis.json
"""

import csv
import json
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
DIAS = ["2026-08-27", "2026-08-28", "2026-08-29", "2026-08-30", "2026-08-31", "2026-09-01"]

# "Humana"/baja frecuencia: bots de alta frecuencia ya cubiertos por otros
# mecanismos (bot_wallets_gate_bucket_fase0.py, wallet_especialistas_
# observer.py) suelen superar cientos de trades/día en un solo dominio.
# Umbral documentado: <10 trades/día de media combinando los dos dominios
# en la ventana de 6 días -> <60 trades totales.
UMBRAL_TRADES_TOTAL = 60


def contar_trades_por_wallet(paths, col_wallet="wallet"):
    c = defaultdict(int)
    for p in paths:
        if not p.exists():
            continue
        with open(p, encoding="utf-8", errors="replace") as f:
            for row in csv.DictReader(f):
                w = (row.get(col_wallet) or "").strip().lower()
                if w:
                    c[w] += 1
    return c


def main():
    sports_paths = [REPO / "data" / "sports" / f"activity_ws_{d}.csv" for d in DIAS]
    crypto_paths = [DATALOGS / f"polymarket_activity_{d}.csv" for d in DIAS]

    n_sports_files = sum(1 for p in sports_paths if p.exists())
    n_crypto_files = sum(1 for p in crypto_paths if p.exists())
    print(f"Ficheros sports encontrados: {n_sports_files}/{len(DIAS)}")
    print(f"Ficheros cripto encontrados: {n_crypto_files}/{len(DIAS)}")

    trades_sports = contar_trades_por_wallet(sports_paths)
    trades_crypto = contar_trades_por_wallet(crypto_paths)
    print(f"Wallets únicas sports: {len(trades_sports)}")
    print(f"Wallets únicas cripto: {len(trades_crypto)}")

    cross = set(trades_sports) & set(trades_crypto)
    print(f"Wallets cross-dominio (aparecen en ambos): {len(cross)}")

    cross_baja_freq = []
    for w in cross:
        total = trades_sports[w] + trades_crypto[w]
        if total <= UMBRAL_TRADES_TOTAL:
            cross_baja_freq.append((w, trades_sports[w], trades_crypto[w], total))
    cross_baja_freq.sort(key=lambda x: -x[3])
    print(f"Wallets cross-dominio de baja frecuencia (<= {UMBRAL_TRADES_TOTAL} trades/6d, "
          f"perfil 'humano'): {len(cross_baja_freq)}")

    # ── Scores de edge ya validados ──────────────────────────────────────
    crypto_score = json.load(open(REPO / "data" / "shadow" / "wallet_edge_score_por_activo_marco.json"))
    sports_score_raw = json.load(open(REPO / "data" / "sports" / "wallet_edge_score_por_categoria.json"))
    sports_validadas = sports_score_raw.get("wallets_validadas", [])

    # índice wallet -> lista de entradas (crypto: dict values ya llevan 'wallet')
    crypto_por_wallet = defaultdict(list)
    for _, v in crypto_score.items():
        w = (v.get("wallet") or "").lower()
        if w:
            crypto_por_wallet[w].append(v)
    sports_por_wallet = defaultdict(list)
    for v in sports_validadas:
        w = (v.get("wallet") or "").lower()
        if w:
            sports_por_wallet[w].append(v)

    def resumen_wallet(entradas):
        """n total, edge_pp ponderado por n, p_shuffle mínimo, cuántas entradas significativas."""
        n_tot = sum(e.get("n", 0) for e in entradas)
        if n_tot == 0:
            return None
        edge_pond = sum(e.get("edge_pp", 0) * e.get("n", 0) for e in entradas) / n_tot
        sig = sum(1 for e in entradas if (e.get("p_shuffle", 1) is not None and e.get("p_shuffle", 1) < 0.05))
        return {"n_total": n_tot, "edge_pp_ponderado": round(edge_pond, 3),
                "n_entradas": len(entradas), "n_significativas_p<0.05": sig}

    resultado_cross = []
    edges_cross_validos = []
    for w, n_sp, n_cr, total in cross_baja_freq:
        r_crypto = resumen_wallet(crypto_por_wallet.get(w, []))
        r_sports = resumen_wallet(sports_por_wallet.get(w, []))
        entry = {"wallet": w, "n_trades_sports_6d": n_sp, "n_trades_crypto_6d": n_cr,
                 "n_trades_total_6d": total, "score_crypto": r_crypto, "score_sports": r_sports}
        resultado_cross.append(entry)
        edges = []
        if r_crypto and r_crypto["n_total"] >= 15:
            edges.append(r_crypto["edge_pp_ponderado"])
        if r_sports and r_sports["n_total"] >= 15:
            edges.append(r_sports["edge_pp_ponderado"])
        if edges:
            edges_cross_validos.append(sum(edges) / len(edges))

    # ── Baseline: wallets especialistas de UN solo dominio ya validadas ──
    crypto_sig = [v for v in crypto_score.values()
                  if v.get("wallet", "").lower() not in cross and v.get("n", 0) >= 15
                  and v.get("sig_bhfdr") is True]
    sports_sig = [v for v in sports_validadas
                  if v.get("wallet", "").lower() not in cross and v.get("n", 0) >= 15
                  and v.get("p_shuffle", 1) is not None and v.get("p_shuffle", 1) < 0.05]
    edges_especialistas = [v.get("edge_pp", 0) for v in crypto_sig] + [v.get("edge_pp", 0) for v in sports_sig]

    edge_medio_cross = round(sum(edges_cross_validos) / len(edges_cross_validos), 3) if edges_cross_validos else None
    edge_medio_especialistas = round(sum(edges_especialistas) / len(edges_especialistas), 3) if edges_especialistas else None

    salida = {
        "generado_utc": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(timespec="seconds"),
        "ventana_dias": DIAS,
        "umbral_trades_total_baja_frecuencia": UMBRAL_TRADES_TOTAL,
        "n_wallets_sports": len(trades_sports),
        "n_wallets_crypto": len(trades_crypto),
        "n_wallets_crossdominio_total": len(cross),
        "n_wallets_crossdominio_baja_frecuencia": len(cross_baja_freq),
        "n_wallets_crossdominio_con_score_valido_n>=15": len(edges_cross_validos),
        "edge_pp_medio_crossdominio_bajafrecuencia": edge_medio_cross,
        "n_wallets_especialistas_baseline": len(edges_especialistas),
        "edge_pp_medio_especialistas_undominio": edge_medio_especialistas,
        "weather_incluido": False,
        "weather_motivo_exclusion": "repo aparte (/root/polymarket-weather), sin overlap de wallets accesible sin tocar su código -- CLAUDE.md prohíbe mezclar",
        "wallets_crossdominio_baja_frecuencia": resultado_cross[:200],  # cap tamaño salida
    }

    out_path = REPO / "data" / "shadow" / "wallets_crossdominio_analisis.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(salida, f, indent=2, ensure_ascii=False)

    print(f"\n→ {out_path}")
    print(f"edge_pp medio cross-dominio (n>=15, baja frec.): {edge_medio_cross}")
    print(f"edge_pp medio especialistas un solo dominio (baseline): {edge_medio_especialistas}")


if __name__ == "__main__":
    main()
