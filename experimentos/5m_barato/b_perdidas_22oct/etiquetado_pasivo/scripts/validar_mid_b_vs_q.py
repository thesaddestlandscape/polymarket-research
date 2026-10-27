#!/usr/bin/env python3
"""Validacion (27-Oct): el mid que mide B (mid0/mid_5s/mid_30s/mid_120s de los puja_fin ORIGINALES con relleno, n~195) y sus bid/ask de
repega/cancela_banda frente al q de m5_registro del mismo token. Solo lee; una carga por fichero-dia (markouts_desde_registro.series_lote).
Salida: JSON a stdout (y a --out). No escribe en ledger ni en puja_fin_markouts. Uso: validar_mid_b_vs_q.py [--out f.json]"""
import os, sys, json, bisect, statistics as st
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import markouts_desde_registro as M
import reconstruir_puja_fin as R


def pct(xs, q):
    xs = sorted(xs); return xs[min(len(xs) - 1, int(q * len(xs)))] if xs else None


def main():
    filas, _ = R.leer_jsonl(R.LEDGER)
    pf = [d for d in filas if d.get('tipo') == 'puja_fin' and d.get('rellenos')]
    rec_slugs = {d['slug'] for d in R.leer_jsonl(R.OUT)[0]}
    recs = [dict(slug=d['slug'], lado=d['lado'], rellenos=d['rellenos']) for d in pf]
    # repega/cancela_banda de los mercados reconstruidos: lado desde puja_post
    lado = {d['slug']: d['lado'] for d in filas if d.get('tipo') == 'puja_post'}
    rep = [d for d in filas if d.get('tipo') in ('repega', 'cancela_banda') and d.get('slug') in rec_slugs and d.get('bid') is not None]
    for s in rec_slugs: recs.append(dict(slug=s, lado=lado[s], rellenos=[{'oid': 'x', 't_deteccion': 0}]))
    ok = M._dias_ok(recs); lista = [r for r in recs if M.completo(r, ok)]
    tok = M.tokens_lote(lista, ok); xs = M.series_lote(lista, tok, ok)
    out = dict(n_puja_fin_con_relleno=len(pf), n_mercados_con_serie=sum(1 for s, v in xs.items() if v), sin_token=[r['slug'] for r in lista if r['slug'] not in tok], mids={})
    # (i) mids de puja_fin originales
    for k, key in (('0', 'mid0'), ('5', 'mid_5s'), ('30', 'mid_30s'), ('120', 'mid_120s')):
        dif, exact, n_stale, sin = [], 0, 0, 0
        for d in pf:
            serie = xs.get(d['slug'])
            if not serie: continue
            ts = [x[0] for x in serie]
            for r in d['rellenos']:
                b = r.get(key)
                if b is None: continue
                m, edad = M.mid_en(serie, ts, r['t_deteccion'] + int(k))
                if m is None: sin += 1; continue
                dif.append(abs(m - b)); exact += abs(m - b) < 1e-9; n_stale += edad > M.STALE_S
        n = len(dif)
        out['mids'][key] = dict(n=n, sin_q=sin, exactos=exact, frac_exacto=round(exact / n, 3) if n else None, dentro_0p5c=sum(x <= 0.005 + 1e-9 for x in dif),
                                mediana_abs=pct(dif, .5), p90_abs=pct(dif, .9), max_abs=max(dif) if dif else None, q_stale=n_stale)
    # (ii) bid/ask de repega/cancela_banda vs top del q: ¿coincide el par y con que desfase?
    import datetime as dt
    cmp_, lag = [], []
    # necesitamos bid y ask del q, no el mid: releer series con bid/ask no esta en series_lote -> aproximamos con el mid (b+a)/2 del par de B
    for d in rep:
        serie = xs.get(d['slug']); t = dt.datetime.fromisoformat(d['ts']).timestamp()
        if not serie: continue
        mb = (d['bid'] + d['ask']) / 2; ts = [x[0] for x in serie]
        m, edad = M.mid_en(serie, ts, t)
        if m is None: continue
        cmp_.append(abs(m - mb))
        # primer instante (|dt|<=5 s) en que el q muestra el mid de B
        c = [x[0] - t for x in serie if abs(x[0] - t) <= 5 and abs(x[1] - mb) < 1e-9]
        if c: lag.append(min(c, key=abs))
    out['repega_cancela_banda'] = dict(n=len(cmp_), mid_igual_en_ts=sum(x < 1e-9 for x in cmp_), mediana_abs=pct(cmp_, .5), p90_abs=pct(cmp_, .9),
                                       n_con_mismo_mid_en_ventana_5s=len(lag), lag_q_menos_B_ms_p10_p50_p90=[round(1000 * pct(lag, q), 0) for q in (.1, .5, .9)] if lag else None)
    print(json.dumps(out, indent=1))
    if '--out' in sys.argv: json.dump(out, open(sys.argv[sys.argv.index('--out') + 1], 'w'), indent=1)


if __name__ == '__main__':
    main()
