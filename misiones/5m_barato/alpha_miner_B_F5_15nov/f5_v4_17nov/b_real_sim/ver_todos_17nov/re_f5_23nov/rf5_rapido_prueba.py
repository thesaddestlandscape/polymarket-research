#!/usr/bin/env python3
"""rf5_rapido_prueba.py DIA [A|K] [perfil] -- tiempo e IGUALDAD BIT A BIT lenta (RF5_LENTO=1: replay_variantes.run_day + EngineBloqueo) vs rapida (rf5_rapido: simulador parcheado + memo de run_segment), fria y caliente, para politicas A (base, F3, VETO_UP), K (K1, K2) y K6 (K6, K6 con Calma vacia == K1)
en un dia NO ciego (<=17-Nov). Compara DataFrames completos (equals), F5_0 por (mid,k), contadores del hook, entradas `fills` y contadores del motor (bloq1). Nunca imprime EV/PnL: solo tiempos, igualdades y aciertos de cache.
Escribe out_rf5_ciego/rapido_DIA_GRUPO.json (grupo A: base,F3 + bloq1 F3; grupo K: K1,K6,CALMA + bloq1 K1 + K6 con Calma vacia == K1; dos procesos para acotar RAM) (y rapido_perfil_DIA.txt con 'perfil'). Se niega a correr dias >= 18-Nov."""
import sys, os, json, time, io
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; d = sys.argv[1]; GRUPO = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] in ('A', 'K') else 'A'
if d >= '2026-11-18': raise SystemExit('dia ciego: prohibido')
os.environ.setdefault('RF5_OUT', HV + 'out_rf5_ciego/'); sys.path.insert(0, HV)
import numpy as np, pandas as pd
import rf5_run as RR, rf5_core as K5, rf5_rapido as RP
import b_policy_sim as BS, eng_v5 as EV, sec7_core as C
cortes = K5.lee_cortes(); t_b = time.time(); E, info = EV.build(d); t_build = round(time.time() - t_b, 1); P = BS.params(); res = dict(dia=d, sha_rapido=None, build_E_s=t_build); tp = RR.t_proc(); bsrc = RR.FB.carga_binance(d) if GRUPO == 'K' else None
def corre(W, nombre, tabla, bs, lento, prof=None):
    if lento: os.environ['RF5_LENTO'] = '1'
    else: os.environ.pop('RF5_LENTO', None)
    ctx = dict(W=W, serie=W._serie); W.cont.clear(); t0 = time.time()      # contadores del MOTOR por replica (si no, la rapida acumula 2 pasadas frente a 1 de la lenta: falso 'distintos')
    if prof: prof.enable()
    R, cov, HK = RR._replay(d, P, W, ctx, nombre, tabla, bs, cortes, tp if bs else None, None)
    if prof: prof.disable()
    os.environ.pop('RF5_LENTO', None); HK._cm = dict(W.cont); return R, HK, round(time.time() - t0, 2)
def igual(A, B): return (len(A) == len(B)) and (len(A) == 0 or A.reset_index(drop=True).equals(B.reset_index(drop=True)))
if 'perfil' in sys.argv:
    import cProfile, pstats; pr = cProfile.Profile(); corre(C.EngineBloqueo(E, activo=False), 'base', K5.POLITICAS_A, None, True, pr); s = io.StringIO(); pstats.Stats(pr, stream=s).sort_stats('tottime').print_stats(18); open(HV + f'out_rf5_ciego/rapido_perfil_{d}.txt', 'w').write(s.getvalue())
res['sha_rapido'] = RP.carga_rapido().sha_rapido; Wr = RP.EngineBloqueoCache(E, activo=False); Ws = C.EngineBloqueo(E, activo=False); Wr._cache = Ws._cache; out = {}      # cache de series COMPARTIDA (memoria)
K6V = dict(K5.POLITICAS_K6); K6V['K6_calma_vacia'] = ('F3', True, True, 74, False, 300)
def casos():
    if GRUPO == 'A':
        for n in ('base', 'F3'): yield n, K5.POLITICAS_A, None
    else:
        yield 'K1', K5.POLITICAS_K, bsrc
        for n in ('K6', 'CALMA', 'K6_tq0'): yield n, K6V, bsrc      # K6_tq0 = sensibilidad tq = t (ESPEC_HOOK_CALMA_V4)
for nombre, tabla, bs in casos():
    import gc; gc.collect()
    Rs, HKs, ts_ = corre(Ws, nombre, tabla, bs, True); Rf, HKf, tf_ = corre(Wr, nombre, tabla, bs, False); Rc, HKc, tc_ = corre(Wr, nombre, tabla, bs, False)
    out[nombre] = dict(lenta_s=ts_, rapida_fria_s=tf_, rapida_caliente_s=tc_, ordenes=int(len(Rs)), igual_fria=bool(igual(Rs, Rf)), igual_caliente=bool(igual(Rs, Rc)), f5_igual=bool(HKs.f5_0 == HKf.f5_0 == HKc.f5_0), cont_igual=bool(dict(HKs.cont) == dict(HKf.cont) == dict(HKc.cont)), tau_igual=bool(HKs.tau == HKf.tau == HKc.tau))
del Ws, Wr; import gc; gc.collect(); n1, t1, b1 = ('F3', K5.POLITICAS_A, None) if GRUPO == 'A' else ('K1', K5.POLITICAS_K, bsrc)
Wb = C.EngineBloqueo(E, activo=True); Wbr = RP.EngineBloqueoCache(E, activo=True); Wbr._cache = Wb._cache; Rs, HKs, ts_ = corre(Wb, n1, t1, b1, True); Rf, HKf, tf_ = corre(Wbr, n1, t1, b1, False); Rc, HKc, tc_ = corre(Wbr, n1, t1, b1, False)
out['bloq1_' + n1] = dict(lenta_s=ts_, rapida_fria_s=tf_, rapida_caliente_s=tc_, igual_fria=bool(igual(Rs, Rf)), igual_caliente=bool(igual(Rs, Rc)), fills_igual=bool(Wb.fills == Wbr.fills), cont_motor_igual=bool(HKs._cm == HKf._cm == HKc._cm and len(HKs._cm) > 0))
del Wb, Wbr; gc.collect()
if GRUPO == 'K':          # K6 con Calma VACIA (sin saltos) == K1 bit a bit (misma politica con el componente Calma presente pero sin disparos)
    Wv = RP.EngineBloqueoCache(E, activo=False); vac = {c_: (np.array([], np.int64), np.array([])) for c_ in bsrc}
    Wv.fills.clear(); Rv, covv = RP.run_day(d, P, E=Wv, HK=K5.construye_hook('K6_calma_vacia', K6V, Wv._serie, bsrc, cortes, tp, lambda: Wv.fills, bsrc_calma=vac)); Wv.fills.clear(); R1, cov1 = RP.run_day(d, P, E=Wv, HK=K5.construye_hook('K1', K5.POLITICAS_K, Wv._serie, bsrc, cortes, tp, lambda: Wv.fills))
    cols = [c for c in Rv.columns if c in R1.columns]; out['k6_calma_vacia_vs_K1'] = dict(ordenes=int(len(Rv)), distintas_de_K1=bool(not igual(Rv[cols], R1[cols])) if len(Rv) == len(R1) else True)
res['pol'] = out; res['todo_igual'] = bool(all(v.get('igual_fria') and v.get('igual_caliente') and v.get('fills_igual', True) and v.get('cont_motor_igual', True) and v.get('f5_igual', True) and v.get('cont_igual', True) and v.get('tau_igual', True) for v in out.values() if 'igual_fria' in v) and not out.get('k6_calma_vacia_vs_K1', {}).get('distintas_de_K1', False)); res['grupo'] = GRUPO
json.dump(res, open(HV + f'out_rf5_ciego/rapido_{d}_{GRUPO}.json', 'w'), indent=1); print(json.dumps(res)[:3500])
