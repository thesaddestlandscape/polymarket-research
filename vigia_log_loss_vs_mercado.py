#!/usr/bin/env python3
"""Vigía (17-Jul, punto 6 de la lista Shannon del checkpoint del mismo día):
¿el log-loss de nuestro modelo (prob_yes_modelo) es REALMENTE mejor que el
log-loss implícito de solo confiar en el precio de mercado (precio_yes_
mercado como probabilidad)? Si no lo es, el "modelo" no añade calibración
por encima de lo que el propio mercado ya sabe -- red flag barata que
complementa IC/hit-rate (que miden DIRECCIÓN, no CALIBRACIÓN de la
confianza).

results.csv ya guarda nuestro log_loss por fila (shadow_resolve.py::
_log_loss, usa prob_yes_modelo). Este vigía recalcula el mismo log-loss
usando precio_yes_mercado como "p" en su lugar (mismo fórmula exacta,
reutilizada) y compara medias por estrategia -- n>=15 (regla del proyecto),
persiste a JSON, avisa por Telegram (con latch, sin repetir) si alguna
estrategia lleva su propio log-loss PEOR que el del mercado.

Solo lectura sobre results.csv. No toca dinero ni config. Pensado para
cron ligero (una pasada de results.csv, sin llamadas de red).
"""
import csv
import json
import math
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data" / "shadow" / "results.csv"
OUT = REPO / "data" / "shadow" / "log_loss_vs_mercado.json"
LATCH = REPO / "data" / "shadow" / "vigia_log_loss_latch.json"
N_MIN = 15  # regla del proyecto: ninguna conclusión con n<15


def _log_loss(p: float, outcome_yes: bool) -> float:
    """Misma fórmula exacta que shadow_resolve.py::_log_loss -- reutilizada,
    no reinventada, solo parametrizada por 'p' en vez de leerlo de prob_yes_modelo."""
    p = min(max(p, 1e-9), 1 - 1e-9)
    o = 1.0 if outcome_yes else 0.0
    return -(o * math.log(p) + (1 - o) * math.log(1 - p))


def cargar_pares() -> dict:
    """clave (strategy) -> lista de (ll_modelo, ll_mercado) por fila resuelta."""
    pares = {}
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("outcome_real") not in ("YES", "NO"):
                continue
            try:
                p_modelo = float(r.get("prob_yes_modelo", "") or "nan")
                p_mercado = float(r.get("precio_yes_mercado", "") or "nan")
            except ValueError:
                continue
            if not (0.0 < p_modelo < 1.0) or not (0.0 < p_mercado < 1.0):
                continue
            outcome_yes = r["outcome_real"] == "YES"
            ll_m = _log_loss(p_modelo, outcome_yes)
            ll_mkt = _log_loss(p_mercado, outcome_yes)
            pares.setdefault(r["strategy"], []).append((ll_m, ll_mkt))
    return pares


def main():
    pares = cargar_pares()
    try:
        latch = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        latch = {}

    resultado = {}
    avisos = []
    for strategy, filas in sorted(pares.items()):
        n = len(filas)
        if n < N_MIN:
            continue
        ll_modelo_medio = sum(f[0] for f in filas) / n
        ll_mercado_medio = sum(f[1] for f in filas) / n
        peor_que_mercado = ll_modelo_medio >= ll_mercado_medio
        resultado[strategy] = {
            "n": n, "log_loss_modelo": round(ll_modelo_medio, 4),
            "log_loss_mercado": round(ll_mercado_medio, 4),
            "gap": round(ll_mercado_medio - ll_modelo_medio, 4),  # positivo = modelo mejor
            "peor_que_mercado": peor_que_mercado,
        }
        if peor_que_mercado and not latch.get(strategy):
            avisos.append(f"{strategy}: log_loss modelo={ll_modelo_medio:.4f} >= "
                           f"mercado={ll_mercado_medio:.4f} (n={n}) -- el modelo NO calibra "
                           f"mejor que el precio de mercado")
            latch[strategy] = True
        elif not peor_que_mercado:
            latch[strategy] = False

    OUT.write_text(json.dumps({"estrategias": resultado}, indent=2, ensure_ascii=False), encoding="utf-8")
    LATCH.write_text(json.dumps(latch, indent=1, ensure_ascii=False), encoding="utf-8")

    if avisos:
        try:
            from shadow_digest import enviar_telegram
            msg = ("📉 VIGÍA log-loss: modelo peor calibrado que el precio de mercado\n"
                   + "\n".join(f"  {a}" for a in avisos)
                   + "\nNo mide dirección (eso ya lo hace IC) -- mide si la CONFIANZA del "
                     "modelo está bien calibrada. No implica desactivar nada por sí solo.")
            ok = enviar_telegram(msg)
            print(f"[vigia_log_loss] {len(avisos)} aviso(s) nuevo(s), telegram={ok}")
        except Exception as e:
            print(f"[vigia_log_loss] no se pudo notificar Telegram: {e}")
    else:
        print("[vigia_log_loss] sin novedades")

    print(f"[vigia_log_loss] {len(resultado)} estrategias con n>={N_MIN}, guardado en {OUT}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_log_loss] ERROR {type(e).__name__}: {e}")
        sys.exit(1)
