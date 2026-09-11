#!/usr/bin/env python3
"""analisis_candidata12_jugada_grande_bots_25ago.py -- Candidata 12:
"jugada grande" (usd_trade >= 2x mediana propia de la wallet) generalizada
a las 84 bot wallets, no solo Wallet Mirror SEGUIR. Reusa pnl_neto/
shuffle_test/bh_fdr_signif de analisis_bot_wallets_gate_bucket_25ago.py
(mismo rigor, no duplicar formula). Desagrega por (arquetipo,activo,marco,
grande) antes de bucket de precio -- CLAUDE.md pt.17.

Solo lectura.
"""
import csv
import statistics
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import shadow_postmortem as sp  # noqa: E402
from analisis_bot_wallets_gate_bucket_25ago import pnl_neto, shuffle_test, bh_fdr_signif  # noqa: E402

IN = REPO / "data/shadow/bot_wallets_gate_bucket_fase0.csv"
N_MIN = 15


def main():
    filas_por_wallet = defaultdict(list)
    with open(IN, encoding="utf-8") as f:
        todas = list(csv.DictReader(f))
    for r in todas:
        try:
            usd = float(r.get("usd_trade") or 0)
        except (TypeError, ValueError):
            continue
        if usd > 0:
            filas_por_wallet[r["wallet"]].append(usd)

    mediana_por_wallet = {w: statistics.median(v) for w, v in filas_por_wallet.items() if len(v) >= 3}
    print(f"wallets con mediana propia calculable (n>=3 trades): {len(mediana_por_wallet)}")

    grupos = defaultdict(list)  # (arquetipo,activo,marco,grande) -> [(ts,pnl)]
    for r in todas:
        if not r.get("outcome_real"):
            continue
        ask_raw = r.get("mejor_ask_deteccion", "")
        if not ask_raw:
            continue
        try:
            ask = float(ask_raw)
            usd = float(r.get("usd_trade") or 0)
        except (TypeError, ValueError):
            continue
        if not (0.0 < ask < 1.0) or usd <= 0:
            continue
        w = r["wallet"]
        mediana = mediana_por_wallet.get(w)
        if mediana is None or mediana <= 0:
            continue
        marco = r.get("marco", "?")
        if sp.es_pre_twap(marco, r.get("timestamp_utc", "")):
            continue
        grande = "grande" if usd >= 2 * mediana else "no_grande"
        acierto = 1 if r.get("outcome_real") == r.get("lado_wallet") else 0
        pnl = pnl_neto(ask, acierto)
        clave = (r.get("arquetipo", "?"), r.get("activo", "?"), marco, grande)
        grupos[clave].append((r["timestamp_utc"], pnl))

    print(f"\ngrupos (arquetipo,activo,marco,grande): {len(grupos)}")
    print(f"{'clave':45} {'n':6} {'pnl_medio':10} {'p_shuffle':10}")

    pendientes = []
    resumen = {}
    for clave, filas in grupos.items():
        if len(filas) < N_MIN:
            continue
        clave_str = "#".join(clave)
        pnls = [p for _, p in filas]
        media = sum(pnls) / len(pnls)
        resumen[clave_str] = {"n": len(pnls), "pnl_medio": round(media, 4)}
        # contraste contra el resto del mismo (arquetipo,activo,marco) con jugada distinta
        arquetipo, activo, marco, grande = clave
        contraria = "no_grande" if grande == "grande" else "grande"
        otras = grupos.get((arquetipo, activo, marco, contraria), [])
        if len(otras) >= N_MIN:
            diff, p = shuffle_test(pnls, [p for _, p in otras],
                                    seed_key=f"cand12#{clave_str}")
            resumen[clave_str]["p_shuffle_vs_contraria"] = round(p, 4)
            resumen[clave_str]["diff_vs_contraria"] = round(diff, 4)
            if p < 0.05:
                pendientes.append((clave_str, diff, p, len(pnls), media))

    for clave_str, d in sorted(resumen.items(), key=lambda kv: -kv[1]["n"])[:30]:
        p_str = f"{d.get('p_shuffle_vs_contraria', ''):>8}" if 'p_shuffle_vs_contraria' in d else "     n/a"
        print(f"{clave_str:45} {d['n']:6} {d['pnl_medio']:+10.3f} {p_str}")

    print(f"\nDiferencias grande-vs-no_grande con p_shuffle<0.05 (sin corregir BH-FDR todavia): {len(pendientes)}")
    for clave_str, diff, p, n, media in sorted(pendientes, key=lambda x: x[2]):
        print(f"  {clave_str}: n={n} pnl_medio={media:+.3f} diff={diff:+.3f} p={p:.4f}")


if __name__ == "__main__":
    main()
