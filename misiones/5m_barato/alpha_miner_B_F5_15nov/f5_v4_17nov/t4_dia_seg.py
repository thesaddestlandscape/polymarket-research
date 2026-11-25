#!/usr/bin/env python3
"""t4_dia_seg.py DIA [--smoke N] -- (17-Nov, tarea 2 de Javi: detector rapido lo<->hi). UNA pasada zcat|awk de m5_registro_DIA (solo lectura): cuentas POR SEGUNDO de RX de las mismas filas q que t2_dia_v4 (tokens 5min, bid [0,03;0,45]) en bandas de d = rx-ex de 2 ms:
banda 0 = d<=9, banda b (1..25) = d en [10+2(b-1), 11+2(b-1)], banda 26 = d>=60 (27 bandas). -> cache/seg_D.npz (int32 [86400, 27]). Idempotente (manifiesto cache/segman_D.json con code/entrada; salida validada); atomico.
Control: suma total == hist_filas de cache/manifest_D.json (mismas filas). 0 ordenes."""
import os, sys, json, hashlib, subprocess, time
HERE = os.path.dirname(os.path.abspath(__file__)); import numpy as np, pandas as pd
CACHE4 = HERE + '/cache/'; REG = '/mnt/HC_Volume_106538179/m5_registro/'; EXPC = '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1/cache/'
D = sys.argv[1]; SMOKE = int(sys.argv[sys.argv.index('--smoke') + 1]) if '--smoke' in sys.argv else 0; pre = CACHE4 + ('smoke_' if SMOKE else ''); MAN = pre + f'segman_{D}.json'; OUTP = pre + f'seg_{D}.npz'; NB = 27
CODE = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()[:12]; fich = REG + f'm5_registro_{D}.csv.gz'; st = os.stat(fich); ENT = dict(bytes=st.st_size, mtime=int(st.st_mtime))
def valida(m):
    try: z = np.load(OUTP)['S']; return m.get('estado') == 'COMPLETE' and m['code'] == CODE and m['entrada'] == ENT and m['smoke'] == SMOKE and z.shape == (86400, NB) and int(z.sum()) == m['filas']
    except Exception: return False
if os.path.exists(MAN):
    try: ok = valida(json.load(open(MAN)))
    except Exception: ok = False
    if ok: print(D, 'seg ya COMPLETE y valido'); sys.exit(0)
t0 = time.time(); man = dict(job='t4_dia_seg', dia=D, estado='RUNNING', code=CODE, entrada=ENT, smoke=SMOKE); json.dump(man, open(MAN, 'w'))
def ant(d): return (pd.Timestamp(d) - pd.Timedelta(days=1)).strftime('%Y-%m-%d')
try:
    kp = [p for p in (EXPC + f'add3_k_{ant(D)}.csv', EXPC + f'k_{ant(D)}.csv', CACHE4 + f'k_{ant(D)}.csv') if os.path.exists(p)]
    toks = set()
    for p in kp[:1]:
        for ln in open(p):
            c = ln.split(',')
            if len(c) > 7: toks.add(c[2])
    tag = pre + f'_seg_{D}_'; open(tag + 'kall.txt', 'w').write('\n'.join(toks) + '\n'); d0 = int(pd.Timestamp(D + 'T00:00:00Z').value // 10**6)
    prog = r'''BEGIN{FS=","; split(COINS,cs,","); for(i in cs) C[cs[i]]=1}
FILENAME==KPF{ if($1!="") K[$1]=1; next }
$1=="k" && $5=="5min" && ($4 in C) {K[$3]=1; next}
$1=="q" && ($3 in K) && $4>=0.03 && $4<=0.45 { rx=$8; if(rx>=D0 && rx<D1){ d=rx-$2; b=(d<=9)?0:((d>=60)?26:int((d-10)/2)+1); S[int((rx-D0)/1000)*32+b]++ } }
END{for(k in S) print k","S[k] > HOUT}'''
    src = f"zcat {fich}" + (f" | head -n {SMOKE}" if SMOKE else '')
    cmd = f"{src} | awk -v COINS=ETH,SOL,XRP,BTC,DOGE,BNB -v KPF={tag}kall.txt -v D0={d0} -v D1={d0 + 86400000} -v HOUT={tag}h.csv '{prog}' {tag}kall.txt -"
    r = subprocess.run(['bash'] + ([] if SMOKE else ['-o', 'pipefail']) + ['-c', cmd], capture_output=True, text=True); assert r.returncode == 0, 'awk: ' + r.stderr[-300:]
    open(tag + 'h.csv', 'a').close(); S = np.zeros((86400, NB), np.int32)
    if os.path.getsize(tag + 'h.csv'):
        h = pd.read_csv(tag + 'h.csv', header=None, names=['k', 'n'], dtype=np.int64); s, b = h.k.values // 32, h.k.values % 32; assert (s >= 0).all() and (s < 86400).all() and (b < NB).all(), 'indices'; S[s, b] = h.n.values
    man.update(filas=int(S.sum()), segundos_con_datos=int((S.sum(1) > 0).sum()), k_prev=kp[0] if kp else None)
    if not SMOKE:
        hm = json.load(open(CACHE4 + f'manifest_{D}.json')); man['control_hist_filas'] = hm['hist_filas']; assert man['filas'] == hm['hist_filas'], f"filas {man['filas']} != hist_filas {hm['hist_filas']}"
    np.savez_compressed(OUTP + '.tmp.npz', S=S); os.replace(OUTP + '.tmp.npz', OUTP); man.update(estado='COMPLETE', duracion_s=round(time.time() - t0)); json.dump(man, open(MAN, 'w'), indent=1)
    for s_ in ('kall.txt', 'h.csv'): os.remove(tag + s_)
    print(D, 'seg COMPLETE filas', man['filas'], 'control', man.get('control_hist_filas'), 's', man['duracion_s'])
except AssertionError as e:
    man.update(estado='FAILED', error=str(e)[:300]); json.dump(man, open(MAN, 'w'), indent=1); print(D, 'FAILED', man['error']); sys.exit(1)
