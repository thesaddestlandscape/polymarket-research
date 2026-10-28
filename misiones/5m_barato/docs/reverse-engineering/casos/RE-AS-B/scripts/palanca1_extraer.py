#!/usr/bin/env python3
"""palanca1_extraer.py --dia D [--src F] [--des F] [--out F] [--max-lineas N]   (RE-AS-B Palanca 1; SOLO LECTURA; python3 -I)
Variante del logger vida_puja_virtual_5m.py (copia la colocacion de pujas virtuales y la deteccion de barrido bb<b; NO toca el original).
Evento REAL = primer barrido (bb<b) de una puja virtual del token tk en el dia (unidad mercado-lado). t_sw = RECEPCION de la fila q que lo muestra.
Sonda = a t_sw+L (L=100,250,500 ms) estado del libro del token COMPLEMENTARIO (ultimo q valido en ORDEN DE FICHERO con recepcion <= objetivo;
se resuelve con la primera fila del mismo mercado (tk o comp) con recepcion > objetivo). Taker: ask nivel 1 (ejecutable si as_>=5). Maker: puja virtual
5 acc en el mejor bid del comp en t_sw+L (cola al final), mismas reglas A/B/C que el logger.
PLACEBO = NPLC instantes aleatorios (hash determinista) por token en [cierre-300 s, cierre-15 s], mismas sondas.
Salida: CSV gz de sondas (una fila por sonda y L). Escritura atomica .tmp->replace; determinista."""
import sys, gzip, json, os, argparse, collections, time, hashlib, random
ap = argparse.ArgumentParser(); ap.add_argument('--dia', required=True); ap.add_argument('--src'); ap.add_argument('--des'); ap.add_argument('--out')
ap.add_argument('--max-lineas', type=int, default=0); ap.add_argument('--nplc', type=int, default=10); a = ap.parse_args()
SRC = a.src or '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz' % a.dia
DESF = a.des or '/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'
OUT = a.out or '/root/polymarket-research-datalogs/palanca1/p1_%s.csv.gz' % a.dia
os.makedirs(os.path.dirname(OUT), exist_ok=True)
DES = json.load(open(DESF))
PASO, VIDA, ACC, LO, HI = 10_000, 60_000, 5.0, 0.10 - 1e-9, 0.30 + 1e-9
LS = (100, 250, 500)
K = {}; COMP = {}; MKTOK = collections.defaultdict(list)       # token -> (coin,mk,cie,lado); (mk,lado)->tok; mk->[tokens]
ultimo_t = {}; ult_coloc = {}; vidas = collections.defaultdict(list)
last_q = {}                      # token -> (recv, bb, ba, bs, as_) ultimo q valido
mclock = {}                      # mk -> mayor recepcion vista (q/t) del mercado
pend = collections.defaultdict(list)   # mk -> lista de sondas pendientes (orden de objetivo)
mvidas = collections.defaultdict(list) # token comp -> vidas maker activas
ev_done = set(); plc_done = set()
cnt = collections.Counter()
hdr = ['dia','kind','draw','mk','coin','lado_ev','lado_buy','cierre','L','t_ev_ms','T_ev_s','b_sw','ask_prev','bid_prev','ask_L','as_L','bid_L','bs_L','age_ms',
       'gana_buy','mk_pes','mk_opt','mk_t_pes','b_m','Q0_m','mk_fin']
fo = gzip.open(OUT + '.tmp', 'wt'); fo.write(','.join(hdr) + '\n')
def gana_buy(mk, lado):
    g = DES.get(str(mk)); return '' if g is None else int(g == lado)
def marca_m(v, now):
    q = v['Q0'] + ACC
    if v['tp'] is None and v['A'] + v['B'] >= q: v['tp'] = now
    if v['to'] is None and (max(v['A'] + v['B'], v['C']) >= q or (v['sw'] and v['A'] + v['B'] > 0)): v['to'] = now
def cerrar_m(v, motivo):
    p = v['p']
    fo.write(','.join(map(str, [a.dia, p['kind'], p['draw'], p['mk'], p['coin'], p['lado_ev'], p['lado_buy'], p['cie'], p['L'], p['t_ev'], '%.1f' % ((p['cie'] - p['t_ev']) / 1000),
             p['b_sw'], p['ask_prev'], p['bid_prev'], p['ask'], p['as'], p['bid'], p['bs'], p['age'], gana_buy(p['mk'], p['lado_buy']),
             int(v['tp'] is not None), int(v['to'] is not None), v['tp'] or '', v['b'], v['Q0'], motivo])) + '\n'); cnt['filas'] += 1
def resolver(p, now_row):
    """estado del comp en p['tgt'] = ultimo q en orden de fichero (recv<=tgt, garantizado por la regla de disparo)."""
    st = last_q.get(p['tkb']); cnt['sondas'] += 1
    if st is None or st[0] > p['tgt']:
        cnt['sin_estado'] += 1; return
    p.update(ask=st[2], as_=st[4], bid=st[1], bs=st[3], age=p['tgt'] - st[0]); p['as'] = st[4]
    v = {'p': p, 'b': st[1], 'Q0': st[3], 'last': st[3], 'A': 0.0, 'B': 0.0, 'C': 0.0, 'sw': False, 'tp': None, 'to': None, 't0': p['tgt'], 'end': min(p['tgt'] + VIDA, p['cie'] - 2000)}
    mvidas[p['tkb']].append(v)
def disparar(mk, now):
    pl = pend.get(mk)
    if not pl: return
    keep = []
    for p in pl:
        if now > p['tgt']: resolver(p, now)
        else: keep.append(p)
    pend[mk] = keep
def avanzar_m(tk, now):
    ks = []
    for v in mvidas.get(tk, []):
        if v['tp'] is not None and v['to'] is not None: cerrar_m(v, 'relleno'); continue
        if now > v['end']: cerrar_m(v, 'vida' if v['tp'] is None else 'relleno_pes'); continue
        ks.append(v)
    mvidas[tk] = ks
def crear_sondas(kind, draw, tk, t_ev, b_sw):
    coin, mk, cie, lado = K[tk]; lb = 'NO' if lado == 'YES' else 'YES'; tkb = COMP.get((mk, lb))
    if not tkb: cnt['sin_comp'] += 1; return
    ps = last_q.get(tkb); ap_ = '' if ps is None else ps[2]; bp_ = '' if ps is None else ps[1]
    for L in LS:
        pend[mk].append({'kind': kind, 'draw': draw, 'mk': mk, 'coin': coin, 'lado_ev': lado, 'lado_buy': lb, 'cie': cie, 'L': L, 't_ev': t_ev, 'tgt': t_ev + L,
                         'tkb': tkb, 'tka': tk, 'b_sw': b_sw, 'ask_prev': ap_, 'bid_prev': bp_})
    pend[mk].sort(key=lambda p: p['tgt'])
t_ini = time.time(); n = 0
def draw_t(mk, lado, j, cie):
    h = hashlib.sha256(('%s|%s|%d' % (mk, lado, j)).encode()).digest(); u = int.from_bytes(h[:8], 'big') / 2**64
    return int(cie - 300_000 + u * (300_000 - 15_000))
with gzip.open(SRC, 'rt', errors='replace') as f:
    try:
        for line in f:
            n += 1
            if a.max_lineas and n > a.max_lineas: break
            c = line.rstrip('\n').split(',')
            ty = c[0]
            if ty == 'k':
                if len(c) >= 8 and c[4] == '5min':
                    try: cie = int(time.mktime(time.strptime(c[6][:19], '%Y-%m-%d %H:%M:%S')) - time.timezone) * 1000
                    except Exception: continue
                    K[c[2]] = (c[3], c[5], cie, c[7]); COMP[(c[5], c[7])] = c[2]
                continue
            if ty not in ('q', 't') or len(c) < 7 or c[2] not in K: continue
            tk = c[2]
            try: now = int(c[7]) if ty == 'q' else int(c[6])
            except (ValueError, IndexError): continue
            coin, mk, cie, lado = K[tk]
            if tk not in plc_done and (mk, 'NO' if lado == 'YES' else 'YES') in COMP:      # placebos al ver la primera fila del token (ya registrados ambos k)
                plc_done.add(tk)
                for j in range(a.nplc): crear_sondas('placebo', j, tk, draw_t(mk, lado, j, cie), '')
            if tk in ultimo_t and now < ultimo_t[tk] - 60_000:
                vidas[tk] = []; ult_coloc.pop(tk, None); last_q.pop(tk, None); cnt['reinicios'] += 1
            elif tk in ultimo_t and now < ultimo_t[tk]: cnt['retroceso_menor'] += 1
            ultimo_t[tk] = now
            # disparo por reloj de mercado (antes de procesar la fila): sondas con objetivo < now usan el estado previo
            disparar(mk, now) if now >= mclock.get(mk, 0) else None
            mclock[mk] = max(mclock.get(mk, 0), now)
            if ty == 't':
                try: p_ = float(c[3]); sz = float(c[5])
                except ValueError: continue
                if c[4] == 'SELL':
                    for v in mvidas.get(tk, []):
                        if p_ <= v['b'] + 1e-9 and now >= v['t0']: v['A'] += sz; marca_m(v, now)
                else:
                    otro = COMP.get((mk, 'NO' if lado == 'YES' else 'YES'))
                    if otro:
                        for v in mvidas.get(otro, []):
                            if p_ >= 1 - v['b'] - 1e-9 and now >= v['t0']: v['B'] += sz; marca_m(v, now)
                continue
            try: bb, ba, bs, as_ = float(c[3]), float(c[4]), float(c[5]), float(c[6])
            except ValueError: continue
            if bb >= ba: cnt['cruzado'] += 1; continue
            # maker virtual sobre este token (comp de alguna sonda)
            for v in mvidas.get(tk, []):
                if abs(bb - v['b']) < 1e-9:
                    if bs < v['last']: v['C'] += v['last'] - bs
                    v['last'] = bs
                elif bb < v['b'] - 1e-9: v['sw'] = True
                marca_m(v, now)
            avanzar_m(tk, now)
            # pujas virtuales del token (deteccion de barrido): copia del logger
            keep = []
            for v in vidas[tk]:
                if now > v['t0'] + VIDA or now > cie - 2000: continue
                if bb < v['b'] - 1e-9 and tk not in ev_done:
                    ev_done.add(tk); crear_sondas('real', 0, tk, now, v['b']); cnt['eventos'] += 1
                    v['sw'] = True
                keep.append(v)
            vidas[tk] = keep
            last_q[tk] = (now, bb, ba, bs, as_)
            T = (cie - now) / 1000.0
            if LO <= bb <= HI and 60 <= T <= 300 and now - ult_coloc.get(tk, -10**15) >= PASO:
                vidas[tk].append({'b': round(bb, 2), 't0': now, 'sw': False}); ult_coloc[tk] = now
    except EOFError:
        print('AVISO: gz truncado tras %d lineas' % n)
# flush: sondas pendientes y maker vivas con el ultimo estado conocido
for mk, pl in list(pend.items()):
    for p in pl:
        if mclock.get(mk, 0) > p['tgt']: resolver(p, 0); cnt['resuelta_en_flush'] += 1
        else: cnt['no_alcanzada'] += 1
for tk, vs in list(mvidas.items()):
    for v in vs: cerrar_m(v, 'fin_fichero')
fo.close(); os.replace(OUT + '.tmp', OUT)
print('dia %s lineas %d %s seg %.0f -> %s' % (a.dia, n, dict(cnt), time.time() - t_ini, OUT))
