#!/usr/bin/env python3
"""anclas_relojes.py -- ANCLAS PROPIAS (ordenes REALES ya enviadas en el pasado; este script solo LEE: 0 ordenes, 0 red) para medir orden -> aparece en el feed en AMBOS relojes.
  sonda  DIA : Sonda1 (datalogs/sonda1/cancel_evid/cancel_evid_<DIA>.jsonl[.gz]): alta{t_envio_ms,t_ack_ms} + user_order{ts_ex_ms (EXCHANGE), t_recv_ms (recepcion del WS de usuario)} +
               cancel_try{t_pre_ms,t_resp_ms}; cruza con el feed PUBLICO libro5_b40 (filas d: t_ms = exchange, recepcion = col 6) buscando la fila d del nivel (token, precio) con delta = +/- tamano.
  breal  DIA : B real (datalogs/experimento_h47_B_ledger.jsonl, puja_post + post_lat{t_call0, t_ret} locales) cruzado con maker_ms filas q (top del libro: ex, bid, ask, szb, sza, rx)
               SOLO para pujas que mejoran o igualan el mejor bid (entonces el alta mueve el top: bid == precio y szb sube en el tamano).
Salida: out_v2/anclas_<fuente>_<DIA>.json (una linea por ancla + resumen p50/p90/n). Un dia cada vez, nice -n 19. Honesto: ancla ambigua (>1 candidato) -> se descarta y se cuenta."""
import sys, os, json, gzip, glob, subprocess, tempfile, collections
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = os.environ.get('ANCLAS_OUT', H + 'out_v2/'); os.makedirs(OUT, exist_ok=True)
DL = '/root/polymarket-research-datalogs/'; B40 = '/mnt/HC_Volume_106538179/libro5_b40/'


def pct(v):
    v = np.asarray([x for x in v if x is not None and np.isfinite(x)], float)
    if len(v) == 0: return dict(n=0)
    p = np.percentile(v, [5, 50, 90]); return dict(n=int(len(v)), p5=float(p[0]), p50=float(p[1]), p90=float(p[2]), min=float(v.min()), max=float(v.max()))


def zrows(path, tokfile, tipo):
    """Filas del tipo dado cuyo token aparece en tokfile (grep -F), en orden de fichero."""
    cmd = f"zcat '{path}' 2>/dev/null | grep -E '^{tipo}(,|$)' | grep -F -f '{tokfile}'"
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, text=True, bufsize=1 << 20)


# ------------------------------------------------------------------ SONDA1
def lee_sonda(dia):
    f = DL + f'sonda1/cancel_evid/cancel_evid_{dia}.jsonl'
    op = open if os.path.exists(f) else gzip.open
    if not os.path.exists(f): f += '.gz'
    ev = []
    for l in op(f, 'rt'):
        try: ev.append(json.loads(l))
        except Exception: pass
    return ev


def sonda(dia):
    ev = lee_sonda(dia)
    alta = {e['oid']: e for e in ev if e['k'] == 'alta'}
    uo = collections.defaultdict(dict)
    for e in ev:
        if e['k'] == 'user_order' and e.get('mine'): uo[e['oid']].setdefault(e['tipo'], e)
    cc = {e['oid']: e for e in ev if e['k'] == 'cancel_try' and e.get('canceled')}
    toks = sorted({e['asset_id'] for o in uo.values() for e in o.values()})
    R = dict(dia=dia, altas=len(alta), con_user_placement=sum(1 for o in alta if 'PLACEMENT' in uo.get(o, {})), cancelaciones=len(cc), filas=[])
    pub = {}
    if toks:
        tf = tempfile.NamedTemporaryFile('w', suffix='.tok', delete=False, dir=OUT); tf.write('\n'.join(toks) + '\n'); tf.close()
        bk = collections.defaultdict(dict); hist = collections.defaultdict(list)          # tok -> {precio_c: size}; tok -> [(ex, rx, side, precio, delta)]
        p = subprocess.Popen(f"zcat '{B40}libro5_b40_{dia}.csv.gz' 2>/dev/null | awk -F, -v tf={tf.name} 'BEGIN{{while((getline l<tf)>0)t[l]}} ($1==\"d\"||$1==\"B\"||$1==\"G\")&&($3 in t)'", shell=True, stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
        for line in p.stdout:
            q = line.rstrip('\n').split(',')
            tk = q[2]
            if q[0] == 'G': bk[tk].clear(); continue
            if q[0] == 'B':
                bk[tk].clear()
                if q[3]:
                    for kv in q[3].split(';'):
                        a, b = kv.split(':'); bk[tk][int(round(float(a) * 100))] = float(b)
                continue
            if q[3] != 'B': continue
            pc = int(round(float(q[4]) * 100)); sz = float(q[5]); old = bk[tk].get(pc, 0.0)
            if sz > 0: bk[tk][pc] = sz
            else: bk[tk].pop(pc, None)
            hist[tk].append((int(q[1]), int(q[6]), pc, sz - old))
        p.wait(); os.unlink(tf.name); pub = hist
    for oid, a in alta.items():
        o = uo.get(oid, {}); pl = o.get('PLACEMENT'); r = dict(oid=oid[:12], precio=a['precio'], t_envio=a['t_envio_ms'], t_ack=a['t_ack_ms'], rtt_post=a['t_ack_ms'] - a['t_envio_ms'])
        if pl:
            r.update(ex_menos_envio=pl['ts_ex_ms'] - a['t_envio_ms'], ack_menos_ex=a['t_ack_ms'] - pl['ts_ex_ms'], user_ws_rx_menos_ex=pl['t_recv_ms'] - pl['ts_ex_ms'])
            tk = pl['asset_id']; pc = int(round(a['precio'] * 100)); sz = float(pl.get('original_size', 5.0))
            cand = [h for h in pub.get(tk, []) if h[2] == pc and abs(h[3] - sz) < 1e-6 and a['t_envio_ms'] - 300 <= h[1] <= a['t_envio_ms'] + 3000]
            r['n_cand_publico'] = len(cand)
            if len(cand) == 1:
                ex, rx = cand[0][0], cand[0][1]
                r.update(pub_ex_menos_envio=ex - a['t_envio_ms'], pub_rx_menos_envio=rx - a['t_envio_ms'], pub_rx_menos_ex=rx - ex, pub_ex_menos_user_ex=ex - pl['ts_ex_ms'], pub_rx_menos_user_rx=rx - pl['t_recv_ms'])
        c = cc.get(oid); cn = o.get('CANCELLATION')
        if c and cn:
            r.update(canc_rtt=c['t_resp_ms'] - c['t_pre_ms'], canc_ex_menos_pre=cn['ts_ex_ms'] - c['t_pre_ms'], canc_user_rx_menos_ex=cn['t_recv_ms'] - cn['ts_ex_ms'])
        R['filas'].append(r)
    keys = ['rtt_post', 'ex_menos_envio', 'ack_menos_ex', 'user_ws_rx_menos_ex', 'pub_ex_menos_envio', 'pub_rx_menos_envio', 'pub_rx_menos_ex', 'pub_ex_menos_user_ex', 'pub_rx_menos_user_rx', 'canc_rtt', 'canc_ex_menos_pre', 'canc_user_rx_menos_ex']
    R['resumen'] = {k: pct([x.get(k) for x in R['filas']]) for k in keys}
    json.dump(R, open(OUT + f'anclas_sonda_{dia}.json', 'w'), indent=1)
    print('sonda', dia, json.dumps(R['resumen']), flush=True)
    return R


# ------------------------------------------------------------------ B real
def breal(dia):
    led = DL + 'experimento_h47_B_ledger.jsonl'; pj = {}; pl = {}
    for l in open(led):
        try: j = json.loads(l)
        except Exception: continue
        if not j.get('ts', '').startswith(dia): continue
        if j['tipo'] == 'puja_post': pj[j['oid']] = j
        elif j['tipo'] == 'post_lat': pl[j['oid']] = j
    an = []
    for oid, p in pj.items():
        if oid not in pl or not p.get('libro') or not p['libro'].get('bids'): continue
        if p['precio'] + 1e-9 < max(b[0] for b in p['libro']['bids']): continue                  # no visible en el top
        an.append((oid, p['precio'], p['size'], pl[oid]['t_call0'] * 1000, pl[oid]['t_ret'] * 1000, p.get('coin'), p['libro']))
    R = dict(dia=dia, pujas=len(pj), candidatas_top=len(an), filas=[])
    if not an: json.dump(R, open(OUT + f'anclas_breal_{dia}.json', 'w')); return R
    tokmap = {}
    for l in open(led):
        try: j = json.loads(l)
        except Exception: continue
        if j['tipo'] == 'intencion_post' and j['oid'] in pj: tokmap[j['oid']] = j['tok']
    tk_set = sorted({tokmap[a[0]] for a in an if a[0] in tokmap})
    tf = tempfile.NamedTemporaryFile('w', suffix='.tok', delete=False, dir=OUT); tf.write('\n'.join(tk_set) + '\n'); tf.close()
    rows = collections.defaultdict(list)
    for f in sorted(glob.glob(DL + f'maker_ms_{dia}_*.csv.gz')):
        p = zrows(f, tf.name, 'q')
        for line in p.stdout:
            q = line.rstrip('\n').split(',')
            if len(q) < 8: continue
            try: rows[q[2]].append((int(q[1]), int(q[7]) if q[7] else -1, float(q[3]) if q[3] != 'None' else np.nan, float(q[5]) if q[5] != 'None' else np.nan))
            except ValueError: continue
        p.wait()
    os.unlink(tf.name)
    for oid, pr, sz, t0, t1, coin, lib in an:
        tk = tokmap.get(oid); rs = rows.get(tk, []); cand = []
        for i in range(1, len(rs)):
            ex, rx, bid, szb = rs[i]; pex, prx, pbid, pszb = rs[i - 1]
            if rx < 0 or not (t0 - 200 <= rx <= t1 + 2000): continue
            if abs(bid - pr) < 1e-9 and ((abs(pbid - pr) < 1e-9 and abs((szb - pszb) - sz) < 1e-6) or (pbid < pr - 1e-9 and abs(szb - sz) < 1e-6)): cand.append((ex, rx))
        r = dict(oid=oid[:12], precio=pr, t_call0=t0, t_ret=t1, rtt_post_local=t1 - t0, n_cand=len(cand))
        if len(cand) == 1:
            ex, rx = cand[0]; r.update(ex_menos_call0=ex - t0, rx_menos_call0=rx - t0, rx_menos_ex=rx - ex, ex_menos_ret=ex - t1, rx_menos_ret=rx - t1)
        R['filas'].append(r)
    ctrl = []                                                                                  # control: rx-ex de TODAS las filas q de esos tokens a +-30 s de cada ancla (misma epoca/carga)
    for oid, pr, sz, t0, t1, coin, lib in an:
        for ex, rx, bid, szb in rows.get(tokmap.get(oid), []):
            if rx > 0 and t0 - 30000 <= rx <= t1 + 30000: ctrl.append(rx - ex)
    R['control_lag_q_misma_ventana'] = pct(ctrl)
    R['ambiguas_o_sin_candidato'] = sum(1 for r in R['filas'] if r['n_cand'] != 1)
    keys = ['rtt_post_local', 'ex_menos_call0', 'rx_menos_call0', 'rx_menos_ex', 'ex_menos_ret', 'rx_menos_ret']
    R['resumen'] = {k: pct([x.get(k) for x in R['filas']]) for k in keys}
    json.dump(R, open(OUT + f'anclas_breal_{dia}.json', 'w'), indent=1)
    print('breal', dia, 'candidatas', len(an), json.dumps(R['resumen']), flush=True)
    return R


if __name__ == '__main__':
    fuente = sys.argv[1]
    for d in sys.argv[2:]: {'sonda': sonda, 'breal': breal}[fuente](d)
