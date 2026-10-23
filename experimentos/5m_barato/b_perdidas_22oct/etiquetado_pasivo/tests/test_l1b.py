"""Tests L1b (rapidos, sin red ni datos reales). Ejecutar: python3 -m pytest -q tests/test_l1b.py"""
import os, sys, json, gzip, importlib.util, tempfile
import numpy as np, pandas as pd
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts')
def cargar(nombre, env):
    for k, v in env.items(): os.environ[k] = v
    sp = importlib.util.spec_from_file_location(nombre, os.path.join(H, nombre + '.py')); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m

def test_ordenes_b_no_asume_orden(tmp_path):
    rl = cargar('retirada_liquidez', {'L1B_RET_OUT': str(tmp_path / 'o')})
    ev = [dict(tipo='post_lat', oid='a', t_call0=100.0), dict(tipo='fuera_libro', oid='a', ts='2026-10-23T00:00:05Z'),     # ANTES de puja_post
          dict(tipo='intencion_post', oid='a', tok='T1'), dict(tipo='puja_post', oid='a', slug='eth-updown-5m-1', coin='eth', lado='YES', precio=0.12, size=5.0, t_dec=99.0),
          dict(tipo='puja_fin', slug='eth-updown-5m-1', lado='YES', rellenos=[dict(oid='a', t_deteccion=102.0, acc=5.0)]*2)]       # relleno duplicado -> 1
    p = tmp_path / 'l.jsonl'; p.write_text('\n'.join(json.dumps(e) for e in ev) + '\n{"tipo": "puja_po')                               # ultima linea a medias
    O = rl.ordenes_b(str(p)); assert O['a']['tc'] == 100.0 and O['a']['t_fuera'] and O['a']['tok'] == 'T1' and O['a']['rel'] == [(102.0, 5.0)]

def test_delta2_estratificado(tmp_path):
    ev = cargar('evaluar_retirada', {'L1B_RET_OUT': str(tmp_path)})
    st = np.array(['a'] * 4 + ['b'] * 4); co = np.ones(8); ex = np.array([1, 1, 0, 0] * 2)
    pn = np.array([-1, -1, 1, 1, -1, -1, 0, 0.0])           # estrato a: EV1=-1, EV0=+1 (dif -2); estrato b: -1 vs 0 (dif -1); pesos 2 y 2
    assert abs(ev.delta2(co, pn, ex, st) - (-1.5)) < 1e-9
    assert np.isnan(ev.delta2(co, pn, np.ones(8, int), st))   # sin ambas clases -> missing, no 0

def test_poblacion_idempotente_y_una_fuente_por_dia(tmp_path):
    pop = tmp_path / 'pop'; r1 = tmp_path / 'r1'; out = tmp_path / 'out'; pop.mkdir(); r1.mkdir()
    m = cargar('etiquetar_poblacion', {'L1B_OUT': str(out), 'L1B_R1': str(r1), 'L1B_POPU': str(pop)})
    cols = 'maker,c,act,mid,fin,lado,des,pc,T,bloque,ts,tx,n_same,rank_same,q,pos1,sh_ahead_same,sh_better,sh_beyond,coste,pnl,acc,gana,es_b,dia'
    row = lambda mk, d, es_b: f'{mk},1,ETH,111,1000000300,YES,YES,0.2,100,1,1000000000,t,1,0,,SOLO,0,0,0,1.0,4.0,5.0,1.0,{es_b},{d}'
    with gzip.open(pop / 'pop_units_2026-10-20.csv.gz', 'wt') as f: f.write(cols + '\n' + row('0xa', '2026-10-20', 0) + '\n' + row('0xb', '2026-10-20', 1) + '\n')   # es_b=1 se excluye
    fu = m.fuentes('2026-10-17'); assert [(d, n) for d, n, _, _ in fu] == [('2026-10-20', 'pop_units_backfill')]
    with gzip.open(r1 / 'units_2026-10-20.csv.gz', 'wt') as f: f.write('dia,maker,mkt,lado_c,act,c,p,sh,T,pc,fin,gana,ts,vol30,hora,R1a,R1b\n')           # R1 de un dia < FWD0 se IGNORA
    assert len(m.fuentes('2026-10-17')) == 1
    n, dias, _ = m.etiquetar('2026-10-17'); assert n == 1 and dias == ['2026-10-20']
    n2, _, _ = m.etiquetar('2026-10-17'); assert n2 == 0
    x = m.leer_dia('2026-10-20'); assert len(x) == 1 and x.forward.iloc[0] == 0 and x.clase_rpre.iloc[0] == 'missing'    # sin bookTicker -> missing, nunca en_contra
