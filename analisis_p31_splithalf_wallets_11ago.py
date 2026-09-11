"""P31 (11-Ago): barrido sistemático de split-half sobre TODO el pool de
wallets con edge significativo (wallet_edge_score_por_activo_marco.json,
ya TWAP-limpio) -- no solo los 8 candidatos revisados a mano. Objetivo:
separar edge robusto (mismo signo en ambas mitades de su propio historial
post-TWAP) de posibles rachas de un solo periodo, antes de proponer
ningún gate/ejecutor. Solo lectura, no toca dinero ni decide nada.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

import shadow_postmortem as sp

DIR_SHADOW = Path("data/shadow")
HIST = DIR_SHADOW / "ballenas_timing_history.csv"
SCORES = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
OUT = DIR_SHADOW / "p31_splithalf_wallets.json"

MARCO_LARGO = {"5m": "5min", "15m": "15min", "60m": "60min", "240m": "240min"}
N_MIN_TOTAL = 30


def cargar_candidatos():
    d = json.loads(SCORES.read_text())
    cands = {}
    for k, v in d.items():
        if v.get("sig_bhfdr") and v.get("n", 0) >= 20:
            cands[(v["wallet"], v["activo"], v["marco"])] = v
    return cands


def main():
    candidatos = cargar_candidatos()
    print(f"Candidatos significativos (n>=20): {len(candidatos)}")

    filas_por_key = defaultdict(list)
    claves = set(candidatos.keys())
    with open(HIST, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            key = (row.get("wallet"), row.get("activo"), row.get("marco"))
            if key not in claves:
                continue
            marco_largo = MARCO_LARGO.get(key[2], key[2])
            if sp.es_pre_twap(marco_largo, row.get("ts_trade", "")):
                continue
            filas_por_key[key].append(row)

    resultados = {}
    n_robustos = 0
    n_flip = 0
    n_insuf = 0
    for key, rows in filas_por_key.items():
        rows.sort(key=lambda r: r["ts_trade"])
        n = len(rows)
        if n < N_MIN_TOTAL:
            n_insuf += 1
            continue
        mid = n // 2
        h1, h2 = rows[:mid], rows[mid:]

        def stats(rs):
            nn = len(rs)
            aciertos = sum(1 for r in rs if r.get("acierto") in ("1", "True", "true"))
            precios = [float(r["precio"]) for r in rs]
            pm = sum(precios) / nn
            hit = aciertos / nn
            return nn, hit, pm, (hit - pm) * 100

        n1, hit1, pm1, e1 = stats(h1)
        n2, hit2, pm2, e2 = stats(h2)
        mismo_signo = (e1 < 0) == (e2 < 0)
        w, activo, marco = key
        resultados[f"{w}#{activo}#{marco}"] = {
            "wallet": w, "activo": activo, "marco": marco,
            "n_total_post_twap": n,
            "edge_pp_original": candidatos[key]["edge_pp"],
            "n1": n1, "edge1_pp": round(e1, 2),
            "n2": n2, "edge2_pp": round(e2, 2),
            "mismo_signo": mismo_signo,
            "se_refuerza": mismo_signo and abs(e2) >= abs(e1),
        }
        if mismo_signo:
            n_robustos += 1
        else:
            n_flip += 1

    print(f"n_total>=30: {len(resultados)}  robustos(mismo signo): {n_robustos}  "
          f"flip: {n_flip}  insuficiente: {n_insuf}")

    OUT.write_text(json.dumps(resultados, indent=1))
    print(f"Guardado en {OUT}")

    print("\n=== ROBUSTOS QUE SE REFUERZAN (edge2 mas fuerte que edge1, mismo signo) ===")
    reforzados = [r for r in resultados.values() if r["se_refuerza"]]
    reforzados.sort(key=lambda r: -abs(r["edge2_pp"]) * min(r["n_total_post_twap"], 300) / 300)
    for r in reforzados[:40]:
        print(f"{r['wallet'][:10]} {r['activo']} {r['marco']:6s} n={r['n_total_post_twap']:5d}  "
              f"1a={r['edge1_pp']:+7.1f}pp(n={r['n1']})  2a={r['edge2_pp']:+7.1f}pp(n={r['n2']})")


if __name__ == "__main__":
    main()
