#!/usr/bin/env python3
"""f3_vpv.py (ADAPTACION de vida_puja_virtual_5m.py para F3 carry: bid del favorito en [0,90-0,99], --marco 5min|15min; sin features Binance). Original:
vida_puja_virtual_5m.py --dia D [--max-lineas N] [--out F]  -- LOGGER PASIVO (solo lectura, 24-Oct, detector_ex_ante sec. 5).
Etiqueta L2 de la POBLACION: pujas VIRTUALES (5 acc al mejor bid, al final de la cola) que estaban en el libro y se rellenaron o NO.
Fuente unica: /mnt/HC_Volume_106538179/m5_registro/m5_registro_D.csv.gz (extraido 04:00Z del libro_estado_ws; cero conexiones nuevas,
no toca observadores_fase0). Filas k (token->moneda,marco,mercado,cierre,lado), q (t_exch, token, bb, ba, bs, as, RECEPCION=c5),
t (t_exch, token, precio, lado tomador, tamano, RECEPCION=c5), x (Binance aggTrade, RECEPCION=c[7]).
Reloj = RECEPCION en ms. El registro NO es cronologico (tramos): estado por token/simbolo, reinicio si la hora retrocede >60 s.
Colocacion: cada 10 s por token 5min, si bb en [0,10;0,30] y T restante en [60;300] s: Q0 = bs (cola delante), b = bb.
Consumo de la cola: (A) prints SELL del propio token a precio <= b; (B) prints BUY del token complementario a precio >= 1-b
(el bid YES a b es el ask NO a 1-b en el libro espejo; puede duplicar A: se guardan por separado); (C) caidas de bs en el nivel b
(operaciones + cancelaciones). relleno_pes: A+B >= Q0+5 (las cancelaciones delante no nos adelantan); relleno_opt: max(A+B, C) >= Q0+5
o nivel barrido (bb < b) con A+B > 0. Vida: hasta relleno o t0+60 s o cierre-2 s. Desenlace: maker_ms_desenlaces_cache.json (missing = vacio).
Salida: /root/polymarket-research-datalogs/vida_puja_virtual/vpv_D.csv.gz (gz; retencion 30 d via --purgar; fuera de git)."""
import sys, gzip, json, os, argparse, collections, glob, time
ap = argparse.ArgumentParser(); ap.add_argument('--dia', required=True); ap.add_argument('--max-lineas', type=int, default=0)
ap.add_argument('--marco', default='5min'); ap.add_argument('--out', default=None); ap.add_argument('--purgar', type=int, default=30); a = ap.parse_args()
PFX = 'm5' if a.marco == '5min' else 'm15'; TMAX = 300 if a.marco == '5min' else 900
SRC = '/mnt/HC_Volume_106538179/%s_registro/%s_registro_%s.csv.gz' % (PFX, PFX, a.dia)
OUTD = '/mnt/HC_Volume_106538179/agentes_datos/f3_carry/'; os.makedirs(OUTD, exist_ok=True)
OUT = a.out or OUTD + 'vpv_%s_%s.csv.gz' % (a.marco, a.dia)
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json')); DES.update(json.load(open('/root/polymarket-research-datalogs/mapa_escala/des.json')))
PASO, VIDA, ACC, LO, HI = 10_000, 60_000, 5.0, 0.90 - 1e-9, 0.99 + 1e-9
K = {}            # token -> (coin, mercado, cierre_ms, lado)
COMP = {}         # (mercado, lado) -> token
ultimo_t = {}; ult_coloc = {}; vidas = collections.defaultdict(list); bn = collections.defaultdict(collections.deque); bn_t = {}
hdr = ['dia','mercado','coin','lado','cierre','t0_recv_ms','T_s','b','Q0','ba','as_','spread','bn_r300ms_bps','bn_r5s_bps','bn_r60s_bps','bn_edad_ms',
       'consA','consB','consC','relleno_pes','t_relleno_pes_ms','relleno_opt','t_relleno_opt_ms','barrido','fin_vida','gana','pnl_5acc_si_relleno']
fo = gzip.open(OUT + '.tmp', 'wt'); fo.write(','.join(hdr) + '\n'); nfil = 0
def bnret(sym, now, dt):
    d = bn.get(sym)
    if not d: return ''
    p1 = d[-1][1]; old = None
    for tt, pp in d:
        if tt <= now - dt: old = pp
        else: break
    return '' if old is None else '%.3f' % ((p1 / old - 1) * 1e4)
def cerrar(v, motivo):
    global nfil
    coin, mk, cie, lado = K[v['tk']]; g = DES.get(str(mk)); gana = '' if g is None else int(g == lado)
    pnl = '' if gana == '' else '%.4f' % (ACC * gana - ACC * v['b'])
    fo.write(','.join(map(str, [a.dia, mk, coin, lado, cie // 1000, v['t0'], '%.1f' % ((cie - v['t0']) / 1000), v['b'], v['Q0'], v['ba'], v['as'], '%.2f' % (v['ba'] - v['b']),
             v['r300'], v['r5'], v['r60'], v['edad'], round(v['A'], 3), round(v['B'], 3), round(v['C'], 3), int(v['tp'] is not None), v['tp'] or '', int(v['to'] is not None), v['to'] or '',
             int(v['sw']), motivo, gana, pnl])) + '\n'); nfil += 1
def avanzar(tk, now):
    keep = []
    for v in vidas[tk]:
        coin, mk, cie, lado = K[tk]
        if v['tp'] is not None and v['to'] is not None: cerrar(v, 'relleno'); continue
        if now > v['t0'] + VIDA or now > cie - 2000: cerrar(v, 'vida' if v['tp'] is None else 'relleno_pes'); continue
        keep.append(v)
    vidas[tk] = keep
def marca(v, now):
    q = v['Q0'] + ACC
    if v['tp'] is None and v['A'] + v['B'] >= q: v['tp'] = now
    if v['to'] is None and (max(v['A'] + v['B'], v['C']) >= q or (v['sw'] and v['A'] + v['B'] > 0)): v['to'] = now
t_ini = time.time(); n = 0
with gzip.open(SRC, 'rt', errors='replace') as f:
    try:
        for line in f:
            n += 1
            if a.max_lineas and n > a.max_lineas: break
            c = line.rstrip('\n').split(',')
            ty = c[0]
            if ty == 'x': continue
            if ty == 'k':
                if len(c) >= 8 and c[4] == a.marco:
                    try: cie = int(time.mktime(time.strptime(c[6][:19], '%Y-%m-%d %H:%M:%S')) - time.timezone) * 1000
                    except Exception: continue
                    K[c[2]] = (c[3], c[5], cie, c[7]); COMP[(c[5], c[7])] = c[2]
                continue
            if ty not in ('q', 't') or len(c) < 7 or c[2] not in K: continue
            tk = c[2]
            try: now = int(c[7]) if ty == 'q' else int(c[6])          # RECEPCION: q c[7], t c[6]
            except (ValueError, IndexError): continue
            if tk in ultimo_t and now < ultimo_t[tk] - 60_000:
                vidas[tk] = []; ult_coloc.pop(tk, None)        # salto atras de tramo: reinicio
            ultimo_t[tk] = now
            coin, mk, cie, lado = K[tk]
            if ty == 't':
                try: p = float(c[3]); sz = float(c[5])
                except ValueError: continue
                if c[4] == 'SELL':
                    for v in vidas[tk]:
                        if p <= v['b'] + 1e-9 and now >= v['t0']: v['A'] += sz; marca(v, now)
                else:
                    otro = COMP.get((mk, 'NO' if lado == 'YES' else 'YES'))
                    if otro:
                        for v in vidas.get(otro, []):
                            if p >= 1 - v['b'] - 1e-9 and now >= v['t0']: v['B'] += sz; marca(v, now)
                continue
            try: bb, ba, bs, as_ = float(c[3]), float(c[4]), float(c[5]), float(c[6])   # q: bb, ba, bs, as
            except ValueError: continue
            if bb >= ba: continue                                           # libro cruzado o bloqueado: descartar
            for v in vidas[tk]:
                if abs(bb - v['b']) < 1e-9:
                    if bs < v['last']: v['C'] += v['last'] - bs
                    v['last'] = bs
                elif bb < v['b'] - 1e-9: v['sw'] = True
                marca(v, now)
            avanzar(tk, now)
            T = (cie - now) / 1000.0
            if LO <= bb <= HI and 60 <= T <= TMAX and now - ult_coloc.get(tk, -10**15) >= PASO:
                sym = coin + 'USDT'; ed = ''
                vidas[tk].append({'tk': tk, 't0': now, 'b': round(bb, 2), 'Q0': bs, 'last': bs, 'ba': ba, 'as': as_, 'A': 0.0, 'B': 0.0, 'C': 0.0, 'sw': False,
                                  'tp': None, 'to': None, 'r300': '', 'r5': '', 'r60': '', 'edad': ed})
                ult_coloc[tk] = now
    except EOFError:
        print('AVISO: gz truncado tras %d lineas (se conserva lo leido)' % n)
for tk in list(vidas):
    for v in vidas[tk]: cerrar(v, 'fin_fichero')
fo.close(); os.replace(OUT + '.tmp', OUT)
print('dia %s lineas %d filas %d tokens5m %d seg %.0f -> %s (%d bytes)' % (a.dia, n, nfil, len(K), time.time() - t_ini, OUT, os.path.getsize(OUT)))
