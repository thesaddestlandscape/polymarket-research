#!/usr/bin/env python3
"""F8 vpv_f8.py --dia D : vidas de puja virtual AMPLIADAS (copia de detector_ex_ante/scripts/vida_puja_virtual_5m.py, PASIVO, solo lectura).
Diferencias DECLARADAS frente a la base (todas hacia el lado PESIMISTA o para QA, ver PREREG f8 y avisos QA):
 (a) relleno pesimista SIN doble conteo del mismo casado: un print de OTRO token del mismo mercado, mismo tamano (4 dec.), precio complementario
     (p1+p2=1) y |dt recepcion| <= 300 ms respecto a un print previo se marca 'dup' y NO consume cola (cota inferior del consumo).
 (b) un print/cambio de libro posterior a t0+60 s o a cierre-2 s no marca relleno (la base lo permitia hasta el siguiente q del token).
 (c) vidas cortadas por reinicio de tramo (hora retrocede >60 s) o fin de fichero se CIERRAN con censurada=1 (no se descartan en silencio);
     el analisis las excluye de forma ex ante (no dependen del desenlace) y las cuenta.
 (d) desenlace oficial = cache maker_ms_desenlaces_cache.json leida AHORA (no la de 04:41); 'gana' vacio = missing (se reporta, nunca = 0 ni se filtra a ciegas).
 (e) rasgos P1/P2 ex ante a t0 (RECEPCION): bn_rng60, prints del mercado en 120 s (n/usd, contra la puja, edades). Binance = recepcion c[7].
Sin optimista (no se usa). Salida: /root/polymarket-research-datalogs/f8_estructura/vpv8_D.csv.gz (fuera de git)."""
import sys, gzip, json, os, argparse, collections, time, csv
ap = argparse.ArgumentParser(); ap.add_argument('--dia', required=True); ap.add_argument('--max-lineas', type=int, default=0)
ap.add_argument('--out', default=None); ap.add_argument('--force', action='store_true'); a = ap.parse_args()
SRC = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz' % a.dia
OUTD = '/root/polymarket-research-datalogs/f8_estructura/'; os.makedirs(OUTD, exist_ok=True)
OUT = a.out or OUTD + 'vpv8_%s.csv.gz' % a.dia
if os.path.exists(OUT) and not a.force and not a.max_lineas:
    print('ya existe', OUT); sys.exit(0)
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
PASO, VIDA, ACC, LO, HI = 10_000, 60_000, 5.0, 0.10 - 1e-9, 0.30 + 1e-9
WIN = 120_000
K = {}; COMP = {}
ultimo_t = {}; ult_coloc = {}; vidas = collections.defaultdict(list); bn = collections.defaultdict(collections.deque); bn_t = {}
mdq = {}; mlast = {}          # mercado -> deque de prints (t, token, lado_token, precio, side, sz, dup); ultimo t visto del mercado
hdr = ['dia', 'mercado', 'coin', 'lado', 'cierre', 't0_recv_ms', 'T_s', 'b', 'Q0', 'ba', 'as_', 'spread', 'bn_r300ms_bps', 'bn_r5s_bps', 'bn_r60s_bps', 'bn_rng60_bps', 'bn_edad_ms',
       'pm_edad_ms', 'pm_n120', 'pm_usd120', 'pc_n120', 'pc_usd120', 'pc_edad_ms',
       'consA', 'consB', 'ndup_vida', 'relleno_pes', 't_relleno_pes_ms', 'censurada', 'fin_vida', 'gana', 'pnl_5acc_si_relleno']
fo = gzip.open(OUT + '.tmp', 'wt', newline=''); W = csv.writer(fo); W.writerow(hdr); nfil = 0
cnt = collections.Counter()
def bnstats(sym, now):
    d = bn.get(sym)
    if not d: return ('', '', '', '')
    p1 = d[-1][1]; o3 = o5 = o60 = None; hi = lo = p1
    for tt, pp in d:
        if tt <= now - 300: o3 = pp
        if tt <= now - 5000: o5 = pp
        if tt <= now - 60000: o60 = pp
        if tt > now - 60000:
            if pp > hi: hi = pp
            if pp < lo: lo = pp
    f = lambda o: '' if o is None else '%.3f' % ((p1 / o - 1) * 1e4)
    return (f(o3), f(o5), f(o60), '%.3f' % ((hi - lo) / p1 * 1e4))
def cerrar(v, motivo, cens):
    global nfil
    coin, mk, cie, lado = K[v['tk']]; g = DES.get(str(mk)); gana = '' if g is None else int(g == lado)
    pnl = '' if gana == '' else '%.4f' % (ACC * gana - ACC * v['b'])
    W.writerow([a.dia, mk, coin, lado, cie // 1000, v['t0'], '%.1f' % ((cie - v['t0']) / 1000), v['b'], v['Q0'], v['ba'], v['as'], '%.2f' % (v['ba'] - v['b'])] + list(v['bn']) +
               [v['edad']] + v['pm'] + [round(v['A'], 3), round(v['B'], 3), v['nd'], int(v['tp'] is not None), v['tp'] or '', int(cens), motivo, gana, pnl]); nfil += 1
def vivo(v, now, cie): return now <= v['t0'] + VIDA and now <= cie - 2000
def avanzar(tk, now):
    keep = []
    coin, mk, cie, lado = K[tk]
    for v in vidas[tk]:
        if v['tp'] is not None: cerrar(v, 'relleno_pes', 0); continue
        if not vivo(v, now, cie): cerrar(v, 'vida', 0); continue
        keep.append(v)
    vidas[tk] = keep
def marca(v, now):
    if v['tp'] is None and v['A'] + v['B'] >= v['Q0'] + ACC: v['tp'] = now
def pm_feats(mk, tk, now):
    d = mdq.get(mk)
    if not d: return ['', 0, 0.0, 0, 0.0, '']
    last = None; n = 0; usd = 0.0; cn = 0; cusd = 0.0; clast = None
    for (t, tok, ld, p, sd, sz, dup) in d:
        if t < now - WIN or t > now: continue
        n += 1; u = p * sz; usd += u; last = t
        # contra la puja (bid del token tk): SELL del propio token, o BUY del complementario
        if (tok == tk and sd == 'SELL') or (tok != tk and sd == 'BUY'):
            cn += 1; cusd += u; clast = t
    return ['' if last is None else now - last, n, round(usd, 3), cn, round(cusd, 3), '' if clast is None else now - clast]
t_ini = time.time(); n = 0
with gzip.open(SRC, 'rt', errors='replace') as f:
    try:
        for line in f:
            n += 1
            if a.max_lineas and n > a.max_lineas: break
            c = line.rstrip('\n').split(',')
            ty = c[0]
            if ty == 'x':
                if len(c) < 8: continue
                sym = c[2]; now = int(c[7]); p = float(c[3]); d = bn[sym]
                if d and now < d[-1][0] - 60_000: d.clear()
                d.append((now, p)); bn_t[sym] = now
                while d and d[0][0] < now - 61_000: d.popleft()
                continue
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
            if tk in ultimo_t and now < ultimo_t[tk] - 60_000:       # salto atras de tramo: cerrar CENSURADAS (no descartar)
                for v in vidas[tk]: cerrar(v, 'reinicio', 1)
                vidas[tk] = []; ult_coloc.pop(tk, None)
            ultimo_t[tk] = now
            if mk in mlast and now < mlast[mk] - 60_000: mdq[mk] = collections.deque(); mlast[mk] = now
            else: mlast[mk] = max(mlast.get(mk, 0), now)
            if ty == 't':
                try: p = float(c[3]); sz = float(c[5])
                except ValueError: continue
                sd = c[4]; d = mdq.get(mk)
                if d is None: d = mdq[mk] = collections.deque()
                while d and d[0][0] < now - 150_000: d.popleft()
                dup = False; sz4 = round(sz, 4)
                for (t2, tok2, ld2, p2, sd2, sz2, dup2) in d:
                    if now - t2 <= 300 and tok2 != tk and round(sz2, 4) == sz4 and abs(p2 + p - 1) < 1e-9: dup = True; break
                d.append((now, tk, lado, p, sd, sz, dup)); cnt['prints'] += 1; cnt['dup'] += dup
                if dup: continue
                if sd == 'SELL':
                    for v in vidas[tk]:
                        if p <= v['b'] + 1e-9 and now >= v['t0'] and vivo(v, now, cie): v['A'] += sz; marca(v, now)
                else:
                    otro = COMP.get((mk, 'NO' if lado == 'YES' else 'YES'))
                    if otro:
                        for v in vidas.get(otro, []):
                            if p >= 1 - v['b'] - 1e-9 and now >= v['t0'] and vivo(v, now, K[otro][2]): v['B'] += sz; marca(v, now)
                continue
            try: bb, ba, bs, as_ = float(c[3]), float(c[4]), float(c[5]), float(c[6])
            except ValueError: continue
            if bb >= ba: continue
            avanzar(tk, now)
            T = (cie - now) / 1000.0
            if LO <= bb <= HI and 60 <= T <= 300 and now - ult_coloc.get(tk, -10**15) >= PASO:
                sym = coin + 'USDT'; ed = now - bn_t[sym] if sym in bn_t else ''
                vidas[tk].append({'tk': tk, 't0': now, 'b': round(bb, 2), 'Q0': bs, 'ba': ba, 'as': as_, 'A': 0.0, 'B': 0.0, 'nd': 0, 'tp': None,
                                  'bn': bnstats(sym, now), 'edad': ed, 'pm': pm_feats(mk, tk, now)})
                ult_coloc[tk] = now
    except EOFError:
        print('AVISO: gz truncado tras %d lineas (se conserva lo leido)' % n)
for tk in list(vidas):
    for v in vidas[tk]: cerrar(v, 'fin_fichero', 1)
fo.close(); os.replace(OUT + '.tmp', OUT)
print('dia %s lineas %d filas %d tokens5m %d prints %d dup %d seg %.0f -> %s' % (a.dia, n, nfil, len(K), cnt['prints'], cnt['dup'], time.time() - t_ini, OUT))
