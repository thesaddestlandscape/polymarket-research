import os, sys, json, importlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
import reconstruir_puja_fin as R

S = 'eth-updown-5m-1000000000'
def ts(x=0): return '2026-10-20T17:55:%02d.000+00:00' % x
F = [dict(tipo='puja_post', oid='0xa', slug=S, coin='eth', lado='YES', k='2', precio='0.23', size='5.0', ts=ts(1)),
     dict(tipo='puja_post', oid='0xb', slug=S, coin='eth', lado='YES', k='2', precio='0.24', size='5.0', ts=ts(2)),
     dict(tipo='lectura', oid='0xa', f=5.0, precio=0.23, ts=ts(3)),
     dict(tipo='verificada', oid='0xb', f=0.0, ts=ts(4)),
     dict(tipo='gemelo_relleno', oid='0xa', acc_total=5.0, ts=ts(5)),
     dict(tipo='cierre_mercado', slug=S, motivo='tick_cambiado', ts=ts(6))]
AHORA = 1000000000 + 300 + 36

def test_reconstruye_relleno_y_cadena():
    r, = R.reconstruir(F, {(S, 'Up'): dict(acciones=5.0, coste=1.15)}, AHORA)
    assert r['reconstruido'] and r['llenas_detectadas'] == 5.0 and r['relleno_real'] and r['n_ordenes'] == 2
    assert r['markouts'] == 'missing' and r['discrepa_cadena'] is False and r['fin_puja'] == 'tick_cambiado'
    assert r['sim_relleno_cualquiera']

def test_no_cerrado_o_con_puja_fin_se_ignora():
    assert R.reconstruir(F, {}, 1000000000 + 320) == []
    assert R.reconstruir(F + [dict(tipo='puja_fin', slug=S)], {}, AHORA) == []

def test_sin_relleno_y_discrepancia():
    f = [x for x in F if x['tipo'] != 'lectura']
    r, = R.reconstruir(f, {(S, 'Up'): dict(acciones=5.0, coste=1.0)}, AHORA)
    assert r['llenas_detectadas'] == 0 and r['relleno_real'] is False and r['discrepa_cadena'] is True
    r2, = R.reconstruir(f, {}, AHORA); assert r2['discrepa_cadena'] is None

def test_idempotente_y_no_toca_ledger(tmp_path, monkeypatch):
    out = tmp_path / 'o.jsonl'; led = tmp_path / 'l.jsonl'
    led.write_text('\n'.join(json.dumps(x) for x in F) + '\n{truncada')
    h = led.read_bytes()
    monkeypatch.setattr(R, 'OUT', str(out)); monkeypatch.setattr(R, 'LEDGER', str(led)); monkeypatch.setattr(R, 'POSIC', str(tmp_path / 'no.csv'))
    filas, bad = R.leer_jsonl(str(led)); assert bad == 1
    regs = R.reconstruir(filas, {}, AHORA)
    assert R.escribir(regs) == (1, 0) and R.escribir(regs) == (0, 1)
    assert len(out.read_text().splitlines()) == 1 and led.read_bytes() == h
