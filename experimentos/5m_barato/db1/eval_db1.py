#!/usr/bin/env python3
"""Evaluador forward de PREREG_DB1 (sha 1d12afa2f22a1bbb3ccece15b2aec01f437d86b7ef83f2a23479708e1197e998). Solo simulacion, 0 ordenes, SIN tocar engine.py/passT.py/rt_sim.py (los ejecuta passdb.py con sha comprobado).
Modos:
  --producir D [--quemado]   corre passdb.py dia D (nice 19, ionice 3, ulimit -v 3000000; BLOQUEADO 06:00-09:15Z y 22:15-22:30Z) -> out/RX_D.pkl + cov/excl/vida
  --aceptacion               sobre QUEMADOS 2026-10-26..11-04 (G0 n=2938, -166,9+-1, EV -0,076; CXJ150 dPnL +128+-1; igualdad exacta de rellenos con toxicidad_thru1/out) -> aceptacion.json
  --evaluar [--hoy D]        informe diario DESCRIPTIVO (dias validos desde 2026-11-10) + checkpoints 10 y 20 (sec. 5) -> estado_db1.json, informe_db1_<hoy>.txt. Exige aceptacion PASS con el sha actual
  --placebo CP ARM           (DB1|DB2) 99 semillas x dias del checkpoint CP (pesado: horas) y agrega -> placebo_db1_cp<CP>_<ARM>.json
Decide pnl SIN rebate (prereg sec. 1: el rebate se reporta aparte); la aceptacion usa pnl con rebate como el motor/thru1. Etiqueta maxima: CANDIDATO (EXPLORATORY hasta medicion L2). Nunca autoriza dinero real."""
import sys, os, re, json, hashlib, argparse, subprocess, datetime as dt, glob
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; Q11 = HERE + '../q11/'
sys.path.insert(0, HERE); sys.path.insert(0, Q11)
import numpy as np, pandas as pd
import eval_thru1 as E1, passdb as P
Q = E1.Q
OUT = HERE + 'out/'; PLA = HERE + 'placebo/'; PBD = E1.PB; DESDE = '2026-11-10'; TOPE = '2026-12-31'; CP20_NO_ANTES = '2026-11-30'
PREREG = '/root/polymarket-research/misiones/5m_barato/docs/PREREG_DB1.md'; PREREG_SHA = '1d12afa2f22a1bbb3ccece15b2aec01f437d86b7ef83f2a23479708e1197e998'
SEED = 20261110; B = 4000; QUEMADOS = E1.QUEMADOS
ARMS = {'DB1': dict(v='DB1_150', inv='INV1_150', pla='PDB1_150', desc=['DB1_300', 'DB1_1000']), 'DB2': dict(v='DB2_150', inv='INV2_150', pla='PDB2_150', desc=['DB2_300', 'DB2_1000'])}
RMR_ARMS = ['G0', 'DB1_150', 'DB2_150', 'DBU_150']
def sha_codigo(): return hashlib.sha256((P.sha_f(P.__file__) + P.sha_f(__file__)).encode()).hexdigest()
def hora_bloqueada(now=None):
    h = now or dt.datetime.now(dt.timezone.utc); m = h.hour * 60 + h.minute; return (360 <= m < 555) or (1335 <= m < 1350)
def nr(x): return x.assign(pnl=x.pnl_nr) if len(x) else x      # decisiones SIN rebate
def V(R, name): return R[R['var'] == name]
def cargar(dias, d_out=None):
    d_out = d_out or OUT; fr = [pd.read_pickle(d_out + f'RX_{d}.pkl') for d in dias]
    for d, x in zip(dias, fr):
        if len(x) and (x['dia'].astype(str) != d).any(): raise ValueError(f'RX_{d}: filas con dia != {d}')
    return pd.concat(fr, ignore_index=True) if fr else pd.DataFrame()
def atomic(path, text): E1.atomic(path, text)
def fechas(desde, hasta): return [(pd.Timestamp(desde) + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in range((pd.Timestamp(hasta) - pd.Timestamp(desde)).days + 1)]
# ---------------------------------------------------------------- produccion / checkpoint durable
def tiene_insumos(d):
    sys.path.insert(0, Q11 + 'barrido_multi'); import bfeat
    return [n for n, ok in (('tape', os.path.exists(PBD + f'tape_{d}.pkl')), ('bad', os.path.exists(PBD + f'bad_{d}.json')), ('x_binance', bool(bfeat.xfile(d))),
                            ('ms_npz', os.path.exists(P.DL + f'sa_ms/ms_{d}.npz'))) if not ok]
def producir(d, quemado=False, ahora=None):
    if hora_bloqueada(ahora): raise SystemExit('BLOQUEADO: no se lanza trabajo pesado entre 06:00-09:15Z ni 22:15-22:30Z')
    if os.path.exists(OUT + f'RX_{d}.pkl'): print('ya', d); return 0
    falta = tiene_insumos(d)
    if falta: raise SystemExit('PENDIENTE: faltan ' + ','.join(falta))
    t0 = dt.datetime.now(dt.timezone.utc); os.makedirs(OUT, exist_ok=True)
    r = subprocess.run(['nice', '-n', '19', 'ionice', '-c3', 'bash', '-c', f'ulimit -v 3000000; export OMP_NUM_THREADS=1; cd {HERE} && python3 -I passdb.py dia {d}'], capture_output=True, text=True)
    open(OUT + 'produccion.log', 'a').write(f'=== {t0:%FT%TZ} dia {d} rc={r.returncode}\n{r.stdout}{r.stderr}\n')
    if r.returncode: raise SystemExit(f'FALLO ({r.returncode}) passdb dia {d}: {r.stderr[-400:]}')
    ck = leer_json(HERE + 'checkpoint_db1.json', {}); cov = leer_json(OUT + f'cov_{d}.json', {})
    ck[d] = dict(rx_sha=P.sha_f(OUT + f'RX_{d}.pkl'), code_sha=sha_codigo(), cobertura_desenlace=cov.get('cobertura_desenlace'), binance_cobertura_min=(cov.get('binance') or {}).get('cobertura_min'), hecho=f'{dt.datetime.now(dt.timezone.utc):%FT%TZ}')
    atomic(HERE + 'checkpoint_db1.json', json.dumps(ck, indent=1, default=float)); print(r.stdout[-300:]); return 0
def leer_json(p, defecto):
    try: return json.load(open(p))
    except Exception: return defecto
# ---------------------------------------------------------------- validez de dia (sec. 4)
def dia_valido(d, hoy=None, ahora=None):
    """-> dict(dia, valido_db1, valido_db2, en_curso/pendiente, motivo). Cache definitiva validez_<D>.json solo para dias cerrados, asentados y con RX/cov."""
    hoy = hoy or Q.hoy_utc(); cache = OUT + f'validez_{d}.json'
    if d >= hoy: return dict(dia=d, valido_db1=False, valido_db2=False, en_curso=True, motivo='EN CURSO')
    c = leer_json(cache, None)
    if c and c.get('prereg_sha') == PREREG_SHA: return c
    falta = tiene_insumos(d) + ([] if os.path.exists(OUT + f'RX_{d}.pkl') and os.path.exists(OUT + f'cov_{d}.json') else ['RX/cov'])
    if falta: return dict(dia=d, valido_db1=False, valido_db2=False, pendiente=True, motivo='PENDIENTE: faltan ' + ','.join(falta))
    ahora = ahora or pd.Timestamp.now(tz='UTC'); ok, why = E1.asentado(d, _xpath(d), PBD + f'bad_{d}.json', ahora)
    if not ok: return dict(dia=d, valido_db1=False, valido_db2=False, pendiente=True, motivo='PENDIENTE: dia ' + why)
    cov = json.load(open(OUT + f'cov_{d}.json')); bn = cov['binance']; mot = []
    if not bn['valido']: mot.append(bn['motivo'])
    cd = cov['cobertura_desenlace']
    if not (cd == cd and cd >= 0.98): mot.append(f'desenlace oficial {cd} < 0,98')
    v1 = not mot; lp = cov['lado_print']; mot2 = list(mot) + ([] if lp['valido'] else [lp['motivo']])
    r = dict(dia=d, prereg_sha=PREREG_SHA, valido_db1=v1, valido_db2=bool(v1 and lp['valido']), motivo='; '.join(mot2), cobertura_desenlace=cd, binance_min=bn['cobertura_min'], concordancia_lado=lp.get('concordancia'), horas_excluidas=bn['horas_excluidas'])
    atomic(cache, json.dumps(r, indent=1, default=float)); return r
def _xpath(d):
    sys.path.insert(0, Q11 + 'barrido_multi'); import bfeat; return bfeat.xfile(d)
# ---------------------------------------------------------------- aceptacion
def aceptacion(salida=None):
    salida = salida or HERE + 'aceptacion.json'; falta = [d for d in QUEMADOS if not os.path.exists(OUT + f'RX_{d}.pkl')]
    if falta: r = dict(pass_=False, motivo='faltan RX de quemados: ' + ','.join(falta)); atomic(salida, json.dumps(r, indent=1)); return r
    R = cargar(QUEMADOS); g0 = V(R, 'G0'); cx = V(R, 'CXJ150'); ev = float(g0.pnl.sum() / g0.cost.sum()); dcx = float(E1.dser(cx, g0).sum())
    ref = pd.concat([pd.read_pickle(E1.TX + f'RT_{d}.pkl') for d in QUEMADOS], ignore_index=True); difs = {}
    for v in ('G0', 'CXJ150'):
        a = V(R, v)[['k', 'L', 'tf', 'q']].round(6).sort_values(['k', 'L', 'tf', 'q']).reset_index(drop=True); b = ref[ref['var'] == v][['k', 'L', 'tf', 'q']].round(6).sort_values(['k', 'L', 'tf', 'q']).reset_index(drop=True)
        difs[v] = int(len(a) != len(b) or not a.equals(b))
    chk = {'G0 n=2938': len(g0) == 2938, 'G0 pnl -166,9+-1': abs(float(g0.pnl.sum()) + 166.9) <= 1.0, 'G0 EV -0,076': round(ev, 3) == -0.076, 'dPnL CXJ150 +128+-1': abs(dcx - 128.0) <= 1.0,
           'G0 igual a toxicidad_thru1/out (fila a fila)': difs['G0'] == 0, 'CXJ150 igual a toxicidad_thru1/out (fila a fila)': difs['CXJ150'] == 0}
    desc = {}
    for a, c in ARMS.items():
        for f in ('BASE', 'CROSS'):
            n = c['v'] if f == 'BASE' else c['v'] + '@CROSS'; g = g0 if f == 'BASE' else V(R, 'G0@CROSS'); x = V(R, n)
            desc[f'{a}_{f}'] = dict(dpnl_con_rebate=float(E1.dser(x, g).sum()), dpnl_sin_rebate=float(E1.dser(nr(x), nr(g)).sum()), n_arm=len(x), n_g0=len(g))
    r = dict(pass_=all(chk.values()), checks=chk, valores=dict(g0_n=len(g0), g0_pnl=float(g0.pnl.sum()), g0_ev=ev, d_cxj150=dcx), descriptivo_quemados_NO_DECIDE=desc, code_sha=sha_codigo(), fecha=Q.hoy_utc(), dias=QUEMADOS)
    atomic(salida, json.dumps(r, indent=1, default=float)); return r
def aceptacion_ok():
    a = leer_json(HERE + 'aceptacion.json', {}); return bool(a.get('pass_') and a.get('code_sha') == sha_codigo()), a
# ---------------------------------------------------------------- metricas de un brazo
def pasa_ic(r, i=0): return bool(r['ic_d'][i] == r['ic_d'][i] and r['ic_d'][i] > 0 and r['ic_c'][i] == r['ic_c'][i] and r['ic_c'][i] > 0)
def franja(L): return '0,05-0,15' if L < 0.15 else ('0,15-0,25' if L < 0.25 else '0,25-0,35')
def metricas(R, arm, days):
    c = ARMS[arm]; g0 = nr(V(R, 'G0')); x = nr(V(R, c['v'])); g0c = nr(V(R, 'G0@CROSS')); xc = nr(V(R, c['v'] + '@CROSS')); out = dict(arm=arm, dias=days, nd=len(days))
    out['base'] = E1.stats_dpnl(x, g0, days); out['cross'] = E1.stats_dpnl(xc, g0c, days) if len(xc) or len(g0c) else None
    out['otras_cotas'] = {f: float(E1.dser(nr(V(R, c['v'] + '@' + f)), nr(V(R, 'G0@' + f))).sum()) for f in ('STRICT', 'OPT', 'THIN')}
    out['dpnl_con_rebate'] = float(E1.dser(V(R, c['v']), V(R, 'G0')).sum()); out['inv'] = float(E1.dser(nr(V(R, c['inv'])), g0).sum())
    out['n_g0'] = len(g0); out['n_arm'] = len(x); ka = set(zip(x.k, x.L.round(2), x.tf)); rem = g0[[(k, l, t) not in ka for k, l, t in zip(g0.k, g0.L.round(2), g0.tf)]]
    out['quitados'] = len(rem); out['quitados_buenos_n'] = int((rem.gana == 1).sum()); out['quitados_malos_n'] = int((rem.gana == 0).sum())
    out['quitados_buenos_pnl'] = float(rem[rem.gana == 1].pnl.sum()); out['quitados_malos_pnl'] = float(rem[rem.gana == 0].pnl.sum())
    out['ev_g0_por_eur'] = float(g0.pnl.sum() / g0.cost.sum()) if len(g0) else float('nan'); out['ev_arm_por_eur'] = float(x.pnl.sum() / x.cost.sum()) if len(x) else float('nan')
    out['ev_arm_por_unidad'] = float((x.pnl / x.cost).mean()) if len(x) else float('nan'); out['rebate_arm'] = float(V(R, c['v']).reb.sum()); out['rebate_g0'] = float(V(R, 'G0').reb.sum())
    dim = {}
    for nm, col, vals in (('moneda', 'act', ('ETH', 'SOL', 'XRP')), ('lado', 'lado', ('YES', 'NO'))): dim[nm] = {v: float(E1.dser(x[x[col] == v], g0[g0[col] == v]).sum()) for v in vals}
    fr = lambda df: df.L.map(franja); dim['franja_L'] = {v: float(E1.dser(x[fr(x) == v], g0[fr(g0) == v]).sum()) for v in ('0,05-0,15', '0,15-0,25', '0,25-0,35')}; out['dim'] = dim
    vid = {}
    for d in days:
        for k_, v in leer_json(OUT + f'vida_{d}.json', {}).items(): vid[k_] = vid.get(k_, 0) + v
    out['tiempo_quitado'] = (1 - vid.get(c['v'], 0) / vid['G0']) if vid.get('G0') else float('nan')
    out['coin_pos_max'] = max_coin_share(dim['moneda']); return out
def max_coin_share(by):
    pos = {k: v for k, v in by.items() if v > 0}; tot = sum(pos.values()); return (max(pos.values()) / tot) if tot > 0 else float('nan')
def rmr(R):
    out = {}; g0e = None
    for v in RMR_ARMS:
        x = V(R, v); b = x[x.burst]; out[v] = dict(n=int(len(b)), eur=float(b.cost.sum()), pnl=float(b.pnl_nr.sum()), n_todos=int(len(x)), conocido=float(x.burst_known.mean()) if len(x) else float('nan'))
    g = out['G0']['eur']
    for v in RMR_ARMS[1:]: out[v]['fraccion_cancelable'] = (1 - out[v]['eur'] / g) if g > 0 else float('nan')
    return out
def markout_salida(R, arms=('G0', 'DB1_150', 'DB2_150', 'DBU_150')):
    """precision/recobrado del marcador ex ante (markout del mid de L <= -2c a +1/+5/+30 s) contra perder (contable) y valor de salida (vender a tf+delta - mantener) sobre los rellenos residuales."""
    o = {}
    for v in arms:
        x = V(R, v); r = {}
        for h in ('mk1', 'mk5', 'mk30'):
            m = x[h] <= -0.02; perd = x.gana == 0
            r[h] = dict(marcados=int(m.sum()), precision=float((m & perd).sum() / m.sum()) if m.sum() else float('nan'), recobrado=float((m & perd).sum() / perd.sum()) if perd.sum() else float('nan'))
        r['salida'] = {s: dict(todos=float(x[s].sum()), marcados_mk1=float(x[x.mk1 <= -0.02][s].sum()), marcados_mk5=float(x[x.mk5 <= -0.02][s].sum())) for s in ('sv150', 'sv500', 'sv1000')}; o[v] = r
    return o
def pvalor(d_obs, perm):
    m = float(np.mean(perm)); p = (1 + sum(abs(x - m) >= abs(d_obs - m) for x in perm)) / (len(perm) + 1); return m, float(p)
def agregar_placebo(cp, arm, days, R=None):
    c = ARMS[arm]; R = R if R is not None else cargar(days); g0 = nr(V(R, 'G0')); d_obs = float(E1.dser(nr(V(R, c['v'])), g0).sum()); perm = []
    for s in range(1, 100):
        Pp = pd.concat([pd.read_pickle(PLA + f's{s}/out/RX_{d}.pkl') for d in days], ignore_index=True); perm.append(float(E1.dser(nr(V(Pp, c['pla'])), g0).sum()))
    m, p = pvalor(d_obs, perm); r = dict(arm=arm, cp=cp, dias=list(days), d_obs=d_obs, m=m, p=p, n_semillas=len(perm), perm=perm)
    atomic(HERE + f'placebo_db1_cp{cp}_{arm}.json', json.dumps(r, indent=1)); return r
def placebo(cp, arm, days):
    if hora_bloqueada(): raise SystemExit('BLOQUEADO: horario')
    for s in range(1, 100):
        for d in days:
            if os.path.exists(PLA + f's{s}/out/RX_{d}.pkl'): continue
            r = subprocess.run(['nice', '-n', '19', 'ionice', '-c3', 'bash', '-c', f'ulimit -v 3000000; export OMP_NUM_THREADS=1; cd {HERE} && python3 -I passdb.py placebo {d} {s}'], capture_output=True, text=True)
            if r.returncode: raise SystemExit(f'FALLO placebo s{s} {d}: {r.stderr[-300:]}')
    return agregar_placebo(cp, arm, days)
# ---------------------------------------------------------------- veredicto de checkpoint (sec. 5)
def veredicto_cp(m, cp, pl, inv_m):
    """-> (etiqueta, dict de criterios). m = metricas; pl = placebo json o None; inv_m = media del placebo (m del json) para C7."""
    b = m['base']; c = {}; nd = m['nd']; dd = list(b['dias'].values())
    if nd <= 2 or b['ncierres'] < 3 or b['tot'] != b['tot']: return 'INSUFFICIENT', {'motivo': 'NaN, <3 cierres o <=2 dias validos'}
    if b['tot'] <= 0: return 'REFUTA', {'motivo': f"dPnL BASE {b['tot']:+.2f} <= 0 en checkpoint {cp} con {nd} dias validos"}
    c['C1'] = nd >= 10 and m['n_g0'] >= 300 and m['quitados'] >= 40
    c['C2'] = b['tot'] > 0 and pasa_ic(b, 0); c['C3'] = bool(m['cross'] and m['cross']['tot'] > 0); c['C4'] = bool(b['sin2dias'] == b['sin2dias'] and b['sin2dias'] > 0)
    c['C5'] = bool(nd >= 10 and 5 * sum(1 for v in dd if v > 0) >= 3 * nd)
    c['C6'] = bool(pl and pl['p'] <= 0.10 and pl['d_obs'] > pl['m']); c['C7'] = bool(pl and m['inv'] <= pl['m'])
    c['C8'] = bool(m['coin_pos_max'] == m['coin_pos_max'] and m['coin_pos_max'] <= 0.70); yes, no = m['dim']['lado']['YES'], m['dim']['lado']['NO']; c['C9'] = bool(yes > 0 and no > 0)
    if cp == 20:
        a1, a2 = np.mean(dd[:10]), np.mean(dd[10:20]); c['C10'] = bool(not (a2 < 0.5 * a1)) if a1 > 0 else True
    cand = all(c.values()); et = 'CANDIDATO (EXPLORATORY hasta medicion L2)' if cand else 'NO CANDIDATO'
    if not c['C9'] and all(v for k, v in c.items() if k != 'C9'): et = 'NO CANDIDATO: NO SEPARABLE DEL REGIMEN (C9)'
    if pl is None: et = 'NO CANDIDATO (placebo no calculado)'
    if cp == 20:
        if not cand: return 'REFUTA', dict(c, motivo='checkpoint 20 sin CANDIDATO')
        prom = pl is not None and pl['p'] <= 0.05 and b['ic_d'][2] > 0 and b['ic_c'][2] > 0; c['PROMOCION'] = bool(prom)
        if prom: et = 'CANDIDATO + PROMOCION: propuesta de prereg de micro-real (wallet dedicada <=5 EUR, /code-review medium, OK de Javi); NUNCA dinero real directo'
    return et, c
# ---------------------------------------------------------------- informe
def fmt_arm(m, rm=None):
    b = m['base']; x = m['cross']; L = []
    L.append(f"[{m['arm']}] dias {m['nd']} | G0 n={m['n_g0']} arm n={m['n_arm']} quitados={m['quitados']} (buenos {m['quitados_buenos_n']} pnl {m['quitados_buenos_pnl']:+.1f} / malos {m['quitados_malos_n']} pnl {m['quitados_malos_pnl']:+.1f}); tiempo de cotizacion quitado {m['tiempo_quitado']:.3f}")
    L.append(f"   dPnL BASE {b['tot']:+.2f} (n cierres {b['ncierres']}, no nulos {b['nnz']}) IC90 cierre ({b['ic_c'][0]:+.2f},{b['ic_c'][1]:+.2f}) IC90 dia ({b['ic_d'][0]:+.2f},{b['ic_d'][1]:+.2f}); sin 2 mejores dias {b['sin2dias']:+.2f}; sin 5 mejores cierres {b['sin5cierres']:+.2f}")
    if x: L.append(f"   dPnL CROSS {x['tot']:+.2f} IC90 cierre ({x['ic_c'][0]:+.2f},{x['ic_c'][1]:+.2f}) dia ({x['ic_d'][0]:+.2f},{x['ic_d'][1]:+.2f}); STRICT/OPT/THIN {m['otras_cotas']['STRICT']:+.2f}/{m['otras_cotas']['OPT']:+.2f}/{m['otras_cotas']['THIN']:+.2f}; con rebate (aparte) BASE {m['dpnl_con_rebate']:+.2f}")
    L.append(f"   EV por EUR (Σpnl/Σcoste, sin rebate): G0 {m['ev_g0_por_eur']:+.3f} -> arm {m['ev_arm_por_eur']:+.3f}; EV por unidad arm {m['ev_arm_por_unidad']:+.3f}; rebate arm {m['rebate_arm']:+.2f} / G0 {m['rebate_g0']:+.2f}")
    L.append(f"   por moneda {fmt_d(m['dim']['moneda'])} | por lado {fmt_d(m['dim']['lado'])} | por franja L {fmt_d(m['dim']['franja_L'])} | mayor moneda del dPnL positivo {m['coin_pos_max']:.2f} | inversion dPnL {m['inv']:+.2f}")
    L.append('   dPnL por dia: ' + ' '.join(f"{d[5:]}:{v:+.1f}" for d, v in b['dias'].items())); return L
def fmt_d(d): return ' '.join(f'{k}:{v:+.1f}' for k, v in d.items())
def informe(hoy, a):
    L = [f'# INFORME DIARIO PREREG_DB1 (DESCRIPTIVO; veredicto solo en checkpoints) generado {dt.datetime.now(dt.timezone.utc):%FT%TZ} | hoy={hoy} | codigo {sha_codigo()[:12]} | prereg {PREREG_SHA[:8]}']
    ok, ac = aceptacion_ok(); est = leer_json(HERE + 'estado_db1.json', {'cp': {}, 'terminal': {}}); cand = [d for d in fechas(DESDE, hoy) if d < hoy and d <= TOPE]
    V_ = {d: dia_valido(d, hoy) for d in cand}; cob = {d: ('valido_db1' if v['valido_db1'] else ('pendiente' if v.get('pendiente') else 'NO VALIDO')) + ('+db2' if v['valido_db2'] else '') for d, v in V_.items()}
    L.append(f'Dias candidatos {len(cand)}: ' + ', '.join(f'{d}={cob[d]}' for d in cand)); [L.append(f"  {d}: {v['motivo']}") for d, v in V_.items() if v['motivo'] and not v.get('en_curso')]
    if not ok: L.append(f"INSUFFICIENT (motivo ACEPTACION): aceptacion sobre quemados {'no pasa' if ac else 'no ejecutada'} o sha de codigo distinto ({ac.get('motivo','') if ac else ''}); los dias se acumulan sin evaluarse"); return L, 'INSUFFICIENT'
    estado = 'OK'
    for arm in ARMS:
        days = [d for d in cand if V_[d]['valido_db2' if arm == 'DB2' else 'valido_db1']]; nd = len(days)
        if nd == 0: L.append(f'[{arm}] INSUFFICIENT: 0 dias validos'); continue
        R = cargar(days); m = metricas(R, arm, days); L += fmt_arm(m)
        rm = rmr(R); L.append('   RMR (rellenos de rafaga residuales; sec. 6): ' + ' | '.join(f"{v}: n {x['n']} / {x['n_todos']} EUR {x['eur']:.1f} pnl {x['pnl']:+.1f}" + (f" cancelable {x['fraccion_cancelable']:.2f}" if 'fraccion_cancelable' in x else '') + f" (rafaga conocida {x['conocido']:.2f})" for v, x in rm.items()))
        ms = markout_salida(R)
        for v in ('G0', ARMS[arm]['v']):
            r = ms[v]; L.append(f"   marcador ex ante {v}: " + ' '.join(f"{h}: marc {r[h]['marcados']} prec {r[h]['precision']:.2f} recob {r[h]['recobrado']:.2f}" for h in ('mk1', 'mk5', 'mk30')) + ' | salida (Δpnl vs mantener, todos/marc mk1) ' + ' '.join(f"{s}:{r['salida'][s]['todos']:+.1f}/{r['salida'][s]['marcados_mk1']:+.1f}" for s in ('sv150', 'sv500', 'sv1000')))
        for cp_ in (10, 20):
            key = f'{arm}_cp{cp_}'
            if key in est['terminal']: L.append(f'   CHECKPOINT {cp_} ya decidido: {est["terminal"][key]}'); continue
            if nd < cp_ or (cp_ == 20 and hoy < CP20_NO_ANTES): continue
            dcp = days[:cp_]; Rc = cargar(dcp); mc = metricas(Rc, arm, dcp); plj = leer_json(HERE + f'placebo_db1_cp{cp_}_{arm}.json', None)
            if plj and plj.get('dias') != dcp: plj = None
            et, crit = veredicto_cp(mc, cp_, plj, None)
            L.append(f'   >>> CHECKPOINT {cp_} {arm} (primeros {cp_} dias validos {dcp[0]}..{dcp[-1]}): {et} | criterios {crit}')
            if et == 'REFUTA' or (plj is not None and not et.startswith('INSUFFICIENT')):
                est['terminal'][f'{arm}_cp{cp_}'] = dict(etiqueta=et, criterios=crit, dias=dcp, decidido=f'{dt.datetime.now(dt.timezone.utc):%FT%TZ}', codigo=sha_codigo())
            else: L.append(f'   (placebo pendiente: python3 -I eval_db1.py --placebo {cp_} {arm}; REFUTA no lo necesita)')
    if hoy > TOPE: L.append(f'TOPE {TOPE}: sin checkpoint 20 => INSUFFICIENT')
    L.append('Nota: techo de etiqueta sin L2 = CANDIDATO (EXPLORATORY hasta medicion L2). Si DB1 y CXJ150 (PREREG_Q11_THRU1_FWD) pasan a la vez: UN solo hallazgo, nunca sumados.')
    atomic(HERE + 'estado_db1.json', json.dumps(est, indent=1, default=float)); return L, estado
def evaluar(a):
    hoy = a.hoy or Q.hoy_utc(); t0 = dt.datetime.now(dt.timezone.utc)
    L, st = informe(hoy, a); txt = '\n'.join(L); atomic(HERE + 'ultimo_informe.txt', txt + '\n'); atomic(HERE + f'informe_db1_{hoy}.txt', txt + '\n'); print(txt)
    atomic(HERE + 'manifest_db1.json', json.dumps(dict(job='db1_forward_diario', prereg=PREREG, prereg_sha=PREREG_SHA, code_sha=sha_codigo(), engine_sha=P.SHA['ENG'], passT_sha=P.SHA['PT'], rt_sim_sha=P.SHA['RT'], hoy=hoy, inicio=f'{t0:%FT%TZ}',
        fin=f'{dt.datetime.now(dt.timezone.utc):%FT%TZ}', estado=('COMPLETE' if st == 'OK' else 'PARTIAL'), motivo=st, dias_con_RX=sorted(os.path.basename(f)[3:13] for f in glob.glob(OUT + 'RX_*.pkl')),
        reproducir='python3 -I experimentos/5m_barato/db1/eval_db1.py --evaluar'), indent=1))
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--producir'); ap.add_argument('--quemado', action='store_true'); ap.add_argument('--aceptacion', action='store_true'); ap.add_argument('--evaluar', action='store_true')
    ap.add_argument('--placebo', nargs=2, metavar=('CP', 'ARM')); ap.add_argument('--hoy', default=None); a = ap.parse_args()
    if a.aceptacion: r = aceptacion(); print(json.dumps(r, indent=1, default=float)); sys.exit(0 if r['pass_'] else 2)
    elif a.evaluar: evaluar(a)
    elif a.producir: sys.exit(producir(a.producir, a.quemado))
    elif a.placebo:
        cp, arm = int(a.placebo[0]), a.placebo[1]; hoy = a.hoy or Q.hoy_utc()
        days = [d for d in fechas(DESDE, hoy) if d < hoy and dia_valido(d, hoy)['valido_db2' if arm == 'DB2' else 'valido_db1']][:cp]; assert len(days) == cp, f'solo {len(days)} dias validos'; placebo(cp, arm, days)
    else: ap.print_help()
