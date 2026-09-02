#!/usr/bin/env python3
"""
analisis_ev_fee_real_microbuckets_02sep.py — re-rankea los micro-buckets
confirmados de gate_bucket_propio.json por EV neto de la curva REAL de
fee (7%*p*(1-p)), no por el slippage plano del 2% que usa
`_pnl_normalizado()` en analisis_gate_bucket_propio_28jul.py.

Origen (02-Sep, propuesta #1 de "10 ineficiencias de plataforma"):
verificado que `results.csv::pnl_neto` (la fuente de gate_bucket_
propio.json) usa `SLIPPAGE=0.02` fijo (shadow_resolve.py:471/474), NUNCA
el fee real de Polymarket (FEE_RATE_TAKER_CRYPTO*p*(1-p), verificado al
céntimo contra fees on-chain reales, ver live_trade.py). La curva de fee
real es máxima en p=0.50 (1.75% del stake) y casi cero en los extremos
(p=0.05/0.95 -> 0.33%) -- un slippage plano del 2% SOBRESTIMA el coste
real en los extremos y puede INFRAESTIMARLO cerca de p=0.50 (aunque en
este caso concreto 1.75%<2%, sigue siendo overestimate, pero el gap
varía por precio, así que el ORDEN relativo entre buckets a distinto
precio puede cambiar).

Mecánica: `_pnl_normalizado()` es invertible -- conocido pnl_medio del
bucket y el precio de entrada real (bucket_mid, ajustado por dirección
BUY_NO), se puede despejar el hit-rate implícito:

    pnl_medio = hit*payout - stake*(1+SLIPPAGE)
    hit = (pnl_medio + stake*(1+SLIPPAGE)) / payout

y con ese hit-rate recalcular el PnL con la curva de fee real en vez del
slippage plano. Mismo stake=1€ normalizado, mismo criterio metodológico
que el módulo original -- solo cambia el coste de fricción modelado.

Solo lectura -- no toca ninguna decisión ni gate_bucket_propio.json
existente. Genera data/shadow/ev_fee_real_microbuckets.json.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent
STAKE = 1.0
SLIPPAGE_SHADOW = 0.02
FEE_RATE_REAL = 0.07
STEP = 0.05
OUT = REPO / "data" / "shadow" / "ev_fee_real_microbuckets.json"


def _precio_entrada(bucket_lo: float, decision: str) -> float:
    py_mid = bucket_lo + STEP / 2
    return (1 - py_mid) if decision == "BUY_NO" else py_mid


def main() -> None:
    d = json.loads((REPO / "data/shadow/gate_bucket_propio.json").read_text())
    filas = []
    for tupla_str, buckets in d.items():
        partes = tupla_str.split("#")
        decision = partes[-1]
        for b_str, info in buckets.items():
            if info.get("veredicto") not in ("bueno_confirmado", "malo_confirmado"):
                continue
            pnl_medio = info.get("pnl_medio")
            n = info.get("n", 0)
            if pnl_medio is None or n < 15:
                continue
            try:
                bucket_lo = float(b_str)
            except ValueError:
                continue
            precio = _precio_entrada(bucket_lo, decision)
            if not (0.01 < precio < 0.99):
                continue
            payout = STAKE / precio
            hit = (pnl_medio + STAKE * (1 + SLIPPAGE_SHADOW)) / payout
            if not (0.0 <= hit <= 1.0):
                continue  # reconstrucción fuera de rango válido, descartar (dato inconsistente)
            fee_real = FEE_RATE_REAL * precio * (1 - precio)
            pnl_fee_real = hit * (payout - STAKE) - (1 - hit) * STAKE - fee_real * STAKE
            filas.append({
                "tupla": tupla_str, "bucket": b_str, "n": n,
                "precio_entrada_estimado": round(precio, 4),
                "hit_reconstruido": round(hit, 4),
                "pnl_medio_shadow_slippage_plano": round(pnl_medio, 4),
                "pnl_medio_fee_real": round(pnl_fee_real, 4),
                "diferencia": round(pnl_fee_real - pnl_medio, 4),
                "veredicto_original": info["veredicto"],
            })

    filas.sort(key=lambda x: -x["pnl_medio_fee_real"])
    OUT.write_text(json.dumps(filas, indent=1, ensure_ascii=False), encoding="utf-8")

    print(f"[ev_fee_real_microbuckets] {len(filas)} buckets recalculados -> {OUT}")
    print("\n--- TOP 10 por EV neto de fee REAL ---")
    for f in filas[:10]:
        print(f"{f['pnl_medio_fee_real']:+.3f} (shadow={f['pnl_medio_shadow_slippage_plano']:+.3f}) "
              f"{f['tupla']} [{f['bucket']}] n={f['n']} precio~{f['precio_entrada_estimado']}")

    # cambios de signo: confirmaba positivo con slippage plano pero es negativo con fee real, o viceversa
    cambios_signo = [f for f in filas if (f["pnl_medio_shadow_slippage_plano"] > 0) != (f["pnl_medio_fee_real"] > 0)]
    print(f"\n--- {len(cambios_signo)} buckets CAMBIAN DE SIGNO entre slippage plano y fee real ---")
    for f in cambios_signo[:15]:
        print(f"shadow={f['pnl_medio_shadow_slippage_plano']:+.3f} -> fee_real={f['pnl_medio_fee_real']:+.3f} "
              f"{f['tupla']} [{f['bucket']}] n={f['n']} veredicto_original={f['veredicto_original']}")


if __name__ == "__main__":
    main()
