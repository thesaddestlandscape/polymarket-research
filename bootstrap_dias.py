#!/usr/bin/env python3
"""bootstrap_dias.py -- (28-Sep, /code-review: extraído de wallet_first_buy_
fwd_tracker.py y buscador_grietas_polymarket.py, que tenían la MISMA función
duplicada byte a byte -- un fix al percentil/lógica de bootstrap en una copia
sin tocar la otra las habría dejado divergir en silencio). Único punto de
verdad para bootstrap IC90 por días en todo el proyecto."""
import random


def bootstrap_ic90_dias(por_dia: dict, iters: int = 1000, seed: int = 5) -> list | None:
    """IC90 bootstrap por DÍAS (nunca por fila -- evita pseudo-replicación
    dentro del mismo día). `por_dia`: {dia: [valor, ...]}. None si hay <2
    días (bootstrap sin sentido con tan poca base)."""
    dias_vals = list(por_dia.values())
    if len(dias_vals) < 2:
        return None
    rng = random.Random(seed)
    medias = []
    for _ in range(iters):
        muestra = [rng.choice(dias_vals) for _ in dias_vals]
        todos = [x for dv in muestra for x in dv]
        if todos:
            medias.append(sum(todos) / len(todos))
    if not medias:
        return None
    medias.sort()
    lo = medias[int(len(medias) * 0.05)]
    hi = medias[min(int(len(medias) * 0.95), len(medias) - 1)]
    return [round(lo, 4), round(hi, 4)]
