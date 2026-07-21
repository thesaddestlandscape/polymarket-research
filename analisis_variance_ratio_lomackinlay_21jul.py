#!/usr/bin/env python3
"""Test de razón de varianzas (Lo & MacKinlay 1988, "Stock Market Prices
Do Not Follow Random Walks") sobre BTC/ETH/SOL/XRP -- ¿hay momentum
(VR>1) o mean-reversion (VR<1) sistemático por horizonte (5/15/60/240min),
de forma rigurosa, en vez del patchwork actual descubierto estrategia por
estrategia (STREAK_FADE_15M, STREAK_MOM_5M, H-DRIFT15-MOMENTUM, etc.)?

Origen (21-Jul): artículo externo sobre los "6 papers fundacionales" de
las quant funds -- de los 6, este es el único que el proyecto no tenía
ya integrado (Shannon~IC, Kelly~live_stake, Black-Scholes~_gbm_p_up,
Markowitz~idea HRP aparcada, Mandelbrot~gate de Kelly log-growth ya
gestiona colas gordas). Ver idea_variance_ratio_test_lomackinlay_21jul.md.

Datos: data/backfill/klines/ (~92 días, 26-Mar a 25-Jun-2026, klines 1min
reales de Binance -- mismo store ya usado por analisis_quarter_hour_
effect_19jul.py y analisis_orderflow_forward_return_19jul.py, mismo
cargar_klines() reusado tal cual). Puramente de lectura, no toca dinero
ni ninguna estrategia -- shadow research puro.

Metodología: VR(q) = 1 + 2*sum_{k=1}^{q-1} (1-k/q)*rho(k), rho(k) =
autocorrelación de retornos log a 1min en el lag k (formulación
algebraicamente equivalente a la razón de varianzas directa de Lo-
MacKinlay, más simple de implementar sin bugs de solapamiento). Dos
estadísticos z: homoscedástico (asume varianza constante, fórmula
clásica) y robusto a heteroscedasticidad (Lo-MacKinlay 1988, ecuación
2.9-2.10 del paper original -- el que corresponde de verdad a datos
financieros con clusters de volatilidad, ver Mandelbrot). Autotest sobre
series sintéticas (random walk / AR(1) reversión / AR(1) momentum) ANTES
de confiar en el resultado real -- un test estadístico mal implementado
puede "confirmar" estructura que no existe.

Uso: python3 analisis_variance_ratio_lomackinlay_21jul.py
"""
import json
from pathlib import Path

import numpy as np

DIR = Path(__file__).parent / "data/backfill/klines"
ACTIVOS = ["BTC", "ETH", "SOL", "XRP"]  # los 4 que operamos; DOGE/BNB fuera de alcance hoy
HORIZONTES_MIN = [5, 15, 60, 240]        # los marcos reales del proyecto
N_MIN_BLOQUES = 30                       # regla del proyecto (n>=15), doblada por ser un test asintótico


def cargar_klines(activo: str) -> list:
    """Dedup por open_time (los ficheros diarios se solapan ~1 día) --
    idéntico a analisis_quarter_hour_effect_19jul.py::cargar_klines, reusado
    tal cual (mismo store, mismo formato)."""
    vistos = {}
    for f in sorted(DIR.glob(f"*_{activo}.json")):
        try:
            filas = json.loads(f.read_text())
        except Exception:
            continue
        for k in filas:
            vistos[k[0]] = k
    return [vistos[ts] for ts in sorted(vistos)]


def log_returns_1min(klines: list) -> np.ndarray:
    """Retornos log de cierre-a-cierre a 1min, exigiendo continuidad real
    (gap de 60000ms exacto entre klines consecutivos) -- un hueco de datos
    (caída de Binance, mantenimiento) rompería el supuesto de muestreo
    regular del test si no se filtra."""
    closes, gaps_ok = [], []
    prev_ts = None
    for k in klines:
        ts, c = k[0], float(k[4])
        if prev_ts is not None and ts - prev_ts != 60000:
            gaps_ok.append(False)
        else:
            gaps_ok.append(True)
        closes.append(c)
        prev_ts = ts
    closes = np.array(closes)
    log_p = np.log(closes)
    r = np.diff(log_p)
    # Un retorno es inválido si CUALQUIERA de los dos precios que lo forman
    # venía tras un hueco (gaps_ok[i] corresponde al precio i, no al retorno).
    valido = np.array(gaps_ok[1:])
    r_validos = r[valido]
    return r_validos, len(r) - len(r_validos)


def variance_ratio(r: np.ndarray, q: int) -> dict:
    """VR(q) vía autocorrelaciones (Lo-MacKinlay 1988, forma equivalente a
    su cálculo directo de varianzas solapadas -- ver Lo & MacKinlay,
    Review of Financial Studies 1988, ecuación 2.6). z homoscedástico
    (ec. 2.8) y robusto a heteroscedasticidad (ec. 2.9-2.10)."""
    T = len(r)
    r_c = r - r.mean()
    var_r = np.sum(r_c**2) / T  # varianza muestral (denominador T, no T-1, consistente con el paper)

    rhos = []
    for k in range(1, q):
        num = np.sum(r_c[k:] * r_c[:-k])
        rho_k = num / (T * var_r)
        rhos.append(rho_k)
    vr = 1 + 2 * sum((1 - k / q) * rho for k, rho in zip(range(1, q), rhos))

    # Homoscedástico
    theta = (2 * (2 * q - 1) * (q - 1)) / (3 * q * T)
    z_homo = (vr - 1) / np.sqrt(theta) if theta > 0 else np.nan

    # Robusto a heteroscedasticidad (delta_k pondera por el producto de
    # varianzas locales, no asume varianza constante -- crucial en cripto,
    # ver Mandelbrot/colas gordas). delta_k es O(1) (sin escalar por T) por
    # construcción -- el estadístico correcto lleva el factor sqrt(T) FUERA
    # (Lo-MacKinlay 1988: z*(q) = sqrt(nq)*[VR(q)-1]/sqrt(theta*(q))), no
    # dentro de theta_star. BUG real cazado por el autotest de abajo (21-Jul):
    # la primera versión omitía ese sqrt(T), dando z_robusto~0 siempre
    # (el estadístico nunca podía alejarse de cero por mucha estructura real
    # que hubiera) -- exactamente el tipo de fallo silencioso que el autotest
    # con series sintéticas de propiedad conocida existe para cazar.
    denom_delta = np.sum(r_c**2) ** 2
    theta_star = 0.0
    for k in range(1, q):
        delta_k = (T * np.sum((r_c[k:] ** 2) * (r_c[:-k] ** 2))) / denom_delta
        theta_star += (2 * (q - k) / q) ** 2 * delta_k
    z_robusto = np.sqrt(T) * (vr - 1) / np.sqrt(theta_star) if theta_star > 0 else np.nan

    return {"vr": vr, "z_homo": z_homo, "z_robusto": z_robusto, "n": T}


def _p_valor_normal(z: float) -> float:
    """P-valor a dos colas de una normal estándar -- sin dependencia de
    scipy (no está en requirements), vía la función de error de math."""
    import math
    return 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))


def autotest():
    """Valida la implementación contra 3 series sintéticas de propiedad
    CONOCIDA antes de confiar en el resultado real -- mismo principio que
    el resto del proyecto (verificar antes de concluir). Semilla fija para
    reproducibilidad."""
    rng = np.random.default_rng(42)
    n = 50_000
    print("=== AUTOTEST (series sintéticas, propiedad conocida) ===")

    # 1. Random walk puro (ruido blanco i.i.d.) -- se espera VR~1, z NO significativo
    r_rw = rng.normal(0, 0.001, n)
    res = variance_ratio(r_rw, q=15)
    print(f"Random walk puro   (q=15): VR={res['vr']:.4f} z_robusto={res['z_robusto']:+.2f} "
          f"p={_p_valor_normal(res['z_robusto']):.3f} "
          f"{'✅ VR~1, no significativo (esperado)' if abs(res['vr']-1) < 0.05 and abs(res['z_robusto']) < 2 else '❌ FALLO'}")

    # 2. AR(1) con phi negativo fuerte -- mean-reversion, se espera VR<1 y z muy negativo
    phi = -0.15
    r_mr = np.zeros(n)
    eps = rng.normal(0, 0.001, n)
    for i in range(1, n):
        r_mr[i] = phi * r_mr[i - 1] + eps[i]
    res = variance_ratio(r_mr, q=15)
    print(f"AR(1) phi={phi:+.2f}  (q=15): VR={res['vr']:.4f} z_robusto={res['z_robusto']:+.2f} "
          f"p={_p_valor_normal(res['z_robusto']):.3f} "
          f"{'✅ VR<1, muy significativo (esperado)' if res['vr'] < 0.9 and res['z_robusto'] < -5 else '❌ FALLO'}")

    # 3. AR(1) con phi positivo -- momentum, se espera VR>1 y z muy positivo
    phi = 0.15
    r_mom = np.zeros(n)
    eps = rng.normal(0, 0.001, n)
    for i in range(1, n):
        r_mom[i] = phi * r_mom[i - 1] + eps[i]
    res = variance_ratio(r_mom, q=15)
    print(f"AR(1) phi={phi:+.2f}  (q=15): VR={res['vr']:.4f} z_robusto={res['z_robusto']:+.2f} "
          f"p={_p_valor_normal(res['z_robusto']):.3f} "
          f"{'✅ VR>1, muy significativo (esperado)' if res['vr'] > 1.1 and res['z_robusto'] > 5 else '❌ FALLO'}")
    print()


def main():
    autotest()

    print("=== RESULTADO REAL (data/backfill/klines, ~92 días, 26-Mar a 25-Jun-2026) ===\n")
    for activo in ACTIVOS:
        klines = cargar_klines(activo)
        if len(klines) < 1000:
            print(f"{activo}: solo {len(klines)} klines, insuficiente -- saltando")
            continue
        r, n_gaps = log_returns_1min(klines)
        print(f"--- {activo} (n_klines={len(klines)}, n_retornos_validos={len(r)}, "
              f"descartados por hueco={n_gaps}) ---")
        for q in HORIZONTES_MIN:
            n_bloques = len(r) // q
            if n_bloques < N_MIN_BLOQUES:
                print(f"  {q:>4}min: n_bloques={n_bloques} < {N_MIN_BLOQUES} -- NO CONCLUYENTE, insuficiente")
                continue
            res = variance_ratio(r, q)
            p = _p_valor_normal(res["z_robusto"])
            if p >= 0.05:
                veredicto = "sin estructura (no se rechaza random walk)"
            elif res["vr"] > 1:
                veredicto = "🔵 MOMENTUM (VR>1, significativo)"
            else:
                veredicto = "🟠 MEAN-REVERSION (VR<1, significativo)"
            print(f"  {q:>4}min: VR={res['vr']:.4f}  z_homo={res['z_homo']:+6.2f}  "
                  f"z_robusto={res['z_robusto']:+6.2f}  p={p:.4f}  n_bloques={n_bloques}  → {veredicto}")
        print()


if __name__ == "__main__":
    main()
