#!/usr/bin/env python3
"""cxb60_resolve.py DIA [--out DIR] [--gmap-dir DIR] -- une el desenlace OFICIAL a los segmentos del dry-run (dec_<D>.csv.gz) y escribe res_<D>.csv.gz (se REGENERA entero cada vez: idempotente, sin duplicar PnL).
Desenlace: gmap_*.json del cron sa_r1 (mid -> 'YES'/'NO', solo lectura; el mismo que usa el motor via capt.outcome). Un relleno sin desenlace queda con gana vacio y se CUENTA como 'sin_desenlace' (missing != 0: no entra en pnl/EV, se reporta la cobertura).
pnl = q*(gana-L) + q*0,2*0,07*L*(1-L) (convencion del motor; rebate 20 %). Unicidad (tok, L, var, seg): duplicados se descartan (se queda el primero) y se cuentan. No envia nada, no usa red."""
import os, sys, csv, gzip, io, json, glob, collections
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import cxb60_dryrun_fase0 as R
REB = 0.2 * 0.07


def carga_gmap(d):
    gm = {}
    for f in sorted(glob.glob(d.rstrip('/') + '/gmap_*.json')):
        try:
            for s, v in json.load(open(f)).items():
                if v.get('des') in ('YES', 'NO'): gm[str(v['id'])] = v['des']
        except (OSError, ValueError): continue
    return gm


def resolve(dec_path, gm):
    txt, ok = R.miembros_validos(dec_path); rows = list(csv.DictReader(io.StringIO(txt))); vistos = set(); out = []; st = collections.Counter()
    for r in rows:
        if r['tipo'] != 'seg': continue
        k = (r['tok'], r['L'], r['var'], r['seg'])
        if k in vistos: st['duplicados'] += 1; continue
        vistos.add(k); q = float(r['q']); L = float(r['L']); des = gm.get(r['mid']); st['seg'] += 1; st['canc'] += int(r['canc'] or 0)
        r['gana'] = ''; r['pnl'] = ''; r['cost'] = ''
        if q > 1e-9:
            st['fills'] += 1
            if des is None: st['sin_desenlace'] += 1
            else:
                g = 1.0 if des == r['lado'] else 0.0; r['gana'] = g; r['pnl'] = round(q * (g - L) + q * REB * L * (1 - L), 6); r['cost'] = round(q * L, 6)
        out.append(r)
    return out, st


def resumen(out):
    por = collections.defaultdict(lambda: [0, 0, 0, 0.0, 0.0])
    for r in out:
        a = por[r['var']]; a[0] += 1; a[1] += int(r['canc'] or 0)
        if r['pnl'] != '': a[2] += 1; a[3] += float(r['cost']); a[4] += float(r['pnl'])
    return {v: dict(seg=a[0], canc=a[1], fills_resueltos=a[2], coste=round(a[3], 2), pnl=round(a[4], 3), ev_por_euro=round(a[4] / a[3], 4) if a[3] > 0 else None) for v, a in sorted(por.items())}


def main():
    import argparse; ap = argparse.ArgumentParser(); ap.add_argument('dia'); ap.add_argument('--out', default=R.DL + 'cxb60_dryrun/'); ap.add_argument('--gmap-dir', default=R.DL + 'sa_r1/'); a = ap.parse_args()
    dec = a.out.rstrip('/') + f'/dec_{a.dia}.csv.gz'; gm = carga_gmap(a.gmap_dir); out, st = resolve(dec, gm)
    cols = R.COLS[:-1] + ['t_wall_ms', 'gana', 'pnl', 'cost']; buf = io.StringIO(); w = csv.DictWriter(buf, fieldnames=cols, extrasaction='ignore'); w.writeheader(); [w.writerow(r) for r in out]
    p = a.out.rstrip('/') + f'/res_{a.dia}.csv.gz'; tmp = p + '.tmp'; open(tmp, 'wb').write(R.gzip.compress(buf.getvalue().encode())); os.replace(tmp, p)
    cob = 1 - st['sin_desenlace'] / max(st['fills'], 1); print(json.dumps(dict(dia=a.dia, **st, cobertura_desenlace=round(cob, 4), resumen=resumen(out)), indent=1))


if __name__ == '__main__': main()
