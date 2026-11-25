#!/usr/bin/env python3
"""a2_agrega.py (ident_17nov, Tarea A) -- SOLO LECTURA. P(golpe <= W) del brazo B REAL (fn_16nov/eventos_D.pkl, brazo 'B', n=1.942) frente a la orden
VIRTUAL de la regla de B (A_ev_D.pkl, mercados SIN orden real), estandarizada a la distribucion de celdas del brazo B.
PRINCIPAL: 20-23 Oct, celdas dia x moneda x L(4 tramos de 5c) x T(3 tramos) x suelo(lo/hi/indet), variante pl_any (paquete_l, relleno cierra).
SENSIBILIDAD: dias >=24-Oct (sin B; horas_malas de dias_validos_E0 fuera; dias NO_VALIDO fuera), celdas sin dia; variantes pl_no y octB_any.
IC90 bootstrap por CIERRE (Poisson, 2000, semilla fija; el mismo peso para B y virtual en el mismo cierre). Salida: A_resumen.json."""
import os, sys, glob, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; FN = H + '../fn_16nov/'
WS = (200, 500, 1000, 3000); SEED = 20261117; NB = 2000
PRIN = ['2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23']
DV = json.load(open(H + '../etapa0/dias_validos_E0.json'))['dias']
def clase_p5(v):
    if v is None or not np.isfinite(v): return 'indet'
    return 'lo' if abs(v - 19.25) <= 5 else ('hi' if abs(v - 39.5) <= 5 else 'indet')
CLc = {}
def clases(d):
    if d not in CLc:
        p = f'/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1/cache/pob_add3_{d}.json'; CL = ['indet'] * 144
        if os.path.exists(p):
            j = json.load(open(p))
            if j.get('estado') == 'COMPLETE': CL = [clase_p5(None if v is None else float(v)) for v in j['C3_suelo_rx_menos_ex']['perfil_p5_10min']]
        CLc[d] = CL
    return CLc[d]
def suelo_de(d, t):
    d0 = int(pd.Timestamp(d, tz='UTC').timestamp() * 1000); i = ((t - d0) // 600000).astype(int); CL = np.array(clases(d))
    return np.where((i >= 0) & (i < 144), CL[np.clip(i, 0, 143)], 'indet')
def bins(E):
    E = E.copy(); E['Lb'] = pd.cut(E.L, [0.095, 0.145, 0.195, 0.245, 0.305], labels=['10-14', '15-19', '20-24', '25-29']).astype(str)
    E['Tb'] = pd.cut(E['T'], [0, 150, 240, 300], labels=['60-150', '150-240', '240-300']).astype(str); E['solo'] = E.otros_L <= 1e-9; return E
# ---- brazo B real
O = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', usecols=['oid', 'size'])
B = []
for d in PRIN:
    e = pd.read_pickle(FN + f'eventos_{d}.pkl'); e = e[e.brazo == 'B'].copy(); e['suelo'] = suelo_de(d, e.t.values); B.append(e)
B = pd.concat(B, ignore_index=True).merge(O, on='oid', how='left')
B['L'] = B.P; B['fin'] = np.round(B.t / 1000 + B['T']).astype(np.int64); B['otros_L'] = np.maximum(0, B.sz - B['size']); B = bins(B)
# ---- virtual
def carga(dias, var):
    out = []
    for d in dias:
        f = H + f'A_ev_{d}.pkl'
        if not os.path.exists(f): continue
        e = pd.read_pickle(f)
        if not len(e): continue
        e = e[(~e.conB) & (e['var'] == var)]
        hm = set(DV.get(d, {}).get('horas_malas', [])); e = e[~e.hora.isin(hm)]
        out.append(e)
    return bins(pd.concat(out, ignore_index=True)) if out else None
SENS = sorted(os.path.basename(f)[5:15] for f in glob.glob(H + 'A_ev_*.pkl'))
SENS = [d for d in SENS if d >= '2026-10-24' and DV.get(d, {}).get('primaria', {}).get('estado', 'VALIDO') == 'VALIDO']
def raw(E):
    return dict(n=int(len(E)), mercados=int((E.dia + '|' + E.mid.astype(str)).nunique()), cierres=int(E.fin.nunique()), **{f'P{W}': round(float((E.dt <= W).mean()), 4) for W in WS})
def boot(EB, EV, cells, W):
    hb = (EB.dt <= W).astype(float); hv = (EV.dt <= W).astype(float)
    kB = EB[cells].astype(str).agg('|'.join, axis=1); kV = EV[cells].astype(str).agg('|'.join, axis=1)
    cov = sorted(set(kB) & set(kV)); ci = {c: i for i, c in enumerate(cov)}
    mB = kB.isin(ci); mV = kV.isin(ci)
    fins = np.unique(np.concatenate([EB.fin.values[mB.values], EV.fin.values[mV.values]])); fi = {f: i for i, f in enumerate(fins)}
    def mat(E, k, h, m):
        nM = np.zeros((len(fins), len(cov))); hM = np.zeros_like(nM)
        r = np.array([fi[f] for f in E.fin.values[m.values]]); c = np.array([ci[x] for x in k[m].values])
        np.add.at(nM, (r, c), 1); np.add.at(hM, (r, c), h[m].values); return nM, hM
    nBm, hBm = mat(EB, kB, hb, mB); nVm, hVm = mat(EV, kV, hv, mV)
    def stat(w):
        NBc = w @ nBm; HBc = w @ hBm; NVc = w @ nVm; HVc = w @ hVm
        pB = HBc.sum(-1) / NBc.sum(-1)
        with np.errstate(invalid='ignore', divide='ignore'): pv = HVc / NVc
        ok = NVc > 0; pvs = np.where(ok, NBc * np.nan_to_num(pv), 0).sum(-1) / np.where(ok, NBc, 0).sum(-1)
        return pB, pvs
    pB0, pV0 = stat(np.ones(len(fins)))
    rng = np.random.default_rng(SEED); w = rng.poisson(1.0, size=(NB, len(fins))).astype(float)
    pB, pV = stat(w); dlt = pB - pV
    q = lambda x: [round(float(np.nanquantile(x, .05)), 4), round(float(np.nanquantile(x, .95)), 4)]
    return dict(W=W, cobertura_B=round(float(mB.mean()), 4), n_B_cubiertos=int(mB.sum()), celdas=len(cov), P_B=round(float(pB0), 4), P_B_IC90=q(pB),
                P_virt_std=round(float(pV0), 4), P_virt_IC90=q(pV), dif_B_menos_virt=round(float(pB0 - pV0), 4), dif_IC90=q(dlt), p_dif_le_0=round(float((dlt <= 0).mean()), 4),
                frac_H1b_vs_anclas=round(float((pB0 - pV0) / (pB0 - 0.055)), 3), frac_H1b_IC90=q((pB - pV) / (pB - 0.055)),
                parte_golpes_B_atraida=round(float(1 - pV0 / pB0), 3), parte_IC90=q(1 - pV / pB))
res = dict(brazo_B=raw(B), brazo_B_por_suelo={s: raw(g) for s, g in B.groupby('suelo')}, brazo_B_por_solo={str(s): raw(g) for s, g in B.groupby('solo')})
C1 = ['dia', 'coin', 'Lb', 'Tb', 'suelo']; C2 = ['coin', 'Lb', 'Tb', 'suelo']
for var in ('pl_any', 'pl_no', 'octB_any'):
    V = carga(PRIN, var)
    if V is None: continue
    r = dict(virtual_raw=raw(V), virtual_por_suelo={s: raw(g) for s, g in V.groupby('suelo')}, virtual_por_solo={str(s): raw(g) for s, g in V.groupby('solo')},
             emparejado={W: boot(B, V, C1, W) for W in WS})
    r['emparejado_por_suelo'] = {s: boot(B[B.suelo == s], V[V.suelo == s], C1, 500) for s in ('lo', 'hi') if (B.suelo == s).sum() >= 30}
    r['emparejado_por_moneda'] = {c: boot(B[B.coin == c], V[V.coin == c], C1, 500) for c in ('ETH', 'SOL', 'XRP')}
    r['emparejado_por_solo'] = {str(s): boot(B[B.solo == s], V[V.solo == s], C1, 500) for s in (True, False)}
    hb = set(zip(B.dia, (B.t // 3600000) % 24)); Vh = V[[x in hb for x in zip(V.dia, V.hora)]]
    if len(Vh) > 50: r['emparejado_horas_activas_B'] = boot(B, Vh, C1, 500)
    r['emparejado_sin_dia'] = boot(B, V, C2, 500)
    res[f'PRINCIPAL_20_23oct_{var}'] = r
    if var == 'pl_any' or var == 'pl_no':
        S = carga(SENS, var)
        if S is not None:
            res[f'SENS_desde24oct_{var}'] = dict(dias=SENS, virtual_raw=raw(S), emparejado={W: boot(B, S, C2, W) for W in (500, 1000)},
                                                por_suelo={s: boot(B[B.suelo == s], S[S.suelo == s], C2, 500) for s in ('lo', 'hi') if (B.suelo == s).sum() >= 30 and (S.suelo == s).sum() >= 30},
                                                por_dia={d: raw(g) for d, g in S.groupby('dia')})
# ---- fidelidad (mercados conB): eventos virtuales pl_any vs eventos del brazo B (mismo k, mismo t, mismo L)
fid = {}
for d in PRIN:
    f = H + f'A_ev_{d}.pkl'
    if not os.path.exists(f): continue
    e = pd.read_pickle(f); e = e[e.conB & (e['var'] == 'pl_any')]; b = B[B.dia == d]
    kv = set(zip(e.k, e.t, np.round(e.L, 2))); kb = set(zip(b.k, b.t, np.round(b.L, 2)))
    fid[d] = dict(B=len(kb), virt_conB=len(kv), comunes=len(kv & kb), fid_json=json.load(open(H + f'A_fid_{d}.json')) if os.path.exists(H + f'A_fid_{d}.json') else None)
res['fidelidad_conB'] = fid
json.dump(res, open(H + 'A_resumen.json', 'w'), indent=1, default=str); print(json.dumps(res, indent=1, default=str)[:20000])
