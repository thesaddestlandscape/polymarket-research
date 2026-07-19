"""Chequeo diagnóstico barato (19-Jul, petición Javi tras leer arXiv 2607.09426,
'The Quarter-Hour Effect: Periodic Algorithmic Trading and Return Predictability
in Cryptocurrency Futures', Kim & Hansen): ¿existe en NUESTROS propios datos de
Binance el burst mecánico de volumen/volatilidad en las marcas de cuarto de hora
(:00/:15/:30/:45) que el paper documenta en 2021-2024?

Puramente de lectura -- no escribe nada en data/, no toca ninguna estrategia.
Usa el backfill ya existente en data/backfill/klines/ (~92 días, 26-Mar a
25-Jun-2026, klines 1min con taker_buy_base_volume real de Binance).

Réplica simplificada de dos piezas del paper (NO la Autocorrelation Map
completa, que exige más trabajo):
  1. Burst mecánico: volumen medio y |retorno| medio por minuto-del-reloj
     (0-59), comparando marcas de cuarto de hora vs el resto.
  2. Placebo (grids desplazados 2/17/32/47, igual que el paper) para
     descartar que sea un artefacto de framing.

Uso: python3 analisis_quarter_hour_effect_19jul.py
"""
import json
from collections import defaultdict
from pathlib import Path

DIR = Path(__file__).parent / "data/backfill/klines"
ACTIVOS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
MARCAS_CUARTO = {0, 15, 30, 45}
MARCAS_PLACEBO = {2, 17, 32, 47}


def cargar_klines(activo):
    """Dedup por open_time (los ficheros diarios se solapan ~1 día)."""
    vistos = {}
    for f in sorted(DIR.glob(f"*_{activo}.json")):
        try:
            filas = json.loads(f.read_text())
        except Exception:
            continue
        for k in filas:
            ts = k[0]
            vistos[ts] = k
    return [vistos[ts] for ts in sorted(vistos)]


def analizar(activo):
    klines = cargar_klines(activo)
    n = len(klines)
    if n < 1000:
        print(f"{activo}: solo n={n} klines, insuficiente")
        return

    por_minuto = defaultdict(lambda: {"vol": [], "abs_ret": [], "n_trades": []})
    for k in klines:
        ts_ms, o, h, l, c, vol = k[0], float(k[1]), float(k[2]), float(k[3]), float(k[4]), float(k[5])
        minuto = (ts_ms // 60000) % 60
        abs_ret = abs(c - o) / o if o > 0 else 0.0
        n_trades = k[8] if len(k) > 8 else None
        d = por_minuto[minuto]
        d["vol"].append(vol)
        d["abs_ret"].append(abs_ret)
        if n_trades is not None:
            d["n_trades"].append(n_trades)

    def media(lst):
        return sum(lst) / len(lst) if lst else 0.0

    vol_cuarto = [v for m in MARCAS_CUARTO for v in por_minuto[m]["vol"]]
    vol_resto = [v for m in range(60) if m not in MARCAS_CUARTO for v in por_minuto[m]["vol"]]
    ret_cuarto = [v for m in MARCAS_CUARTO for v in por_minuto[m]["abs_ret"]]
    ret_resto = [v for m in range(60) if m not in MARCAS_CUARTO for v in por_minuto[m]["abs_ret"]]

    vol_placebo = [v for m in MARCAS_PLACEBO for v in por_minuto[m]["vol"]]
    ret_placebo = [v for m in MARCAS_PLACEBO for v in por_minuto[m]["abs_ret"]]

    vol_cuarto_m, vol_resto_m, vol_placebo_m = media(vol_cuarto), media(vol_resto), media(vol_placebo)
    ret_cuarto_m, ret_resto_m, ret_placebo_m = media(ret_cuarto), media(ret_resto), media(ret_placebo)

    print(f"\n=== {activo} (n={n} velas 1min, {n/1440:.0f} días aprox) ===")
    print(f"  Volumen medio:   cuarto-hora={vol_cuarto_m:.4f}  resto={vol_resto_m:.4f}  "
          f"gap={(vol_cuarto_m/vol_resto_m-1)*100:+.1f}%  placebo={(vol_placebo_m/vol_resto_m-1)*100:+.1f}%")
    print(f"  |Retorno| medio: cuarto-hora={ret_cuarto_m:.6f}  resto={ret_resto_m:.6f}  "
          f"gap={(ret_cuarto_m/ret_resto_m-1)*100:+.1f}%  placebo={(ret_placebo_m/ret_resto_m-1)*100:+.1f}%")

    # Desglose por marca individual (0,15,30,45) vs vecinos inmediatos
    print(f"  Por marca individual (vol / |ret|) vs media de resto (vol={vol_resto_m:.4f} ret={ret_resto_m:.6f}):")
    for m in sorted(MARCAS_CUARTO):
        vm = media(por_minuto[m]["vol"])
        rm = media(por_minuto[m]["abs_ret"])
        print(f"    minuto={m:>2}: vol={vm:.4f} ({(vm/vol_resto_m-1)*100:+.1f}%)  "
              f"|ret|={rm:.6f} ({(rm/ret_resto_m-1)*100:+.1f}%)")

    return {
        "activo": activo, "n": n,
        "vol_gap_pct": (vol_cuarto_m/vol_resto_m-1)*100 if vol_resto_m else None,
        "ret_gap_pct": (ret_cuarto_m/ret_resto_m-1)*100 if ret_resto_m else None,
        "vol_placebo_pct": (vol_placebo_m/vol_resto_m-1)*100 if vol_resto_m else None,
        "ret_placebo_pct": (ret_placebo_m/ret_resto_m-1)*100 if ret_resto_m else None,
    }


def main():
    resultados = []
    for activo in ACTIVOS:
        r = analizar(activo)
        if r:
            resultados.append(r)

    print("\n\n=== RESUMEN (gap cuarto-hora vs resto, y placebo de control) ===")
    print(f"{'activo':<6} {'n':>8} {'vol_gap%':>10} {'ret_gap%':>10} {'vol_placebo%':>14} {'ret_placebo%':>14}")
    for r in resultados:
        print(f"{r['activo']:<6} {r['n']:>8} {r['vol_gap_pct']:>9.1f}% {r['ret_gap_pct']:>9.1f}% "
              f"{r['vol_placebo_pct']:>13.1f}% {r['ret_placebo_pct']:>13.1f}%")


if __name__ == "__main__":
    main()
