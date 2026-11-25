"""Tests de _tokens_universo (stage). Gamma/CLOB simulados; sin red. Ejecutar: .venv/bin/python -I test_tokens_universo.py"""
import sys, types, threading, datetime as dt
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import time as _real_time

class Fake:  # estado compartido de los dobles
    universo = {}; gamma = {}; clob = {}; ncalls_gamma = 0; ncalls_clob = 0; reloj = 1_000_000.0
FK = Fake
class Resp:
    def __init__(s, code, js=None, bad=False): s.status_code, s._js, s.bad = code, js, bad
    def raise_for_status(s):
        if s.status_code != 200: raise RuntimeError(f'HTTP {s.status_code}')
    def json(s):
        if s.bad: raise ValueError('json roto')
        return s._js
FK.hook = None; FK.llamadas = []
class Sess:
    def get(s, url, timeout=0):
        if FK.hook: FK.hook(url, timeout)
        FK.llamadas.append((url, timeout, FK.reloj))
        cid = url.rsplit('/', 1)[1]
        if '/markets/0x' not in url:                                  # gamma
            FK.ncalls_gamma += 1; r = FK.gamma.get(cid)
            if isinstance(r, Exception): raise r
            if r is None: return Resp(404)
            if isinstance(r, tuple):
                c = FK.universo.get(cid); d = {'clobTokenIds': json.dumps([r[0], r[1]]), 'outcomes': json.dumps(['Up', 'Down'])}
                if c: d['conditionId'] = c[2]
                return Resp(200, d)
            return r
        FK.ncalls_clob += 1; r = FK.clob.get(cid)
        if isinstance(r, Exception): raise r
        return r if r is not None else Resp(404)
fl = types.ModuleType('fetch_libro_ambos_lados'); fl._universo_activo = lambda: {k: v for k, v in FK.universo.items() if v[3].timestamp() > FK.reloj}
def _parse(q):
    a, n = q.split('|')[:2]; return ('slot', int(n))
fl._parse_updown_tipo = _parse; fl.identificar_activo = lambda q: q.split('|')[0]; fl.ACTIVOS = {'BTC', 'ETH', 'SOL'}; fl.MARCOS_TRACKEADOS = {5, 15, 60}
sys.modules['fetch_libro_ambos_lados'] = fl
import json
import libro_estado_ws as L, tempfile, os
from pathlib import Path
TMP = Path(tempfile.mkdtemp()); L.TOK_CACHE_PATH = TMP / 'cache.json'; MK = Path(tempfile.mkdtemp()); L.TOK_MARKETS_DIR = MK
class T:   # reloj falso
    time = staticmethod(lambda: FK.reloj); sleep = staticmethod(lambda x: None)
L.time = T
_SESION_REAL = L._sesion_datos
L._sesion_datos = lambda: Sess()
L._MARCOS.clear(); L._MARCOS['5min'] = None; L._MARCOS['15min'] = None
FUT = dt.datetime.fromtimestamp(FK.reloj + 3600, dt.timezone.utc)
def reset():
    for d in (L._TOK, L._TOK_FALLO, L._MKT): d.clear()
    L._SIN_CONTRASTE.clear(); L._SC_SRC.clear(); L._SC_ESTADO.clear(); L._ALARMA.clear(); L._CACHE_ENTRIES.clear(); L._CACHE.clear(); L._CACHE.update(cargado=True, sucio=False, prox_intento=0.0, n_err=0, ult_log=0.0, borrar={}, liberar=set(), mt=None); L._TOMB.clear(); L._AYER.update(clave=None, mercados={}); L._GAMMA.pop('ayer_err', None); FK.hook = None; FK.llamadas = []
    for f in TMP.glob('*'): f.unlink()
    for f in MK.glob('*'): f.unlink()
    L._GAMMA.clear(); L._GAMMA['score'] = 0.0; [L._ESTADO.pop(k, None) for k in ('tok_pendientes', 'tok_cuarentena', 'tok_sin_contraste', 'tok_discrepancias', 'cache_err', 'tok_contrastados')]
    if L._REFRESCO_LOCK.locked(): L._REFRESCO_LOCK.release()
    FK.universo = {}; FK.gamma = {}; FK.clob = {}; FK.ncalls_gamma = FK.ncalls_clob = 0; FK.reloj = 1_000_000.0
    L._UNIVERSO = {'toks': None, 'claves': {}, 'meta': {}}
def mk(n, marco='5min', edt=FUT):
    for i in range(n):
        mid = f'm{i}'; cid = '0x' + f'{i:064x}'; FK.universo[mid] = ('BTC', marco, cid, edt)
        FK.gamma[mid] = (f'1{i}', f'2{i}'); FK.clob[cid] = good(cid, f'1{i}', f'2{i}')
def good(cid, y, n, order=('Up', 'Down')):
    tk = {'Up': y, 'Down': n}; return Resp(200, {'condition_id': cid, 'tokens': [{'outcome': o, 'token_id': tk[o]} for o in order]})
res = []
def t(f): 
    try: f(); res.append((f.__name__, 'OK'))
    except AssertionError as e: res.append((f.__name__, f'FALLA {e} @ linea {__import__("traceback").extract_tb(e.__traceback__)[-1].lineno}'))
    except Exception as e: res.append((f.__name__, f'ERROR {type(e).__name__}: {e}'))

def t01_cache_no_repite_gamma():
    reset(); mk(3); a = L._tokens_universo(); g = FK.ncalls_gamma; b = L._tokens_universo()
    assert sorted(a) == sorted(b) and len(a) == 6 and FK.ncalls_gamma == g == 3
def t02_conocido_sobrevive_a_429():
    reset(); mk(3); L._tokens_universo(); FK.gamma = {m: RuntimeError('429') for m in FK.universo}; FK.clob = {}
    FK.reloj += 30; assert len(L._tokens_universo()) == 6
def t03_nuevo_con_gamma_429_usa_clob():
    reset(); mk(2); FK.gamma = {m: RuntimeError('429') for m in FK.universo}; o = L._tokens_universo()
    assert sorted(o) == ['10', '11', '20', '21'] and L._UNIVERSO['meta']['10'][4] == 'YES' and L._UNIVERSO['meta']['20'][4] == 'NO'
def t04_arranque_en_paron_cache_vacia():
    reset(); mk(40); FK.gamma = {m: RuntimeError('429') for m in FK.universo}; o = L._tokens_universo()
    assert len(o) == 80 and 5 <= FK.ncalls_gamma <= 6   # circuito: 5 fallos + 1 sonda
def t05_ambos_fallan_backoff_por_marco_y_reintento():
    reset(); mk(1); FK.gamma = {'m0': RuntimeError('429')}; FK.clob = {'0x' + '0' * 64: Resp(500)}
    assert L._tokens_universo() == [] and FK.ncalls_gamma == 1 and L._ESTADO['tok_pendientes'] == 1
    FK.reloj += 1; L._tokens_universo(); assert FK.ncalls_gamma == 1          # dentro del backoff (2 s +-20 %) no martillea
    FK.reloj += 3; L._tokens_universo(); assert FK.ncalls_gamma == 2
    FK.gamma['m0'] = ('1', '2'); FK.reloj += 15; assert sorted(L._tokens_universo()) == ['1', '2'] and 'm0' not in L._TOK_FALLO
def t06_hallazgo1_backoff_5m_nunca_300s():
    for marco, tope in (('5min', 10), ('15min', 20), ('60min', 60)):
        reset(); L._MARCOS[marco] = None; mk(1, marco=marco); FK.gamma = {'m0': RuntimeError('x')}; FK.clob = {}
        for _ in range(15): FK.reloj += 100; L._tokens_universo()
        assert L._TOK_FALLO['m0'][1] - FK.reloj <= tope * 1.2 + 0.01, (marco, L._TOK_FALLO['m0'][1] - FK.reloj)
        if marco == '60min': L._MARCOS.pop('60min')
    reset(); mk(1, edt=dt.datetime.fromtimestamp(FK.reloj + 20, dt.timezone.utc)); FK.gamma = {'m0': RuntimeError('x')}; FK.clob = {}
    for _ in range(6): L._tokens_universo()
    assert L._TOK_FALLO['m0'][1] - FK.reloj <= 5 * 1.2 + 0.01          # <= vida/4
def t06b_nuevo_5m_con_gamma_y_clob_caidos_se_suscribe_al_volver_clob():
    reset(); mk(1); FK.gamma = {'m0': RuntimeError('429')}; saved = FK.clob; FK.clob = {}; L._tokens_universo(); FK.clob = saved
    FK.reloj += 13; assert sorted(L._tokens_universo()) == ['10', '20']      # <=12 s despues, no 300
def t07_clob_rechazos_fail_closed():
    cid = '0x' + '0' * 64
    casos = {'json roto': Resp(200, bad=True), 'condition distinto': Resp(200, {'condition_id': '0xdead', 'tokens': [{'outcome': 'Up', 'token_id': '1'}, {'outcome': 'Down', 'token_id': '2'}]}),
             '3 tokens': Resp(200, {'condition_id': cid, 'tokens': [{'outcome': 'Up', 'token_id': '1'}, {'outcome': 'Down', 'token_id': '2'}, {'outcome': 'X', 'token_id': '3'}]}),
             'outcomes raros': Resp(200, {'condition_id': cid, 'tokens': [{'outcome': 'Over', 'token_id': '1'}, {'outcome': 'Under', 'token_id': '2'}]}),
             'outcome duplicado': Resp(200, {'condition_id': cid, 'tokens': [{'outcome': 'Up', 'token_id': '1'}, {'outcome': 'Up', 'token_id': '2'}]}),
             'token no numerico': Resp(200, {'condition_id': cid, 'tokens': [{'outcome': 'Up', 'token_id': 'abc'}, {'outcome': 'Down', 'token_id': '2'}]}),
             'mezcla up/no': Resp(200, {'condition_id': cid, 'tokens': [{'outcome': 'Up', 'token_id': '1'}, {'outcome': 'No', 'token_id': '2'}]}),
             'tokens iguales': Resp(200, {'condition_id': cid, 'tokens': [{'outcome': 'Up', 'token_id': '1'}, {'outcome': 'Down', 'token_id': '1'}]}),
             '404': Resp(404), 'timeout': TimeoutError('t'), 'tokens None': Resp(200, {'condition_id': cid, 'tokens': None})}
    for nom, r in casos.items():
        reset(); mk(1); FK.gamma = {'m0': RuntimeError('429')}; FK.clob = {cid: r}
        assert L._tokens_universo() == [], nom
def t08_clob_orden_invertido_se_mapea_por_outcome():
    reset(); mk(1); cid = '0x' + '0' * 64; FK.gamma = {'m0': RuntimeError('x')}; FK.clob = {cid: good(cid, '111', '222', order=('Down', 'Up'))}
    L._tokens_universo(); assert L._TOK['m0'][:2] == ('111', '222')
def t09_gamma_validacion_es_fail_closed_sin_clob_ni_circuito():
    reset(); mk(10); FK.gamma = {m: Resp(200, {'clobTokenIds': '["1", "2"]', 'outcomes': '["Over", "Under"]'}) for m in FK.universo}
    assert L._tokens_universo() == [] and FK.ncalls_clob == 0 and L._GAMMA['score'] == 0.0 and FK.ncalls_gamma == 10
def t09b_transporte_requests_cuenta_y_json_roto_cuenta():
    import requests
    reset(); mk(2); FK.gamma = {'m0': requests.exceptions.HTTPError('429'), 'm1': requests.exceptions.JSONDecodeError('x', '', 0)}
    o = L._tokens_universo(); assert L._GAMMA['score'] == 2.0 and len(o) == 4
def t10_sale_y_vuelve():
    reset(); mk(2); L._tokens_universo(); u = dict(FK.universo); FK.reloj += 7200; FK.universo = {k: v for k, v in u.items() if k != 'm1'}
    L._tokens_universo(); assert set(L._TOK) == {'m0'} or set(L._TOK) == set()      # m1 y m0 vencidos en la cache; m0 sigue en CSV
    FK.universo = u; FK.reloj = 1_000_000.0; FK.universo = {k: (a, m, c, FUT) for k, (a, m, c, e) in u.items()}
    g = FK.ncalls_gamma; assert len(L._tokens_universo()) == 4
def t11_cache_acotada_con_rotacion():
    reset()
    for k in range(300):
        FK.universo = {}; FK.gamma = {}; FK.clob = {}
        for i in range(10):
            mid = f'r{k}_{i}'; cid = '0x' + f'{k * 10 + i:064x}'
            FK.universo[mid] = ('ETH', '5min', cid, dt.datetime.fromtimestamp(FK.reloj + 300, dt.timezone.utc)); FK.gamma[mid] = (f'{k}{i}1', f'{k}{i}2')
        L._tokens_universo(); FK.reloj += 60
    assert len(L._TOK) <= 60 and len(L._MKT) == len(L._TOK) and len(L._TOK_FALLO) == 0     # solo los vigentes (5 min = 5 rondas)
def t11b_tope_duro_solo_de_lo_retenido():
    reset(); L.TOK_MKT_MAX = 50
    try:
        mk(80); full = dict(FK.universo); L._tokens_universo(); assert len(L._TOK) == 80          # en CSV: nunca se descarta (evita rebote)
        FK.universo = {}; L._tokens_universo(); assert len(L._MKT) <= 50 and len(L._TOK) <= 50
    finally: L.TOK_MKT_MAX = 3000
def t12_concurrencia():
    reset(); mk(20); out = []
    th = [threading.Thread(target=lambda: out.append(sorted(L._tokens_universo()))) for _ in range(8)]
    [x.start() for x in th]; [x.join() for x in th]
    assert FK.ncalls_gamma == 20 and sum(len(o) == 40 for o in out) >= 1 and all(len(o) in (0, 40) for o in out)
def t13_hallazgo2_universo_parcial_no_poda():
    reset(); mk(131); L._tokens_universo(); full = dict(FK.universo)
    FK.universo = {k: full[k] for k in ('m0', 'm1', 'm2')}; FK.gamma = {m: RuntimeError('429') for m in full}; FK.clob = {}
    o = L._tokens_universo(); assert len(o) == 262 and len(L._UNIVERSO['meta']) == 262 and len(L._TOK) == 131
    FK.reloj += 7200; assert L._tokens_universo() == [] and len(L._TOK) == 0      # vencidos: ahora si fuera (los 3 del CSV tambien: edt vencido)
def t13b_parcial_con_mercados_vencidos_se_podan_y_nuevos_entran():
    reset(); mk(10); L._tokens_universo()
    FK.reloj += 1800
    # 5 mercados de la cache vencen a los 1500 s; el CSV parcial trae uno nuevo
    for m in ('m0', 'm1', 'm2', 'm3', 'm4'):
        a, mc, c, e = L._MKT[m]; L._MKT[m] = (a, mc, c, dt.datetime.fromtimestamp(FK.reloj - 10, dt.timezone.utc))
    FK.universo = {'nuevo': ('BTC', '5min', '0x' + 'f' * 64, FUT)}; FK.gamma['nuevo'] = ('777', '888')
    o = L._tokens_universo(); assert len(o) == 2 * 5 + 2 and set(L._TOK) == {'m5', 'm6', 'm7', 'm8', 'm9', 'nuevo'}
def t13c_universo_vacio_conserva_y_respeta_extra_y_poda_fallo():
    reset(); mk(3); L._tokens_universo(); L._TOK_FALLO['fantasma'] = (3, FK.reloj + 99, 0); L._HIST['999'] = []; L._EXTRA['999'] = FK.reloj + 500
    FK.universo = {}; o = L._tokens_universo(); assert len(o) == 6 and 'fantasma' not in L._TOK_FALLO
    assert all(t in L._UNIVERSO['meta'] and t in L._UNIVERSO['claves'] for t in o) and set(L._TOK) == {'m0', 'm1', 'm2'}
    L._podar(set(o) | set(L._EXTRA)); assert '999' in L._HIST; L._HIST.pop('999'); L._EXTRA.pop('999')
def t15_filtro_marcos():
    reset(); mk(2, marco='60min'); assert L._tokens_universo() == []        # 60min no pedido -> 'no'
    L._MARCOS['60min'] = {'ETH'}; assert L._tokens_universo() == []; L._MARCOS['60min'] = {'BTC'}; assert len(L._tokens_universo()) == 4; L._MARCOS.pop('60min')
def t16_tasa_llamadas_con_ambos_caidos():
    reset(); mk(100); FK.gamma = {m: RuntimeError('429') for m in FK.universo}; FK.clob = {}
    for _ in range(240): FK.reloj += 5; L._tokens_universo()       # 20 min de caida total, refresco de 5 s
    assert FK.ncalls_gamma < 100 * 40 and FK.ncalls_clob < 100 * 130, (FK.ncalls_gamma, FK.ncalls_clob)
def t17_hallazgo3_red_fuera_de_cerrojos_y_presupuesto():
    reset(); mk(60); vistos = []
    def h(url, timeout):
        vistos.append(L._TOK_LOCK.locked() or L._LOCK.locked()); FK.reloj += 0.5       # cada llamada tarda 0,5 s
    FK.hook = h
    L._tokens_universo(); assert not any(vistos) and 18 <= FK.ncalls_gamma <= 22 and L._ESTADO['tok_pendientes'] >= 38      # presupuesto 20 s (gamma+clob)
    FK.hook = None; L._tokens_universo(); L._tokens_universo(); L._tokens_universo(); assert len(L._TOK) == 60                  # el resto al siguiente
def t18_circuito_decae_no_se_reinicia_con_un_exito():
    reset(); mk(10); L._GAMMA['score'] = 8.0; FK.gamma['m0'] = ('1', '2'); FK.gamma['m1'] = ('3', '4')
    L._tokens_universo(); assert FK.ncalls_gamma == 1                  # abierto: una sola sonda; el resto por CLOB
    assert abs(L._GAMMA['score'] - 8.0 * L.TOK_GAMMA_DECAY) < 1e-9 and L._GAMMA['score'] >= L.TOK_GAMMA_SCORE_MAX      # un exito no lo reinicia ni lo cierra
def t19_hallazgo4_publicacion_atomica():
    reset(); mk(30); stop = []; malos = []
    def lector():
        while not stop:
            u = L._UNIVERSO
            if u['toks'] is not None and not (set(u['claves']) == set(u['meta']) == set(u['toks'])): malos.append(1)
    th = threading.Thread(target=lector); th.start()
    try:
        for k in range(200):
            FK.universo = {m: v for i, (m, v) in enumerate(FK.universo.items()) if i % (k % 3 + 1) == 0} if k % 5 else dict(FK.universo); L._tokens_universo()
    finally: stop.append(1); th.join()
    assert not malos
    reset(); mk(5); L._tokens_universo(); old = L._UNIVERSO; foto = (list(old['toks']), dict(old['claves']), dict(old['meta']))
    FK.universo = {}; mk(7); L._tokens_universo()
    assert L._UNIVERSO is not old and (list(old['toks']), dict(old['claves']), dict(old['meta'])) == foto     # dict nuevo, el anterior intacto
def t20_hallazgo5_tipos():
    reset(); mk(2); L._tokens_universo(); assert all(len(v) == 2 for v in L._TOK.values()) and L.random.__name__ == 'random'
def t21_validacion_en_clob_no_toca_circuito_y_es_fail_closed():
    reset(); mk(3); FK.gamma = {m: RuntimeError('x') for m in FK.universo}
    for m in FK.universo.values(): FK.clob[m[2]] = Resp(200, {'condition_id': m[2], 'tokens': []})
    assert L._tokens_universo() == [] and L._GAMMA['score'] == 3.0
def t22_pendientes_acortan_refresco():
    reset(); mk(1); FK.gamma = {'m0': RuntimeError('x')}; FK.clob = {}; L._tokens_universo(); assert L._ESTADO['tok_pendientes'] == 1
    FK.gamma['m0'] = ('1', '2'); FK.reloj += 15; L._tokens_universo(); assert L._ESTADO['tok_pendientes'] == 0

def t23_A_cuarentena_por_mercado_no_mantiene_refresco_corto():
    reset(); mk(3); FK.gamma['m1'] = Resp(200, {'clobTokenIds': '["5", "5"]', 'outcomes': '["Up", "Down"]'})          # un mercado con fallo de validacion persistente
    logs = []; old = L._log; L._log = lambda m: logs.append(m)
    try:
        for _ in range(12): FK.reloj += 100; L._tokens_universo()                   # cada intento tras su espera (max 72 s)
    finally: L._log = old
    assert L._TOK_FALLO['m1'][0] >= L.TOK_CUARENTENA_N and L._ESTADO['tok_cuarentena'] == 1
    assert L._ESTADO['tok_pendientes'] == 0                                           # ya NO acorta el refresco
    assert sum('cuarentena' in m for m in logs) == 1                                  # log unico
    g = FK.ncalls_gamma; FK.reloj += 10; L._tokens_universo(); assert FK.ncalls_gamma == g          # dentro de los ~60 s no reintenta
    FK.reloj += 80; L._tokens_universo(); assert FK.ncalls_gamma == g + 1               # a ~60 s si
    assert len(L._UNIVERSO['toks']) == 4                                                # los otros siguen suscritos
def t24_B_swap_gamma_vs_clob_no_suscribe_y_alarma():
    reset(); mk(2); cid0 = '0x' + '0' * 64; FK.clob[cid0] = good(cid0, '20', '10')   # clob: YES/NO invertidos respecto a gamma
    logs = []; old = L._log; L._log = lambda m: logs.append(m)
    try: o = L._tokens_universo()
    finally: L._log = old
    assert sorted(o) == ['11', '21'] and 'm0' not in L._TOK and any('ALARMA' in m and 'm0' in m for m in logs)
def t25_B_contraste_clob_cae_acepta_gamma_sin_contraste():
    reset(); mk(2); FK.clob = {c: TimeoutError('t') for c in FK.clob}
    o = L._tokens_universo(); assert len(o) == 4 and L._SIN_CONTRASTE == {'m0', 'm1'} and L._ESTADO['tok_sin_contraste'] == 2
    FK.clob = {}; FK.reloj += 5; L._tokens_universo(); assert L._ESTADO['tok_sin_contraste'] == 2        # persiste mientras viva
def t26_B_clob_fallback_tambien_marca_sin_contraste():
    reset(); mk(1); FK.gamma = {'m0': RuntimeError('429')}; L._tokens_universo(); assert L._SIN_CONTRASTE == {'m0'}
def t27_B_contraste_coincide_no_marca():
    reset(); mk(2); L._tokens_universo(); assert not L._SIN_CONTRASTE and FK.ncalls_clob == 2
def t28_C_persistencia_atomica_y_carga_en_frio_sin_gamma_ni_csv():
    reset(); mk(6); L._tokens_universo(); assert L.TOK_CACHE_PATH.exists() and not list(TMP.glob('*.tmp*'))
    j = json.loads(L.TOK_CACHE_PATH.read_text()); assert j['v'] == 1 and len(j['mercados']) == 6 and 'edt' in j['mercados']['m0']
    # reinicio durante un paron: cache vacia en memoria, CSV vacio, gamma y clob caidos
    for d in (L._TOK, L._MKT, L._TOK_FALLO): d.clear()
    c0 = FK.ncalls_clob; L._CACHE.update(cargado=False, sucio=False); FK.universo = {}; FK.gamma = {m: RuntimeError('429') for m in FK.gamma}; FK.clob = {}
    g0 = FK.ncalls_gamma; o = L._tokens_universo(); assert FK.ncalls_gamma == g0 and FK.ncalls_clob == c0       # el arranque en frio no llama a gamma ni a clob
    assert len(o) == 12 and L._ESTADO['tok_pendientes'] == 1                      # publica ya y pide refresco corto
    assert len(L._tokens_universo()) == 12                                         # siguiente refresco (CSV vacio): lo retenido sigue
def t29_C_carga_valida_vigencia_y_basura():
    reset(); mk(3); L._tokens_universo(); j = json.loads(L.TOK_CACHE_PATH.read_text())
    j['mercados']['m0']['edt'] = dt.datetime.fromtimestamp(FK.reloj - 5, dt.timezone.utc).isoformat()       # vencido
    j['mercados']['m1']['yes'] = 'abc'                                                                      # token no numerico
    j['mercados']['m2']['no'] = j['mercados']['m2']['yes']                                                  # tokens iguales
    j['mercados']['mx'] = {'yes': '1'}                                                                      # incompleto
    L.TOK_CACHE_PATH.write_text(json.dumps(j))
    for d in (L._TOK, L._MKT): d.clear()
    assert L._cache_cargar(FK.reloj) == 0 and not L._TOK
    for malo in ('{{no json', json.dumps({'v': 99, 'mercados': {}}), json.dumps([1, 2]), json.dumps({'v': 1, 'mercados': 5}), ''):
        L.TOK_CACHE_PATH.write_text(malo); assert L._cache_cargar(FK.reloj) == 0
    L.TOK_CACHE_PATH.unlink(); assert L._cache_cargar(FK.reloj) == 0
def t30_C_cache_corrupta_en_arranque_cae_al_camino_normal():
    reset(); mk(3); L.TOK_CACHE_PATH.write_text('{{basura'); L._CACHE.update(cargado=False)
    o = L._tokens_universo(); assert len(o) == 6 and FK.ncalls_gamma == 3
def t31_C_fallo_de_escritura_no_rompe_el_refresco():
    reset(); mk(2); old = L.TOK_CACHE_PATH; L.TOK_CACHE_PATH = TMP / 'no_existe' / 'c.json'
    try: assert len(L._tokens_universo()) == 4
    finally: L.TOK_CACHE_PATH = old
def t32_C_sin_escritura_si_no_hay_cambios():
    reset(); mk(2); L._tokens_universo(); m1 = L.TOK_CACHE_PATH.stat().st_mtime_ns; FK.reloj += 30; L._tokens_universo(); assert L.TOK_CACHE_PATH.stat().st_mtime_ns == m1
def t33_C_marco_no_registrado_aun_no_se_poda_ni_se_borra_de_disco():
    reset(); mk(2, marco='60min'); L._MARCOS['60min'] = None; L._tokens_universo(); L._MARCOS.pop('60min')
    L._tokens_universo(); assert len(L._MKT) == 2 and len(json.loads(L.TOK_CACHE_PATH.read_text())['mercados']) == 2 and L._UNIVERSO['toks'] == []
    L._MARCOS['60min'] = None; g = FK.ncalls_gamma; assert len(L._tokens_universo()) == 4 and FK.ncalls_gamma == g; L._MARCOS.pop('60min')
def t34_iniciar_despierta_universo_solo_si_cambian_marcos():
    L._REFRESCO_EVT.clear(); L._ESTADO['iniciado'] = True
    try:
        L.iniciar(('5min',)); assert not L._REFRESCO_EVT.is_set()                  # ya estaba (None): sin cambio
        L.iniciar(('777min',)); assert L._REFRESCO_EVT.is_set(); L._REFRESCO_EVT.clear()
        L.iniciar(('777min',)); assert not L._REFRESCO_EVT.is_set()
        L.iniciar(('888min',), activos=['BTC']); assert L._REFRESCO_EVT.is_set(); L._REFRESCO_EVT.clear()
        L.iniciar(('888min',), activos=['BTC']); assert not L._REFRESCO_EVT.is_set()
    finally: L._ESTADO['iniciado'] = False; L._MARCOS.pop('777min', None); L._MARCOS.pop('888min', None)

CID0 = '0x' + '0' * 64
def silencio():
    logs = []; old = L._log; L._log = lambda m: logs.append(m); return logs, old
def t35_H1_cache_compartida_multiproceso_real():
    """3 procesos (fork) con marcos distintos escriben a la vez: ninguno pierde los mercados del otro y el fichero nunca se ve truncado/ilegible."""
    import multiprocessing as mp
    reset(); L._CACHE.update(prox_intento=0.0)
    def hijo(k):
        L._CACHE_ENTRIES.clear(); L._CACHE.update(prox_intento=0.0, n_err=0, sucio=True)
        for r in range(25):
            for i in range(8):
                mid = f'p{k}_{r}_{i}'
                L._CACHE_ENTRIES[mid] = {'yes': f'{k}{r}{i}1', 'no': f'{k}{r}{i}2', 'activo': 'BTC', 'marco': ('5min', '15min', '60min')[k], 'cid': '0x' + f'{k}{r}{i}'.rjust(64, '0'),
                                         'edt': FUT.isoformat(), 'sc': False}
            L._CACHE['sucio'] = True; L._CACHE['prox_intento'] = 0.0; L._cache_guardar()
        os._exit(0 if L._CACHE['n_err'] == 0 else 3)
    ctx = mp.get_context('fork'); ps = [ctx.Process(target=hijo, args=(k,)) for k in range(3)]
    malos = []; stop = []
    def lector():
        while not stop:
            try: j = json.loads(L.TOK_CACHE_PATH.read_text()); assert j['v'] == 1 and isinstance(j['mercados'], dict)
            except FileNotFoundError: pass
            except Exception as e: malos.append(repr(e))
    th = threading.Thread(target=lector); th.start()
    [p.start() for p in ps]; [p.join(60) for p in ps]; stop.append(1); th.join()
    assert [p.exitcode for p in ps] == [0, 0, 0], [p.exitcode for p in ps]
    assert not malos, malos[:2]
    m = json.loads(L.TOK_CACHE_PATH.read_text())['mercados']
    assert len(m) == 3 * 25 * 8, len(m)                                    # union completa: nadie pisa a otro con un subconjunto
    assert {k.split('_')[0] for k in m} == {'p0', 'p1', 'p2'} and not list(TMP.glob('*.tmp.*'))
def t36_H1_fusion_con_disco_no_pierde_los_de_otro_marco():
    reset(); mk(2); L._tokens_universo()
    j = json.loads(L.TOK_CACHE_PATH.read_text()); j['mercados']['otro'] = {'yes': '9', 'no': '8', 'activo': 'ETH', 'marco': '60min', 'cid': '0x' + '9' * 64, 'edt': FUT.isoformat(), 'sc': False}
    L.TOK_CACHE_PATH.write_text(json.dumps(j))                              # otro proceso escribio un mercado que NO conocemos
    FK.universo = {}; mk(3); L._tokens_universo()                           # nuevo mercado nuestro -> escritura
    assert 'otro' in json.loads(L.TOK_CACHE_PATH.read_text())['mercados']
def t37_H2_incompleto_no_es_incoherente_clob_inmediato():
    reset(); mk(1)
    for g in (Resp(200, {'conditionId': CID0, 'clobTokenIds': '', 'outcomes': ''}), Resp(200, {'conditionId': CID0}), Resp(200, {'conditionId': CID0, 'clobTokenIds': None, 'outcomes': None}),
              Resp(200, {'conditionId': CID0, 'clobTokenIds': '[]', 'outcomes': '[]'})):
        reset(); mk(1); FK.gamma = {'m0': g}; o = L._tokens_universo()
        assert sorted(o) == ['10', '20'] and FK.ncalls_clob == 1 and L._SIN_CONTRASTE == {'m0'}, g._js     # CLOB en la misma ronda, no espera
        assert L._GAMMA['score'] == 0.0                                     # gamma contesto: no es caida
def t38_H2_incompleto_en_ambos_nunca_cuarentena_reintento_corto():
    reset(); mk(1); FK.gamma = {'m0': Resp(200, {'conditionId': CID0, 'clobTokenIds': '', 'outcomes': ''})}; FK.clob = {CID0: Resp(200, {'condition_id': CID0, 'tokens': []})}
    logs, old = silencio()
    try:
        for _ in range(30): FK.reloj += 30; L._tokens_universo()
    finally: L._log = old
    assert L._ESTADO['tok_cuarentena'] == 0 and L._TOK_FALLO['m0'][2] == 0 and not any('cuarentena' in m for m in logs)
    assert L._TOK_FALLO['m0'][1] - FK.reloj <= 10 * 1.2 + 0.01              # 5m: reintento <= 10 s siempre
    FK.clob = {CID0: good(CID0, '1', '2')}; FK.reloj += 15; assert sorted(L._tokens_universo()) == ['1', '2']      # el mercado aparece y se suscribe
def t39_H2_transporte_clasificado_incluye_errores_raros():
    import requests
    casos = {'lista': Resp(200, ['x']), 'None': Resp(200, None), 'error': Resp(200, {'error': 'rate limited'}), 'message': Resp(200, {'message': 'Too Many Requests'}),
             'json roto': Resp(200, bad=True), '429': Resp(429), 'AttributeError': AttributeError('x'), 'TypeError': TypeError('x'), 'req': requests.exceptions.ConnectionError('x'),
             'str': Resp(200, 'texto')}
    for nom, g in casos.items():
        reset(); mk(1); FK.gamma = {'m0': g}; o = L._tokens_universo()
        assert sorted(o) == ['10', '20'] and L._GAMMA['score'] == 1.0 and L._TOK_FALLO.get('m0') is None, nom       # transporte: circuito +1 y fallback a CLOB
    for nom, c in {'AttributeError': AttributeError('x'), 'error': Resp(200, {'error': 'x'}), 'lista': Resp(200, [1])}.items():
        reset(); mk(1); FK.gamma = {'m0': RuntimeError('x')}; FK.clob = {CID0: c}; assert L._tokens_universo() == [] and L._TOK_FALLO['m0'][2] == 0, nom      # transporte en CLOB: no incoherencia
def t40_H2_incoherente_cuarentena_solo_tras_n():
    reset(); mk(2); FK.gamma['m0'] = Resp(200, {'conditionId': CID0, 'clobTokenIds': '["5","5"]', 'outcomes': '["Up","Down"]'})
    for k in range(1, 5): FK.reloj += 100; L._tokens_universo(); assert L._ESTADO['tok_cuarentena'] == 0 and L._TOK_FALLO['m0'][2] == k
    FK.reloj += 100; L._tokens_universo(); assert L._ESTADO['tok_cuarentena'] == 1
    assert 'm0' not in L._TOK and 'm1' in L._TOK
    reset(); mk(1); FK.gamma = {'m0': Resp(200, {'conditionId': '0xdead', 'clobTokenIds': '["1","2"]', 'outcomes': '["Up","Down"]'})}
    assert L._tokens_universo() == [] and FK.ncalls_clob == 0           # conditionId distinto del CSV: incoherente, fail-closed
def t41_H3_latch_alarma_una_por_episodio_y_contador():
    reset(); mk(2); FK.clob[CID0] = good(CID0, '20', '10'); logs, old = silencio()
    try:
        for _ in range(12): FK.reloj += 100; L._tokens_universo()
        n1 = sum('ALARMA' in m for m in logs); assert n1 == 1 and L._ESTADO['tok_discrepancias'] == 1 and L._ALARMA['m0'] >= 5, (n1, L._ALARMA)
        FK.clob[CID0] = good(CID0, '10', '20'); FK.reloj += 100; L._tokens_universo()
        assert 'm0' in L._TOK and 'm0' not in L._ALARMA and L._ESTADO['tok_discrepancias'] == 0          # episodio cerrado
    finally: L._log = old
def t42_H3_validacion_clob_es_dudoso_transporte_es_sin_contraste():
    reset(); mk(1); FK.clob = {CID0: Resp(200, {'condition_id': CID0, 'tokens': [{'outcome': 'Up', 'token_id': '1'}, {'outcome': 'Down', 'token_id': '2'}, {'outcome': 'X', 'token_id': '3'}]})}
    assert L._tokens_universo() == [] and 'm0' not in L._SIN_CONTRASTE                       # CLOB incoherente: gamma NO basta
    for c in (TimeoutError('t'), Resp(500), Resp(404), Resp(200, bad=True), Resp(200, {'error': 'x'})):
        reset(); mk(1); FK.clob = {CID0: c}; assert sorted(L._tokens_universo()) == ['10', '20'] and L._SIN_CONTRASTE == {'m0'}
def t43_H4_deadline_por_llamada_timeout_acotado():
    reset(); mk(30); FK.hook = lambda url, timeout: setattr(FK, 'reloj', FK.reloj + 3.0)      # cada llamada gasta 3 s del reloj
    L._tokens_universo()
    t0 = 1_000_000.0 + 0.0
    assert FK.llamadas, 'sin llamadas'
    for url, to, reloj in FK.llamadas:
        conn, rd = to; restante = (t0 + L.TOK_PRESUPUESTO_S) - (reloj - 3.0 + 3.0 * 0)         # reloj ya avanzado 3 por el hook: restante al llamar = deadline-(reloj-3)
        assert rd <= L.TOK_GAMMA_TIMEOUT_S and conn <= 3.0 and rd <= (t0 + L.TOK_PRESUPUESTO_S) - (reloj - 3.0) + 1e-6, (to, reloj)
    ult = FK.llamadas[-1][2] - 3.0
    assert ult < t0 + L.TOK_PRESUPUESTO_S - L.TOK_MIN_RESTANTE_S + 1e-6                          # ninguna llamada empieza con menos de TOK_MIN_RESTANTE_S
    assert FK.reloj - t0 <= L.TOK_PRESUPUESTO_S + 3.0 + 1e-6 and L._ESTADO['tok_pendientes'] > 0
def t44_H4_universo_y_enviar_no_dependen_de_los_cerrojos_de_red():
    import inspect
    for f in (L._enviar_deseados, L._podar, L._universo):
        src = inspect.getsource(f); assert '_REFRESCO_LOCK' not in src and '_TOK_LOCK' not in src, f.__name__
    reset(); mk(3); L._tokens_universo()
    L._REFRESCO_LOCK.acquire(); L._TOK_LOCK.acquire()                                              # una ronda de red "colgada" sostiene ambos
    try:
        assert len(L._universo()['toks']) == 6 and len(L._tokens_universo()) == 6                    # el que no coge el cerrojo devuelve lo ultimo publicado
    finally: L._TOK_LOCK.release(); L._REFRESCO_LOCK.release()
def t45_H5_tope_conserva_los_que_vencen_antes_y_desde_disco():
    reset(); L.TOK_MKT_MAX = 5
    try:
        for i in range(12):
            mid = f'r{i}'; cid = '0x' + f'{i:064x}'; edt = dt.datetime.fromtimestamp(FK.reloj + 100 + (11 - i) * 50, dt.timezone.utc)   # r11 vence primero
            FK.universo[mid] = ('BTC', '5min', cid, edt); FK.gamma[mid] = (f'1{i}', f'2{i}'); FK.clob[cid] = good(cid, f'1{i}', f'2{i}')
        L._tokens_universo(); assert len(L._TOK) == 12
        FK.universo = {}; L._tokens_universo()
        assert set(L._TOK) == {f'r{i}' for i in range(7, 12)} and set(L._MKT) == set(L._TOK) and set(L._CACHE_ENTRIES) == set(L._TOK)     # los 5 mas inminentes
        reset(); L.TOK_MKT_MAX = 12
        for i in range(12):
            mid = f'r{i}'; cid = '0x' + f'{i:064x}'; edt = dt.datetime.fromtimestamp(FK.reloj + 100 + (11 - i) * 50, dt.timezone.utc)
            FK.universo[mid] = ('BTC', '5min', cid, edt); FK.gamma[mid] = (f'1{i}', f'2{i}')
        L._tokens_universo(); L.TOK_MKT_MAX = 5
        for d in (L._TOK, L._MKT, L._CACHE_ENTRIES): d.clear()
        assert L._cache_cargar(FK.reloj) == 5 and set(L._TOK) == {f'r{i}' for i in range(7, 12)}                                           # ordenado por edt al cargar
    finally: L.TOK_MKT_MAX = 3000
def t46_H5_poda_atomica_bajo_un_solo_cerrojo_conserva_backoff_de_vivos():
    reset(); mk(3); FK.gamma = {m: RuntimeError('x') for m in FK.universo}; FK.clob = {}; L._tokens_universo()
    bo = dict(L._TOK_FALLO); assert len(bo) == 3
    FK.universo = {k: v for k, v in FK.universo.items() if k != 'm2'}; FK.reloj += 1; L._tokens_universo()
    assert {k: v for k, v in L._TOK_FALLO.items() if k != 'm2'} == {k: v for k, v in bo.items() if k != 'm2'} or L._TOK_FALLO['m0'][0] >= bo['m0'][0]
    assert 'm2' not in L._TOK_FALLO                                                                  # no esta en cand (CSV sin el y sin _MKT): se poda
    import inspect; src = inspect.getsource(L._tokens_universo); assert src.count('_olvidar(m)') >= 2
def t47_H6_arranque_en_frio_refiltra_edt_al_publicar():
    reset(); mk(4); soon = dt.datetime.fromtimestamp(FK.reloj + 100, dt.timezone.utc)
    FK.universo['m0'] = ('BTC', '5min', FK.universo['m0'][2], soon); FK.universo['m1'] = ('BTC', '5min', FK.universo['m1'][2], soon); L._tokens_universo()
    for d in (L._TOK, L._MKT, L._TOK_FALLO, L._CACHE_ENTRIES): d.clear()
    L._CACHE.update(cargado=False); orig = L._cache_cargar
    def carga_y_pasa_el_tiempo(ahora):
        n = orig(ahora); FK.reloj += 200; return n                                                     # entre validar y publicar vencen m0 y m1
    L._cache_cargar = carga_y_pasa_el_tiempo
    try: o = L._tokens_universo()
    finally: L._cache_cargar = orig
    assert sorted(o) == ['12', '13', '22', '23'] and sorted(L._UNIVERSO['claves']) == sorted(o), o
    # y si el refresco corto falla (CSV ilegible) no se conservan tokens vencidos
    FK.reloj += 4000; fl._universo_activo = lambda: (_ for _ in ()).throw(OSError('csv'))
    logs, old = silencio()
    try: assert L._tokens_universo() == [] and not L._MKT
    finally: L._log = old; fl._universo_activo = lambda: {k: v for k, v in FK.universo.items() if v[3].timestamp() > FK.reloj}
def t48_H7_universo_api_privada_getter_y_nadie_lo_importa():
    reset(); mk(2); L._tokens_universo(); assert L._universo() is L._UNIVERSO and set(L._universo()) == {'toks', 'claves', 'meta'}
    import re, glob
    pp = Path(__file__).resolve().parents; raiz = pp[6] if len(pp) > 6 else Path('/nonexistent')
    if (raiz / 'libro_estado_ws.py').exists():
        pat = re.compile(r'(libro_estado_ws|\bLE|\bles)\._UNIVERSO|from\s+libro_estado_ws\s+import[^\n]*_UNIVERSO')
        malos = [f for f in glob.glob(str(raiz / '*.py')) if pat.search(open(f, errors='ignore').read()) and not f.endswith('libro_estado_ws.py')]
        assert not malos, malos
def t49_H8_iniciar_no_pierde_el_aviso_y_compara_claves_y_valores():
    L._ESTADO['iniciado'] = True; g0 = L._MARCOS_GEN[0]; L._REFRESCO_EVT.clear()
    try:
        L.iniciar(('5min',), activos=['BTC']); assert L._MARCOS_GEN[0] == g0 and not L._REFRESCO_EVT.is_set()       # 5min ya es None (todos): sin cambio
        L.iniciar(('777min',), activos=['BTC']); assert L._MARCOS_GEN[0] == g0 + 1 and L._REFRESCO_EVT.is_set(); L._REFRESCO_EVT.clear()
        L.iniciar(('777min',), activos=['ETH']); assert L._MARCOS_GEN[0] == g0 + 2 and L._MARCOS['777min'] == {'BTC', 'ETH'} and L._REFRESCO_EVT.is_set()   # mismo marco, activos nuevos
        L.iniciar(('777min',), activos=['ETH']); assert L._MARCOS_GEN[0] == g0 + 2
    finally: L._ESTADO['iniciado'] = False; L._MARCOS.pop('777min', None); L._REFRESCO_EVT.clear()
    # carrera: iniciar() llega DURANTE la ronda del hilo (despues de su clear): no se duerme REFRESCO_S
    rondas = []; o = (L._tokens_universo, L._enviar_deseados, L._podar, L.REFRESCO_S, L.TOK_REFRESCO_PENDIENTES_S)
    def ronda():
        rondas.append(1)
        if len(rondas) == 1:
            L._ESTADO['iniciado'] = True; L.iniciar(('888min',))
        if len(rondas) >= 3: raise SystemExit
        return []
    L._tokens_universo = ronda; L._enviar_deseados = lambda: None; L._podar = lambda s: None; L.REFRESCO_S = L.TOK_REFRESCO_PENDIENTES_S = 1000
    th = threading.Thread(target=L._hilo_universo, daemon=True); th.start()
    try:
        _real_time.sleep(1.0); assert len(rondas) >= 2, rondas                 # 2a ronda inmediata (sin dormir 1000 s)
    finally:
        L._REFRESCO_EVT.set(); th.join(3); L._tokens_universo, L._enviar_deseados, L._podar, L.REFRESCO_S, L.TOK_REFRESCO_PENDIENTES_S = o
        L._ESTADO['iniciado'] = False; L._MARCOS.pop('888min', None); L._REFRESCO_EVT.clear()
def t50_H9_sesion_propia_sin_live_trade():
    import requests
    src = open(L.__file__).read(); lineas = src.splitlines()
    assert 'live_trade' not in sys.modules                                                              # el modulo no lo importa (ni de forma perezosa)
    assert not any(l.strip().startswith(('import live_trade', 'from live_trade')) or '_SESSION' in l.split('#')[0] for l in lineas)
    assert 'import requests' in lineas                                                                  # a nivel de modulo
    viejo = L._sesion_datos; L._sesion_datos = _SESION_REAL; L._SESION['s'] = None
    try:
        s1 = L._sesion_datos(); assert isinstance(s1, requests.Session) and L._sesion_datos() is s1 and s1 is not requests.Session()
        a = s1.get_adapter('https://x'); assert a._pool_maxsize == 4 and a.max_retries.total == 0
    finally: L._SESION['s'] = None; L._sesion_datos = viejo
def t51_H10_fallo_de_cache_backoff_metrica_y_log_acotado():
    reset(); mk(2); old = L.TOK_CACHE_PATH; L.TOK_CACHE_PATH = TMP / 'no_existe' / 'c.json'; logs, ol = silencio()
    try:
        for _ in range(40):
            FK.reloj += 5; L._CACHE['sucio'] = True; L._cache_guardar()                                 # 200 s de fallo continuo, intentos cada 5 s
        n_err, n_log = L._ESTADO['cache_err'], sum('no se pudo escribir' in m for m in logs)
        assert n_log == 1 and 1 < n_err < 20 and L._CACHE['sucio'] and L._CACHE['n_err'] == n_err, (n_log, n_err)       # backoff: pocos intentos, 1 log, metrica visible
        L.TOK_CACHE_PATH = old; FK.reloj += 400; L._CACHE_ENTRIES.update({'m0': L._CACHE_ENTRIES.get('m0') or {}})
        L._cache_guardar(); assert not L._CACHE['sucio'] and L._CACHE['n_err'] == 0 and old.exists()
    finally: L.TOK_CACHE_PATH = old; L._log = ol
    reset(); mk(2); L._tokens_universo(); t0 = L._CACHE['sucio']
    import inspect; assert 'for ' not in inspect.getsource(L._cache_guardar).split('mias = dict(_CACHE_ENTRIES)')[0].split('with _TOK_LOCK:')[-1]     # no reconstruye el dict bajo el cerrojo

def solo_clob_por_429(n):
    """n mercados aceptados SOLO por CLOB (gamma 429 en el alta); deja gamma caido y el circuito abierto."""
    reset(); mk(n); gam = dict(FK.gamma); FK.gamma = {m: RuntimeError('429') for m in FK.universo}; L._tokens_universo()
    assert L._SIN_CONTRASTE == set(FK.universo) and all(L._SC_SRC[m] == 'clob' for m in FK.universo)
    return gam
def t52_R1_recontraste_tras_recuperacion_de_gamma_baja_a_cero_y_persiste():
    gam = solo_clob_por_429(12); assert L._ESTADO['tok_sin_contraste'] == 12 and L._GAMMA['score'] >= L.TOK_GAMMA_SCORE_MAX
    g0 = FK.ncalls_gamma; FK.reloj += 30; L._tokens_universo(); assert FK.ncalls_gamma == g0 + 1      # gamma sigue caida: solo la sonda, no martillea
    FK.gamma = gam; hist = []
    for _ in range(6):
        FK.reloj += 30; g = FK.ncalls_gamma; L._tokens_universo(); hist.append((FK.ncalls_gamma - g, L._ESTADO['tok_sin_contraste']))
    assert max(h[0] for h in hist) <= L.TOK_RECONTRASTE_MAX + 1 and hist[-1][1] == 0 and L._ESTADO['tok_contrastados'] == 12, hist     # presupuesto acotado por refresco
    assert len(L._UNIVERSO['toks']) == 24 and not L._SIN_CONTRASTE and not L._SC_SRC
    e = json.loads(L.TOK_CACHE_PATH.read_text())['mercados']; assert all(v['sc'] is False and v['ctr'] is True for v in e.values()) and len(e) == 12   # 'contrastado' en disco
    g = FK.ncalls_gamma; c = FK.ncalls_clob; FK.reloj += 30; L._tokens_universo(); assert FK.ncalls_gamma == g and FK.ncalls_clob == c       # UNA vez: no se repite
def t53_R1_discrepancia_en_recontraste_desuscribe_alarma_latcheada_cuarentena_y_borra_de_disco():
    gam = solo_clob_por_429(3); FK.gamma = dict(gam); FK.gamma['m0'] = ('99', '98'); logs, old = silencio()
    try:
        FK.reloj += 30; o = L._tokens_universo()
        assert sorted(o) == ['11', '12', '21', '22'] and 'm0' not in L._TOK and sum('ALARMA' in m and 'm0' in m for m in logs) == 1, (o, logs)
        assert L._TOK_FALLO['m0'][2] >= L.TOK_CUARENTENA_N and L._ESTADO['tok_cuarentena'] == 1 and L._ESTADO['tok_pendientes'] == 0
        assert 'm0' not in json.loads(L.TOK_CACHE_PATH.read_text())['mercados']                       # tombstone: tampoco se sirve del disco al reiniciar
        g = FK.ncalls_gamma; FK.reloj += 10; L._tokens_universo(); assert FK.ncalls_gamma == g          # en cuarentena ~60 s: no reintenta
        for _ in range(4): FK.reloj += 100; L._tokens_universo()                                         # tras la cuarentena gamma!=clob persiste: sigue fuera, sin 2a alarma
        assert 'm0' not in L._TOK and sum('ALARMA' in m and 'm0' in m for m in logs) == 1 and len(L._UNIVERSO['toks']) == 4
    finally: L._log = old
def t54_R1_fuente_unica_gamma_se_recontrasta_con_clob():
    reset(); mk(3); clob_ok = dict(FK.clob); FK.clob = {c: TimeoutError('t') for c in clob_ok}; L._tokens_universo()
    assert L._SIN_CONTRASTE == {'m0', 'm1', 'm2'} and set(L._SC_SRC.values()) == {'gamma'}
    FK.clob = dict(clob_ok); c0 = '0x' + '1'.rjust(64, '0'); FK.clob[c0] = good(c0, '999', '998')          # m1 difiere, m0/m2 coinciden
    logs, old = silencio()
    try: FK.reloj += 30; o = L._tokens_universo()
    finally: L._log = old
    assert 'm1' not in L._TOK and set(L._TOK) == {'m0', 'm2'} and not L._SIN_CONTRASTE and L._ESTADO['tok_sin_contraste'] == 0 and sorted(o) == ['10', '12', '20', '22']
    assert sum('ALARMA' in m for m in logs) == 1
def t55_R1_otra_fuente_sigue_caida_backoff_y_no_toca_nada():
    solo_clob_por_429(2)
    FK.gamma = {m: ('1' + m[1:], '2' + m[1:]) for m in FK.universo}; L._GAMMA['score'] = 0.0; FK.gamma = {m: RuntimeError('429') for m in FK.universo}      # circuito cerrado pero gamma da 429
    n = []
    for _ in range(20): FK.reloj += 5; g = FK.ncalls_gamma; L._tokens_universo(); n.append(FK.ncalls_gamma - g)
    assert sum(n) < 40 and L._SIN_CONTRASTE == {'m0', 'm1'} and len(L._UNIVERSO['toks']) == 4 and all(v[0] >= 1 for v in L._SC_ESTADO.values()), n     # backoff, sigue suscrito
    FK.gamma = {m: ('1' + m[1:], '2' + m[1:]) for m in FK.universo}; L._GAMMA['score'] = 0.0
    for _ in range(40): FK.reloj += 30; L._tokens_universo()
    assert not L._SIN_CONTRASTE
def t56_R1_arranque_en_frio_con_sc_en_disco_y_sin_campos_nuevos_se_recontrasta():
    gam = solo_clob_por_429(2); j = json.loads(L.TOK_CACHE_PATH.read_text())
    for v in j['mercados'].values(): v.pop('src', None); v.pop('ctr', None)                              # cache escrita por la v3
    L.TOK_CACHE_PATH.write_text(json.dumps(j))
    for d in (L._TOK, L._MKT, L._TOK_FALLO, L._CACHE_ENTRIES, L._SC_SRC): d.clear()
    L._SIN_CONTRASTE.clear(); L._CACHE.update(cargado=False); FK.gamma = dict(gam); L._GAMMA['score'] = 0.0
    assert len(L._tokens_universo()) == 4 and L._SIN_CONTRASTE == {'m0', 'm1'}                           # publica ya desde disco
    FK.reloj += 30; L._tokens_universo(); assert not L._SIN_CONTRASTE and L._ESTADO['tok_sin_contraste'] == 0
def t57_R1_sin_marca_stale_si_el_mercado_vence_o_sale():
    solo_clob_por_429(2); FK.reloj += 7200; L._tokens_universo(); assert not L._SIN_CONTRASTE and not L._SC_SRC and not L._SC_ESTADO
def t58_R1_backoff_del_recontraste_con_clob_caido():
    reset(); mk(2); ok = dict(FK.clob); FK.clob = {c: TimeoutError('t') for c in ok}; L._tokens_universo(); assert L._SIN_CONTRASTE == {'m0', 'm1'}
    c0 = FK.ncalls_clob
    for _ in range(24): FK.reloj += 5; L._tokens_universo()                                           # 120 s con CLOB caido
    assert FK.ncalls_clob - c0 < 14 and L._SIN_CONTRASTE == {'m0', 'm1'} and len(L._UNIVERSO['toks']) == 4, FK.ncalls_clob - c0   # backoff exponencial; sigue suscrito
    FK.clob = ok
    for _ in range(30): FK.reloj += 30; L._tokens_universo()
    assert not L._SIN_CONTRASTE

H = 'timestamp_utc,market_id,condition_id,question,slug,end_date\n'
def dia(ep): return dt.datetime.fromtimestamp(ep, dt.timezone.utc).strftime('%Y-%m-%d')
def iso(ep): return dt.datetime.fromtimestamp(ep, dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
def csv_rows(rows):   # rows: (mid, activo, marco, cid, edt_epoch)
    return ''.join(f'2026-01-01T00:00:00+00:00,{m},{c},"{a}|{mr}|x",slug-{m},{iso(e)}\n' for m, a, mr, c, e in rows)
def noche(seg=60):
    FK.reloj = 12 * 86400 + 86400 + float(seg)                       # 1970-01-13 00:00:00 + seg
def ayer_csv(rows, extra=''):
    (MK / (dia(FK.reloj - 86400) + '.csv')).write_text(H + csv_rows(rows) + extra)
def cid_(i): return '0x' + f'{i:064x}'
def tk(c): return '1' + str(int(c, 16)), '2' + str(int(c, 16))
def alta_gamma(rows):
    for m, a, mr, c, e in rows:
        if c.startswith('0x'): FK.gamma[m] = tk(c); FK.clob[c] = good(c, *tk(c))
def t59_I1_hoy_ausente_ayer_aporta_vigentes_y_excluye_vencidos():
    reset(); noche(60); e = FK.reloj
    rows = [('a1', 'BTC', 5, cid_(1), e + 300), ('a2', 'ETH', 15, cid_(2), e + 900), ('a3', 'SOL', 60, cid_(3), e + 3600), ('old', 'BTC', 5, cid_(4), e - 10), ('nocid', 'BTC', 5, 'sin', e + 300),
            ('otro', 'DOGE', 5, cid_(5), e + 300), ('raro', 'BTC', 7, cid_(6), e + 300)]
    ayer_csv(rows); alta_gamma(rows); assert not (MK / (dia(FK.reloj) + '.csv')).exists()
    L._MARCOS['60min'] = None
    try: o = L._tokens_universo()
    finally: L._MARCOS.pop('60min')
    assert sorted(o) == sorted(sum([list(tk(cid_(i))) for i in (1, 2, 3)], [])), o          # solo trackeados, vigentes, con cid; DOGE no esta en ACTIVOS
    assert set(L._MKT) == {'a1', 'a2', 'a3'} and L._MKT['a2'][1] == '15min'
def t60_I1_hoy_parcial_se_fusiona_por_market_id_y_hoy_manda():
    reset(); noche(300); e = FK.reloj
    ayer_csv([('mA', 'BTC', 5, cid_(1), e + 100), ('mB', 'BTC', 5, cid_(2), e + 400)]); alta_gamma([('mA', 'BTC', 5, cid_(1), 0), ('mB', 'BTC', 5, cid_(2), 0), ('mC', 'BTC', 5, cid_(3), 0)])
    FK.universo = {'mA': ('BTC', '5min', cid_(1), dt.datetime.fromtimestamp(e + 700, dt.timezone.utc)), 'mC': ('BTC', '5min', cid_(3), dt.datetime.fromtimestamp(e + 800, dt.timezone.utc))}
    (MK / (dia(FK.reloj) + '.csv')).write_text(H)                                                       # existe, fresco, parcial
    L._tokens_universo(); assert set(L._MKT) == {'mA', 'mB', 'mC'} and L._MKT['mA'][3].timestamp() == e + 700            # hoy manda sobre ayer en la misma clave
def t61_I1_hoy_corrupto_o_ilegible_ayer_corrupto_no_rompen():
    reset(); noche(120); e = FK.reloj; rows = [('a1', 'BTC', 5, cid_(1), e + 300)]; ayer_csv(rows); alta_gamma(rows)
    old = fl._universo_activo; fl._universo_activo = lambda: (_ for _ in ()).throw(OSError('csv de hoy corrupto'))
    logs, ol = silencio()
    try: assert len(L._tokens_universo()) == 2 and 'a1' in L._MKT
    finally: fl._universo_activo = old; L._log = ol
    for malo in (b'\x00\xff\xfe garbage \x00\n\x01', b'', b'timestamp_utc,market_id\n1,2', H.encode() + b'sin,comas\n"abierta,comilla\n'):
        reset(); noche(120); (MK / (dia(FK.reloj - 86400) + '.csv')).write_bytes(malo)
        logs, ol = silencio()
        try: assert L._tokens_universo() == [], malo
        finally: L._log = ol
    reset(); noche(120); ayer_csv(rows, extra='2026-01-01T00:00:00+00:00,zz,0xabc,"BTC|5|x",s,' + iso(e + 300))               # ultima linea sin \n: incompleta, se descarta
    alta_gamma(rows); L._tokens_universo(); r = L._csv_ayer(dt.datetime.fromtimestamp(FK.reloj, dt.timezone.utc)); assert 'zz' not in r and 'a1' in r and 'a1' in L._MKT
def t62_I1_fuera_de_ventana_con_hoy_fresco_no_lee_ayer_y_con_hoy_parado_si():
    reset(); FK.reloj = 12 * 86400 + 86400 + 40000.0; e = FK.reloj; rows = [('a1', 'BTC', 5, cid_(1), e + 300)]; ayer_csv(rows); alta_gamma(rows)
    hoy = MK / (dia(FK.reloj) + '.csv'); hoy.write_text(H); n = []; orig = L._leer_cola_csv; L._leer_cola_csv = lambda *a: (n.append(1), orig(*a))[1]
    try:
        L._tokens_universo(); assert not n and not L._MKT                                              # hoy fresco y fuera de las 2 h: no se toca ayer
        os.utime(hoy, (0, 0)); L._tokens_universo(); assert len(n) == 1 and 'a1' in L._MKT              # hoy parado (> 600 s sin escribir): ayer entra
        L._tokens_universo(); assert len(n) == 1                                                       # cache por ino/size/mtime
        ayer = MK / (dia(FK.reloj - 86400) + '.csv'); ayer.write_text(H + csv_rows(rows + [('a9', 'ETH', 5, cid_(9), e + 200)])); L._tokens_universo(); assert len(n) == 2   # cambio -> relee
    finally: L._leer_cola_csv = orig
def t63_I1_solo_se_lee_la_cola_y_se_descarta_la_linea_cortada():
    reset(); noche(60); e = FK.reloj
    rows = [(f'm{i}', 'BTC', 5, cid_(i), e + 300) for i in range(40)]; ayer_csv(rows); f = MK / (dia(FK.reloj - 86400) + '.csv'); tam = f.stat().st_size
    L.TOK_AYER_COLA_BYTES = tam // 3
    try:
        r = L._leer_cola_csv(f, dt.datetime.fromtimestamp(0, dt.timezone.utc))
        assert 5 < len(r) < 40 and 'm39' in r and 'm0' not in r and all(v[2].startswith('0x') and len(v[2]) == 66 for v in r.values())         # la cola; ninguna linea cortada
    finally: L.TOK_AYER_COLA_BYTES = 32 * 1024 * 1024
def t64_I1_desde_las_dos_h_sin_hoy_ausente_no_hay_fallback_ni_error():
    reset(); FK.reloj = 12 * 86400 + 86400 + 40000.0; assert L._tokens_universo() == []                   # hoy ausente (edad None) y ayer ausente: sin error
def t65_T2_tombstone_persiste_con_expiracion_en_disco_y_se_libera_al_re_resolver():
    gam = solo_clob_por_429(2); FK.gamma = dict(gam); FK.gamma['m0'] = ('99', '98'); L._GAMMA['score'] = 0.0
    FK.reloj += 30; L._tokens_universo()
    j = json.loads(L.TOK_CACHE_PATH.read_text()); assert 'm0' not in j['mercados'] and abs(j['tombstones']['m0'] - FUT.timestamp()) < 1 and 'm1' in j['mercados']      # expira con el mercado
    assert 'm0' in L._TOMB and L._CACHE['borrar'] == {}
    FK.gamma['m0'] = ('10', '20')                                                                           # ahora gamma y clob coinciden: re-resuelve, libera
    for _ in range(4): FK.reloj += 100; L._tokens_universo()
    j = json.loads(L.TOK_CACHE_PATH.read_text()); assert 'm0' in j['mercados'] and 'm0' not in j.get('tombstones', {}) and 'm0' in L._TOK
    FK.gamma['m1'] = ('77', '78'); L._GAMMA['score'] = 0.0; reset_sc = L._SIN_CONTRASTE; L._SIN_CONTRASTE.add('m1'); L._SC_SRC['m1'] = 'clob'; L._SC_ESTADO['m1'] = (0, 0.0)
    L._tokens_universo(); FK.reloj = FUT.timestamp() + 10; L._tokens_universo(); L._CACHE['sucio'] = True; L._cache_guardar()
    assert json.loads(L.TOK_CACHE_PATH.read_text()).get('tombstones') == {}                                # expirado el mercado, expira el tombstone
def t66_T2_tombstone_ajeno_expirado_se_ignora_y_basura_no_rompe():
    reset(); mk(1); L._tokens_universo(); j = json.loads(L.TOK_CACHE_PATH.read_text())
    j['tombstones'] = {'m0': FK.reloj - 1, 'x': 'abc', 'y': None, 'z': FK.reloj + 100}; L.TOK_CACHE_PATH.write_text(json.dumps(j))
    disco, malos, tomb = L._leer_disco(FK.reloj); assert 'm0' in disco and tomb == {'z': FK.reloj + 100}
    j['tombstones'] = [1, 2]; L.TOK_CACHE_PATH.write_text(json.dumps(j)); disco, _, tomb = L._leer_disco(FK.reloj); assert 'm0' in disco and tomb == {}
def t67_T2_sincroniza_el_tombstone_de_otro_proceso_en_el_refresco_sin_escribir():
    reset(); mk(3); L._tokens_universo(); assert len(L._UNIVERSO['toks']) == 6
    j = json.loads(L.TOK_CACHE_PATH.read_text()); del j['mercados']['m1']; j['tombstones'] = {'m1': FUT.timestamp()}; L.TOK_CACHE_PATH.write_text(json.dumps(j))      # otro proceso tumbo m1
    os.utime(L.TOK_CACHE_PATH, ns=(0, L.TOK_CACHE_PATH.stat().st_mtime_ns + 10 ** 9)); FK.reloj += 30; logs, ol = silencio()
    try: o = L._tokens_universo()
    finally: L._log = ol
    assert sorted(o) == ['10', '12', '20', '22'] and 'm1' not in L._TOK and L._ESTADO['tok_cuarentena'] == 1 and any('tombstone de otro proceso' in m for m in logs)
    assert 'm1' not in json.loads(L.TOK_CACHE_PATH.read_text())['mercados']
def t68_T2_multiproceso_real_el_que_tenia_el_mercado_en_memoria_no_lo_reescribe():
    import multiprocessing as mp
    reset(); mk(3); L._tokens_universo(); assert 'm1' in json.loads(L.TOK_CACHE_PATH.read_text())['mercados']
    ctx = mp.get_context('fork'); a_hecho = ctx.Event(); b_listo = ctx.Event(); fin_b = ctx.Event()
    def proc_a():
        b_listo.wait(20); L._CACHE_ENTRIES.pop('m1', None); L._TOK.pop('m1', None); L._CACHE['borrar']['m1'] = FUT.timestamp(); L._CACHE['sucio'] = True; L._CACHE['prox_intento'] = 0.0
        L._cache_guardar(); ok = 'm1' in json.loads(L.TOK_CACHE_PATH.read_text()).get('tombstones', {}); a_hecho.set(); os._exit(0 if ok and L._CACHE['n_err'] == 0 else 3)
    def proc_b():                                                         # B conserva m1 en memoria (estado heredado) y escribe 30 veces con entradas nuevas
        b_listo.set(); a_hecho.wait(20); malos = 0
        for r in range(30):
            L._CACHE_ENTRIES[f'b{r}'] = {'yes': f'7{r}', 'no': f'8{r}', 'activo': 'BTC', 'marco': '5min', 'cid': cid_(1000 + r), 'edt': FUT.isoformat(), 'sc': False, 'src': '', 'ctr': True}
            L._CACHE['sucio'] = True; L._CACHE['prox_intento'] = 0.0; L._cache_guardar()
            j = json.loads(L.TOK_CACHE_PATH.read_text()); malos += ('m1' in j['mercados'])
        os._exit(0 if malos == 0 and 'm1' not in L._TOK and L._TOK_FALLO.get('m1', (0, 0, 0))[2] >= L.TOK_CUARENTENA_N else 4)
    pa, pb = ctx.Process(target=proc_a), ctx.Process(target=proc_b); pb.start(); pa.start(); pa.join(60); pb.join(60)
    assert (pa.exitcode, pb.exitcode) == (0, 0), (pa.exitcode, pb.exitcode)
    j = json.loads(L.TOK_CACHE_PATH.read_text()); assert 'm1' not in j['mercados'] and 'm1' in j['tombstones'] and 'm0' in j['mercados'] and 'm2' in j['mercados'] and len(j['mercados']) == 2 + 30
def t69_T2_dos_procesos_en_carrera_el_tombstone_nunca_se_pierde():
    import multiprocessing as mp
    reset(); mk(2); L._tokens_universo(); ctx = mp.get_context('fork'); parar = ctx.Event()
    def escritor(k):
        for r in range(60):
            L._CACHE_ENTRIES[f'w{k}_{r}'] = {'yes': f'7{k}{r}', 'no': f'8{k}{r}', 'activo': 'BTC', 'marco': '5min', 'cid': cid_(2000 + k * 100 + r), 'edt': FUT.isoformat(), 'sc': False, 'src': '', 'ctr': True}
            L._CACHE['sucio'] = True; L._CACHE['prox_intento'] = 0.0; L._cache_guardar()
        os._exit(0 if L._CACHE['n_err'] == 0 else 3)
    def tumbador():
        time.sleep(0.05) if False else _real_time.sleep(0.05)
        L._CACHE_ENTRIES.pop('m0', None); L._CACHE['borrar']['m0'] = FUT.timestamp(); L._CACHE['sucio'] = True; L._CACHE['prox_intento'] = 0.0; L._cache_guardar(); os._exit(0 if L._CACHE['n_err'] == 0 else 3)
    ps = [ctx.Process(target=escritor, args=(1,)), ctx.Process(target=escritor, args=(2,)), ctx.Process(target=tumbador)]
    [p.start() for p in ps]; [p.join(90) for p in ps]; assert [p.exitcode for p in ps] == [0, 0, 0]
    # los escritores arrancaron con 'm0' en memoria; el que escribe tras el tombstone no puede reintroducirlo; los que escribieron antes: sobrescritos por el tombstone
    j = json.loads(L.TOK_CACHE_PATH.read_text())
    for p in [ctx.Process(target=escritor, args=(3,))]: p.start(); p.join(60)               # un escritor posterior con m0 en memoria
    j = json.loads(L.TOK_CACHE_PATH.read_text()); assert 'm0' not in j['mercados'] and 'm0' in j['tombstones'] and 'm1' in j['mercados'] and len(j['mercados']) == 1 + 180
def t70_S4_cache_de_4h_descarta_vencidos_y_el_refresco_los_repone():
    reset(); mk(6); far = dt.datetime.fromtimestamp(FK.reloj + 20000, dt.timezone.utc)
    for i in (6, 7):
        mid = f'm{i}'; cid = cid_(900 + i); FK.universo[mid] = ('ETH', '60min', cid, far); FK.gamma[mid] = tk(cid); FK.clob[cid] = good(cid, *tk(cid))
    L._MARCOS['60min'] = None
    try:
        L._tokens_universo(); assert len(L._TOK) == 8 and len(json.loads(L.TOK_CACHE_PATH.read_text())['mercados']) == 8
        FK.reloj += 14400                                                                  # el despliegue ocurre ~4 h despues de sembrar
        for d in (L._TOK, L._MKT, L._TOK_FALLO, L._CACHE_ENTRIES): d.clear()
        L._SIN_CONTRASTE.clear(); L._CACHE.update(cargado=False, sucio=False); FK.universo = {}
        logs, ol = silencio()
        try: o = L._tokens_universo()
        finally: L._log = ol
        assert len(o) == 4 and set(L._MKT) == {'m6', 'm7'} and any('2 mercados vigentes (6 descartados' in m for m in logs), (o, logs)      # solo los de vida larga; ningun vencido
        assert all(v[3].timestamp() > FK.reloj for v in L._MKT.values())
        fut2 = dt.datetime.fromtimestamp(FK.reloj + 3000, dt.timezone.utc)
        for i in range(10, 16):
            mid = f'n{i}'; cid = cid_(i); FK.universo[mid] = ('BTC', '5min', cid, fut2); FK.gamma[mid] = tk(cid); FK.clob[cid] = good(cid, *tk(cid))
        FK.reloj += 5; o = L._tokens_universo(); assert len(o) == 4 + 12 and len(L._TOK) == 8                                       # el refresco repone el universo actual
    finally: L._MARCOS.pop('60min', None)
def t80_horizonte_5m_solo_resuelve_y_suscribe_lo_cercano():
    reset(); L.HORIZONTE_5M_S = 7200.0
    for i, h in enumerate((600, 3600, 7000, 8000, 80000)):              # cierre a +h s (inicio = cierre-300)
        mid = f'h{i}'; cid = '0x' + f'{i:064x}'; FK.universo[mid] = ('BTC', '5min', cid, dt.datetime.fromtimestamp(FK.reloj + h, dt.timezone.utc))
        FK.gamma[mid] = (f'1{i}', f'2{i}'); FK.clob[cid] = good(cid, f'1{i}', f'2{i}')
    o = L._tokens_universo()
    assert len(o) == 6 and FK.ncalls_gamma == 3, (len(o), FK.ncalls_gamma)     # h3 (inicio +7700) y h4 fuera: ni gamma ni WS
    FK.reloj += 1000; o = L._tokens_universo(); assert len(o) == 6 and FK.ncalls_gamma == 4   # h0 vence, h3 entra al avanzar el reloj
def t81_horizonte_no_afecta_15m_ni_60m_y_cero_es_sin_limite():
    reset(); L.HORIZONTE_5M_S = 7200.0; L._MARCOS['60min'] = None
    try:
        mk(2, marco='15min', edt=dt.datetime.fromtimestamp(FK.reloj + 50000, dt.timezone.utc))
        for i in (2, 3):
            mid = f'm{i}'; cid = '0x' + f'{i:064x}'; FK.universo[mid] = ('BTC', '60min', cid, dt.datetime.fromtimestamp(FK.reloj + 50000, dt.timezone.utc)); FK.gamma[mid] = (f'1{i}', f'2{i}'); FK.clob[cid] = good(cid, f'1{i}', f'2{i}')
        assert len(L._tokens_universo()) == 8
        reset(); L.HORIZONTE_5M_S = 0.0; mk(2, edt=dt.datetime.fromtimestamp(FK.reloj + 80000, dt.timezone.utc)); assert len(L._tokens_universo()) == 4
    finally: L._MARCOS.pop('60min', None); L.HORIZONTE_5M_S = 7200.0

# ---------------------------------------------------------------- siembra desde new_market_universo (delta_nmu)
U5 = L._U5; NMUDIR = Path(tempfile.mkdtemp()); U5.UNIV_DIR = NMUDIR
_reset_v5 = reset
def reset():                                                                                         # todos los tests parten sin fichero de universo
    _reset_v5(); NMUDIR.mkdir(exist_ok=True)
    for f in NMUDIR.glob('*'): f.unlink()
    U5._CACHE.clear()
def nmu_reset():
    reset()
    L._ESTADO.pop('tok_sembrados', None); getattr(L, '_NMU_ULT', [0.0]).__setitem__(0, 0.0); U5._CACHE.clear(); L._GAMMA.pop('nmu_err', None); L._GAMMA.pop('nmu_st', None); L.NMU_ACTIVO = True; L.HORIZONTE_5M_S = 7200.0
def nmu_fila(i, marco='5m', activo='btc', cierre_off=1200, t=None, up=None, dn=None, cid=None, mid=None):
    cierre = int(FK.reloj) + cierre_off; dur = {'5m': 300, '15m': 900}[marco]
    e = {'id': mid or f'n{i}', 'market': cid or ('0x' + f'{i + 5000:064x}'), 'slug': f'{activo}-updown-{marco}-{cierre - dur}', 'assets_ids': [up or f'7{i}1', dn or f'7{i}2'],
         'outcomes': ['Up', 'Down'], 'timestamp': '1'}
    return U5.parsear_nuevo(e, int((t if t is not None else FK.reloj) * 1000))
def t90_arranque_en_frio_cero_llamadas_y_5m_por_delante_del_csv():
    nmu_reset(); U5.escribir([nmu_fila(i, cierre_off=600 + 300 * i) for i in range(25)], NMUDIR)    # 25 mercados 5m, hasta +2 h; CSV vacio
    o = L._tokens_universo()
    assert len(o) == 48 and FK.ncalls_gamma == 0 and FK.ncalls_clob == 0, (len(o), FK.ncalls_gamma, FK.ncalls_clob)   # 24 de 25: el 25 cae fuera de las 2 h
    assert L._UNIVERSO['meta']['701'][4] == 'YES' and L._UNIVERSO['meta']['702'][4] == 'NO' and L._UNIVERSO['claves']['701'] == 'BTC#5min'
    assert L._ESTADO['tok_sembrados'] == 24
def t91_csv_y_fichero_a_la_vez_no_consultan_red_al_resolver():
    nmu_reset(); mk(3)                                                                              # CSV: m0..m2 con cid 0x..i
    U5.escribir([nmu_fila(i, cid='0x' + f'{i:064x}', mid=f'm{i}', up=f'1{i}', dn=f'2{i}') for i in range(3)], NMUDIR)
    o = L._tokens_universo()
    assert sorted(o) == ['10', '11', '12', '20', '21', '22'] and FK.ncalls_gamma == 0 and FK.ncalls_clob == 0
def t92_sin_fichero_o_corrupto_camino_v5_intacto():
    nmu_reset(); mk(2); o = L._tokens_universo()
    assert len(o) == 4 and FK.ncalls_gamma == 2                                                      # sin fichero: v5
    nmu_reset(); mk(2); NMUDIR.mkdir(exist_ok=True)
    U5.fichero(U5.dia_utc(FK.reloj), NMUDIR).write_bytes(b'\x1f\x8b basura'); o = L._tokens_universo()
    assert len(o) == 4 and FK.ncalls_gamma == 2
    nmu_reset(); mk(2); L._U5 = None; L.NMU_ACTIVO = False
    try: assert len(L._tokens_universo()) == 4 and FK.ncalls_gamma == 2                               # modulo ausente
    finally: L._U5 = U5
def t93_horizonte_aplica_a_lo_sembrado():
    nmu_reset(); U5.escribir([nmu_fila(0, cierre_off=600), nmu_fila(1, cierre_off=9000), nmu_fila(2, cierre_off=90000)], NMUDIR)
    assert len(L._tokens_universo()) == 2 and FK.ncalls_gamma == 0                                   # solo n0 (inicio +300 s)
    FK.reloj += 2000; o = L._tokens_universo(); assert len(o) == 2 and L._UNIVERSO['meta']['711'][2] == 'n1'   # n0 vence, n1 entra
def t94_condition_id_distinto_al_csv_no_se_siembra():
    nmu_reset(); mk(1); U5.escribir([nmu_fila(0, cid='0x' + 'ab' * 32, mid='m0', up='555', dn='666')], NMUDIR)
    o = L._tokens_universo()
    assert sorted(o) == ['10', '20'] and FK.ncalls_gamma >= 1                                         # gana el camino v5 (gamma/CLOB)
def t95_conflicto_dentro_del_fichero_excluye():
    nmu_reset(); U5.escribir([nmu_fila(0), nmu_fila(0, up='999')], NMUDIR)
    assert L._tokens_universo() == [] and FK.ncalls_gamma == 0
def t96_15m_solo_si_viene_del_csv_y_5m_apagado_por_marco():
    nmu_reset(); U5.escribir([nmu_fila(0, marco='15m'), nmu_fila(1, marco='5m')], NMUDIR)
    assert sorted(L._tokens_universo()) == ['711', '712']                                             # el 15m no se anade
    nmu_reset(); L._MARCOS.pop('5min'); U5.escribir([nmu_fila(0)], NMUDIR)
    try: assert L._tokens_universo() == []                                                           # marco no permitido
    finally: L._MARCOS['5min'] = None
def t97_medianoche_lee_ayer():
    nmu_reset(); FK.reloj = 1_036_800.0 - 900.0                                                       # 23:45 del dia D
    U5.escribir([nmu_fila(i, cierre_off=2400 + 300 * i) for i in range(4)], NMUDIR)                   # cierran 00:25 .. 00:40 del dia D+1
    FK.reloj = 1_036_800.0 + 60.0; U5._CACHE.clear()                                                  # arranque en frio a las 00:01 de D+1: solo existe el fichero de AYER
    assert not U5.fichero(U5.dia_utc(FK.reloj), NMUDIR).exists()
    o = L._tokens_universo(); assert len(o) == 8 and FK.ncalls_gamma == 0 and FK.ncalls_clob == 0
def _sleep_avanza(on):                                                                               # el sleep falso hace avanzar el reloj falso (mide el espaciado real)
    T.sleep = staticmethod((lambda x: setattr(FK, 'reloj', FK.reloj + x)) if on else (lambda x: None))
def _nmu_cid(i): return '0x' + f'{i + 5000:064x}'
def _nmu_setup(n, cierre0=600, paso=10, clob_ok=True):
    nmu_reset(); U5.escribir([nmu_fila(i, cierre_off=cierre0 + paso * i) for i in range(n)], NMUDIR)
    for i in range(n):
        FK.universo[f'n{i}'] = ('BTC', '5min', _nmu_cid(i), dt.datetime.fromtimestamp(int(FK.reloj) + cierre0 + paso * i, dt.timezone.utc)); FK.gamma[f'n{i}'] = RuntimeError('gamma NO debe consultarse')
        if clob_ok: FK.clob[_nmu_cid(i)] = good(_nmu_cid(i), f'7{i}1', f'7{i}2')
def t98_nmu_solo_clob_acotado_espaciado_y_fail_closed_si_discrepa():
    _sleep_avanza(True)
    try:
        _nmu_setup(40); FK.clob[_nmu_cid(7)] = good(_nmu_cid(7), '888', '889')                      # CLOB discrepa en n7
        L._tokens_universo(); assert FK.ncalls_gamma == 0 and FK.ncalls_clob == 0   # arranque: ninguna llamada
        maxpor = 0
        for _ in range(16):
            n0 = len(FK.llamadas); FK.reloj += 31; L._tokens_universo()
            nuevas = [x for x in FK.llamadas[n0:] if not x[0].endswith('/n7') and not x[0].endswith(_nmu_cid(7))]; maxpor = max(maxpor, len(nuevas))   # n7 (desuscrito) sigue el camino v5 de cuarentena
            assert all('/markets/0x' in u for u, _t, _r in nuevas)                                 # TODAS al CLOB, ninguna a gamma
            ts = [r for _u, _t, r in nuevas]; assert all(b - a >= L.TOK_NMU_INTERVALO_S - 1e-6 for a, b in zip(ts, ts[1:])), ts   # <= 0,5 req/s
        assert maxpor <= L.TOK_NMU_REFRESCO_MAX, maxpor
        assert L._TOK.get('n7') != ('771', '772') and L._ESTADO.get('tok_contrastados', 0) >= 39 and 40 <= FK.ncalls_clob <= 44, (FK.ncalls_clob, L._ESTADO.get('tok_contrastados'))   # UNA llamada por mercado
    finally: _sleep_avanza(False)
def t99_nmu_clob_429_aborta_el_refresco_y_agota_intentos():
    _sleep_avanza(True)
    try:
        _nmu_setup(10, cierre0=1700, clob_ok=False)
        for i in range(10): FK.clob[_nmu_cid(i)] = Resp(429)
        L._tokens_universo()
        n0 = len(FK.llamadas); FK.reloj += 31; L._tokens_universo()
        assert len(FK.llamadas) - n0 == 1 and FK.ncalls_gamma == 0                                  # primer 429 -> aborta los demas contrastes del refresco
        for _ in range(45): FK.reloj += 31; L._tokens_universo()
        assert 10 <= FK.ncalls_clob <= 10 * L.TOK_NMU_INTENTOS_MAX and FK.ncalls_gamma == 0 and len(L._TOK) == 10      # acotado; todo sigue suscrito
    finally: _sleep_avanza(False)
def t101_nmu_ventana_de_30_min():
    _sleep_avanza(True)
    try:
        _nmu_setup(1, cierre0=3600)
        L._tokens_universo()
        for _ in range(5): FK.reloj += 31; L._tokens_universo()
        assert FK.ncalls_clob == 0 and FK.ncalls_gamma == 0                                         # lejos del cierre: no se consulta nada
        FK.reloj += 1745; L._tokens_universo(); FK.reloj += 31; L._tokens_universo()
        assert FK.ncalls_clob == 1 and FK.ncalls_gamma == 0 and 'n0' not in L._SIN_CONTRASTE         # al entrar en los 30 min: UNA vez
        FK.reloj += 31; L._tokens_universo(); assert FK.ncalls_clob == 1
    finally: _sleep_avanza(False)
def t102_gamma_en_pausa_compartida_no_se_llama_y_429_la_activa():
    nmu_reset(); mk(3)                                                                              # v5: 3 mercados del CSV, gamma responde
    ahora = FK.reloj; (NMUDIR / 'gamma_pausa.json').write_text(json.dumps({'hasta': ahora + 600}))
    o = L._tokens_universo()
    assert FK.ncalls_gamma == 0 and FK.ncalls_clob == 3 and len(o) == 6                              # en pausa: resuelve solo por CLOB
    (NMUDIR / 'gamma_pausa.json').unlink(); nmu_reset(); mk(2); FK.gamma = {m: Resp(429) for m in FK.universo}
    marcas = []; real = U5.marcar_429; U5.marcar_429 = lambda *a, **k: marcas.append(1)
    try: L._tokens_universo()
    finally: U5.marcar_429 = real
    assert marcas and len(L._TOK) == 2                                                              # 429 de gamma -> pausa compartida; fallback CLOB
def t103_sin_modulo_io_ni_pausa_no_rompe():
    nmu_reset(); mk(2); u = L._U5; L._U5 = None
    try: assert len(L._tokens_universo()) == 4 and FK.ncalls_gamma == 2
    finally: L._U5 = u
def t104_calls_hora_gamma_y_clob():
    """Escenario 60 min simulados (refresco 30 s): 144 mercados 5m ya en horizonte + 6 monedas nuevas cada 5 min. Imprime llamadas/hora."""
    _sleep_avanza(True)
    try:
        nmu_reset()
        base = FK.reloj; k = 0
        def alta(cierre_abs):
            nonlocal k
            i = k; k += 1; off = int(cierre_abs - FK.reloj)
            U5.escribir([nmu_fila(i, cierre_off=off, cid=_nmu_cid(i), mid=f'n{i}', up=f'7{i}1', dn=f'7{i}2')], NMUDIR)
            FK.universo[f'n{i}'] = ('BTC', '5min', _nmu_cid(i), dt.datetime.fromtimestamp(int(FK.reloj) + off, dt.timezone.utc)); FK.gamma[f'n{i}'] = (f'7{i}1', f'7{i}2'); FK.clob[_nmu_cid(i)] = good(_nmu_cid(i), f'7{i}1', f'7{i}2')
        for m in range(24):
            for _c in range(6): alta(base + 600 + 300 * m)
        L._tokens_universo(); g0, c0 = FK.ncalls_gamma, FK.ncalls_clob
        for step in range(120):
            FK.reloj += 30
            if step % 10 == 0:
                for _c in range(6): alta(FK.reloj + 7200 + 300)
            L._tokens_universo()
        print('CALLS_HORA gamma=%d clob=%d (arranque en frio: gamma=%d clob=%d)' % (FK.ncalls_gamma - g0, FK.ncalls_clob - c0, g0, c0))
    finally: _sleep_avanza(False)
def t100_apagado_por_variable():
    nmu_reset(); L.NMU_ACTIVO = False; U5.escribir([nmu_fila(0)], NMUDIR)
    try: assert L._tokens_universo() == []
    finally: L.NMU_ACTIVO = True
for f in [v for k, v in sorted(globals().items()) if k.startswith('t') and k[1:3].isdigit()]: t(f)
for n, r in res: print(f'{n}: {r}')
print('TOTAL', sum(r == 'OK' for _, r in res), '/', len(res)); sys.exit(0 if all(r == 'OK' for _, r in res) else 1)
