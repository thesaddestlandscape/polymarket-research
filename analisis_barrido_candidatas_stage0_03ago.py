#!/usr/bin/env python3
"""
analisis_barrido_candidatas_stage0_03ago.py — barrido de las 271
candidatos_evaluacion_live: ¿cuáles ya cruzan los gates estándar
(n>=40, IC>=0.08) y tienen ya cobertura de fill-ability real
(libro_snapshots.csv) para poder evaluarse en serio?

Petición Javi 03-Ago: avanzar Stage 0 (cerrar gap modelo-realidad) barriendo
candidatas listas para cruzar el gate, no solo dejarlas acumular sin mirar.

Solo lectura.
"""
import csv
import json
from collections import defaultdict

CONFIG = json.load(open("data/live/config_live.json"))
CANDIDATOS = CONFIG.get("candidatos_evaluacion_live", [])
PARES_LIVE = set(CONFIG.get("pares_permitidos_live", []))

params = json.load(open("data/shadow/strategy_params.json")).get("estrategias", {})


def _split(tupla):
    partes = tupla.split("#")
    return partes[0], "#".join(partes[1:-1]), partes[-1]


def ic_n_de(tupla):
    """03-Ago, bug real cazado y corregido: la versión anterior caía a
    params.get(strategy) (agregado BASE de toda la estrategia, todas las
    monedas/marcos mezclados) cuando la clave exacta subtype no existía --
    eso atribuyó n=6845-8159 de FAVORITO_CONFIRMADO#BTC/ETH/SOL/... a
    'FAVORITO_CONFIRMADO#DOGE#240min', un subtype que NUNCA aparece en
    results.csv (confirmado: DOGE solo tiene datos reales en 5min/15min).
    Ahora exige la clave EXACTA (strategy#subtype) -- si no existe, no hay
    dato propio, se descarta en vez de inventar con el agregado."""
    strategy, subtype, direction = _split(tupla)
    clave = f"{strategy}#{subtype}"
    e = params.get(clave)
    if e is None:
        return None, None
    dec_suf = direction  # "BUY_YES"/"BUY_NO"
    n = e.get(f"n_{dec_suf}")
    ic = e.get(f"ic_{dec_suf}")
    return ic, n


# cobertura de libro_snapshots.csv por tupla exacta
cobertura_libro = defaultdict(int)
with open("data/live/libro_snapshots.csv", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        key = f"{r.get('strategy')}#{r.get('subtype')}#{r.get('direction')}"
        cobertura_libro[key] += 1


listos = []
cerca = []
for t in CANDIDATOS:
    if t in PARES_LIVE:
        continue
    ic, n = ic_n_de(t)
    if ic is None or n is None:
        continue
    n_libro = cobertura_libro.get(t, 0)
    if n >= 40 and ic >= 0.08:
        listos.append((t, ic, n, n_libro))
    elif n >= 25 and ic >= 0.05:
        cerca.append((t, ic, n, n_libro))

listos.sort(key=lambda x: -x[1])
cerca.sort(key=lambda x: -x[2])

print(f"=== LISTAS: n>=40, IC>=0.08 ({len(listos)}) — candidatas a evaluar YA con rigor completo ===")
for t, ic, n, nl in listos:
    print(f"  {t:<65} IC={ic:+.3f} n={n:>5} libro_snapshots_n={nl}")

print(f"\n=== CERCA: n>=25, IC>=0.05 ({len(cerca)}) — vigilar, no concluir ===")
for t, ic, n, nl in cerca[:20]:
    print(f"  {t:<65} IC={ic:+.3f} n={n:>5} libro_snapshots_n={nl}")
