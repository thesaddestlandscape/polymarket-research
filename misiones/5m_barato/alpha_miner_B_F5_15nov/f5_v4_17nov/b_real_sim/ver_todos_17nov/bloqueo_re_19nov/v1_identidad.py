"""v1_identidad.py -- mide PREREG_V1_IDENTIDAD_19nov.md (sha da9f4a89...). Solo lectura, 0 ordenes, no EV.
Uso: python3 -I v1_identidad.py <libro5.gz> <onchain.gz> <tag>"""
import sys, gzip, json, pickle, collections, bisect
L5, OC, TAG = sys.argv[1], sys.argv[2], sys.argv[3]
EXCH = '0xe111180000d2663c0091e4f400237545b87b996b'
def pk(x): return int(round(float(x) * 1000))
with gzip.open(L5, 'rt', errors='replace') as f:
    f.readline(); rx0 = int(f.readline().split(',')[6])
W0, W1 = rx0 / 1000 - 60, rx0 / 1000 + 4 * 3600
# ---------- on-chain ----------
tk = {}; mk = collections.defaultdict(list); ntk_all = 0
with gzip.open(OC, 'rt', errors='replace') as f:
    f.readline()
    for ln in f:
        c = ln.rstrip('\n').split(',')
        if len(c) < 13 or c[0] != 'F': continue
        try: ts = float(c[2]); b = int(c[1]); ma = float(c[10]); ta = float(c[11])
        except ValueError: continue
        if ts < W0 or ts > W1 + 3600 or ma <= 0 or ta <= 0: continue
        h = c[5]; side = c[8]
        if c[7] == EXCH:
            if ts <= W1 and h not in tk:
                sh = ta if side == '0' else ma
                tk[h] = dict(b=b, ts=ts, tok=c[9], side=side, sh=sh, w=c[6], tx=c[3])
        elif h in tk and b > tk[h]['b']:
            p = ma / ta if side == '0' else ta / ma; sh = ta if side == '0' else ma
            mk[h].append((b, ts, pk(p), sh))
rest = {h: v for h, v in tk.items() if h in mk}
for h, v in rest.items():
    v['plim'] = mk[h][0][2]; v['Rlb'] = sum(x[3] for x in mk[h]); v['dt_mk'] = mk[h][0][1] - v['ts']
print('onchain: tomadoras en ventana', len(tk), '| REST+', len(rest), flush=True)
# ---------- libro5 ----------
book = {}; valid = set(); comp_votes = collections.Counter(); toks = set()
tl = []          # lotes con T: (rx, [T...], [inc...])
near = collections.deque()  # lotes recientes (rx, incs) para V1c
pend_c = []      # indices tl esperando lotes futuros (<= rx+2)
pseudo = collections.deque(); plac = {}
tgt_keys = set()
for v in rest.values():
    tgt_keys.add((v['tok'], 'B' if v['side'] == '0' else 'A', v['plim']))
tgt_log = collections.defaultdict(list)
def flush(rx, T, inc, dpairs):
    for i in range(len(dpairs)):
        for j in range(i + 1, len(dpairs)):
            a, b_ = dpairs[i], dpairs[j]
            if a[1] == b_[1] and a[2] != b_[2] and a[3] + b_[3] == 1000 and a[0] != b_[0] and a[4] == b_[4]:
                comp_votes[(a[0], b_[0])] += 1; comp_votes[(b_[0], a[0])] += 1
    while pseudo and pseudo[0][0] <= rx:
        _, idx = pseudo.popleft(); plac[idx] = (rx, inc)
    for idx in list(pend_c):
        if rx - tl[idx][0] <= 2: tl[idx][3].extend(inc)
        else: pend_c.remove(idx)
    while near and rx - near[0][0] > 2: near.popleft()
    if T:
        ext = [x for r_, ii in near for x in ii]
        tl.append([rx, T, inc, ext]); pend_c.append(len(tl) - 1); pseudo.append((rx + 10000, len(tl) - 1))
    near.append((rx, inc))
cur = None; T = []; inc = []; dp = []; nrow = 0; rxl = rx0
with gzip.open(L5, 'rt', errors='replace') as f:
    f.readline()
    for ln in f:
        c = ln.rstrip('\n').split(',')
        if len(c) < 8: continue
        try: rx = int(c[6]); t = int(c[1])
        except ValueError: continue
        nrow += 1
        if rx != cur:
            if cur is not None: flush(cur, T, inc, dp)
            cur = rx; T = []; inc = []; dp = []
        rxl = rx; k = c[0]; tok = c[2]
        if k == 'G':
            if tok == '*': valid.clear()
            else: valid.discard(tok)
            continue
        if k == 'T':
            T.append((tok, c[4], pk(c[3]), float(c[5]), t)); toks.add(tok); continue
        if k == 'B':
            new = {}
            for sd, s in (('B', c[3]), ('A', c[4])):
                dct = {}
                for it in s.split(';'):
                    if ':' in it:
                        p_, q_ = it.split(':'); dct[pk(p_)] = float(q_)
                new[sd] = dct
            old = book.get(tok) if tok in valid else None
            if old is not None:
                for sd in ('B', 'A'):
                    for p_ in set(old[sd]) | set(new[sd]):
                        dl = new[sd].get(p_, 0.0) - old[sd].get(p_, 0.0)
                        if abs(dl) > 1e-9:
                            if dl > 0: inc.append((tok, sd, p_, dl, t, 'B'))
                            if (tok, sd, p_) in tgt_keys: tgt_log[(tok, sd, p_)].append((rx, t, dl, new[sd].get(p_, 0.0), 'B'))
            book[tok] = new; valid.add(tok); toks.add(tok); continue
        if k == 'd':
            if tok not in valid: continue
            sd = c[3]; p_ = pk(c[4]); q_ = float(c[5]); dl = q_ - book[tok][sd].get(p_, 0.0)
            if q_ > 0: book[tok][sd][p_] = q_
            else: book[tok][sd].pop(p_, None)
            dp.append((tok, sd, p_, p_ if sd == 'B' else 1000 - p_, t))
            if dl > 1e-9: inc.append((tok, sd, p_, dl, t, 'd'))
            if (tok, sd, p_) in tgt_keys and abs(dl) > 1e-9: tgt_log[(tok, sd, p_)].append((rx, t, dl, q_, 'd'))
    flush(cur, T, inc, dp)
# comp map: mejor voto
comp = {}
for (a, b_), n in comp_votes.most_common():
    if a not in comp and n >= 3: comp[a] = b_
print('libro5 filas', nrow, '| rx0', rx0, 'rxl', rxl, '| tokens', len(toks), '| comp', len(comp), '| lotes con T', len(tl), flush=True)
pickle.dump(dict(rest=rest, ntk=len(tk), tk_toks=collections.Counter(v['tok'] in toks for v in tk.values()), tl=tl, plac=plac,
                 comp=comp, tgt_log=dict(tgt_log), rx0=rx0, rxl=rxl, toks=toks), open(f'out/v1_{TAG}.pkl', 'wb'))
print('OK', flush=True)
