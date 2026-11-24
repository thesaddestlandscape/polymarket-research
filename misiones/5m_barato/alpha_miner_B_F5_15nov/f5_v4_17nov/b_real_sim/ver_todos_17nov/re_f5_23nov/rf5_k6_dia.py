#!/usr/bin/env python3
"""rf5_k6_dia.py [dia ...] -- JUEZ CALMA v4 (ESPEC_HOOK_CALMA_V4_23nov, ADENDA_RF5_K6_CALMA_v2): simula K6 = K1 + Calma-T1 (y sus LOO, lc 111/147, sensibilidad tq=t, Calma sola) como UNA sola simulacion (HookRF5 con Calma de tercer componente) sobre cada dia
con manifest rf5dia COMPLETE. Misma cinta, mismo motor passT_v4, misma t_proc/L_cancel y fuentes de Binance (m5_registro) que K1. Escribe rf5K6_D.pkl + manifest_rf5K6_D.json (cobertura de Calma, NO_EVALUABLE_CALMA, particion por primera regla, Calma∩F3).
Sin dato => NO_EVALUABLE ese dia (K1-K5 siguen). Solo CONTEOS: no imprime EV/PnL. Idempotente (COMPLETE con mismo codigo se salta). Cron 11:50Z (run_k6.sh); un job pesado a la vez (cron_pesado)."""
import sys, os, json, time
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import numpy as np, pandas as pd
import rf5_run as RR, rf5_core as K5, calma_hook as CH
RU, FB, HU = RR.RU, RR.FB, RR.HU; OUT = RR.OUT; ts, log, atomic_json, atomic_pkl = RR.ts, RR.log, RR.atomic_json, RR.atomic_pkl

def particion(R, HK):
    """conteo de ordenes colocadas por PRIMERA regla que las cancela (V5/V6/CALMA, orden fijo en empate) o 'ninguna'; F3/F5 vetan antes de colocar (no hay orden). tambien_Calma = Calma habria disparado igual. Solo conteos."""
    out = {'V5': 0, 'V6': 0, 'CALMA': 0, 'ninguna': 0}
    for o in R.itertuples():
        q = HK.quien.get((o.mid, int(o.n_ord)))
        pr = 'ninguna' if not q else q.split('+')[0]; out[pr] = out.get(pr, 0) + 1
    out['total'] = int(len(R)); out['suma_ok'] = bool(sum(v for k, v in out.items() if k not in ('total', 'suma_ok')) == len(R)); return out

def calma_inter_f3(R, HK):
    """ordenes colocadas en un (mid,k) que F3 habria vetado: debe ser 0 (el veto F3 de entrada precede a todo)."""
    return int(sum(bool(HK.vetado.get((o.mid, int(o.k)), False)) for o in R.itertuples()))

def run_K6(d):
    import b_policy_sim as BS, eng_v5 as EV
    tp = RR.t_proc()
    if tp is None: raise RuntimeError('BLOCKED_T_PROC')
    cortes = K5.lee_cortes(); bsrc = FB.carga_binance(d)
    if not bsrc: raise RuntimeError('DATA_BLOCKED: sin m5_registro Binance (ETH/SOL/XRP) para Calma en %s' % d)
    with RR.desenlace_con_marcador() as unres:
        E, info = EV.build(d); P = BS.params(); Rs = []; cov = dict(motor=info, t_proc_ms=tp, jobs={}, binance_coins=sorted(bsrc), sha_calma_gate=CH.verifica_gate())
        RR.GAPS = HU.gaps_de_motor(E); RR.GAPS_BN = HU.gaps_binance(bsrc); cov['huecos_ms'] = RR._res_huecos(RR.GAPS); cov['huecos_binance'] = RR._res_huecos(RR.GAPS_BN)
        for bloq in (0, 1):
            W = RR.motor(E, bool(bloq)); ctx = dict(W=W, serie=W._serie)
            for nombre in K5.POLITICAS_K6:
                if bloq == 1 and nombre != 'K6': continue
                R, c, HK = RR._replay(d, P, W, ctx, nombre, K5.POLITICAS_K6, bsrc, cortes, tp, None)
                if len(R): Rs.append(RR._col(R, bloq, unres))
                j = dict(ordenes=int(len(R)), rellenos=int((R.q > 0).sum()) if len(R) else 0, contadores=dict(HK.cont), saltados=c.get('skip'), quien_cancela=pd.Series(list(HK.quien.values())).value_counts().to_dict() if HK.quien else {})
                if HK.calma is not None: j['calma'] = dict(contadores=dict(HK.calma.cont), delay_armar_ms=HK.calma.delay_armar_ms)
                if nombre == 'K6' and bloq == 0:
                    j['particion'] = particion(R, HK) if len(R) else {}; j['calma_inter_f3'] = calma_inter_f3(R, HK) if len(R) else 0; cov['calma_evaluable'] = CH.estado_evaluable(HK.calma.cont, set(bsrc))
                cov['jobs'][f'bloq{bloq}/{nombre}'] = j
        RA = pd.concat(Rs, ignore_index=True); cov['c3'] = RR.c3_lados(RA); cov['desenlace_sin_resolver_mercados'] = len(unres)
    atomic_pkl(OUT + f'rf5K6_{d}.pkl', RA)
    return dict(etiqueta='CONTEOS; sin EV', evaluable=cov['calma_evaluable']['estado'], politicas={k: dict(ordenes=v['ordenes'], rellenos=v['rellenos']) for k, v in cov['jobs'].items()}), cov

def procesa(d):
    m = RR.lee_dia(d)
    if not m or m.get('status') != 'COMPLETE': log('K6 omitido (rf5dia no COMPLETE)', d, (m or {}).get('status')); return 'SALTADO'
    needs = dict(RU.inputs_dia(d), m5=FB.M5 % d, ms2=RR.SA2 + f'ms2_{d}.npz')
    return RU.job('rf5K6', d, [f'rf5K6_{d}.pkl'], run_K6, needs)

if __name__ == '__main__':
    dias = sys.argv[1:] or sorted(f[len('manifest_rf5dia_'):-5] for f in os.listdir(OUT) if f.startswith('manifest_rf5dia_') and f.endswith('.json')); rc = 0
    for d in dias:
        if d < '2026-11-18': continue                  # calendario ciego
        try: r = procesa(d)
        except Exception: import traceback; traceback.print_exc(); r = 'FAILED'
        print(ts(), 'K6', d, r); rc |= int(r in ('FAILED',))
    sys.exit(rc)
