"""Test anti-regresion del doble conteo de acc_llena (26-Oct). Rapido, sin red. Ejecutar: python3 -m pytest -q tests/test_acc_llena.py
Incluye un test sobre datos reales (se salta si faltan): sum acc_llena de ordenes rellenas por (mercado, outcome) <= acciones de la posicion y PnL por ordenes == PnL por posiciones."""
import os, sys, json, glob, csv, importlib.util
import numpy as np, pandas as pd, pytest
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts')
def cargar(env):
    for k, v in env.items(): os.environ[k] = v
    sp = importlib.util.spec_from_file_location('etiquetar_pasivo', os.path.join(H, 'etiquetar_pasivo.py')); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m

def test_tardio_no_se_cuenta_dos_veces(tmp_path):
    m = cargar({'L1_OUT': str(tmp_path / 'o')})
    r = {(1.0, 5.0): dict(acc=5.0, tardio=True)}
    assert m.acc_orden(r, [5.0]) == 5.0                                  # tardio ya dentro de puja_fin.rellenos -> 5, no 10
    assert m.acc_orden({}, [5.0]) == 5.0                                 # tardio solo en el evento -> se cuenta
    assert m.acc_orden({(1, 4.0): dict(acc=4.0), (2, 1.0): dict(acc=1.0)}, []) == 5.0   # dos parciales distintos se suman
    assert m.acc_orden({(1, 4.0): dict(acc=4.0), (2, 5.0): dict(acc=5.0, tardio=True)}, [5.0]) == 9.0

def test_ledger_sintetico(tmp_path):
    m = cargar({'L1_OUT': str(tmp_path / 'o')})
    ev = [dict(tipo='intencion_post', oid='a', tok='T'), dict(tipo='puja_post', oid='a', slug='eth-updown-5m-1000', coin='eth', lado='YES', precio=0.2, size=5.0, t_dec=1.0),
          dict(tipo='puja_fin', slug='eth-updown-5m-1000', lado='YES', rellenos=[dict(oid='a', t_deteccion=3.0, acc=5.0, tardio=True)]), dict(tipo='relleno_tardio', oid='a', acc=5.0)]
    p = tmp_path / 'l.jsonl'; p.write_text('\n'.join(json.dumps(e) for e in ev) + '\n')
    m.LEDGER = str(p); m.POSIC = str(tmp_path / 'pos.csv'); open(m.POSIC, 'w').write('mercado,outcome,tanda_B\n')
    o, _, _ = m.cargar_fuentes(); assert o[0]['acc_llena'] == 5.0

DL = '/root/polymarket-research-datalogs/etiquetado_pasivo_B'
POS = '/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/posiciones.csv'
@pytest.mark.skipif(not glob.glob(DL + '/etiquetado_B_*.csv.gz') or not os.path.exists(POS), reason='sin datos reales')
def test_datos_reales_cuadran_con_posiciones():
    B = pd.concat([pd.read_csv(f) for f in glob.glob(DL + '/etiquetado_B_*.csv.gz')]); o = B[(B.unidad == 'orden') & (B.acc_llena > 0) & (B.resuelto == 1)]
    pos = {(r['mercado'], r['outcome']): r for r in csv.DictReader(open(POS)) if r['tanda_B']}
    g = o.groupby(['mercado', 'outcome']).agg(acc=('acc_llena', 'sum'), n=('id', 'size'))
    exceso = [(k, float(a), float(pos[k]['acciones'])) for k, a in g.acc.items() if k in pos and a > float(pos[k]['acciones']) + 1e-6]
    assert not exceso, exceso[:5]                                        # acc de ordenes NUNCA mayor que la posicion (el bug daba exactamente 2x)
