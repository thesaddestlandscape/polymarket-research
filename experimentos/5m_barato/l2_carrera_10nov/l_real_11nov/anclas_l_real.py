#!/usr/bin/env python3
"""anclas_l_real.py -- TODAS las anclas PROPIAS ya existentes de latencia de ordenes (alta/cancelacion), SOLO LECTURA: 0 ordenes, 0 red, 0 firma.
Fuentes (datalogs, no se editan): sonda1/real/sonda1_ordenes_*.csv.gz + sonda1_eventos_*.csv.gz (Sonda1 real 30-Oct..04-Nov; WS publico propio),
sonda1/cancel_evid/cancel_evid_2026-11-04.jsonl (canal de USUARIO: ts_ex_ms = EXCHANGE), experimento_h47_B_ledger.jsonl (B real 20-23 Oct: post_lat/cancel_lat/intencion_cancel),
medir_latencia_ordenes_15m_ledger.jsonl (07-Oct, T1 GTC post-only + cancel), medir_cancelacion_delay_ledger.jsonl (14-Oct, 3 GTC reales).
Tipos de medida (reloj LOC salvo `ex`): rtt_post, rtt_cancel (envio -> respuesta), dec2send_post (t_dec -> t_call0/t_envio), dec2send_cancel (B: ts intencion -> envio),
  cancel_ex_menos_envio (canal usuario, EXCHANGE: n pequeno), cancel_visto_rx_menos_envio (WS publico propio, RECEPCION), alta_ex_menos_envio (canal usuario).
Estimador derivado de l (send -> cancelacion EFECTIVA en el exchange): eff = rtt_cancel - ACK_MENOS_EX (mediana de las anclas de canal de usuario: RTT - (ex - envio)), una sola constante, y
variante pesimista eff_pes = rtt_cancel - 22 (todo el exceso de cola en la subida). l = d_proc + eff, con d_proc (rx del disparo -> envio del DELETE) NO medido en un bucle de disparo real (B mide ~0 ms
entre intencion y llamada, pero esa intencion se escribe justo antes del DELETE); se declara 0-5 ms y lo medira el dry-run (columna t_dec_rx -> t_send_virtual).
Epocas (CAUSA_SUELO_Y_LATENCIA_11nov.md): feed lento 17-Oct 08:35..27-Oct ~11:50 (B 20-23 Oct); Rescale (4 -> 8 vCPU) 22-Oct 09:58:31Z (carga local: p50 POST 110 -> 75 ms).
Salida: out/anclas_l_real.json (+ stdout). Un fichero cada vez; nice 19."""
import os, sys, json, glob, gzip, collections
import numpy as np, pandas as pd
from datetime import datetime
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = H + 'out/'; os.makedirs(OUT, exist_ok=True)
DL = '/root/polymarket-research-datalogs/'
RESCALE = datetime.fromisoformat('2026-10-22T09:58:31+00:00').timestamp()
RNG = np.random.default_rng(20261111)


def T(s): return datetime.fromisoformat(s).timestamp()


def pct(v, boot=True):
    v = np.asarray([x for x in v if x is not None and np.isfinite(x)], float)
    if len(v) == 0: return dict(n=0)
    r = dict(n=int(len(v)), p10=float(np.percentile(v, 10)), p50=float(np.median(v)), p90=float(np.percentile(v, 90)), min=float(v.min()), max=float(v.max()))
    if boot and len(v) >= 5:
        b = RNG.integers(0, len(v), (2000, len(v))); s = v[b]
        r['p50_ic90'] = [float(np.percentile(np.median(s, 1), 5)), float(np.percentile(np.median(s, 1), 95))]
        r['p90_ic90'] = [float(np.percentile(np.percentile(s, 90, axis=1), 5)), float(np.percentile(np.percentile(s, 90, axis=1), 95))]
    return r


def sonda():
    fs = sorted(glob.glob(DL + 'sonda1/real/sonda1_ordenes_2026-1*.csv*'))
    O = pd.concat([pd.read_csv(f, dtype={'oid': str}) for f in fs]).drop_duplicates('oid').set_index('oid')       # job1638211 repite 8 oid de 04-Nov
    ev = pd.concat([pd.read_csv(f, dtype={'oid': str}) for f in sorted(glob.glob(DL + 'sonda1/real/sonda1_eventos_2026-1*.csv.gz'))]).drop_duplicates()
    ev = ev[ev.tipo == 'nivel'].copy(); ev['d'] = ev.size_nuevo - ev.size_viejo; byoid = {o: g for o, g in ev.groupby('oid')}
    R = dict(rtt_post=[], rtt_cancel=[], dec2send_post=[], cancel_visto_rx_menos_envio=[], alta_visto_rx_menos_envio=[], por_dia_rtt_cancel=collections.defaultdict(list), por_dia_rtt_post=collections.defaultdict(list))
    cv_cand = []
    for oid, r in O.iterrows():
        R['rtt_post'].append(r.t_ack_ms - r.t_envio_ms); R['dec2send_post'].append(r.t_envio_ms - r.t_decision_ms); R['por_dia_rtt_post'][r.dia].append(r.t_ack_ms - r.t_envio_ms)
        has_c = pd.notna(r.t_cancel_envio_ms)
        if has_c: R['rtt_cancel'].append(r.t_cancel_ack_ms - r.t_cancel_envio_ms); R['por_dia_rtt_cancel'][r.dia].append(r.t_cancel_ack_ms - r.t_cancel_envio_ms)
        e = byoid.get(oid)
        if e is None: continue
        if has_c:                                                      # cancelacion VISTA en el WS publico: primer 'nivel' con delta == -size tras el envio; solo candidatas unicas (<=2 eventos en [envio, ack+400])
            c = e[(e.t_recv_ms >= r.t_cancel_envio_ms - 5) & ((e.d + r['size']).abs() < 0.011)]
            win = e[(e.t_recv_ms >= r.t_cancel_envio_ms - 5) & (e.t_recv_ms <= r.t_cancel_ack_ms + 400)]
            if len(c) and len(win) <= 2 and 0 <= c.t_recv_ms.iloc[0] - r.t_cancel_envio_ms <= 400: R['cancel_visto_rx_menos_envio'].append(float(c.t_recv_ms.iloc[0] - r.t_cancel_envio_ms))
        a = e[(e.t_recv_ms >= r.t_envio_ms) & ((e.d - r['size']).abs() < 0.011)]
        win = e[(e.t_recv_ms >= r.t_envio_ms) & (e.t_recv_ms <= r.t_ack_ms + 300)]
        if len(a) and len(win) <= 2 and 0 <= a.t_recv_ms.iloc[0] - r.t_envio_ms <= 400: R['alta_visto_rx_menos_envio'].append(float(a.t_recv_ms.iloc[0] - r.t_envio_ms))
    return R, len(O)


def usuario_sonda():
    """canal de usuario (EXCHANGE): alta{t_envio_ms,t_ack_ms} + user_order{ts_ex_ms} + cancel_try{t_pre_ms,t_resp_ms}. 04-Nov (unico dia con registro de canal de usuario)."""
    f = DL + 'sonda1/cancel_evid/cancel_evid_2026-11-04.jsonl'; ev = [json.loads(l) for l in open(f) if l.strip().startswith('{')]
    alta = {e['oid']: e for e in ev if e.get('k') == 'alta'}; uo = collections.defaultdict(dict)
    for e in ev:
        if e.get('k') == 'user_order' and e.get('mine'): uo[e['oid']].setdefault(e['tipo'], e)
    cc = {e['oid']: e for e in ev if e.get('k') == 'cancel_try' and e.get('canceled')}
    R = dict(alta_ex_menos_envio=[], alta_ack_menos_ex=[], cancel_ex_menos_envio=[], cancel_ack_menos_ex=[], cancel_user_rx_menos_ex=[])
    for oid, a in alta.items():
        p = uo.get(oid, {}).get('PLACEMENT')
        if p: R['alta_ex_menos_envio'].append(p['ts_ex_ms'] - a['t_envio_ms']); R['alta_ack_menos_ex'].append(a['t_ack_ms'] - p['ts_ex_ms'])
        c = uo.get(oid, {}).get('CANCELLATION')
        if c and oid in cc:
            R['cancel_ex_menos_envio'].append(c['ts_ex_ms'] - cc[oid]['t_pre_ms']); R['cancel_ack_menos_ex'].append(cc[oid]['t_resp_ms'] - c['ts_ex_ms']); R['cancel_user_rx_menos_ex'].append(c['t_recv_ms'] - c['ts_ex_ms'])
    return R


def breal():
    ic = {}; cl = {}; pl = {}; pp = {}
    for l in open(DL + 'experimento_h47_B_ledger.jsonl'):
        try: d = json.loads(l)
        except Exception: continue
        t = d.get('tipo')
        if t == 'intencion_cancel': ic[d['oid']] = T(d['ts'])
        elif t == 'cancel_lat' and d.get('ok'): cl[d['oid']] = (T(d['ts']), d['ms'])
        elif t == 'post_lat': pl[d['oid']] = d
        elif t == 'puja_post': pp[d['oid']] = d
    ep = lambda ts: 'B_20-22Oct_pre_rescale_4vCPU' if ts < RESCALE else 'B_22-23Oct_post_rescale_8vCPU'
    R = collections.defaultdict(lambda: collections.defaultdict(list))
    for o, d in pl.items():
        e = ep(T(d['ts'])); R[e]['rtt_post'].append(d['ms']); R['B_todo']['rtt_post'].append(d['ms'])
        if o in pp: R[e]['dec2send_post'].append((d['t_call0'] - pp[o]['t_dec']) * 1000)
    for o, (ts, ms) in cl.items():
        e = ep(ts); R[e]['rtt_cancel'].append(ms); R['B_todo']['rtt_cancel'].append(ms)
        if o in ic: R[e]['dec2send_cancel'].append((ts - ms / 1000 - ic[o]) * 1000)
    return R


def t1_7oct():
    R = collections.defaultdict(list); last = {}
    for l in open(DL + 'medir_latencia_ordenes_15m_ledger.jsonl'):
        d = json.loads(l); t = d['tipo']
        if t == 'T1_post': R['rtt_post'].append(d['ms'])
        elif t == 'T1_cancel': R['rtt_cancel'].append(d['ms'])
    c14 = [float(json.loads(l)['post_ms']) for l in open(DL + 'medir_cancelacion_delay_ledger.jsonl') if '"post_ms"' in l and json.loads(l).get('tipo') == 'GTC']
    R['rtt_post_14oct'] = c14
    return R


def main():
    S, nS = sonda(); U = usuario_sonda(); B = breal(); T1 = t1_7oct()
    ack_ex = float(np.median(U['cancel_ack_menos_ex']))                       # RTT - (ex - envio) en cancelaciones con canal de usuario (n=4)
    out = dict(generado=datetime.utcnow().isoformat() + 'Z', ack_menos_ex_cancel_p50=ack_ex, n_sonda_ordenes=nS, tabla={}, por_dia_sonda={}, derivado={}, notas=[])
    tab = out['tabla']
    tab['sonda_rtt_post'] = pct(S['rtt_post']); tab['sonda_rtt_cancel'] = pct(S['rtt_cancel']); tab['sonda_dec2send_post'] = pct(S['dec2send_post'])
    tab['sonda_cancel_visto_ws_publico_rx_menos_envio'] = pct(S['cancel_visto_rx_menos_envio']); tab['sonda_alta_visto_ws_publico_rx_menos_envio'] = pct(S['alta_visto_rx_menos_envio'])
    for k, v in U.items(): tab['usuario_' + k] = pct(v, boot=False)
    for e, d in B.items():
        for k, v in d.items(): tab[f'{e}_{k}'] = pct(v)
    tab['T1_7oct_rtt_post'] = pct(T1['rtt_post']); tab['T1_7oct_rtt_cancel'] = pct(T1['rtt_cancel']); tab['GTC_14oct_post_ms'] = pct(T1['rtt_post_14oct'], boot=False)
    out['por_dia_sonda'] = {k: {d: pct(v, boot=False) for d, v in S[k].items()} for k in ('por_dia_rtt_post', 'por_dia_rtt_cancel')}
    # ---- l efectivo (send -> cancelacion efectiva en el exchange) derivado de RTT de cancelacion
    pools = {'sonda_fast_8vCPU(30Oct-04Nov)': S['rtt_cancel'], 'T1_7oct_fast_4vCPU': T1['rtt_cancel'], 'B_22-23Oct_post_rescale': B['B_22-23Oct_post_rescale_8vCPU']['rtt_cancel'],
             'B_20-22Oct_pre_rescale': B['B_20-22Oct_pre_rescale_4vCPU']['rtt_cancel']}
    for nm, v in pools.items():
        v = np.asarray(v, float); out['derivado'][nm] = dict(rtt=pct(v), eff_rtt_menos_ack=pct(v - ack_ex), eff_pes_rtt_menos_22=pct(v - 22.0),
                                                                eff_mitad_exceso=pct(35.0 + (v - np.median(v)) / 2.0))
    out['pool_empirico_l'] = dict(descripcion='eff = rtt_cancel - ack_ex, pool = Sonda(30Oct-04Nov) U B(22-23Oct post-Rescale); lo usa passT_cxb_l.py para la variante `emp`',
                                  valores=sorted(float(x - ack_ex) for x in list(S['rtt_cancel']) + list(B['B_22-23Oct_post_rescale_8vCPU']['rtt_cancel'])))
    out['pool_empirico_l']['n'] = len(out['pool_empirico_l']['valores']); out['pool_empirico_l']['pct'] = pct(out['pool_empirico_l']['valores'], boot=False)
    json.dump(out, open(OUT + 'anclas_l_real.json', 'w'), indent=1)
    def fmt(d): return ' '.join(f"{k}={d[k]:.0f}" if isinstance(d.get(k), float) else '' for k in ('p10', 'p50', 'p90')) + (f" p50_ic90=({d['p50_ic90'][0]:.0f},{d['p50_ic90'][1]:.0f})" if 'p50_ic90' in d else '') + (f" p90_ic90=({d['p90_ic90'][0]:.0f},{d['p90_ic90'][1]:.0f})" if 'p90_ic90' in d else '')
    for k, v in tab.items(): print(f"{k:60s} n={v.get('n', 0):5d} {fmt(v) if v.get('n') else ''}")
    print('ack_menos_ex_cancel_p50 (usuario, n=%d):' % len(U['cancel_ack_menos_ex']), ack_ex)
    for k, v in out['derivado'].items(): print('DERIVADO', k, 'rtt', fmt(v['rtt']), '| eff(rtt-ack)', fmt(v['eff_rtt_menos_ack']), '| eff_pes(rtt-22)', fmt(v['eff_pes_rtt_menos_22']))
    print('pool empirico l: n=%d' % out['pool_empirico_l']['n'], fmt(out['pool_empirico_l']['pct']))


if __name__ == '__main__': main()
