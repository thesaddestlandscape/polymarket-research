#!/usr/bin/env python3
"""e1q_sim.py ELEGIR|MEDIR [max_mercados] -- PREREG_P2_PALANCAS (sha d3dae831...). Simulador de puja tipo B CON COLA sobre libro L2 libro5.
Politica importada de seleccion_adversa_plan/scripts/e1_sim.py (obj_raw, STEP, T_HI, T_LO, SETTLE). Salida datos/e1q_<FASE>.csv.gz:
una fila por (mercado, variante). Solo lectura de produccion."""
import sys, os, json, gzip, hashlib, bisect, glob, math, collections
import numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_P2_PALANCAS.md'), 'rb').read()).hexdigest().startswith('d3dae8316ceb8be5')
sys.path.insert(0, os.path.join(AQ, '../../salida/scripts')); sys.path.insert(0, os.path.join(AQ, '../../seleccion_adversa_plan/scripts'))
import e1_sim as E
STEP, T_HI, T_LO, SETTLE = E.STEP, E.T_HI, E.T_LO, E.SETTLE
LAT_POST, LAT_CAN, REPOST = 85, 65, 150
WB, WA = 300, 150
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
DES.update(json.load(open(os.path.join(AQ, '../../salida/datos/desenlaces_extra.json'))))
FASE = os.environ.get('E1Q_FASE') or sys.argv[1]
SOLO = [v for v in os.environ.get('E1Q_SOLO', '').split(',') if v]; SUF = os.environ.get('E1Q_SUF', '')
SRC = {'ELEGIR': '/mnt/HC_Volume_106538179/datalogs_analisis_caches/colas_20oct/', 'MEDIR': '/root/polymarket-research-datalogs/cola_vs_cruce/'}[FASE]
DIAS = {'ELEGIR': ('2026-10-17', '2026-10-18', '2026-10-19'), 'MEDIR': ('2026-10-20', '2026-10-21', '2026-10-22')}[FASE]
FIN_MIN = {'ELEGIR': 0, 'MEDIR': 1792491000 + 300}[FASE]          # MEDIR: 20-Oct desde ~10:10Z (cache ELEGIR acaba ahi)
FIN_MAX = {'ELEGIR': 1792491000, 'MEDIR': 1792680000}[FASE]       # MEDIR: 22-Oct hasta 14:40Z (fin del npz y del token map)
VARS = {'BASE': dict(), 'S250': dict(settle=250), 'K0': dict(dk=-99), 'KMAS': dict(dk=1), 'NOTOP': dict(notop=True),
        'COLA50': dict(cola_min=50), 'COLA0': dict(cola_max=50), 'K10': dict(size=10),
        # DESVIACION D2 (declarada tras ELEGIR, fuera de la familia: DESCRIPTIVA). El codigo real de B (experimento_maker_h47.decidir)
        # NO espera a que el top este quieto 1,5 s: recalcula top-k cada ~0,1 s y cancela en cuanto cambia; el 1,5 s es el ASENTADO
        # tras cancelar (no repone hasta 1,5 s despues). BREAL reproduce eso; BREAL_R250 = reponer a 250 ms (palanca de latencia).
        'BREAL': dict(settle=0, repost=1500), 'BREAL_R250': dict(settle=0, repost=250),
        # DESVIACION D3 (declarada; exploratoria): B_FIEL = BREAL con la reaccion MEDIDA de B real (repega 0,21 s mediana tras el cambio
        # del top, p2_verif_repega.py) + cancelacion 65 ms -> cancelacion efectiva 280 ms tras el tick de decision. Palancas sobre B_FIEL:
        'B_FIEL': dict(settle=0, repost=1500, lat_can=280), 'BF_RAPIDO': dict(settle=0, repost=1500, lat_can=65),
        'BF_R250': dict(settle=0, repost=250, lat_can=280), 'BF_K0': dict(settle=0, repost=1500, lat_can=280, dk=-99),
        'BF_KMAS': dict(settle=0, repost=1500, lat_can=280, dk=1), 'BF_NOTOP': dict(settle=0, repost=1500, lat_can=280, notop=True),
        'BF_COLA50': dict(settle=0, repost=1500, lat_can=280, cola_min=50), 'BF_K10': dict(settle=0, repost=1500, lat_can=280, size=10)}
def mills(p): return int(round(float(p) * 1000))
def pbook(s):
    d = {}
    if isinstance(s, str) and s:
        for x in s.split(';'):
            if ':' in x:
                p, z = x.split(':'); z = float(z)
                if z > 0: d[mills(p)] = z
    return d
GALL = []
gf = SRC + 'g_all.txt'
if os.path.exists(gf):
    for l in open(gf):
        try: r, m = l.strip().split(',', 1); GALL.append(int(r))
        except Exception: pass
GALL.sort()
OPP = {'Y': 'N', 'N': 'Y'}

def load(path):
    ev = []
    with gzip.open(path, 'rt', errors='replace') as f:
        try:
            for ln in f:
                c = ln.rstrip('\n').split(',')
                if len(c) < 4: continue
                L, t = c[0], c[1]
                try:
                    if t == 'd':
                        if len(c) == 6:
                            if c[3] != 'B': continue
                            ev.append((int(c[2]), 1, L, mills(c[4]), float(c[5])))
                        else: ev.append((int(c[2]), 1, L, mills(c[3]), float(c[4])))
                    elif t == 'T': ev.append((int(c[2]), 2, L, c[3], mills(c[4]), float(c[5])))
                    elif t == 'B': ev.append((int(c[2]), 0, L, pbook(c[3])))
                    elif t == 'G': ev.append((int(c[2]), 3, L))
                except (ValueError, IndexError): continue
        except (EOFError, OSError): pass
    return ev

def prepara(ev, fin):
    """replay del libro: series de top bid por lado, historia de tamano por nivel, trades normalizados, bajadas explicadas."""
    bids = {'Y': {}, 'N': {}}; valid = {'Y': False, 'N': False}
    topT = {'Y': [], 'N': []}; topV = {'Y': [], 'N': []}
    lvl = collections.defaultdict(list)      # (L,q) -> [r, size_nuevo, delta, explicado]
    NT = {'Y': [], 'N': []}                  # (r, q, acc) normalizados al lado cuyo bid se golpea
    roto = False; w0, w1 = (fin - 300) * 1000, (fin - 60) * 1000
    def push_top(L, r):
        b = max(bids[L]) if (valid[L] and bids[L]) else -1
        if not topV[L] or topV[L][-1] != b: topT[L].append(r); topV[L].append(b)
    for e in ev:
        r, ty, L = e[0], e[1], e[2]
        if ty == 3:
            valid[L] = False; push_top(L, r)
            if w0 - 5000 <= r <= w1: roto = True
            continue
        if ty == 0:
            nb = e[3]
            if valid[L]:
                for q in set(bids[L]) | set(nb):
                    dl = nb.get(q, 0.0) - bids[L].get(q, 0.0)
                    if abs(dl) > 1e-6: lvl[(L, q)].append([r, nb.get(q, 0.0), dl, 0.0])
            else:
                for q, s in nb.items(): lvl[(L, q)].append([r, s, 0.0, 0.0])
            bids[L] = dict(nb); valid[L] = True; push_top(L, r); continue
        if ty == 1:
            q, sz = e[3], e[4]
            if not valid[L]: continue
            old = bids[L].get(q, 0.0)
            if sz > 0: bids[L][q] = sz
            else: bids[L].pop(q, None)
            if abs(sz - old) > 1e-9: lvl[(L, q)].append([r, sz, sz - old, 0.0])
            push_top(L, r); continue
        if ty == 2:
            side, q, acc = e[3], e[4], e[5]
            if side == 'SELL': NT[L].append((r, q, acc))
            elif side == 'BUY': NT[OPP[L]].append((r, 1000 - q, acc))
    for L in 'YN': NT[L].sort()
    # emparejado trade -> bajadas del mismo nivel en [r-WB, r+WA]
    for L in 'YN':
        porq = collections.defaultdict(list)
        for (r, q, acc) in NT[L]: porq[q].append((r, acc))
        for q, trs in porq.items():
            lst = [x for x in lvl.get((L, q), ()) if x[2] < 0]
            if not lst: continue
            times = [x[0] for x in lst]
            for (rt, acc) in trs:
                rem = acc; i = bisect.bisect_left(times, rt - WB); j = bisect.bisect_right(times, rt + WA)
                for k in sorted(range(i, j), key=lambda k: abs(lst[k][0] - rt)):
                    if rem <= 1e-9: break
                    u = min(rem, -lst[k][2] - lst[k][3])
                    if u > 1e-9: lst[k][3] += u; rem -= u
    TT = {L: np.array(topT[L], np.int64) for L in 'YN'}; TV = {L: np.array(topV[L], np.int64) for L in 'YN'}
    return TT, TV, lvl, NT, roto

def top_at(TT, TV, L, t):
    j = np.searchsorted(TT[L], t, 'right') - 1
    return int(TV[L][j]) if j >= 0 else -1

def lastchange(TT, TV, L, t):
    j = np.searchsorted(TT[L], t, 'right') - 1
    return int(TT[L][j]) if j >= 0 else None

def nivel_en(lvl, L, q, t):
    h = lvl.get((L, q))
    if not h: return 0.0
    i = bisect.bisect_right([x[0] for x in h], t) - 1
    return h[i][1] if i >= 0 else 0.0

def objetivo(b, a, k):
    """b, a en milesimas. k>=1: obj_raw de e1_sim; k==0: AL top (< ask)."""
    if k <= 0:
        if 110 < b <= 300 and b < a and b % 10 == 0: return b
        return None
    bid = np.array([b / 1000.0]); ask = np.array([a / 1000.0]); o = E.obj_raw(bid, ask, k)[0]
    return mills(o) if np.isfinite(o) else None

def vida_orden(lvl, NT, L, o, t_live, t_end, size, alloc='prop'):
    """replay de una orden virtual en (L,o) viva en [t_live, t_end): (r_fill, acc, tipo) o None. tipo 'X' atraviesa, 'P' al precio."""
    ah = nivel_en(lvl, L, o, t_live); bh = 0.0; rest = size; fills = []
    evs = [(x[0], 0, x) for x in lvl.get((L, o), ()) if t_live < x[0] < t_end]
    i0 = bisect.bisect_right(NT[L], (t_live, 10**9, 0)); 
    for (r, q, acc) in NT[L][i0:]:
        if r >= t_end: break
        if q <= o: evs.append((r, 1, (q, acc)))
    evs.sort(key=lambda z: (z[0], z[1]))
    for (r, pri, x) in evs:
        if pri == 0:
            _, _, dl, ex = x
            if dl > 0: bh += dl
            else:
                u = max(0.0, -dl - ex)
                if u > 0:
                    tot = ah + bh
                    if tot <= 1e-9: continue
                    c = u * ah / tot if alloc == 'prop' else (min(u, ah) if alloc == 'hi' else max(0.0, u - bh))
                    c = min(c, ah); ah -= c; bh = max(0.0, bh - (u - c))
        else:
            q, acc = x
            # DESVIACION D1 (declarada, smoke test de 30 mercados sin EV): la orden virtual no esta en el libro; una operacion a q < o
            # habria golpeado ANTES nuestra puja (prioridad de precio). Consume lo que quede delante en o y luego a nosotros; la tomadora
            # sigue mas alla de nuestro nivel solo si su tamano excede (delante + nuestro resto) -> 'X'; si no, se para en nosotros -> 'P'.
            u = min(acc, ah); ah -= u; left = acc - u
            if left > 1e-9:
                if q < o and left > rest + 1e-9: return (r, rest, 'X')
                return (r, min(left, rest), 'P')
    return None

def politica(TT, TV, lvl, NT, fin, L, k, settle=SETTLE, dk=0, notop=False, cola_min=None, cola_max=None, size=5.0, alloc='prop', repost=REPOST, lat_can=LAT_CAN):
    kk = 0 if dk == -99 else k + dk
    g = (fin * 1000 - np.arange(T_HI * 1000, T_LO * 1000 - 1, -STEP)).astype(np.int64)
    cur = None; live = None; t_next = 0; npost = 0
    for t in g:
        b = top_at(TT, TV, L, t); bo = top_at(TT, TV, OPP[L], t); a = 1000 - bo if bo > 0 else 9999
        lc = lastchange(TT, TV, L, t)
        if b > 0 and lc is not None and t - lc >= settle:
            cur = objetivo(b, a, kk) if (110 < b <= 300 and b < a) else None
        if live is not None:
            o, tl = live
            quitar = (cur is None) or (cur != o) or (notop and b <= o)
            if quitar:
                res = vida_orden(lvl, NT, L, o, tl, t + lat_can, size, alloc)
                if res: return res + (o, npost)
                live = None; t_next = t + repost
            continue
        if cur is None or t < t_next: continue
        if notop and b <= cur: continue
        ah = nivel_en(lvl, L, cur, t + LAT_POST)
        if cola_min is not None and ah < cola_min: continue
        if cola_max is not None and ah >= cola_max: continue
        live = (cur, int(t + LAT_POST)); npost += 1
    if live is not None:
        res = vida_orden(lvl, NT, L, live[0], live[1], int(g[-1]) + lat_can, size, alloc)
        if res: return res + (live[0], npost)
    return (None, 0.0, None, None, npost)

def clase(NT, L, r, o, tipo):
    if tipo == 'X': return 'X1'
    i = bisect.bisect_right(NT[L], (r, 10**9, 0))
    for (rr, q, acc) in NT[L][i:]:
        if rr > r + 2000: break
        if q < o: return 'X2'
    return 'X3'

def main():
    TOK = json.load(open(SRC + 'tokens.json')); mk = {}
    for t, v in TOK.items():
        if v[0] in ('ETH', 'SOL', 'XRP'): mk[(v[0], str(v[1]))] = float(v[3])
    lim = int(sys.argv[2]) if len(sys.argv) > 2 else None
    rows = []; nmiss = collections.Counter(); n = 0
    out = os.path.join(D, f'e1q_{FASE}{SUF}.csv.gz')
    for (act, mid), fin in sorted(mk.items(), key=lambda x: x[1]):
        fin = int(fin)
        dia = pd.Timestamp(fin, unit='s').strftime('%Y-%m-%d')
        if dia not in DIAS or not (FIN_MIN <= fin <= FIN_MAX): continue
        path = SRC + f'mk/{act}_{mid}.gz'
        if not os.path.exists(path): nmiss['sin_fichero'] += 1; continue
        w = DES.get(mid)
        if w is None: nmiss['sin_desenlace'] += 1; continue
        gi = bisect.bisect_left(GALL, (fin - 305) * 1000)
        if gi < len(GALL) and GALL[gi] <= (fin - 60) * 1000: nmiss['hueco_global'] += 1; continue
        ev = load(path)
        if not ev: nmiss['vacio'] += 1; continue
        TT, TV, lvl, NT, roto = prepara(ev, fin)
        if roto: nmiss['hueco_token'] += 1; continue
        # lado: primer L cuyo top bid entra en banda en la rejilla (como E1)
        g = (fin * 1000 - np.arange(T_HI * 1000, T_LO * 1000 - 1, -STEP)).astype(np.int64)
        L = None
        for t in g:
            for LL in ('Y', 'N'):
                b = top_at(TT, TV, LL, t)
                if 110 < b <= 300: L = LL; break
            if L: break
        if L is None: continue
        k = 2 if act == 'ETH' else 1; gana = int((w == 'YES') == (L == 'Y'))
        for var, kw in VARS.items():
            if SOLO and var not in SOLO: continue
            for alloc in (('prop', 'lo', 'hi') if var == 'BASE' else ('prop',)):
                r, acc, tipo, o, npost = politica(TT, TV, lvl, NT, fin, L, k, alloc=alloc, **kw)
                cl = clase(NT, L, r, o, tipo) if r is not None else None
                rows.append(dict(dia=dia, act=act, mid=mid, fin=fin, lado=L, gana=gana, var=var, alloc=alloc, fill=int(r is not None),
                                 acc=acc, p=(o / 1000.0 if o else np.nan), r=r, T=(fin - r / 1000.0) if r else np.nan, clase=cl, npost=npost))
        n += 1
        if n % 100 == 0: print(FASE, n, 'mercados', dict(nmiss), flush=True)
        if lim and n >= lim: break
    pd.DataFrame(rows).to_csv(out, index=False); print(FASE, 'FIN mercados', n, 'excluidos', dict(nmiss), '->', out, flush=True)
if __name__ == '__main__':
    main()
