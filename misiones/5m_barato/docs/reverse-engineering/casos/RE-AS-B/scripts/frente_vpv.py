#!/usr/bin/env python3
"""frente_vpv.py --dia D --out F [--max-lineas N] [--maxload 7] -- SOLO LECTURA. E-RE-AS-B-FRENTE (PREREG_FRENTE.md sha 1528f06b...).
Mismo calendario que experimentos/5m_barato/b_perdidas_22oct/detector_ex_ante/scripts/vida_puja_virtual_5m.py (cada 10 s por token
5min, bb en [0,10;0,30], T en [60;300] s, en la RECEPCION de la fila q; reinicio de token si la hora retrocede >60 s; q cruzadas fuera).
Politica: puja 5 acc a b'=bb+0,01 solo si ba-bb>=0,02 (nivel nuevo, cola delante 0). Por vida guarda el estado del libro (bb,ba) de
la primera q del token con recv>=t0+85 y >=t0+250 ms, y los prints que la rellenarian (recv>=t0 y <=fin): A = SELL del token a p<=b';
B = BUY del complementario a p>=1-b'. Deja de guardar cuando max(A,B) contados desde t0+250 >= 5 (basta para Lp<=250 y ambas reglas).
fin = min(t0+60 s, cierre-2 s). Una fila por vida con pol=1 (las de spread<0,02 solo se cuentan, pero fijan el calendario)."""
import gzip, json, os, argparse, time
ap = argparse.ArgumentParser(); ap.add_argument('--dia', required=True); ap.add_argument('--out', required=True)
ap.add_argument('--max-lineas', type=int, default=0); ap.add_argument('--maxload', type=float, default=7.0); a = ap.parse_args()
SRC = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz' % a.dia
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
PASO, VIDA, ACC, LO, HI = 10_000, 60_000, 5.0, 0.10 - 1e-9, 0.30 + 1e-9
K = {}; COMP = {}; ultimo_t = {}; ult_coloc = {}; vidas = {}
cnt = dict(lineas=0, filas=0, calendario=0, pol0=0, reinicios=0, pausas=0)
fo = gzip.open(a.out + '.tmp', 'wt')
fo.write('dia,mercado,coin,lado,cierre,t0,T_s,bb,bp,ba,Q0,bb85,ba85,bb250,ba250,fin,motivo,gana,prints\n')
def cerrar(v, motivo):
    coin, mk, cie, lado = K[v['tk']]; g = DES.get(str(mk)); gana = '' if g is None else int(g == lado)
    a85 = v['arr'].get(85, ('', '')); a250 = v['arr'].get(250, ('', ''))
    pr = ';'.join('%d:%g:%s' % x for x in v['pr'])
    fo.write(','.join(map(str, [a.dia, mk, coin, lado, cie // 1000, v['t0'], '%.1f' % ((cie - v['t0']) / 1000), v['b'], v['bp'], v['ba'], v['Q0'],
                                a85[0], a85[1], a250[0], a250[1], v['fin'], motivo, gana, pr])) + '\n')
    cnt['filas'] += 1
def suma(v, now, sz, typ):
    if v['done'] or now < v['t0'] or now > v['fin']: return
    v['pr'].append((now, sz, typ))
    if now >= v['t0'] + 250:
        v[typ] += sz
        if max(v['A'], v['B']) >= ACC: v['done'] = True
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
            if tk in ultimo_t and now < ultimo_t[tk] - 60_000:
                vidas[tk] = []; ult_coloc.pop(tk, None); cnt['reinicios'] += 1
            ultimo_t[tk] = now
            coin, mk, cie, lado = K[tk]
            if ty == 't':
                try: p = float(c[3]); sz = float(c[5])
                except ValueError: continue
                if c[4] == 'SELL':
                    for v in vidas.get(tk, []):
                        if p <= v['bp'] + 1e-9: suma(v, now, sz, 'A')
                else:
                    otro = COMP.get((mk, 'NO' if lado == 'YES' else 'YES'))
                    if otro:
                        for v in vidas.get(otro, []):
                            if p >= 1 - v['bp'] - 1e-9: suma(v, now, sz, 'B')
                continue
            try: bb, ba, bs = float(c[3]), float(c[4]), float(c[5])
            except ValueError: continue
            if bb >= ba: continue
            keep = []
            for v in vidas.get(tk, []):
                for L in (85, 250):
                    if L not in v['arr'] and now >= v['t0'] + L: v['arr'][L] = (bb, ba)
                if v['done']: cerrar(v, 'lleno'); continue
                if now > v['fin']: cerrar(v, 'vida'); continue
                keep.append(v)
            vidas[tk] = keep
            T = (cie - now) / 1000.0
            if LO <= bb <= HI and 60 <= T <= 300 and now - ult_coloc.get(tk, -10**15) >= PASO:
                cnt['calendario'] += 1; ult_coloc[tk] = now
                if ba - bb >= 0.02 - 1e-9:
                    vidas.setdefault(tk, []).append({'tk': tk, 't0': now, 'b': round(bb, 2), 'bp': round(bb + 0.01, 2), 'ba': ba, 'Q0': bs,
                                                     'fin': min(now + VIDA, cie - 2000), 'arr': {}, 'pr': [], 'A': 0.0, 'B': 0.0, 'done': False})
                else: cnt['pol0'] += 1
    except EOFError:
        print('AVISO: gz truncado tras %d lineas (se conserva lo leido)' % cnt['lineas'])
for tk in list(vidas):
    for v in vidas[tk]: cerrar(v, 'lleno' if v['done'] else 'fin_fichero')
fo.close(); os.replace(a.out + '.tmp', a.out)
print('dia', a.dia, cnt, 'seg %.0f' % (time.time() - t_ini), a.out)
