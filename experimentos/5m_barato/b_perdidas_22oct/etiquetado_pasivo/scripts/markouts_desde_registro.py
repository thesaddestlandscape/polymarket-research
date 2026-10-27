#!/usr/bin/env python3
"""Markouts (+5/+30/+120 s, como Exp.finalizar de experimento_maker_h47.py) de los rellenos de los puja_fin RECONSTRUIDOS,
con el mid (bid+ask)/2 del token reconstruido desde las filas `q` de VOL/m5_registro (top de libro por WS, hora de RECEPCION c5).
SOLO LEE: puja_fin_reconstruido.jsonl y m5_registro_D.csv.gz. Escribe en un fichero SEPARADO (nunca el ledger), idempotente por (slug,oid).
Regla de finalizar: t0+s > fin del mercado (start+300) o relleno tardio -> missing (None), nunca 0. mid_en = ultimo mid con recepcion <= t.
Ademas guarda edad_q_s (t - recepcion del q usado) y flag stale si > STALE_S: la fuente es por cambio de top, no por reloj.
Uso: markouts_desde_registro.py [--dry]   (env MDR_DL, MDR_VOL, MDR_OUT)"""
import os, sys, json, gzip, subprocess, datetime as dt, bisect

DL = os.environ.get('MDR_DL', '/root/polymarket-research-datalogs')
VOL = os.environ.get('MDR_VOL', '/mnt/HC_Volume_106538179/m5_registro')
IN = os.path.join(DL, 'puja_fin_reconstruido.jsonl')
OUT = os.environ.get('MDR_OUT', os.path.join(DL, 'puja_fin_markouts_m5registro.jsonl'))
MARK_S = (5, 30, 120)
STALE_S = 30.0


def dias(t0, t1, atras=1800):
    d = dt.datetime.utcfromtimestamp(t0 - atras).date()
    out = []
    while d <= dt.datetime.utcfromtimestamp(t1 + 200).date():
        out.append(d.isoformat()); d += dt.timedelta(days=1)
    return out


def _lineas(path, grep_args):
    if not os.path.exists(path): return []
    p = subprocess.run(f"zcat '{path}' | grep {grep_args}", shell=True, capture_output=True, text=True)
    return p.stdout.splitlines()


def token_de(slug, lado, d):
    """token YES/NO de un slug desde filas k (k,t,token,COIN,5min,market_id,end,YES|NO)."""
    coin, ini = slug.split('-')[0], slug.rsplit('-', 1)[1]
    fin = dt.datetime.utcfromtimestamp(int(ini) + 300).strftime('%Y-%m-%d %H:%M:%S+00:00')
    for dia in dias(int(ini), int(ini) + 300):
        for l in _lineas(os.path.join(VOL, f'm5_registro_{dia}.csv.gz'), f"-F -e ',{coin.upper()},5min,'"):
            c = l.split(',')
            if len(c) >= 8 and c[0] == 'k' and c[6] == fin and c[7] == lado:
                return c[2]
    return None


def serie_mid(tok, slug):
    ini = int(slug.rsplit('-', 1)[1]); xs = []
    for dia in dias(ini, ini + 300 + 200):
        for l in _lineas(os.path.join(VOL, f'm5_registro_{dia}.csv.gz'), f"-F '{tok}'"):
            c = l.split(',')
            if c[0] != 'q' or len(c) < 8: continue
            try: b, a, rec = float(c[3]), float(c[4]), float(c[7]) / 1000.0
            except ValueError: continue
            if b > 0 and a > 0 and b <= a: xs.append((rec, (b + a) / 2))     # libro cruzado/vacio -> no es mid
    xs.sort()
    return xs


def mid_en(xs, ts, t):
    i = bisect.bisect_right(ts, t)
    return (xs[i - 1][1], t - xs[i - 1][0]) if i else (None, None)


def calcular(rec, xs):
    """rec = un puja_fin reconstruido; xs = serie [(recepcion_s, mid)] del token. Devuelve lista de filas por relleno."""
    fin = float(rec['slug'].rsplit('-', 1)[1]) + 300.0
    ts = [x[0] for x in xs]; out = []
    for r in rec['rellenos']:
        t0 = r['t_deteccion']; f = {'slug': rec['slug'], 'oid': r['oid'], 'lado': rec['lado'], 'acc': r['acc'], 'precio': r['precio'],
                                    't_deteccion': t0, 'fuente_mid': 'm5_registro.q', 'n_q_serie': len(xs)}
        for s in MARK_S:
            m, edad = (mid_en(xs, ts, t0 + s) if (t0 + s <= fin and not r.get('tardio') and xs) else (None, None))
            f[f'mid_{s}s'] = m
            f[f'markout_{s}s'] = (m - r['precio']) / r['precio'] if m is not None else None
            f[f'edad_q_{s}s'] = edad
            f[f'stale_{s}s'] = (edad > STALE_S) if edad is not None else None
        out.append(f)
    return out


def main(dry=False):
    recs = [json.loads(l) for l in open(IN) if l.strip()]
    hechos = set()
    if os.path.exists(OUT):
        for l in open(OUT):
            try: d = json.loads(l); hechos.add((d['slug'], d['oid']))
            except Exception: pass
    nuevas = []
    for rec in recs:
        if all((rec['slug'], r['oid']) in hechos for r in rec['rellenos']): continue
        tok = token_de(rec['slug'], rec['lado'], None)
        xs = serie_mid(tok, rec['slug']) if tok else []
        filas = calcular(rec, xs)
        for f in filas: f['token'] = tok; f['reconstruido_utc'] = dt.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        nuevas += [f for f in filas if (f['slug'], f['oid']) not in hechos]
    for f in nuevas: print(json.dumps(f))
    if not dry and nuevas:
        with open(OUT, 'a') as fh:
            for f in nuevas: fh.write(json.dumps(f) + '\n')
    return nuevas


if __name__ == '__main__':
    main(dry='--dry' in sys.argv)
