"""Tests de ancla_p1b_28nov.py (fixtures sinteticas: ledger + libro5_ms en tmp; 0 red). Ejecutar: python3 -m pytest -q test_ancla_p1b_28nov.py"""
import gzip
import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ancla_p1b_28nov as A

TOK = '111'
T0 = 1_795_000_000_000                      # ms epoch del envio
NS = 1_000_000


def libro(tmp, filas, nombre='libro5_ms_2026-11-28_1.csv.gz'):
    """filas = [(t_ms, tok, lado, precio, size, rx, seq)] en el ORDEN DEL FICHERO."""
    p = os.path.join(tmp, nombre)
    with gzip.open(p, 'wt') as f:
        f.write('tipo,t_ms,token,c1,c2,c3,recepcion,seq\n')
        for t, tok, lado, pr, sz, rx, seq in filas:
            f.write(f'd,{t},{tok},{lado},{pr},{sz},{rx},{seq}\n')
    return p


def ledger(tmp, ordenes, nombre='run'):
    """ordenes = [dict(oid, coin, tok, size, send_ms, ack_ms, cancels=[(send_ms, ack_ms, ok)])]"""
    d = os.path.join(tmp, nombre)
    os.makedirs(d, exist_ok=True)
    with open(d + '/ledger.jsonl', 'w') as f:
        for o in ordenes:
            f.write(json.dumps(dict(k='intencion', oid_local=o['oid'], coin=o['coin'], tok=o['tok'], size=o['size'])) + '\n')
            f.write(json.dumps(dict(k='post', oid_local=o['oid'], clase='ok', t_send_ns=int(o['send_ms'] * NS), t_ack_ns=int(o['ack_ms'] * NS))) + '\n')
            for n, (s, a, ok) in enumerate(o.get('cancels', []), 1):
                f.write(json.dumps(dict(k='cancel', oid=o['oid'], intento=n, ok=ok, t_send_ns=int(s * NS), t_ack_ns=int(a * NS))) + '\n')
    return d


def corre(tmp, filas, ordenes):
    p = libro(tmp, filas)
    d = ledger(tmp, ordenes)
    return A.analiza_run(d, libro=[p], SC=None)


def base_niv(seq0=1, size=1000.00):
    return [(T0 - 5000, TOK, 'B', '0.01', f'{size:.2f}', T0 - 4980, seq0)]


def orden(size=5.01, cancels=None, oid='0xa'):
    return dict(oid=oid, coin='ETH', tok=TOK, size=size, send_ms=T0, ack_ms=T0 + 120, cancels=cancels or [])


def test_ancla_unica_alta_y_cancel_con_reintento(tmp_path):
    # alta +5,01 a +40 ms del envio; cancel: intento 1 falla (envio T0+2000), intento 2 ok (envio +2100); efecto -5,01 a +2035 (tras el 1.er envio, antes del 2.o): se mide desde el 1.o
    fil = base_niv() + [(T0 + 40, TOK, 'B', '0.01', '1005.01', T0 + 62, 2), (T0 + 2035, TOK, 'B', '0.01', '1000.00', T0 + 2058, 3)]
    r = corre(str(tmp_path), fil, [orden(cancels=[(T0 + 2000, T0 + 2090, False), (T0 + 2100, T0 + 2160, True)])])
    a = {f['tipo']: f for f in r['anclas']}
    assert a['alta']['estado'] == 'ancla' and a['alta']['lat_ex_ms'] == 40 and a['alta']['lat_rx_ms'] == 62
    assert a['cancel']['estado'] == 'ancla' and a['cancel']['lat_ex_ms'] == 35 and a['cancel']['n_intentos'] == 2          # reintentos incluidos: la ventana arranca en el 1.er envio
    assert a['cancel']['lat_ex_desde_envio_ok_ms'] == -65                                                                  # medido desde el intento OK seria negativo: por eso la referencia es el 1.o


def test_doble_salto_es_censurada_multi_no_excluida(tmp_path):
    # dos +5,01 distintos dentro de la ventana [envio-5, ack+500] => no unica
    fil = base_niv() + [(T0 + 40, TOK, 'B', '0.01', '1005.01', T0 + 60, 2), (T0 + 200, TOK, 'B', '0.01', '1010.02', T0 + 220, 3)]
    r = corre(str(tmp_path), fil, [orden()])
    f = r['anclas'][0]
    assert f['estado'] == 'censurada_multi' and f['n_candidatos'] == 2 and f['censura_ms'] == 40
    x = r['resumen']['alta']['ETH']
    assert x['esperado'] == 1 and x['anclas'] == 0 and x['censuradas_multi'] == 1 and x['tasa_censura'] == 1.0          # en el denominador


def test_sin_match_censurada_0_en_ack_mas_500(tmp_path):
    fil = base_niv() + [(T0 + 40, TOK, 'B', '0.01', '1003.00', T0 + 60, 2)]                                               # +3,00: no es nuestra firma
    r = corre(str(tmp_path), fil, [orden()])
    f = r['anclas'][0]
    assert f['estado'] == 'censurada_0' and f['censura_ms'] == 620.0                                                        # t_ack + 500 - t_envio


def test_fuera_de_ventana_no_cuenta(tmp_path):
    for t_ev, esperado in ((T0 + 120 + 501, 'censurada_0'), (T0 - 6, 'censurada_0'), (T0 - 5, 'ancla'), (T0 + 120 + 500, 'ancla')):
        d = tmp_path / str(t_ev)
        d.mkdir()
        fil = base_niv() + [(t_ev, TOK, 'B', '0.01', '1005.01', t_ev + 20, 2)]
        r = corre(str(d), fil, [orden()])
        assert r['anclas'][0]['estado'] == esperado, (t_ev - T0, r['anclas'][0])


def test_orden_por_seq_no_por_tiempo(tmp_path):
    # en el fichero y por seq: 1000.00 -> 1005.01 (+5,01, t=+40); la fila de seq 3 lleva t_ms ANTERIOR (sello de lote) y baja 1005.01 -> 1000.00 (-5,01).
    # Ordenar por t_ms invertiria el orden y fabricaria un -5,01 espurio antes y un +5,01 despues; por seq: un solo +5,01 y un -5,01 posterior.
    fil = base_niv() + [(T0 + 40, TOK, 'B', '0.01', '1005.01', T0 + 60, 2), (T0 + 30, TOK, 'B', '0.01', '1000.00', T0 + 61, 3)]
    r = corre(str(tmp_path), fil, [orden()])
    niv, _, _ = A.lee_libro([os.path.join(str(tmp_path), 'libro5_ms_2026-11-28_1.csv.gz')], {TOK}, T0)
    e = A.eventos_delta(niv)[TOK]
    assert [(x[1], x[3]) for x in e] == [(501, 2), (-501, 3)]
    assert r['anclas'][0]['estado'] == 'ancla' and r['anclas'][0]['seq'] == 2


def test_lado_y_precio_exactos(tmp_path):
    # mismo delta en lado A, o precio 0,02, o otro token: NO cuenta
    fil = base_niv() + [(T0 + 40, TOK, 'A', '0.01', '1005.01', T0 + 60, 2), (T0 + 41, TOK, 'B', '0.02', '1005.01', T0 + 61, 3), (T0 + 42, '999', 'B', '0.01', '1005.01', T0 + 62, 4)]
    r = corre(str(tmp_path), fil, [orden()])
    assert r['anclas'][0]['estado'] == 'censurada_0'


def test_duplicados_y_truncado(tmp_path):
    fil = base_niv() + [(T0 + 40, TOK, 'B', '0.01', '1005.01', T0 + 60, 2), (T0 + 40, TOK, 'B', '0.01', '1005.01', T0 + 60, 2)]
    p = libro(str(tmp_path), fil)
    raw = open(p, 'rb').read()
    open(p, 'wb').write(raw[:-8])                                                                                         # gz truncado (fichero en escritura)
    niv, todas, info = A.lee_libro([p], {TOK}, T0)
    assert info['ficheros'][0]['llego_a_eof'] is True                                                                     # no revienta
    p2 = libro(str(tmp_path), fil, 'libro5_ms_2026-11-28_2.csv.gz')
    niv, todas, info = A.lee_libro([p2], {TOK}, T0)
    assert info['duplicadas'] == 1 and len(niv[TOK]) == 2


def test_reproducible_bytes_y_hash_prefijo(tmp_path):
    fil = base_niv() + [(T0 + 40, TOK, 'B', '0.01', '1005.01', T0 + 60, 2)]
    p = libro(str(tmp_path), fil)
    d = ledger(str(tmp_path), [orden()])
    a = json.dumps(A.analiza([d], libro=[p]), sort_keys=True)
    b = json.dumps(A.analiza([d], libro=[p]), sort_keys=True)
    assert a == b
    j = json.loads(a)
    assert j['runs'][0]['entradas']['libro']['ficheros'][0]['sha256_prefijo_leido'] == A.sha256_fichero(p)             # lectura completa => hash del fichero
    assert j['codigo']['ancla_p1b_28nov_sha256'] == A.sha256_fichero(A.__file__) and len(j['sha256_resultado']) == 64


def test_km_censura():
    obs = [(10, True), (20, True), (30, False), (40, True), (50, False)]
    assert A.km_cuantil(obs, .5) == 40 and A.km_cuantil([(10, True), (20, False), (30, False)], .9) is None            # censura excesiva: no estimable
    assert A.km_cuantil([(5, True)] * 3, .5) == 5


def _ruido(rng, t_ini_ms, dur_s, lam, firmas_prohibidas, tamanos):
    """Eventos de ruido de Poisson (lam/s) con deltas aleatorios en centimos que NO son firma propia; devuelve [(t_ms, delta_cent)]."""
    t, out = t_ini_ms, []
    while True:
        t += rng.expovariate(lam) * 1000
        if t > t_ini_ms + dur_s * 1000:
            return out
        d = rng.choice(tamanos) * rng.choice((1, -1))
        out.append((int(t), d))


def _simula(rng, n, lam, firma_unica, tamanos_ruido, ruido_exacto5=0.0):
    """n ordenes, cada una con su token, su alta (+s a +30..60 ms) y su cancel (-s a +30..60 ms del envio de cancel) + ruido Poisson lam/s sobre el MISMO nivel. Devuelve fracción de anclas correctas, censura."""
    ok = cen = mal = 0
    for k in range(n):
        s = 5.01 + 0.01 * k if firma_unica else 5.00
        sc = int(round(s * 100))
        ev = [(T0 + int(rng.uniform(30, 60)), sc)]
        ev_c = [(T0 + 2500 + int(rng.uniform(30, 60)), -sc)]
        ruido = _ruido(rng, T0 - 5000, 12, lam, set(), tamanos_ruido)
        # ruido que imita +-5,00 exacto con la tasa pedida (BTC: 40 % de los eventos)
        ruido = [(t, (500 if d > 0 else -500) if rng.random() < ruido_exacto5 else d) for t, d in ruido]
        todos = sorted(ev + ev_c + ruido)
        size, niv = 100000, [(1, T0 - 5000, 100000, T0 - 4990)]
        for i, (t, d) in enumerate(todos, 2):
            size += d
            niv.append((i, t, size, t + 20))
        e = A.eventos_delta({TOK: niv})[TOK]
        m = A.candidatos(e, T0 - 5, T0 + 120 + 500, +sc)
        if len(m) == 1:
            if abs(m[0][0] - ev[0][0]) == 0:
                ok += 1
            else:
                mal += 1
        else:
            cen += 1
    return ok / n, cen / n, mal / n


def test_sintetico_ruido_lambda_003_recuperacion_95_con_firma_de_tamano():
    rng = random.Random(7)
    ok, cen, mal = _simula(rng, 249, 0.03, True, list(range(1, 2000)))
    assert ok >= 0.95 and mal == 0.0, (ok, cen, mal)


def test_sintetico_btc_con_5_00_fijo_no_recupera_y_con_firma_si():
    rng = random.Random(11)
    ok5, cen5, mal5 = _simula(rng, 200, 24.0, False, [500, 100, 200, 300, 150], ruido_exacto5=0.40)               # BTC: 24 ev/s, 40 % exactamente 5,00
    okf, cenf, malf = _simula(rng, 200, 24.0, True, [500, 100, 200, 300, 150], ruido_exacto5=0.40)
    assert ok5 < 0.20                                                                                                  # con 5,00 fijo el ancla es casi siempre ambigua (se demuestra el problema)
    assert okf > 0.95 - 0.30 and malf <= 0.05 and okf > ok5 + 0.5, (ok5, okf, malf)                                    # con firma unica (ruido que no coincide en centimos) recupera; los falsos son raros


def test_clase_suelo_lo_y_indet():
    class SC:                                                                                                          # stub minimo de suelo_causal
        BIN_MS, D_LO, ND = 10_000, -50, 451
        @staticmethod
        def clase_de_ventanas(h1, h2):
            tot = int((h1 + h2).sum())
            return ('lo' if tot >= 200 else 'indet'), dict(p5=19.0 if tot else None)
    rx = [T0 - 590_000 + i * 1000 for i in range(200)]
    c, _ = A.clase_suelo(dict(rx=rx, d=[19] * 200), T0, SC)
    assert c == 'lo'
    c, _ = A.clase_suelo(dict(rx=rx[:50], d=[19] * 50), T0, SC)
    assert c == 'indet'
    c, _ = A.clase_suelo(dict(rx=rx, d=[19] * 200), T0, None)
    assert c == 'sin_clase'


def test_aceptacion_censura_y_ack():
    I = {f'0x{k}': dict(coin='ETH', tok=TOK, size=5.0) for k in range(10)}
    P = {o: dict(t_send_ns=0, t_ack_ns=100 * NS) for o in I}
    led = dict(intenciones=I, posts=P, cancels={}, corruptas=0)
    filas = [dict(oid=o, coin='ETH', tipo='alta', estado='ancla', lat_ex_ms=40.0, lat_rx_ms=60.0, ack_http_ms=100.0, adelantado=False, clase='lo') for o in list(I)[:9]]
    filas.append(dict(oid='0x9', coin='ETH', tipo='alta', estado='censurada_0', censura_ms=600.0, ack_http_ms=100.0))
    r = A.agrega(filas, led, {o: 'ETH' for o in I})['alta']['ETH']
    assert r['tasa_censura'] == 0.1 and r['aceptacion']['censura_ok'] and r['por_clase']['lo']['n'] == 9
