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
class Sess:
    def get(s, url, timeout=0):
        FK.ncalls_clob += 1; cid = url.rsplit('/', 1)[1]; r = FK.clob.get(cid)
        if isinstance(r, Exception): raise r
        return r if r is not None else Resp(404)
lt = types.ModuleType('live_trade'); lt._SESSION = Sess()
def _gti(mid):
    FK.ncalls_gamma += 1; r = FK.gamma.get(mid)
    if isinstance(r, Exception): raise r
    if r is None: raise RuntimeError('404')
    return r[0], r[1], 'c'
lt._get_token_ids = _gti
fl = types.ModuleType('fetch_libro_ambos_lados'); fl._universo_activo = lambda: {k: v for k, v in FK.universo.items() if v[3].timestamp() > FK.reloj}
sys.modules['live_trade'] = lt; sys.modules['fetch_libro_ambos_lados'] = fl
import libro_estado_ws as L
class T:   # reloj falso
    time = staticmethod(lambda: FK.reloj); sleep = staticmethod(lambda x: None)
L.time = T
L._MARCOS.clear(); L._MARCOS['5min'] = None; L._MARCOS['15min'] = None
FUT = dt.datetime.fromtimestamp(FK.reloj + 3600, dt.timezone.utc)
def reset():
    for d in (L._TOK, L._TOK_FALLO, L._MKT): d.clear()
    L._GAMMA.clear(); L._GAMMA['score'] = 0.0; L._ESTADO.pop('tok_pendientes', None)
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
        for _ in range(15): FK.reloj += 70; L._tokens_universo()
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
    reset(); mk(10); FK.gamma = {m: ValueError('outcomes inesperados') for m in FK.universo}
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
    reset(); mk(3); L._tokens_universo(); L._TOK_FALLO['fantasma'] = (3, FK.reloj + 99); L._HIST['999'] = []; L._EXTRA['999'] = FK.reloj + 500
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
    reset(); mk(60); vistos = []; base = FK.gamma.copy()
    def g(mid):
        vistos.append(L._TOK_LOCK.locked()); FK.reloj += 1.0; return base[mid] + ('c',)
    lt._get_token_ids = lambda mid: (setattr(FK, 'ncalls_gamma', FK.ncalls_gamma + 1), g(mid)[:2] + ('c',))[1]
    try:
        L._tokens_universo(); assert not any(vistos) and 20 <= FK.ncalls_gamma <= 22 and L._ESTADO['tok_pendientes'] >= 38      # presupuesto 20 s
        L._tokens_universo(); L._tokens_universo(); assert len(L._TOK) == 60                                                         # el resto al siguiente
    finally: lt._get_token_ids = _gti
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
for f in [v for k, v in sorted(globals().items()) if k.startswith('t') and k[1:3].isdigit()]: t(f)
for n, r in res: print(f'{n}: {r}')
print('TOTAL', sum(r == 'OK' for _, r in res), '/', len(res)); sys.exit(0 if all(r == 'OK' for _, r in res) else 1)
