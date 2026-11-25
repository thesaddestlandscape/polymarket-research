#!/usr/bin/env python3
"""verif_datos_b.py -- FASE B, pendientes 4 y 5 (LIGERO, solo lectura, sin motor): (a) YES == Up en los tokens de B contra gamma (GET publico de lectura; fail-closed si no se puede verificar);
(b) cruce m5_registro vs x_*.csv.gz de Sonda1 (dev) en una ventana corta (1 h) de 17 y 18 Nov (filas x: sym, px, qty, recv); (c) % de instantes sin dato Binance fresco por moneda (proxy de 'altas sin dato':
muestra uniforme de instantes, ventanas de retorno de V5=1 s y V6=2 s, regla de passT: ultimo tick <=15 s y j0>=0). Las altas REALES de B (con su t) quedan para el runner de FASE B.
Uso: python3 verif_datos_b.py [--hora 10] [--dias 2026-11-17,2026-11-18] [--sin-red]. Salida: out_fase_b/verif_datos_b.json (atomico). 0 ordenes, 0 escritura en data/."""
import sys, os, json, gzip, subprocess, time, urllib.request, calendar, argparse
import numpy as np
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import variantes_b as VB
M5 = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz'; XD = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/fwd/x_%s.csv.gz'
GAMMA = 'https://gamma-api.polymarket.com/markets/%s'
BCOINS = ('ETHUSDT', 'SOLUSDT', 'XRPUSDT')

def ts0(dia, hora): return calendar.timegm(time.strptime(f'{dia} {hora:02d}', '%Y-%m-%d %H')) * 1000
def x_rows(path, a, b):
    """filas x con recv en [a, b) -> {sym: (recv[], px[], qty[])}; filtra por streaming (awk), nunca carga el fichero."""
    cmd = f"zcat '{path}' | awk -F, -v a={a} -v b={b} '$1==\"x\" && $8>=a && $8<b {{print $3\",\"$4\",\"$5\",\"$8}}'"
    out = subprocess.run(['bash', '-c', cmd], capture_output=True, text=True, timeout=900).stdout.splitlines(); d = {}
    for l in out:
        s, p, q, r = l.split(','); d.setdefault(s, []).append((int(r), float(p), float(q)))
    return {s: tuple(np.array(c) for c in zip(*v)) for s, v in d.items()}

def cruce(dia, hora):
    a = ts0(dia, hora); b = a + 3600_000; A = x_rows(M5 % dia, a, b); B = x_rows(XD % dia, a, b); res = {}
    for s in BCOINS:
        if s not in A or s not in B: res[s] = dict(estado='FALTA', en_m5=int(len(A.get(s, ([],))[0])), en_x=int(len(B.get(s, ([],))[0]))); continue
        ka = set(zip(A[s][0].tolist(), A[s][1].tolist(), A[s][2].tolist())); kb = set(zip(B[s][0].tolist(), B[s][1].tolist(), B[s][2].tolist()))
        inter = len(ka & kb); res[s] = dict(en_m5=len(ka), en_x=len(kb), comunes=inter, frac_m5_en_x=inter / max(len(ka), 1), frac_x_en_m5=inter / max(len(kb), 1), estado='OK' if len(ka) and inter / len(ka) >= 0.999 and inter / max(len(kb), 1) >= 0.999 else 'DIFIERE')
    return res, A

def sin_dato(A, dia, hora, paso_ms=1000):
    """proxy de 'altas sin dato': instante tq uniforme cada paso_ms; sin dato = ret_bps NaN (j0<0, j1<0 o ultimo tick > 15 s) con w=1000 (V5) y w=2000 (V6); ademas p95 y max del hueco entre ticks."""
    a = ts0(dia, hora); q = np.arange(a + 5000, a + 3600_000, paso_ms, dtype=np.int64); out = {}
    for s in BCOINS:
        if s not in A: out[s] = dict(estado='FALTA'); continue
        t, p = VB.ordena_rx(A[s][0], A[s][1]); gap = np.diff(t)
        out[s] = dict(n_ticks=int(len(t)), pct_sin_dato_w1000=float(np.isnan(VB.ret_bps(t, p, q, 1000)).mean()), pct_sin_dato_w2000=float(np.isnan(VB.ret_bps(t, p, q, 2000)).mean()),
                      gap_p95_ms=float(np.percentile(gap, 95)) if len(gap) else None, gap_max_ms=int(gap.max()) if len(gap) else None, n_gaps_mayor_15s=int((gap > 15000).sum()), pasos_negativos_recv_en_fichero=None)
    return out

def yes_es_up(dia, n_por_moneda=12, red=True):
    """YES == Up: de las filas k de m5_registro (id, coin, tf, market, fin, lado) toma n mercados 5m por moneda y comprueba en gamma que el token YES == clobTokenIds[outcomes.index('Up')]. Fail-closed: sin red o cualquier discrepancia -> no verificado."""
    if not red: return dict(estado='NO_VERIFICADO', motivo='--sin-red')
    cmd = f"zcat '{M5 % dia}' | head -700000 | awk -F, '$1==\"k\" && $5==\"5min\" && $8==\"YES\" {{print $3\",\"$4\",\"$6}}'"; rows = subprocess.run(['bash', '-c', cmd], capture_output=True, text=True, timeout=300).stdout.splitlines()
    por = {}
    for l in rows:
        tok, coin, mk = l.split(','); por.setdefault(coin, []).append((tok, mk))
    res = dict(por_moneda={}, discrepancias=[]); n_ok = 0; n_tot = 0
    for coin in ('ETH', 'SOL', 'XRP'):
        c = por.get(coin, [])[::max(1, len(por.get(coin, [])) // n_por_moneda)][:n_por_moneda]; ok = 0
        for tok, mk in c:
            try:
                g = json.loads(urllib.request.urlopen(GAMMA % mk, timeout=10).read()); outs = json.loads(g['outcomes']); ids = json.loads(g['clobTokenIds']); good = outs.index('Up') < len(ids) and ids[outs.index('Up')] == tok and 'Down' in outs
            except Exception as ex: res['discrepancias'].append(dict(coin=coin, market=mk, err=repr(ex)[:120])); n_tot += 1; continue
            n_tot += 1; ok += int(good); n_ok += int(good)
            if not good: res['discrepancias'].append(dict(coin=coin, market=mk, outcomes=outs, motivo='YES != Up'))
            time.sleep(0.15)
        res['por_moneda'][coin] = dict(n=len(c), ok=ok)
    res['estado'] = 'VERIFICADO' if n_tot > 0 and n_ok == n_tot and all(v['n'] >= 5 for v in res['por_moneda'].values()) else 'NO_VERIFICADO'; res['n_ok'] = n_ok; res['n_total'] = n_tot; return res

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--hora', type=int, default=10); ap.add_argument('--dias', default='2026-11-17,2026-11-18'); ap.add_argument('--sin-red', action='store_true'); a = ap.parse_args()
    out = dict(job='verif_datos_b', ventana=f'{a.hora:02d}:00-{a.hora + 1:02d}:00Z', dias={}, etiqueta='LIGERO; muestra de 1 h por dia; proxy de altas sin dato (instantes uniformes), no las altas reales de B')
    for d in a.dias.split(','):
        c, A = cruce(d, a.hora); out['dias'][d] = dict(cruce_m5_vs_x=c, sin_dato_proxy=sin_dato(A, d, a.hora))
    out['yes_es_up'] = yes_es_up(a.dias.split(',')[0], red=not a.sin_red)
    os.makedirs(HV + 'out_fase_b/', exist_ok=True); p = HV + 'out_fase_b/verif_datos_b.json'; json.dump(out, open(p + '.tmp', 'w'), indent=1, default=str); os.replace(p + '.tmp', p)
    print(json.dumps({d: {k: {s: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items() if kk in ('estado', 'frac_m5_en_x', 'frac_x_en_m5', 'pct_sin_dato_w1000', 'pct_sin_dato_w2000', 'n_gaps_mayor_15s')}) for s, v in dd.items()} for k, dd in dv.items()} for d, dv in out['dias'].items()}, default=str)[:1800]); print('yes_es_up', out['yes_es_up']['estado'], out['yes_es_up'].get('n_ok'), '/', out['yes_es_up'].get('n_total'), out['yes_es_up'].get('discrepancias', [])[:2])
