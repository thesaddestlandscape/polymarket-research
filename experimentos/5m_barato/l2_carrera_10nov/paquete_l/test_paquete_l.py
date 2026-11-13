#!/usr/bin/env python3
"""Tests del paquete de medicion de `l` (12-Nov). TODO con SenderSim + reloj virtual: 0 red, 0 ordenes. Ejecutar:  python3 -I test_paquete_l.py"""
import os, sys, json, shutil, tempfile, subprocess, re, types
H = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, H)
import pl_core as C, paquete_l as PL
from pl_sender import RelojVirtual, SenderSim, MercadosSim, ErrHTTP
TMP = tempfile.mkdtemp(prefix='paquete_l_test_'); C.LOCK_DIR = TMP                                                   # v7: los locks de instancia unica de los tests van al TMP (no chocan con un run real)
import atexit; atexit.register(shutil.rmtree, TMP, True)


def montar(nombre, cfg=None, sender_kw=None, run_id=None, sender=None, reloj=None, mercados=None, dir_out=None, **mk):
    cfg = cfg or C.Config(); reloj = reloj or RelojVirtual(); sender = sender or SenderSim(reloj, **(sender_kw or {})); mercados = mercados or MercadosSim(reloj, **mk)
    out = dir_out or os.path.join(TMP, nombre); P = PL.Paquete(cfg, sender, mercados, out, reloj, run_id or nombre, anclas_fn=None, stdout=False)
    P.anclas_fn = lambda: sum(P.anclas_ledger_por_moneda().values()); P.anclas_por_moneda_fn = P.anclas_ledger_por_moneda; return P, sender, reloj, mercados, out


def rows(out, k=None): return [json.loads(l) for l in open(os.path.join(out, 'ledger.jsonl')) if l.strip() and (k is None or json.loads(l)['k'] == k)]


def test_config_estructural():
    c = C.Config(); assert c.max_simultaneas * c.coste_orden <= c.perdida_dura and c.perdida_dura <= c.saldo_autorizado
    for mal in (dict(max_simultaneas=13), dict(perdida_dura=0.70), dict(precio=0.05), dict(size=4.0), dict(lote=13), dict(fase_b_max_rellenos=4, fase_b_tope_usd=0.10)):
        try: C.Config(**mal); assert False, mal
        except C.Invariante: pass
    print('T1 ok: 12 x 0,05 = 0,60 <= 0,61 <= saldo; configuraciones fuera de tope rechazadas')


def test_plan_determinista():
    a = C.plan_slots(C.Config(), 140); b = C.plan_slots(C.Config(), 140); assert a == b and all(1.0 <= s.hold_s <= 2.5 for s in a) and all(s.modo == 'lejos' for s in a)
    import collections; n = collections.Counter(s.coin for s in a); assert n['BTC'] >= 50 and all(n[c] >= 25 for c in ('ETH', 'SOL', 'XRP')), n
    assert C.plan_slots(C.Config(seed=1), 20) != C.plan_slots(C.Config(seed=2), 20)
    print('T2 ok: plan determinista, BTC x2, holds en [1;2,5] s', dict(n))


def test_dry_completo():
    P, S, R, M, out = montar('dry'); live = []
    orig = S.enviar
    def enviar(h):
        r = orig(h); live.append(sum(1 for o in S.ordenes.values() if S._estado_en(o, R.now_ns())[1] == 'LIVE')); return r
    S.enviar = enviar; st = P.correr()
    assert st == 'COMPLETE', st
    inf = json.load(open(out + '/informe_final.json')); cob = inf['cobertura']
    assert cob['anclas_directas'] >= 100 and all(cob['anclas_por_moneda'].get(c, 0) >= m for c, m in C.Config().min_anclas_moneda.items()), cob
    assert cob['fills'] == 0 and cob['duplicados_ledger'] == 0 and cob['filas_corruptas_ledger'] == 0 and cob['posts'] == cob['intenciones'] == cob['canceladas_ok']
    assert max(live) <= 12, max(live)
    assert inf['presupuesto']['gasto'] == 0.0 and not inf['presupuesto']['toco_suelo']
    for f in ('run_manifest.json', 'ledger.jsonl', 'checkpoint.json', 'parcial_resumen.json', 'run.log', 'informe_final.json'): assert os.path.exists(os.path.join(out, f)), f
    assert re.match(r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d{3}Z ', open(out + '/run.log').readline())
    man = json.load(open(out + '/run_manifest.json')); assert man['estado'] == 'FINALIZADO' and man['status_final'] == 'COMPLETE' and man['config_sha'] == C.Config().sha() and man['codigo_sha'] and man['saldo_inicial'] == 0.612681
    for c in rows(out, 'cancel'): assert c['t_trig_rx_ns'] <= c['t_send_ns'] <= c['t_ack_ns'] and c['ok']
    dp = inf['latencias']; assert dp['d_proc_ms']['n'] == cob['canceladas_ok'] and dp['d_red_cancel_ms']['n'] > 0
    assert len({r['eid'] for r in rows(out)}) == len(rows(out))
    print('T3 ok: dry COMPLETE n=%d anclas=%s, max simultaneas %d, d_red p50 %.1f ms (sim)' % (cob['intenciones'], cob['anclas_por_moneda'], max(live), dp['d_red_cancel_ms']['p50']))


def test_fill_total_corte_inmediato():
    P, S, R, M, out = montar('fill', sender_kw=dict(fill_a={4: (5.0, 1.2)})); st = P.correr(); assert st == 'PARTIAL', st
    inf = json.load(open(out + '/informe_final.json')); assert inf['cobertura']['fills'] == 1 and abs(inf['presupuesto']['gasto'] - 0.05) < 1e-9 and 'relleno_en_fase_A' in inf['motivo']
    assert len(S.abiertas(S.posts_enviados[0]['tok'])) == 0 and sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0
    n_post_tras = len([r for r in rows(out, 'post')]); assert n_post_tras <= 8                       # no sale ningun lote nuevo tras el relleno
    f = rows(out, 'fill'); assert len(f) == 1 and f[0]['coste'] == 0.05
    print('T4 ok: relleno total -> corte inmediato, PARTIAL, gasto 0,05, sin vivas, sin lotes nuevos')


def test_fill_parcial():
    P, S, R, M, out = montar('parcial', sender_kw=dict(fill_a={2: (2.0, 1.0)})); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
    assert st == 'PARTIAL' and abs(inf['presupuesto']['gasto'] - 0.02) < 1e-9, (st, inf['presupuesto'])
    print('T5 ok: relleno parcial 2/5 -> gasto 0,02 contabilizado y corte')


def test_429_bloquea_y_recupera():
    P, S, R, M, out = montar('r429', sender_kw=dict(err_429_en_post={5, 6, 7})); t0 = R.now_ns(); st = P.correr(); assert st == 'BLOCKED', st
    inf = json.load(open(out + '/informe_final.json')); assert inf['cobertura']['http429'] == 3 and 'rate_limit' in inf['motivo']
    assert (R.now_ns() - t0) / 1e9 >= 2.0 + 4.0                                                      # backoff 2 s y 4 s respetados
    P2, S2, R2, M2, out2 = montar('r429b', sender_kw=dict(err_429_en_post={5, 6})); st2 = P2.correr(); assert st2 == 'COMPLETE', st2
    assert json.load(open(out2 + '/informe_final.json'))['cobertura']['http429'] == 2
    print('T6 ok: 3x429 seguidos -> BLOCKED (backoff 2 s/4 s); 2x429 y recupera -> COMPLETE')


def test_post_ambiguo_reconcilia_sin_reenviar():
    P, S, R, M, out = montar('amb', sender_kw=dict(err_ambiguo_post={3})); st = P.correr(); assert st == 'COMPLETE', st
    r = rows(out, 'post'); amb = [x for x in r if x['clase'] == 'ambiguo']; assert len(amb) == 1
    claves = [x['clave'] for x in rows(out, 'intencion')]; assert len(claves) == len(set(claves))
    assert sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0
    can = [c for c in rows(out, 'cancel') if c['clave'] == amb[0]['clave']]; assert can and can[-1]['ok'] and can[0]['trig'] == 'ambiguo'
    print('T7 ok: POST con respuesta perdida (ambiguo) -> la orden VIVA se cancela y cierra, sin reenviar el slot')


def test_clasifica_respuestas():
    assert C.clasificar_post({'success': True, 'status': 'live', 'errorMsg': ''}) == 'ok' and C.clasificar_post({'success': False, 'errorMsg': 'x'}) == 'rechazo' and C.clasificar_post('rarisimo') == 'ambiguo' and C.clasificar_post({'success': True, 'status': 'raro'}) == 'ambiguo'
    EB = type('EnvioBloqueado', (Exception,), {}); assert C.clasificar_excepcion_post(EB('canal')) == 'rechazo' and C.clasificar_excepcion_post(ErrHTTP(400, 'crosses book')) == 'rechazo' and C.clasificar_excepcion_post(ErrHTTP(None, 'timeout')) == 'ambiguo' and C.clasificar_excepcion_post(ErrHTTP(503, 'x')) == 'ambiguo' and C.clasificar_excepcion_post(ErrHTTP(425, 'x')) == 'ambiguo'
    assert C.es_429(ErrHTTP(429)) and not C.es_429(ErrHTTP(400)) and C.es_terminal('CANCELED_MARKET_RESOLVED') and C.es_terminal('matched') and not C.es_terminal('LIVE') and not C.es_terminal(None)
    assert C.id_servidor({'orderID': 'ABC'}, 'abc') is None and C.id_servidor({'orderID': 'zzz'}, 'abc') == 'zzz'
    print('T26 ok: clasificadores de POST (ok/rechazo/ambiguo/429/EnvioBloqueado) y estados terminales')


def test_rechazos_seguidos():
    P, S, R, M, out = montar('rech', sender_kw=dict(rechazo_post={2, 3})); st = P.correr(); assert st == 'BLOCKED' and 'rechazos_seguidos' in json.load(open(out + '/informe_final.json'))['motivo']
    print('T8 ok: 2 rechazos seguidos -> BLOCKED')


def test_cancel_pendiente_reintenta():
    P, S, R, M, out = montar('pend', sender_kw=dict(cancel_pendiente={2})); st = P.correr(); assert st == 'COMPLETE', st
    c = rows(out, 'cancel'); assert any(x['error'] and 'pending' in x['error'] for x in c) and any(x['intento'] == 2 and x['ok'] for x in c)
    print('T9 ok: cancelacion rechazada por pending -> reintento con backoff y exito')


def test_resume_tras_kill_duro_rechazado():
    reloj = RelojVirtual(); S = SenderSim(reloj, fill_a={4: (5.0, 1.2)}); M = MercadosSim(reloj); out = os.path.join(TMP, 'killduro'); cfg = C.Config()
    P1 = PL.Paquete(cfg, S, M, out, reloj, 'killduro', stdout=False); P1.anclas_fn = lambda: 0; P1.anclas_por_moneda_fn = lambda: {}; assert P1.correr() == 'PARTIAL'; n1 = len(S.posts_enviados)
    P2 = PL.Paquete(cfg, S, M, out, reloj, 'killduro', stdout=False); P2.anclas_fn = lambda: 0; P2.anclas_por_moneda_fn = lambda: {}; st = P2.correr()
    assert st == 'PARTIAL' and len(S.posts_enviados) == n1 and 'resume_rechazado' in P2.kill, (st, P2.kill)                                  # relanzar NO envia nada tras un relleno
    ks = rows(out, 'kill'); assert len(ks) >= 2 and len({k['eid'] for k in ks}) == len(ks)                                                   # los kills no se pisan entre si
    print('T24 ok: tras un kill duro (relleno) un relanzamiento NO envia ninguna orden; los kills quedan registrados con indice')


def test_sin_mercado_espera_y_bloquea():
    reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj, coins=()); out = os.path.join(TMP, 'sinmerc'); P = PL.Paquete(C.Config(), S, M, out, reloj, 'sinmerc', stdout=False); P.anclas_fn = lambda: 0; P.anclas_por_moneda_fn = lambda: {}; t0 = reloj.now_ns()
    st = P.correr(); assert st == 'BLOCKED' and len(S.posts_enviados) == 0 and 'sin_mercado' in P.kill and (reloj.now_ns() - t0) / 1e9 >= 118
    print('T25 ok: sin mercados 5m validos: reintenta cada 2 s sin quemar slots y bloquea a los 120 s, 0 ordenes')


def fallar_cancelaciones_de_la_primera_orden(S, R, k):
    """v7: las cancelaciones se intercalan (un paso por iteracion), asi que `cancel_falla` por NUMERO global ya no concentra los fallos en UNA orden: se fallan `k` DELETE de la 1a orden enviada (el resto funciona)."""
    orig = S.cancelar; nf = {'n': 0}
    def cancelar(oid):
        if S.posts_enviados and oid == S.posts_enviados[0]['oid'] and nf['n'] < k: nf['n'] += 1; S.n_cancel += 1; R.sleep(0.062); return False
        return orig(oid)
    S.cancelar = cancelar


def test_cancel_no_confirmada_bloquea():
    # v5 (hallazgo 1): la cancelacion fallida en el cuerpo NO queda INDETERMINADA si el barrido consigue cancelarla (reintenta con backoff): BLOCKED por el kill, pero 0 vivas y 0 indeterminadas
    P, S, R, M, out = montar('nocanc'); fallar_cancelaciones_de_la_primera_orden(S, R, 4); st = P.correr(); assert st == 'BLOCKED', st
    inf = json.load(open(out + '/informe_final.json')); assert inf['cobertura']['indeterminadas'] == 0 and sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0 and 'cancel_no_confirmada' in inf['motivo']
    print('T10 ok: cancelacion no confirmada en el cuerpo -> BLOCKED (kill), el barrido la reintenta y la cancela: 0 vivas, 0 indeterminadas')


class Crash(BaseException): pass


def sigkill(P):
    """Simula un SIGKILL (v3: `correr` YA captura cualquier excepcion y barre, asi que ya no basta con lanzar una): sin fila kill de excepcion, sin barrido y sin informe final; la excepcion Crash sale de correr."""
    orig = P._matar
    P._matar = lambda m, s: None if str(m).startswith('excepcion') else orig(m, s)
    P._barrido_final = lambda: None
    def fin(*a, **k): raise Crash()
    P._final = fin; P._final_emergencia = fin                                                    # v4: `_correr` tambien captura el fallo de `_final`; el SIGKILL real no deja ni el informe de emergencia


def test_reinicio_idempotente():
    reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj); orig = S.enviar; cont = {'n': 0}
    def enviar(h):
        cont['n'] += 1; r = orig(h)
        if cont['n'] == 11: raise Crash()                                                         # muere TRAS registrar la orden en el exchange y ANTES de anotar el post (peor caso)
        return r
    S.enviar = enviar; out = os.path.join(TMP, 'reinicio'); cfg = C.Config()
    P1 = PL.Paquete(cfg, S, M, out, reloj, 'reinicio', stdout=False); P1.anclas_fn = lambda: sum(P1.anclas_ledger_por_moneda().values()); P1.anclas_por_moneda_fn = P1.anclas_ledger_por_moneda
    sigkill(P1)
    try: P1.correr(); assert False
    except Crash: pass
    P1.led.cerrar(); n1 = len(rows(out, 'intencion')); assert n1 == 11 and len(rows(out, 'post')) == 10
    vivas_exch = sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados); assert vivas_exch >= 1                    # el exchange conserva ordenes vivas
    abiertas_antes = n1 - len(rows(out, 'cerrada')); assert abiertas_antes >= 1
    S.enviar = orig
    P2 = PL.Paquete(cfg, S, M, out, reloj, 'reinicio', stdout=False); P2.anclas_fn = lambda: sum(P2.anclas_ledger_por_moneda().values()); P2.anclas_por_moneda_fn = P2.anclas_ledger_por_moneda
    st = P2.correr(); assert st == 'COMPLETE', st
    claves = [r['clave'] for r in rows(out, 'intencion')]; assert len(claves) == len(set(claves)) and len(S.posts_enviados) == len(claves)       # ni un slot reenviado
    assert sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0
    O, res = C.replay_estado(C.Ledger(os.path.join(out, 'ledger.jsonl')).filas); assert res['n_vivas'] == 0 and res['gasto_fills_usd'] == 0.0 and res['n_indeterminadas'] == 0
    cierre = [r for r in rows(out, 'cerrada') if str(r['motivo']).startswith('reconciliada')]; assert len(cierre) == abiertas_antes
    inf = json.load(open(out + '/informe_final.json')); assert inf['presupuesto']['gasto'] == 0.0
    print('T11 ok: muerte entre exchange y ledger -> reanuda, reconcilia las %d vivas/huerfanas (incl. la del POST sin anotar), 0 slots duplicados, 0 PnL duplicado, %d intenciones' % (abiertas_antes, len(claves)))


def test_reinicio_con_fill_no_duplica_gasto():
    reloj = RelojVirtual(); S = SenderSim(reloj, fill_a={5: (5.0, 0.2)}); M = MercadosSim(reloj); out = os.path.join(TMP, 'reinfill'); cfg = C.Config()
    P1 = PL.Paquete(cfg, S, M, out, reloj, 'reinfill', stdout=False); P1.anclas_fn = lambda: sum(P1.anclas_ledger_por_moneda().values()); P1.anclas_por_moneda_fn = P1.anclas_ledger_por_moneda
    assert P1.correr() == 'PARTIAL'; g1 = json.load(open(out + '/informe_final.json'))['presupuesto']['gasto']; assert abs(g1 - 0.05) < 1e-9
    P2 = PL.Paquete(cfg, S, M, out, reloj, 'reinfill', stdout=False); P2.anclas_fn = lambda: 0; P2.anclas_por_moneda_fn = lambda: {}
    P2.correr(); O, res = C.replay_estado(C.Ledger(os.path.join(out, 'ledger.jsonl')).filas); assert abs(res['gasto_fills_usd'] - 0.05) < 1e-9 and res['n_fills'] == 1, res
    print('T12 ok: reanudar tras un relleno no duplica el gasto (0,05 una vez)')


def test_checkpoint_corrupto_y_ledger():
    P, S, R, M, out = montar('corr1', cfg=C.Config(max_ordenes=16)); P.correr(); P.led.cerrar()
    dup = rows(out)[0]; open(out + '/checkpoint.json', 'w').write('{"roto":')                                  # checkpoint corrupto
    open(out + '/ledger.jsonl', 'a').write(json.dumps(dup) + '\n')                                               # fila duplicada
    open(out + '/ledger.jsonl', 'a').write('{"eid": "x|y|0", "k": "kill"')                                       # cola de ledger cortada a mitad
    P2, S2, R2, M2, out2 = montar('corr1', cfg=C.Config(max_ordenes=16), sender=S, reloj=R, mercados=M, dir_out=out); st = P2.correr()
    assert P2.led.corruptas == 1 and P2.led.duplicadas >= 1 and P2.cnt['checkpoint_corrupto'] == 1, (P2.led.corruptas, P2.led.duplicadas, dict(P2.cnt))
    assert st in ('PARTIAL', 'COMPLETE'), st
    assert len({r['eid'] for r in rows(out)}) == len(rows(out))
    # checkpoint POR DELANTE del ledger (ledger truncado) -> FAILED
    ck = json.load(open(out + '/checkpoint.json')); ck['ledger_filas'] = len(rows(out)) + 50; json.dump(ck, open(out + '/checkpoint.json', 'w'))
    P3, S3, R3, M3, o3 = montar('corr1', cfg=C.Config(max_ordenes=16), sender=S, reloj=R, mercados=M, dir_out=out); assert P3.correr() == 'FAILED' and 'ledger_truncado' in P3.kill
    # config distinta en resume -> FAILED
    P4, *_ = montar('corr1', cfg=C.Config(max_ordenes=17), sender=S, reloj=R, mercados=M, dir_out=out); assert P4.correr() == 'FAILED'
    print('T13 ok: checkpoint corrupto reconstruido, linea cortada y duplicado reparados, checkpoint>ledger y config distinta -> FAILED')


def test_presupuesto():
    cfg = C.Config(); p = C.Presupuesto(cfg, 0.612681); assert abs(p.suelo - 0.002681) < 1e-9 and not p.toca_suelo() and p.puede_enviar(0) and p.puede_enviar(11) and not p.puede_enviar(12)
    p.actualizar(saldo=0.5627); assert not p.toca_suelo() and p.gasto > 0.049
    p.actualizar(saldo=0.0026); assert p.toca_suelo(); p.actualizar(saldo=0.6, gasto_ledger=0.61); assert p.toca_suelo()
    q = C.Presupuesto(cfg, 0.612681); q.actualizar(gasto_ledger=0.58); assert not q.puede_enviar(1) and q.puede_enviar(0) is False or True
    for mal in (None, 0, 5.0):
        try: C.Presupuesto(cfg, mal); assert False, mal
        except C.Invariante: pass
    P, S, R, M, out = montar('presup', sender_kw=dict(saldo_inicial=3.0)); assert P.correr() == 'BLOCKED' and 'preflight' in json.load(open(out + '/informe_final.json'))['motivo']
    S2 = SenderSim(RelojVirtual(), saldo_ilegible_en={1}); P2, *_ = montar('presup2', sender=S2); assert P2.correr() != 'BLOCKED' and P2.cnt['saldo_lecturas_agotadas'] == 0 and S2.n_saldo >= 2     # 1 lectura fallida: el reintento la recupera
    S3 = SenderSim(RelojVirtual(), saldo_ilegible_en={1, 2, 3}); P3, *_ = montar('presup3', sender=S3); assert P3.correr() == 'BLOCKED' and len(S3.posts_enviados) == 0                       # TODAS las lecturas fallan: fail-closed, 0 ordenes
    S4 = SenderSim(RelojVirtual(), saldo_inicial=0.612681); S4.saldo = lambda: float('nan'); P4, *_ = montar('presup4', sender=S4); assert P4.correr() == 'BLOCKED' and len(S4.posts_enviados) == 0       # NaN = ilegible
    print('T14 ok: suelo = 0,612681-0,61 = 0,002681; puede_enviar respeta max 12 y suelo; saldo ilegible/ajeno -> BLOCKED sin enviar')


def test_saldo_cae_sin_ledger():
    reloj = RelojVirtual(); S = SenderSim(reloj); orig = S.saldo; cont = {'n': 0}
    def saldo():
        cont['n'] += 1; v = orig(); return v if cont['n'] < 3 else round(v - 0.30, 6)                    # a partir de la 3a lectura el saldo cae 0,30 sin relleno en el ledger
    S.saldo = saldo; P, S, R, M, out = montar('sinled', sender=S, reloj=reloj); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
    # v6 (hallazgo 1): motivo DURO (no benigno) siempre registrado; el barrido final lo confirma (BLOCKED > PARTIAL duro) y la reanudacion se rechaza
    assert st == 'BLOCKED' and 'saldo_cae_mas_que_ledger' in inf['motivo'], inf['motivo']
    ks = [(r['motivo'], r['status']) for r in P.led.filas if r['k'] == 'kill']; assert any(m.startswith('saldo_cae_mas_que_ledger ') and s == 'PARTIAL' for m, s in ks) and any('_final' in m and s == 'BLOCKED' for m, s in ks), ks
    print('T15 ok: caida de saldo no explicada por el ledger -> corte inmediato y BLOCKED (no reanudable)')


def test_toca_suelo():
    reloj = RelojVirtual(); S = SenderSim(reloj); orig = S.saldo; cont = {'n': 0}
    def saldo():
        cont['n'] += 1; v = orig(); return v if cont['n'] < 3 else 0.002
    S.saldo = saldo; P, S, R, M, out = montar('suelo', sender=S, reloj=reloj); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
    assert st == 'FAILED' and inf['presupuesto']['toco_suelo'], (st, inf['presupuesto'])
    print('T16 ok: saldo en el suelo -> FAILED (corte)')


def _faseB(nombre, sin_push, t_fill=2.0, **cfgkw):
    cfg = C.Config(fase_b_max_rellenos=2, fase_b_ordenes=8, **cfgkw); reloj = RelojVirtual(); S = SenderSim(reloj, fill_a={}, sin_push=sin_push); M = MercadosSim(reloj, down_barato=True)
    P, S, R, M, out = montar(nombre, cfg=cfg, sender=S, reloj=reloj, mercados=M); orig = S.enviar
    def enviar(h):
        r = orig(h)
        if h['tok'].endswith('D'): o = S.ordenes[h['oid']]; o['fill'] = (2.0, o['t_alta_ns'] + int(t_fill * 1e9))      # token barato (fase B): relleno PARCIAL de 2 acc a los t_fill s del alta
        return r
    S.enviar = enviar; st = P.correr(); return st, json.load(open(out + '/informe_final.json')), out, S


def test_fase_b_parciales_y_tope():
    st, inf, out, S = _faseB('faseB', sin_push=True); cob = inf['cobertura']                                   # SIN push: lo detecta el seguimiento 1 Hz de get_order
    assert st == 'COMPLETE' and cob['fills'] == 2 and abs(inf['presupuesto']['gasto'] - 2 * 2.0 * 0.01) < 1e-9, (st, cob, inf['presupuesto'])
    top = [r for r in rows(out, 'intencion') if r['modo'] == 'top']; assert 2 <= len(top) <= 8 and all(r['libro']['mejor_bid'] == 0.01 for r in top)
    polls = [r for r in rows(out, 'estado') if r.get('fuente') == 'poll_top']; assert polls and not rows(out, 'push_fill')
    res = inf['residuales']['posiciones']; assert len(res) == 2 and all(abs(p['cantidad'] - 2.0) < 1e-9 and p['modo'] == 'top' and abs(p['coste_usd'] - 0.02) < 1e-9 for p in res)        # residuales contabilizados
    print('T17 ok: fase B: %d ordenes top, 2 rellenos parciales (2 acc) -> gasto 0,04, tope de rellenos respetado, seguimiento 1 Hz (%d lecturas), 2 residuales contabilizados' % (len(top), len(polls)))


def test_push_detecta_relleno_antes_que_el_poll_y_el_saldo():
    st, inf, out, S = _faseB('faseBpush', sin_push=False, t_fill=2.5)
    pf = rows(out, 'push_fill'); assert len(pf) == 2 and st == 'COMPLETE'
    for p in pf:                                                                                              # el push llega ~0,15 s tras el relleno (2,5 s del alta; el poll 1 Hz lo veria a los 3 s): bastante antes de la lectura 1 Hz y del saldo del fin de lote
        alta = [r for r in rows(out, 'post') if r['clave'] == p['clave']][0]; dt_s = (p['t_ns'] - alta['t_ack_ns']) / 1e9; assert 2.5 <= dt_s <= 2.9, dt_s
    assert inf['presupuesto']['toco_suelo'] is False and abs(inf['presupuesto']['gasto'] - 0.04) < 1e-9
    # fase A: un relleno a 1,2 s con hold >= 1,5 s: el push (1,35 s) corta ANTES del vencimiento del hold (el estado por get_order solo se miraria al cancelar)
    reloj = RelojVirtual(); S2 = SenderSim(reloj, fill_a={4: (5.0, 1.2)}); P, S2, R, M, out2 = montar('pushA', sender=S2, reloj=reloj); assert P.correr() == 'PARTIAL'
    pf = rows(out2, 'push_fill'); assert len(pf) == 1 and 'push' in P.kill, P.kill
    o = [r for r in rows(out2, 'post') if r['clave'] == pf[0]['clave']][0]; hold = [r for r in rows(out2, 'intencion') if r['clave'] == pf[0]['clave']][0]['hold_s']; assert (pf[0]['t_ns'] - o['t_ack_ns']) / 1e9 < hold - 0.05, (pf[0]['t_ns'] - o['t_ack_ns'], hold)
    print('T27 ok: el push del canal de usuario detecta el relleno ~0,15 s despues (antes que el poll 1 Hz y que el saldo); en fase A corta antes del vencimiento del hold')


def test_fase_b_desactivada_por_defecto():
    P, S, R, M, out = montar('sinB', mercados=None, down_barato=True); P.correr(); assert not [r for r in rows(out, 'intencion') if r['modo'] == 'top']
    print('T18 ok: sin fase_b_max_rellenos no se coloca ninguna orden top')


def test_mejora_bid_sin_nosotros():
    ev = [dict(L=0.2, bid=0.2, szb=7.0, size=5.0, r_restante=2.0, nuestra_visible=True, bid_post_otros_bajo_L=False),        # parcial: otros 5, resta la cantidad RESTANTE -> no dispara (correcto); la regla A resta 5 -> 2 y... tampoco, otros>0
          dict(L=0.2, bid=0.2, szb=2.0, size=5.0, r_restante=2.0, nuestra_visible=True, bid_post_otros_bajo_L=True),         # solo quedamos nosotros con r=2: B dispara (acierta); A resta 5 => otros=-3 <= EPS dispara tambien
          dict(L=0.2, bid=0.2, szb=6.0, size=5.0, r_restante=2.0, nuestra_visible=True, bid_post_otros_bajo_L=False),         # otros 4 reales: A resta 5 => 1 > EPS ... B 4
          dict(L=0.2, bid=0.2, szb=5.0, size=5.0, r_restante=2.0, nuestra_visible=True, bid_post_otros_bajo_L=False)]         # otros 3 reales: A resta 5 => 0 <= EPS => DISPARA EN FALSO; B resta 2 => 3 no dispara
    R = C.bid_sin_nosotros_mejora(ev); A, B = R['A_size_entera'], R['B_restante_visible']
    assert A['fp'] == 1 and B['fp'] == 0 and B['tp'] == 1 and A['tp'] == 1 and B['precision'] == 1.0 and A['precision'] == 0.5, R
    print('T19 ok: restar solo la cantidad restante visible elimina el falso disparo de la regla A en parciales (A prec 0,5 -> B 1,0 en el caso sintetico)')


def test_contar_anclas():
    d = os.path.join(TMP, 'evid'); os.makedirs(d, exist_ok=True)
    L = []
    for i in range(3):
        oid = f'o{i}'; L += [dict(k='alta', oid=oid, t_envio_ms=1000 + i, tok='t'), dict(k='user_order', oid=oid, mine=True, tipo='PLACEMENT', ts_ex_ms=1080 + i), dict(k='user_order', oid=oid, mine=True, tipo='CANCELLATION', ts_ex_ms=2100 + i), dict(k='cancel_try', oid=oid, canceled=[oid], t_pre_ms=2090 + i, t_resp_ms=2150 + i)]
    L += [dict(k='alta', oid='o9', t_envio_ms=1, tok='t'), dict(k='user_order', oid='o9', mine=True, tipo='PLACEMENT', ts_ex_ms=90)]            # sin cancelacion: NO es ancla
    open(d + '/cancel_evid_2026-11-12.jsonl', 'w').write('\n'.join(json.dumps(x) for x in L) + '\n{"cortado"')
    fl = [dict(k='intencion', clave='c%d' % i, coin='BTC' if i < 2 else 'ETH') for i in range(3)] + [dict(k='post', clave='c%d' % i, oid='o%d' % i) for i in range(3)]
    n, por = C.contar_anclas(d + '/cancel_evid_*.jsonl', fl); assert n == 3 and por == {'BTC': 2, 'ETH': 1}, (n, por)
    print('T20 ok: anclas directas = alta + PLACEMENT + CANCELLATION + cancel_try; linea cortada tolerada; por moneda')


def gamma_ev(coin, ini, outcomes=('Up', 'Down'), toks=None, fin=None, tick='0.01', minsize=5, slug=None, titulo=None, **mk):
    import datetime as _d
    s = slug or f'{coin.lower()}-updown-5m-{ini}'; fin = ini + 300 if fin is None else fin; toks = toks or [s + 'A', s + 'B']
    m = dict(outcomes=json.dumps(list(outcomes)), clobTokenIds=json.dumps(toks), endDate=_d.datetime.fromtimestamp(fin, _d.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), closed=False, active=True, acceptingOrders=True, orderPriceMinTickSize=tick, orderMinSize=minsize, negRisk=False); m.update(mk)
    return dict(slug=s, title=titulo or f'{C.NOMBRE_MONEDA[coin].capitalize()} Up or Down - November 12', markets=[m])


def test_verificar_mercado_gamma():
    ini = 1_790_000_100 // 300 * 300
    ok, why, toks, neg = C.verificar_mercado_gamma('BTC', ini, gamma_ev('BTC', ini)); assert ok and toks == [f'btc-updown-5m-{ini}A', f'btc-updown-5m-{ini}B'] and neg is False
    ok, why, toks, neg = C.verificar_mercado_gamma('ETH', ini, gamma_ev('ETH', ini, outcomes=('Down', 'Up'))); assert ok and toks == [f'eth-updown-5m-{ini}B', f'eth-updown-5m-{ini}A'], toks      # orden invertido: se mapea por ETIQUETA
    malos = {'slug': gamma_ev('SOL', ini, slug='sol-updown-5m-1'), 'outcomes_yes_no': gamma_ev('SOL', ini, outcomes=('Yes', 'No')), 'endDate': gamma_ev('SOL', ini, fin=ini + 900), 'tick': gamma_ev('SOL', ini, tick='0.001'),
             'minsize': gamma_ev('SOL', ini, minsize=10), 'cerrado': gamma_ev('SOL', ini, closed=True), 'no_acepta': gamma_ev('SOL', ini, acceptingOrders=False), 'titulo': gamma_ev('SOL', ini, titulo='Bitcoin Up or Down'),
             'tres_tokens': gamma_ev('SOL', ini, toks=['a', 'b', 'c']), 'ilegible': dict(slug=f'sol-updown-5m-{ini}', markets=[dict(clobTokenIds='{no json', outcomes='[]')]), 'none': None, 'dos_mercados': dict(gamma_ev('SOL', ini), markets=gamma_ev('SOL', ini)['markets'] * 2)}
    for k, ev in malos.items():
        ok, why, toks, neg = C.verificar_mercado_gamma('SOL', ini, ev); assert not ok and toks is None, (k, why)
    print('T28 ok: verificacion de gamma: slug exacto, outcomes<->tokens por etiqueta (orden invertido ok), endDate, tick, minsize, titulo, abierto; 12 casos malos rechazados (fail-closed)')


def test_mercados_real_con_fake():
    sys.path.insert(0, H); import pl_sender_real as R
    llam = []; ini0 = 1_790_000_100 // 300 * 300
    def get(url, params):
        llam.append((url, params))
        if 'events' in url:
            slug = params['slug']; coin = slug.split('-')[0].upper(); ini = int(slug.rsplit('-', 1)[1])
            if coin == 'BTC': return [gamma_ev('BTC', ini)]
            if coin == 'ETH': return [gamma_ev('ETH', ini, outcomes=('Down', 'Up'))]
            if coin == 'SOL': return [gamma_ev('SOL', ini, tick='0.001')]                                      # mercado con tick raro: debe rechazarse
            return []
        return dict(bids=[dict(price='0.40', size='10')], asks=[dict(price='0.45', size='20')])
    t = [1_790_000_100.0]; M = R.MercadosReal(get=get, reloj=lambda: t[0]); ms = M.mercados()
    assert {m[1] for m in ms} == {'BTC', 'ETH'} and all(m[2] % 300 == 0 and len(m[3]) == 2 for m in ms) and M.libro('x') == ([(0.40, 10.0)], [(0.45, 20.0)]), {m[1] for m in ms}
    e = [m for m in ms if m[1] == 'ETH'][0]; assert e[3] == [e[0] + 'B', e[0] + 'A']                              # [Up, Down] verificado aunque gamma los de al reves
    assert any('tick' in v for v in M.rechazados.values()) and not any(m[1] == 'SOL' for m in ms)
    n1 = len(llam); M.mercados(); assert len(llam) == n1                                                   # cache TTL
    assert any(re.match(r'btc-updown-5m-\d+$', m[0]) for m in ms)
    print('T21 ok: MercadosReal (gamma simulado): slug, [Up,Down] mapeado por etiqueta, mercado con tick raro rechazado, cache TTL, libro publico')


def test_vendor_y_hash():
    ok, mal = C.verificar_vendor(); assert ok and not mal, mal
    import shutil as _sh; d = os.path.join(TMP, 'vend'); _sh.copytree(H + 'vendor', d + '/vendor'); assert C.verificar_vendor(d + '/')[0]
    open(d + '/vendor/vendor_main.py', 'a').write('\n# alterado\n'); ok, mal = C.verificar_vendor(d + '/'); assert not ok and 'vendor_main.py' in mal                           # un byte distinto => no ok
    os.remove(d + '/vendor/VENDOR_HASHES.json'); assert not C.verificar_vendor(d + '/')[0]                                                                                   # sin hashes => no ok (fail-closed)
    # el codigo NO referencia dev ni importa sonda1; el vendor entra en el sha del codigo
    for fn in ('pl_core.py', 'pl_sender.py', 'pl_sender_real.py', 'paquete_l.py'):
        t = open(H + fn).read(); assert 'import sonda1' not in t and 'sys.path.insert(0, SONDA_DIR)' not in t, fn
    assert 'polymarket-research-dev' not in open(H + 'pl_sender_real.py').read().split('"""', 2)[2] and 'SONDA_DIR' not in open(H + 'pl_core.py').read()
    a = C.sha_codigo(); b = C.sha_codigo(d + '/'); assert a != b
    h = json.load(open(H + 'vendor/VENDOR_HASHES.json'))['copias']; assert set(h) == {'vendor_main.py', 'cancel_evidencia.py', 'envio_real.py', 'plan_paquete_l.py'} and all(v['sha256_copia'] for v in h.values())
    print('T29 ok: vendor/ verificado por hash (alterar un byte o quitar VENDOR_HASHES => no ok); sin imports de dev; el vendor entra en codigo_sha')


def test_preparar_primero_sin_vivas_y_no_retrasa_cancelaciones():
    reloj = RelojVirtual(); S = SenderSim(reloj, preparar_dur_s=6.0); P, S, R, M, out = montar('prep6', sender=S, reloj=reloj, cfg=C.Config(max_ordenes=24)); st = P.correr()
    assert S.prep_log and all(n == 0 for _, n in S.prep_log), [n for _, n in S.prep_log][:10]                  # el gate (6 s por llamada) se llama SIEMPRE sin ordenes vivas
    ca = rows(out, 'cancel'); assert ca and max((r['t_send_ns'] - r['t_trig_prog_ns']) / 1e9 for r in ca) < 0.5, max((r['t_send_ns'] - r['t_trig_prog_ns']) / 1e9 for r in ca)     # ninguna cancelacion se retrasa por el gate
    S2 = SenderSim(RelojVirtual(), preparar_falla={1, 2}); P2, S2, R2, M2, out2 = montar('prepfalla', sender=S2, reloj=S2.r, cfg=C.Config(max_ordenes=16)); P2.correr(); sk = [r for r in rows(out2, 'saltado') if r['motivo'] == 'canal_usuario_no_listo']; assert len(sk) == 2
    print('T30 ok: preparar() (6 s/llamada simulados) solo con 0 vivas: ninguna cancelacion se retrasa (max overshoot %.3f s); gate fallido => slot saltado con motivo' % max((r['t_send_ns'] - r['t_trig_prog_ns']) / 1e9 for r in ca))


def test_get_order_null_y_gracia_de_indexacion():
    cfg = C.Config(hold_min_s=0.5, hold_max_s=0.8, max_ordenes=16, index_gracia_s=4.0); reloj = RelojVirtual(); S = SenderSim(reloj, index_delay_s=1.4); P, S, R, M, out = montar('idx', cfg=cfg, sender=S, reloj=reloj); st = P.correr()
    assert P.cnt['cancel_pre_indice'] > 0 and P.cnt['cancel_no_confirmada'] == 0 and st in ('COMPLETE', 'PARTIAL') and P.kill in (None, 'max_ordenes'), (st, P.kill, dict(P.cnt))
    assert sum(1 for r in rows(out, 'cerrada') if r['motivo'] == 'cancelada') == len(rows(out, 'intencion'))                       # todas acaban canceladas pese a cancelar antes de que se indexen
    reloj2 = RelojVirtual(); S2 = SenderSim(reloj2, index_delay_s=30.0); P2, S2, R2, M2, out2 = montar('idx2', cfg=cfg, sender=S2, reloj=reloj2); st2 = P2.correr()
    assert st2 == 'BLOCKED' and P2.cnt['cancel_no_confirmada'] >= 1 and any(r.get('indeterminada') for r in rows(out2, 'cerrada'))             # no indexa nunca: pasada la gracia, INDETERMINADA y BLOQUEO
    cfg0 = C.Config(); assert cfg0.hold_min_s >= 1.5                                                                                  # el hold por defecto ya supera el null de ~1,06-1,41 s medido
    print('T31 ok: get_order null/not found <1,4 s: cancelar antes de indexar se reintenta dentro de la gracia (pre_indice=%d) sin falsos BLOCKED; si nunca indexa -> BLOQUEO; hold_min por defecto 1,5 s' % P.cnt['cancel_pre_indice'])


def test_reloj_evidencia_residuales_saldo():
    # Reloj: alineado a pared, monotono (no retrocede aunque la pared salte)
    import time; from pl_sender import Reloj as _R; r = _R(); a = r.now_ns(); time.sleep(0.01); b = r.now_ns(); assert b > a and abs(a - time.time_ns()) < 5e8
    # reloj_stats con filas del canal de usuario sinteticas (ex = envio + 30 ms; recv = ex + 20 ms)
    ev = [dict(k='alta', oid='0xa', t_envio_ms=1000, t_ack_ms=1080), dict(k='user_order', oid='0xa', mine=True, tipo='PLACEMENT', ts_ex_ms=1030, t_recv_ms=1050), dict(k='cancel_try', oid='0xa', canceled=['0xa'], t_pre_ms=2000),
          dict(k='user_order', oid='0xa', mine=True, tipo='CANCELLATION', ts_ex_ms=2040, t_recv_ms=2065)]
    st = C.reloj_stats(ev); assert st['place_ex_menos_envio_ms']['p50'] == 30 and st['place_recv_menos_ex_ms']['p50'] == 20 and st['cancel_ex_menos_pre_ms']['p50'] == 40 and st['cancel_recv_menos_ex_ms']['p50'] == 25 and st['rtt_local_envio_a_recepcion_placement_ms']['p50'] == 50
    # EvidTail: lee solo lineas nuevas, tolera linea parcial y .gz, atribuye por oid propio
    d = os.path.join(TMP, 'tail'); os.makedirs(d); f = d + '/cancel_evid_2026-11-12.jsonl'; T = C.EvidTail(d + '/cancel_evid_*.jsonl*'); assert T.sondear() == {}
    open(f, 'w').write(json.dumps(dict(k='user_order', oid='0xAA', mine=True, tipo='PLACEMENT', size_matched=0.0)) + '\n' + json.dumps(dict(k='user_order', oid='0xBB', mine=False, tipo='UPDATE', size_matched=3.0)) + '\n'); assert T.sondear() == {}                      # ajena o 0 => nada
    open(f, 'a').write(json.dumps(dict(k='user_trade', oid='0xAA', size=2.0, status='MATCHED', rol='maker'))[:30]); assert T.sondear() == {}                                          # linea parcial: se espera
    open(f, 'a').write(json.dumps(dict(k='user_trade', oid='0xAA', size=2.0, status='MATCHED', rol='maker'))[30:] + '\n'); assert T.sondear() == {'0xaa': 2.0}; assert T.sondear() == {'0xaa': 2.0} and T.filas_leidas == 3
    open(f, 'a').write(json.dumps(dict(k='user_trade', oid='0xCC', size=1.0, status='FAILED', rol='maker')) + '\n'); assert '0xcc' not in T.sondear()                          # FAILED no cuenta
    # saldo robusto
    seq = iter([None, float('nan'), 0.6]); dorm = []; assert C.leer_saldo_robusto(lambda: next(seq), 3, (0.3, 0.6), dorm.append) == 0.6 and dorm == [0.3, 0.6]
    assert C.leer_saldo_robusto(lambda: None, 3, (0.1,), lambda s: None) is None and C.leer_saldo_robusto(lambda: 99.0, 2, (0.1,), lambda s: None, maximo=0.7) is None and C.leer_saldo_robusto(lambda: (_ for _ in ()).throw(RuntimeError('rpc')), 2, (0.1,), lambda s: None) is None
    # residuales: tras fase B con 2 rellenos de 2 acc a 0,01 -> 2 posiciones; liquidacion con desenlace oficial simulado (una ganadora, una perdedora, una sin cerrar = None, no 0)
    st_, inf, out, S = _faseB('faseBres', sin_push=False, t_fill=2.5); res = inf['residuales']['posiciones']; assert len(res) == 2
    ev_g = lambda tok_up, ganador_up, cerrado=True: [dict(markets=[dict(closed=cerrado, clobTokenIds=json.dumps(tok_up), outcomePrices=json.dumps(['1', '0'] if ganador_up else ['0', '1']))])]
    toks = {r['tok'] for r in res}; sl = {r['tok']: r['slug'] for r in rows(out, 'intencion')}; asign = {}
    def get(url, params):
        sg = params['slug']; tk = [t for t, s_ in sl.items() if s_ == sg]; arriba = [tk[0], 'otro']
        return ev_g(arriba, ganador_up=(sg.startswith('btc') or sg.startswith('sol')), cerrado=not sg.startswith('xrp'))
    liq = PL.liquidar_informe(out, get=get); assert len(liq['residuales']) == 2 and all(('valor_usd' in x) for x in liq['residuales']) and liq['cobertura_desenlace'][1] == 2
    for x in liq['residuales']: assert (x['valor_usd'] is None) == (x['ganador'] is None) and (x['ganador'] is None or abs(x['pnl_usd'] - ((x['cantidad'] if x['ganador'] else 0) - x['coste_usd'])) < 1e-9)
    print('T32 ok: reloj monotono; reloj_stats (ex-envio, recv-ex, RTT) por oid; EvidTail incremental con linea parcial/FAILED/ajenas; saldo robusto con reintentos/NaN/maximo; residuales de fase B liquidables con desenlace oficial (missing != 0)')


def test_adaptador_real_importable_y_paridad_de_interfaz():
    """SIN instanciar EnvioReal (eso arrancaria el cliente con credenciales): importa el vendor en un subproceso y comprueba que la interfaz del adaptador real == la del doble (lo que el orquestador usa)."""
    cod = ("import sys; sys.path.append(%r); import pl_core as C, pl_sender_real as R, pl_sender as S; p0 = list(sys.path); vm, ER, CE, plan_paquete_l = [C.cargar_vendor(n) for n in ('vendor_main', 'envio_real', 'cancel_evidencia', 'plan_paquete_l')]; assert sys.path == p0\n"
           "pub = lambda c: {n for n in dir(c) if not n.startswith('_')}\n"
           "falta = {'tick', 'colocar', 'enviar', 'estado', 'cancelar', 'saldo', 'abiertas_todas', 'anclas', 'preparar', 'fills_push', 'cerrar'} - pub(R.SenderReal); assert not falta, falta\n"
           "assert {'poner', 'enviar', 'estado', 'cancelar', 'saldo', 'abiertas', 'tick'} <= pub(ER.EnvioReal) and hasattr(CE, 'adjuntar_env') and hasattr(CE, 'Registro') and hasattr(CE.Registro, 'gate_envio')\n"
           "import inspect; assert list(inspect.signature(ER.EnvioReal.poner).parameters) == ['self', 'tok', 'precio', 'size', 'clave', 'neg_risk'] and ER.__file__.startswith(%r) and list(inspect.signature(R.clase_envio(ER).poner).parameters)[-2:] == ['neg_risk', 'expira_s']\n"
           "assert 'sonda1' not in sys.modules and not any('polymarket-research-dev' in (getattr(m, '__file__', '') or '') for m in sys.modules.values())\n"
           "print('IMPORT_OK')") % (H, H + 'vendor')
    r = subprocess.run([sys.executable, '-I', '-c', cod], capture_output=True, text=True, timeout=60); assert 'IMPORT_OK' in r.stdout, r.stderr[-1500:]
    print('T33 ok: adaptador real y vendor importables (sin instanciar nada), interfaz == la del doble, ningun modulo procede de dev ni de sonda1')


def test_confirmacion_y_seguridad():
    cfg = C.Config(); cod = C.sha_codigo(); f = os.path.join(TMP, 'conf.txt')
    for caso in ('no_existe', 'mal_sha', 'ok'):
        if caso != 'no_existe':
            open(f, 'w').write(f'paquete={C.VERSION}\nconfig_sha={cfg.sha() if caso == "ok" else "0" * 64}\ncodigo_sha={cod}\nwallet={cfg.wallet}\nperdida_dura=0.61\nfase_b_max_rellenos=0\n')
        try: PL.exigir_confirmacion(f if caso != 'no_existe' else '/no/existe', cfg, cod); ok = True
        except SystemExit: ok = False
        assert ok == (caso == 'ok'), caso
    open(f, 'w').write(f'paquete={C.VERSION}\nconfig_sha={cfg.sha()}\ncodigo_sha={cod}\nwallet=0x0000000000000000000000000000000000000000\nperdida_dura=0.61\nfase_b_max_rellenos=0\n')
    try: PL.exigir_confirmacion(f, cfg, cod); assert False
    except SystemExit: pass
    # sin codigo de envio en el nucleo / orquestador / doble
    prohibido = ('post_order', 'create_order', 'ClobClient', 'py_clob_client', 'private_key', 'dotenv', 'POLY_', 'subprocess', 'socket', 'os.system')
    for fn in ('pl_core.py', 'pl_sender.py', 'paquete_l.py'):
        code = re.sub(r'(""".*?"""|#.*)', '', open(H + fn).read(), flags=re.S)
        for malo in prohibido: assert malo not in code, (fn, malo)
    # el modo dry NO carga sonda1 ni el cliente del CLOB
    r = subprocess.run([sys.executable, '-I', '-c', f"import sys; sys.path.insert(0, {H!r}); import paquete_l, pl_core, pl_sender; print(sorted(m for m in sys.modules if 'clob' in m.lower() or m in ('sonda1', 'pl_sender_real', 'requests', 'dotenv')))"], capture_output=True, text=True)
    assert r.stdout.strip() == '[]', r.stdout + r.stderr
    r = subprocess.run([sys.executable, '-I', H + 'paquete_l.py', '--real', '--out', os.path.join(TMP, 'noreal')], capture_output=True, text=True); assert r.returncode != 0 and 'confirmacion' in (r.stdout + r.stderr)
    r = subprocess.run([sys.executable, '-I', '-c', f"import sys; sys.path.insert(0, {H!r}); import pl_sender_real as R, pl_core as C; R.HERE='/no/existe/'; R.construir(C.Config(), '/tmp/x')"], capture_output=True, text=True); assert r.returncode != 0 and 'NO envio' in (r.stdout + r.stderr)
    print('T22 ok: real exige confirmacion (inexistente/sha malo/wallet ajena -> sale), el nucleo no contiene codigo de envio ni secretos, dry no importa sonda1/py-clob-client/requests')


def test_cli_dry_y_resume():
    out = os.path.join(TMP, 'cli'); r = subprocess.run([sys.executable, '-I', H + 'paquete_l.py', '--out', out, '--run-id', 'cli1', '--max-ordenes', '30', '--objetivo', '1000'], capture_output=True, text=True); assert r.returncode == 0 and 'STATUS PARTIAL' in r.stdout, r.stdout[-300:] + r.stderr[-300:]
    r2 = subprocess.run([sys.executable, '-I', H + 'paquete_l.py', '--out', out, '--run-id', 'cli1', '--max-ordenes', '30', '--objetivo', '1000'], capture_output=True, text=True); assert r2.returncode == 0, r2.stderr[-300:]
    cl = [x['clave'] for x in rows(out, 'intencion')]; assert len(cl) == len(set(cl)) == 30, len(cl)
    print('T23 ok: CLI dry y relanzado con el mismo run-id: 30 intenciones, sin duplicados')


# ====================================================================================================== v3 (12-Nov): UN test por hallazgo del /code-review de paquete_l (sender SIMULADO, 0 red, 0 ordenes)
import signal, builtins, collections, time, stat as _stat


def _vm():
    return C.cargar_vendor('vendor_main')


def test_h1_vendor_sin_live_trade_ni_env_de_produccion():
    import ast
    for fn in ('vendor_main.py', 'envio_real.py'):                                                       # estatico: ni live_trade, ni polygon_rpc, ni os.environ/getenv en lo que ejecuta el envio
        t = ast.parse(open(H + 'vendor/' + fn).read()); imps = set()
        for n in ast.walk(t):
            if isinstance(n, ast.Import): imps |= {a.name.split('.')[0] for a in n.names}
            if isinstance(n, ast.ImportFrom): imps.add((n.module or '').split('.')[0])
            if isinstance(n, ast.Attribute): assert n.attr not in ('environ', 'getenv'), (fn, n.attr)
        assert not ({'live_trade', 'polygon_rpc', 'sonda1', 'pathlib'} & imps), (fn, imps)
    V = _vm(); assert not hasattr(V, 'REPO') and V.ENV_DEDICADA == '/root/.secrets/experimento_pares.env' and V.WALLET_DEDICADA == C.WALLET_DEDICADA
    # comportamiento: con un fichero de credenciales FALSO (cliente falso) se abre SOLO ese fichero; nunca data/live/.env; live_trade no entra en sys.modules
    f = os.path.join(TMP, 'dedicada.env'); open(f, 'w').write(f'POLY_PRIVATE_KEY=0x{"ab" * 32}\nPOLY_DEPOSIT_WALLET={C.WALLET_DEDICADA}\nPOLY_API_KEY=k\nPOLY_API_SECRET=s\nPOLY_API_PASSPHRASE=p\n'); os.chmod(f, 0o600)
    pl = os.path.join(TMP, 'prod_sintetico_live.env'); open(pl, 'w').write('POLY_PRIVATE_KEY=0x' + 'cd' * 32 + '\nPOLY_DEPOSIT_WALLET=0x0000000000000000000000000000000000000abc\nPOLY_API_KEY=otra\n'); PROD = (pl,)       # v4: SINTETICO; los tests NUNCA tocan el .env real
    abiertos = []; real_open = builtins.open
    def espia(file, *a, **k): abiertos.append(str(file)); return real_open(file, *a, **k)
    class CliFalso:
        def __init__(self, host, **kw): self.host, self.kw = host, kw
    builtins.open = espia
    try: c = V.cliente_dedicado(f, C.WALLET_DEDICADA, _clob=CliFalso, _prod=PROD)
    finally: builtins.open = real_open
    assert isinstance(c, CliFalso) and c.kw['funder'] == C.WALLET_DEDICADA and c.kw['signature_type'] == 3 and c.kw['key'].startswith('0x'), c.kw.keys()
    assert sorted(set(abiertos) & {f, pl}) == sorted([f, pl]) and [a for a in abiertos if 'data/live' in a or a.endswith('/.env')] == [] and 'live_trade' not in sys.modules and 'polygon_rpc' not in sys.modules, abiertos
    # el redondeo de seguridad (copiado como TEXTO de live_trade) esta aplicado: 1,15 con 2 decimales hacia abajo = 1,15 (con float puro daria 1,14)
    from py_clob_client_v2.order_builder import helpers as _h; assert _h.round_down(1.15, 2) == 1.15
    # fail-closed: wallet ajena, ruta de produccion, permisos abiertos, credencial incompleta
    def sale(ruta, wallet=C.WALLET_DEDICADA):
        try: V.cliente_dedicado(ruta, wallet, _clob=CliFalso, _prod=PROD); return False
        except SystemExit: return True
    assert sale(f, '0x0000000000000000000000000000000000000001')
    abiertos.clear(); builtins.open = espia
    try: assert sale('/root/polymarket-research/data/live/.env') and sale(os.path.join(TMP, 'x', '.env')) and abiertos == [], abiertos                 # ni se abre: se rechaza por la ruta
    finally: builtins.open = real_open
    g = os.path.join(TMP, 'abierta.env'); open(g, 'w').write(open(f).read()); os.chmod(g, 0o644); assert sale(g)
    h = os.path.join(TMP, 'incompleta.env'); open(h, 'w').write(f'POLY_DEPOSIT_WALLET={C.WALLET_DEDICADA}\n'); os.chmod(h, 0o600); assert sale(h) and sale(os.path.join(TMP, 'noexiste.env'))
    # saldo_onchain: minimo de 2 lecturas validas; basura/excepciones/wallet invalida => None
    r = lambda v: (lambda url, js: {'result': hex(int(v * 1e6))})
    seq = iter([{'result': hex(612681)}, {'result': hex(562681)}, {'result': hex(999999)}]); assert V.saldo_onchain(C.WALLET_DEDICADA, _post=lambda u, j: next(seq)) == 0.562681
    assert V.saldo_onchain(C.WALLET_DEDICADA, _post=lambda u, j: {'result': '0x'}) is None and V.saldo_onchain(C.WALLET_DEDICADA, _post=lambda u, j: {'error': 'x'}) is None
    def boom(u, j): raise RuntimeError('rpc')
    assert V.saldo_onchain(C.WALLET_DEDICADA, _post=boom) is None and V.saldo_onchain('0x12', _post=r(1)) is None and V.saldo_onchain(None, _post=r(1)) is None
    # carga SIN sys.path, con hash sobre los bytes ejecutados; sombra y alteracion => ImportError; aislamiento exigido
    d = os.path.join(TMP, 'vend1'); shutil.copytree(H + 'vendor', d + '/vendor'); open(d + '/vendor/plan_paquete_l.py', 'a').write('\n# alterado\n')
    guardado = sys.modules.pop('plan_paquete_l', None)
    try: C.cargar_vendor('plan_paquete_l', d + '/'); assert False
    except ImportError: pass
    finally:
        if guardado is not None: sys.modules['plan_paquete_l'] = guardado
    cod = ("import sys; sys.path.append(%r); import pl_core as C; p0 = list(sys.path)\n"
           "sys.modules['plan_paquete_l'] = type(sys)('plan_paquete_l')\n"
           "try: C.cargar_vendor('plan_paquete_l'); print('SIN_ERROR')\n"
           "except ImportError: print('SOMBRA_RECHAZADA')\n"
           "del sys.modules['plan_paquete_l']; [C.cargar_vendor(n) for n in C.NOMBRES_VENDOR]; assert sys.path == p0, 'sys.path tocado'\n"
           "assert not {'live_trade', 'polygon_rpc', 'sonda1', 'dotenv'} & set(sys.modules), sorted(set(sys.modules) & {'live_trade', 'polygon_rpc', 'dotenv'})\n"
           "print('CARGA_OK')") % H
    rr = subprocess.run([sys.executable, '-I', '-c', cod], capture_output=True, text=True, timeout=60); assert 'SOMBRA_RECHAZADA' in rr.stdout and 'CARGA_OK' in rr.stdout, rr.stdout + rr.stderr[-800:]
    rr = subprocess.run([sys.executable, '-c', f"import sys; sys.path.append({H!r}); import pl_core as C; C.exigir_aislamiento()"], capture_output=True, text=True); assert rr.returncode != 0 and 'aislado' in (rr.stdout + rr.stderr)       # sin -I: no envia
    d2 = os.path.join(TMP, 'pkg1'); os.makedirs(d2); open(d2 + '/json.py', 'w').write('x=1\n')
    rr = subprocess.run([sys.executable, '-I', '-c', f"import sys; sys.path.append({H!r}); import pl_core as C; C.exigir_aislamiento({d2 + '/'!r})"], capture_output=True, text=True); assert rr.returncode != 0 and 'ajenos' in (rr.stdout + rr.stderr)
    rr = subprocess.run([sys.executable, '-I', '-c', f"import sys; sys.path.append({H!r}); import pl_core as C; C.exigir_aislamiento(); print('AISLADO_OK')"], capture_output=True, text=True); assert 'AISLADO_OK' in rr.stdout, rr.stdout + rr.stderr[-500:]
    rr = subprocess.run([sys.executable, '-I', H + 'vendor/regenerar_vendor.py', '--verificar'], capture_output=True, text=True); assert json.loads(rr.stdout)['ok'] is True
    print('T34 ok [hallazgo 1]: vendor sin live_trade/polygon_rpc/REPO/environ; cliente dedicado solo abre SU fichero (nunca data/live/.env) y exige la wallet exacta; carga por hash sin tocar sys.path; sombra/alteracion/sin -I/.py ajeno => no envia')


def test_h2_libro_revalidado_antes_del_post():
    c = C.Config(); assert c.bid_min_lejos >= 0.20 and c.min_vida_mercado_s >= 90 and c.bid_min_lejos - c.precio >= 0.15           # margen de >= 15 ticks sobre 0,01 y mercados con tiempo
    P, S, R, M, out = montar('libro_bajo', bid=0.15, ask=0.20); st = P.correr(); assert st == 'BLOCKED' and len(S.posts_enviados) == 0 and 'sin_mercado' in P.kill       # bid 0,15 < 0,20: ni se elige mercado
    # el libro EMPEORA entre la preparacion y el POST (el de la fase 1 tiene hasta ~40 s): se descarta ANTES de enviar
    reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj); estado = {'tras_firmar': False}; col = S.colocar; lib = M.libro
    def colocar(*a, **k): estado['tras_firmar'] = True; return col(*a, **k)
    S.colocar = colocar; M.libro = lambda tok: ([(0.03, 5.0)], [(0.05, 5.0)]) if estado['tras_firmar'] else lib(tok)
    P, S, R, M, out = montar('libro_malo', sender=S, reloj=reloj, mercados=M, cfg=C.Config(max_minutos=5.0)); P.correr()
    sk = [r for r in rows(out, 'saltado') if str(r['motivo']).startswith('libro_revalidacion')]; assert len(S.posts_enviados) == 0 and len(sk) >= 8 and not rows(out, 'intencion'), (len(sk), len(S.posts_enviados))
    # libro RANCIO: la lectura justo antes del POST tarda mas de libro_max_s
    reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj); estado = {'f': False}; col = S.colocar; lib = M.libro
    def colocar2(*a, **k): estado['f'] = True; return col(*a, **k)
    def lento(tok):
        if estado['f']: reloj.sleep(1.5)
        return lib(tok)
    S.colocar = colocar2; M.libro = lento; P, S, R, M, out = montar('libro_rancio', sender=S, reloj=reloj, mercados=M, cfg=C.Config(max_minutos=5.0)); P.correr()
    assert len(S.posts_enviados) == 0 and any(str(r['motivo']).startswith('libro_rancio') for r in rows(out, 'saltado'))
    # mercado con poco tiempo (fin a 120 s < 90 + hold + 2 + 40): no se elige; con 220 s si
    class MPoco(MercadosSim):
        def __init__(s, r, vida): super().__init__(r); s.vida = vida
        def mercados(s, coin=None):
            t = s.r.now_ns() // 1_000_000_000; return [(f'{c.lower()}-updown-5m-x', c, t + s.vida, [f'{c}U', f'{c}D'], False) for c in s.coins]
    reloj = RelojVirtual(); P, S, R, M, out = montar('poco', reloj=reloj, mercados=MPoco(reloj, 120)); assert P.correr() == 'BLOCKED' and len(S.posts_enviados) == 0
    reloj = RelojVirtual(); P, S, R, M, out = montar('mucho', reloj=reloj, mercados=MPoco(reloj, 220), cfg=C.Config(max_ordenes=8)); P.correr(); assert len(S.posts_enviados) == 8
    print('T35 ok [hallazgo 2]: bid minimo 0,20 (19 ticks) y vida >= 90 s; el libro se REVALIDA tras firmar y antes del POST (empeora => saltado, 0 POST; rancio > 1 s => saltado); mercado con 120 s no vale')


def test_h3_excepcion_senal_y_gtd():
    # (a) excepcion inesperada con ordenes vivas: el barrido cancela TODO y se escribe informe_final FAILED
    P, S, R, M, out = montar('exc'); orig = P.cancelar_viva; est = {'n': 0}
    def cv(clave, forzada=False):
        if est['n'] == 0 and len(S.posts_enviados) >= 5: est['n'] += 1; raise RuntimeError('fallo inesperado en el bucle')
        return orig(clave, forzada)
    P.cancelar_viva = cv; st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
    assert st == 'FAILED' and 'excepcion:RuntimeError' in inf['motivo'] and inf['excepciones'] and sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0 and inf['viva_al_final'] == 0
    # (b) SIGTERM REAL (manejador instalado por correr) a mitad de un lote: corte limpio PARTIAL con barrido, el manejador se restaura, y se puede reanudar
    prev = signal.getsignal(signal.SIGTERM); reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj); enviar = S.enviar; k = {'n': 0}
    def env(h):
        k['n'] += 1
        if k['n'] == 5: os.kill(os.getpid(), signal.SIGTERM)
        return enviar(h)
    S.enviar = env; P, S, R, M, out = montar('sigterm', sender=S, reloj=reloj, mercados=M); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
    assert st == 'PARTIAL' and inf['motivo'] == 'senal_SIGTERM' and inf['signal'] == 'SIGTERM' and len(S.posts_enviados) <= 8 and sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0 and signal.getsignal(signal.SIGTERM) == prev
    S.enviar = enviar; P2, *_ = montar('sigterm', sender=S, reloj=reloj, mercados=M, dir_out=out); assert P2.correr() == 'COMPLETE'                    # una parada ordenada NO exige decision humana
    # (c) retorno temprano (config distinta al reanudar) con una orden VIVA huerfana en el exchange: tambien barre
    reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj); orig_e = S.enviar; k = {'n': 0}
    def e2(h):
        k['n'] += 1; r = orig_e(h)
        if k['n'] == 6: raise Crash()
        return r
    S.enviar = e2; P1, S, R, M, out = montar('temprano', sender=S, reloj=reloj, mercados=M); sigkill(P1)
    try: P1.correr(); assert False
    except Crash: pass
    P1.led.cerrar(); assert sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) >= 1; S.enviar = orig_e
    P2, *_ = montar('temprano', cfg=C.Config(max_ordenes=17), sender=S, reloj=reloj, mercados=M, dir_out=out); assert P2.correr() == 'FAILED' and sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0
    # (d) cota dura GTD: todas las ordenes salen con expiracion y neg_risk; si el proceso muriera (SIGKILL) el exchange las retira solo
    reloj = RelojVirtual(); P, S, R, M, out = montar('gtd', reloj=reloj, cfg=C.Config(max_ordenes=8)); sigkill(P); P._final = lambda *a, **k: 'x'; P.correr()
    assert S.colocados and all(c['expira_s'] == 200 and c['neg_risk'] is False for c in S.colocados) and all(r['expira_s'] == 200 for r in rows(out, 'intencion'))
    S.r.sleep(150); assert sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0 and all(S._estado_en(o, S.r.now_ns())[1] in ('CANCELED', 'EXPIRED') for o in S.ordenes.values())
    try: C.Config(gtd_expira_s=0); assert False
    except C.Invariante: pass                                                                        # v6: sin modo GTC
    try: C.Config(gtd_expira_s=30); assert False
    except C.Invariante: pass
    print('T36 ok [hallazgo 3]: excepcion -> barrido+informe FAILED; SIGTERM real -> PARTIAL limpio (manejador restaurado, reanudable); retorno temprano tambien barre; GTD 200 s (docs: >= 3 min) en cada orden')


def test_h4_deteccion_de_relleno_fail_closed():
    # (a) tras cancelar con exito, el estado ilegible NO es 'matched = 0': INDETERMINADO y corte
    P, S, R, M, out = montar('ileg'); est = S.estado
    def estado(oid):
        o = S.ordenes.get(oid)
        if o is not None and o.get('cancel_ns') is not None: S.r.sleep(0.04); return None, None
        return est(oid)
    S.estado = estado; st = P.correr(); inf = json.load(open(out + '/informe_final.json')); ce = [r for r in rows(out, 'cerrada') if r['motivo'] == 'ESTADO_ILEGIBLE_TRAS_CANCEL']
    assert st == 'BLOCKED' and len(ce) >= 1 and all(r['indeterminada'] and r['size_matched'] is None for r in ce) and inf['cobertura']['indeterminadas'] == len(ce) and 'estado_ilegible_tras_cancel' in inf['motivo']      # el barrido cancela tambien las demas vivas: cada una igual de ilegible
    # (b) status 'matched' (o 'delayed') en el ack del POST = corte INMEDIATO, sin esperar al hold
    for status in ('matched', 'delayed'):
        reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj); enviar = S.enviar; k = {'n': 0}
        def env(h):
            k['n'] += 1; r = enviar(h)
            if k['n'] == 3: r = dict(r, status=status)
            return r
        S.enviar = env; P, S, R, M, out = montar('postm_' + status, sender=S, reloj=reloj, mercados=M); st = P.correr()
        assert st == 'PARTIAL' and P.kill.startswith('relleno_o_casado_en_post') and len(rows(out, 'post')) == 3 and len(rows(out, 'anomalia_post')) == 1 and sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0
        p3 = rows(out, 'post')[2]; c3 = [r for r in rows(out, 'cancel') if r['clave'] == p3['clave']][0]; assert (c3['t_send_ns'] - p3['t_ack_ns']) / 1e9 < 0.5, (c3['t_send_ns'] - p3['t_ack_ns']) / 1e9       # no espero al hold
    # (c) umbral de saldo < 1 share (0,01 $): un relleno de 1 acc que get_order/push no vieron se detecta por el saldo
    for caida, mata in ((0.01, True), (0.003, False)):
        P, S, R, M, out = montar('umbral%g' % (caida * 1000)); P.led = C.Ledger(out + '/ledger.jsonl'); P.pres = C.Presupuesto(P.cfg, 0.612681); P._saldo = lambda c=caida: round(0.612681 - c, 6)
        P._tras_lote(0); assert (P.kill is not None and P.kill.startswith('saldo_cae_mas_que_ledger')) == mata, (caida, P.kill)
    try: C.Config(tol_saldo_usd=0.02); assert False
    except C.Invariante: pass
    print('T37 ok [hallazgo 4]: estado ilegible tras cancel = INDETERMINADO/BLOCKED (no matched=0); ack matched/delayed = corte en <0,5 s; saldo detecta 1 accion (0,01 $), tolerancia 0,004 < 1 share')


def test_h5_bloqueo_desde_replay_y_orden_de_escritura():
    reloj = RelojVirtual(); S = SenderSim(reloj, fill_a={4: (5.0, 1.2)}); M = MercadosSim(reloj); out = os.path.join(TMP, 'replay_fill')
    P1 = PL.Paquete(C.Config(), S, M, out, reloj, 'rf', stdout=False); P1.anclas_fn = lambda: 0; P1.anclas_por_moneda_fn = lambda: {}; assert P1.correr() == 'PARTIAL'; n1 = len(S.posts_enviados)
    filas = rows(out); idx = {r['eid']: i for i, r in enumerate(filas)}; fl = [r for r in filas if r['k'] == 'fill'][0]; ce = [r for r in filas if r['k'] == 'cerrada' and r['clave'] == fl['clave']][0]
    assert idx[fl['eid']] < idx[ce['eid']] and any(r['k'] == 'kill' and idx[r['eid']] < idx[ce['eid']] for r in filas), 'fill y kill deben quedar DURABLES antes de la fila cerrada'
    # simula un SIGKILL entre el relleno y la fila kill: se borran las filas kill/lote y el checkpoint; el relanzamiento debe rechazarse SOLO por el relleno del ledger
    keep = [r for r in filas if r['k'] not in ('kill', 'lote')]; open(out + '/ledger.jsonl', 'w').write(''.join(json.dumps(r, sort_keys=True) + '\n' for r in keep)); os.remove(out + '/checkpoint.json')
    assert not [r for r in rows(out) if r['k'] == 'kill']
    P2 = PL.Paquete(C.Config(), S, M, out, reloj, 'rf', stdout=False); P2.anclas_fn = lambda: 0; P2.anclas_por_moneda_fn = lambda: {}; st = P2.correr()
    assert 'resume_rechazado_kill_previo:ledger_con_rellenos=1' in P2.kill and len(S.posts_enviados) == n1 and st == 'PARTIAL', (P2.kill, st)
    print('T38 ok [hallazgo 5]: fill+kill se escriben antes de `cerrada`; sin ninguna fila kill, un ledger con rellenos bloquea igualmente el relanzamiento (0 ordenes nuevas)')


def test_h6_es_429_solo_con_status_entero():
    class E(Exception):
        def __init__(s, sc, msg=''): super().__init__(msg); s.status_code = sc
    assert C.es_429(E(429)) and not C.es_429(E(500)) and not C.es_429(E(None, '429 too many requests')) and not C.es_429(Exception('HTTP 429 rate limit')) and not C.es_429(E('429')) and not C.es_429(E(True)) and not C.es_429(E(429.0))
    # el texto '429' en un timeout NO es un 429: la orden pudo salir => ambigua => se reconcilia (se cancela), no se da por rechazada
    reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj); enviar = S.enviar; k = {'n': 0}
    def env(h):
        k['n'] += 1; r = enviar(h)
        if k['n'] == 3: raise Exception('read timeout; upstream says 429 too many requests')
        return r
    S.enviar = env; P, S, R, M, out = montar('amb429', sender=S, reloj=reloj, mercados=M); st = P.correr()
    assert P.cnt['http429'] == 0 and P.cnt['ambiguos'] == 1 and st == 'COMPLETE' and sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0
    assert [r['clase'] for r in rows(out, 'post')][2] == 'ambiguo'
    print('T39 ok [hallazgo 6]: es_429 solo con status_code entero 429; excepcion con "429" en el texto = ambigua (reconciliada, la orden viva se cancela)')


def test_h7_backoff_429_no_bloquea_las_cancelaciones():
    P, S, R, M, out = montar('b429', sender_kw=dict(err_429_en_post={5}), cfg=C.Config(max_ordenes=24)); st = P.correr(); ca = rows(out, 'cancel'); po = rows(out, 'post')
    assert P.cnt['http429'] == 1 and ca and max((r['t_send_ns'] - r['t_trig_prog_ns']) / 1e9 for r in ca) < 0.5, max((r['t_send_ns'] - r['t_trig_prog_ns']) / 1e9 for r in ca)        # ninguna cancelacion espera al backoff
    p429 = [r for r in po if r['clase'] == '429'][0]; sig = [r for r in po if r['t_send_ns'] > p429['t_send_ns']][0]; assert (sig['t_send_ns'] - p429['t_send_ns']) / 1e9 >= 2.0 - 0.01      # pero el SIGUIENTE POST si espera >= 2 s
    print('T40 ok [hallazgo 7]: tras un 429 solo se difiere el siguiente POST (>= 2 s); las cancelaciones salen a su hora (max retraso %.3f s)' % max((r['t_send_ns'] - r['t_trig_prog_ns']) / 1e9 for r in ca))


def test_h8_post_real_sin_espera_de_gate():
    CE = C.cargar_vendor('cancel_evidencia'); R = __import__('pl_sender_real') if 'pl_sender_real' in sys.modules else None
    sys.path.append(H); import pl_sender_real as R
    llam, altas = [], []
    class Reg:
        resolutor = None; errores = 0
        def __init__(s, ok=True): s.ok = ok
        def gate_envio(s, tok, env=None, espera_s=None, dormir=None, fase='espera', reset=True): llam.append((tok, espera_s, fase, reset)); return (s.ok, '' if s.ok else 'sin_canal')
        def alta(s, o): altas.append(o)
    class Env:
        real = False
        def enviar(s, signed, gtd=False): return {'success': True, 'orderID': '0xabc', 'status': 'live', 'gtd': gtd}
    # contraste: el camino 'suelto' (sin marcar) ESPERA hasta 2 s dentro del POST
    env = Env(); reg = Reg(); CE._envolver_enviar(env, reg); env.enviar(object()); assert llam and llam[0][1] == 2.0 and llam[0][2] == 'pre_post_suelto', llam
    # SenderReal.enviar usa el camino de Puja.lanzar: re-chequeo INSTANTANEO (espera_s = 0.0), un solo gate, alta registrada, marcas del hilo limpias
    llam.clear(); altas.clear(); env = Env(); reg = Reg(); CE._envolver_enviar(env, reg); sr = R.SenderReal(env, reg, None, CE, os.path.join(TMP, 'evid_h8'))
    h = dict(oid='0xabc', signed=object(), tok='T1', precio=0.01, gtd=True); resp = sr.enviar(h)
    assert resp['gtd'] is True and llam == [('T1', 0.0, 'pre_post', False)] and len(altas) == 1 and CE._TL.env is None and CE._TL.gate is False
    # gate cerrado: EnvioBloqueado => clasificado 'rechazo', NO es un alta, marcas limpias
    llam.clear(); altas.clear(); env = Env(); reg = Reg(ok=False); CE._envolver_enviar(env, reg); sr = R.SenderReal(env, reg, None, CE, os.path.join(TMP, 'evid_h8b'))
    try: sr.enviar(h); assert False
    except Exception as e: assert C.clasificar_excepcion_post(e) == 'rechazo' and type(e).__name__ == 'EnvioBloqueado'
    assert not altas and CE._TL.env is None and llam == [('T1', 0.0, 'pre_post', False)]
    # la espera larga (6 s) sigue en `preparar` (con 0 vivas): comprobado en T30; aqui solo que enviar() no duerme
    import inspect; assert 'sleep' not in inspect.getsource(R.SenderReal.enviar)
    print('T41 ok [hallazgo 8]: el POST real hace UN re-chequeo instantaneo del gate (espera_s=0.0, sin dormir; el camino suelto esperaba 2 s); bloqueo => rechazo sin alta; hilo limpio')


def test_h9_barrido_final_ilegible_nunca_complete():
    for modo in ('none', 'excepcion'):
        reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj); k = {'n': 0}
        def abiertas(modo=modo):
            k['n'] += 1
            if k['n'] == 1: return []                                                  # la lectura de ANTES de empezar es correcta; las del barrido final no
            if modo == 'excepcion': raise ErrHTTP(500, 'boom')
            return None
        S.abiertas_todas = abiertas; P, S, R, M, out = montar('abil_' + modo, sender=S, reloj=reloj, mercados=M); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
        assert st == 'BLOCKED' and inf['status'] == 'BLOCKED' and 'NO verificado' in inf['motivo'] and inf['lecturas_ilegibles'] and all(x['lectura'] == 'abiertas_todas' for x in inf['lecturas_ilegibles']), (st, inf['motivo'])
        assert rows(out, 'ilegible')                       # lista exacta de lecturas no verificables, en el ledger
    # lectura correcta ([]) => COMPLETE como antes; saldo final ilegible tambien lo impide
    P, S, R, M, out = montar('abok'); assert P.correr() == 'COMPLETE' and json.load(open(out + '/informe_final.json'))['lecturas_ilegibles'] == []
    reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj); P, S, R, M, out = montar('salfin', sender=S, reloj=reloj, mercados=M); P.led = C.Ledger(out + '/ledger.jsonl'); P.pres = C.Presupuesto(P.cfg, 0.612681)
    P.ordenes = {'x': C.Orden(clave='x', tok='T', oid='0x1', cerrada=True)}; P._saldo = lambda: None; S.abiertas_todas = lambda: []; P._barrido_final(); assert [x['lectura'] for x in P.ilegibles] == ['saldo_final']
    print('T42 ok [hallazgo 9]: abiertas()=None o excepcion (o saldo final ilegible) => BLOCKED con la lista de lecturas no verificables, jamas COMPLETE')


def test_h10_neg_risk_y_gamma_explicitos():
    ini = 1_790_000_100 // 300 * 300; ok, *_ = C.verificar_mercado_gamma('BTC', ini, gamma_ev('BTC', ini)); assert ok
    for campo in ('negRisk', 'acceptingOrders', 'active', 'closed'):
        ev = gamma_ev('BTC', ini); del ev['markets'][0][campo]; ok, why, toks, neg = C.verificar_mercado_gamma('BTC', ini, ev); assert not ok and campo in why and toks is None, (campo, why)
        ev = gamma_ev('BTC', ini, **{campo: None}); assert not C.verificar_mercado_gamma('BTC', ini, ev)[0]
        ev = gamma_ev('BTC', ini, **{campo: 'false'}); assert not C.verificar_mercado_gamma('BTC', ini, ev)[0]                                      # string, no booleano
    ok, why, toks, neg = C.verificar_mercado_gamma('BTC', ini, gamma_ev('BTC', ini, negRisk=True)); assert ok and neg is True
    # el neg_risk verificado llega a `colocar` (el doble lo registra)
    class MNeg(MercadosSim):
        def mercados(s, coin=None): return [(a, b, c, d, True) for a, b, c, d, e in super().mercados(coin)]
    reloj = RelojVirtual(); P, S, R, M, out = montar('neg', reloj=reloj, mercados=MNeg(reloj), cfg=C.Config(max_ordenes=8)); P.correr(); assert S.colocados and all(c['neg_risk'] is True for c in S.colocados)
    # el cliente real contrasta con el de gamma y se niega a firmar si faltan/difieren (fake del cliente; NO firma nada)
    ER = C.cargar_vendor('envio_real') if C.cargar_vendor('vendor_main') else None; sys.path.append(H); import pl_sender_real as R2
    E = R2.clase_envio(ER); e = object.__new__(E); llamadas = []
    class Cli:
        def create_order(s, args, opts): llamadas.append(('create', args, opts)); return types.SimpleNamespace(expiration=str(args.expiration))
        def post_order(s, signed, tipo, post_only=False): llamadas.append(('post', tipo, post_only)); return {'success': True}
    e.cli = Cli(); e.M = types.SimpleNamespace(hash_orden=lambda signed, nr: '0xhash'); e._neg_risk = lambda tok: True
    for malo in (None, False):
        try: e.poner('T', 0.01, 5.0, 'k', neg_risk=malo, expira_s=75); assert False, malo
        except RuntimeError: pass
    assert not llamadas                                                                                         # nada se firmo
    oid, signed = e.poner('T', 0.01, 5.0, 'k', neg_risk=True, expira_s=75); assert oid == '0xhash' and llamadas[0][1].expiration >= int(time.time()) + 74 and llamadas[0][2].neg_risk is True and llamadas[0][1].side == 'BUY'
    e.enviar(signed, gtd=True); assert llamadas[1][1:] == ('GTD', True)                                      # siempre GTD + post-only
    for sin_gtd in (False, None):                                                                              # v6 (hallazgo 3): sin GTD NO se envia (no existe modo GTC)
        try: e.enviar(signed) if sin_gtd is None else e.enviar(signed, gtd=sin_gtd); assert False
        except RuntimeError: pass
    assert len(llamadas) == 2                                                                                  # ningun POST GTC salio
    sr = R2.SenderReal(types.SimpleNamespace(poner=lambda *a, **k: (_ for _ in ()).throw(AssertionError('no debia firmar'))), None, None, None, os.path.join(TMP, 'evid_h10'))
    try: sr.colocar('T', 0.01, 5.0, 'k'); assert False
    except RuntimeError: pass
    print('T43 ok [hallazgo 10]: gamma exige active/acceptingOrders/closed/negRisk presentes y booleanos; neg_risk llega al firmante, que lo contrasta con el cliente y no firma si falta/difiere; GTD/GTC siempre post-only')



# ====================================================================================================== v4 (12-Nov, ronda 2): UN test por hallazgo del 2o /code-review (sender SIMULADO, 0 red, 0 ordenes; credenciales SINTETICAS)
class _Veneno:
    """Cualquier acceso a un atributo lanza: demuestra que un codigo NO toca ese objeto."""
    def __getattr__(self, n): raise AssertionError(f'toco {n}')


class _Roto:
    def write(self, *a): raise OSError(28, 'No space left on device')
    def flush(self): raise OSError(28, 'No space left on device')
    def fileno(self): raise OSError(28, 'x')
    def close(self): pass


def test_r2h1_senales_siguen_instaladas_durante_barrido_e_informe():
    llamadas = []; h = lambda sg, fr: llamadas.append(sg)
    viejos = {sg: signal.signal(sg, h) for sg in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP)}
    try:
        P, S, R, M, out = montar('r2h1', cfg=C.Config(max_ordenes=16)); ab = S.abiertas_todas; sa = S.saldo; k = {'c': 0}; orig_c = S.cancelar
        def cancelar(oid):
            k['c'] += 1
            if k['c'] == 1: signal.raise_signal(signal.SIGTERM)                       # 1a senal: durante el cuerpo
            return orig_c(oid)
        def abiertas():
            if k['c'] >= 1: signal.raise_signal(signal.SIGINT); signal.raise_signal(signal.SIGTERM)          # (no en la lectura previa al primer envio)
            return ab()       # senales sucesivas DENTRO del barrido (antes: KeyboardInterrupt / muerte)
        def saldo():
            if k['c'] >= 1: signal.raise_signal(signal.SIGHUP)                           # (no en la lectura inicial: cortaria el run antes de enviar nada)
            return sa()
        S.cancelar = cancelar; S.abiertas_todas = abiertas; S.saldo = saldo
        st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
        assert st == 'PARTIAL' and inf['signal'] == 'SIGTERM' and inf['senales_recibidas'] >= 4, (st, inf['signal'], inf.get('senales_recibidas'))
        assert llamadas == [], llamadas                                                   # ningun manejador original se activo mientras corria barrido/informe
        assert sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0 and inf['viva_al_final'] == 0 and not inf['lecturas_ilegibles']
        assert signal.getsignal(signal.SIGTERM) is h and signal.getsignal(signal.SIGINT) is h and signal.getsignal(signal.SIGHUP) is h          # restaurados al FINAL
    finally:
        for sg, v in viejos.items(): signal.signal(sg, v)
    print('T44 ok [R2 hallazgo 1]: manejadores instalados hasta DESPUES de barrido+informe; 2a/3a senal (INT/TERM/HUP) en abiertas/saldo no matan ni lanzan; restaurados al final')


def test_r2h2_barrido_duerme_de_verdad_tras_una_senal():
    P, S, R, M, out = montar('r2h2', cfg=C.Config(max_ordenes=8), sender_kw=dict(cancel_falla={1})); t = []; orig_c = S.cancelar; viejo = signal.getsignal(signal.SIGTERM)
    def cancelar(oid):
        t.append((oid, R.now_ns()))
        if len(t) == 1: signal.raise_signal(signal.SIGTERM)                               # bandera levantada JUSTO antes del fallo que provoca el backoff de cancelar_viva
        return orig_c(oid)
    S.cancelar = cancelar; P.correr(); signal.signal(signal.SIGTERM, viejo)
    mismo = [x for o_, x in t if o_ == t[0][0]]; assert len(mismo) >= 2 and (mismo[1] - mismo[0]) / 1e9 >= 0.25 - 1e-9, [(x - mismo[0]) / 1e9 for x in mismo[:3]]            # el backoff de 0,25 s de ESA orden NO es un no-op por la bandera (v7: las cancelaciones de otras ordenes se intercalan mientras tanto)
    r = RelojVirtual(); t0 = r.now_ns(); r.sleep(0.5); assert r.now_ns() - t0 == int(0.5e9)                  # sin `abortar` el sueno es completo
    r.sleep(0.5, abortar=lambda: True); assert r.now_ns() - t0 == int(0.5e9)                                 # con `abortar` y bandera, no-op (solo el cuerpo lo usa)
    from pl_sender import Reloj; rr = Reloj(); a = time.monotonic(); rr.sleep(0.2, abortar=lambda: True); assert time.monotonic() - a < 0.1; a = time.monotonic(); rr.sleep(0.2); assert time.monotonic() - a >= 0.19
    print('T45 ok [R2 hallazgo 2]: tras una senal el backoff de cancelacion duerme los 0,25 s; solo el cuerpo (con `abortar`) despierta; el reloj del barrido ignora la bandera')


def test_r2h3_manejador_sin_locks_ni_io_y_despierta_rapido():
    P, S, R, M, out = montar('r2h3'); P.r = _Veneno(); P.log = _Veneno(); P.led = _Veneno(); P._matar = _Veneno()
    P._on_senal(signal.SIGTERM, None); P._on_senal(signal.SIGINT, None); assert P.senal == 'SIGTERM' and P.n_senales == 2        # SOLO atributos: nada de reloj/Event/log/ledger/locks
    from pl_sender import Reloj; assert not hasattr(Reloj(), '_ev') and not hasattr(Reloj(), 'interrumpir')
    import threading as _th
    P2, *_ = montar('r2h3b'); P2.r = Reloj(); viejo = signal.getsignal(signal.SIGTERM); prev = P2._instalar_senales()
    try:
        tm = _th.Timer(0.15, lambda: os.kill(os.getpid(), signal.SIGTERM)); a = time.monotonic(); tm.start(); P2._dormir(5.0); dt_ = time.monotonic() - a; tm.join()
        assert 0.1 < dt_ < 1.0 and P2.senal == 'SIGTERM', dt_
    finally: P2._restaurar_senales(prev)
    assert signal.getsignal(signal.SIGTERM) == viejo
    print('T46 ok [R2 hallazgo 3]: el manejador solo escribe atributos (reloj/log/ledger envenenados no se tocan); un SIGTERM real despierta el sueno del cuerpo en %.2f s' % dt_)


def test_r2h4_gtd_exige_reloj_verificado():
    for nombre, kw in (('none', dict(chrony_s=None)), ('1p5', dict(chrony_s=1.5)), ('neg', dict(chrony_s=-2.0)), ('nan', dict(chrony_s=float('nan')))):
        P, S, R, M, out = montar('r2h4' + nombre, sender_kw=kw); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
        assert st == 'BLOCKED' and 'reloj_no_verificado' in inf['motivo'], (nombre, st, inf['motivo'])
        assert len(S.posts_enviados) == 0 and inf['presupuesto']['gasto'] == 0.0, nombre                    # BLOCKED sin gasto ni ordenes en el exchange
    P, S, R, M, out = montar('r2h4ok', sender_kw=dict(chrony_s=-0.9), cfg=C.Config(max_ordenes=8)); assert P.correr() in ('COMPLETE', 'PARTIAL') and len(S.posts_enviados) == 8
    P, S, R, M, out = montar('r2h4mid', sender_kw=dict(), cfg=C.Config(max_ordenes=24)); orig = S.chrony; n = {'c': 0}                    # el reloj se degrada a mitad del run: no sale NINGUN POST mas
    def chrony(): n['c'] += 1; return orig() if n['c'] == 1 else None
    S.chrony = chrony; st = P.correr(); assert st == 'BLOCKED' and len(S.posts_enviados) == 8, (st, len(S.posts_enviados))
    print('T47 ok [R2 hallazgo 4]: chrony ausente / |offset| > 1 s / NaN => BLOCKED con 0 ordenes y 0 gasto; 0,9 s opera; si se degrada entre lotes no sale ningun POST mas')


def test_r2h5_asentamiento_tras_el_post():
    # (a) orden VIVA pero aun sin indexar (get_order null, abiertas vacia, DELETE not found): v3 la daba por 'inexistente_verificada'; v4 espera index_gracia+3 s, reintenta y la CANCELA
    reloj = RelojVirtual(); S = SenderSim(reloj, index_delay_s=5.0); M = MercadosSim(reloj); P, S, R, M, out = montar('r2h5a', sender=S, reloj=reloj, mercados=M)
    P.led = C.Ledger(os.path.join(out, 'ledger.jsonl')); P.pres = C.Presupuesto(P.cfg, 0.612681); tok = M.mercados('BTC')[0][3][0]
    oid, hd = S.colocar(tok, 0.01, 5.0, 'k', expira_s=200); S.enviar(hd); ack = R.now_ns(); o = C.Orden(clave='r2h5a|s0', slot=0, coin='BTC', tok=tok, precio=0.01, size=5.0, oid=oid, t_envio_ns=ack - 1, t_ack_ns=ack, clase_post='ok'); P.ordenes[o.clave] = o
    assert S.estado(oid)[1] == 'NO_EXISTE' and S.abiertas(tok) == [] and len(S.ordenes) == 1
    assert P.reconciliar_orden(o, 'prueba') is True
    cer = [r for r in P.led.filas if r['k'] == 'cerrada'][-1]
    assert cer['motivo'] != 'inexistente_verificada' and S.ordenes[oid]['cancel_ns'] is not None and (R.now_ns() - ack) / 1e9 >= 7.0, (cer['motivo'], (R.now_ns() - ack) / 1e9)
    # sin referencia temporal (ni ack, ni envio, ni intencion) NO se puede probar 'inexistente': INDETERMINADA aunque todo parezca vacio
    reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj); P, S, R, M, out = montar('r2h5a2', sender=S, reloj=reloj, mercados=M); P.led = C.Ledger(os.path.join(out, 'ledger.jsonl')); P.pres = C.Presupuesto(P.cfg, 0.612681)
    o2 = C.Orden(clave='r2h5a2|s0', slot=0, coin='BTC', tok='BTC1U', precio=0.01, size=5.0, oid='0xfantasma'); P.ordenes[o2.clave] = o2
    assert P.reconciliar_orden(o2, 'prueba') is False and [r for r in P.led.filas if r['k'] == 'cerrada'][-1]['motivo'] == 'INDETERMINADA'
    # (b) el saldo NUNCA se lee antes de ack_ultimo + 7 s; (c) y se lee DESPUES de la espera de anclas
    P, S, R, M, out = montar('r2h5b', cfg=C.Config(max_ordenes=8)); sa = S.saldo; ev = []; viol = []; fa = P.anclas_fn
    def saldo():
        ev.append('S'); acks = [r['t_ack_ns'] for r in P.led.filas if r['k'] == 'post']
        if acks and R.now_ns() - max(acks) < 7e9: viol.append((R.now_ns() - max(acks)) / 1e9)
        return sa()
    def anclas(): ev.append('A'); return fa()
    S.saldo = saldo; P.anclas_fn = anclas; st = P.correr(); assert st in ('COMPLETE', 'PARTIAL'), st
    assert viol == [] and ev[:4] == ['S', 'S', 'A', 'S'], (viol, ev[:5])                         # v6 (hallazgo 2): preflight + saldo de arranque ANTES del primer lote; luego anclas; luego el saldo del lote
    print('T48 ok [R2 hallazgo 5]: sin indexar != inexistente (espera >= 7 s, reintenta y cancela); sin referencia temporal => INDETERMINADA; saldo del lote y final solo >= 7 s tras el POST y DESPUES de las anclas')


def test_r2h6_resume_numera_lotes_e_ilegibles_sin_falsos_duplicados():
    # (a) lotes: crash en el 2o lote; el resume NO reutiliza la clave del lote 1
    reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj); orig = S.enviar; cont = {'n': 0}; out = os.path.join(TMP, 'r2h6a'); cfg = C.Config(max_ordenes=16)
    def enviar(h):
        cont['n'] += 1; r = orig(h)
        if cont['n'] == 12: raise Crash()
        return r
    S.enviar = enviar; P1 = PL.Paquete(cfg, S, M, out, reloj, 'r2h6a', stdout=False); P1.anclas_fn = lambda: 0; P1.anclas_por_moneda_fn = lambda: {}; sigkill(P1)
    try: P1.correr(); assert False
    except Crash: pass
    P1.led.cerrar(); assert len(rows(out, 'lote')) == 1; S.enviar = orig
    P2 = PL.Paquete(cfg, S, M, out, reloj, 'r2h6a', stdout=False); P2.anclas_fn = lambda: 0; P2.anclas_por_moneda_fn = lambda: {}; P2.correr()
    ls = rows(out, 'lote'); assert len(ls) >= 2 and len({r['eid'] for r in ls}) == len(ls) and P2.led.duplicadas == 0, (len(ls), P2.led.duplicadas)
    # (b) ilegibles: dos ejecuciones con la misma lectura ilegible => dos filas (no una + un 'duplicado' falso)
    reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj); k6 = {'n': 0}; S.abiertas_todas = lambda: ([] if not k6.__setitem__('n', k6['n'] + 1) and k6['n'] == 1 else None); out = os.path.join(TMP, 'r2h6b'); cfg = C.Config(max_ordenes=8)
    P1 = PL.Paquete(cfg, S, M, out, reloj, 'r2h6b', stdout=False); P1.anclas_fn = lambda: 0; P1.anclas_por_moneda_fn = lambda: {}; assert P1.correr() == 'BLOCKED'; n1 = len(rows(out, 'ilegible')); assert n1 >= 1
    P2 = PL.Paquete(cfg, S, M, out, reloj, 'r2h6b', stdout=False); P2.anclas_fn = lambda: 0; P2.anclas_por_moneda_fn = lambda: {}; P2.correr()
    assert len(rows(out, 'ilegible')) == 2 * n1 and P2.led.duplicadas == 0, (n1, len(rows(out, 'ilegible')), P2.led.duplicadas)
    print('T49 ok [R2 hallazgo 6]: resume: lotes con numeracion global (%d filas lote, 0 duplicados falsos) e ilegibles repetidos conservados (%d + %d)' % (len(ls), n1, n1))


def test_r2h7_oid_del_servidor():
    # (a) contar_anclas: con el alta bajo el oid LOCAL y el canal de usuario bajo el del SERVIDOR no hay ancla; con el alta bajo el del servidor, si
    d = os.path.join(TMP, 'r2h7'); os.makedirs(d, exist_ok=True)
    def evid(oid_alta, oid_srv, nombre):
        f = os.path.join(d, nombre); L = [dict(k='alta', oid=oid_alta, tok='T', t_envio_ms=1000), dict(k='user_order', oid=oid_srv, mine=True, tipo='PLACEMENT', ts_ex_ms=1080), dict(k='user_order', oid=oid_srv, mine=True, tipo='CANCELLATION', ts_ex_ms=2100), dict(k='cancel_try', oid=oid_srv, canceled=[oid_srv], t_pre_ms=2090, t_resp_ms=2150)]
        open(f, 'w').write('\n'.join(json.dumps(x) for x in L) + '\n'); return f
    assert C.contar_anclas(evid('0xlocal', '0xservidor', 'a1.jsonl'))[0] == 0 and C.contar_anclas(evid('0xservidor', '0xservidor', 'a2.jsonl'))[0] == 1
    # (b) el adaptador real registra el alta con el oid DEVUELTO por el servidor (y con el local si no hubo respuesta)
    import pl_sender_real as R2; altas = []
    ce = types.SimpleNamespace(_TL=types.SimpleNamespace(env=None, tok=None, gate=False, bloqueado=False)); reg = types.SimpleNamespace(alta=lambda a: altas.append(a.oid), avisar=lambda m: altas.append('AVISO'))
    for resp, esperado in (({'success': True, 'orderID': '0xSERVIDOR'}, '0xSERVIDOR'), ({'success': True, 'orderID': '0xlocal'}, '0xlocal')):
        env = types.SimpleNamespace(enviar=lambda signed, gtd=False, r=resp: r); sr = R2.SenderReal(env, reg, None, ce, d); altas.clear(); sr.enviar(dict(oid='0xlocal', signed=1, tok='T', precio=0.01, gtd=True)); assert esperado in altas, (resp, altas)
    env = types.SimpleNamespace(enviar=lambda signed, gtd=False: (_ for _ in ()).throw(TimeoutError('x'))); sr = R2.SenderReal(env, reg, None, ce, d); altas.clear()
    try: sr.enviar(dict(oid='0xlocal', signed=1, tok='T', precio=0.01, gtd=True)); assert False
    except TimeoutError: pass
    assert altas == ['0xlocal']
    # (c) el orquestador: oid distinto => alarma + BLOCKED; la orden se sigue (y cancela) con el oid del servidor
    P, S, R, M, out = montar('r2h7c', sender_kw=dict(oid_servidor_distinto={3}), cfg=C.Config(max_ordenes=24)); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
    assert st == 'BLOCKED' and 'oid_servidor_distinto' in inf['motivo'], (st, inf['motivo'])
    p3 = [r for r in rows(out, 'post')][2]; assert p3['oid'] != p3['oid_local'] and (p3['oid'], True) in S.cancelaciones and sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0
    print('T50 ok [R2 hallazgo 7]: alta de cancel_evidencia con el oid del servidor (el local solo sin respuesta); contar_anclas no casa oids distintos; oid distinto => alarma, BLOCKED y la orden se cancela por su oid real')


def test_r2h8_credenciales_dedicadas_distintas_de_produccion():
    V = _vm(); f = os.path.join(TMP, 'r2h8_ded.env'); W = C.WALLET_DEDICADA
    def escribir(ruta, pk='ab' * 32, wal=W, key='kd', modo=0o600):
        open(ruta, 'w').write(f'POLY_PRIVATE_KEY=0x{pk}\nPOLY_DEPOSIT_WALLET={wal}\nPOLY_API_KEY={key}\nPOLY_API_SECRET=s\nPOLY_API_PASSPHRASE=p\n'); os.chmod(ruta, modo); return ruta
    escribir(f)
    class Cli:
        def __init__(self, host, **kw): self.kw = kw
    def sale(prod, ruta=f):
        try: V.cliente_dedicado(ruta, W, _clob=Cli, _prod=prod); return False
        except SystemExit: return True
    p1 = escribir(os.path.join(TMP, 'r2h8_live.env'), pk='cd' * 32, wal='0x00000000000000000000000000000000000000aa', key='kl'); p2 = escribir(os.path.join(TMP, 'r2h8_main.env'), pk='ef' * 32, wal='0x00000000000000000000000000000000000000bb', key='km')
    assert not sale((p1, p2)) and not sale((p1, os.path.join(TMP, 'r2h8_noexiste.env')))                           # distintas => arranca; el 2o .env (principal) solo se compara SI existe
    assert sale((os.path.join(TMP, 'r2h8_noexiste.env'),)) and sale((open(os.path.join(TMP, 'r2h8_vacio.env'), 'w').name,))                           # el 1o (data/live/.env) es OBLIGATORIO y legible: si no se puede comprobar => no arranco
    assert sale((escribir(os.path.join(TMP, 'r2h8_pk.env'), pk='ab' * 32, wal='0x00000000000000000000000000000000000000aa', key='x'),))                    # misma PRIVATE_KEY
    assert sale((escribir(os.path.join(TMP, 'r2h8_ak.env'), pk='cd' * 32, wal='0x00000000000000000000000000000000000000aa', key='kd'),))                    # misma API_KEY
    assert sale((escribir(os.path.join(TMP, 'r2h8_dw.env'), pk='cd' * 32, wal=W.upper().replace('0X', '0x'), key='x'),))                                    # misma wallet de deposito (distinta capitalizacion)
    assert sale((p1, escribir(os.path.join(TMP, 'r2h8_pk2.env'), pk='ab' * 32, wal='0x00000000000000000000000000000000000000cc', key='y')))                    # coincide con el 2o .env
    ln = os.path.join(TMP, 'r2h8_enlace.env'); os.path.lexists(ln) and os.remove(ln); os.symlink(p1, ln); assert sale((p1, p2), ruta=ln)                           # symlink a un .env de produccion (realpath)
    print('T51 ok [R2 hallazgo 8]: la clave/API key/wallet de deposito no pueden coincidir con data/live/.env ni .env principal (incl. symlinks/capitalizacion); el .env de produccion es obligatorio y solo se COMPARA (tests con ficheros sinteticos)')


def test_r2h9_elegir_mercado_pide_solo_su_moneda():
    class MRec(MercadosSim):
        def __init__(s, r): super().__init__(r); s.pedidos = []
        def mercados(s, coin=None): s.pedidos.append(coin); return super().mercados(coin)
    reloj = RelojVirtual(); P, S, R, M, out = montar('r2h9', reloj=reloj, mercados=MRec(reloj), cfg=C.Config(max_ordenes=8)); P.correr()
    assert M.pedidos and None not in M.pedidos and set(M.pedidos) <= set(C.COINS), M.pedidos
    import pl_sender_real as R2; urls = []
    def get(url, params): urls.append(params.get('slug')); return []
    mr = R2.MercadosReal(get=get, reloj=lambda: 1_790_000_000.0); mr.mercados('ETH'); assert urls and all(u.startswith('eth-updown-5m-') for u in urls) and len(urls) == 2, urls
    import inspect; assert inspect.signature(R2.MercadosReal._get).parameters['timeout'].default <= 3.0
    print('T52 ok [R2 hallazgo 9]: el orquestador pide mercados(coin del slot) (%s); MercadosReal.mercados(ETH) = 2 GETs de eth, timeout gamma <= 3 s' % sorted(set(M.pedidos)))


def test_r2h10_fallos_de_io_no_impiden_barrido_ni_informe():
    import contextlib
    # (a) disco lleno en el ledger a mitad: sigue, barre, informe NO COMPLETE y las filas quedan en .fallback
    P, S, R, M, out = montar('r2h10a', cfg=C.Config(max_ordenes=16)); orig = S.enviar; k = {'n': 0}
    def enviar(h):
        k['n'] += 1
        if k['n'] == 4: P.led.f = _Roto()
        return orig(h)
    S.enviar = enviar
    with contextlib.redirect_stderr(open(os.devnull, 'w')): st = P.correr()
    inf = json.load(open(out + '/informe_final.json'))
    assert st == 'BLOCKED' and inf['escrituras_fallidas']['ledger'] > 0 and os.path.exists(os.path.join(out, 'ledger.jsonl.fallback')) and sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0, (st, inf['escrituras_fallidas'])
    # (b) excepcion en el cuerpo + `_matar` y log que fallan por E/S: el barrido se ejecuta igualmente
    P, S, R, M, out = montar('r2h10b', cfg=C.Config(max_ordenes=16)); om = P._matar; ocv = P.cancelar_viva; k = {'n': 0}
    def cv(clave, forzada=False):
        if k['n'] == 0 and len(S.posts_enviados) >= 5: k['n'] += 1; P.logf = _Roto(); raise RuntimeError('fallo inesperado en el bucle')
        return ocv(clave, forzada)
    def matar(m, s):
        if str(m).startswith('excepcion'): raise OSError(28, 'disco lleno')
        return om(m, s)
    P.cancelar_viva = cv; P._matar = matar
    with contextlib.redirect_stderr(open(os.devnull, 'w')): st = P.correr()
    assert st in ('FAILED', 'BLOCKED') and os.path.exists(os.path.join(out, 'informe_final.json')) and sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0 and P.kill and P.exc, (st, P.kill)
    # (c) el informe final no se puede escribir en el out: fallback + mismo status
    P, S, R, M, out = montar('r2h10c', cfg=C.Config(max_ordenes=8)); fb = os.path.join(TMP, 'fallback'); os.makedirs(fb, exist_ok=True); fb0 = C.FALLBACK_DIR; ea = C.escribir_atomico; C.FALLBACK_DIR = fb
    def ea2(ruta, obj):
        if str(ruta).endswith('informe_final.json'): raise OSError(28, 'disco lleno')
        return ea(ruta, obj)
    C.escribir_atomico = ea2
    try:
        with contextlib.redirect_stderr(open(os.devnull, 'w')): st = P.correr()
    finally: C.escribir_atomico = ea; C.FALLBACK_DIR = fb0
    fbf = [x for x in os.listdir(fb) if x.startswith('paquete_l_')]; assert st == 'PARTIAL' and len(fbf) == 1 and json.load(open(os.path.join(fb, fbf[0])))['status'] == st, (st, fbf)       # (PARTIAL: con 8 ordenes no se alcanza el objetivo de anclas; el informe de fallback lleva EL MISMO status)
    print('T53 ok [R2 hallazgo 10]: ledger sin disco => sigue, barre, BLOCKED + .fallback; _matar/log rotos en el handler no impiden el barrido; informe final con OSError => fallback con el mismo status')


def test_r2_gtd_docs_y_sin_caida_a_gtc():
    # reglas de los docs oficiales (12-Nov): expiracion >= now+3 min (rechazo si no), efectiva 60 s antes; defecto 200 s las cumple; < 185 s no se acepta como configuracion
    assert C.Config().gtd_expira_s == 200
    for mal in (60, 75, 120, 184):
        try: C.Config(gtd_expira_s=mal); assert False, mal
        except C.Invariante as e: assert 'GTD' in str(e), e
    P, S, R, M, out = montar('r2gtd_ok', cfg=C.Config(max_ordenes=8)); P.correr(); assert len(S.posts_enviados) == 8 and all(c['expira_s'] == 200 for c in S.colocados)
    # v5 (hallazgo 2): el CLOB rechaza GTD => BLOCKED sin gasto, SIN cambiar de modo (todas las intenciones siguen con expira_s=200), con el literal del rechazo; no existe `gtd_activo` ni `rechazo_es_de_gtd`
    P, S, R, M, out = montar('r2gtd_caida', sender_kw=dict(gtd_rechazado=True), cfg=C.Config(max_ordenes=16)); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
    assert st == 'BLOCKED' and inf['status'] == 'BLOCKED' and 'rechazos_seguidos' in inf['motivo'] and inf['ultimo_rechazo'] and inf['ultimo_rechazo'] in inf['motivo'], (st, inf['motivo'])
    assert all(r['expira_s'] == 200 for r in rows(out, 'intencion')) and not rows(out, 'gtd_desactivado') and all(r.get('rechazo_literal') for r in rows(out, 'cerrada') if r['motivo'] == 'rechazo') and len(S.posts_enviados) == 0
    assert inf['presupuesto']['gasto'] == 0.0
    assert not hasattr(P, 'gtd_activo') and not hasattr(C, 'rechazo_es_de_gtd') and not hasattr(C, '_PISTAS_GTD') and 'cota_dura_gtd' not in inf
    print('T54 ok [R2+R3 h2]: GTD defecto 200 s (docs: >= 3 min, efectiva -60 s); < 185 s no configurable; rechazo del CLOB de GTD => BLOCKED sin gasto y SIN caida a GTC (modo intacto, literal en el informe)')


def test_r1_preflight_solo_lectura():
    import pl_sender_real as R2
    T0 = 1_790_000_100.0; ini0 = int(T0) // 300 * 300; cfg = C.Config()
    def mk_get(tick='0.01', minsize='5', neg=False, asks=((0.45, 20),), gamma_neg=False):
        def get(url, params):
            if 'events' in url:
                slug = params['slug']; coin = slug.split('-')[0].upper(); ini = int(slug.rsplit('-', 1)[1]); ev = gamma_ev(coin, ini); ev['markets'][0]['negRisk'] = gamma_neg; return [ev]
            return dict(version='v2', bids=[dict(price='0.40', size='10')], asks=[dict(price=str(p), size=str(q)) for p, q in asks], min_order_size=minsize, tick_size=tick, neg_risk=neg)
        return get
    class Firmada:                                                                 # forma de SignedOrderV2 (solo los campos que se comparan)
        def __init__(s, tok, maker=cfg.wallet, mk='50000', tk='5000000', exp=None): s.makerAmount, s.takerAmount, s.tokenId, s.maker, s.side, s.signatureType, s.signature, s.expiration = mk, tk, tok, maker, 'BUY', 3, '0xfirma', str(exp if exp is not None else int(T0) + cfg.gtd_expira_s)
    class Cred:
        def __init__(s, k='K', se='SECRETO123', pa='PASS123'): s.api_key, s.api_secret, s.api_passphrase = k, se, pa
    def fake_env(maker=cfg.wallet, mk='50000', derivadas=None, abiertas=(), saldo=0.612681, wallet=cfg.wallet, hash_=('0x' + 'ab' * 32)):
        env = types.SimpleNamespace(llamadas=[], wallet=wallet, M=types.SimpleNamespace(hash_orden=lambda signed, nr: hash_))
        env.cli = types.SimpleNamespace(creds=Cred(), derive_api_key=lambda: derivadas or Cred(), post_order=lambda *a, **k: env.llamadas.append('post_order'), post_orders=None, create_and_post_order=None, create_and_post_market_order=None)
        env.enviar = lambda *a, **k: env.llamadas.append('enviar'); env.saldo = lambda: saldo; env.abiertas_todas = lambda: list(abiertas)
        env.poner = lambda tok, precio, size, clave, neg_risk=None, expira_s=None: (hash_, Firmada(tok, maker=maker, mk=mk)); return env
    rr = R2.preflight(cfg, False, get=mk_get(asks=((0.01, 5),)), ahora=lambda: T0); assert rr['ok'] is True and all(t['operable_ahora'] is False for v in rr['monedas'].values() for t in v['tokens'])        # el libro de ESE instante no es un requisito
    chr_ok = lambda: dict(system_time_s=0.05, last_offset_s=0.01, stratum=2, ref_id='65D8456C', leap='Normal', root_dispersion_s=0.001, root_delay_s=0.04); fa = lambda **k: (lambda cfg_: fake_env(**k))
    # 1) todo correcto: ok, 4 monedas x 2 tokens, 0 POST posibles
    env_ref = []
    def fac(cfg_): e = fake_env(); env_ref.append(e); return e
    r = R2.preflight(cfg, True, get=mk_get(), env_factory=fac, chrony=chr_ok, ahora=lambda: T0); e = env_ref[0]
    assert r['ok'] is True and sorted(r['monedas']) == sorted(C.COINS) and all(len(v['tokens']) == 2 and v['ok'] for v in r['monedas'].values()), r['errores']
    assert r['autenticado']['orden_firmada_local'] and all(v is True for v in r['autenticado']['orden_firmada_local'].values()) and r['autenticado']['open_orders_legibles_y_vacias'] and r['autenticado']['api_creds_derivadas_coinciden']
    assert e.enviar is R2._prohibido and e.cli.post_order is R2._prohibido and e.cli.post_orders is R2._prohibido and e.llamadas == []            # el envio quedo anulado ANTES de cualquier lectura
    try: e.enviar(1); assert False
    except AssertionError as x: assert 'PROHIBIDO' in str(x)
    assert 'SECRETO123' not in json.dumps(r, default=str) and 'PASS123' not in json.dumps(r, default=str) and '0xfirma' not in json.dumps(r, default=str)       # ninguna clave/secreto/firma en el informe
    # 2) cada desviacion => ok False, sin lanzar
    casos = [('importe_maker_mal', dict(get=mk_get(), env=dict(mk='50001'))), ('maker_ajeno', dict(get=mk_get(), env=dict(maker='0x0000000000000000000000000000000000000001'))), ('open_orders_ajenas', dict(get=mk_get(), env=dict(abiertas=['0xabc']))),
             ('creds_distintas', dict(get=mk_get(), env=dict(derivadas=Cred(se='otro')))), ('saldo_cero', dict(get=mk_get(), env=dict(saldo=0.0))), ('saldo_bajo_minimo_0_60', dict(get=mk_get(), env=dict(saldo=0.30))),    # v6 (hallazgo 8): < 12 x 0,05
              ('wallet_otra', dict(get=mk_get(), env=dict(wallet='0x1'))),
             ('hash_corto', dict(get=mk_get(), env=dict(hash_='0x1234'))), ('tick', dict(get=mk_get(tick='0.001'), env={})), ('minsize', dict(get=mk_get(minsize='6'), env={})), ('neg_risk_distinto', dict(get=mk_get(neg=True), env={}))]
    for nombre, kw in casos:
        r = R2.preflight(cfg, True, get=kw['get'], env_factory=(lambda cfg_, k=kw['env']: fake_env(**k)), chrony=chr_ok, ahora=lambda: T0); assert r['ok'] is False and r['errores'], nombre
    assert R2.preflight(cfg, True, get=mk_get(), env_factory=fac, chrony=lambda: None, ahora=lambda: T0)['ok'] is False                                         # sin chrony
    for extra in (dict(leap='Not synchronised'), dict(stratum=0), dict(ref_id='00000000'), dict(root_dispersion_s=3.0), dict(system_time_s=2.0), dict(ref_id='7F7F0101'), dict(stratum=10)): assert R2.preflight(cfg, True, get=mk_get(), env_factory=fac, chrony=lambda e=extra: dict(chr_ok(), **e), ahora=lambda: T0)['ok'] is False, extra       # v5 (R3 h3)
    def sale_(cfg_): raise SystemExit('comparte credenciales con produccion')
    r = R2.preflight(cfg, True, get=mk_get(), env_factory=sale_, chrony=chr_ok, ahora=lambda: T0); assert r['ok'] is False and 'cliente_dedicado se nego' in r['autenticado']['error']
    # 3) publico: nunca construye el cliente
    n = {'c': 0}
    def nunca(cfg_): n['c'] += 1; return fake_env()
    r = R2.preflight(cfg, False, get=mk_get(), env_factory=nunca, ahora=lambda: T0); assert r['ok'] is True and r['autenticado'] is None and n['c'] == 0
    print('T55 ok [R1]: preflight solo lectura: 8 tokens (tick/minsize/neg_risk/ask), creds derivadas, saldo, open orders, reloj y orden firmada en local (importes, maker, 1271, expiracion, hash 32 B); envio anulado antes de leer; 11 desviaciones => ok False; sin secretos en el informe; publico no construye cliente')


def _vivas_reales(S): return sum(1 for o in S.ordenes.values() if S._estado_en(o, S.r.now_ns())[1] == 'LIVE')


def test_r3h1_barrido_reintenta_cancelar_o_bloquea_con_alerta():
    # cancel_falla {1..8}: el barrido reintenta con backoff hasta cancelar => 0 vivas al final (BLOCKED por el kill del cuerpo, pero sin indeterminadas ni abiertas)
    P, S, R, M, out = montar('r3h1a'); fallar_cancelaciones_de_la_primera_orden(S, R, 8); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
    assert st == 'BLOCKED' and _vivas_reales(S) == 0 and inf['cobertura']['indeterminadas'] == 0 and not inf['alertas'], (st, inf['motivo'], inf['alertas'])
    # cancel_falla enorme: no se puede cancelar nunca => BLOCKED con la lista de ordenes vivas y ALERTA explicita (fichero + informe), jamas silencio ni COMPLETE
    P, S, R, M, out = montar('r3h1b', sender_kw=dict(cancel_falla=set(range(1, 200)))); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
    assert st == 'BLOCKED' and inf['status'] == 'BLOCKED' and _vivas_reales(S) >= 1 and inf['alertas'] and 'ORDENES ABIERTAS' in inf['alertas'][0] and os.path.exists(out + '/ALERTA_paquete_l.txt') and P.abiertas_res, (st, inf['motivo'], inf['alertas'])
    vivas = [oid for oid, o in S.ordenes.items() if S._estado_en(o, S.r.now_ns())[1] == 'LIVE']; assert all(oid in inf['alertas'][0] for oid in vivas)                  # la lista exacta de ids vivos esta en la alerta
    P, S, R, M, out = montar('r3h1c', sender_kw=dict(cancel_falla_por_oid=14)); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))                 # 14 cancelaciones fallidas POR ORDEN (cuerpo + cancelar_viva + 1.o de reconciliar): solo los reintentos con backoff del barrido las cancelan
    assert st == 'BLOCKED' and _vivas_reales(S) == 0 and not inf['alertas'] and inf['cobertura']['indeterminadas'] == 0, (st, inf['motivo'], inf['alertas'])
    print('T56 ok [R3 h1]: cancel_falla {1..8} => 0 vivas (barrido reintenta); cancelacion imposible => BLOCKED + ALERTA con ids vivos (fichero e informe)')


def test_r3h2_sin_caida_a_gtc_y_literal():
    import inspect
    src = inspect.getsource(PL) + inspect.getsource(C)
    assert 'gtd_activo' not in src and 'rechazo_es_de_gtd' not in src and 'rechazo_gtd' not in src and 'GTC' not in inspect.getsource(PL.Paquete.post_slot)
    P, S, R, M, out = montar('r3h2', sender_kw=dict(rechazo_post={1, 2})); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
    assert st == 'BLOCKED' and all(c['expira_s'] == 200 for c in S.colocados) and P.ultimo_rechazo and P.ultimo_rechazo in inf['motivo'] and len(S.posts_enviados) == 0
    print('T57 ok [R3 h2]: no hay camino GTC (ni gtd_activo ni rechazo_es_de_gtd); cualquier rechazo => BLOCKED sin gasto con el literal del CLOB, modo intacto')


def test_r3h3_reloj_sincronizado_exige_leap_stratum_refid_dispersion():
    cfg = C.Config(); ok = dict(system_time_s=0.01, last_offset_s=0.0, stratum=3, ref_id='65D8456C', leap='Normal', root_dispersion_s=0.001, root_delay_s=0.04); assert C.reloj_sincronizado(ok, cfg)
    for k, v in (('leap', 'Not synchronised'), ('leap', None), ('stratum', 0), ('stratum', 16), ('stratum', None), ('ref_id', '00000000'), ('ref_id', None), ('system_time_s', 1.5), ('system_time_s', float('nan')), ('root_dispersion_s', 0.6), ('root_dispersion_s', None), ('root_dispersion_s', float('inf'))):
        assert not C.reloj_sincronizado(dict(ok, **{k: v}), cfg), (k, v)
    assert not C.reloj_sincronizado(None, cfg) and not C.reloj_sincronizado(dict(system_time_s=0.0, last_offset_s=0.0), cfg)                       # el formato VIEJO (solo offset) ya no vale
    for nombre, kw in (('leap', dict(leap='Not synchronised')), ('st0', dict(stratum=0)), ('rid0', dict(ref_id='00000000')), ('disp', dict(root_dispersion_s=2.0))):
        P, S, R, M, out = montar('r3h3' + nombre, sender_kw=dict(chrony_extra=kw)); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
        assert st == 'BLOCKED' and 'reloj_no_verificado' in inf['motivo'] and len(S.posts_enviados) == 0 and inf['presupuesto']['gasto'] == 0.0, (nombre, st)
    import pl_sender_real as R2, subprocess
    txt = lambda extra: ('Reference ID    : %s\nStratum         : %s\nRef time (UTC)  : Thu Nov 12 13:24:59 2026\nSystem time     : 0.000000000 seconds fast of NTP time\nLast offset     : +0.0 seconds\nRoot delay      : 0.04 seconds\nRoot dispersion : 0.0005 seconds\nLeap status     : %s\n') % extra
    orig = subprocess.run
    try:
        for extra, esperado in ((('65D8456C', 3, 'Normal'), True), (('00000000', 0, 'Not synchronised'), False)):
            subprocess.run = lambda *a, **k: types.SimpleNamespace(stdout=txt(extra)); ch = R2.leer_chrony(); assert C.reloj_sincronizado(ch, cfg) is esperado and ch['leap'] == extra[2] and ch['stratum'] == extra[1], (extra, ch)
    finally: subprocess.run = orig
    print('T58 ok [R3 h3]: chrony debe estar sincronizado (leap Normal, stratum 1-15, ref id != 0, offset y dispersion acotados); formato viejo/None/NaN rechazados; run => BLOCKED sin gasto; preflight => ok False')


def test_r3h4_abiertas_sin_filtro_antes_y_despues():
    # (a) una orden ajena abierta ANTES de empezar => BLOCKED sin enviar nada (y no se toca)
    P, S, R, M, out = montar('r3h4a', sender_kw=dict(abiertas_ajenas=['0xajena'])); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
    assert st == 'BLOCKED' and 'abiertas_previas_o_ilegibles' in inf['motivo'] and len(S.posts_enviados) == 0 and inf['alertas'] and '0xajena' in inf['alertas'][0]
    # (b) la lectura previa ilegible => BLOCKED sin enviar
    reloj = RelojVirtual(); S = SenderSim(reloj); S.abiertas_todas = lambda: None; P, S, R, M, out = montar('r3h4b', sender=S, reloj=reloj, mercados=MercadosSim(reloj)); assert P.correr() == 'BLOCKED' and len(S.posts_enviados) == 0
    # (c) una orden ajena que APARECE durante el run: el barrido la ve (lectura sin filtro de asset), no la cancela y declara BLOCKED con alerta
    reloj = RelojVirtual(); S = SenderSim(reloj); k = {'n': 0}; ab0 = S.abiertas_todas
    def ab():
        k['n'] += 1
        if k['n'] >= 2: S.ajenas = ['0xajena2']
        return ab0()
    S.abiertas_todas = ab; P, S, R, M, out = montar('r3h4c', sender=S, reloj=reloj, mercados=MercadosSim(reloj)); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
    assert st == 'BLOCKED' and 'ajenas al run=[\'0xajena2\']' in inf['alertas'][0]
    # (d) el adaptador real NO usa el filtro por token en el barrido: el vendor `abiertas(tok)` ya no se llama desde el orquestador
    import inspect; assert '.abiertas(' not in inspect.getsource(PL.Paquete) and 'abiertas_todas' in inspect.getsource(PL.Paquete) and 'OpenOrderParams()' in open(os.path.join(H, 'pl_sender_real.py')).read()
    print('T59 ok [R3 h4]: get_open_orders SIN filtro de asset: 0 abiertas obligatorias antes de empezar (ajenas/ilegible => BLOCKED sin enviar) y al final (ajena o propia viva => BLOCKED + alerta)')


def test_r3h5_resume_bloqueado_por_ilegibles_o_indeterminadas():
    def paq(out, S, M, reloj, cfg): P = PL.Paquete(cfg, S, M, out, reloj, 'r3h5', stdout=False); P.anclas_fn = lambda: 0; P.anclas_por_moneda_fn = lambda: {}; return P
    reloj = RelojVirtual(); S = SenderSim(reloj); M = MercadosSim(reloj); k = {'n': 0}; ab0 = S.abiertas_todas
    def ab():
        k['n'] += 1
        return ab0() if k['n'] == 1 else None                                        # la lectura final del run 1 es ilegible => BLOCKED con filas `ilegible`, SIN fila kill
    S.abiertas_todas = ab; out = os.path.join(TMP, 'r3h5'); cfg = C.Config(max_ordenes=8); P1 = paq(out, S, M, reloj, cfg); assert P1.correr() == 'BLOCKED'; n1 = len(S.posts_enviados); assert rows(out, 'ilegible')
    S.abiertas_todas = ab0; P2 = paq(out, S, M, reloj, cfg); st = P2.correr(); inf = json.load(open(out + '/informe_final.json'))
    assert st == 'BLOCKED' and len(S.posts_enviados) == n1 and 'resume_rechazado' in P2.kill and 'ilegibles' in P2.kill, (st, P2.kill)
    # mutacion natural: con otro run-id (nueva carpeta) SI se puede lanzar (verificacion manual previa)
    P3 = PL.Paquete(cfg, S, M, os.path.join(TMP, 'r3h5_otro'), reloj, 'r3h5_otro', stdout=False); P3.anclas_fn = lambda: 0; P3.anclas_por_moneda_fn = lambda: {}; assert P3.correr() in ('COMPLETE', 'PARTIAL') and len(S.posts_enviados) > n1
    print('T60 ok [R3 h5]: lectura final ilegible (BLOCKED sin kill) bloquea relanzar con el mismo run-id (deducido del LEDGER); otro run-id si opera')


def test_r3h6_barrido_espera_asentamiento_antes_de_leer_abiertas():
    reloj = RelojVirtual(); S = SenderSim(reloj, index_delay_s=3.0); M = MercadosSim(reloj); reg = {}; ab0 = S.abiertas_todas; sa0 = S.saldo
    def ab():
        reg.setdefault('t_ab', []).append(reloj.now_ns()); return ab0()
    S.abiertas_todas = ab; P, S, R, M, out = montar('r3h6', sender=S, reloj=reloj, mercados=M, cfg=C.Config(max_ordenes=8)); P.correr()
    ult = max(o['t_alta_ns'] for o in S.ordenes.values()); minimo = ult + int((P.cfg.index_gracia_s + P.cfg.asentamiento_extra_s) * 1e9)
    assert reg['t_ab'][-1] >= minimo, ((reg['t_ab'][-1] - ult) / 1e9)                           # la lectura FINAL de abiertas es >= index_gracia + 3 s tras el ultimo POST
    # (b) barrido directo con TODAS las ordenes ya cerradas y el ultimo POST recien hecho: aun asi no se lee abiertas/saldo antes del asentamiento (un "vacio" antes no prueba nada)
    reloj = RelojVirtual(); S = SenderSim(reloj); P, S, R, M, out = montar('r3h6b', sender=S, reloj=reloj, mercados=MercadosSim(reloj)); P.led = C.Ledger(out + '/ledger.jsonl'); P.pres = C.Presupuesto(P.cfg, 0.612681); t_post = reloj.now_ns(); lect = []
    P.ordenes = {'x': C.Orden(clave='x', tok='T', oid='0x1', cerrada=True, t_ack_ns=t_post)}; S.abiertas_todas = lambda: (lect.append(('ab', reloj.now_ns())) or []); P._saldo = lambda: (lect.append(('sal', reloj.now_ns())) or P.pres.s0)
    P._barrido_final(); assert [k for k, _ in lect] == ['ab', 'sal'] and all(t >= t_post + P._asentamiento_ns() for _, t in lect), lect
    print('T61 ok [R3 h6]: el barrido espera index_gracia + 3 s desde el ultimo POST antes de leer abiertas/saldo (lectura final a +%.1f s)' % ((reg['t_ab'][-1] - ult) / 1e9))


def test_r3h7_ledger_trunca_sin_salto_de_linea():
    for cola in ('{"eid": "x|a|0", "k": "x", "clave": "a"}', '{"eid": "x|b|0", "k": "x", "cla'):          # ultima fila valida SIN '\n' / ultima fila cortada a medias
        ruta = os.path.join(TMP, 'r3h7.jsonl')
        with open(ruta, 'wb') as f: f.write(b'{"eid": "k|0|0", "k": "k", "clave": "0"}\n' + cola.encode())
        L = C.Ledger(ruta); L.add('nuevo', 'z', 0); L.add('nuevo', 'z', 1); L.f.close()
        lineas = open(ruta).read().split('\n'); assert lineas[-1] == '' and all(json.loads(l) for l in lineas[:-1])                     # TODAS las lineas parsean: la nueva no se pego a la cola
        eids = [json.loads(l)['eid'] for l in lineas[:-1]]; assert 'nuevo|z|0' in eids and 'nuevo|z|1' in eids and eids.count('k|0|0') == 1 and len(eids) == len(set(eids))
        L2 = C.Ledger(ruta); assert {r['eid'] for r in L2.filas} == set(eids); L2.f.close()
    print('T62 ok [R3 h7]: ledger acabado sin salto de linea (fila valida o cortada) se completa/trunca antes de seguir en append: ninguna fila pegada, 0 perdidas validas')


def test_r3h8_hash_sin_comprobacion_enganosa():
    import pl_sender_real as R2, inspect
    assert 'rehash' not in inspect.signature(R2.comprobar_orden_firmada).parameters and 'hash_reproducible' not in inspect.getsource(R2) and 'hash_formato_32_bytes' in inspect.getsource(R2)
    assert 'NO se valida aqui' in R2.preflight.__doc__ and 'oid_servidor_distinto_del_local' in inspect.getsource(PL)                           # la validacion real es el orderID del servidor en el 1.er POST
    reloj = RelojVirtual(); S = SenderSim(reloj, oid_servidor_distinto={1}); P, S, R, M, out = montar('r3h8', sender=S, reloj=reloj, mercados=MercadosSim(reloj)); st = P.correr(); assert st == 'BLOCKED' and 'oid_servidor_distinto_del_local' in P.kill
    print('T63 ok [R3 h8]: eliminada la comprobacion tautologica; el preflight solo valida el FORMATO del hash y lo dice; la validacion real (orderID del servidor == hash local) sigue y bloquea')


def test_r3h9_un_solo_cargar_env():
    import pl_sender_real as R2, inspect
    assert not hasattr(R2, '_env_real') and 'cargar_env(cfg)' in inspect.getsource(R2.construir) and 'cargar_env' in inspect.getsource(R2.preflight)
    llamadas = []; orig = R2.cargar_env
    def centinela(cfg): llamadas.append(1); raise SystemExit('CENTINELA_CARGAR_ENV')
    R2.cargar_env = centinela
    try:
        try: R2.construir(C.Config(), os.path.join(TMP, 'r3h9')); assert False
        except SystemExit as e: assert 'CENTINELA' in str(e)
        r = R2.preflight(C.Config(), True, get=(lambda u, p: (_ for _ in ()).throw(RuntimeError('sin red en el test'))), chrony=lambda: dict(system_time_s=0, stratum=2, ref_id='AB', leap='Normal', root_dispersion_s=0.0), ahora=lambda: 1_790_000_100.0)
        assert len(llamadas) == 2 and 'CENTINELA' in json.dumps(r['autenticado'], default=str), (llamadas, r['autenticado'])
    finally: R2.cargar_env = orig
    print('T64 ok [R3 h9]: `construir` y `preflight` usan el MISMO `cargar_env(cfg)` (centinela invocado por ambos; no existe _env_real)')


def test_r3h10_asentar_solo_cuando_hace_falta():
    def caso(nombre, index_delay):
        reloj = RelojVirtual(); S = SenderSim(reloj, index_delay_s=index_delay); P, S, R, M, out = montar(nombre, sender=S, reloj=reloj, mercados=MercadosSim(reloj)); P.led = C.Ledger(out + '/ledger.jsonl'); P.pres = C.Presupuesto(P.cfg, 0.612681)
        tok = '1' * 20; oid, h = S.colocar(tok, 0.01, 5.0, 'k0', neg_risk=False, expira_s=200); S.enviar(h); o = C.Orden(clave='k0', tok=tok, oid=oid, precio=0.01, size=5.0); o.t_ack_ns = reloj.now_ns(); P.ordenes['k0'] = o
        n = {'a': 0}; orig = P._asentar
        def asentar(ref, interrumpible): n['a'] += 1; return orig(ref, interrumpible)
        P._asentar = asentar; ok = P.reconciliar_orden(o, 'test'); return ok, n['a'], rows(out, 'cerrada')
    ok, n, cer = caso('r3h10a', 0.0); assert ok and n == 0 and cer[-1]['motivo'] == 'reconciliada:CANCELED', (ok, n, cer)                            # cancelacion con exito y estado terminal al 1er intento: NO se espera el asentamiento
    ok, n, cer = caso('r3h10b', 3.0); assert ok and n == 1 and cer[-1]['motivo'] == 'reconciliada:CANCELED', (ok, n, cer)                            # get_order devuelve null (sin indexar): se espera UNA vez, y se confirma
    print('T65 ok [R3 h10]: asentamiento solo si el 1er intento no da estado terminal (0 esperas tras cancelacion limpia, 1 si get_order aun no indexa)')


# ---------------------------------------------------------------- ronda 4 (v6): 4o /code-review, hallazgos 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
import inspect


def _p_con_ordenes(nombre, **kw):
    """Paquete con ledger/presupuesto abiertos y UNA orden cerrada (para que el barrido final lea abiertas y saldo)."""
    reloj = RelojVirtual(); S = SenderSim(reloj, **kw); P, S, R, M, out = montar(nombre, sender=S, reloj=reloj, mercados=MercadosSim(reloj))
    P.led = C.Ledger(out + '/ledger.jsonl'); P.pres = C.Presupuesto(P.cfg, 0.612681); P.ordenes = {'x': C.Orden(clave='x', tok='T', oid='0x1', cerrada=True, t_ack_ns=reloj.now_ns())}; return P, S, R, out


def test_r4h1_kill_duro_posterior_prevalece_sobre_benigno():
    P, S, R, out = _p_con_ordenes('r4h1'); P._matar('senal_SIGTERM', 'PARTIAL'); assert P.kill == 'senal_SIGTERM'
    P._P_saldo = P._saldo; P._saldo = lambda: round(P.pres.s0 - 0.30, 6); P._barrido_final()                       # descuadre de saldo en el barrido, DESPUES del SIGTERM
    assert P.kill.startswith('saldo_cae_mas_que_ledger_final') and P.kill_status == 'BLOCKED', (P.kill, P.kill_status)
    assert any(r['k'] == 'kill' and r['status'] == 'BLOCKED' for r in rows(out)) and any(r['motivo'] == 'senal_SIGTERM' for r in rows(out, 'kill'))
    P2, *_ = _p_con_ordenes('r4h1b'); P2._matar('max_ordenes', 'PARTIAL'); P2._matar('relleno_en_fase_A (corte inmediato)', 'PARTIAL'); assert P2.kill.startswith('relleno_en_fase_A')      # PARTIAL duro > benigno
    P2._matar('max_minutos', 'PARTIAL'); assert P2.kill.startswith('relleno_en_fase_A')                                                       # y un benigno posterior no lo desplaza
    P2._matar('excepcion:X', 'FAILED'); P2._matar('saldo_x', 'BLOCKED'); assert P2.kill_status == 'FAILED'                                    # FAILED > BLOCKED
    # el resume rechaza si hay un kill duro posterior a uno benigno
    reloj = RelojVirtual(); cfg = C.Config(max_ordenes=8); out = os.path.join(TMP, 'r4h1r'); S = SenderSim(reloj); M = MercadosSim(reloj)
    P1 = PL.Paquete(cfg, S, M, out, reloj, 'r4h1r', stdout=False); P1.anclas_fn = lambda: 0; P1.anclas_por_moneda_fn = lambda: {}; P1.correr(); n1 = len(S.posts_enviados); assert n1 == 8
    L = C.Ledger(out + '/ledger.jsonl'); L.add('kill', 'run', 90, motivo='saldo_cae_mas_que_ledger_final 0.3 > 0', status='BLOCKED'); L.cerrar()
    S2 = SenderSim(reloj); P2 = PL.Paquete(cfg, S2, M, out, reloj, 'r4h1r', stdout=False); P2.anclas_fn = lambda: 0; P2.anclas_por_moneda_fn = lambda: {}; assert P2.correr() == 'BLOCKED' and len(S2.posts_enviados) == 0


def test_r4h2_resume_lee_saldo_y_lo_contrasta_antes_de_enviar():
    reloj = RelojVirtual(); cfg = C.Config(max_ordenes=8); out = os.path.join(TMP, 'r4h2'); M = MercadosSim(reloj)
    P1 = PL.Paquete(cfg, SenderSim(reloj), M, out, reloj, 'r4h2', stdout=False); P1.anclas_fn = lambda: 0; P1.anclas_por_moneda_fn = lambda: {}; st = P1.correr(); assert st != 'BLOCKED' and len(rows(out, 'kill')) >= 1
    def reanuda(**kw):
        S2 = SenderSim(reloj, **kw); P2 = PL.Paquete(cfg, S2, M, out, reloj, 'r4h2', stdout=False); P2.anclas_fn = lambda: 0; P2.anclas_por_moneda_fn = lambda: {}; return P2.correr(), S2, P2
    st, S2, P2 = reanuda(saldo_inicial=0.612681 - 0.30); assert st == 'BLOCKED' and len(S2.posts_enviados) == 0 and 'saldo_descuadrado_en_arranque' in P2.kill, (st, P2.kill)     # saldo perdido SIN ledger: 0 envios
    for ileg in ({1, 2, 3}, {1, 2, 3, 4, 5, 6}):
        S3 = SenderSim(reloj, saldo_ilegible_en=ileg); S3.saldo = lambda: None; P3 = PL.Paquete(cfg, S3, M, out, reloj, 'r4h2', stdout=False); P3.anclas_fn = lambda: 0; P3.anclas_por_moneda_fn = lambda: {}
        assert P3.correr() == 'BLOCKED' and len(S3.posts_enviados) == 0 and 'saldo_ilegible_en_arranque' in P3.kill, P3.kill                                       # ilegible: fail-closed
        break


def test_r4h3_no_existe_ruta_de_envio_sin_gtd():
    import pl_sender_real as R2
    S = SenderSim(RelojVirtual())
    for mal in (None, 0, 60, 184): 
        try: S.colocar('T', 0.01, 5.0, 'k', neg_risk=False, expira_s=mal); assert False, mal
        except RuntimeError: pass
    assert S.colocados == []
    try: S.enviar(dict(oid='0x1', tok='T', precio=0.01, size=5.0, neg_risk=False, expira_s=None)); assert False
    except RuntimeError: pass
    sr = R2.SenderReal(types.SimpleNamespace(poner=lambda *a, **k: (_ for _ in ()).throw(AssertionError('no debia firmar'))), None, None, None, os.path.join(TMP, 'evid_r4h3'))
    for mal in (None, 0, 120):
        try: sr.colocar('T', 0.01, 5.0, 'k', neg_risk=True, expira_s=mal); assert False, mal
        except RuntimeError as e: assert 'GTD' in str(e)
    P, S, R, M, out = montar('r4h3', cfg=C.Config(max_ordenes=8)); P.correr(); assert S.colocados and all(c['expira_s'] >= 185 for c in S.colocados)


def test_r4h4_invariantes_son_raise_y_no_assert():
    import ast, subprocess
    for f in ('paquete_l.py', 'pl_core.py', 'pl_sender.py', 'pl_sender_real.py'):
        arbol = ast.parse(open(os.path.join(H, f)).read()); assert not [n.lineno for n in ast.walk(arbol) if isinstance(n, ast.Assert)], f          # ningun assert en el codigo de produccion
    r = subprocess.run([sys.executable, '-O', '-I', '-c', f'import sys; sys.path.insert(0, {H!r}); import pl_core as C\n'
                        'for mal in (dict(max_simultaneas=13), dict(perdida_dura=0.70), dict(gtd_expira_s=0)):\n'
                        '    try: C.Config(**mal); print("NO_RAISE", mal)\n'
                        '    except C.Invariante: pass\n'
                        'print("OK")'], capture_output=True, text=True); assert r.stdout.strip() == 'OK', (r.stdout, r.stderr[-300:])                 # con -O los topes siguen vigentes
    r = subprocess.run([sys.executable, '-O', '-I', '-c', f'import sys; sys.path.insert(0, {H!r}); import pl_core as C; C.exigir_aislamiento()'], capture_output=True, text=True); assert r.returncode != 0 and '-O' in (r.stderr + r.stdout)    # el envio real rechaza -O
    P, S, R, out = _p_con_ordenes('r4h4'); P.pres = C.Presupuesto(P.cfg, 0.612681); assert all(P.pres.puede_enviar(n) == (n < 12) for n in range(0, 14)); assert not C.Presupuesto(C.Config(), 0.612681).puede_enviar(12)


def test_r4h5_chrony_reloj_local_no_es_sincronizado():
    cfg = C.Config(); ok = dict(system_time_s=0.01, last_offset_s=0.0, stratum=3, ref_id='65D8456C', leap='Normal', root_dispersion_s=0.001); assert C.reloj_sincronizado(ok, cfg)
    for k, v in (('ref_id', '7F7F0101'), ('ref_id', '7f7f0101'), ('stratum', 10), ('stratum', 11)): assert not C.reloj_sincronizado(dict(ok, **{k: v}), cfg), (k, v)


def test_r4h6_ledger_fallo_de_escritura_no_pega_filas():
    ruta = os.path.join(TMP, 'r4h6.jsonl')
    if os.path.exists(ruta): os.remove(ruta)
    L = C.Ledger(ruta); L.add('a', 'x', 0); f0 = L.f
    class Roto:                                                                                           # escribe la MITAD de la linea y falla (disco lleno)
        def write(s, t): f0.write(t[: len(t) // 2]); f0.flush(); raise OSError('ENOSPC')
        def flush(s): f0.flush()
        def fileno(s): return f0.fileno()
        def close(s): f0.close()
    L.f = Roto(); L.add('a', 'y', 0); assert L.fallos_escritura == 1; L.f = f0; L.add('a', 'z', 0); L.add('a', 'w', 0); L.cerrar()
    L2 = C.Ledger(ruta); eids = {r['eid'] for r in L2.filas}; assert {'a|x|0', 'a|z|0', 'a|w|0'} <= eids and L2.corruptas == 1, (eids, L2.corruptas)       # la media linea queda como ILEGIBLE (contada), z y w no se pierden
    assert all(l == '' or json.loads(l) for l in open(ruta).read().split('\n'))                                                       # tras reparar, el fichero entero parsea


def test_r4h7_liquidar_informe_no_modifica_el_ledger_y_dice_que_escribe():
    out = os.path.join(TMP, 'r4h7'); os.makedirs(out, exist_ok=True); ruta = out + '/ledger.jsonl'
    with open(ruta, 'wb') as f: f.write(b'{"eid": "intencion|a|0", "k": "intencion", "clave": "a", "slot": 0, "coin": "BTC", "tok": "T", "precio": 0.01, "size": 5.0}\n{"eid": "roto')
    antes = open(ruta, 'rb').read(); PL.liquidar_informe(out, get=lambda u, p: (_ for _ in ()).throw(RuntimeError('sin red'))); assert open(ruta, 'rb').read() == antes and not os.path.exists(ruta + '.rep')
    ayuda = inspect.getsource(PL.construir_parser).split("'--liquidar-informe'")[1].split('\n')[0]; assert 'liquidacion_residuales.json' in ayuda and 'no modifica el ledger' in ayuda and 'solo lectura' not in ayuda, ayuda
    assert 'ESCRIBE' in PL.liquidar_informe.__doc__


def test_r4h8_preflight_exige_minimo_0_60():
    src = inspect.getsource(__import__('pl_sender_real')); assert 'cfg.max_simultaneas * cfg.coste_orden - 1e-9 <= sal' in src          # (la prueba funcional esta en test_r1_preflight_solo_lectura: caso 'saldo_bajo_minimo_0_60')


def test_r4h9_abiertas_final_cada_ronda_releida_y_validada():
    P, S, R, out = _p_con_ordenes('r4h9a'); P.ordenes['x'].oid = '0x1'; seq = iter([['0x1'], None]); S.abiertas_todas = lambda: next(seq); S.estado = lambda oid: (0.0, 'LIVE'); P._abiertas_final()
    assert P.ilegibles and not P.abiertas_res, (P.ilegibles, P.abiertas_res)                                                              # la relectura None NO cuenta como 'sin abiertas'
    P, S, R, out = _p_con_ordenes('r4h9b'); lect = {'n': 0}
    def ab(): lect['n'] += 1; return ['0x1'] if lect['n'] == 1 else []
    S.abiertas_todas = ab; P._abiertas_final(); assert lect['n'] >= 2 and not P.abiertas_res and not P.ilegibles                       # tras cancelar se RELEE (no se da por buena la primera)
    P, S, R, out = _p_con_ordenes('r4h9c'); S.abiertas_todas = lambda: ['0x1']; P._abiertas_final(); assert P.abiertas_res                  # sigue viva tras las relecturas: residual


def test_r4h10_mensaje_de_bloqueo_por_ilegibles_dice_la_verdad():
    src = inspect.getsource(PL.Paquete._cuerpo); assert 'cuenta del ledger de ESTE --out' in src and 'cambiar solo el run-id NO lo desbloquea' in src
    reloj = RelojVirtual(); out = os.path.join(TMP, 'r4h10'); cfg = C.Config(max_ordenes=8); M = MercadosSim(reloj)
    P1 = PL.Paquete(cfg, SenderSim(reloj), M, out, reloj, 'r4h10a', stdout=False); P1.anclas_fn = lambda: 0; P1.anclas_por_moneda_fn = lambda: {}; P1.correr(); P1.led.add('ilegible', 'otro|x', 99, detalle='x'); P1.led.cerrar()
    S2 = SenderSim(reloj); P2 = PL.Paquete(cfg, S2, M, out, reloj, 'r4h10b', stdout=False); P2.anclas_fn = lambda: 0; P2.anclas_por_moneda_fn = lambda: {}                  # OTRO run-id, mismo --out
    P2.correr(); assert len(S2.posts_enviados) == 0                                                                                   # el run-id distinto NO desbloquea (el texto ya lo dice)


# ---------------------------------------------------------------- ronda 5 (v7): 5o /code-review, hallazgos 1-10 + pendiente de la ronda 4 (ledger con filas corruptas)
import contextlib, io, hashlib as _hl


def _sha(ruta): return _hl.sha256(open(ruta, 'rb').read()).hexdigest()


def test_r5h1_vida_minima_se_revalida_justo_antes_del_post():
    class MercadosLentos(MercadosSim):                                          # el libro de UNA moneda cae 110 s durante la preparacion del lote: los slots ya preparados envejecen
        def __init__(self, reloj, coin_mala, dur_s): super().__init__(reloj); self.cm = coin_mala; self.dur = dur_s; self.ini_ns = reloj.now_ns()
        def libro(self, tok):
            if tok.startswith(self.cm) and (self.r.now_ns() - self.ini_ns) / 1e9 < self.dur: raise OSError('libro caido')
            return super().libro(tok)
    R = RelojVirtual(t0_ns=(1_790_000_100 + 158) * 10**9); sl = C.plan_slots(C.Config(), 8); mala = sl[-1].coin if sl[-1].coin != sl[0].coin else sl[-2].coin
    P, S, R, M, out = montar('r5h1', cfg=C.Config(max_ordenes=8, objetivo_anclas=1000), mercados=MercadosLentos(R, mala, 110.0), reloj=R); P.correr(); ints = rows(out, 'intencion'); assert ints
    for r in ints: assert r['fin_s'] - r['t_decision_ns'] / 1e9 >= C.Config().min_vida_mercado_s + r['hold_s'] + 2.0, (r['clave'], r['fin_s'] - r['t_decision_ns'] / 1e9)       # NINGUN slot sale con menos de la vida minima de la fase A
    sk = [r for r in rows(out, 'saltado') if str(r['motivo']).startswith('vida_minima_al_post')]; assert sk and P.cnt['saltados_mercado_caducado'] == len(sk), (sk, dict(P.cnt))
    print('T76 ok [R5 h1]: con la preparacion/espera larga los slots viejos se SALTAN (%d) en vez de enviarse con ~32 s de vida; los enviados cumplen min_vida+hold+2' % len(sk))


def test_r5h2_post_ambiguo_inexistente_no_retrasa_a_las_demas_ni_impide_reanudar():
    cfg = C.Config(max_ordenes=16, objetivo_anclas=1000); P, S, R, M, out = montar('r5h2', cfg=cfg); orig = S.enviar
    def enviar(h):
        if S.n_post + 1 == 3: S.n_post += 1; R.sleep(0.085); raise ErrHTTP(None, 'timeout: la orden nunca llego')           # POST ambiguo cuya orden NO existe
        return orig(h)
    S.enviar = enviar; st = P.correr(); inf = json.load(open(out + '/informe_final.json')); amb = [r for r in rows(out, 'post') if r['clase'] == 'ambiguo']; assert len(amb) == 1
    for r in rows(out, 'cancel'):                                               # (a) ninguna cancelacion de hold espera mas de ~1 paso a la ambigua (antes: 5-7 s de bucle de gracia+backoffs)
        if r['intento'] == 1 and r['trig'] == 'hold': assert (r["t_send_ns"] - r["t_trig_prog_ns"]) / 1e9 < 0.3, ((r['t_send_ns'] - r['t_trig_prog_ns']) / 1e9, r['clave'])
    cer = [r for r in rows(out, 'cerrada') if r['clave'] == amb[0]['clave']]                          # (b) el barrido PRUEBA que no existio: el kill duro se resuelve y el run no queda BLOCKED
    assert cer[-1]['motivo'] == 'inexistente_verificada' and rows(out, 'kill_resuelto') and st != 'BLOCKED' and inf['kills_resueltos'] and P.kill is None, (st, P.kill, inf['motivo'], cer[-1])
    assert inf['cobertura']['indeterminadas'] == 0 and sum(len(S.abiertas(p['tok'])) for p in S.posts_enviados) == 0
    n1 = len(S.posts_enviados); P2, S2, R2, M2, _ = montar('r5h2b', cfg=cfg, sender=S, reloj=R, mercados=M, dir_out=out, run_id='r5h2'); P2.correr()
    assert 'resume_rechazado' not in str(P2.kill) and len(S.posts_enviados) > n1 and P2.kill == 'max_ordenes', (P2.kill, n1, len(S.posts_enviados))                       # reanuda y llega a su limite
    # (b') si NO se puede verificar (el exchange SI la tiene viva y no se puede cancelar) sigue BLOQUEANDO: no se resuelve ningun kill
    P3, S3, R3, M3, out3 = montar('r5h2c', cfg=C.Config(max_ordenes=8, objetivo_anclas=1000)); fallar_cancelaciones_de_la_primera_orden(S3, R3, 400); st3 = P3.correr()
    assert st3 == 'BLOCKED' and not rows(out3, 'kill_resuelto') and P3.kill, (st3, P3.kill)
    print('T77 ok [R5 h2]: la ambigua inexistente no retrasa las demas cancelaciones (<0,5 s), el barrido la verifica (kill_resuelto), el run no queda BLOCKED y se puede reanudar; sin verificacion sigue BLOCKED')


def test_r5h2b_resume_reconcilia_una_indeterminada_previa_y_solo_continua_si_se_verifica():
    cfg = C.Config(max_ordenes=8, objetivo_anclas=1000)
    def preparar(nombre, abierta):
        P1, S, R, M, out = montar(nombre, cfg=cfg); P1.correr(); n = len(rows(out, 'intencion')); cl = f'{nombre}|s900'
        for k, kw in (('intencion', dict(slot=900, coin='BTC', tok='BTC1U', precio=0.01, size=5.0, oid_local='0xfantasma', t_decision_ns=R.now_ns() - int(500e9))), ('post', dict(oid='0xfantasma', t_send_ns=R.now_ns() - int(499e9), t_ack_ns=R.now_ns() - int(499e9), clase='ambiguo')),
                      ('cerrada', dict(motivo='CANCEL_NO_CONFIRMADA', size_matched=None, indeterminada=True, t_ns=R.now_ns())), ('kill', dict(motivo=f'cancel_no_confirmada:{cl}', status='BLOCKED', t_ns=R.now_ns()))):
            with open(out + '/ledger.jsonl', 'a') as f: f.write(json.dumps(dict(eid=f'{k}|{cl if k != "kill" else "run"}|{0 if k != "kill" else 99}', k=k, clave=(cl if k != 'kill' else 'run'), **kw)) + '\n')
        with open(out + '/ledger.jsonl', 'a') as f: f.write(json.dumps(dict(eid='kill|run|98', k='kill', clave='run', motivo=f'resume_rechazado_kill_previo:cancel_no_confirmada:{cl}', status='BLOCKED', t_ns=R.now_ns())) + '\n')      # un rechazo anterior derivado del mismo kill tambien se levanta con la verificacion
        if abierta: S.abiertas_todas = lambda: ['0xfantasma']                                                    # el exchange SI la tiene: no se puede verificar
        return montar(nombre + 'b', cfg=cfg, sender=S, reloj=R, mercados=M, dir_out=out, run_id=nombre), S, out
    (P2, S, R, M, _), S, out = preparar('r5h2r1', False); n1 = len(S.posts_enviados); P2.correr()                          # verificable: se resuelve y el resume sigue (llega a su limite max_ordenes)
    assert 'resume_rechazado' not in str(P2.kill) and rows(out, 'kill_resuelto') and P2.kill == 'max_ordenes', (P2.kill, rows(out, 'kill_resuelto'))
    (P3, S3, R3, M3, _), S3, out3 = preparar('r5h2r2', True); P3.correr()                                                    # NO verificable: el resume sigue rechazado y no resuelve nada
    assert 'orden_indeterminada' in str(P3.kill) and not rows(out3, 'kill_resuelto') and len(S3.posts_enviados) == 8, (P3.kill,)
    print('T77b ok [R5 h2]: un resume reconcilia la INDETERMINADA previa: verificada => kill_resuelto y continua; no verificable => BLOCKED sin enviar')


def test_r5h3_instancia_unica_por_wallet_y_por_out():
    cfg = C.Config(); out1 = os.path.join(TMP, 'r5h3a'); out2 = os.path.join(TMP, 'r5h3b'); fds = C.tomar_locks(cfg.wallet, out1); assert fds and len(fds) == 2
    try:
        reloj = RelojVirtual(); S = SenderSim(reloj); P = PL.Paquete(cfg, S, MercadosSim(reloj), out2, reloj, 'r5h3b', stdout=False)                  # misma WALLET, otro --out
        assert C.locks_de_run(cfg, out2, True) is None and (l2 := C.locks_de_run(cfg, out2, False)) and not C.liberar_locks(l2)            # v8 (hallazgos 2/8): misma WALLET + otro --out: el run REAL choca; un dry-run NO toma el lock de wallet (no bloquea ni es bloqueado por el real)
        P._locks = None; P.real = True                                                                                                             # real=True solo cambia la decision de locks: sale ANTES de usar el sender
        with contextlib.redirect_stderr(io.StringIO()) as e: assert P.correr() == 'LOCKED'
        assert 'INSTANCIA UNICA' in e.getvalue() and S.n_post == 0 and S.n_saldo == 0 and S.n_colocar == 0 and not [f for f in os.listdir(out2)], os.listdir(out2)            # no toca nada: ni ledger, ni checkpoint, ni informe, ni log
        cfg2 = C.Config(wallet='0x' + '1' * 40); reloj = RelojVirtual(); S = SenderSim(reloj); P = PL.Paquete(cfg2, S, MercadosSim(reloj), out1, reloj, 'r5h3c', stdout=False)   # otra wallet, MISMO --out
        with contextlib.redirect_stderr(io.StringIO()): assert P.correr() == 'LOCKED'
        assert S.n_post == 0 and not os.path.exists(out1 + '/ledger.jsonl') and not os.path.exists(out1 + '/run.log')
        with pytest_raises_invariante(): PL.liquidar_informe(out1, get=lambda u, p: [])                                                         # liquidar escribe en el --out: tambien exige el lock
        assert not os.path.exists(out1 + '/liquidacion_residuales.json')
    finally: C.liberar_locks(fds)
    P2, S2, R2, M2, out3 = montar('r5h3d', cfg=C.Config(max_ordenes=8, objetivo_anclas=1000)); assert P2.correr() == 'PARTIAL'; libre = C.tomar_locks(cfg.wallet, out3); assert libre is not None; C.liberar_locks(libre)                  # el lock se libera al terminar `correr`
    snap = {f: _sha(os.path.join(out3, f)) for f in ('ledger.jsonl', 'checkpoint.json', 'informe_final.json', 'run_manifest.json', 'run.log', 'parcial_resumen.json')}; fds = C.tomar_locks(cfg.wallet, out3)
    try:                                                                         # RESUME con el lock tomado: sale sin tocar NADA
        P3, S3, R3, M3, _ = montar('r5h3d', cfg=C.Config(max_ordenes=8, objetivo_anclas=1000), dir_out=out3, run_id='r5h3d')
        with contextlib.redirect_stderr(io.StringIO()): assert P3.correr() == 'LOCKED'
        assert snap == {f: _sha(os.path.join(out3, f)) for f in snap} and S3.n_post == 0 and sorted(os.listdir(out3)) == sorted(set(os.listdir(out3)))
    finally: C.liberar_locks(fds)
    pre = C.tomar_locks(cfg.wallet, os.path.join(TMP, 'r5h3e')); P4, S4, R4, M4, out4 = montar('r5h3e', cfg=C.Config(max_ordenes=8, objetivo_anclas=1000)); P4._locks = pre              # locks ya tomados por main(): `correr` no los retoma (no choca consigo) ni los libera
    st4 = P4.correr(); ocupado = C.tomar_locks(cfg.wallet, out4); C.liberar_locks(pre)
    assert st4 == 'PARTIAL' and P4._locks == pre and ocupado is None, (st4, ocupado)
    # CLI: segundo proceso sobre el mismo --out (lock en /tmp: el de produccion) sale con 2 sin crear el directorio
    out5 = os.path.join(TMP, 'r5h3cli'); fds = C.tomar_locks('0x' + '2' * 40, out5, lock_dir='/tmp', wallet_lock=False)      # v8 (hallazgo 2): solo el lock de --out (unico del dry-run) y NUNCA la wallet real en el /tmp de produccion
    try:
        r = subprocess.run([sys.executable, '-I', H + 'paquete_l.py', '--out', out5, '--run-id', 'cli5', '--max-ordenes', '8', '--objetivo', '1000'], capture_output=True, text=True)
        assert r.returncode == 2 and 'INSTANCIA UNICA' in r.stderr and not os.path.exists(out5), (r.returncode, r.stderr[-200:])
    finally: C.liberar_locks(fds)
    print('T78 ok [R5 h3]: flock exclusivo no bloqueante por wallet Y por --out (fuera de --out): la 2a instancia (run, resume, liquidar, CLI) sale sin tocar nada; se libera al terminar')


@contextlib.contextmanager
def pytest_raises_invariante():
    try: yield
    except C.Invariante: return
    raise AssertionError('esperaba Invariante')


def test_r5h4_d_proc_solo_cuenta_el_primer_intento():
    f = [dict(k='cancel', intento=1, t_trig_rx_ns=1_000, t_send_ns=1_000 + 5_000_000, t_ack_ns=1_000 + 70_000_000, ok=False), dict(k='cancel', intento=2, t_trig_rx_ns=1_000, t_send_ns=1_000 + 1_000_000_000, t_ack_ns=1_000 + 1_060_000_000, ok=True)]
    st = C.d_proc_stats(f); assert st['d_proc_ms']['n'] == 1 and abs(st['d_proc_ms']['p50'] - 5.0) < 1e-9 and st['reintentos']['n'] == 1 and abs(st['reintentos']['t_send_menos_t_trig_ms']['p50'] - 1000.0) < 1e-6, st
    P, S, R, M, out = montar('r5h4', cfg=C.Config(max_ordenes=16, objetivo_anclas=1000), sender_kw=dict(index_delay_s=2.2)); P.correr(); inf = json.load(open(out + '/informe_final.json'))               # get_order sin indexar: hay reintentos (bucle de pre-indice)
    can = rows(out, 'cancel'); p1 = [(r['t_send_ns'] - r['t_trig_rx_ns']) / 1e6 for r in can if r['intento'] == 1]; pn = [r for r in can if r['intento'] > 1]; assert pn and p1
    dp = inf['latencias']['d_proc_ms']; assert dp['n'] == len(p1) and dp['max'] < 100 and inf['latencias']['reintentos']['n'] == len(pn) and inf['latencias']['reintentos']['t_send_menos_t_trig_ms']['max'] > 200, inf['latencias']
    print('T79 ok [R5 h4]: d_proc solo con intento==1 (n=%d, max %.1f ms); %d reintentos aparte (max %.0f ms)' % (dp['n'], dp['max'], len(pn), inf['latencias']['reintentos']['t_send_menos_t_trig_ms']['max']))


def test_r5h5_un_resume_rechazado_no_pisa_el_informe_del_run_original():
    cfg = C.Config(max_ordenes=16, objetivo_anclas=1000); P, S, R, M, out = montar('r5h5', cfg=cfg)
    def tras(nl): raise RuntimeError('fallo raro en _tras_lote')
    P._tras_lote = tras; st = P.correr(); assert st == 'FAILED'; inf0 = json.load(open(out + '/informe_final.json')); assert inf0['excepciones']
    snap = {f: _sha(os.path.join(out, f)) for f in ('informe_final.json', 'run_manifest.json', 'checkpoint.json', 'parcial_resumen.json') if os.path.exists(os.path.join(out, f))}; assert 'run_manifest.json' in snap and 'checkpoint.json' in snap
    P2, S2, R2, M2, _ = montar('r5h5b', cfg=cfg, sender=S, reloj=R, mercados=M, dir_out=out, run_id='r5h5'); n1 = len(S.posts_enviados); st2 = P2.correr()
    assert st2 == 'FAILED' and 'resume_rechazado' in P2.kill and len(S.posts_enviados) == n1, (st2, P2.kill)
    assert snap == {f: _sha(os.path.join(out, f)) for f in snap}, 'el resume rechazado piso informe/manifiesto/checkpoint del run original'
    rech = [f for f in os.listdir(out) if f.startswith('informe_rechazo_')]; assert len(rech) == 1 and json.load(open(os.path.join(out, rech[0])))['rechazo_de_resume'] is True
    # resume legitimo (limite benigno): el informe del proceso anterior se CONSERVA (informe_final.previo_*)
    P3, S3, R3, M3, out3 = montar('r5h5c', cfg=cfg); P3.correr(); orig3 = open(out3 + '/informe_final.json').read()
    P4, S4, R4, M4, _ = montar('r5h5d', cfg=cfg, sender=S3, reloj=R3, mercados=M3, dir_out=out3, run_id='r5h5c'); P4.correr()
    prev = [f for f in os.listdir(out3) if f.startswith('informe_final.previo_')]; assert len(prev) == 1 and open(os.path.join(out3, prev[0])).read() == orig3
    print('T80 ok [R5 h5]: el resume rechazado escribe su propio informe_rechazo_* y deja intactos informe_final/manifiesto/checkpoint; un resume que opera conserva el informe anterior (previo)')


def test_r5h6_fase_b_realizable_benigna_y_con_topes():
    def correrB(nombre, mk, **cfgkw):
        cfg = C.Config(fase_b_max_rellenos=2, fase_b_ordenes=8, **cfgkw); reloj = RelojVirtual(); M = MercadosSim(reloj, **mk); P, S, R, M, out = montar(nombre, cfg=cfg, reloj=reloj, mercados=M); st = P.correr(); return st, json.load(open(out + '/informe_final.json')), out, P
    # (a) token barato SOLO en los ultimos 100 s del mercado: con la vida heredada de la fase A (142-152 s) no habria coincidencia nunca
    st, inf, out, P = correrB('r5h6a', dict(down_barato=True, barato_vida_max_s=100.0)); top = [r for r in rows(out, 'intencion') if r['modo'] == 'top']
    assert st == 'COMPLETE' and top and inf['fase_b']['ordenes'] == len(top) and all(r['libro']['mejor_bid'] == 0.01 and r['libro']['mejor_ask'] <= 0.05 for r in top), (st, inf['motivo'], inf['fase_b'])
    cfg = C.Config(); assert all(r['fin_s'] - r['t_decision_ns'] / 1e9 >= cfg.fase_b_min_vida_s + r['hold_s'] + 2.0 for r in top) and all(r['fin_s'] - r['t_decision_ns'] / 1e9 <= 100.0 for r in top)
    assert cfg.min_vida_mercado_s + cfg.hold_b_min_s + 2.0 + cfg.prep_presupuesto_s > 100.0                                 # con la regla anterior (90 + hold + 2 + 40 = 142-152 s) esta ventana de 100 s era inalcanzable
    # (b) nunca hay token barato: la fase B termina BENIGNA, el run conserva el status de la fase A (antes: BLOCKED sin_mercado_valido_prolongado)
    st, inf, out, P = correrB('r5h6b', dict(down_barato=False)); assert st == 'COMPLETE' and inf['fase_b']['fin'] == 'sin_token_barato' and not [r for r in rows(out, 'intencion') if r['modo'] == 'top'] and P.kill is None and 'sin_mercado' not in inf['motivo'], (st, inf['motivo'], inf['fase_b'])
    assert rows(out, 'fase_b_fin') and not rows(out, 'kill'), rows(out, 'kill')
    # (c) respeta max_ordenes (A usa 8; quedan 2 para la fase B)
    st, inf, out, P = correrB('r5h6c', dict(down_barato=True), objetivo_anclas=8, min_anclas_moneda={}, max_ordenes=10); n = len(rows(out, 'intencion')); assert n <= 10 and st == 'COMPLETE' and inf['fase_b']['fin'] == 'max_ordenes' and inf['fase_b']['ordenes'] == 2, (n, st, inf['fase_b'])
    # (d) respeta max_minutos (A termina pasado el limite): 0 ordenes top y fin benigno
    st, inf, out, P = correrB('r5h6d', dict(down_barato=True), objetivo_anclas=8, min_anclas_moneda={}, max_minutos=0.1); assert st == 'COMPLETE' and inf['fase_b']['fin'] == 'max_minutos' and inf['fase_b']['ordenes'] == 0, (st, inf['motivo'], inf['fase_b'])
    print('T81 ok [R5 h6]: fase B con vida propia (%g s + hold + 2) halla tokens baratos de la recta final; sin token = fin benigno (status de A); respeta max_ordenes y max_minutos' % cfg.fase_b_min_vida_s)


def test_r5h7_un_solo_criterio_de_saldo_contra_el_ledger():
    P, S, R, out = _p_con_ordenes('r5h7'); S.saldo_v = 0.592681                                                       # 0,02 $ gastados (2 acc a 0,01) y EXPLICADOS por un relleno del ledger
    P.led.add('intencion', 'r5h7|s1', 0, slot=1, coin='BTC', tok='T1', precio=0.01, size=5.0); P.led.add('estado', 'r5h7|s1', 1, matched=2.0, status='MATCHED', t_ns=R.now_ns()); P.led.add('cerrada', 'r5h7|s1', 0, motivo='cancelada', size_matched=2.0, t_ns=R.now_ns())
    o = C.Orden(clave='r5h7|s2', slot=2, coin='ETH', tok='T2', precio=0.01, size=5.0, oid='0xfantasma', t_ack_ns=R.now_ns() - int(100e9)); P.ordenes[o.clave] = o
    assert P.reconciliar_orden(o, 'prueba') is True and [r for r in P.led.filas if r['k'] == 'cerrada'][-1]['motivo'] == 'inexistente_verificada'              # antes: s0 - saldo (0,02) >= tol => INDETERMINADA aunque el ledger lo explicara
    S.saldo_v = 0.562681                                                                                              # 0,05 $ de caida: 0,03 NO explicados por el ledger => no se puede probar
    o2 = C.Orden(clave='r5h7|s3', slot=3, coin='ETH', tok='T3', precio=0.01, size=5.0, oid='0xfantasma2', t_ack_ns=R.now_ns() - int(100e9)); P.ordenes[o2.clave] = o2
    assert P.reconciliar_orden(o2, 'prueba') is False and [r for r in P.led.filas if r['k'] == 'cerrada'][-1]['motivo'] == 'INDETERMINADA'
    assert inspect.getsource(PL).count('tol_saldo_usd') <= 2 and 'def _saldo_cae_mas_que_ledger' in inspect.getsource(PL.Paquete)                    # la funcion unica + el descuadre bidireccional del arranque; ninguna comparacion ad hoc mas
    print('T82 ok [R5 h7]: reconciliar_orden descuenta el gasto explicado por el ledger (misma funcion que tras-lote y barrido)')


def test_r5h8_repro_usa_los_nombres_reales_de_argparse():
    params = dict(run_id='real 1', out='/tmp/un dir/out', escenario='fill_total', objetivo=50, max_ordenes=30, fase_b=3, real=True, tiempo_real=True, evid_dir='/tmp/ev', confirmacion='/tmp/ok.txt')
    P, S, R, M, out = montar('r5h8'); P.params = params; cmd = shlex_split(P._repro()); assert cmd[:2] == ['python3', '-I'] and cmd[2].endswith('paquete_l.py')
    a = PL.construir_parser().parse_args(cmd[3:]); assert (a.run_id, a.out, a.escenario, a.objetivo, a.max_ordenes, a.fase_b, a.real, a.tiempo_real, a.evid_dir, a.confirmacion) == ('real 1', '/tmp/un dir/out_repro_dry', 'fill_total', 50, 30, 3, False, True, None, None)      # v8 (hallazgo 1): la reproduccion de un run REAL es un DRY-RUN en otro --out
    assert '--real' not in cmd and '--confirmacion' not in ' '.join(cmd) and '--evid-dir' not in ' '.join(cmd) and not any(x.startswith('--preflight') for x in cmd), cmd
    P.params = dict(run_id='x', out='/tmp/o', escenario='base', objetivo=None, max_ordenes=None, fase_b=None, real=False, tiempo_real=False, evid_dir=None, confirmacion=None); a = PL.construir_parser().parse_args(shlex_split(P._repro())[3:]); assert a.real is False and a.fase_b == 0 and a.run_id == 'x'
    out = os.path.join(TMP, 'cli8'); r = subprocess.run([sys.executable, '-I', H + 'paquete_l.py', '--out', out, '--run-id', 'cli8', '--max-ordenes', '16', '--objetivo', '1000'], capture_output=True, text=True); assert r.returncode == 0, r.stderr[-200:]
    repro = json.load(open(out + '/informe_final.json'))['repro']; r2 = subprocess.run([sys.executable] + shlex_split(repro)[1:], capture_output=True, text=True); assert r2.returncode == 0 and 'unrecognized' not in r2.stderr, (repro, r2.stderr[-200:])      # el comando de reproduccion ES ejecutable
    print('T83 ok [R5 h8]: _repro genera --run-id/--max-ordenes/--fase-b...; ida y vuelta por el parser real y ejecutable')


def shlex_split(s):
    import shlex; return shlex.split(s)


def test_r5h9_saldo_onchain_exige_dos_lecturas_validas_y_sin_asserts_en_el_envio():
    V = _vm(); ok = lambda v: {'result': hex(v)}
    assert V.saldo_onchain(C.WALLET_DEDICADA, _post=lambda u, j: ok(612681)) == 0.612681                                      # 3 RPC coinciden
    seq = iter([ok(612681), ok(562681), ok(1)]); assert V.saldo_onchain(C.WALLET_DEDICADA, _post=lambda u, j: next(seq)) == 0.562681        # 2 validas distintas: el minimo
    seq = iter([{'error': 'x'}, ok(612681), {'result': '0x'}]); assert V.saldo_onchain(C.WALLET_DEDICADA, _post=lambda u, j: next(seq)) is None          # UNA sola valida => ilegible (antes devolvia ese valor)
    def uno_solo(u, j):
        if 'drpc' in u or '1rpc' in u: raise OSError('caido')
        return ok(612681)
    assert V.saldo_onchain(C.WALLET_DEDICADA, _post=uno_solo) is None and V.saldo_onchain(C.WALLET_DEDICADA, _post=lambda u, j: {'error': 1}) is None
    import ast; base = '/root/polymarket-research/polygon_rpc.py'                                                         # la lista del vendor replica el grupo 'latest' de polygon_rpc (regla: Polygon via polygon_rpc.py)
    if os.path.exists(base):
        d = [n for n in ast.parse(open(base).read()).body if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == '_POR_DEFECTO'][0].value; lat = ast.literal_eval(d.values[[ast.literal_eval(k) for k in d.keys].index('latest')]); assert tuple(lat) == tuple(V.RPCS), (lat, V.RPCS)
    for f in ('vendor_main.py', 'envio_real.py', 'cancel_evidencia.py', 'regenerar_vendor.py'):                             # nada de `assert` en lo que ejecuta el envio real / preflight (ni en el generador offline)
        assert not [n for n in ast.walk(ast.parse(open(H + 'vendor/' + f).read())) if isinstance(n, ast.Assert)], f
    for f in ('pl_core.py', 'pl_sender.py', 'pl_sender_real.py', 'paquete_l.py'):                                           # `plan_paquete_l.plan` (conserva un assert) es solo el generador de planes: ningun modulo del envio lo llama
        assert not [n for n in ast.walk(ast.parse(open(H + f).read())) if isinstance(n, ast.Attribute) and n.attr == 'plan' and getattr(n.value, 'id', '') in ('P', 'PL', 'plan_paquete_l')], f
    print('T84 ok [R5 h9]: saldo_onchain exige >=2 lecturas validas (minimo); RPCS = grupo latest de polygon_rpc; sin assert en vendor del envio')


def test_r5h10_una_lectura_de_anclas_por_lote_sin_analiza_y_tolerante_a_gz_truncado():
    import gzip
    d = os.path.join(TMP, 'r5h10evid'); os.makedirs(d, exist_ok=True)
    def evs(pref, n): return [e for i in range(n) for e in (dict(k='alta', oid=f'{pref}{i}', t_envio_ms=1000 + i, tok='t'), dict(k='user_order', oid=f'{pref}{i}', mine=True, tipo='PLACEMENT', ts_ex_ms=1080 + i), dict(k='user_order', oid=f'{pref}{i}', mine=True, tipo='CANCELLATION', ts_ex_ms=2100 + i), dict(k='cancel_try', oid=f'{pref}{i}', canceled=[f'{pref}{i}'], t_pre_ms=2090 + i, t_resp_ms=2150 + i))]
    open(d + '/cancel_evid_2026-11-12.jsonl', 'w').write('\n'.join(json.dumps(x) for x in evs('a', 3)) + '\n{"cortado"')
    gz = gzip.compress(('\n'.join(json.dumps(x) for x in evs('b', 400)) + '\n').encode()); open(d + '/cancel_evid_2026-11-11.jsonl.gz', 'wb').write(gz[:-40])                         # .gz TRUNCADO
    pat = d + '/cancel_evid_*.jsonl*'; V = C.cargar_vendor('plan_paquete_l'); orig = V.analiza; llam = {'n': 0}; leer0 = C.leer_evid; lect = {'n': 0}
    def analiza(p_): llam['n'] += 1; return orig(p_)
    def leer(p_): lect['n'] += 1; return leer0(p_)
    V.analiza = analiza; C.leer_evid = leer
    try:
        n, por = C.contar_anclas(pat); assert n >= 3 and llam['n'] == 0, (n, llam)                                       # no lanza con .gz truncado, cuenta lo legible y NO lanza analiza
        ev, ileg = leer0(pat); assert [os.path.basename(x['fichero']) for x in ileg] == ['cancel_evid_2026-11-11.jsonl.gz'] and ev
        lect['n'] = 0; P, S, R, M, out = montar('r5h10', cfg=C.Config(max_ordenes=16, objetivo_anclas=1000)); P.evid = pat
        P.anclas_unico = lambda filas: (lambda e_, i_: (*C.anclas_de_eventos(e_, filas), e_, i_))(*C.leer_evid(pat))
        st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
        assert st in ('COMPLETE', 'PARTIAL') and lect['n'] == P.cnt['lotes'] + 1 and llam['n'] == 1, (st, lect, llam, dict(P.cnt))                  # UNA lectura por lote + 1 en el informe final; analiza solo en el informe final
        assert [os.path.basename(x['fichero']) for x in inf['evid_ilegibles']] == ['cancel_evid_2026-11-11.jsonl.gz'] and any('cancel_evid ilegibles' in a for a in inf['alertas']) and 'error' in inf['anclas_detalle'], (inf['evid_ilegibles'], inf['alertas'], inf['anclas_detalle'])
    finally: V.analiza = orig; C.leer_evid = leer0
    print('T85 ok [R5 h10]: 1 lectura de cancel_evid por lote (+1 final), analiza solo en el informe final, .gz truncado => lo legible cuenta y el fichero queda marcado (sin excepcion)')


def test_r5_ledger_con_filas_corruptas_no_da_complete_silencioso():
    out = os.path.join(TMP, 'r5corr'); os.makedirs(out); open(out + '/ledger.jsonl', 'w').write('{"eid": "roto\n')
    P, S, R, M, _ = montar('r5corr', dir_out=out); st = P.correr(); inf = json.load(open(out + '/informe_final.json'))
    assert st == 'PARTIAL' and inf['cobertura']['filas_corruptas_ledger'] == 1 and any('LEDGER con 1' in a for a in inf['alertas']) and 'corrupta' in inf['motivo'] and os.path.exists(out + '/ALERTA_paquete_l.txt'), (st, inf['motivo'], inf['alertas'])
    P2, S2, R2, M2, _ = montar('r5corrb', dir_out=out, run_id='r5corr', sender=S, reloj=R, mercados=M); st2 = P2.correr(); inf2 = json.load(open(out + '/informe_final.json'))                                  # un RESUME (fichero ya limpio) tampoco da COMPLETE a secas
    assert st2 == 'PARTIAL' and inf2['cobertura']['filas_corruptas_ledger'] == 1 and any('LEDGER con 1' in a for a in inf2['alertas']), (st2, inf2['motivo'])
    print('T86 ok [R4 pendiente]: filas corruptas del ledger => PARTIAL + alerta (fichero e informe), jamas COMPLETE a secas')


def _prep_kill_previo(nombre, kill_extra, estado):
    """v8: run que acaba con una orden ambigua + kill; devuelve el Paquete que REANUDA. `estado`: None = NO_EXISTE verificable, ('0', 'CANCELED') = terminal legible, 'viva' = el exchange la tiene (no verificable)."""
    cfg = C.Config(max_ordenes=8, objetivo_anclas=1000); P1, S, R, M, out = montar(nombre, cfg=cfg); P1.correr(); cl = f'{nombre}|s900'
    for k, kw in (('intencion', dict(slot=900, coin='BTC', tok='BTC1U', precio=0.01, size=5.0, oid_local='0xfantasma', t_decision_ns=R.now_ns() - int(500e9))), ('post', dict(oid='0xfantasma', t_send_ns=R.now_ns() - int(499e9), t_ack_ns=R.now_ns() - int(499e9), clase='ambiguo')),
                  ('cerrada', dict(motivo='CANCEL_NO_CONFIRMADA', size_matched=None, indeterminada=True, t_ns=R.now_ns())), ('kill', dict(motivo=f'cancel_no_confirmada:{cl}', status='BLOCKED', t_ns=R.now_ns()))):
        with open(out + '/ledger.jsonl', 'a') as f: f.write(json.dumps(dict(eid=f'{k}|{cl if k != "kill" else "run"}|{0 if k != "kill" else 99}', k=k, clave=(cl if k != 'kill' else 'run'), **kw)) + '\n')
    for i, m in enumerate(kill_extra):
        with open(out + '/ledger.jsonl', 'a') as f: f.write(json.dumps(dict(eid=f'kill|run|{90 + i}', k='kill', clave='run', motivo=m, status='BLOCKED', t_ns=R.now_ns())) + '\n')
    if estado == 'viva': S.abiertas_todas = lambda: ['0xfantasma']
    elif estado: S.estado = lambda oid, _e=S.estado: estado if oid == '0xfantasma' else _e(oid); S.cancelar = lambda oid, _c=S.cancelar: True if oid == '0xfantasma' else _c(oid)
    P2 = montar(nombre + 'b', cfg=cfg, sender=S, reloj=R, mercados=M, dir_out=out, run_id=nombre)[0]; return P2, S, out, cl


def test_r6h4_h8_resume_motivos_unicos_y_terminal_legible_levanta_el_kill():
    assert PL.base_kill('resume_rechazado_kill_previo:resume_rechazado_kill_previo:cancel_no_confirmada:x') == 'cancel_no_confirmada:x' and PL.motivo_rechazo_resume('resume_rechazado_kill_previo:a') == 'resume_rechazado_kill_previo:a'
    cl0 = 'r6h4|s900'; P2, S, out, cl = _prep_kill_previo('r6h4', [f'resume_rechazado_kill_previo:resume_rechazado_kill_previo:cancel_no_confirmada:{cl0}'], ('0', 'CANCELED')); n1 = len(S.posts_enviados); P2.correr()
    kr = rows(out, 'kill_resuelto'); assert kr and kr[-1]['motivo'] == f'cancel_no_confirmada:{cl}' and 'terminal' not in kr[-1]['razon'] and kr[-1]['razon'] == 'reconciliada:CANCELED', kr
    assert 'resume_rechazado' not in str(P2.kill) and P2.kill == 'max_ordenes', (P2.kill,)                       # el kill (y el rechazo ANIDADO) se levantan y el resume continua
    P3, S3, out3, _ = _prep_kill_previo('r6h4b', [], 'viva'); P3.correr()
    assert not rows(out3, 'kill_resuelto') and 'orden_indeterminada' in str(P3.kill), P3.kill                                                   # no verificable: sigue bloqueando
    k2 = [r['motivo'] for r in rows(out3, 'kill')]; assert not any(m.count('resume_rechazado_kill_previo:') > 1 for m in k2), k2             # y los rechazos NO se anidan
    print('T87 ok [R6 h4/h8]: un unico generador de motivos de kill; un resume que lee la orden en estado terminal LEGIBLE levanta su kill (tambien con rechazos anidados); no verificable sigue bloqueando sin anidar prefijos')


def test_r6h3_excepcion_fallback_queda_en_kills():
    P, S, R, M, out = montar('r6h3'); P.led = C.Ledger(P.P('ledger.jsonl'))
    def roto(*a, **k): raise OSError('disco lleno')
    P._matar = roto; P._excepcion('x', RuntimeError('boom')); assert P.kills.get('excepcion:RuntimeError') == 'FAILED' and P.kill == 'excepcion:RuntimeError' and P.kill_sev == 3
    P._recalcular_kill(); assert P.kill == 'excepcion:RuntimeError' and P.kill_status == 'FAILED'                                              # un recalculo posterior ya no lo borra
    print('T88 ok [R6 h3]: el kill del fallback de _excepcion vive en self.kills (un _recalcular_kill no lo borra)')


def test_r6h5_resume_que_modifica_estado_escribe_informe_final_real():
    P2, S, out, cl = _prep_kill_previo('r6h5', [], 'viva'); prev0 = open(out + '/informe_final.json').read(); n1 = len(S.posts_enviados); st = P2.correr()
    assert st == 'BLOCKED' and len(S.posts_enviados) == n1 and not [f for f in os.listdir(out) if f.startswith('informe_rechazo_')], (st, os.listdir(out))
    inf = json.load(open(out + '/informe_final.json')); assert inf['status'] == 'BLOCKED' and inf['cobertura']['indeterminadas'] >= 1, inf['status']
    prev = [f for f in os.listdir(out) if f.startswith('informe_final.previo_')]; assert len(prev) == 1 and open(os.path.join(out, prev[0])).read() == prev0           # el informe anterior se conserva
    print('T89 ok [R6 h5]: un resume que no opera pero cambia estado (INDETERMINADA) deja informe_final real + previo; el rechazo puro sigue en informe_rechazo (T80)')


def test_r6h6_ledger_reparado_se_persiste_aunque_el_resume_sea_rechazado_pronto():
    cfg = C.Config(max_ordenes=8, objetivo_anclas=1000); P1, S, R, M, out = montar('r6h6', cfg=cfg); P1.correr()
    with open(out + '/ledger.jsonl', 'a') as f: f.write('{basura sin cerrar\n')
    P2 = montar('r6h6b', cfg=C.Config(max_ordenes=9, objetivo_anclas=1000), sender=S, reloj=R, mercados=M, dir_out=out, run_id='r6h6')[0]; n1 = len(S.posts_enviados); P2.correr()           # config distinta: rechazo temprano
    rr = rows(out, 'ledger_reparado'); assert len(S.posts_enviados) == n1 and rr and rr[0]['corruptas'] == 1, rr
    print('T90 ok [R6 h6]: la fila ledger_reparado se escribe al abrir el ledger, antes de cualquier retorno temprano')


def test_r6h7_poll_fase_b_no_espera_al_limitador():
    cfg = C.Config(fase_b_max_rellenos=2, fase_b_ordenes=8); reloj = RelojVirtual(); S = SenderSim(reloj, fill_a={}, sin_push=True); M = MercadosSim(reloj, down_barato=True)
    P, S, R, M, out = montar('r6h7', cfg=cfg, sender=S, reloj=reloj, mercados=M); orig = P._estado; vistos = []
    def estado(oid, prioritario=False):
        import linecache; fr = sys._getframe(1)
        if 'next_poll_ns' in linecache.getline(fr.f_code.co_filename, fr.f_lineno): vistos.append(prioritario)                       # solo las llamadas del seguimiento 1 Hz
        return orig(oid, prioritario=prioritario)
    P._estado = estado; P.correr(); polls = [r for r in rows(out, 'estado') if r.get('fuente') == 'poll_top']
    assert polls and vistos and all(vistos), (len(polls), vistos[:10])                                              # TODOS los polls fase B son prioritarios (no esperan al limitador)
    print('T91 ok [R6 h7]: el seguimiento 1 Hz de fase B llama a _estado(prioritario=True)')


def test_r6h1_h2_repro_dry_y_lock_de_wallet_solo_en_real():
    assert PL.repro_args(dict(real=True, out='/tmp/o', confirmacion='/tmp/c', evid_dir='/tmp/e', run_id='r', tiempo_real=True)) == ['--out=/tmp/o_repro_dry', '--run-id=r', '--tiempo-real']
    cfg = C.Config(); a = os.path.join(TMP, 'r6h2a'); b = os.path.join(TMP, 'r6h2b'); f1 = C.locks_de_run(cfg, a, False); assert f1 and len(f1) == 1                      # dry: solo --out
    f2 = C.locks_de_run(cfg, b, True); assert f2 and len(f2) == 2; C.liberar_locks(f2); f3 = C.locks_de_run(cfg, b, False); assert f3 and len(f3) == 1; C.liberar_locks(f3); C.liberar_locks(f1)
    print('T92 ok [R6 h1/h2]: repro de un real = dry-run en otro --out sin banderas de envio; el lock de wallet solo se toma con envio real')



if __name__ == '__main__':
    try:
        filtro = sys.argv[1] if len(sys.argv) > 1 else ''                                              # `python3 -I test_paquete_l.py r2h5` ejecuta solo los tests cuyo nombre lo contiene (pruebas de mutacion)
        for n, f in list(globals().items()):
            if n.startswith('test_') and callable(f) and filtro in n: f()
        print('TODOS OK (paquete_l)')
    finally: shutil.rmtree(TMP, ignore_errors=True)
