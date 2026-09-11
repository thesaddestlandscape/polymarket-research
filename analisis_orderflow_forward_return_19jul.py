"""Parte 2 de arXiv 2607.09426 (Kim & Hansen): ¿el desequilibrio de orden
(order imbalance, == nuestro delta_ratio ya existente) medido justo tras la
apertura de una marca de hora/cuarto-hora predice el retorno de las
siguientes 4-12h? Réplica sobre datos propios (backfill klines, 92 días
26-Mar a 25-Jun-2026), no los de Binance 2021-2024 del paper.

Metodología: para cada marca de reloj (0/15/30/45), calcular delta_ratio
con las primeras 5 velas 1min tras la marca (mismo patrón que
s_order_flow_5m en shadow_predict.py: cum_delta = sum(2*taker_buy - vol),
normalizado por volumen total), y correlacionarlo con el retorno forward
a 4h y 12h desde ese punto. Shuffle test (1000 permutaciones) antes de
concluir nada -- mismo rigor que el resto del proyecto
(feedback_shuffle_antes_de_bloquear).

Puramente de lectura -- no escribe nada en data/, no toca ninguna estrategia.
Uso: python3 analisis_orderflow_forward_return_19jul.py
"""
import json
import random
from pathlib import Path

DIR = Path(__file__).parent / "data/backfill/klines"
ACTIVOS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
MARCAS = [0, 15, 30, 45]
HORIZONTES_MIN = {"4h": 240, "12h": 720}
N_VELAS_IMBALANCE = 5
N_SHUFFLE = 1000


def cargar_klines(activo):
    vistos = {}
    for f in sorted(DIR.glob(f"*_{activo}.json")):
        try:
            filas = json.loads(f.read_text())
        except Exception:
            continue
        for k in filas:
            vistos[k[0]] = k
    ts_ordenados = sorted(vistos)
    return ts_ordenados, vistos


def analizar(activo):
    ts_ordenados, klines_por_ts = cargar_klines(activo)
    n_total = len(ts_ordenados)
    if n_total < 5000:
        print(f"{activo}: insuficiente ({n_total})")
        return None
    idx_por_ts = {ts: i for i, ts in enumerate(ts_ordenados)}

    resultados = {"4h": [], "12h": []}  # (imbalance, fwd_return)

    for i, ts in enumerate(ts_ordenados):
        minuto = (ts // 60000) % 60
        if minuto not in MARCAS:
            continue
        # Order imbalance con las N_VELAS_IMBALANCE velas desde ts
        if i + N_VELAS_IMBALANCE > n_total:
            continue
        velas_imb = ts_ordenados[i:i + N_VELAS_IMBALANCE]
        if len(velas_imb) < N_VELAS_IMBALANCE:
            continue
        cum_delta = 0.0
        total_vol = 0.0
        ok = True
        for vts in velas_imb:
            k = klines_por_ts[vts]
            try:
                vol = float(k[5])
                taker_buy = float(k[9]) if len(k) > 9 else vol / 2
            except (ValueError, TypeError, IndexError):
                ok = False
                break
            total_vol += vol
            cum_delta += 2 * taker_buy - vol
        if not ok or total_vol <= 0:
            continue
        imbalance = cum_delta / total_vol
        precio_ref = float(klines_por_ts[ts][1])  # open de la vela en la marca

        for horiz, minutos in HORIZONTES_MIN.items():
            ts_fwd = ts + minutos * 60000
            if ts_fwd not in idx_por_ts:
                continue
            precio_fwd = float(klines_por_ts[ts_fwd][1])
            ret_fwd = (precio_fwd - precio_ref) / precio_ref
            resultados[horiz].append((imbalance, ret_fwd))

    return resultados


def correlacion(pares):
    n = len(pares)
    if n < 2:
        return None, n
    mx = sum(p[0] for p in pares) / n
    my = sum(p[1] for p in pares) / n
    cov = sum((x - mx) * (y - my) for x, y in pares) / n
    vx = sum((x - mx) ** 2 for x, y in pares) / n
    vy = sum((y - my) ** 2 for x, y in pares) / n
    if vx <= 0 or vy <= 0:
        return None, n
    return cov / (vx ** 0.5 * vy ** 0.5), n


def shuffle_pvalue(pares, r_obs, n_shuffle=N_SHUFFLE, seed=19):
    rnd = random.Random(seed)
    ys = [p[1] for p in pares]
    xs = [p[0] for p in pares]
    n = len(pares)
    if n < 2:
        return None
    conteo = 0
    for _ in range(n_shuffle):
        ys_shuf = ys[:]
        rnd.shuffle(ys_shuf)
        r_s, _ = correlacion(list(zip(xs, ys_shuf)))
        if r_s is not None and abs(r_s) >= abs(r_obs):
            conteo += 1
    return conteo / n_shuffle


def main():
    print(f"Marcas testeadas: {MARCAS} | ventana imbalance: {N_VELAS_IMBALANCE}min | horizontes: {list(HORIZONTES_MIN)}")
    resumen = []
    for activo in ACTIVOS:
        res = analizar(activo)
        if not res:
            continue
        print(f"\n=== {activo} ===")
        for horiz in HORIZONTES_MIN:
            pares = res[horiz]
            r, n = correlacion(pares)
            if r is None:
                print(f"  {horiz}: sin datos suficientes (n={n})")
                continue
            p = shuffle_pvalue(pares, r)
            print(f"  {horiz}: n={n:>5}  corr(imbalance, retorno_fwd)={r:+.4f}  p_shuffle={p:.4f}")
            resumen.append((activo, horiz, n, r, p))

    print("\n\n=== RESUMEN ===")
    print(f"{'activo':<6} {'horiz':<5} {'n':>6} {'corr':>8} {'p_shuffle':>10}")
    for activo, horiz, n, r, p in resumen:
        sig = "***" if p < 0.01 else ("*" if p < 0.05 else "")
        print(f"{activo:<6} {horiz:<5} {n:>6} {r:>+.4f} {p:>10.4f} {sig}")


if __name__ == "__main__":
    main()
