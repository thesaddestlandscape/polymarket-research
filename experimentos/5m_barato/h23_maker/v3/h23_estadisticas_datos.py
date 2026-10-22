#!/usr/bin/env python3
"""h23_estadisticas_datos.py -- estadisticas de la CELDA PRIMARIA del replay v3 por moneda y brazo, PARTIDAS por calidad de transporte del cierre (22-Oct-2026). SOLO LECTURA.
Celda primaria (PREREGISTRO §3): cola base, alta 79, cancel 60, tamano real, un relleno cierra. Reps r150 y r1500 (placebo). Estados: `todos`, `limpios` (ningun hueco de coin#5min/15min en
[C-305 s, C-10 s] segun h23_huecos_ws) y `con_hueco` (relleno DUDOSO: estado del libro obsoleto). Mismas funciones estadisticas que el vigia h23_repuja (resumen_pos: EV ponderado por EUR,
por unidad, sin 2 mejores dias, IC90 por dias solo con >=5 dias). Etiquetas: no declara nada rentable. Uso: python3 -I h23_estadisticas_datos.py --monedas BTC,ETH --dias 2026-10-19:2026-10-21 [--json F]"""
import argparse, csv, json, os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import h23_huecos_ws as H
import h23_job_replay as J
import vigia_h23_repuja as V

OUT = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3/'


def cargar(coins, dias, out=OUT, ledger=None):
    led = ledger if ledger is not None else H.cargar()
    pos = defaultdict(list)          # (coin, brazo, rep, estado) -> [pos]
    cob = defaultdict(lambda: dict(cotizados=0, con_libro=0, dias=0, sin_desenlace=0))
    for c in coins:
        for D in dias:
            f, fc = out + f'v3_{c}_{D}.csv', out + f'v3_cobertura_{c}_{D}.json'
            if not (os.path.exists(f) and os.path.exists(fc)):
                continue
            cl = H.clasificar(c, D, led) if led else {}
            cj = json.load(open(fc))
            cob[c]['dias'] += 1; cob[c]['con_libro'] += cj['con_libro']; cob[c]['sin_desenlace'] += cj['sin_desenlace']
            with open(f, newline='') as fh:
                for r in csv.DictReader(fh):
                    if r['sizing'] != 'real' or r['modo'] != 'primer' or r['cola'] != 'base' or r['lat_post'] != '79' or r['lat_cancel'] != '60' or r['rep'] not in ('150', '1500', '0'):
                        continue
                    C = int(r['cierre'])
                    if r['rep'] == '150' and r['n_cotiz'] != '0':
                        cob[c]['cotizados'] += 1 if r['brazo'] == 'A' else 0
                    lleno = float(r['lleno'])
                    if lleno <= 0:
                        continue
                    g = {'True': 1.0, 'False': 0.0}.get(r['gana'])
                    if g is None:
                        cob[c]['sin_desenlace_fills'] = cob[c].get('sin_desenlace_fills', 0) + 1
                        continue
                    coste = float(r['coste'])
                    p = dict(dia=D, cierre=C, lleno=lleno, coste=coste, g=g, pnl=lleno * g - coste + float(r['rebate']))
                    est = cl.get(C, 'sin_ledger')
                    for e in ('todos', 'limpios' if est == 'limpio' else 'con_hueco'):
                        pos[(c, r['brazo'], int(r['rep']), e)].append(p)
    return pos, cob


def fila(k, v):
    s = V.resumen_pos(v)
    if not s.get('n'):
        return f'{k}: n=0'
    f = lambda x, d=3: 'NA' if x is None else f'{x:+.{d}f}'
    return (f"{k}: n={s['n']} dias={s['dias']}({s['dias_pos']}+) EV_pond={f(s['ev_pond'])} EV_unit={f(s['ev_unit'])} sin2mejores={f(s['sin2'])} "
            f"IC90_dias=({f(s['ic_lo'], 2)};{f(s['ic_hi'], 2)}) acierto={s['acierto']:.2f} PnL={s['pnl']:+.2f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--monedas', default='BTC'); ap.add_argument('--dias', required=True); ap.add_argument('--json', default=None)
    ap.add_argument('--reps', default='150,1500'); ap.add_argument('--estados', default='todos,limpios,con_hueco')
    a = ap.parse_args()
    coins, dias = a.monedas.split(','), J.rangos(a.dias)
    pos, cob = cargar(coins, dias)
    reps, ests = [int(x) for x in a.reps.split(',')], a.estados.split(',')
    res = {}
    for c in coins:
        print(f'## {c}  dias con replay {cob[c]["dias"]}/{len(dias)}  cierres con libro {cob[c]["con_libro"]}  fills sin desenlace (missing, excluidos) {cob[c].get("sin_desenlace_fills", 0)}')
        for b in 'AB':
            for rep in reps:
                for e in ests:
                    v = pos.get((c, b, rep, e), [])
                    print('  ' + fila(f'{b} r{rep} {e}', v))
                    res[f'{c}|{b}|r{rep}|{e}'] = V.resumen_pos(v)
    # agregado ALTS5
    alts = [c for c in coins if c != 'BTC']
    if len(alts) > 1:
        print(f'## ALTS ({",".join(alts)}) agrupadas')
        for b in 'AB':
            for rep in reps:
                for e in ests:
                    v = [p for c in alts for p in pos.get((c, b, rep, e), [])]
                    print('  ' + fila(f'ALTS {b} r{rep} {e}', v))
                    res[f'ALTS|{b}|r{rep}|{e}'] = V.resumen_pos(v)
    if a.json:
        json.dump(res, open(a.json, 'w'), indent=1, default=float)
    return 0


if __name__ == '__main__':
    sys.exit(main())
