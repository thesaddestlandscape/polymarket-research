#!/usr/bin/env python3
"""Pruebas minimas del piloto M1/M4 (fixture diminuta, sin red ni datos reales). Ejecutar: python3 -I -B test_piloto_m1_m4.py"""
import sys, os, gzip, json, tempfile, pickle
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
import piloto_m1_m4 as P

def test_libro():
    lb = P.Libro(); lb.b = P.parse_bk('0.20:10;0.22:5;0.23:7'); lb.a = P.parse_bk('0.99:3;0.25:4'); lb.recalc()
    assert lb.top() == (0.23, 0.25); assert lb.nivel(0.22) == 5
    lb.aplica('B', 0.23, 0); assert lb.top()[0] == 0.22          # el top se vacia -> recalcula
    lb.aplica('A', 0.21, 2); assert lb.top() == (0.22, 0.21)     # cruzado (bid > ask)
    lb.aplica('A', 0.22, 1); lb.aplica('A', 0.21, 0); assert lb.top() == (0.22, 0.22)   # bloqueado

def test_cons():
    assert P.q_cons(None, dict(ahead=10.0), [12.0, 0, 0, 0, 0, 1], 5) == 2.0
    assert P.q_cons(None, dict(ahead=10.0), [3.0, 0, 0, 0, 0, 1], 5) == 0.0
    assert P.q_cons(None, dict(ahead=10.0), [0.0, 1.0, 0, 0, 0, 1], 50) == 50.0       # barrido misma ficha
    assert P.q_cons(None, dict(ahead=10.0), [6.0, 0, 0, 6.0, 0, 2], 50) == 2.0      # espejo suma
    assert P.q_cons(None, dict(ahead=10.0), [6.0, 0, 0, 6.0, 0, 2], 50, espejo=False) == 0.0
    assert np.isnan(P.q_cons(None, None, [0] * 6, 5))
    assert P.q_cons(None, dict(ahead=10.0), None, 5) == 0.0                       # sin trades = flujo 0 (dato presente), no NaN
    assert P.q_cons(None, dict(ahead=1.0), [0, 0, 0, 0, 0, 0, 0, 5.0, 0], 5, todo_lado=True) == 4.0

def test_unidades():
    df = pd.DataFrame([dict(mid='m1', lado='YES', coin='eth', clase='lo', fin=100, L=0.2, n_ord=0, size=5, gana=1.0, q=0.0),
                       dict(mid='m1', lado='YES', coin='eth', clase='lo', fin=100, L=0.21, n_ord=1, size=5, gana=1.0, q=5.0),
                       dict(mid='m2', lado='NO', coin='eth', clase='lo', fin=100, L=0.3, n_ord=0, size=5, gana=0.0, q=0.0)])
    u = P.unidades(df, 'q')
    assert len(u) == 2 and u.q.tolist() == [5.0, 0.0]                           # 1.er relleno; puja sin relleno = 0 (no missing)
    r = P.resumen_u(u)
    assert abs(r['pnl_eur'] - 5 * (1 - 0.21)) < 1e-9 and abs(r['ev_eur_ponderado'] - (1 - 0.21) / 0.21) < 1e-9
    assert abs(r['identidad_P_x_EVcond'] - r['ev_incondicional_pnl_por_puja']) < 1e-9
    assert r['n_pujas'] == 2 and r['n_rellenos'] == 1 and r['p_relleno'] == 0.5

def test_etapa2_fixture():
    d = tempfile.mkdtemp(); ms = d + '/ms/'; tx = d + '/tx/'; os.makedirs(ms); os.makedirs(tx)
    tok = '111'; tok2 = '222'
    with gzip.open(ms + 'libro5_ms_2026-01-01_1.csv.gz', 'wt') as f:
        f.write('tipo,t_ms,token,c1,c2,c3,recepcion,seq\nG,1000,*,arranque,,,1000,1\n')
        f.write(f'B,900,{tok},0.20:10;0.22:5,0.30:4,,1001,2\nB,900,{tok2},0.50:1,0.60:1,,1001,3\n')
        f.write(f'd,1100,{tok},B,0.22,8.0,1100,4\n')                             # nivel 0.22 pasa a 8
        f.write(f'T,1150,{tok},0.22,SELL,3.0,1150,5\n')
        f.write(f'T,1160,{tok2},0.50,SELL,2.0,1160,6\nT,1170,{tok2},0.78,BUY,4.0,1170,8\n')
        f.write(f'd,1200,{tok},B,0.22,5.0,1200,7\n')
    with gzip.open(tx + 'libro5_tx_2026-01-01_1.csv.gz', 'wt') as f:
        f.write(f'1150,{tok},0xaa,1150\n1160,{tok2},0xbb,1160\n1170,{tok2},0xcc,1170\n1180,{tok2},0xee,1180\n')
    with gzip.open(d + '/onchain.csv.gz', 'wt') as f:
        f.write('tipo,bloque,ts_est,tx,log_index,order_hash,maker,taker,side,token_id,maker_amt,taker_amt,fee\n')
        f.write(f'F,1,3600.0,0xaa,1,h1,0x1,0x2,0,{tok},1,1,0\nF,1,3600.0,0xbb,1,h2,0x1,0x2,0,{tok2},1,1,0\nF,1,3600.0,0xcc,1,h3,0x1,0x2,0,{tok2},1,1,0\nF,1,3600.0,0xee,1,h5,0x1,0x2,0,{tok2},1,1,0\nF,1,3600.0,0xaa,2,h6,0x1,0x2,1,{tok2},1,1,0\nF,1,3600.0,0xdd,1,h4,0x659aab,0x2,0,999,1,1,0\n')
    open(d + '/seco.jsonl', 'w').write('')
    for k, v in (('L5MS', ms), ('L5TX', tx), ('OUT', d + '/out/'), ('SECO', d + '/seco.jsonl')): setattr(P, k, v)
    P.ONCH = d + '/onchain_%s.csv.gz'; os.rename(d + '/onchain.csv.gz', d + '/onchain_2026-01-01.csv.gz'); os.makedirs(P.OUT)
    P.puerta = lambda *a, **k: None
    R = pd.DataFrame([dict(token=tok, token_comp=tok2, t_arr=1050, t_end=1300, L=0.22)])
    for b in P.BRAZOS: R.to_pickle(P.OUT + f'ordenes_{P.POL}_{b}_2026-01-01.pkl')
    P.etapa2('2026-01-01')
    e2 = pickle.load(open(P.OUT + 'etapa2_2026-01-01.pkl', 'rb'))
    assert e2['snap'][('base', 0, 0)]['ahead'] == 5.0                            # estado a t_arr=1050 (antes del delta rx=1100)
    assert e2['snap'][('base', 0, 40)]['ahead'] == 5.0 and e2['snap'][('base', 0, 0)]['best_bid'] == 0.22
    assert e2['flujo'][('base', 0)][0] == 3.0 and e2['flujo'][('base', 0)][3] == 4.0   # SELL misma ficha en el nivel + BUY espejo a 1-L=0.78
    r = e2['res']
    assert r['libro5_tx_cubiertas_por_ms'] == 3 / 4                               # 0xee (1180) no esta en libro5_ms: missing != cubierto
    assert r['onchain_tx_token_universo'] == 5 and abs(r["onchain_cubiertas_por_libro5_ms"] - 3 / 5) < 1e-9   # (aa,tok2) esta en onchain pero el WS lo publico bajo tok: por (tx,ficha) no cubierto
    assert r['onchain_tx_universo'] == 4 and abs(r['onchain_cubiertas_por_tx'] - 3 / 4) < 1e-9          # por tx SI esta cubierto aa
    assert r['onchain_filas_de_wallets_propias_prefijo_0x659a_0xb6ed'] == 1

def test_idempotente():
    # relanzar etapa2 sobre el mismo dia reescribe la MISMA salida (determinista)
    import hashlib
    a = hashlib.sha256(open(P.OUT + 'etapa2_2026-01-01_cobertura.json', 'rb').read()).hexdigest()
    P.etapa2('2026-01-01'); b = hashlib.sha256(open(P.OUT + 'etapa2_2026-01-01_cobertura.json', 'rb').read()).hexdigest()
    assert a == b

if __name__ == '__main__':
    for n, f in list(globals().items()):
        if n.startswith('test_'): f(); print('OK', n)
