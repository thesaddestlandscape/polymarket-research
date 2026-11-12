#!/usr/bin/env python3
"""replay_runner_vs_modeB.py DIA --coin ETH --horas H0 H1 [--out DIR] -- B (12-Nov): REPRODUCCION barata del RUNNER sobre datos REALES de un dia TRAIN (<= 2026-11-09; HOLD >= 10-Nov prohibido), SIN el preambulo del motor (RSS ~1 GB).
1) Convierte las filas k/q/t de sa_ms2/ms2_<D>.npz de UN subconjunto (moneda x franja horaria: tokens 5m, sus complementarios y los 15m) a un fichero `maker_ms_<D>_replay.csv.gz` con el FORMATO del registro ms (q: ex,tok,bid,ask,szb,sza,rx; t: ex,tok,precio,lado,size,rx; flotas
   con repr(float(float32)) para que el parseo de texto reproduzca exactamente los float64 del modo B de replay_train), ordenado por rx, en miembros gz de 50k lineas (ejercita el lector incremental).
2) Ejecuta `cxb60_dryrun_fase0.py --once` (CON verificacion de hashes) sobre ese fichero.
3) Calcula EN PROCESO lo mismo con los buffers de las filas del npz (TokBuf + TokenFeats + make_live_fill + Market.advance(1e18): modo B de replay_train) y compara fila a fila (tok, L, var, seg) -> t_dec_rx, t_arr, t_end, canc, q, tf, motivo_fin, t_trig_rx.
Criterio: 0 diferencias en los mercados que el runner NO salto (los saltados, p.ej. incompleto_arranque, se listan). Es el puente runner==nucleo con datos reales (parseo, lectura incremental, W, causalidad por SETTLE); la exactitud del NUCLEO vs el motor original (modo A) la da replay_train.py.
Memoria: carga las columnas del npz una a una (q_k primero) y solo conserva las filas del subconjunto."""
import os, sys, json, time, gzip, subprocess, math, datetime as dt, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import cxb60_core as C, cxb60_io as IO

D_ = sys.argv[1]; assert D_ <= '2026-11-09', 'HOLD >= 10-Nov no se usa'
coin = sys.argv[sys.argv.index('--coin') + 1]; h0, h1 = int(sys.argv[sys.argv.index('--horas') + 1]), int(sys.argv[sys.argv.index('--horas') + 2])
OUT = (sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else HERE + f'out_replay/runner_vs_B_{D_}_{coin}/').rstrip('/') + '/'; os.makedirs(OUT, exist_ok=True); T0 = time.time()
z = np.load('/root/polymarket-research-datalogs/sa_ms2/' + f'ms2_{D_}.npz', allow_pickle=True); t0 = int(z['t0']); TOK = [str(x) for x in z['tokens']]; TM = z['tmap']
iso = lambda s: int(dt.datetime.fromisoformat(str(s).replace(' ', 'T')).timestamp())
info = {i: dict(tok=TOK[i], coin=str(TM[i, 0]), marco=str(TM[i, 1]), mid=str(TM[i, 2]), fin=iso(TM[i, 3]), fin_s=str(TM[i, 3]), lado=str(TM[i, 4])) for i in range(len(TOK))}
d0 = int(dt.datetime.fromisoformat(D_ + 'T00:00:00+00:00').timestamp()); by5 = {(m['mid'], m['lado']): i for i, m in info.items() if m['marco'] == '5min'}; by15 = {(m['coin'], m['fin'], m['lado']): i for i, m in info.items() if m['marco'] == '15min'}
sel5 = [i for i, m in info.items() if m['marco'] == '5min' and m['coin'] == coin and d0 + h0 * 3600 + 300 <= m['fin'] <= d0 + h1 * 3600]
need = set(sel5)
for i in sel5:
    m = info[i]; c = by5.get((m['mid'], 'NO' if m['lado'] == 'YES' else 'YES')); f15 = int(math.ceil(m['fin'] / 900.0) * 900)
    for lado in ('YES', 'NO'):
        j = by15.get((coin, f15, lado)); need.add(j) if j is not None else None
    need.add(c) if c is not None else None
need = sorted(x for x in need if x is not None); print('tokens seleccionados', len(need), 'mercados 5m (tokens)', len(sel5), flush=True)
qk = z['q_k']; mq = np.isin(qk, np.array(need, dtype=qk.dtype)); iq = np.flatnonzero(mq); del mq
Q = dict(k=qk[iq].astype(np.int64), ex=z['q_t_ex'][iq].astype(np.int64) + t0, rx=z['q_t_rx'][iq].astype(np.int64), v=[z[f'q_v{j}'][iq] for j in range(4)]); del qk
Q['ok'] = Q['rx'] >= 0; Q['rx'] = Q['rx'] + t0; tk = z['t_k']; it = np.flatnonzero(np.isin(tk, np.array(need, dtype=tk.dtype)))
Tt = dict(k=tk[it].astype(np.int64), ex=z['t_t_ex'][it].astype(np.int64) + t0, rx=z['t_t_rx'][it].astype(np.int64), pr=z['t_pr'][it], sd=z['t_sd'][it], sz=z['t_sz'][it]); Tt['ok'] = Tt['rx'] >= 0; Tt['rx'] = Tt['rx'] + t0; z = None
# ---- 1) fichero en formato maker_ms (solo filas con rx valido: las que usa el modo B)
f = lambda x: repr(float(x))
rows = []
for n_ in range(len(Q['k'])):
    if Q['ok'][n_]: rows.append((int(Q['rx'][n_]), 0, n_, f'q,{int(Q["ex"][n_])},{TOK[Q["k"][n_]]},{f(Q["v"][0][n_])},{f(Q["v"][1][n_])},{f(Q["v"][2][n_])},{f(Q["v"][3][n_])},{int(Q["rx"][n_])}'))
for n_ in range(len(Tt['k'])):
    if Tt['ok'][n_]: rows.append((int(Tt['rx'][n_]), 1, n_, f't,{int(Tt["ex"][n_])},{TOK[Tt["k"][n_]]},{f(Tt["pr"][n_])},{"BUY" if Tt["sd"][n_] > 0.5 else "SELL"},{f(Tt["sz"][n_])},{int(Tt["rx"][n_])}'))
rows.sort(key=lambda r: (r[0], r[1], r[2])); first_rx = rows[0][0]
kl = [f'k,{first_rx - 1000},{TOK[i]},{info[i]["coin"]},{info[i]["marco"]},{info[i]["mid"]},{info[i]["fin_s"]},{info[i]["lado"]}' for i in need]
lines = ['tipo,t_ms,id,c1,c2,c3,c4,c5'] + kl + [r[3] for r in rows]; fpath = OUT + f'maker_ms_{D_}_replay.csv.gz'
with open(fpath, 'wb') as fh:
    for a in range(0, len(lines), 50000): fh.write(gzip.compress(('\n'.join(lines[a:a + 50000]) + '\n').encode()))
print('fichero', fpath, 'lineas', len(lines), round(time.time() - T0, 1), 's', flush=True)
# ---- 2) runner --once (con verificacion de hashes)
ro = OUT + 'runner/'; shutil_ok = os.path.exists(ro)
if shutil_ok:
    import shutil; shutil.rmtree(ro)
cmd = [sys.executable, '-I', HERE + 'cxb60_dryrun_fase0.py', '--out', ro, '--once', '--files', fpath, '--solo-dia', D_, '--c-print-par', '0', '--placebo', '0']; _t = time.time(); r = subprocess.run(cmd, capture_output=True, text=True, timeout=3600); w0 = time.time() - _t
print('runner rc', r.returncode, (r.stderr or r.stdout)[-300:].replace('\n', ' | '), round(time.time() - T0, 1), 's', flush=True); assert r.returncode == 0
dec = [x for x in IO.lee_dec(ro + f'dec_{D_}.csv.gz')]; man = json.load(open(ro + 'run_manifest.json')); skipped = man['saltados']
# ---- 3) modo B en proceso con los mismos buffers (npz)
def mkbuf(k):
    b = C.TokBuf(); m = (Q['k'] == k) & Q['ok']; o = np.lexsort((np.flatnonzero(m), Q['rx'][m]))
    b.qrx = Q['rx'][m][o].astype(np.int64); b.qex = Q['ex'][m][o].astype(np.int64); b.qbid, b.qask, b.qszb, b.qsza = [Q['v'][j][m][o].astype(np.float64) for j in range(4)]
    m = (Tt['k'] == k) & Tt['ok']; o = np.lexsort((np.flatnonzero(m), Tt['rx'][m])); b.trx = Tt['rx'][m][o].astype(np.int64); b.tex = Tt['ex'][m][o].astype(np.int64); b.tp = Tt['pr'][m][o].astype(np.float64); b.tbuy = Tt['sd'][m][o].astype(np.float64); b.tsz = Tt['sz'][m][o].astype(np.float64); return b
BUF = {k: mkbuf(k) for k in need}; specs = C.default_specs((35, 60, 100, 150), 0); modeB = {}
for i in sel5:
    m = info[i]
    if m['tok'] in skipped: continue
    c = by5.get((m['mid'], 'NO' if m['lado'] == 'YES' else 'YES')); f15 = int(math.ceil(m['fin'] / 900.0) * 900); t15 = by15.get((coin, f15, m['lado']))
    if c is None or t15 is None: continue
    mc = dict(tok=info[c]['tok'], mid=info[c]['mid'], lado=info[c]['lado'], coin=coin, fin=info[c]['fin']); mk_ = dict(tok=m['tok'], mid=m['mid'], lado=m['lado'], coin=coin, fin=m['fin'])
    fill = C.make_live_fill(lambda t_, i=i, c=c: (BUF[i], BUF[c]), lambda t_, mk_=mk_, mc=mc: [mk_, mc], C.C_PRINT)
    mkt = C.Market(m['tok'], m['fin'], coin, m['lado'], m['mid'], info[c]['tok'], BUF[i], BUF[c], BUF[t15], specs)
    for rec in mkt.advance(10 ** 18, fill): modeB[(rec['tok'], str(rec['L']), rec['var'], str(rec['seg']))] = rec
# ---- 4) comparacion
sv = lambda v: '' if v is None else str(v)
seg = [x for x in dec if x['tipo'] == 'seg']; R = {(x['tok'], x['L'], x['var'], x['seg']): x for x in seg}; difs = []; campos = [('t_dec_rx', int), ('t_arr', int), ('t_end', int), ('canc', int), ('tf', int), ('motivo_fin', str)]
for k, b in modeB.items():
    x = R.get(k)
    if x is None: difs.append((k, 'falta en runner')); continue
    for nm, tp in campos:
        if sv(b[nm]) != sv(x[nm]): difs.append((k, nm, b[nm], x[nm]))
    if abs(round(b['q'], 6) - float(x['q'])) > 1e-9: difs.append((k, 'q', b['q'], x['q']))
    if sv(b['t_trig_rx']) != x['t_trig_rx']: difs.append((k, 't_trig_rx', b['t_trig_rx'], x['t_trig_rx']))
extra = [k for k in R if k not in modeB]; res = dict(dia=D_, coin=coin, horas=[h0, h1], tokens_5m_seleccionados=len(sel5), saltados_por_el_runner=skipped, segmentos_runner=len(R), segmentos_modoB=len(modeB), rellenos_runner=sum(1 for x in seg if float(x['q']) > 0), cancelaciones_runner=sum(int(x['canc']) for x in seg),
                                                          diferencias=len(difs) + len(extra), faltan_en_runner_o_campos=len(difs), extra_en_runner=len(extra), ejemplos=[str(d) for d in difs[:8]] + [str(e) for e in extra[:4]], segundos=round(time.time() - T0, 1), hash_check_runner=man.get('hash_check', {}).get('ok'))
json.dump(res, open(OUT + 'resultado.json', 'w'), indent=1, default=str); print(json.dumps(res, indent=1, default=str))

# ---- 5) coste de la configuracion de PRODUCCION (placebo 100 + escenario c59) sobre los mismos datos reales: tiempo de pared, bytes del dec_, cpu_advance_us
def corre(tag, extra):
    o = OUT + tag + '/'
    if os.path.exists(o):
        import shutil; shutil.rmtree(o)
    t = time.time(); rr = subprocess.run([sys.executable, '-I', HERE + 'cxb60_dryrun_fase0.py', '--out', o, '--once', '--files', fpath, '--solo-dia', D_] + extra, capture_output=True, text=True, timeout=7200); w = time.time() - t
    hb = json.load(open(o + 'heartbeat.json')) if os.path.exists(o + 'heartbeat.json') else {}
    return dict(rc=rr.returncode, segundos=round(w, 1), bytes_dec=sum(os.path.getsize(f) for f in __import__('glob').glob(o + '**/dec_*.csv.gz', recursive=True)), rss_pico_mb=hb.get('rss_pico_mb'), cpu_advance_us=hb.get('cpu_advance_us'), cerrados=hb.get('cerrados'))
coste = {'placebo0_sin_c59': dict(segundos=round(w0, 1)), 'placebo20_sin_c59': corre('c_pl20', ['--c-print-par', '0', '--placebo', '20']), 'placebo100_con_c59_PRODUCCION': corre('c_prod', [])}
res['coste_placebo_y_c59'] = coste; json.dump(res, open(OUT + 'resultado.json', 'w'), indent=1, default=str); print(json.dumps(coste, indent=1))
