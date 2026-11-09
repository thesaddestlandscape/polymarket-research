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
E.ESPERA_REST = 0   # los reintentos REST no duermen en las pruebas
res = lambda tot, cc, cd, nc, n: dict(dpnl=dict(tot=tot, ncierres=nc, ic_c=(0, cc, 0, 0), ic_d=(0, cd, 0, 0)), n_arm=n, conds={'C3 x': False, 'C7 y': False, 'C2 z': False})
ok(E.refuta_fuerte(res(-10, -1, -1, 50, 300))[0], 'thru1 REFUTA fuerte: dPnL<0, sup cierre<0, sup dia<0, >=300 rellenos')
for args, m in ((res(0, -1, -1, 50, 300), 'dPnL=0 (ya no refuta con <=0)'), (res(-10, 1, -1, 50, 300), 'IC cierre cruza 0'), (res(-10, -1, 1, 50, 300), 'IC dia cruza 0'), (res(-10, -1, -1, 2, 300), '<3 cierres'), (res(-10, -1, -1, 50, 299), '<300 rellenos'), (res(float('nan'), -1, -1, 50, 300), 'NaN')):
    ok(not E.refuta_fuerte(args)[0], 'thru1 NO refuta: ' + m)
ok('no identificado por el relleno' in E.motivo_refuted(res(-1, 1, 1, 50, 300)) and 'no separable del regimen' in E.motivo_refuted(res(-1, 1, 1, 50, 300)), 'motivo REFUTED')
# ---------- revision /code-review (09-Nov): fila B vs F, racha a la baja, cargar_dias canonico, PROMOCION congelada, sin sobrescribir ----------
t, w, s_ = V(E0, err=['dec2_2026-12-30.pkl: filas con dia != 2026-12-30'], nd=11, hoy='2027-01-01'); ok(t == 'CERRADO_INSUFFICIENT [EN REVISION]' and s_['terminal']['causa'] == 'ERROR_DATOS', 'ADDENDUM5: la fila B2 sustituye al escenario absorbente de ADDENDUM4: ERROR_DATOS con hoy>=2027-01-01 => CERRADO_INSUFFICIENT')
t, w, s_ = V(E0, nvalid=0, nd=0, hoy='2027-02-01'); ok(t == 'CERRADO_INSUFFICIENT' and s_['terminal']['causa'] == 'SIN_DIAS_VALIDOS', 'ADDENDUM5 B2: 0 dias validos con hoy>=2027-01-01 => CERRADO_INSUFFICIENT')
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

# ---------- ADDENDUM5 (sha becb8cfd) sec. 1-3 / 5: fila B2, nd_ficheros, en_revision, last_nd, salida temprana unica, reapertura (T1-T11) ----------
ERRX = ['dec2_2026-12-20_old.pkl: nombre no canonico']
# T1: B (hoy < 2027-01-01): ERROR_DATOS y nvalid=0 => INSUFFICIENT con estado intacto (tambien via veredicto_sin_datos: no escribe fichero)
t, w, s_ = V(E0, err=ERRX, hoy='2026-12-31'); ok(t == 'INSUFFICIENT' and s_ == E0, 'T1 B con ERROR_DATOS antes de 2027: INSUFFICIENT, estado intacto')
t, w, s_ = V(E0, nvalid=0, nd=0, hoy='2026-12-31'); ok(t == 'INSUFFICIENT' and s_ == E0, 'T1 B con nvalid=0 antes de 2027: INSUFFICIENT, estado intacto')
# T2: B2 ERROR_DATOS hoy=2027-01-01: terminal escrito con causa, last_nd, nd_ficheros, en_revision; 2a ejecucion: A, no se reescribe, sigue EN REVISION
spb = tempfile.mkdtemp() + '/estado_b2.json'; Q.guardar_estado(spb, {'racha': 1, 'last_nd': 7, 'terminal': None, 'last_eval': '2026-12-20'})
tk, wy = Q.veredicto_sin_datos(spb, ERRX, '2026-12-31', 3); ok(tk == 'INSUFFICIENT' and Q.cargar_estado(spb)['terminal'] is None, 'T6 veredicto_sin_datos NO escribe antes de 2027')
tk, wy = Q.veredicto_sin_datos(spb, ERRX, '2027-01-01', 3); st_ = Q.cargar_estado(spb); tt = st_['terminal']
ok(tk == 'CERRADO_INSUFFICIENT [EN REVISION]' and tt['veredicto'] == 'CERRADO_INSUFFICIENT' and tt['causa'] == 'ERROR_DATOS' and tt['nd'] == 7 and tt['nd_ficheros'] == 3 and tt['en_revision'] is True and tt['fecha'] == '2027-01-01' and 'nd_ficheros' in tt and ERRX[0] in tt['motivo'], 'T2/T5 B2 ERROR_DATOS: terminal escrito (causa, nd=last_nd=7, nd_ficheros, en_revision)')
m0 = open(spb).read(); tk2, wy2 = Q.veredicto_sin_datos(spb, [], '2027-01-05', 0)
ok(tk2 == 'CERRADO_INSUFFICIENT [EN REVISION]' and open(spb).read() == m0 and 'ADMINISTRATIVO' in wy2, 'T2 2a ejecucion: fila A, no se reescribe el estado y sigue EN REVISION (persistido)')
# T3: B2 con nvalid=0 hoy=2027-02-01: causa SIN_DIAS_VALIDOS (en_revision solo si nd_ficheros>=20: T10)
t, w, s_ = V(E0, nvalid=0, nd=0, hoy='2027-02-01'); ok(t == 'CERRADO_INSUFFICIENT' and s_['terminal']['causa'] == 'SIN_DIAS_VALIDOS' and s_['terminal']['en_revision'] is False and s_['terminal']['nd'] == 0 and s_['terminal']['fecha'] == '2027-02-01', 'T3 B2 SIN_DIAS_VALIDOS, last_nd=0 por defecto')
# T4: con terminal previo prevalece el previo (A antes de B2); no se reescribe
for v in ('CONFIRMA_FINAL', 'REFUTA', 'REFUTED', 'CERRADO_INSUFFICIENT'):
    t, w, s_ = V(TERM(v, '2026-12-01'), err=ERRX, nvalid=0, nd=0, hoy='2027-01-01'); ok(t.startswith(v) and s_['terminal']['veredicto'] == v and 'causa' not in s_['terminal'], f'T4 A antes que B2 ({v})')
# T5: racha: last_nd=12 y nd actual 0 => terminal con nd=12 (no el nd actual)
t, w, s_ = V({'racha': 2, 'last_nd': 12, 'terminal': None}, nvalid=0, nd=0, hoy='2027-01-01'); ok(s_['terminal']['nd'] == 12, 'T5 B2 usa last_nd (12), no nd actual (0)')
# T6: veredicto_sin_datos escribe SOLO en B2 (hecho arriba); con terminal ya emitido nunca escribe
sp6 = tempfile.mkdtemp() + '/e.json'; Q.guardar_estado(sp6, TERM('REFUTA', '2026-12-10')); m6 = open(sp6).read(); Q.veredicto_sin_datos(sp6, ERRX, '2027-03-01', 5); ok(open(sp6).read() == m6, 'T6 con terminal previo veredicto_sin_datos no escribe')
# T7: fichero no canonico con hoy=2027-01-01 => B2; retirado antes de 2027 => B normal y la evaluacion sigue
o7 = tempfile.mkdtemp() + '/'
for nm in ('dec2', 'dec3s100'): mkp('2026-12-20').to_pickle(o7 + f'{nm}_2026-12-20.pkl')
mkp('2026-12-20').to_pickle(o7 + 'dec2_2026-12-20_old.pkl')
d7, R2_, R3_, e7 = Q.cargar_dias(o7, '2026-11-06'); ok(e7 and Q.nd_ficheros(o7, '2026-11-06') == 1, 'T7 el no canonico da ERROR_DATOS y nd_ficheros cuenta solo por nombre canonico (1)')
sp7 = tempfile.mkdtemp() + '/e.json'; Q.veredicto_sin_datos(sp7, e7, '2026-12-31', Q.nd_ficheros(o7, '2026-11-06')); ok(not os.path.exists(sp7), 'T7 antes de 2027 (B): no se escribe estado')
Q.veredicto_sin_datos(sp7, e7, '2027-01-01', Q.nd_ficheros(o7, '2026-11-06')); ok(Q.cargar_estado(sp7)['terminal']['causa'] == 'ERROR_DATOS', 'T7 a >= 2027 con el fichero no canonico: B2')
os.remove(o7 + 'dec2_2026-12-20_old.pkl'); d7, R2_, R3_, e7 = Q.cargar_dias(o7, '2026-11-06'); ok(not e7 and d7 == ['2026-12-20'], 'T7 retirado el fichero: B normal, la evaluacion sigue')
# nd_ficheros: tope (D<=2026-12-31) y desde; pareja incompleta no cuenta
o7b = tempfile.mkdtemp() + '/'
for d_ in ('2026-12-30', '2027-01-02', '2026-11-01'):
    for nm in ('dec2', 'dec3s100'): mkp(d_).to_pickle(o7b + f'{nm}_{d_}.pkl')
mkp('2026-12-29').to_pickle(o7b + 'dec2_2026-12-29.pkl'); ok(Q.nd_ficheros(o7b, '2026-11-06') == 1 and Q.nd_ficheros(o7b, '2026-10-01') == 2, 'nd_ficheros: tope 2026-12-31, desde, solo con ambos ficheros')
# T8: Chainlink ausente (P-A/P-C) a >= 2027 => B2 (P-A y P-C; P-B sigue evaluandose); antes de 2027 no escribe estado
for script, ests in ((EVD + 'eval_giro.py', ['P-C']), (EVD + 'eval_pistas.py', ['P-A'])):
    sd = tempfile.mkdtemp(); r = subprocess.run(['python3', '-I', script, '--desde', '2026-11-06', '--out', oc, '--salida', sd, '--hoy', '2026-12-31', '--cl-cache', tempfile.mkdtemp() + '/c/'], capture_output=True, text=True)
    ok(r.returncode == 0 and not any(f == f'estado_{e_}.json' for e_ in ests for f in os.listdir(sd)), f'T8 {os.path.basename(script)} antes de 2027: sin estado ({r.stderr[-200:]})')
    sd = tempfile.mkdtemp(); r = subprocess.run(['python3', '-I', script, '--desde', '2026-11-06', '--out', oc, '--salida', sd, '--hoy', '2027-01-01', '--cl-cache', tempfile.mkdtemp() + '/c/'], capture_output=True, text=True)
    for e_ in ests:
        f_ = sd + f'/estado_{e_}.json'; ok(r.returncode == 0 and os.path.exists(f_) and json.load(open(f_))['terminal']['causa'] == 'ERROR_DATOS' and json.load(open(f_))['terminal']['nd_ficheros'] == 1 and json.load(open(f_))['terminal']['en_revision'] is True, f'T8 {os.path.basename(script)} a >= 2027: B2 de {e_} escrito ({r.stderr[-300:]} {r.stdout[-300:]})')
    r2 = subprocess.run(['python3', '-I', script, '--desde', '2026-11-06', '--out', oc, '--salida', sd, '--hoy', '2027-01-03', '--cl-cache', tempfile.mkdtemp() + '/c/'], capture_output=True, text=True)
    ok('EN REVISION' in r2.stdout and 'CERRADO_INSUFFICIENT' in r2.stdout, f'T8 2a ejecucion de {os.path.basename(script)} sigue marcada EN REVISION')
# filtro_sol013 a >= 2027 con ERROR_DATOS: B2 escrito y listado
o7c = tempfile.mkdtemp() + '/'
for nm in ('dec2', 'dec3s100'): mkp('2026-12-20').to_pickle(o7c + f'{nm}_2026-12-20.pkl')
mkp('2026-12-20').to_pickle(o7c + 'dec2_2026-12-20_old.pkl')
sdf = tempfile.mkdtemp(); r = subprocess.run(['python3', '-I', FSOL, '--desde', '2026-11-06', '--out', o7c, '--salida', sdf, '--hoy', '2027-01-01'], capture_output=True, text=True)
ok(r.returncode == 0 and 'ERROR_DATOS' in open(sdf + '/AVISO_ultima_ejecucion.txt').read() and 'CERRADO_INSUFFICIENT' in open(sdf + '/AVISO_ultima_ejecucion.txt').read() and json.load(open(sdf + '/estado_sol013.json'))['terminal']['causa'] == 'ERROR_DATOS', f'filtro_sol013 B2 escrito y listado ({r.stderr[-200:]})')
# T9/T8 thru1: salida unica a >= 2027, por brazo sin terminal; brazos con terminal intactos; last_nd por brazo
import argparse
rtx, rtr = tempfile.mkdtemp() + '/', tempfile.mkdtemp() + '/'
for d_ in ('2026-11-12', '2026-11-13'): open(rtx + f'RT_{d_}.pkl', 'wb').write(b'x'); open(rtr + f'RT_{d_}.pkl', 'wb').write(b'x')
sv = (E.TX, E.RTD, E.check_shas)
def thru1(hoy, salida, bad=None, **kw):
    E.TX, E.RTD = rtx, rtr; E.check_shas = (lambda: bad) if bad is not None else sv[2]
    ns = argparse.Namespace(salida=salida, hoy=hoy, desde='2026-11-09', ensayo=False, cl_cache=cc, reevaluar_b2=None); ns.__dict__.update(kw)
    try: E.evaluar(ns)
    except SystemExit: pass
    finally: E.TX, E.RTD, E.check_shas = sv
    return open(f'{salida}/informe_thru1_{hoy}.txt').read()
st9 = {'arms': {'GEO6': {'terminal': {'veredicto': 'REFUTA', 'fecha': '2026-12-01', 'nd': 11, 'cp': 10}, 'cp': {}, 'last_nd': 11}, 'CXJ150': {'terminal': None, 'cp': {}, 'last_nd': 7}}}
for causa_msg, bad, extra in (('sha', ['engine.py sha distinto'], {}), ('aceptacion', [], {})):
    sd = tempfile.mkdtemp(); json.dump(st9, open(sd + '/estado_thru1.json', 'w')); inf = thru1('2026-12-31', sd, bad=bad if bad else [], **extra); ok(json.load(open(sd + '/estado_thru1.json')) == st9 and 'fila B' in inf, f'T9 thru1 ({causa_msg}) antes de 2027: INSUFFICIENT, estado intacto')
    sd = tempfile.mkdtemp(); json.dump(st9, open(sd + '/estado_thru1.json', 'w')); inf = thru1('2027-01-01', sd, bad=bad if bad else [], **extra); S9 = json.load(open(sd + '/estado_thru1.json'))['arms']
    ok(S9['GEO6']['terminal'] == st9['arms']['GEO6']['terminal'] and S9['CXJ150']['terminal']['causa'] == ('SHA_DISTINTO' if bad else 'ACEPTACION') and S9['CXJ150']['terminal']['nd'] == 7 and S9['CXJ150']['terminal']['nd_ficheros'] == 2 and S9['CXJ150']['terminal']['en_revision'] is True and all(S9[a_]['terminal']['veredicto'] == 'CERRADO_INSUFFICIENT' for a_ in E.ARMS if a_ != 'GEO6') and 'EN REVISION' in inf, f'T9 thru1 ({causa_msg}) a >= 2027: B2 por brazo sin terminal con last_nd/nd_ficheros; GEO6 intacto')
    ok(S9['PG_O50']['terminal']['nd'] == 0 and set(S9) == set(E.ARMS), 'T9 brazo sin last_nd previo: nd=0')
sd = tempfile.mkdtemp(); inf = thru1('2027-01-01', sd, bad=[], ensayo=True); S9 = json.load(open(sd + '/estado_thru1.json'))['arms']; ok(all(S9[a_]['terminal']['causa'] == 'SIN_DIAS_VALIDOS' for a_ in E.ARMS) or all(S9[a_]['terminal']['causa'] == 'ERROR_DATOS' for a_ in E.ARMS), 'T9 0 dias validos / ERROR_DATOS de cargar (RT sinteticos ilegibles) a >= 2027: B2 en todos los brazos')
# T10: nd_ficheros>=20 con error => en_revision=true y causa visible (para SIN_DIAS_VALIDOS el marcador sale solo con nd_ficheros>=20)
t, w, s_ = V(E0, nvalid=0, nd=0, hoy='2027-01-01'); ok(Q.veredicto(E0, [], 0, 0, False, False, '2027-01-01', 25)[2]['terminal']['en_revision'] is True and s_['terminal']['en_revision'] is False, 'T10 SIN_DIAS_VALIDOS: en_revision solo con nd_ficheros>=20')
t, w, s_ = Q.veredicto(E0, ERRX, 0, 0, False, False, '2027-01-01', 25); ok('[EN REVISION]' in t and 'causa=ERROR_DATOS' in w and s_['terminal']['nd_ficheros'] == 25, 'T10 nd_ficheros>=20 con error: en_revision y causa visibles')
# T11 (ADDENDUM5 sec. 3): reevaluacion tras reabrir un B2: nunca CONFIRMA_FINAL/CONFIRMA/CANDIDATO/PROMOCION; sin ref no reabre; solo reabre B2
sp11 = tempfile.mkdtemp() + '/e.json'; Q.guardar_estado(sp11, {'racha': 0, 'last_nd': 12, 'terminal': None}); Q.veredicto_sin_datos(sp11, ERRX, '2027-01-01', 3)
try: Q.reabrir_b2(sp11, ''); ok(False, 'T11 sin referencia debe fallar')
except SystemExit: ok(True, 'T11 sin referencia escrita no reabre')
ok(Q.reabrir_si_b2(sp11, 'DECISION_LOG 2027-01-10 sha=abc', '2027-01-10') and Q.cargar_estado(sp11)['terminal'] is None and Q.cargar_estado(sp11)['reabierto'][0]['terminal']['causa'] == 'ERROR_DATOS', 'T11 reabre solo con ref; conserva el terminal anulado')
sr = Q.cargar_estado(sp11); sr['racha'] = 2; sr['last_nd'] = 11
t, w, s_ = V(sr, nd=12, confirma=True, hoy='2027-01-12'); ok(t == 'CERRADO_INSUFFICIENT' and s_['terminal']['nd'] == 12, 'T11 reevaluacion: no puede emitir CONFIRMA_FINAL (nd<=20, racha 3): cae a F')
t, w, s_ = V(sr, nd=12, confirma=True, hoy='2026-12-20'); ok(t == 'INSUFFICIENT' and s_['racha'] == 0, 'T11 reevaluacion: no hay CONFIRMA provisional')
t, w, s_ = V(sr, nd=12, refuta=True, hoy='2027-01-12'); ok(t == 'REFUTA', 'T11 reevaluacion: REFUTA si se cumple')
t, w, s_ = V(sr, nd=20, confirma=True, hoy='2027-01-12'); ok(t == 'REFUTED', 'T11 reevaluacion: REFUTED a nd>=20')
Q.guardar_estado(sp11, TERM('REFUTA', '2026-12-01')); ok(not Q.reabrir_si_b2(sp11, 'x') and Q.cargar_estado(sp11)['terminal']['veredicto'] == 'REFUTA', 'T11 un terminal que no es B2 NO se reabre')
# thru1 reevaluar-b2: reabre solo los B2 y bloquea CANDIDATO (el bloqueo en codigo)
ok("s.get('reabierto')" in open(EVD + 'eval_thru1.py').read() and "CANDIDATO/PROMOCION no emitibles" in open(EVD + 'eval_thru1.py').read(), 'thru1: bloqueo de CANDIDATO/PROMOCION en reevaluacion presente en el codigo')
sd = tempfile.mkdtemp(); json.dump(st9, open(sd + '/estado_thru1.json', 'w')); thru1('2027-01-01', sd, bad=['x']); inf = thru1('2027-01-20', sd, bad=['x'], reevaluar_b2='LOG 2027-01-20 sha=abc'); S9 = json.load(open(sd + '/estado_thru1.json'))['arms']
ok('B2 reabierto (CXJ150)' in inf and 'B2 reabierto (GEO6)' not in inf and S9['GEO6']['terminal']['veredicto'] == 'REFUTA' and S9['CXJ150']['reabierto'][0]['ref'].startswith('LOG'), 'thru1 --reevaluar-b2 reabre solo los B2')
# ---------- ADDENDUM6 (sha 04487461): salud del feed Binance H1/H2/H3 ----------
D0 = int(pd.Timestamp('2026-11-09', tz='UTC').timestamp()) * 1000; SAN = list(range(24)); rng_ = np.random.default_rng(1)
def flujo(huecos=(), hasta=86400, paso=1.0):
    """Ticks cada `paso` s (4 simbolos alternos) con huecos [(inicio_s, fin_s)] sin ticks."""
    t = np.arange(0.0, hasta, paso); m = np.ones(len(t), bool)
    for a_, b_ in huecos: m &= ~((t >= a_) & (t < b_))
    ms = (D0 + t[m] * 1000).astype(np.int64); sy = np.array(E.SIMB_FLUJO)[np.arange(len(ms)) % 6]; return {k: ms[sy == k] for k in E.SIMB_FLUJO}
def h12(rec, sanas=SAN): return E.salud_h1h2(rec, D0, sanas)
r_ = h12(flujo(huecos=[(1000, 1059)])); ok(r_['h1'] and abs(r_['h1_hueco_max_s'] - 60) < 1.5, f'H1 hueco 59 s valido ({r_["h1_hueco_max_s"]})')
r_ = h12(flujo(huecos=[(1000, 1061)])); ok(not r_['h1'] and r_['h2'] and r_['h1_hueco_max_s'] > 60, 'H1 hueco 61 s NO valido (H2 sigue ok)')
r_ = h12(flujo(huecos=[(5000, 5046)])); ok(r_['h1'] and r_['h2'], 'H1 reconexion de 46 s valida')
r_ = h12(flujo(huecos=[(2 * 3600 + 100, 2 * 3600 + 190)]), sanas=[h for h in SAN if h != 2]); ok(r_['h1'] and r_['h2'], 'hueco de 90 s dentro de hora NO sana ignorado')
r_ = h12(flujo(huecos=[(2 * 3600 + 100, 2 * 3600 + 190)])); ok(not r_['h1'], 'el mismo hueco de 90 s en hora sana invalida H1')
fin_ = {k: v for k, v in flujo(paso=0.25).items()}; fin_['BTC'] = flujo(paso=0.5)['BTC']   # BTC continuo; ETH/SOL/XRP con huecos >60 s pero flujo conjunto continuo => valido
ln = {k: v[(v < D0 + 3000000) | (v > D0 + 3200000)] for k, v in flujo(paso=0.25).items() if k != 'BTC'}; ln['BTC'] = flujo(paso=0.5)['BTC']; r_ = h12(ln)
ok(r_['h1'] and r_['h2'] and r_['por_moneda']['ETH']['hueco_max_s'] > 60 and r_['por_moneda']['XRP']['hueco_max_s'] > 60, f'moneda fina con huecos >60 s pero flujo conjunto continuo => valido ({r_["por_moneda"]["ETH"]["hueco_max_s"]})')
def cob(frac): n = int(86400 * frac); sec = np.sort(rng_.choice(86400, n, replace=False)); ms = D0 + sec * 1000 + 10; sy = np.array(E.SIMB_FLUJO)[np.arange(len(ms)) % 6]; return {k: ms[sy == k] for k in E.SIMB_FLUJO}
r_ = h12(cob(0.949)); ok(not r_['h2'] and abs(r_['h2_cobertura'] - 0.949) < 0.001, f'H2 cobertura conjunta 0,949 NO valido ({r_["h2_cobertura"]})')
r_ = h12(cob(0.951)); ok(r_['h2'] and abs(r_['h2_cobertura'] - 0.951) < 0.001, f'H2 cobertura conjunta 0,951 valido ({r_["h2_cobertura"]})')
r_ = h12(flujo(huecos=[(1000, 1049)])); ok(r_['h1_var'] == {'50': True, '60': True, '73': True}, 'sensibilidad H1: 49 s pasa 50/60/73'); r_ = h12(flujo(huecos=[(1000, 1066)])); ok(r_['h1_var'] == {'50': False, '60': False, '73': True}, 'sensibilidad H1: 66 s solo pasa 73')
r_ = h12(flujo(huecos=[(1000, 1055)])); ok(r_['h1_var'] == {'50': False, '60': True, '73': True}, 'sensibilidad H1: 55 s pasa 60/73 y no 50')
ok(h12({k: v[:0] for k, v in flujo().items()})['h1'] is False, 'sin ticks: el hueco de dia completo invalida H1')
# H3: x_D sintetico y kline sintetico; minimo de los 4 simbolos; 0,949/0,951
kv = {k: np.full(1440, 10.0) for k in E.SIMB_H3}
def trd(ratio, simb=E.SIMB_H3, n_por_min=1):
    out = {}
    for k in E.SIMB_H3:
        r0 = ratio.get(k, 1.0) if isinstance(ratio, dict) else ratio; T = (D0 + np.arange(1440) * 60000 + 100).astype(np.int64); out[k] = (T, np.full(1440, 10.0 * r0))
    return out
r3 = E.salud_h3(trd(0.949), kv, D0); ok(not r3['h3'] and abs(r3['h3_min'] - 0.949) < 1e-9, 'H3 ratio 0,949 NO valido')
r3 = E.salud_h3(trd(0.951), kv, D0); ok(r3['h3'] and r3['h3_var'] == {'0.93': True, '0.95': True, '0.97': False}, 'H3 ratio 0,951 valido; sensibilidad 0,93/0,95/0,97')
r3 = E.salud_h3(trd({'BTC': 1.0, 'ETH': 0.99, 'SOL': 0.949, 'XRP': 1.0}), kv, D0); ok(not r3['h3'] and abs(r3['h3_min'] - 0.949) < 1e-9, 'H3: el MINIMO de los 4 simbolos decide (SOL 0,949 con los demas ok)')
r3 = E.salud_h3(trd(0.99), {**kv, 'XRP': np.zeros(1440)}, D0); ok(not r3['h3'], 'H3 volumen de kline 0 => ratio NaN => no valido (nunca dia valido)')
kvb = {k: v.copy() for k, v in kv.items()}; kvb['BTC'][100] = 5000.0; tb = trd(1.0); tb['BTC'][1][100] = 0.0; r3 = E.salud_h3(tb, kvb, D0); ok(r3['h3_diag']['BTC']['n_min_ratio_lt05_vol_gt10x'] == 1, 'diagnostico: minuto con ratio<0,5 y kline>10x mediana')
# REST: fallo / kline incompleto => ErrorDatos (ERROR_DATOS), cache por dia en datalogs sin repetir llamadas
kc = tempfile.mkdtemp() + '/k/'; ncall = [0]
def fetch_ok(sym, day0): ncall[0] += 1; return [(day0 + 60000 * i, 10.0) for i in range(1440)]
v1 = E.klines_dia('BTC', '2026-11-09', kc, fetch_ok); v2 = E.klines_dia('BTC', '2026-11-09', kc, fetch_ok); ok(ncall[0] == 1 and len(v1) == 1440 and (v1 == v2).all() and os.path.exists(kc + 'klines_BTC_2026-11-09.json'), 'klines REST cacheados por dia: 1 sola llamada')
def fetch_mal(sym, day0): raise OSError('sin red')
for ff, m_ in ((fetch_mal, 'fallo REST'), (lambda s_, d0: [(d0 + 60000 * i, 1.0) for i in range(1439)], 'kline incompleto'), (lambda s_, d0: [(d0 + 60000 * (i + 1), 1.0) for i in range(1440)], 'kline desplazado')):
    try: E.klines_dia('ETH', '2026-11-09', tempfile.mkdtemp() + '/k/', ff); ok(False, m_ + ' debe dar ErrorDatos')
    except E.ErrorDatos: ok(True, m_ + ' => ErrorDatos')
open(kc + 'klines_SOL_2026-11-09.json', 'w').write('{corrupto'); ok(len(E.klines_dia('SOL', '2026-11-09', kc, fetch_ok)) == 1440, 'cache de klines ilegible: se vuelve a pedir')
# dia_valido: cache sin `criterio` rechazada; validez_D.json guarda criterio, diagnostico y sensibilidad; REST fallido => error, sin cache; dia en curso no valido
vd = tempfile.mkdtemp() + '/'; json.dump({'dia': '2026-11-09', 'valido': True, 'cobertura_binance': {'ETH': 0.99}}, open(vd + 'validez_2026-11-09.json', 'w'))
import types, importlib; bfeat_stub = types.ModuleType('bfeat'); xf = tempfile.mkdtemp() + '/x_2026-11-09.csv.gz'; bfeat_stub.xfile = lambda d: xf
fl = flujo(); filas = sorted([(int(t), k) for k, v in fl.items() for t in v]); k_ = {k: 0 for k in E.SIMB_FLUJO}
with gzip.open(xf, 'wt') as fh:
    for t, sy in filas: fh.write(f'x,{t},{sy}USDT,1.0,{1.0:.8f},0,{t},{t + 5}\n')   # q por tick tal que ~ vol/minuto = 10 por simbolo (10 ticks/min por simbolo, 6 simbolos)
sys.modules['bfeat'] = bfeat_stub; E_PB, E_TX, E_RTD = E.PB, E.TX, E.RTD; pbt = tempfile.mkdtemp() + '/'; txt_ = tempfile.mkdtemp() + '/'; rtt = tempfile.mkdtemp() + '/'
open(pbt + 'tape_2026-11-09.pkl', 'wb').write(b'x'); json.dump({'bad': []}, open(pbt + 'bad_2026-11-09.json', 'w')); MT_OK = pd.Timestamp('2026-11-10 06:00', tz='UTC').timestamp(); os.utime(xf, (MT_OK, MT_OK)); os.utime(pbt + 'bad_2026-11-09.json', (MT_OK, MT_OK)); open(txt_ + 'RT_2026-11-09.pkl', 'wb').write(b'x'); open(rtt + 'RT_2026-11-09.pkl', 'wb').write(b'x')
try:
    E.PB, E.TX, E.RTD = pbt, txt_, rtt
    rv = E.dia_valido('2026-11-09', '2026-11-12', vd, kc, fetch_ok); ok(rv.get('criterio') == 'ADDENDUM7' and 'cobertura_binance' not in rv and 'h3_min' in rv and set(rv['sensibilidad']) == {'H1=50s', 'H1=60s', 'H1=73s', 'H3=0.93', 'H3=0.95', 'H3=0.97', 'H2=4simb'}, 'cache sin `criterio` rechazada y recalculada con la regla nueva y sensibilidad completa')
    ok(json.load(open(vd + 'validez_2026-11-09.json'))['criterio'] == 'ADDENDUM7' and 'intervalos_ge30s' in rv and set(rv['por_moneda']) == set(E.SIMB_FLUJO), 'validez_D.json con criterio, diagnostico por moneda e intervalos')
    ok(rv['h1'] and rv['h2'] and abs(rv['h3_min'] - 1.0) < 1e-6 and rv['valido'], f'dia sintetico sano: valido (min ratio {rv["h3_min"]})')
    os.remove(vd + 'validez_2026-11-09.json'); rv2 = E.dia_valido('2026-11-09', '2026-11-12', vd, tempfile.mkdtemp() + '/k/', fetch_mal); ok(rv2['valido'] is False and rv2.get('error') and 'ERROR_DATOS' in rv2['motivo'] and not os.path.exists(vd + 'validez_2026-11-09.json'), 'REST fallido => ERROR_DATOS, nunca dia valido, sin cache')
    nc0 = ncall[0]; rv3 = E.dia_valido('2026-11-09', '2026-11-09', vd, tempfile.mkdtemp() + '/k/', fetch_ok); ok(rv3['valido'] is False and rv3.get('en_curso') and ncall[0] == nc0 and not os.path.exists(vd + 'validez_2026-11-09.json.nuevo'), 'ADDENDUM7 C2/T7: dia EN CURSO: ni valido ni NO VALIDO, sin REST')
finally: E.PB, E.TX, E.RTD = E_PB, E_TX, E_RTD; sys.modules.pop('bfeat', None)
ok(E.FWD_DESDE == '2026-11-09' and E.DESCRIPTIVOS_DESDE == '2026-11-07', '--desde por defecto 2026-11-09; 07/08-Nov descriptivos')
sd = tempfile.mkdtemp(); inf = thru1('2026-12-20', sd, bad=[], desde='2026-11-07', ensayo=True); ok(True, 'ensayo ejecutable')
sd = tempfile.mkdtemp(); inf = thru1('2026-12-20', sd, bad=['x']); ok('fila B' in inf, 'informe de salida temprana')
sd = tempfile.mkdtemp()
for d_ in ('2026-11-07', '2026-11-08'): open(rtx + f'RT_{d_}.pkl', 'wb').write(b'x'); open(rtr + f'RT_{d_}.pkl', 'wb').write(b'x')
inf = thru1('2026-12-20', sd, bad=[], desde='2026-11-09', ensayo=True); ok('DESCRIPTIVOS-QUEMADOS' in inf and '2026-11-07' in inf.split('DESCRIPTIVOS-QUEMADOS')[1].split('\n')[0], '07/08-Nov se muestran como descriptivos y no cuentan (desde 2026-11-09)')


# ---------- ADDENDUM7 (sha 204d870c) ----------
src_ws = open('/root/polymarket-research/libro_estado_ws.py').read(); import re as _re
ok(tuple(x[:-4].upper() for x in _re.search(r'_SIMB_BN\s*=\s*\(([^)]*)\)', src_ws).group(1).replace('"', '').replace(' ', '').strip(',').split(',')) == E.SIMB_FLUJO and E.SIMB_H3 == ('BTC', 'ETH', 'SOL', 'XRP') and E.CRITERIO == 'ADDENDUM7', 'SIMB_FLUJO = libro_estado_ws._SIMB_BN (6); SIMB_H3 (4); CRITERIO ADDENDUM7')
# T6: H1/H2 con 6 simbolos
def ticks(ms_por_simb): return {k: np.asarray(v, np.int64) for k, v in ms_por_simb.items()}
def seis(ms): sy = np.array(E.SIMB_FLUJO)[np.arange(len(ms)) % 6]; return {k: ms[sy == k] for k in E.SIMB_FLUJO}
def gap_ms(gap, ini_s=1000, shift=0):
    t = np.arange(0, 86400000, 1000); n = (gap // 1000) - 1; i0 = ini_s; t = np.concatenate([t[:i0 + 1], t[i0 + 1 + n:] + shift]); return seis(D0 + t.astype(np.int64))
r_ = h12(gap_ms(60000)); ok(r_['h1'] and r_['h1_hueco_max_s'] == 60.0, f'T6 hueco de 60,0 s valido ({r_["h1_hueco_max_s"]})')
r_ = h12(gap_ms(60000, shift=100)); ok(not r_['h1'] and abs(r_['h1_hueco_max_s'] - 60.1) < 1e-9, f'T6 hueco de 60,1 s NO valido ({r_["h1_hueco_max_s"]})')
base_ = np.arange(0, 86400000, 1000)
tt = base_[(base_ < (1 * 3600 + 3570) * 1000) | (base_ > (1 * 3600 + 3570 + 120) * 1000)]   # hueco 01:59:30 -> 02:01:30
r_ = h12(seis(D0 + tt), sanas=[h for h in SAN if h != 1]); ok(r_['h1'], 'T6 hueco que EMPIEZA en hora mala (01) se ignora aunque termine en hora sana')
r_ = h12(seis(D0 + tt), sanas=[h for h in SAN if h != 2]); ok(not r_['h1'], 'T6 hueco que empieza en hora sana cuenta aunque termine en hora mala')
r_ = h12(seis(D0 + base_[base_ >= 61000])); ok(not r_['h1'] and r_['h1_hueco_max_s'] == 61.0, 'T6 el primer intervalo empieza en 00:00 (sin ticks hasta 61 s => no valido)')
r_ = h12(seis(D0 + base_[base_ <= 86400000 - 62000])); ok(not r_['h1'], 'T6 el ultimo intervalo llega hasta 24:00')
ok(h12(seis(D0 + base_), sanas=[])['h1'] is False and h12(seis(D0 + base_), sanas=[])['h2'] is False, 'T6 sin horas sanas: NO VALIDO')
sin_doge = {k: v for k, v in gap_ms(1000).items() if k != 'DOGE'}; r_ = h12(sin_doge); ok(not r_['h1'] and not r_['h2'] and r_['simbolos_ausentes'] == ['DOGE'], 'T6 simbolo DOGE ausente => NO VALIDO (h1=h2=False, motivo)')
# 4 simbolos 0,949 pero 6 simbolos 0,96 => h2 valido con h2_cobertura_4 < 0,95
sec4 = np.sort(rng_.choice(86400, int(86400 * 0.949), replace=False)); resto = np.setdiff1d(np.arange(86400), sec4); sec6x = np.sort(rng_.choice(resto, int(86400 * 0.011), replace=False))
rc = {k: D0 + sec4[np.arange(len(sec4)) % 4 == i] * 1000 + 10 for i, k in enumerate(E.SIMB_H3)}; rc['DOGE'] = D0 + sec6x[::2] * 1000 + 10; rc['BNB'] = D0 + sec6x[1::2] * 1000 + 10
r_ = h12(rc); ok(r_['h2'] and abs(r_['h2_cobertura'] - 0.960) < 0.002 and r_['h2_cobertura_4'] < 0.95 and abs(r_['h2_cobertura_4'] - 0.949) < 0.002, f'T6 4 simbolos {r_["h2_cobertura_4"]:.4f} pero 6 simbolos {r_["h2_cobertura"]:.4f} => H2 valido con h2_cobertura_4 < 0,95')
ln6 = {k: v[(v < D0 + 3000000) | (v > D0 + 3200000)] for k, v in gap_ms(1000).items() if k not in ('BTC', 'DOGE')}; ln6['BTC'] = D0 + np.arange(0, 86400000, 500); ln6['DOGE'] = D0 + np.arange(0, 86400000, 500) + 7; r_ = h12(ln6)
ok(r_['h1'] and r_['por_moneda']['ETH']['hueco_max_s'] > 60 and r_['por_moneda']['XRP']['hueco_max_s'] > 60 and set(r_['por_moneda']) == set(E.SIMB_FLUJO), 'T6 moneda fina con huecos >60 s y flujo conjunto continuo => valido; diagnosticos por moneda sobre los 6')
tr6 = trd(1.0); tr6['BNB'] = (tr6['BTC'][0], np.zeros(1440)); tr6['DOGE'] = (tr6['BTC'][0], np.zeros(1440)); r3 = E.salud_h3(tr6, kv, D0); ok(r3['h3'] and set(r3['h3_ratio']) == set(E.SIMB_H3), 'T6 H3 = minimo de los 4 (BNB/DOGE no entran)')
# FRAGIL y motivo en evaluar_salud (x_D sintetico con DOGE ausente / FRAGIL)
def xdia(flujo_, ruta, q=1.0):
    filas_ = sorted([(int(t), k) for k, v in flujo_.items() for t in v])
    with gzip.open(ruta, 'wt') as fh:
        for t, sy in filas_: fh.write(f'x,{t},{sy}USDT,1.0,{q:.8f},0,{t},{t + 5}\n')
xf2 = tempfile.mkdtemp() + '/x.csv.gz'; xdia(rc, xf2, q=1.0 * 1440 * 1e-9 + 0.0); kv_ok = lambda s_, d0: [(d0 + 60000 * i, 1e9) for i in range(1440)]
ev_ = E.evaluar_salud('2026-11-09', xf2, SAN, tempfile.mkdtemp() + '/k/', lambda s_, d0: [(d0 + 60000 * i, 1e-9 * len(sec4) / 1440 * 6) for i in range(1440)]); ok(ev_['h1'] and ev_['h2'] and ev_['fragil_criterio_salud'] is (ev_['valido']) and ev_['h2_cobertura_4'] < 0.95, 'T6 dia con H2(4)<0,95 y H2(6)>=0,95: marca FRAGIL AL CRITERIO DE SALUD (si es valido)')
xf3 = tempfile.mkdtemp() + '/x.csv.gz'; xdia(sin_doge, xf3); ev_ = E.evaluar_salud('2026-11-09', xf3, SAN, tempfile.mkdtemp() + '/k/', kv_ok); ok(not ev_['valido'] and 'simbolo del flujo ausente: DOGE' in ev_['motivo'], 'T6 DOGE ausente en x_D => dia NO VALIDO con motivo explicito')
# T7: REST / klines / cache / EN CURSO
for ff, m_ in ((lambda s_, d0: [(d0 + 60000 * i, 1.0) for i in range(1439)], 'kline 1439 minutos'), (lambda s_, d0: [(d0 + 60000 * i, 0.0) for i in range(1440)], 'volumen total 0'), (fetch_mal, 'REST que lanza')):
    kd = tempfile.mkdtemp() + '/k/'
    try: E.klines_dia('BTC', '2026-11-09', kd, ff); ok(False, m_)
    except E.ErrorDatos: ok(not os.path.exists(kd + 'klines_BTC_2026-11-09.json'), f'T7 {m_} => ErrorDatos, no se cachea')
# dia NO VALIDO cacheado no se recalcula; cache ADDENDUM6 rechazada; REST fallido global (sin cache de validez)
try:
    E.PB, E.TX, E.RTD = pbt, txt_, rtt; sys.modules['bfeat'] = bfeat_stub; vd2 = tempfile.mkdtemp() + '/'; kd2 = tempfile.mkdtemp() + '/k/'; nc = [0]
    def fetch_bajo(sym, d0): nc[0] += 1; return [(d0 + 60000 * i, 100.0) for i in range(1440)]   # volumen 10x el logueado => H3 NO valido
    rA = E.dia_valido('2026-11-09', '2026-11-12', vd2, kd2, fetch_bajo); n1 = nc[0]; ok(rA['valido'] is False and not rA['h3'] and 'H3' in rA['motivo'] and n1 == 4 and os.path.exists(vd2 + 'validez_2026-11-09.json'), 'T7 dia NO VALIDO por H3 queda cacheado')
    rB = E.dia_valido('2026-11-09', '2026-11-12', vd2, kd2, fetch_ok); ok(rB['valido'] is False and nc[0] == n1, 'T7 el NO VALIDO cacheado es definitivo (no se recalcula ni se reintenta)')
    c6 = json.load(open(vd2 + 'validez_2026-11-09.json')); c6['criterio'] = 'ADDENDUM6'; c6['valido'] = True; json.dump(c6, open(vd2 + 'validez_2026-11-09.json', 'w')); rC = E.dia_valido('2026-11-09', '2026-11-12', vd2, tempfile.mkdtemp() + '/k/', fetch_ok); ok(rC['criterio'] == 'ADDENDUM7' and rC['valido'], 'T7 cache ADDENDUM6 rechazada y recalculada')
    vd3 = tempfile.mkdtemp() + '/'; rD = E.dia_valido('2026-11-09', '2026-11-12', vd3, tempfile.mkdtemp() + '/k/', lambda s_, d0: [(d0 + 60000 * i, 0.0) for i in range(1440)]); ok(rD.get('error') and rD['valido'] is False and not os.listdir(vd3), 'T7 volumen 0 en el kline: ERROR_DATOS (error=True), sin cache de validez (no es NO VALIDO)')
    os.remove(txt_ + 'RT_2026-11-09.pkl'); rE = E.dia_valido('2026-11-09', '2026-11-12', tempfile.mkdtemp() + '/', kd2, fetch_ok); ok(rE.get('pendiente') and rE['valido'] is False and 'RT_passT' in rE['motivo'], 'T8 insumo incompleto de un dia cerrado: PENDIENTE (no NO VALIDO, sin cache)'); open(txt_ + 'RT_2026-11-09.pkl', 'wb').write(b'x')
finally: E.PB, E.TX, E.RTD = E_PB, E_TX, E_RTD; sys.modules.pop('bfeat', None)
# --- evaluar sintetico (ADDENDUM7 A, C3, C4, C5): evaluar con cargar/armar_base/dia_valido parcheados; datos sinteticos con dias/brazos controlados ---
def _g0(days, nper=3):
    rows = [dict(fin=1800000000 + i * 1000 + j, dia=d, act=('ETH', 'SOL', 'XRP')[j % 3], lado='NO' if j % 2 == 0 else 'YES', pnl=0.1 * ((i + j) % 3 - 1) + 0.02, cost=1.0) for i, d in enumerate(days) for j in range(nper)]
    return pd.DataFrame(rows, columns=['fin', 'dia', 'act', 'lado', 'pnl', 'cost'])
def _A(days):
    g = _g0(days); A = {'G0': g, 'GEO6': g.assign(pnl=g.pnl + .05), 'CXJ150': g.assign(pnl=g.pnl + .03), 'PC_AS': g.assign(pnl=g.pnl + .04)}
    for v in ('NJ3A', 'CXJ1000', 'GEO6NJ3', 'CXB150', 'CXB300', 'CXB1000', 'CXB3000'): A[v] = g.assign(pnl=g.pnl + .01)
    for pol_, dp in (('G0', 0.0), ('GEO6', .05), ('PG_O50', .06), ('PC_AS', .04)):
        for f in E.FV: A[f'rt_{pol_}_{f}'] = g.assign(pnl=g.pnl + dp)
    for f in ('BASE', 'CROSS'): A[f'rt_CXJ150_{f}'] = g.assign(pnl=g.pnl + .03)
    return A
def _U(days, cov):
    rows = []
    for d in days:
        c1, c4 = cov.get(d, (1.0, 1.0)); n_ = 50
        for k in range(n_): rows.append(dict(dia=d, fin=1900000000 + len(rows), act='ETH', r1=(0.01 if k < int(round(c1 * n_)) else np.nan), r4=(-0.01 if k < int(round(c4 * n_)) else np.nan)))
    u = pd.DataFrame(rows, columns=['dia', 'fin', 'act', 'r1', 'r4']); u['flag'] = (u.r1 > 0) & (u.r4 < 0); return u
def ev7(hoy, days, cov=None, cl_err=None, pend=(), estado=None, reev=None, fake_cp=None, ensayo=False, vz_extra=None):
    cov = cov or {}; sd = tempfile.mkdtemp(); rx, rr, bc, rxx = (tempfile.mkdtemp() + '/' for _ in range(4))
    for d_ in days:
        open(rx + f'RT_{d_}.pkl', 'wb').write(b'x'); open(rr + f'RT_{d_}.pkl', 'wb').write(b'x'); open(bc + f'Po_{d_}.pkl', 'wb').write(b'x'); open(rxx + f'RX_{d_}.pkl', 'wb').write(b'x')
    if estado is not None: json.dump(estado, open(sd + '/estado_thru1.json', 'w'))
    json.dump({'pass_': True, 'eval_sha': E.eval_sha()}, open(sd + '/aceptacion.json', 'w'))
    sv_ = (E.TX, E.RTD, E.BCO, E.RXD, E.check_shas, E.dia_valido, E.cargar, E.armar_base, E.checkpoint)
    E.TX, E.RTD, E.BCO, E.RXD = rx, rr, bc, rxx; E.check_shas = lambda: []
    E.dia_valido = lambda d, hoy_=None, *a_, **k_: ({'valido': False, 'pendiente': True, 'motivo': 'PENDIENTE: faltan RT_rt_sim'} if d in pend else {'valido': True, 'motivo': 'x'})
    E.cargar = lambda dias: (pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), [])
    E.armar_base = lambda T, R, S, X, dias, hoy_=None, cache=None: (_A(dias), _U(dias, cov), 0.99, list(cl_err or []))
    if fake_cp: E.checkpoint = fake_cp
    ns = argparse.Namespace(salida=sd, hoy=hoy, desde='2026-11-09', ensayo=ensayo, cl_cache=cc, reevaluar_b2=reev)
    try: E.evaluar(ns)
    except SystemExit: pass
    finally: E.TX, E.RTD, E.BCO, E.RXD, E.check_shas, E.dia_valido, E.cargar, E.armar_base, E.checkpoint = sv_
    inf = open(f'{sd}/informe_thru1_{hoy}.txt').read(); stp = sd + '/estado_thru1.json'; return inf, (json.load(open(stp)) if os.path.exists(stp) else None)
dA, dB, dC = '2026-11-12', '2026-11-13', '2026-11-14'
# T1: un dia con cobertura PC_AS 0,94 => PC_AS nd=2; resto nd=3; G0 del comparador de PC_AS solo en [a,b]
inf, S_ = ev7('2026-11-20', [dA, dB, dC], cov={dC: (0.94, 0.94)})
ok(S_['arms']['PC_AS']['last_nd'] == 2 and all(S_['arms'][a_]['last_nd'] == 3 for a_ in ('PG_O50', 'GEO6', 'CXJ150')) and 'PC_AS: dias no validos por rasgo' in inf and dC in inf.split('PC_AS: dias no validos por rasgo')[1].split('\n')[0], 'T1 el dia con rasgo < 0,95 solo sale de PC_AS: nd PC_AS=2, resto=3')
ok('## PC_AS: dias que cuentan nd_validos=2 (validos 2); G0 6 rellenos' in inf and '## GEO6: dias que cuentan nd_validos=3 (validos 3); G0 9 rellenos' in inf, 'T1 el G0 del comparador de PC_AS solo cubre [a,b] (6 rellenos; GEO6 9)')
ok('dias comunes' in inf.lower() or 'DIAS COMUNES' in inf, 'T1 secundarios marcados como dias comunes')
# T2: r1 definida y r4 NaN en 6 % => dia no valido para PC_AS y valido para el resto
inf, S_ = ev7('2026-11-20', [dA, dB, dC], cov={dB: (1.0, 0.94)}); ok(S_['arms']['PC_AS']['last_nd'] == 2 and S_['arms']['GEO6']['last_nd'] == 3 and dB in inf.split('PC_AS: dias no validos por rasgo')[1].split('\n')[0], 'T2 r4 NaN en 6 %: dia no valido para PC_AS (r1&r4) y valido para los demas')
inf, S_ = ev7('2026-11-20', [dA, dB, dC], cov={dB: (1.0, 0.95)}); ok(S_['arms']['PC_AS']['last_nd'] == 3, 'T2 cobertura exactamente 0,95 cumple')
# T3: cl_err => PC_AS INSUFFICIENT y resto evaluado; a >= 2027 B2 solo PC_AS
inf, S_ = ev7('2026-12-20', [dA, dB, dC], cl_err=['CSV chainlink 2026-11-12 ausente']); ok('VEREDICTO PC_AS: INSUFFICIENT' in inf and 'PC_AS' not in S_['arms'] and S_['arms']['GEO6']['last_nd'] == 3 and all(S_['arms'][a_]['terminal'] is None for a_ in ('PG_O50', 'GEO6', 'CXJ150')), 'T3 cl_err antes de 2027: PC_AS INSUFFICIENT sin estado; los demas brazos evaluados')
inf, S_ = ev7('2027-01-01', [dA, dB, dC], cl_err=['CSV chainlink 2026-11-12 ausente']); ok(S_['arms']['PC_AS']['terminal']['causa'] == 'ERROR_DATOS' and S_['arms']['PC_AS']['terminal']['veredicto'] == 'CERRADO_INSUFFICIENT' and S_['arms']['GEO6']['terminal']['veredicto'] == 'CERRADO_INSUFFICIENT' and 'causa' not in S_['arms']['GEO6']['terminal'] and S_['arms']['GEO6']['terminal']['motivo'].startswith('fila G'), 'T3 a >= 2027 B2 solo PC_AS (causa ERROR_DATOS); los demas cierran por la fila G de siempre (nd<20), no por B2')
# T4: PC_AS con arm_dias vacio antes y despues de 2027, sin tocar otros brazos
cov0 = {d_: (0.5, 0.5) for d_ in (dA, dB, dC)}
inf, S_ = ev7('2026-12-20', [dA, dB, dC], cov=cov0); ok('VEREDICTO PC_AS: INSUFFICIENT' in inf and 'PC_AS' not in S_['arms'] and S_['arms']['GEO6']['last_nd'] == 3, 'T4 PC_AS sin ningun dia con rasgo >= 95 % antes de 2027: fila B solo PC_AS, los demas siguen')
inf, S_ = ev7('2027-01-01', [dA, dB, dC], cov=cov0); t4 = S_['arms']['PC_AS']['terminal']; ok(t4['causa'] == 'SIN_DIAS_VALIDOS' and t4['motivo'] == 'rasgo PC_AS < 95 %' and t4['nd'] == 0 and t4['nd_ficheros'] == 3 and t4['en_revision'] is False and 'causa' not in S_['arms']['GEO6']['terminal'], 'T4 a >= 2027: B2 solo PC_AS, causa SIN_DIAS_VALIDOS, motivo rasgo PC_AS < 95 %')
# T5: checkpoint 10 de PC_AS usa SUS 10 primeros dias aunque el comun tenga otros
d12 = [(pd.Timestamp('2026-11-09') + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in range(12)]
inf, S_ = ev7('2026-11-25', d12, cov={d12[2]: (0.5, 0.5)}); cp_pc = S_['arms']['PC_AS']['cp']['10']['dias']; cp_g = S_['arms']['GEO6']['cp']['10']['dias']
ok(cp_g == d12[:10] and cp_pc == [d for d in d12 if d != d12[2]][:10] and d12[2] not in cp_pc and S_['arms']['PC_AS']['last_nd'] == 11, 'T5 checkpoint 10 de PC_AS = sus primeros 10 dias (sin el dia sin rasgo); GEO6 los primeros 10 del comun')
# T8: dia PENDIENTE anterior al ultimo candidato bloquea el checkpoint; al completarse, orden cronologico correcto
inf, S_ = ev7('2026-11-25', d12, pend={d12[2]}); ok(all(not S_['arms'][a_]['cp'] and S_['arms'][a_]['terminal'] is None for a_ in ('GEO6', 'CXJ150', 'PC_AS')) and 'BLOQUEAN checkpoints' in inf and 'checkpoints NO evaluados' in inf, 'T8 PENDIENTE anterior bloquea el checkpoint 10 (no se congela)')
inf_, S_ = ev7('2026-11-25', d12, pend={d12[10]}); ok('ESCALAR' not in inf_ and 'BLOQUEAN' in inf_, 'T8 PENDIENTE de <=7 dias bloquea pero aun no se escala')
inf, S_ = ev7('2026-11-25', d12, pend={d12[0]}); ok('ESCALAR A LA SESION PRINCIPAL' in inf, 'T8 PENDIENTE con mas de 7 dias de antiguedad: aviso de escalado')
inf, S_ = ev7('2026-11-25', d12, pend={d12[-1]}); ok(S_['arms']['GEO6']['cp']['10']['dias'] == d12[:10] and 'BLOQUEAN' not in inf, 'T8 PENDIENTE solo el ultimo dia: no bloquea (ningun dia posterior); el checkpoint usa los 10 primeros')
inf, S_ = ev7('2026-11-25', d12); ok(S_['arms']['GEO6']['cp']['10']['dias'] == d12[:10], 'T8 completado el dia: el checkpoint usa el orden cronologico correcto')
inf, S_ = ev7('2027-01-01', d12, pend={d12[2]}); ok(all(S_['arms'][a_]['terminal']['veredicto'] == 'CERRADO_INSUFFICIENT' and 'causa' not in S_['arms'][a_]['terminal'] and S_['arms'][a_]['terminal']['motivo'].startswith('fila G') for a_ in E.ARMS) and 'PENDIENTES a >= 2027-01-01' in inf and 'NO bloquean' in inf and 'BLOQUEAN checkpoints' not in inf, 'rev3 #6 PENDIENTE a >= 2027: NO cierra B2 global; no bloquea; cada brazo cierra por la fila G normal (nd<20) con linea de aviso/DECISION_LOG')
# C3: ERROR_DATOS global por REST
inf, S_ = ev7('2026-12-20', [dA, dB, dC]); sd_ = tempfile.mkdtemp()
sv2 = E.dia_valido
def _ev_err(hoy):
    rx, rr = tempfile.mkdtemp() + '/', tempfile.mkdtemp() + '/'; sd = tempfile.mkdtemp()
    for d_ in (dA, dB): open(rx + f'RT_{d_}.pkl', 'wb').write(b'x'); open(rr + f'RT_{d_}.pkl', 'wb').write(b'x')
    sv_ = (E.TX, E.RTD, E.check_shas, E.dia_valido); E.TX, E.RTD, E.check_shas = rx, rr, (lambda: [])
    E.dia_valido = lambda d, hoy_=None, *a_, **k_: ({'valido': False, 'error': True, 'motivo': 'ERROR_DATOS: REST klines BTC: OSError'} if d == dB else {'valido': True, 'motivo': 'x'})
    ns = argparse.Namespace(salida=sd, hoy=hoy, desde='2026-11-09', ensayo=False, cl_cache=cc, reevaluar_b2=None)
    ac = {'pass_': True, 'eval_sha': E.eval_sha()}; json.dump(ac, open(sd + '/aceptacion.json', 'w'))
    try: E.evaluar(ns)
    except SystemExit: pass
    finally: E.TX, E.RTD, E.check_shas, E.dia_valido = sv_
    return open(f'{sd}/informe_thru1_{hoy}.txt').read(), (json.load(open(sd + '/estado_thru1.json')) if os.path.exists(sd + '/estado_thru1.json') else None)
inf, S_ = _ev_err('2026-12-20'); ok('ERROR_DATOS salud Binance' in inf and S_ is None, 'T7 REST fallido de UN dia => ERROR_DATOS GLOBAL (INSUFFICIENT, sin estado, sin checkpoints)')
inf, S_ = _ev_err('2027-01-01'); ok(all(S_['arms'][a_]['terminal']['causa'] == 'ERROR_DATOS' for a_ in E.ARMS), 'T7 a >= 2027: B2 en todos los brazos por ERROR_DATOS global')
# T9: reevaluacion tras B2: CANDIDATO cp20 => CERRADO_INSUFFICIENT con el motivo de C4; cp10 etiqueta; sin PROMOCION; REFUTA fuerte disponible
def fake_res(cp, cand=True, dpnl=1.0, icsup=1.0):
    dp = dict(tot=dpnl, ncierres=50, nnz=50, dias={}, ic_c=(0.1, icsup, 0, 0), ic_d=(0.1, icsup, 0, 0), sin2dias=1.0, sin5cierres=1.0)
    return dict(cp=cp, dias=[], nd=cp, candidato=cand, conds={'C1 x': cand}, dpnl=dp, ev=dict(ev=0.1, ic_inf_p=0.05), n_arm=400, cross=1.0, placebo=None, pg_menos_geo6=None, shrink=None, label='CANDIDATO (EXPLORATORY hasta medicion L2)' if cand else 'NO CANDIDATO')
reab = {'terminal': None, 'cp': {}, 'last_nd': 0, 'reabierto': [{'terminal': {'veredicto': 'CERRADO_INSUFFICIENT', 'causa': 'ERROR_DATOS'}, 'ref': 'LOG', 'fecha': '2027-01-10'}]}
d20 = [(pd.Timestamp('2026-11-09') + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in range(21)]
inf, S_ = ev7('2026-12-10', d20[:12], estado={'arms': {'GEO6': dict(reab)}}, fake_cp=lambda arm, A, days, cp, U, plc: fake_res(cp)); g6 = S_['arms']['GEO6']
ok(g6['cp']['10']['label'] == 'CANDIDATO NO EMITIBLE (reevaluacion B2)' and g6['terminal'] is None, 'T9 reevaluacion: CANDIDATO en cp10 => etiqueta "CANDIDATO NO EMITIBLE (reevaluacion B2)" sin efecto')
inf, S_ = ev7('2026-12-10', d20[:21], estado={'arms': {'GEO6': dict(reab)}}, fake_cp=lambda arm, A, days, cp, U, plc: fake_res(cp)); g6 = S_['arms']['GEO6']
ok(g6['terminal']['veredicto'] == 'CERRADO_INSUFFICIENT' and g6['terminal']['motivo'] == 'reevaluacion tras B2 (ADDENDUM5 sec. 3): CANDIDATO/PROMOCION no emitibles' and 'PROMOCION (alfa' not in inf.split('## GEO6')[1].split('## CXJ150')[0], 'T9 reevaluacion: CANDIDATO en cp20 => CERRADO_INSUFFICIENT con el motivo de C4, sin linea PROMOCION')
inf, S_ = ev7('2026-12-10', d20[:21], fake_cp=lambda arm, A, days, cp, U, plc: fake_res(cp)); ok(S_['arms']['GEO6']['terminal']['veredicto'] == 'CANDIDATO', 'T9 control: sin B2 reabierto el CANDIDATO de cp20 se emite normalmente')
inf, S_ = ev7('2026-12-10', d20[:12], estado={'arms': {'GEO6': dict(reab)}}, fake_cp=lambda arm, A, days, cp, U, plc: fake_res(cp, cand=False, dpnl=-5.0, icsup=-1.0)); ok(S_['arms']['GEO6']['terminal']['veredicto'] == 'REFUTA', 'T9 reevaluacion: REFUTA fuerte sigue disponible')
# T10: 07 y 08-Nov siguen descriptivos
rt10 = tempfile.mkdtemp() + '/'; inf, S_ = ev7('2026-11-20', ['2026-11-07', '2026-11-08', dA]); ok('DESCRIPTIVOS-QUEMADOS' in inf and S_['arms']['GEO6']['last_nd'] == 1, 'T10 07 y 08-Nov descriptivos: no cuentan (nd=1)')
inf, S_ = ev7('2026-11-12', [dA]); ok('EN CURSO' in inf and 'No hay' not in inf, 'C2 el dia EN CURSO (d >= hoy) no es valido ni NO VALIDO ni entra en nd')


# ---------- 3a revision /code-review ----------
# #1 streaming: mismo resultado con chunks pequenos (muchos limites de chunk) que con uno grande y que la referencia en memoria; memoria O(86400)
rng7 = np.random.default_rng(7); n_ = 4000; secs = np.sort(rng7.choice(86400, n_, replace=False)); tms = D0 + secs * 1000 + rng7.integers(0, 1000, n_); symk = rng7.choice(E.SIMB_FLUJO, n_)
xr = tempfile.mkdtemp() + '/x_s.csv.gz'
with gzip.open(xr, 'wt') as fh:
    for t, sy, qq in zip(tms, symk, rng7.uniform(0.1, 2, n_)): fh.write(f'x,{t - 3},{sy}USDT,1.0,{qq:.6f},0,{t},{t}\n')
def leer_chunk(ch):
    acc = E.acc_nuevo(); 
    for c_ in pd.read_csv(xr, header=None, usecols=[1, 2, 4, 7], names=['T', 'sym', 'q', 'recv'], dtype={'T': 'int64', 'sym': 'category', 'q': 'float64', 'recv': 'int64'}, chunksize=ch):
        for sy_, g in c_.groupby('sym', observed=True): E.acc_add(acc, str(sy_)[:-4], g.recv.values, g['T'].values, g.q.values, D0)
    return acc
a1, a2, a3 = leer_chunk(7), leer_chunk(1000000), E.leer_x(xr, D0)
ok(all(np.allclose(a1[k], a2[k], rtol=1e-12, atol=1e-9) and np.allclose(a2[k], a3[k], rtol=1e-12, atol=1e-9) for k in a1) and a1['rmin'].shape == (6, 86400) and a1['qsum'].shape == (4, 1440) and a1['rmin'].nbytes < 5e6, '#1 streaming: identico con chunk=7 y chunk grande y con leer_x; memoria O(86400) (no guarda filas)')
brute = np.sort(tms); pts_ = np.concatenate([[D0], brute, [D0 + 86400000]]); gb = np.diff(pts_); h12s = E.salud_h1h2(a3, D0, SAN)
ok(abs(h12s['h1_hueco_max_s'] - gb.max() / 1000) < 1e-9 and h12s['n_intervalos_ge30s'] == int((gb >= 30000).sum()) and abs(h12s['h2_cobertura'] - len(np.unique((brute - D0) // 1000)) / 86400) < 1e-12, '#1 H1/H2 en streaming = referencia ordenada en memoria (hueco max, n>=30 s, cobertura)')
ok(sum(m['n'] for m in h12s['por_moneda'].values()) == n_ and all(m['hueco_max_s'] >= 1 for m in h12s['por_moneda'].values()), '#1 diagnosticos por moneda de un solo recorrido (6 simbolos)')
ref4 = np.unique((np.sort(tms[np.isin(symk, E.SIMB_H3)]) - D0) // 1000); ok(abs(h12s['h2_cobertura_4'] - len(ref4) / 86400) < 1e-12, '#1 H2 con 4 simbolos del mismo recorrido')
r3s = E.salud_h3(a3, {k: np.full(1440, 1.0) for k in E.SIMB_H3}, D0); ok(abs(r3s['h3_ratio']['BTC'] - a3['qsum'][0].sum() / 1440) < 1e-12 and r3s['h1b_hueco_trade_max_s'] > 0, '#1 H3 y H1b del mismo acumulador')
# #2 cache de klines validada al leer y al escribir
kc2 = tempfile.mkdtemp() + '/k/'; os.makedirs(kc2); nc2 = [0]
def f2(sym, d0): nc2[0] += 1; return [(d0 + 60000 * i, 5.0) for i in range(1440)]
for bad_ in ([float('nan')] * 1440, [0.0] * 1440, [1.0] * 1439):
    json.dump({'dia': '2026-11-09', 'sym': 'BTC', 'vol': bad_}, open(kc2 + 'klines_BTC_2026-11-09.json', 'w')); n0 = nc2[0]; v_ = E.klines_dia('BTC', '2026-11-09', kc2, f2)
    ok(nc2[0] == n0 + 1 and np.isfinite(v_).all() and v_.sum() > 0, f'#2 cache invalida ({str(bad_[0])[:4]}, {len(bad_)}) descartada y re-descargada')
n0 = nc2[0]; E.klines_dia('BTC', '2026-11-09', kc2, f2); ok(nc2[0] == n0, '#2 cache valida: sin llamada')
kc3 = tempfile.mkdtemp() + '/k/'
try: E.klines_dia('ETH', '2026-11-09', kc3, lambda s_, d0: [(d0 + 60000 * i, float('nan') if i == 5 else 1.0) for i in range(1440)]); ok(False, 'NaN')
except E.ErrorDatos: ok(not os.path.exists(kc3 + 'klines_ETH_2026-11-09.json'), '#2 al escribir: kline con NaN => ErrorDatos, sin cache')
# reintentos REST: 3 intentos con espera
nr = [0]
def f_flaky(sym, d0):
    nr[0] += 1
    if nr[0] < 3: raise OSError('timeout')
    return [(d0 + 60000 * i, 2.0) for i in range(1440)]
ok(len(E.klines_dia('SOL', '2026-11-09', tempfile.mkdtemp() + '/k/', f_flaky)) == 1440 and nr[0] == 3, 'rev3: REST que falla 2 veces y acierta a la 3a => dia evaluable (3 intentos)')
nr[0] = 0
def f_dead(sym, d0): nr[0] += 1; raise OSError('caido')
try: E.klines_dia('SOL', '2026-11-09', tempfile.mkdtemp() + '/k/', f_dead); ok(False, 'dead')
except E.ErrorDatos as e_: ok(nr[0] == 3 and '3 intentos' in str(e_), 'rev3: REST caido => ErrorDatos tras exactamente 3 intentos')
# #3 asentamiento antes de cachear (lectura: x_D/bad_D producidos DESPUES del asentamiento y estables; ver docstring de `asentado`)
try:
    E.PB, E.TX, E.RTD = pbt, txt_, rtt; sys.modules['bfeat'] = bfeat_stub; vd5 = tempfile.mkdtemp() + '/'; nc5 = [0]
    def f5(sym, d0): nc5[0] += 1; return [(d0 + 60000 * i, 10.0) for i in range(1440)]
    A_ = pd.Timestamp; bt = pbt + 'bad_2026-11-09.json'; ut = lambda p_, h_: os.utime(p_, (A_(h_, tz='UTC').timestamp(),) * 2)
    r5 = E.dia_valido('2026-11-09', '2026-11-10', vd5, tempfile.mkdtemp() + '/k/', f5, ahora=A_('2026-11-10 00:20', tz='UTC')); ok(r5.get('pendiente') and 'sin asentar' in r5['motivo'] and nc5[0] == 0 and not os.listdir(vd5), '#3 < 30 min tras la medianoche de d+1: PENDIENTE sin cache ni REST')
    ut(xf, '2026-11-10 00:10'); r5 = E.dia_valido('2026-11-09', '2026-11-10', vd5, tempfile.mkdtemp() + '/k/', f5, ahora=A_('2026-11-10 12:00', tz='UTC')); ok(r5.get('pendiente') and 'x_' in r5['motivo'] and 'antes de' in r5['motivo'] and nc5[0] == 0 and not os.listdir(vd5), '#3 x_D producido antes del asentamiento: PENDIENTE sin cache')
    ut(xf, '2026-11-10 11:55'); r5 = E.dia_valido('2026-11-09', '2026-11-10', vd5, tempfile.mkdtemp() + '/k/', f5, ahora=A_('2026-11-10 12:00', tz='UTC')); ok(r5.get('pendiente') and 'menos de 10 min' in r5['motivo'] and not os.listdir(vd5), '#3 x_D tocado hace < 10 min (aun escribiendose): PENDIENTE sin cache')
    ut(xf, '2026-11-10 06:00'); ut(bt, '2026-11-10 00:15'); r5 = E.dia_valido('2026-11-09', '2026-11-10', vd5, tempfile.mkdtemp() + '/k/', f5, ahora=A_('2026-11-10 12:00', tz='UTC')); ok(r5.get('pendiente') and 'bad_' in r5['motivo'] and not os.listdir(vd5), '#3 bad_D.json producido antes del asentamiento: PENDIENTE sin cache')
    ut(bt, '2026-11-10 06:00'); r5 = E.dia_valido('2026-11-09', '2026-11-10', vd5, tempfile.mkdtemp() + '/k/', f5, ahora=A_('2026-11-10 12:00', tz='UTC')); ok('pendiente' not in r5 and r5['criterio'] == 'ADDENDUM7' and os.path.exists(vd5 + 'validez_2026-11-09.json'), '#3 asentado (>=30 min, ficheros posteriores y estables): se calcula y se cachea')
finally: E.PB, E.TX, E.RTD = E_PB, E_TX, E_RTD; sys.modules.pop('bfeat', None)
# #4 la reapertura se persiste YA (aunque haya salida temprana) con referencia y cp/last_nd coherentes
st4 = {'arms': {'CXJ150': {'terminal': {'veredicto': 'CERRADO_INSUFFICIENT', 'causa': 'ERROR_DATOS', 'fecha': '2027-01-01', 'nd': 0, 'nd_ficheros': 3, 'en_revision': True}, 'cp': {'10': {'dias': ['x']}}, 'last_nd': 0}, 'GEO6': {'terminal': {'veredicto': 'REFUTA', 'fecha': '2026-12-01', 'nd': 11}, 'cp': {}}}}
sd4 = tempfile.mkdtemp(); json.dump(st4, open(sd4 + '/estado_thru1.json', 'w')); inf4 = thru1('2026-12-20', sd4, bad=['x'], reevaluar_b2='LOG 2027-01-20 sha=abc'); S4 = json.load(open(sd4 + '/estado_thru1.json'))['arms']
ok(S4['CXJ150']['terminal'] is None and S4['CXJ150']['reabierto'][0]['ref'].startswith('LOG') and S4['CXJ150']['last_nd'] == 10 and S4['CXJ150']['racha'] == 0 and '10' in S4['CXJ150']['cp'] and S4['GEO6']['terminal']['veredicto'] == 'REFUTA' and 'reabierto' not in S4['GEO6'] and 'fila B' in inf4, '#4 reapertura persistida inmediatamente aunque haya salida temprana (fila B): ref, last_nd=10 coherente con cp, GEO6 intacto')
# #5 helper unico de en_revision
ok(not Q.en_revision('SIN_DIAS_VALIDOS', 19) and Q.en_revision('SIN_DIAS_VALIDOS', 20) and Q.en_revision('ERROR_DATOS', 0) and Q.en_revision('SIN_DIAS_VALIDOS', 0, ['e']) and Q.en_revision('SHA_DISTINTO', 0, (), thru1=True) and not Q.en_revision('SHA_DISTINTO', 0), '#5 Q.en_revision: ERROR_DATOS o nd_ficheros>=20 o err; thru1 siempre true')
t, w, s_ = Q.veredicto(E0, [], 0, 0, False, False, '2027-01-01', 25); t2, w2, s2_ = Q.veredicto(E0, [], 0, 0, False, False, '2027-01-01', 19); ok(s_['terminal']['en_revision'] is True and s2_['terminal']['en_revision'] is False, '#5 SOL013/P-*: el terminal usa el helper (nd_ficheros 25 true, 19 false)')
d21 = [(pd.Timestamp('2026-11-09') + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in range(21)]
inf, S_ = ev7('2027-01-01', d21, cov={d_: (0.5, 0.5) for d_ in d21}); ok(S_['arms']['PC_AS']['terminal']['causa'] == 'SIN_DIAS_VALIDOS' and S_['arms']['PC_AS']['terminal']['en_revision'] is True and S_['arms']['PC_AS']['terminal']['nd_ficheros'] == 21, '#5 rama PC_AS: SIN_DIAS_VALIDOS con nd_ficheros>=20 => en_revision (misma regla)')
inf, S_ = ev7('2027-01-01', [dA, dB, dC], cl_err=['x']); ok(S_['arms']['PC_AS']['terminal']['en_revision'] is True, '#5 rama PC_AS: ERROR_DATOS => en_revision')
inf, S_ = ev7('2027-01-01', [dA, dB], estado={'arms': {}}); ok(S_['arms']['GEO6']['terminal']['motivo'].startswith('fila G'), 'control: sin errores a >= 2027 los brazos cierran por la fila G')
sdq = tempfile.mkdtemp(); json.dump(st9, open(sdq + '/estado_thru1.json', 'w')); thru1('2027-01-01', sdq, bad=['x']); ok(json.load(open(sdq + '/estado_thru1.json'))['arms']['CXJ150']['terminal']['en_revision'] is True, '#5 thru1 salida temprana: en_revision (helper, thru1=True)')
# #7 descriptivo de PC_AS solo con arm_dias(PC_AS)
inf, S_ = ev7('2026-11-20', [dA, dB, dC], cov={dC: (0.5, 0.5)}); ln7 = [l for l in inf.split('\n') if l.startswith('Cobertura rasgo PC_AS')][0]
ok('SOLO en arm_dias(PC_AS)=2 dias' in ln7 and '1.000' in ln7 and 'G0 rellenos 6' in ln7 and 'G0 todos los dias comunes: 9 rellenos' in ln7, f'#7 Cobertura rasgo PC_AS solo sobre arm_dias(PC_AS) (cobertura 1.000 sin el dia excluido; G0 6 de 9): {ln7[:200]}')
ok('NO son arm_dias(PC_AS)' in inf and 'DIAS COMUNES' in inf, '#7 la etiqueta de los secundarios aclara que son dias comunes')

print(f'OK test_q11_decision ({n_ok} comprobaciones, unitarios puros)')
