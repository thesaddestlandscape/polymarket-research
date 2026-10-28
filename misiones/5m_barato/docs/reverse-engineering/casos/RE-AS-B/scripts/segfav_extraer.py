#!/usr/bin/env python3
"""segfav_extraer.py --dia D --out F [--max-lineas N] [--maxload 7] -- SOLO LECTURA. E-RE-AS-B-SEGFAV (PREREG_SEGFAV.md).
Senal: print TOMADOR BUY del token F (5min) a p en [0,70;0,90], T=(cierre-recv)/1000 en [20;300). Decision t_d = RECEPCION del print (c[6]).
Unidad: primer print por (mercado, lado F, Tbucket) con Tbuckets [20,60) [60,120) [120,180) [180,240) [240,300).
Ejecucion: estado del libro de F (y de su complementario C) = ultimo q valido (bb<ba) con recepcion <= t_d+L, L en (100,250,400);
se resuelve con la primera fila q/t del MERCADO con recepcion > t_d+L (o al cerrar el fichero). Guarda ask/as de F y de C en cada L,
edad del estado y el ask de F justo antes de t_d (pre).
PLACEBO (no condicionado a prints): por (mercado, lado F, Tbucket), primera fila q de F con ba en [0,70;0,90] dentro del Tbucket;
t_d = su recepcion; misma ejecucion. Reinicio del estado de un token si su reloj retrocede >60 s (tramos unidos)."""
import gzip, json, os, argparse, time
ap = argparse.ArgumentParser(); ap.add_argument('--dia', required=True); ap.add_argument('--out', required=True)
ap.add_argument('--max-lineas', type=int, default=0); ap.add_argument('--maxload', type=float, default=7.0); a = ap.parse_args()
SRC = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz' % a.dia
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
LS = (100, 250, 400); LMAX = max(LS); LO, HI = 0.70 - 1e-9, 0.90 + 1e-9
TB = ((20, 60), (60, 120), (120, 180), (180, 240), (240, 300))
def tbucket(T):
    for lo, hi in TB:
        if lo <= T < hi: return lo
    return None
K = {}; COMP = {}; ST = {}; ult = {}; usados = set(); pend = {}
cnt = dict(lineas=0, sen=0, plac=0, filas=0, reinicios=0, pausas=0, sin_estado_pre=0)
fo = gzip.open(a.out + '.tmp', 'wt')
fo.write('dia,tipo,mercado,coin,lado,cierre,td,T_s,tb,p_print,sz_print,askpre,' +
         ','.join('askF%d,asF%d,ageF%d,askC%d,asC%d' % (L, L, L, L, L) for L in LS) + ',gana\n')
def snap(tk):
    s = ST.get(tk); return s
def cerrar(u):
    g = DES.get(str(u['mk'])); gana = '' if g is None else int(g == u['lado'])
    cols = []
    for L in LS:
        f = u['ex'].get(L);
        if f is None: cols += ['', '', '', '', '']
        else: cols += [f[0], f[1], f[2], f[3], f[4]]
    fo.write(','.join(map(str, [a.dia, u['tipo'], u['mk'], u['coin'], u['lado'], u['cie'] // 1000, u['td'], '%.1f' % u['T'], u['tb'],
                                u['p'], u['sz'], u['askpre']] + cols + [gana])) + '\n')
    cnt['filas'] += 1
def fija(u, L):
    f = ST.get(u['tk']); c = ST.get(u['tkc']) if u['tkc'] else None
    if f is None: u['ex'][L] = ('', '', '', c[1] if c else '', c[3] if c else ''); return
    u['ex'][L] = (f[1], f[3], u['td'] + L - f[4], c[1] if c else '', c[3] if c else '')
def avanza(mk, now):
    lst = pend.get(mk)
    if not lst: return
    keep = []
    for u in lst:
        for L in LS:
            if L not in u['ex'] and now > u['td'] + L: fija(u, L)
        if len(u['ex']) == len(LS): cerrar(u)
        else: keep.append(u)
    pend[mk] = keep
def nueva(tipo, tk, now, T, tb, p, sz):
    coin, mk, cie, lado = K[tk]
    s = ST.get(tk)
    if s is None: cnt['sin_estado_pre'] += 1
    u = {'tipo': tipo, 'tk': tk, 'tkc': COMP.get((mk, 'NO' if lado == 'YES' else 'YES')), 'mk': mk, 'coin': coin, 'lado': lado, 'cie': cie,
         'td': now, 'T': T, 'tb': tb, 'p': p, 'sz': sz, 'askpre': s[1] if s else '', 'ex': {}}
    pend.setdefault(mk, []).append(u); usados.add((tipo, mk, lado, tb)); cnt['sen' if tipo == 'S' else 'plac'] += 1
def carga():
    try: return float(open('/proc/loadavg').read().split()[1])
    except Exception: return 0.0
t_ini = time.time()
with gzip.open(SRC, 'rt', errors='replace') as f:
    try:
        for line in f:
            cnt['lineas'] += 1; n = cnt['lineas']
            if a.max_lineas and n > a.max_lineas: break
            if n % 2_000_000 == 0:
                while carga() > a.maxload: cnt['pausas'] += 1; time.sleep(20)
            c = line.rstrip('\n').split(','); ty = c[0]
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
            if tk in ult and now < ult[tk] - 60_000:
                ST.pop(tk, None); cnt['reinicios'] += 1
                mk0 = K[tk][1]; pend[mk0] = [u for u in pend.get(mk0, []) if u['tk'] != tk and u['tkc'] != tk]
            ult[tk] = now
            coin, mk, cie, lado = K[tk]
            avanza(mk, now)                      # fija estados con recv <= td+L ANTES de aplicar esta fila
            T = (cie - now) / 1000.0; tb = tbucket(T)
            if ty == 't':
                if c[4] != 'BUY' or tb is None: continue
                try: p = float(c[3]); sz = float(c[5])
                except ValueError: continue
                if LO <= p <= HI and ('S', mk, lado, tb) not in usados: nueva('S', tk, now, T, tb, p, sz)
                continue
            try: bb, ba, bs, as_ = float(c[3]), float(c[4]), float(c[5]), float(c[6])
            except ValueError: continue
            if bb >= ba: continue
            ST[tk] = (bb, ba, bs, as_, now)
            if tb is not None and LO <= ba <= HI and ('P', mk, lado, tb) not in usados: nueva('P', tk, now, T, tb, '', '')
    except EOFError:
        print('AVISO: gz truncado tras %d lineas (se conserva lo leido)' % cnt['lineas'])
for mk in list(pend):
    for u in pend[mk]:
        for L in LS:
            if L not in u['ex']: fija(u, L)
        cerrar(u)
fo.close(); os.replace(a.out + '.tmp', a.out)
print('dia', a.dia, cnt, 'seg %.0f' % (time.time() - t_ini), a.out)
