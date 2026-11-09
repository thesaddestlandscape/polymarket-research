"""Pruebas de q11_decision / eval_thru1 (ADDENDUM3 sha c991602c + ADDENDUM4 sha 3dac1bf4). Uso: python3 -I test_q11_decision.py
Cubre: filas A-H de ADDENDUM4 sec. 4 (una prueba por fila), incoherencias a1-a3 de sec. 5, ERROR_DATOS+terminal (5b), R1-R3, IC90 por dia con semillas,
corte de dias en el tope, racha, estado atomico/corrupto, evaluar_par sintetico. UNITARIOS PUROS (datos sinteticos, sin pickles de dev): la ACEPTACION sobre quemados
(G0 2938, thru1, GEO6, CXJ150, SOL013) esta en test_q11_aceptacion.py."""
import sys, os, json, tempfile, copy, subprocess
sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/forward_sol013/'); sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/q11/')
import numpy as np, pandas as pd, q11_decision as Q
E0 = {'racha': 0, 'last_nd': 0, 'terminal': None}
V = lambda st=E0, err=(), nvalid=10, nd=10, confirma=False, refuta=False, hoy='2026-11-20': Q.veredicto(st, list(err), nvalid, nd, confirma, refuta, hoy)
TERM = lambda v, f='2026-11-20', nd=12: {'racha': 0, 'last_nd': nd, 'terminal': {'veredicto': v, 'fecha': f, 'nd': nd}}
n_ok = 0
def ok(c, msg):
    global n_ok
    if not c: raise AssertionError(msg)
    n_ok += 1
# ---------- utilidades ----------
ok(Q.ok60(6, 10) and not Q.ok60(5, 10) and not Q.ok60(6, 9) and Q.ok60(12, 20) and not Q.ok60(11, 20), 'test entero 60 %')
ok(Q.TOPE == '2026-12-31' and Q.EJEC_CIERRE == '2027-01-01', 'constantes de tope')
ok(Q.SEEDS_DIA == {'SOL013': 20261113, 'P-A': 20261114, 'P-B': 20261115, 'P-C': 20261116, 'thru1': 20261107}, 'semillas ADDENDUM4 sec. 2')
# ---------- tabla ADDENDUM4 sec. 4: una prueba por fila ----------
for v in ('CONFIRMA_FINAL', 'REFUTA', 'REFUTED', 'CERRADO_INSUFFICIENT'):                       # A: terminal se mantiene aunque ahora todo diga otra cosa
    t, w, s = V(TERM(v), nd=15, confirma=True, refuta=True, hoy='2027-02-01'); ok(t == v and s['terminal']['veredicto'] == v, f'A {v}')
t, w, s = V(E0, err=['dec2_2026-11-07.pkl: filas con dia != 2026-11-07'], confirma=True, refuta=True); ok(t == 'INSUFFICIENT' and 'ERROR_DATOS' in w and s == E0, 'B error => INSUFFICIENT sin tocar estado')   # B
t, w, s = V(E0, nvalid=0, nd=0); ok(t == 'INSUFFICIENT' and s == E0, 'B 0 dias validos')
st3 = {'racha': 2, 'last_nd': 11, 'terminal': None}                                              # C: k=3 con nd<=20
t, w, s = V(st3, nd=12, confirma=True); ok(t == 'CONFIRMA_FINAL' and s['terminal']['nd'] == 12 and s['racha'] == 3, 'C CONFIRMA_FINAL')
t, w, s = V({'racha': 2, 'last_nd': 19, 'terminal': None}, nd=20, confirma=True); ok(t == 'CONFIRMA_FINAL', 'C con nd==20 y k=3 gana a D')
t, w, s = V(E0, nd=20); ok(t == 'REFUTED' and s['terminal']['veredicto'] == 'REFUTED', 'D nd>=20 => REFUTED')                  # D
t, w, s = V({'racha': 1, 'last_nd': 19, 'terminal': None}, nd=20, confirma=True); ok(t == 'REFUTED', 'D una racha en curso no lo evita')
t, w, s = V(E0, nd=25, confirma=True, refuta=True); ok(t == 'REFUTED', 'D antes que E')
t, w, s = V(E0, nd=10, refuta=True); ok(t == 'REFUTA' and s['terminal']['veredicto'] == 'REFUTA', 'E nd>=10 y R1-R3 => REFUTA')   # E
t, w, s = V(E0, nd=19, refuta=True); ok(t == 'REFUTA', 'E nd=19')
t, w, s = V(E0, nd=9, refuta=True); ok(t == 'INSUFFICIENT', 'E exige nd>=10 (H con nd<=9)')
t, w, s = V(E0, nd=11, hoy='2027-01-01'); ok(t == 'CERRADO_INSUFFICIENT' and s['terminal']['fecha'] == '2027-01-01', 'F fecha>=2027-01-01 y nd<20')   # F
t, w, s = V(E0, nd=11, hoy='2026-12-31'); ok(t == 'INSUFFICIENT', 'F no antes del 2027-01-01')
t, w, s = V({'racha': 0, 'last_nd': 10, 'terminal': None}, nd=11, confirma=True); ok(t == 'CONFIRMA' and s['racha'] == 1 and s['terminal'] is None, 'G CONFIRMA provisional 1/3')   # G
for kw in (dict(nd=9), dict(nd=2), dict(nd=1), dict(nd=12), dict(nd=15, refuta=False)):          # H: nd<=9; nd<=2; 10<=nd<=19 sin R3 (incluye NaN/minimos = refuta False)
    t, w, s = V(E0, **kw); ok(t == 'INSUFFICIENT' and s['terminal'] is None, f'H {kw}')
# ---------- incoherencias a1-a3 (ADDENDUM4 sec. 5a) de q11_decision.veredicto (sha a9ec3580) ----------
t, w, s = V(E0, nd=12, refuta=True, hoy='2027-01-01'); ok(t == 'REFUTA', 'a1: el 01-Ene un REFUTA cumplido con 10<=nd<=19 NO sale CERRADO_INSUFFICIENT')
t, w, s = V({'racha': 0, 'last_nd': 11, 'terminal': None}, nd=12, confirma=True, hoy='2027-01-01'); ok(t == 'CERRADO_INSUFFICIENT', 'a2: CONFIRMA provisional tras el tope cierra (no es absorbente)')
o = tempfile.mkdtemp() + '/'; mkp = lambda d: pd.DataFrame({'dia': [d], 'cost': [1.0], 'pnl': [0.1]})
for d in ('2026-12-30', '2026-12-31', '2027-01-01', '2027-01-02'): mkp(d).to_pickle(o + f'dec2_{d}.pkl'); mkp(d).to_pickle(o + f'dec3s100_{d}.pkl')
dias, _, _, err = Q.cargar_dias(o, '2026-11-06'); ok(dias == ['2026-12-30', '2026-12-31'] and not err, 'a2: dias cargados cortados en 2026-12-31')
dias, _, _, err = Q.cargar_dias(o, '2026-11-06', '2027-03-01'); ok(dias == ['2026-12-30', '2026-12-31'], 'a2: --hasta posterior no salta el tope')
t, w, s = V(E0, nd=24, confirma=False, refuta=False); ok(t == 'REFUTED', 'a3: nd>=20 con n<40/NaN (refuta=False) cae en REFUTED, no INSUFFICIENT para siempre')
# a3 a nivel evaluar_par: n(H)<40 con 20 dias comparables => REFUTED; y NaN/minimos nunca REFUTA con nd=12
def mkpar(ndias, nfill_H, evH_pos, ncierres_por_dia):
    rows = []; fin = 0
    for i in range(ndias):
        d = f'2026-11-{6 + i:02d}' if i < 25 else f'2026-12-{i - 24:02d}'
        for lado, nf in (('H', nfill_H), ('C', 4)):
            for j in range(nf):
                fin += 1 if (j % ncierres_por_dia == 0 or lado == 'C') else 0; rows.append((d, fin if lado == 'H' else 10 ** 6 + fin, 0.3 if (lado == 'H') == evH_pos else -0.3, 1.0, lado))
    x = pd.DataFrame(rows, columns=['dia', 'fin', 'pnl', 'cost', 'lado']); return x[x.lado == 'H'].drop(columns='lado'), x[x.lado == 'C'].drop(columns='lado'), sorted(x.dia.unique())
def ev_par(Hn, Cn, dias, hoy='2026-12-20'):
    p = tempfile.mkdtemp() + '/estado.json'; tok, L, inf = Q.evaluar_par('P-X', ('H', 'C'), Hn, Cn, dias, [], p, hoy, lambda ds: {}, None, 20261106, p_aplica=False, seed_dia=20261114)
    return tok, inf, json.load(open(p))
Hn, Cn, dd = mkpar(20, 1, True, 1); tok, inf, st = ev_par(Hn, Cn, dd); ok(inf['nd'] == 20 and not inf['refuta'] and tok == 'REFUTED', f'a3 evaluar_par nd=20, n(H)=20<40 => REFUTED ({tok})')
Hn, Cn, dd = mkpar(12, 4, True, 1); tok, inf, st = ev_par(Hn, Cn, dd); ok(inf['nd'] == 12 and inf['r123'] == {'R1': True, 'R2': True, 'R3': True} and tok == 'REFUTA' and st['terminal']['veredicto'] == 'REFUTA', f'E evaluar_par: EV_w(H)>0, n=48, cierres 48, IC por cierre y dia > 0 => REFUTA ({tok}, {inf["r123"]})')
Hn, Cn, dd = mkpar(12, 4, True, 4); tok, inf, st = ev_par(Hn, Cn, dd); ok(inf['r123']['R2'] is False and tok == 'INSUFFICIENT', f'R2: 48 fills pero 12 cierres (<25) => no REFUTA ({inf["r123"]})')
Hn, Cn, dd = mkpar(12, 4, False, 1); tok, inf, st = ev_par(Hn, Cn, dd); ok(inf['r123']['R3'] is False and tok not in ('REFUTA', 'REFUTED') and inf['confirma'] and tok == 'CONFIRMA', f'R3: EV_w(H)<0 (la hipotesis acierta) NUNCA refuta; con CONFIRMA cumplida da CONFIRMA provisional ({tok}); E y G disjuntas')
Hn, Cn, dd = mkpar(9, 6, True, 1); tok, inf, st = ev_par(Hn, Cn, dd); ok(inf['nd'] == 9 and tok == 'INSUFFICIENT' and inf['ic_dia'][0] != inf['ic_dia'][0], 'nd=9: IC por dia = NaN => sin REFUTA')
# ---------- ERROR_DATOS junto al terminal (5b): aviso, sin estado, EN REVISION solo si afecta a dias <= fecha del terminal ----------
t, w, s = V(TERM('CONFIRMA_FINAL', '2026-11-20'), err=['dec2_2026-11-15.pkl: filas con dia != 2026-11-15']); ok(t == 'CONFIRMA_FINAL [EN REVISION]' and 'ERROR_DATOS' in w and 'EN REVISION' in w and s['terminal']['veredicto'] == 'CONFIRMA_FINAL', '5b dia <= fecha => EN REVISION (terminal intacto)')
t, w, s = V(TERM('REFUTA', '2026-11-20'), err=['dec2_2026-11-25.pkl: filas con dia != 2026-11-25']); ok(t == 'REFUTA' and 'ERROR_DATOS' in w and 'EN REVISION' not in w, '5b error posterior al terminal: solo aviso')
t, w, s = V(TERM('REFUTED', '2026-11-20'), err=['mensaje sin fecha']); ok(t.endswith('[EN REVISION]'), '5b error sin fecha => fail-closed EN REVISION')
ok(Q.err_dias(['x dec3s100_2026-11-07.pkl: dia != 2026-11-07', 'sin']) == ['2026-11-07', None], 'err_dias')
sp = tempfile.mkdtemp() + '/e/estado.json'; Q.guardar_estado(sp, TERM('CONFIRMA_FINAL')); tok, w = Q.veredicto_sin_datos(sp, ['dec2_2026-11-07.pkl: x'], '2026-11-21'); ok(tok == 'CONFIRMA_FINAL [EN REVISION]' and Q.cargar_estado(sp)['terminal']['fecha'] == '2026-11-20', 'veredicto_sin_datos imprime el terminal y no reescribe el estado')
sp2 = tempfile.mkdtemp() + '/nada.json'; tok, w = Q.veredicto_sin_datos(sp2, [], '2026-11-21'); ok(tok == 'INSUFFICIENT' and not os.path.exists(sp2), 'veredicto_sin_datos sin estado: INSUFFICIENT y no crea fichero')
# ---------- R1-R3 ----------
nan = float('nan'); r = lambda *a: Q.refuta_r123(*a)
ok(r(40, 3, 40, 3, -0.2, (-0.5, -0.1), (-0.4, -0.05), 'neg')[0], 'SOL013: n=40, 3 cierres, EV<0, limites sup<0 => REFUTA')
ok(not r(39, 30, 40, 3, -0.2, (-0.5, -0.1), (-0.4, -0.05), 'neg')[0], 'R2 n<40')
ok(not r(50, 2, 40, 3, -0.2, (-0.5, -0.1), (-0.4, -0.05), 'neg')[0], 'R1 <3 cierres')
ok(not r(50, 30, 40, 3, -0.2, (-0.5, nan), (-0.4, -0.05), 'neg')[0] and not r(50, 30, 40, 3, nan, (-0.5, -0.1), (-0.4, -0.05), 'neg')[0] and not r(50, 30, 40, 3, -0.2, (-0.5, -0.1), (nan, nan), 'neg')[0], 'R1 NaN (IC cierre, EV, IC dia) => nunca REFUTA')
ok(not r(50, 30, 40, 3, -0.2, (-0.5, 0.02), (-0.4, -0.05), 'neg')[0] and not r(50, 30, 40, 3, -0.2, (-0.5, -0.1), (-0.4, 0.01), 'neg')[0], 'R3 exige AMBOS limites (cierre Y dia)')
ok(not r(50, 30, 40, 3, 0.2, (0.1, 0.5), (0.05, 0.4), 'neg')[0], 'SOL013 con EV>0 no refuta')
ok(r(48, 25, 40, 25, 0.2, (0.1, 0.5), (0.05, 0.4), 'pos')[0] and not r(48, 24, 40, 25, 0.2, (0.1, 0.5), (0.05, 0.4), 'pos')[0] and not r(48, 25, 40, 25, -0.2, (-0.5, -0.1), (-0.4, -0.05), 'pos')[0], 'P-A/B/C: EV_w(H)>0 con limites INFERIORES >0, >=25 cierres')
# ---------- IC90 por dia (sec. 2) ----------
rng = np.random.default_rng(7); xd = pd.DataFrame({'dia': [f'2026-11-{6 + i:02d}' for i in range(12) for _ in range(3)], 'pnl': rng.normal(0.1, 1, 36), 'cost': 1.0})
lo, hi = Q.ic_dia(xd, 20261113); g = xd.groupby('dia')[['pnl', 'cost']].sum(); idx = np.random.default_rng(20261113).integers(0, 12, (4000, 12)); rr = g.pnl.values[idx].sum(1) / g.cost.values[idx].sum(1)
ok(abs(lo - np.quantile(rr, .05)) < 1e-12 and abs(hi - np.quantile(rr, .95)) < 1e-12 and Q.ic_dia(xd, 20261113) == (lo, hi) and Q.ic_dia(xd, 20261114) != (lo, hi), 'ic_dia = cuantiles 0,05/0,95 de default_rng(semilla).integers(0, nd, (4000, nd)), ponderado por EUR')
ok(all(v != v for v in Q.ic_dia(xd[xd.dia.isin(g.index[:9])], 1)), 'ic_dia con <10 dias = NaN')
# ---------- racha / estado / cargar_dias / victoria estricta (heredado de ADDENDUM3) ----------
t, w, st1 = V(E0, nd=10, confirma=True); ok(t == 'CONFIRMA' and st1['racha'] == 1, 'racha 1')
t, w, st2 = V(st1, nvalid=11, nd=10, confirma=True); ok(st2['racha'] == 1, 'mismo nd: no alarga la racha')
t, w, st2 = V(st2, nvalid=11, nd=11, confirma=True); t, w, st4 = V(st2, nvalid=12, nd=12, confirma=True); ok(t == 'CONFIRMA_FINAL', 'racha 3 con nd creciente')
t, w, s = V(st1, nd=11, confirma=False); ok(s['racha'] == 0, 'rompe la racha si nd aumenta y no confirma')
d = tempfile.mkdtemp(); p = d + '/e/estado.json'; Q.guardar_estado(p, st4); ok(Q.cargar_estado(p)['terminal']['veredicto'] == 'CONFIRMA_FINAL' and not os.path.exists(p + '.tmp'), 'estado atomico round-trip')
open(p, 'w').write('{corrupto')
try: Q.cargar_estado(p); ok(False, 'estado corrupto aceptado')
except json.JSONDecodeError: ok(True, '')
mk = lambda rows: pd.DataFrame(rows, columns=['dia', 'fin', 'pnl', 'cost'])
A = mk([('d1', 1, 1.0, 1.0), ('d2', 2, 1.0, 1.0), ('d3', 3, 0.0, 0.0)]); B = mk([('d1', 1, 1.0, 1.0), ('d2', 2, 0.5, 1.0), ('d4', 4, 1.0, 1.0)])
Dc = sorted(Q.dias_relleno(A) & Q.dias_relleno(B)); eA, eB = Q.evdia(A), Q.evdia(B); ok(Dc == ['d1', 'd2'] and sum(eA[x] > eB[x] for x in Dc) == 1, 'victoria estricta (empate no es victoria; sin relleno no cuenta)')
o = tempfile.mkdtemp() + '/'; good = pd.DataFrame({'dia': ['2026-11-06'] * 2, 'cost': [1.0, 0.0], 'pnl': [0.1, 0.0]}); bad = good.assign(dia='2026-11-05')
good.to_pickle(o + 'dec2_2026-11-06.pkl'); good.to_pickle(o + 'dec3s100_2026-11-06.pkl'); good.to_pickle(o + 'dec2_2026-11-07.pkl'); bad.to_pickle(o + 'dec2_2026-11-08.pkl'); bad.to_pickle(o + 'dec3s100_2026-11-08.pkl')
dias, R2, R3, err = Q.cargar_dias(o, '2026-11-06'); ok(dias == ['2026-11-06', '2026-11-08'] and len(err) == 2 and len(R2) == 2, 'cargar_dias: dia != D => ERROR_DATOS; falta dec3s100 => no valido; cost 0 descartado')
# ---------- eval_thru1: REFUTA fuerte (sec. 3), motivo y ACEPTACION sobre quemados ----------
import eval_thru1 as E
res = lambda tot, cc, cd, nc, n: dict(dpnl=dict(tot=tot, ncierres=nc, ic_c=(0, cc, 0, 0), ic_d=(0, cd, 0, 0)), n_arm=n, conds={'C3 x': False, 'C7 y': False, 'C2 z': False})
ok(E.refuta_fuerte(res(-10, -1, -1, 50, 300))[0], 'thru1 REFUTA fuerte: dPnL<0, sup cierre<0, sup dia<0, >=300 rellenos')
for args, m in ((res(0, -1, -1, 50, 300), 'dPnL=0 (ya no refuta con <=0)'), (res(-10, 1, -1, 50, 300), 'IC cierre cruza 0'), (res(-10, -1, 1, 50, 300), 'IC dia cruza 0'), (res(-10, -1, -1, 2, 300), '<3 cierres'), (res(-10, -1, -1, 50, 299), '<300 rellenos'), (res(float('nan'), -1, -1, 50, 300), 'NaN')):
    ok(not E.refuta_fuerte(args)[0], 'thru1 NO refuta: ' + m)
ok('no identificado por el relleno' in E.motivo_refuted(res(-1, 1, 1, 50, 300)) and 'no separable del regimen' in E.motivo_refuted(res(-1, 1, 1, 50, 300)), 'motivo REFUTED')
# ---------- revision /code-review (09-Nov): fila B vs F, racha a la baja, cargar_dias canonico, PROMOCION congelada, sin sobrescribir ----------
t, w, s_ = V(E0, err=['dec2_2026-12-30.pkl: filas con dia != 2026-12-30'], nd=11, hoy='2027-01-01'); ok(t == 'INSUFFICIENT' and s_ == E0, 'fila B antes de F (literal ADDENDUM4): ERROR_DATOS con hoy>=2027-01-01 => INSUFFICIENT, no CERRADO (escenario absorbente documentado)')
t, w, s_ = V(E0, nvalid=0, nd=0, hoy='2027-02-01'); ok(t == 'INSUFFICIENT' and s_ == E0, 'fila B antes de F (literal): 0 dias validos con hoy>=2027-01-01 => INSUFFICIENT (absorbente)')
t, w, s_ = V(TERM('CERRADO_INSUFFICIENT', '2027-01-01'), err=['dec2_2026-12-30.pkl: x'], hoy='2027-01-02'); ok(t.startswith('CERRADO_INSUFFICIENT') and 'ERROR_DATOS' in w, 'terminal prevalece sobre ERROR_DATOS posterior')
# racha: invariante last_nd <= nd
t, w, s_ = V({'racha': 2, 'last_nd': 15, 'terminal': None}, nvalid=12, nd=12, confirma=True); ok(s_['racha'] == 0 and s_['last_nd'] == 12 and t == 'CONFIRMA' and 'racha reiniciada' in w, f'nd baja (15->12): racha reiniciada sin credito ({t}, {s_["racha"]})')
t, w, s_ = V(s_, nvalid=13, nd=13, confirma=True); ok(s_['racha'] == 1, 'tras la bajada, la racha vuelve a contar desde 1')
t, w, s_ = V({'racha': 2, 'last_nd': 15, 'terminal': None}, nvalid=12, nd=12, confirma=True, refuta=False); ok(t != 'CONFIRMA_FINAL', 'una bajada de nd no puede cerrar CONFIRMA_FINAL con la racha vieja')
# cargar_dias: patron canonico + sorted(set) + ambiguos
o = tempfile.mkdtemp() + '/'
for nm in ('dec2', 'dec3s100'): mkp('2026-11-10').to_pickle(o + f'{nm}_2026-11-10.pkl')
mkp('2026-11-10').to_pickle(o + 'dec2_2026-11-10_old.pkl'); mkp('2026-11-10').to_pickle(o + 'dec2_2026-11-10.pkl.bak.pkl'); mkp('2026-10-01').to_pickle(o + 'dec2_2026-10-01_x.pkl'); mkp('2026-11-10').to_pickle(o + 'dec2_sin_fecha.pkl')
dias, R2, R3, err = Q.cargar_dias(o, '2026-11-06'); ok(dias == ['2026-11-10'] and len(R2) == 1 and len(err) == 2 and all('no canonico' in e for e in err) and Q.err_dias(err) == ['2026-11-10', '2026-11-10'], f'cargar_dias: nombres extra que citan un dia de la ventana => ERROR_DATOS; fuera de ventana o sin fecha se ignoran ({err})')
t_, w_, _ = Q.veredicto(E0, err, 1, 1, False, False, '2026-11-20'); ok(t_ == 'INSUFFICIENT' and 'ERROR_DATOS' in w_, 'ese error entra por la fila B')
# PROMOCION congelada al emitir el terminal
Hn, Cn, dd = mkpar(12, 4, False, 1); sp = tempfile.mkdtemp() + '/estado.json'; Q.guardar_estado(sp, {'racha': 2, 'last_nd': 11, 'terminal': None})
ev1 = lambda H, C, d_: Q.evaluar_par('P-X', ('H', 'C'), H, C, d_, [], sp, '2026-11-25', lambda ds: {}, None, 20261106, p_aplica=False, seed_dia=20261114)
tok1, L1, inf1 = ev1(Hn, Cn, dd); st1 = Q.cargar_estado(sp); ok(tok1 == 'CONFIRMA_FINAL' and 'promocion_linea' in st1['terminal'], 'terminal CONFIRMA_FINAL emitido con PROMOCION guardada')
p1 = [x for x in L1 if x.startswith('PROMOCION')][0]; Hm = Hn.assign(pnl=Hn.pnl * 0.5 + 1.0); tok2, L2, inf2 = ev1(Hm, Cn, dd)   # datos distintos despues del terminal
p2 = [x for x in L2 if x.startswith('PROMOCION')][0]; ok(tok2 == 'CONFIRMA_FINAL' and p1 == p2 == st1['terminal']['promocion_linea'] and inf2['promocion'] == inf1['promocion'], 'PROMOCION no se recalcula tras el terminal')
# ERROR_DATOS/sin dias: los evaluadores NO sobrescriben el ultimo resultado valido (aviso en fichero aparte)
EVD = '/root/polymarket-research/experimentos/5m_barato/q11/'; FSOL = '/root/polymarket-research/misiones/5m_barato/forward_sol013/filtro_sol013.py'
od = tempfile.mkdtemp() + '/'; mkp('2026-11-12').assign(dia='2026-11-11').to_pickle(od + 'dec2_2026-11-12.pkl'); mkp('2026-11-12').assign(dia='2026-11-11').to_pickle(od + 'dec3s100_2026-11-12.pkl')
def corre(script, extra, salida, fich_valido):
    open(salida + '/' + fich_valido, 'w').write('VALIDO\n'); r = subprocess.run(['python3', '-I', script, '--desde', '2026-11-06', '--out', od, '--salida', salida, '--hoy', '2026-11-20'] + extra, capture_output=True, text=True); return r
for script, valido, aviso in ((FSOL, 'RESUMEN.md', 'AVISO_ultima_ejecucion.txt'), (EVD + 'eval_pistas.py', 'eval_pistas_resultado.txt', 'eval_pistas_AVISO.txt'), (EVD + 'eval_giro.py', 'eval_giro_resultado.txt', 'eval_giro_AVISO.txt')):
    sd = tempfile.mkdtemp(); r = corre(script, [], sd, valido); rv = open(sd + '/' + valido).read(); rv = rv.split('\n', 1)[1] if rv.startswith('> AVISO') else rv; ok(r.returncode == 0 and rv == 'VALIDO\n' and 'ERROR_DATOS' in open(sd + '/' + aviso).read(), f'{os.path.basename(script)}: ERROR_DATOS no sobrescribe {valido}; aviso en {aviso} ({r.stderr[-200:]})')
    ok(not any(f.startswith('estado_') for f in os.listdir(sd)), f'{os.path.basename(script)}: ERROR_DATOS no escribe estado')
# Chainlink ausente (dias sin CSV) = ERROR_DATOS en P-C y P-A (no filas descartadas), sin estado y sin sobrescribir
oc = tempfile.mkdtemp() + '/'; dc = '2026-12-15'
fila = pd.DataFrame({'dia': [dc] * 3, 'fin': [10, 11, 12], 'pnl': [0.1, -0.1, 0.2], 'cost': [1.0, 1.0, 1.0], 'var': ['T1'] * 3, 'lado': ['NO'] * 3, 'act': ['ETH'] * 3, 'lagj': [1000.0, 5000.0, 2000.0]})
fila.to_pickle(oc + f'dec2_{dc}.pkl'); fila.to_pickle(oc + f'dec3s100_{dc}.pkl')
for script, valido, aviso, marca in ((EVD + 'eval_giro.py', 'eval_giro_resultado.txt', 'eval_giro_AVISO.txt', 'sin cache ni CSV'), (EVD + 'eval_pistas.py', 'eval_pistas_resultado.txt', None, 'sin cache ni CSV')):
    sd = tempfile.mkdtemp(); open(sd + '/' + valido, 'w').write('VALIDO\n')
    r = subprocess.run(['python3', '-I', script, '--desde', '2026-11-06', '--out', oc, '--salida', sd, '--hoy', '2026-12-16', '--cl-cache', tempfile.mkdtemp() + '/c/'], capture_output=True, text=True)
    txt = open(sd + '/' + (aviso or valido)).read(); ok(r.returncode == 0 and 'ERROR_DATOS' in txt and marca in txt and not any(f.startswith('estado_P-A') or f.startswith('estado_P-C') for f in os.listdir(sd)), f'{os.path.basename(script)}: Chainlink ausente => ERROR_DATOS, sin estado ({r.stderr[-300:]})')
    if aviso: ok(open(sd + '/' + valido).read() == 'VALIDO\n', 'no sobrescribe el resultado valido')
# eval_giro: el rasgo de 5 h solo necesita el dia y el anterior (k=2 retirado)
ok("for k in (0, 1)})" in open(EVD + 'eval_giro.py').read(), 'eval_giro need = dia y dia-1')
# rt_cxj150_cross: argumentos validados
for bad in ('../x', '2026-13-45', 'foo'):
    r = subprocess.run(['python3', '-I', EVD + 'redteam/rt_cxj150_cross.py', bad], capture_output=True, text=True); ok(r.returncode == 2 and 'uso' in r.stderr, f'rt_cxj150_cross rechaza {bad!r}')
# ---------- 2a pasada /code-review: cache Chainlink, dias sin pareja, eval_sha, filtro con estado corrupto ----------
import hashlib, gzip
pr = tempfile.mkdtemp() + '/'; cc = tempfile.mkdtemp() + '/cache/'
def csvcl(dia, coins=('ETH', 'SOL', 'XRP'), n=3, gz=True):
    rows = ['timestamp_utc,asset,price_usd,source']
    for c in coins:
        for k in range(n): rows.append(f'{dia}T00:00:{k:02d}+00:00,{c},{100 + k},chainlink')
    rows.append(f'{dia}T00:00:09+00:00,ETH,1,pyth'); txt = '\n'.join(rows) + '\n'
    (gzip.open(pr + f'chainlink_{dia}.csv.gz', 'wt') if gz else open(pr + f'chainlink_{dia}.csv', 'w')).write(txt)
csvcl('2026-11-05'); ser, e = Q.cl_dia('2026-11-05', '2026-11-09', cc, pr); ok(e is None and set(ser) == set(Q.COINS) and len(ser['ETH']) == 3 and os.path.exists(cc + 'cl_2026-11-05.pkl'), 'cl_dia: lee el CSV una vez (solo source=chainlink) y congela la cache de un dia completo')
mt = pd.read_pickle(cc + 'cl_2026-11-05.pkl'); ok(mt['dia'] == '2026-11-05' and len(mt['sha256_fuente']) == 64 and mt['n'] == {'ETH': 3, 'SOL': 3, 'XRP': 3} and 'creado' in mt, 'cache con metadatos (dia, sha de la fuente, fecha, n)')
os.remove(pr + 'chainlink_2026-11-05.csv.gz'); ser, e = Q.cl_dia('2026-11-05', '2026-11-09', cc, pr); ok(e is None and len(ser['SOL']) == 3, 'rotado el CSV, el dia sigue disponible desde la cache (ya no es ERROR_DATOS)')
ser, e = Q.cl_dia('2026-11-04', '2026-11-09', cc, pr); ok(ser is None and 'sin cache ni CSV' in e and Q.err_dias([e]) == ['2026-11-04'], 'ERROR_DATOS solo si no esta en cache Y falta el CSV')
csvcl('2026-11-09', gz=False); ser, e = Q.cl_dia('2026-11-09', '2026-11-09', cc, pr); ok(e is None and not os.path.exists(cc + 'cl_2026-11-09.pkl'), 'un dia en curso (dia >= hoy) NO se congela')
csvcl('2026-11-03', coins=('ETH', 'XRP')); ser, e = Q.cl_dia('2026-11-03', '2026-11-09', cc, pr); ok(ser is None and 'SOL' in e, 'CSV sin filas de una moneda => ERROR_DATOS (no filas descartadas)')
ser, e = Q.cl_dia('2026-11-03', '2026-11-09', cc, pr, coins=('ETH',)); ok(e is None, 'P-A (solo ETH) no exige SOL')
open(cc + 'cl_2026-11-02.pkl', 'wb').write(b'basura'); ser, e = Q.cl_dia('2026-11-02', '2026-11-09', cc, pr); ok(ser is None and 'ilegible' in e, 'cache corrupta => ERROR_DATOS')
csvcl('2026-11-06'); S_, errs = Q.cl_series(['2026-11-05', '2026-11-06', '2026-11-06'], hoy='2026-11-09', cache=cc, prices=pr); ok(not errs and len(S_['ETH'][0]) == 6 and (np.diff(S_['ETH'][0]) > 0).all(), 'cl_series une dias (cache + CSV), ordenado y sin duplicados')
S_, errs = Q.cl_series(['2026-11-05', '2026-11-04'], hoy='2026-11-09', cache=cc, prices=pr); ok(S_ == {} and len(errs) == 1, 'cl_series con un dia sin cache ni CSV => error y sin serie')
# thru1: feat_chainlink fail-closed (sin crash con df vacio) y sin error cuando hay cache
Q_PR, Q_CC = Q.PRICES, Q.CL_CACHE
try:
    Q.PRICES = pr; Q.CL_CACHE = cc
    U = pd.DataFrame({'dia': ['2026-11-06'] * 2, 'fin': [1793923200, 1793923500], 'act': ['ETH', 'SOL']})
    o_, e_ = E.feat_chainlink(['2026-11-06'], U, '2026-11-09', cc); ok(e_ == [] and len(o_) == 2 and {'r1', 'r4'} <= set(o_.columns), 'feat_chainlink con cache/CSV: sin error')
    o_, e_ = E.feat_chainlink(['2026-11-07'], U, '2026-11-09', cc); ok(e_ and o_.r1.isna().all(), 'feat_chainlink: CSV ausente => ERROR_DATOS del brazo (sin crash)')
    o_, e_ = E.feat_chainlink(['2026-11-07'], U.iloc[:0], '2026-11-09', cc); ok(e_ and len(o_) == 0, 'feat_chainlink con unidades vacias no revienta')
finally: Q.PRICES, Q.CL_CACHE = Q_PR, Q_CC
# dias sin pareja
od2 = tempfile.mkdtemp() + '/'; mkp('2026-11-10').to_pickle(od2 + 'dec2_2026-11-10.pkl'); mkp('2026-11-11').to_pickle(od2 + 'dec3s100_2026-11-11.pkl'); fila.assign(dia='2026-11-12').to_pickle(od2 + 'dec2_2026-11-12.pkl'); fila.assign(dia='2026-11-12').to_pickle(od2 + 'dec3s100_2026-11-12.pkl'); mkp('2027-02-01').to_pickle(od2 + 'dec2_2027-02-01.pkl')
sp_, _g = Q.dias_sin_pareja(od2, '2026-11-06'); ok(sp_ == ['2026-11-10', '2026-11-11'], f'dias_sin_pareja avisa de dec2 sin dec3s100 y al reves (y no del tope): {sp_}')
r = subprocess.run(['python3', '-I', EVD + 'eval_giro.py', '--desde', '2026-11-06', '--out', od2, '--salida', tempfile.mkdtemp(), '--hoy', '2026-11-20', '--cl-cache', cc], capture_output=True, text=True); ok('AVISO: dias con dec2 sin dec3s100' in r.stdout and '2026-11-10' in r.stdout, 'los evaluadores imprimen el aviso de dias sin pareja')
# eval_sha cubre q11_decision.py
ok(E.eval_sha() == hashlib.sha256((E.sha(E.__file__) + E.sha(Q.__file__)).encode()).hexdigest() and E.eval_sha() != E.sha(E.__file__), 'eval_sha = sha256(sha(eval_thru1)+sha(q11_decision)): editar q11_decision invalida aceptacion.json')
# filtro_sol013: ERROR_DATOS con estado corrupto => AVISO igualmente; RESUMEN.md conserva contenido y formato, con UNA linea de aviso delante (idempotente)
sd = tempfile.mkdtemp(); open(sd + '/estado_sol013.json', 'w').write('{corrupto'); val = '# RESUMEN H-Q11-SOL013 (generado X)\nlinea 2\n## VEREDICTO: INSUFFICIENT (nd=3)\n'; open(sd + '/RESUMEN.md', 'w').write(val); open(sd + '/resumen.json', 'w').write('{"v": 1}')
for _ in range(2): r = subprocess.run(['python3', '-I', FSOL, '--desde', '2026-11-06', '--out', od, '--salida', sd, '--hoy', '2026-11-20'], capture_output=True, text=True)
rs = open(sd + '/RESUMEN.md').read(); ok(r.returncode == 0 and os.path.exists(sd + '/AVISO_ultima_ejecucion.txt') and 'corrupto' in open(sd + '/AVISO_ultima_ejecucion.txt').read() and rs.split('\n', 1)[0].startswith('> AVISO') and rs.split('\n', 1)[1] == val and rs.count('> AVISO') == 1 and open(sd + '/resumen.json').read() == '{"v": 1}', f'filtro_sol013: aviso con estado corrupto; RESUMEN.md intacto salvo 1 linea (idempotente) ({r.stderr[-200:]})')
print(f'OK test_q11_decision ({n_ok} comprobaciones, unitarios puros)')
