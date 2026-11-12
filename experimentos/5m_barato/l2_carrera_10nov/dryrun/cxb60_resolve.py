#!/usr/bin/env python3
"""cxb60_resolve.py DIA [--out DIR] [--gmap-dir DIR] -- une el desenlace OFICIAL a los segmentos del dry-run (dec_<D>.csv.gz) y escribe res_<D>.csv.gz (se REGENERA entero cada vez: idempotente, sin duplicar PnL). Solo importa cxb60_io (H9: ya no arrastra el motor).
Desenlace: gmap_*.json del cron sa_r1 (mid -> 'YES'/'NO', solo lectura). JOIN EXACTO (H10): por `mid` Y comprobando que el token del segmento esta en `toks` del gmap; si no esta, el segmento queda sin desenlace y se cuenta como `join_tok_mismatch` (no se resuelve por aproximacion).
Un relleno sin desenlace queda con gana vacio y se CUENTA como 'sin_desenlace' (missing != 0: no entra en pnl/EV; se reporta la cobertura).
pnl = q*(gana-L) + q*0,2*0,07*L*(1-L) (convencion del motor; rebate 20 %); cost = q*L; cost_pot = rem_antes*L (dinero que la colocacion habria comprometido: denominador del EV incondicional).
Unicidad (tok, L, var, seg): duplicados se descartan (se queda el primero) y se cuentan. No envia nada, no usa red."""
import os, sys, csv, gzip, io, json, glob, collections
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import cxb60_io as IO
REB = 0.2 * 0.07
DL = '/root/polymarket-research-datalogs/'


def carga_gmap(d):
    """mid -> (des, set(toks) o None). Si un mid aparece en varios ficheros gana el ultimo con des valido."""
    gm = {}
    for f in sorted(glob.glob(d.rstrip('/') + '/gmap_*.json')):
        try:
            for s, v in json.load(open(f)).items():
                if v.get('des') in ('YES', 'NO'): gm[str(v['id'])] = (v['des'], set(map(str, v['toks'])) if v.get('toks') else None)
        except (OSError, ValueError): continue
    return gm


def resolve_iter(dec_path, gm, st):
    """Generador de filas seg resueltas (streaming: no materializa el dia entero). `st` (Counter) acumula contadores."""
    txt, ok = IO.miembros_validos(dec_path); vistos = set()
    for r in csv.DictReader(io.StringIO(txt)):
        if r['tipo'] != 'seg': continue
        k = (r['tok'], r['L'], r['var'], r['seg'])
        if k in vistos: st['duplicados'] += 1; continue
        vistos.add(k); q = float(r['q']); L = float(r['L']); g = gm.get(r['mid']); des = None; st['seg'] += 1; st['canc'] += int(r['canc'] or 0)
        if g is not None:
            if g[1] is not None and r['tok'] not in g[1]: st['join_tok_mismatch'] += 1
            else: des = g[0]
        r['gana'] = ''; r['pnl'] = ''; r['cost'] = ''; r['cost_pot'] = round(float(r['rem_antes']) * L, 6); r['des'] = des or ''
        if q > 1e-9:
            st['fills'] += 1
            if des is None: st['sin_desenlace'] += 1
            else:
                gg = 1.0 if des == r['lado'] else 0.0; r['gana'] = gg; r['pnl'] = round(q * (gg - L) + q * REB * L * (1 - L), 6); r['cost'] = round(q * L, 6)
        yield r


def resolve(dec_path, gm):
    st = collections.Counter(); out = list(resolve_iter(dec_path, gm, st)); return out, st


class Resumen:
    """Acumulador por variante (sin placebo), incremental."""
    def __init__(self): self.por = collections.defaultdict(lambda: [0, 0, 0, 0.0, 0.0])

    def add(self, r):
        a = self.por[r['var']]; a[0] += 1; a[1] += int(r['canc'] or 0)
        if r['pnl'] != '': a[2] += 1; a[3] += float(r['cost']); a[4] += float(r['pnl'])

    def out(self): return {v: dict(seg=a[0], canc=a[1], fills_resueltos=a[2], coste=round(a[3], 2), pnl=round(a[4], 3), ev_por_euro_condicional_a_fill=round(a[4] / a[3], 4) if a[3] > 0 else None) for v, a in sorted(self.por.items()) if not v.startswith('PLC60_')}


def resumen(out):
    R = Resumen(); [R.add(r) for r in out]; return R.out()


def main():
    import argparse; ap = argparse.ArgumentParser(); ap.add_argument('dia'); ap.add_argument('--out', default=DL + 'cxb60_dryrun/'); ap.add_argument('--gmap-dir', default=DL + 'sa_r1/'); a = ap.parse_args()
    dec = a.out.rstrip('/') + f'/dec_{a.dia}.csv.gz'; gm = carga_gmap(a.gmap_dir); st = collections.Counter(); R = Resumen()
    cols = IO.COLS[:-1] + ['t_wall_ms', 'gana', 'pnl', 'cost', 'cost_pot', 'des']; p = a.out.rstrip('/') + f'/res_{a.dia}.csv.gz'; tmp = p + '.tmp'
    with gzip.open(tmp, 'wt', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction='ignore', lineterminator='\n'); w.writeheader()
        for r in resolve_iter(dec, gm, st): w.writerow(r); R.add(r)
    os.replace(tmp, p); cob = 1 - st['sin_desenlace'] / max(st['fills'], 1); print(json.dumps(dict(dia=a.dia, **st, cobertura_desenlace=round(cob, 4), gmap_mids=len(gm), resumen=R.out()), indent=1))


if __name__ == '__main__': main()
