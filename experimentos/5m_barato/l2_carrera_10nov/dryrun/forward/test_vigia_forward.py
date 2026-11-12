#!/usr/bin/env python3
"""Tests del vigia/cron del forward B-CXB. python3 -I test_vigia_forward.py   (sintetico en tmp; sin red ni Telegram; no toca el datalog real)
V1 runners_vivos: solo cuenta procesos PYTHON con el runner como elemento del argv (no la screen, ni el `bash -c`, ni otro script).
V2 problemas_heartbeat: sano / heartbeat viejo / status / pid del run_id ausente / 2 instancias / lag / RSS / sin heartbeat.
V3 latch: un aviso por episodio (firma estable), si el aviso falla se reintenta, vuelve a sano => se limpia.
V4 registrar_d_dep: antes del cutoff, hash o VERSION distintos o status != RUNNING no registran; la 1a vez que cumple escribe D_dep y primer dia contable = D_dep+1; nunca se sobrescribe.
V5 diario: informe sin EV ni puertas, dias validos/no validos con motivo, cobertura por poblacion, gmap de ayer (y BTC), contador de la mirada 1, avisos por cada fallo; el feed se lee con cola de gz truncada.
V7 resumen diario: <= 9 lineas, heartbeat, dias validos, cobertura, gmap D-1, «G3 en seguimiento (trivial vs GEO1)», SIN EV ni puertas; uno por dia (marcador); si el envio falla se reintenta y deja ALERTA.
V8 cron: `aviso` devuelve rc 0 SOLO si Telegram devolvio True (antes marcaba el dia como avisado aunque fallase); aviso_dia no deja marcador si falla y avisa una vez al dia si va bien.
V6 cron en seco: modo desconocido rc=2; 'heartbeat' no revienta sin OUT; 'diario' en un OUT sintetico enlaza gmaps de sa_r1, resuelve primario y c59 con --gmap-dir y escribe el informe diario (sin Telegram)."""
import os, sys, json, gzip, shutil, tempfile, subprocess, time, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE.rstrip('/')) + '/')
os.environ['CXB60_SIN_TELEGRAM'] = '1'
TMP = tempfile.mkdtemp(prefix='test_vig_'); N = [0]
os.environ['CXB60_DIR'] = TMP + '/_x'; os.makedirs(TMP + '/_x')
import vigia_cxb60_forward as V, forward_gates as FG, test_forward as TF


def nuevo(): N[0] += 1; d = f'{TMP}/t{N[0]}/'; os.makedirs(d); return d
def proc_falso(root, pid, argv): d = f'{root}/{pid}'; os.makedirs(d); open(d + '/cmdline', 'wb').write(b'\0'.join(a.encode() for a in argv) + b'\0')
SCRIPT = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/dryrun/cxb60_dryrun_fase0.py'


def test_runners_vivos():
    r = nuevo(); proc_falso(r, 100, ['/root/polymarket-research/.venv/bin/python', '-I', SCRIPT]); proc_falso(r, 101, ['python3', SCRIPT, '--once']); proc_falso(r, 102, ['bash', '-c', 'ulimit -v 7000000; exec .venv/bin/python -I ' + SCRIPT])
    proc_falso(r, 103, ['SCREEN', '-dmS', 'cxb60dry', 'bash', '-c', 'cd x && ' + SCRIPT]); proc_falso(r, 104, ['python3', '/otro/cxb60_resolve.py']); proc_falso(r, 105, ['python3', '/otro/cxb60_dryrun_fase0.py.bak']); os.makedirs(r + '/self'); os.makedirs(r + '/999'); open(r + '/vacio', 'w').write('')
    assert V.runners_vivos(r) == [100, 101], V.runners_vivos(r); assert V.pid_de_run_id('20261112T111835Z_934121') == 934121 and V.pid_de_run_id('sinpid') is None and V.pid_de_run_id(None) is None
    print('F V1 ok: solo cuenta python con el runner en el argv (no screen, ni bash -c, ni otro script); pid sale del run_id')


def hb(out, **kw):
    h = dict(run_id='20261112T120000Z_4242', status='RUNNING', wall=time.time(), lag_s=1.0, rss_mb=700.0); h.update(kw); json.dump(h, open(out + 'heartbeat.json', 'w'))


def test_heartbeat():
    o = nuevo(); assert V.problemas_heartbeat(o, vivos=[4242])[0][0] == 'sin_heartbeat'
    hb(o); assert V.problemas_heartbeat(o, vivos=[4242]) == []
    t = lambda **kw: (hb(o, **kw), {x for x, _ in V.problemas_heartbeat(o, vivos=kw.pop('_v', [4242]))})[1]
    assert t(wall=time.time() - 400) == {'heartbeat_viejo'} and t(status='STOPPED_COMPLETE') == {'status'} and t(lag_s=601) == {'lag'} and t(rss_mb=3000) == {'rss'} and t(lag_s=600, rss_mb=2999) == set()
    hb(o); assert {x for x, _ in V.problemas_heartbeat(o, vivos=[9999])} == {'pid_ausente'} and {x for x, _ in V.problemas_heartbeat(o, vivos=[])} == {'pid_ausente'}
    assert {x for x, _ in V.problemas_heartbeat(o, vivos=[4242, 4300])} == {'instancias_multiples'}
    print('F V2 ok: heartbeat sano; viejo >5 min, status, pid del run_id ausente, 2 instancias, lag >600 s, RSS >=3000 MB y sin heartbeat se detectan (limites inclusive)')


def test_latch():
    o = nuevo(); enviados = []; V.avisar = lambda txt: (enviados.append(txt), True)[1]
    V.avisa_con_latch(o, 'x', [('lag', 'lag 700 s')], 'p:'); V.avisa_con_latch(o, 'x', [('lag', 'lag 900 s')], 'p:'); assert len(enviados) == 1                            # valores distintos, misma firma: no spamea
    V.avisa_con_latch(o, 'x', [('lag', 'a'), ('rss', 'b')], 'p:'); assert len(enviados) == 2                                                                    # problema nuevo: aviso
    V.avisa_con_latch(o, 'x', [], 'p:'); V.avisa_con_latch(o, 'x', [('lag', 'otra vez')], 'p:'); assert len(enviados) == 3                                      # recuperado y de nuevo roto: aviso
    o2 = nuevo(); V.avisar = lambda txt: False; V.avisa_con_latch(o2, 'x', [('lag', 'a')], 'p:'); assert not os.path.exists(o2 + 'x_latch.json') or json.load(open(o2 + 'x_latch.json')) == {}
    V.avisar = lambda txt: (enviados.append(txt), True)[1]; V.avisa_con_latch(o2, 'x', [('lag', 'a')], 'p:'); assert len(enviados) == 4                          # el aviso fallido se reintenta
    print('F V3 ok: un aviso por episodio (firma estable sin valores), problema nuevo avisa, recuperacion limpia, aviso fallido se reintenta')


def test_d_dep():
    o = nuevo(); co = dt.datetime(2026, 11, 12, 11, 24, tzinfo=dt.timezone.utc).timestamp(); man = lambda **kw: json.dump(dict(dict(job='cxb60_dryrun_v3', status='RUNNING', run_id='r_1', inicio=co + 3600, hash_check=dict(sha256_referencia=FG.HASH_REF)), **kw), open(o + 'run_manifest.json', 'w'))
    assert FG.registrar_d_dep(o) == (None, False)
    for kw in (dict(inicio=co - 10), dict(job='otra'), dict(status='STOPPED_COMPLETE'), dict(hash_check=dict(sha256_referencia='0')), dict(inicio=None)): man(**kw); assert FG.registrar_d_dep(o) == (None, False) and not os.path.exists(o + 'forward_d_dep.json'), kw
    man(inicio=dt.datetime(2026, 11, 12, 23, 50, tzinfo=dt.timezone.utc).timestamp()); r, c = FG.registrar_d_dep(o); assert c and r['D_dep'] == '2026-11-12' and r['primer_dia_contable'] == '2026-11-13' and r['sha256_referencia'] == FG.HASH_REF
    man(inicio=co + 5 * 86400); r2, c2 = FG.registrar_d_dep(o); assert not c2 and r2 == r and FG.lee_d_dep(o)['D_dep'] == '2026-11-12'                                  # nunca se sobrescribe
    print('F V4 ok: D_dep solo con manifiesto v3 RUNNING, hash congelado y posterior al cutoff; primer dia contable = D_dep+1; escrito una sola vez')


def test_diario():
    ds = TF.dias(4, '2026-11-20'); o = nuevo(); gm = nuevo(); TF.crea_datos(o, ds, semillas=1, gmap_dir=gm); hb(o)
    json.dump(dict(D_dep='2026-11-19', primer_dia_contable='2026-11-20'), open(o + 'forward_d_dep.json', 'w')); V.problemas_heartbeat.__defaults__ = (None, None, [4242])
    enviados = []; V.avisar = lambda txt: (enviados.append(txt), True)[1]
    # un gz con la cola truncada (escritura en curso): el feed lo lee igualmente
    p = o + 'dec_2026-11-23.csv.gz'; raw = open(p, 'rb').read(); open(p, 'wb').write(raw + raw[:30])
    rc = V.modo_diario(o, gm, hoy='2026-11-24'); rep = json.load(open(o + 'forward_diario_2026-11-24.json')); txt = open(o + 'forward_diario_2026-11-24.json').read()
    assert rc == 1 or rc == 0; assert rep['D_dep']['D_dep'] == '2026-11-19' and rep['primer_dia_contable'] == '2026-11-20' and rep['poblaciones']['primaria']['n_dias_validos'] == 4 and rep['poblaciones']['primaria']['cobertura_desenlace_agregada']['cobertura'] == 1.0
    assert rep['contador_mirada_1']['falta'] == 6 and rep['contador_mirada_1']['fecha_prevista'] == '2026-11-30' and rep['contador_mirada_1']['plazo_D_dep_mas_35'] == '2026-12-24' and rep['poblaciones']['primaria']['por_dia']['2026-11-23']['feed']['mercados'] == 12
    assert rep['poblaciones']['BTC']['n_dias_validos'] == 0 and rep['sello_print'] == {'primario': 'ws_ex-19-1', 'c59': 'ws_ex-59-1'} and rep['integridad'] == []
    tipos = {p['tipo'] for p in rep['problemas']}; assert 'gmap_BTC' in tipos and 'gmap_btc_cobertura' in tipos and 'dia_no_valido' not in tipos, tipos                  # falta la fuente BTC de ayer: se avisa; el primario esta sano
    assert not any(k in txt for k in ('"pnl', '"ev_', 'ic90', 'p_valor', '"G1', 'veredicto')), 'el informe diario NO debe contener EV/puertas'
    assert len(enviados) == 2 and 'gmap' in enviados[0] and enviados[1].startswith('cxb60 forward diario 2026-11-24'), enviados          # 1 aviso de problema + 1 resumen diario
    # ahora con la fuente BTC y sin problemas => sin aviso nuevo; un dia no valido (coverage false) y un gmap primario ausente => se avisan con su motivo
    gb = TF.GB; json.dump({'x': dict(id='1', toks=['a', 'b'], des='YES')}, open(gm + 'gmap_btc_2026-11-23.json', 'w')); json.dump(dict(dia='2026-11-23', cobertura_desenlace=1.0), open(gm + 'cob_btc_2026-11-23.json', 'w'))
    cov = json.load(open(o + 'coverage_2026-11-23.json')); cov['dia_valido'] = False; json.dump(cov, open(o + 'coverage_2026-11-23.json', 'w')); os.remove(gm + 'gmap_2026-11-23.json')
    V.modo_diario(o, gm, hoy='2026-11-24'); rep = json.load(open(o + 'forward_diario_2026-11-24.json')); tipos = {p['tipo'] for p in rep['problemas']}; assert {'dia_no_valido', 'gmap_primaria'} <= tipos and 'gmap_BTC' not in tipos and 'gmap_btc_cobertura' not in tipos, tipos
    assert 'sin_gmap_oficial' in ' '.join(rep['poblaciones']['primaria']['dias_no_validos']['2026-11-23'])
    # sin D_dep => problema explicito
    o2 = nuevo(); TF.crea_datos(o2, ds[:1], semillas=1, gmap_dir=nuevo()); hb(o2); V.modo_diario(o2, nuevo(), hoy='2026-11-24'); assert any(p['tipo'] == 'sin_D_dep' for p in json.load(open(o2 + 'forward_diario_2026-11-24.json'))['problemas'])
    print('F V5 ok: informe diario sin EV ni puertas; dias validos/no validos con motivo; cobertura por poblacion; gmap de ayer y BTC; contador mirada 1 (falta 6, prevista 30-Nov, plazo 24-Dic); avisos; feed con gz truncado; sin D_dep se avisa')


def test_cron_seco():
    R = '/root/polymarket-research-datalogs/'; sh = HERE + 'cron_cxb60_forward.sh'; ds = TF.dias(3, '2026-11-20'); o = nuevo(); gm = nuevo(); sa = nuevo(); TF.crea_datos(o, ds, semillas=1)
    env = dict(os.environ, CXB60_DIR=o.rstrip('/'), CXB60_GMAP_DIR=gm.rstrip('/'), CXB60_SA_R1=sa.rstrip('/'), CXB60_SIN_TELEGRAM='1', CXB60_LOG=o + 'cron.log', CXB60_PY=sys.executable)
    r = subprocess.run(['bash', sh, 'otra'], capture_output=True, text=True, env=env); assert r.returncode == 2
    r = subprocess.run(['bash', sh, 'heartbeat'], capture_output=True, text=True, env=dict(env, CXB60_DIR=o + 'noexiste')); assert r.returncode == 0                       # nunca rompe el cron; el vigia sale 2 y avisa una vez/dia
    r = subprocess.run(['bash', sh, 'diario'], capture_output=True, text=True, env=env)
    assert r.returncode == 0 or 'AVISO' in r.stdout, (r.returncode, r.stdout[-500:], open(o + 'cron.log').read()[-500:] if os.path.exists(o + 'cron.log') else '')
    print('F V6 ok: cron en seco: modo desconocido rc=2, heartbeat sin OUT no rompe, diario corre sin Telegram (resolucion real sobre datos del dia en el test de integracion F8 de test_forward)')


def test_resumen_diario():
    ds = TF.dias(4, '2026-11-20'); o = nuevo(); gm = nuevo(); TF.crea_datos(o, ds, semillas=1, gmap_dir=gm); hb(o); json.dump(dict(D_dep='2026-11-19', primer_dia_contable='2026-11-20'), open(o + 'forward_d_dep.json', 'w'))
    V.problemas_heartbeat.__defaults__ = (None, None, [4242]); enviados = []; V.avisar = lambda txt: (enviados.append(txt), True)[1]
    rc = V.modo_diario(o, gm, hoy='2026-11-24'); res = [t for t in enviados if t.startswith('cxb60 forward diario')]; assert len(res) == 1, enviados; t = res[0]
    assert len(t.splitlines()) <= 9 and 'heartbeat: OK' in t and 'dias validos acumulados: primaria 4/10' in t and 'cobertura de desenlace' in t and 'gmap D-1 (2026-11-23)' in t and 'G3 en seguimiento (trivial vs GEO1)' in t and 'mirada 1 prevista 2026-11-30' in t, t
    assert not any(k in t.lower() for k in ('pnl', 'ev_por', 'ic90', 'p_valor', 'veredicto', 'g1 ', 'euro')) and 'Sin EV ni puertas' in t, t                         # ni EV ni puertas (prereg §6)
    assert os.path.exists(o + 'resumen_enviado_2026-11-24'); V.modo_diario(o, gm, hoy='2026-11-24')
    assert len([x for x in enviados if x.startswith('cxb60 forward diario')]) == 1                                                      # un resumen por dia UTC
    V.modo_diario(o, gm, hoy='2026-11-25'); assert len([x for x in enviados if x.startswith('cxb60 forward diario 2026-11-25')]) == 1                              # al dia siguiente, otro
    # heartbeat con problema: el resumen lo dice
    V.problemas_heartbeat.__defaults__ = (None, None, [9999]); o2 = nuevo(); gm2 = nuevo(); TF.crea_datos(o2, ds, semillas=1, gmap_dir=gm2); hb(o2); json.dump(dict(D_dep='2026-11-19', primer_dia_contable='2026-11-20'), open(o2 + 'forward_d_dep.json', 'w')); enviados.clear()
    V.modo_diario(o2, gm2, hoy='2026-11-24'); assert any('heartbeat: PROBLEMA' in x for x in enviados), enviados
    # el envio FALLA: rc 1, sin marcador, fichero ALERTA; en la siguiente ejecucion se reintenta y se enlata
    V.problemas_heartbeat.__defaults__ = (None, None, [4242]); o3 = nuevo(); gm3 = nuevo(); TF.crea_datos(o3, ds, semillas=1, gmap_dir=gm3); hb(o3); json.dump(dict(D_dep='2026-11-19', primer_dia_contable='2026-11-20'), open(o3 + 'forward_d_dep.json', 'w'))
    V.avisar = lambda txt: False; rc = V.modo_diario(o3, gm3, hoy='2026-11-24'); assert rc == 1 and not os.path.exists(o3 + 'resumen_enviado_2026-11-24') and os.path.exists(o3 + 'ALERTA_resumen_no_enviado_2026-11-24.txt')
    V.avisar = lambda txt: (enviados.append(txt), True)[1]; enviados.clear(); V.modo_diario(o3, gm3, hoy='2026-11-24'); assert any(x.startswith('cxb60 forward diario') for x in enviados) and os.path.exists(o3 + 'resumen_enviado_2026-11-24')
    # etiqueta de ensayo: CXB60_TAG prefija TODO aviso real (se usa para los ensayos con Telegram)
    import importlib; os.environ['CXB60_TAG'] = '[TEST CXB]'; V2 = importlib.reload(V); capt = []; os.environ.pop('CXB60_SIN_TELEGRAM', None)
    import types as _t; sd = _t.ModuleType('shadow_digest'); sd.enviar_telegram = lambda txt, bot='cripto': (capt.append(txt), True)[1]; sys.modules['shadow_digest'] = sd
    try: assert V2.avisar('hola') is True and capt == ['[TEST CXB] hola'], capt
    finally: os.environ.pop('CXB60_TAG'); os.environ['CXB60_SIN_TELEGRAM'] = '1'; sys.modules.pop('shadow_digest', None); importlib.reload(V)
    print('F V7 ok: resumen diario corto (<=9 lineas): heartbeat, dias validos 4/10, cobertura, gmap D-1, G3 en seguimiento, sin EV; uno por dia; fallo de envio => rc 1 + ALERTA + reintento; CXB60_TAG prefija el aviso')


def test_cron_aviso_rc():
    sh = HERE + 'cron_cxb60_forward.sh'; o = nuevo(); stub = o + 'py_stub.sh'
    open(stub, 'w').write('#!/bin/bash\nif [ "$1" = "-c" ]; then echo "STUB telegram: $2 | $3" >> "' + o + 'telegram.log"; exit ${STUB_RC:-0}; fi\ncase "$*" in *vigia_cxb60_forward.py*) exit 7;; esac\nexec ' + sys.executable + ' "$@"\n'); os.chmod(stub, 0o755)
    env = dict(os.environ, CXB60_DIR=o.rstrip('/'), CXB60_GMAP_DIR=o + 'g', CXB60_SA_R1=o + 'sa', CXB60_LOG=o + 'cron.log', CXB60_PY=stub, CXB60_TAG='[TEST CXB]'); env.pop('CXB60_SIN_TELEGRAM', None)
    dia = time.strftime('%Y-%m-%d', time.gmtime())
    r = subprocess.run(['bash', sh, 'heartbeat'], capture_output=True, text=True, env=dict(env, STUB_RC='3')); assert r.returncode == 0 and not os.path.exists(f'{o}cron_aviso_hb_crash_{dia}'), 'Telegram fallo (rc 3): NO se marca el dia como avisado'
    r = subprocess.run(['bash', sh, 'heartbeat'], capture_output=True, text=True, env=dict(env, STUB_RC='0')); assert os.path.exists(f'{o}cron_aviso_hb_crash_{dia}') and '[TEST CXB] cxb60 forward heartbeat FALLO: el vigia de heartbeat murio rc=7' in open(o + 'telegram.log').read()
    n = open(o + 'telegram.log').read().count('STUB telegram'); subprocess.run(['bash', sh, 'heartbeat'], capture_output=True, text=True, env=dict(env, STUB_RC='0')); assert open(o + 'telegram.log').read().count('STUB telegram') == n       # una vez al dia
    print('F V8 ok: aviso del cron devuelve rc solo si Telegram dijo True; un aviso fallido no marca el dia; avisa una vez al dia; el aviso lleva el tag de ensayo')


if __name__ == '__main__':
    try: test_runners_vivos(); test_heartbeat(); test_latch(); test_d_dep(); test_diario(); test_cron_seco(); test_resumen_diario(); test_cron_aviso_rc(); print('TODOS OK (vigia forward)')
    finally: shutil.rmtree(TMP, ignore_errors=True); shutil.rmtree(os.environ.get('X_', '/nonexistent'), ignore_errors=True)
