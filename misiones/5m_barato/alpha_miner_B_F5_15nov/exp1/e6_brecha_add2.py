#!/usr/bin/env python3
"""E6 (ADDENDUM1 §3 E6): cuenta de la BRECHA de B por palanca. Brecha = EV real de B (pond. EUR, sello tm3 v3, 215 fills, 20-23 Oct, 100 % R1) - EV esperado de la POBLACION en las mismas celdas dia x moneda (T_rem > 60 s = ventana de B;
tipo B y todas; spec p60 y p35), recalculado con las definiciones v3; esperado = media de EV de celda ponderada por el coste de B en la celda (y agrupado). Palancas: CXB60 / F5C / F5A / UNION (E3, MEDIDO sobre fills reales con timing de cancelacion SIMULADO),
regimen (E5, POBLACION), colocacion/tamano (SIN MEDIR: se declara). Cada cifra lleva su etiqueta MEDIDO / SIMULADO / POBLACION. Desglose por epoca de la poblacion (B = R1). Solo lectura de caches y de E3/E5 json."""
import os, sys, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from popdata_add2 import *
t0 = time.time(); P, est = carga_pob(specs_keep=['p60', 'p35']); cobL, por = resumen_cobertura(est); COMPLETO = len(por.get('COMPLETE', [])) == len(est)
txt = [f'# E6 cuenta de la brecha de B (ADDENDUM1 sha {ADD_SHA[:8]} + ADDENDUM2 {ADD2_SHA[:8]}: 37 dias, 16 y 24-Oct con epoca por suelo medido)'] + cobL + [f'Estado poblacion: {"COMPLETO" if COMPLETO else "PARTIAL"}; prints {len(P)}']
Bf = pd.read_pickle(EXP + 'B_fills_v3.pkl'); assert len(Bf) == 215 and (Bf.epoca == 'R1').all()
eB = Bf.pnl.sum() / Bf.coste.sum(); nu = Bf.mkt_lado.nunique(); ncl = Bf.cierre.nunique()
txt += ['', f'## B real (sello tm3): {len(Bf)} fills, {nu} unidades (mercado-lado), {ncl} cierres, {Bf.dia.nunique()} dias, 100 % R1 | EV pond. EUR {eB:+.4f} | PnL {Bf.pnl.sum():+.2f} EUR sobre {Bf.coste.sum():.2f} EUR (sin comision ni rebate)']
pd_ = Bf.groupby('dia').apply(lambda d: pd.Series({'fills': len(d), 'coste': d.coste.sum(), 'pnl': d.pnl.sum(), 'EV': d.pnl.sum() / d.coste.sum()}), include_groups=False); txt += ['Por dia:', pd_.round(3).to_string()]
pc_ = Bf.groupby('coin').apply(lambda d: pd.Series({'fills': len(d), 'coste': d.coste.sum(), 'pnl': d.pnl.sum(), 'EV': d.pnl.sum() / d.coste.sum()}), include_groups=False); txt += ['Por moneda:', pc_.round(3).to_string()]
b60 = Bf.bid_p60.values.astype(float); tipoB_fill = np.isfinite(b60) & ((b60 - Bf.precio.values) >= 0.0099 - 1e-12)
txt.append(f"Fills de B tipo B (bid(t_dec,l=60) - precio >= 0,0099): {int(tipoB_fill.sum())}/215 (EV pond. {Bf.pnl.values[tipoB_fill].sum() / max(Bf.coste.values[tipoB_fill].sum(), 1e-9):+.3f}); resto (a la altura del bid o por encima) {int((~tipoB_fill).sum())} (EV pond. {Bf.pnl.values[~tipoB_fill].sum() / max(Bf.coste.values[~tipoB_fill].sum(), 1e-9):+.3f})")
# ---------------- poblacion en las mismas celdas
P = P.copy(); P['trem'] = P.fin.values.astype(np.int64) - P.r_ex.values / 1000.0; cells = Bf.groupby(['dia', 'coin']).agg(cB=('coste', 'sum'), pB=('pnl', 'sum')).reset_index(); RES = dict(B=dict(ev=float(eB), n=len(Bf)), pop={})
def pop_cell(spec, tipoB, trem_min=60):
    b = P['bid_' + spec].values.astype(float); m = (P.trem.values > trem_min)
    if tipoB: m &= np.isfinite(b) & ((b - P.q.values.astype(float)) >= 0.0099 - 1e-12)
    S = P[m].groupby(['dia', 'coin']).agg(p=('pnl', 'sum'), k=('coste', 'sum'), n=('pnl', 'size')).reset_index(); return cells.merge(S, on=['dia', 'coin'], how='left')
txt += ['', '## Poblacion en las MISMAS celdas dia x moneda de B (T_rem > 60 s), definiciones v3 (r_v3, t_dec = r_v3 - l_ef - 3 ms)']
for spec in ('p60', 'p35'):
    for tb in (True, False):
        M = pop_cell(spec, tb); ok = M.k.fillna(0) > 0; evc = (M.p / M.k).where(ok); w = M.cB.where(ok); ex_w = float((evc * w).sum() / w.sum()) if ok.any() else np.nan; ex_p = float(M.p[ok].sum() / M.k[ok].sum()) if ok.any() else np.nan
        RES['pop'][f"{spec}|{'B' if tb else 'todas'}"] = dict(esperado_pond_coste_B=ex_w, esperado_agrupado=ex_p, celdas=int(ok.sum()), prints=int(M.n.fillna(0).sum()), brecha_pond=float(eB - ex_w), brecha_agrupada=float(eB - ex_p))
        txt.append(f"{spec} | {'tipo B' if tb else 'todas las filas'}: {int(ok.sum())}/{len(M)} celdas con poblacion, {int(M.n.fillna(0).sum())} prints | EV esperado (pond. por coste de B en la celda) {ex_w:+.4f}; agrupado {ex_p:+.4f} | B real {eB:+.4f} -> BRECHA = {eB - ex_w:+.4f} (pond.) / {eB - ex_p:+.4f} (agrupada)  [POBLACION vs MEDIDO]")
        if spec == 'p60':
            txt.append('    por celda (dia moneda: coste B, EV B, EV poblacion, n prints): ' + '; '.join(f"{r.dia[5:]} {r.coin}: {r.cB:.1f}, {r.pB / r.cB:+.2f}, {(r.p / r.k) if (r.k or 0) > 0 else float('nan'):+.2f}, {int(r.n) if r.n == r.n else 0}" for r in M.itertuples()))
# ---------------- poblacion por epoca (mismas definiciones; T_rem > 60; p60; tipo B y todas)
txt += ['', '## Poblacion (todas las celdas) por EPOCA, T_rem > 60 s, p60: EV pond. EUR  [POBLACION]']
for e in ('R0', 'R1', 'R2'):
    for tb in (True, False):
        b = P['bid_p60'].values.astype(float); m = (P.epoca.to_numpy(dtype=object) == e) & (P.trem.values > 60)
        if tb: m &= np.isfinite(b) & ((b - P.q.values.astype(float)) >= 0.0099 - 1e-12)
        if m.sum() < 200: continue
        S = P[m].groupby('dia').agg(p=('pnl', 'sum'), k=('coste', 'sum')); evd = (S.p / S.k).values; lo, pt, mu = t_ic(evd) if len(evd) >= 3 else (np.nan, np.nan, np.nan)
        txt.append(f"{e} | {'tipo B' if tb else 'todas'}: prints {int(m.sum())}, dias {len(S)} | EV pond. {S.p.sum() / S.k.sum():+.3f} | media diaria {mu:+.3f} IC90 inf {lo:+.3f} | dias+ {int((evd > 0).sum())}/{len(evd)}")
# ---------------- palancas (E3 y E5)
def carga(p): return json.load(open(p)) if os.path.exists(p) else None
E3 = carga(EXP + 'E3_reglas.json'); E5 = carga(EXP + 'E5_regimen_add2.json'); txt += ['', '## Palancas y su efecto sobre la brecha (puntos de EV por EUR; brecha de referencia = tipo B, T_rem > 60 s, p60, pond.)']
gap = -RES['pop']['p60|B']['brecha_pond'] if 'p60|B' in RES['pop'] else np.nan                 # lo que falta para igualar la poblacion = esperado - B (positivo si B esta por debajo)
txt.append(f"Falta para igualar a la poblacion (tipo B): {gap:+.4f} EV por EUR; para igualar a la de todas las filas: {-RES['pop']['p60|todas']['brecha_pond']:+.4f}; para EV = 0: {-eB:+.4f}")
if E3:
    R3 = E3['RES']; txt.append('E3 [MEDIDO sobre los 215 fills reales con tm3; timing de cancelacion SIMULADO]  (dEV = EV retenido - EV de todos los fills; dPnL = -pnl evitado):')
    for rg in ('CXB60', 'F5C', 'F5A', 'UNION'):
        for l in (35, 60, 100, 150):
            o = R3.get(f'{rg}_l{l}');
            if not o: continue
            ic = o.get('dEV_ic90', ['', '']); txt.append(f"  {rg} l_ef={l}: dEV {o['dEV']:+.4f} IC90 cierre {ic} | EV retenido {o['ev_kept']:+.4f} | dPnL {o['dPnL']:+.2f} EUR | evitados {o['n_evit']:.0f} | % de la brecha-a-poblacion cerrada {100 * o['dEV'] / gap:+.0f} % | % del camino a EV=0 {100 * o['dEV'] / -eB:+.0f} %")
    txt.append('  R2-equivalente (+20,5 ms de holgura de deteccion; SIMULADA): ' + '; '.join(f"{rg} l60 dEV {R3[f'{rg}_l60_R2-equivalente (+20,5 ms; SIMULADA)']['dEV']:+.4f}" for rg in ('CXB60', 'F5C', 'UNION') if f'{rg}_l60_R2-equivalente (+20,5 ms; SIMULADA)' in R3))
else: txt.append('E3: NO DISPONIBLE (e3_reglas.json no existe)')
if E5:
    prim = E5.get('PRIMARIO tipo B, todo T, todos los terciles', {}); txt.append('E5 regimen [POBLACION, descriptivo; no aditivo con E3]:')
    for k, nmb in (('1', 'D1 vol30'), ('2', 'D2 vol4h'), ('3', 'D3 EV bloque previo'), ('4', 'D4 EV slot')):
        r = prim.get(k)
        if r and r.get('n_unidades', 0): txt.append(f"  {nmb}: dEV diario medio {r['media_dia']:+.3f} IC90 inf {r['ic90_dias_inf']:+.3f}, dias+ {r['dias_pos']}/{r['n_dias']}, EV viables {r['ev_viables']:+.3f} vs todo {r['ev_todo']:+.3f}, {100 * r['frac_coste_viable']:.0f} % del coste viable -> {r['etiqueta']}")
else: txt.append('E5: NO DISPONIBLE (e5_regimen.json no existe)')
txt.append('Colocacion / tamano / cola (donde pone B la orden, tamano por orden, tiempo de vida): SIN MEDIR en EXP-1 (declarado en el ADDENDUM1 §3 E6); es el residuo de la cuenta.')
txt += ['', f'RESUMEN: B real {eB:+.4f} vs poblacion tipo B misma celda {RES["pop"]["p60|B"]["esperado_pond_coste_B"]:+.4f}: brecha {RES["pop"]["p60|B"]["brecha_pond"]:+.4f} (B por debajo si <0); 4 dias R1, 202 unidades, 129 cierres: IC amplio; ninguna palanca de E3 sustituye al forward (dry-run CXB60 desde 22-Nov). Tiempo {time.time() - t0:.0f} s.' + ('' if COMPLETO else ' PARTIAL: faltan dias de poblacion.')]
write(EXP + 'E6_brecha_add2.txt', txt); json.dump(RES, open(EXP + 'E6_brecha_add2.json', 'w'), default=float, indent=1); estado_fase('E6_add2', 'COMPLETE' if COMPLETO else 'PARTIAL'); print('\n'.join(txt))
