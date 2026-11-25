#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""salida_dinamica_28oct/extras_sal.py - escala en $ del canal A30, cola bid<=0,02, desglose por moneda y COTA ORACULO.
Reutiliza eval_sal.py (exec silencioso). SOLO LECTURA. Uso: python3 extras_sal.py > extras_sal_salida.txt"""
import io, contextlib, os
HERE = os.path.dirname(os.path.abspath(__file__))
E = {}
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    exec(compile(open(os.path.join(HERE, 'eval_sal.py')).read(), 'eval_sal.py', 'exec'), E)
U = E['U']; fee = E['fee']
ND = len(set(u['dia'] for u in U)); NS = [u for u in U if u['ns']]
cS = sum(u['cost'] for u in U); dS = sum(u['d30'] for u in NS)
print('dias %d | P rellenadas %d (coste %.0f $) | NS %d' % (ND, len(U), cS, len(NS)))
print('A30: Σ Δ = %+.1f $ en %d dias = %+.2f $/dia (escala sim: TODAS las unidades elegibles) | Δ/coste total %+.4f' % (dS, ND, dS / ND, dS / cS))
tail = [u for u in NS if u['x3'][0] <= 0.02]; w = sum(1 for u in tail if u['g'] == 1.0); sq = sum(u['q3'] for u in tail)
dT = sum(u['d30'] for u in tail)
print('cola bid<=0.02 (NS): n=%d ganadoras=%d (%.2f%%) acciones vendidas=%.0f bid medio %.4f | Σ Δ=%+.1f $ (%+.4f €/€ total) | resto NS (bid>0.02): n=%d Σ Δ=%+.1f $' % (
    len(tail), w, 100.0 * w / len(tail), sq, sum(u['x3'][0] for u in tail) / len(tail), dT, dT / cS, len(NS) - len(tail), dS - dT))
print('--- por moneda (A30): ΣΔ $ | n NS | Δ/coste de la moneda')
for c in ('BTC', 'ETH', 'SOL', 'XRP', 'DOGE', 'BNB'):
    Uc = [u for u in U if u['coin'] == c]; Nc = [u for u in Uc if u['ns']]
    print('  %-5s ΣΔ=%+7.1f $  nNS=%4d  nP=%5d  Δ/coste=%+.4f' % (c, sum(u['d30'] for u in Nc), len(Nc), len(Uc), sum(u['d30'] for u in Nc) / sum(u['cost'] for u in Uc)))
loss = [u for u in U if u['g'] == 0.0]
orac = sum(u['sh'] * (0.01 - fee(0.01)) for u in loss)
print('COTA ORACULO (vender TODO perdedor a 0,01 al T-30s, sin ganadoras): %+.4f €/€ (perdedoras %d de %d = %.1f%%)' % (orac / cS, len(loss), len(U), 100.0 * len(loss) / len(U)))
print('A30 captura %.1f%% de esa cota' % (100.0 * dS / orac))
print('precio medio de entrada %.3f ; acierto medio de las rellenadas %.3f' % (sum(u['avg'] for u in U) / len(U), sum(u['g'] for u in U) / len(U)))
