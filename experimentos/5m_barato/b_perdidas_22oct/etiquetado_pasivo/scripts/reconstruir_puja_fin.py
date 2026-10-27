#!/usr/bin/env python3
"""Reconstruye un `puja_fin` para mercados B que tienen puja_post pero no puja_fin (proceso muerto antes de Exp.finalizar).
SOLO LEE el ledger original (nunca escribe en el). Salida separada, idempotente por slug: DL/puja_fin_reconstruido.jsonl (reconstruido=true).
Que se reconstruye: rellenos por lectura/verificada/relleno_tardio (get_order en vivo), gemelo simulado, motivo de cierre, contraste con
posiciones.csv (cadena). Que NO se puede: markouts (mid libro WS no persistido) -> None (missing, nunca 0); contraste /trades -> None.
Uso: reconstruir_puja_fin.py [--slugs a,b,..] [--dry]  (sin --slugs: todos los cerrados sin puja_fin)"""
import os, sys, json, csv, time, fcntl, argparse, datetime as dt

DL = os.environ.get('RPF_DL', '/root/polymarket-research-datalogs')
LEDGER = os.environ.get('RPF_LEDGER', os.path.join(DL, 'experimento_h47_B_ledger.jsonl'))
OUT = os.environ.get('RPF_OUT', os.path.join(DL, 'puja_fin_reconstruido.jsonl'))
POSIC = os.environ.get('RPF_POSIC', '/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/posiciones.csv')
MARGEN_S = 35.0


def leer_jsonl(path):
    """Tolera una ultima linea a medias o corrupta; devuelve (filas, n_malas)."""
    out, bad = [], 0
    if not os.path.exists(path): return out, bad
    for l in open(path):
        try: out.append(json.loads(l))
        except Exception: bad += 1
    return out, bad


def fin_de(slug): return float(slug.rsplit('-', 1)[1]) + 300.0


def reconstruir(filas, posic, ahora, slugs=None):
    """Devuelve lista de registros puja_fin reconstruidos (uno por slug candidato)."""
    posts, fin, oid2slug = {}, set(), {}
    for d in filas:
        t = d.get('tipo')
        if t == 'puja_fin': fin.add(d['slug'])
        elif t == 'puja_post':
            posts.setdefault(d['slug'], {}).setdefault(d['oid'], d); oid2slug[d['oid']] = d['slug']
    cand = [s for s in posts if s not in fin and ahora >= fin_de(s) + MARGEN_S and (slugs is None or s in slugs)]
    por = {s: dict(lec={}, ver={}, tard={}, gem={}, cierre=None, mfin=False, repega=0, banda=0) for s in cand}
    for d in filas:
        t = d.get('tipo'); s = d.get('slug') or oid2slug.get(d.get('oid'))
        if s not in por: continue
        p = por[s]; o = d.get('oid')
        if t == 'lectura': 
            if (d.get('f') or 0) >= p['lec'].get(o, (0, None))[0]: p['lec'][o] = (d.get('f') or 0, d)
        elif t == 'verificada': p['ver'][o] = max(p['ver'].get(o, 0), d.get('f') or 0)
        elif t == 'relleno_tardio': p['tard'].setdefault(o, []).append(d.get('acc') or 0)
        elif t == 'gemelo_relleno': p['gem'][o] = max(p['gem'].get(o, 0), d.get('acc_total') or 0)
        elif t == 'cierre_mercado': p['cierre'] = d.get('motivo')
        elif t == 'mercado_fin': p['mfin'] = True
        elif t == 'repega': p['repega'] += 1
        elif t == 'cancela_banda': p['banda'] += 1
    res = []
    for s in sorted(cand):
        p, op = por[s], posts[s]
        pr = next(iter(op.values()))
        rell, tot = [], 0.0
        for o, d0 in op.items():
            f_l = p['lec'].get(o, (0, None))[0]; f_v = p['ver'].get(o, 0); f_t = sum(p['tard'].get(o, []))
            f = max(f_l, f_v, f_t)
            if f > 1e-9:
                fuente = 'lectura' if f == f_l else ('verificada' if f == f_v else 'relleno_tardio')
                ld = p['lec'].get(o, (0, None))[1]
                rell.append(dict(oid=o, acc=f, precio=(ld or {}).get('precio', float(d0['precio'])), fuente=fuente,
                                 t_deteccion=dt.datetime.fromisoformat((ld or d0)['ts']).timestamp(), tardio=(f == f_t and f_t > max(f_l, f_v)),
                                 markouts_disponibles=False))
                tot += f
        lado = pr['lado']; outc = 'Up' if lado == 'YES' else 'Down'
        ch = posic.get((s, outc))
        gem = [p['gem'].get(o, 0.0) for o in op]
        res.append(dict(tipo='puja_fin', reconstruido=True, slug=s, coin=pr['coin'], lado=lado, k=pr.get('k'), n_ordenes=len(op),
                        llenas_detectadas=tot, relleno_real=bool(tot > 1e-9), fin_puja=p['cierre'], mercado_fin_original=p['mfin'],
                        n_repega=p['repega'], n_cancela_banda=p['banda'], rellenos=rell,
                        sim_relleno_cualquiera=bool(any(x > 1e-9 for x in gem)), sim_acciones_max=max(gem) if gem else 0.0,
                        markouts='missing', contraste_trades='missing',
                        contraste_cadena=dict(acciones=ch['acciones'], coste=ch['coste']) if ch else None,
                        discrepa_cadena=(None if ch is None and tot <= 1e-9 else (abs((ch['acciones'] if ch else 0.0) - tot) > 1e-6)),
                        variante=pr.get('variante'), reconstruido_utc=dt.datetime.fromtimestamp(ahora, dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')))
    return res


def cargar_posic():
    out = {}
    if not os.path.exists(POSIC): return out
    for r in csv.DictReader(open(POSIC)):
        if not r.get('tanda_B'): continue
        k = (r['mercado'], r['outcome'])
        a = out.setdefault(k, dict(acciones=0.0, coste=0.0)); a['acciones'] += float(r['acciones']); a['coste'] += float(r['coste'])
    return out


def escribir(regs):
    """Idempotente por slug, bajo flock; solo anade; fsync. Devuelve (nuevos, ya_estaban)."""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT + '.lock', 'w') as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        ya = {d.get('slug') for d in leer_jsonl(OUT)[0]}
        nuevos = [r for r in regs if r['slug'] not in ya]
        if nuevos:
            with open(OUT, 'a') as f:
                if f.tell() and open(OUT, 'rb').read()[-1:] != b'\n': f.write('\n')    # cola a medias
                for r in nuevos: f.write(json.dumps(r, separators=(',', ':')) + '\n')
                f.flush(); os.fsync(f.fileno())
    return len(nuevos), len(regs) - len(nuevos)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--slugs'); ap.add_argument('--dry', action='store_true'); a = ap.parse_args()
    filas, bad = leer_jsonl(LEDGER)
    regs = reconstruir(filas, cargar_posic(), time.time(), set(a.slugs.split(',')) if a.slugs else None)
    print(f'ledger_filas={len(filas)} malas={bad} candidatos={len(regs)}')
    for r in regs: print(r['slug'], 'acc', r['llenas_detectadas'], 'cadena', r['contraste_cadena'], 'discrepa', r['discrepa_cadena'], 'cierre', r['fin_puja'])
    if not a.dry: print('nuevos=%d ya_estaban=%d -> %s' % (*escribir(regs), OUT))


if __name__ == '__main__': main()
