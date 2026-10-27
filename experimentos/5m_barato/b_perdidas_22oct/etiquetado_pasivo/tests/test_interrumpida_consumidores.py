"""4a review #2: los consumidores de puja_fin tratan `interrumpida` (parcial de salida) explicitamente: sin usar t_deteccion=hora de salida como hora de
relleno ni contar el parcial como cierre. Sin red."""
import os, sys, json, importlib.util, subprocess
import pytest
ES = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts')
B5 = os.path.abspath(os.path.join(ES, '..', '..', '..'))                      # experimentos/5m_barato


def cargar(nombre, path, env=None):
    for k, v in (env or {}).items(): os.environ[k] = v
    sp = importlib.util.spec_from_file_location(nombre, path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m


EV = [dict(tipo='intencion_post', oid='a', tok='T'), dict(tipo='puja_post', oid='a', slug='eth-updown-5m-1000', coin='eth', lado='YES', precio=0.2, size=5.0, t_dec=1.0, ts='x'),
      dict(tipo='lectura', oid='a', f=5.0), dict(tipo='relleno_tardio', oid='a', slug='eth-updown-5m-1000', acc=5.0),
      dict(tipo='puja_fin', slug='eth-updown-5m-1000', lado='YES', interrumpida=True, llenas_detectadas=5.0,
           rellenos=[dict(oid='a', t_deteccion=9999.0, acc=5.0, tardio=True), dict(oid='a', t_deteccion=3.0, acc=1.0)])]


def test_etiquetar_pasivo_no_usa_la_hora_de_salida_ni_cuenta_doble(tmp_path):
    m = cargar('etiquetar_pasivo', os.path.join(ES, 'etiquetar_pasivo.py'), {'L1_OUT': str(tmp_path / 'o')})
    p = tmp_path / 'l.jsonl'; p.write_text('\n'.join(json.dumps(e) for e in EV) + '\n')
    m.LEDGER = str(p); m.POSIC = str(tmp_path / 'pos.csv'); open(m.POSIC, 'w').write('mercado,outcome,tanda_B\n')
    o, _, _ = m.cargar_fuentes()
    assert o[0]['acc_llena'] == 6.0                                           # 1 (relleno real) + 5 (relleno_tardio del ledger), sin duplicar el tardio del parcial
    ev2 = [e for e in EV if e['tipo'] != 'relleno_tardio']
    p.write_text('\n'.join(json.dumps(e) for e in ev2) + '\n')
    m.POSIC = str(tmp_path / 'pos.csv')
    assert m.cargar_fuentes()[0][0]['acc_llena'] == 1.0                       # solo el relleno real (el tardio del parcial siempre va acompanado de su relleno_tardio en el ledger)


def test_retirada_liquidez_ignora_tardios_del_parcial(tmp_path):
    m = cargar('retirada_liquidez', os.path.join(ES, 'retirada_liquidez.py'))
    p = tmp_path / 'l.jsonl'; p.write_text('\n'.join(json.dumps(e) for e in EV) + '\n')
    O = m.ordenes_b(str(p))
    assert O['a']['rel'] == [(3.0, 1.0)]                                      # el tardio del parcial (hora de salida 9999) no entra


def test_conciliar_ledger_B_usa_el_parcial_solo_si_no_hay_completo(tmp_path, monkeypatch):
    A = cargar('actualizar_wd', os.path.join(B5, 'contabilidad_wallet_dedicada', 'actualizar.py'))
    s = 'eth-updown-5m-1000'
    def corre(filas):
        monkeypatch.setattr(A, 'leer_jsonl', lambda p: filas)
        return A.conciliar_ledger_B([])
    parcial = dict(tipo='puja_fin', slug=s, interrumpida=True, llenas_detectadas=5.0, real=True)
    r = corre([parcial])
    assert r['acciones_ledger'] == 5.0                                        # parcial solo: cota inferior que ya incluye los tardios
    r = corre([parcial, dict(tipo='relleno_tardio', slug=s, acc=5.0, real=True)])
    assert r['acciones_ledger'] == 5.0                                        # no se suma el tardio otra vez
    r = corre([parcial, dict(tipo='puja_fin', slug=s, llenas_detectadas=7.0, real=True)])
    assert r['acciones_ledger'] == 7.0                                        # con puja_fin completo, el parcial no cuenta


def test_b_postmortem_no_toma_el_parcial_como_cierre():
    src = open(os.path.join(B5, 'b_seleccion_adversa', 'scripts', 'b_postmortem.py')).read()
    assert "elif t == 'puja_fin' and not r.get('interrumpida')" in src
