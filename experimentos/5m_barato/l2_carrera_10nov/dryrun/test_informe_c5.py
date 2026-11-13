#!/usr/bin/env python3
"""Tests de informe_c5_cxb60.py (C5). python3 -I test_informe_c5.py  (sintetico en tmp; sin red; no toca el datalog real)
I1 definiciones a mano: colocaciones (con y sin relleno), P(fill), EV incondicional por colocacion / mercado-lado / EUR comprometido (no colocado = 0), EV|fill ponderado por EUR vs media de razones.
I2 relleno SIN desenlace: no se descarta ni se cuenta como 0 en el EV resuelto; se reporta (conteo, coste, cotas peor/mejor) y la cobertura de resolucion baja.
I3 dias con cobertura <0,95: se REPORTAN (cobertura por dia x moneda, motivo) y entran en la vista 'todos' pero no en 'validos'.
I4 duplicados (tok,L,var,seg) se descartan y se cuentan; sin los 2 mejores dias solo con >=3 dias; n efectivo por cierre/dia; placebo p-valor.
I5 mercado-lado sin colocacion cuenta 0 en el denominador (mkt del dec_)."""
import os, sys, json, gzip, shutil, tempfile
import pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import cxb60_io as IO, informe_c5_cxb60 as C5
TMP = tempfile.mkdtemp(prefix='t_c5_'); REB = 0.2 * 0.07


def pnl(q, L, gana): return q * (gana - L) + q * REB * L * (1 - L)


def dia(out, d, filas, mkts, cov_ok=True, cov=0.99):
    """filas: (tok, coin, var, L, seg, fin, q, rem, gana|None). mkts: {coin: [tok,...]} procesados."""
    rows = []
    for tok, coin, var, L, seg, fin, q, rem, gana in filas:
        fill = q > 0; res = gana is not None and fill
        rows.append(dict(tok=tok, coin=coin, var=var, L=L, seg=seg, fin=fin, q=q, rem_antes=rem, pnl=pnl(q, L, gana) if res else None, cost=q * L if res else None, cost_pot=rem * L))
    with gzip.open(out + f'res_{d}.csv.gz', 'wt') as f: pd.DataFrame(rows).to_csv(f, index=False)
    lines = []
    for c, toks in mkts.items():
        for t in toks:
            r = ['mkt', 'run', d, t, '1', c, 'YES', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '{}', '0']; lines.append(','.join(r))
    IO.append_gz(out + f'dec_{d}.csv.gz', '\n'.join(lines) + '\n')
    json.dump(dict(dia=d, cobertura=cov, dia_valido=cov_ok, dia_completo=True, por_moneda={c: dict(procesados=len(t), esperados_teoricos=len(t), cobertura=cov, ok_095=cov_ok) for c, t in mkts.items()}), open(out + f'coverage_{d}.json', 'w'))


def test_definiciones_y_no_resueltos():
    out = TMP + '/a/'; os.makedirs(out)
    # CXB60: 4 colocaciones: t1 relleno 5 a 0,10 gana (resuelto), t2 relleno 5 a 0,20 pierde (resuelto), t3 relleno 5 a 0,10 SIN desenlace, t4 sin relleno. 3 mercados-lado procesados extra sin colocacion (t5,t6,t7) -> 7 en total.
    f = [('t1', 'ETH', 'CXB60', 0.1, 0, 100, 5.0, 5.0, 1.0), ('t2', 'ETH', 'CXB60', 0.2, 0, 100, 5.0, 5.0, 0.0), ('t3', 'SOL', 'CXB60', 0.1, 0, 200, 5.0, 5.0, None), ('t4', 'SOL', 'CXB60', 0.1, 0, 200, 0.0, 5.0, None),
         ('t1', 'ETH', 'PLC60_1', 0.1, 0, 100, 5.0, 5.0, 0.0), ('t1', 'ETH', 'PLC60_2', 0.1, 0, 100, 5.0, 5.0, 1.0)]
    dia(out, '2026-11-20', f, {'ETH': ['t1', 't2', 't5', 't6'], 'SOL': ['t3', 't4', 't7']})
    import io, contextlib
    b = io.StringIO()
    with contextlib.redirect_stdout(b): C5.main(['--out', out, '--salida', out + 'i.json'])
    inf = json.load(open(out + 'i.json')); v = inf['todos']['variantes']['CXB60']
    pn = pnl(5, .1, 1) + pnl(5, .2, 0); co = 5 * .1 + 5 * .2
    assert v['n_colocaciones'] == 4 and v['n_rellenos'] == 3 and v['n_rellenos_resueltos'] == 2 and v['rellenos_sin_desenlace'] == 1, v
    assert abs(v['P_fill_colocaciones'] - 0.75) < 1e-9 and abs(v['cobertura_resolucion_rellenos'] - 2 / 3) < 1e-3, v                                            # I2
    assert abs(v['pnl_total'] - round(pn, 3)) < 1e-9 and abs(v['coste_rellenos'] - co) < 1e-9 and abs(v['coste_rellenos_sin_desenlace'] - 0.5) < 1e-9
    assert abs(v['EV_incond_por_colocacion_eur'] - round(pn / 4, 6)) < 1e-9 and v['mercados_lado_procesados'] == 7 and abs(v['EV_incond_por_mercado_lado_eur'] - round(pn / 7, 6)) < 1e-9      # I1/I5
    assert abs(v['EV_incond_por_eur_comprometido'] - round(pn / 2.5, 4)) < 1e-4                                                                 # cost_pot = rem*L de las 4 colocaciones = .5+1+.5+.5 = 2.5
    assert abs(v['EV_cond_fill_ponderado_eur'] - round(pn / co, 4)) < 1e-4 and abs(v['EV_cond_fill_por_unidad_media'] - round((pnl(5, .1, 1) / .5 + pnl(5, .2, 0) / 1.0) / 2, 4)) < 1e-4, v
    peor, mejor = v['EV_cond_fill_cota_peor'], v['EV_cond_fill_cota_mejor']; assert peor < v['EV_cond_fill_ponderado_eur'] < mejor, (peor, v['EV_cond_fill_ponderado_eur'], mejor)
    assert v['n_efectivo']['cierres_con_relleno'] == 1 and v['n_efectivo']['mercados_lado_con_relleno'] == 2 and v['EV_cond_sin_2_mejores_dias'] is None                         # I4 (1 dia)
    p = inf['todos']['placebo_PLC60']; assert p['S'] == 2 and 0 < p['p_valor'] <= 1 and p['S_minimo_prereg'] == 100


def test_cobertura_y_duplicados():
    out = TMP + '/b/'; os.makedirs(out)
    f = [('t1', 'ETH', 'CXB60', 0.1, 0, 100, 5.0, 5.0, 1.0), ('t1', 'ETH', 'CXB60', 0.1, 0, 100, 5.0, 5.0, 1.0)]       # duplicado exacto
    dia(out, '2026-11-20', f, {'ETH': ['t1']}, cov_ok=True, cov=0.99); dia(out, '2026-11-21', [('t9', 'ETH', 'CXB60', 0.1, 0, 300, 5.0, 5.0, 0.0)], {'ETH': ['t9']}, cov_ok=False, cov=0.80)
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()): C5.main(['--out', out, '--salida', out + 'i.json'])
    inf = json.load(open(out + 'i.json'))
    assert inf['duplicados_descartados'] == 1 and inf['dias_validos'] == ['2026-11-20'] and inf['dias_no_validos'] == ['2026-11-21'], inf                              # I3/I4
    c = inf['cobertura_por_dia_y_moneda']['2026-11-21']; assert c['valido'] is False and c['por_moneda']['ETH']['cobertura'] == 0.8 and c['motivo_no_valido'] == ['ETH']
    assert inf['todos']['variantes']['CXB60']['n_rellenos'] == 2 and inf['validos']['variantes']['CXB60']['n_rellenos'] == 1 and sorted(inf['todos']['dias']) == ['2026-11-20', '2026-11-21']
    out2 = TMP + '/c/'; os.makedirs(out2)
    with contextlib.redirect_stdout(io.StringIO()): C5.main(['--out', out2, '--salida', out2 + 'i.json'])
    assert json.load(open(out2 + 'i.json'))['todos']['estado'] == 'SIN_DATOS'


def test_sin_2_mejores_dias():
    out = TMP + '/d/'; os.makedirs(out)
    for i, g in enumerate([1.0, 1.0, 0.0, 0.0]):                                   # dos dias ganadores, dos perdedores
        dia(out, f'2026-11-2{i}', [(f't{i}', 'ETH', 'CXB60', 0.1, 0, 100 + i, 5.0, 5.0, g)], {'ETH': [f't{i}']})
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()): C5.main(['--out', out, '--salida', out + 'i.json'])
    v = json.load(open(out + 'i.json'))['todos']['variantes']['CXB60']; esp = round(pnl(5, .1, 0) / (5 * .1), 4)
    assert v['n_efectivo']['dias_con_relleno'] == 4 and abs(v['EV_cond_sin_2_mejores_dias'] - esp) < 1e-4, v


if __name__ == '__main__':
    try: test_definiciones_y_no_resueltos(); test_cobertura_y_duplicados(); test_sin_2_mejores_dias(); print('TODOS OK (informe_c5_cxb60)')
    finally: shutil.rmtree(TMP, ignore_errors=True)
