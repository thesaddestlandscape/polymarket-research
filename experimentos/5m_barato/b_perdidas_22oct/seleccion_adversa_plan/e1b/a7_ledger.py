#!/usr/bin/env python3
"""a7_ledger.py [--desde 2026-10-20] [--json] -- A7 del ADDENDUM_E1b (DESCRIPTIVO, no puerta; SOLO LECTURA del ledger de B y de unidades_b.csv).
Por dia UTC: cancelaciones (intencion_cancel), repegas hacia abajo / arriba (objetivo < de), cancela_banda, errores 429 y rechazos, y rellenos reales de B con y sin tras_cancel
(precio del primer relleno, acierto, EV por EUR). Responde: (1) ¿B ya re-puja mas barato? (2) ¿cuantas cancelaciones/hora hace hoy y cuantos 429 aparecen? (S1 anadiria cancelaciones)."""
import sys, os, json, collections
import pandas as pd

LEDGER = '/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl'
UB0 = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'salida', 'datos', 'unidades_b.csv'))
UB = os.environ.get('E1B_DIR', '/root/polymarket-research-datalogs/e1b/').rstrip('/') + '/unidades_b.csv'
UB = UB if os.path.exists(UB) else UB0


def ledger_por_dia(desde):
    C = collections.defaultdict(collections.Counter); horas = collections.defaultdict(set)
    for l in open(LEDGER):
        try: d = json.loads(l)
        except Exception: continue
        dia = str(d.get('ts', ''))[:10]
        if dia < desde: continue
        t = d.get('tipo'); C[dia][t] += 1; horas[dia].add(str(d.get('ts', ''))[11:13])
        if t == 'repega' and d.get('objetivo') is not None and d.get('de') is not None: C[dia]['repega_abajo' if d['objetivo'] < d['de'] else 'repega_arriba_o_igual'] += 1
        if '429' in l and ('status_code=429' in l): C[dia]['n_429'] += 1
    return {d: {**{k: C[d][k] for k in ('intencion_cancel', 'cancel_lat', 'repega', 'repega_abajo', 'repega_arriba_o_igual', 'cancela_banda', 'post_rechazada', 'n_429', 'relleno_tardio', 'intencion_post')},
                'horas_con_actividad': len(horas[d]), 'cancel_por_hora_activa': round(C[d]['intencion_cancel'] / max(len(horas[d]), 1), 1)} for d in sorted(C)}


def rellenos(desde):
    if not os.path.exists(UB): return None
    U = pd.read_csv(UB); U = U[U.dia >= desde]; out = {}
    for tc, g in U.groupby(U.tras_cancel.fillna(False).astype(bool)):
        out['tras_cancel' if tc else 'sin_tras_cancel'] = {'n': len(g), 'precio_primer_relleno': float(g.p_fill.mean()), 'acierto': float(g.gana.mean()),
                                                           'ev_por_eur': float(g.pnl.sum() / g.coste.sum()), 'pnl': float(g.pnl.sum())}
    return out


if __name__ == '__main__':
    desde = sys.argv[sys.argv.index('--desde') + 1] if '--desde' in sys.argv else '2026-10-20'
    r = {'ledger_por_dia': ledger_por_dia(desde), 'rellenos_reales_B': rellenos(desde)}
    print(json.dumps(r, indent=1, default=float))
