#!/usr/bin/env python3
"""Markouts (+5/+30/+120 s, como Exp.finalizar de experimento_maker_h47.py) de los rellenos de los puja_fin RECONSTRUIDOS,
con el mid (bid+ask)/2 del token reconstruido desde las filas `q` de VOL/m5_registro (top de libro por WS, hora de RECEPCION c5).
SOLO LEE: puja_fin_reconstruido.jsonl y m5_registro_D.csv.gz. Escribe en un fichero SEPARADO (nunca el ledger), idempotente por (slug,oid).
Regla de finalizar: t0+s > fin del mercado (start+300) o relleno tardio -> missing (None), nunca 0. mid_en = ultimo mid con recepcion <= t.
Ademas guarda edad_q_s (t - recepcion del q usado) y flag stale si > STALE_S: la fuente es por cambio de top, no por reloj.
27-Oct: (a) UNA pasada por dia (series_lote: todos los mercados de un dia en un solo zcat|grep -F -f); (b) FALLBACK a libro5_ms
(feed crudo B/d/T/G del libro, recepcion c[6]) SOLO donde la serie q falte o este stale (> STALE_S): campo fuente_<s>s.
Mercados cuyo fichero m5_registro del dia aun no esta archivado (04:03 del dia siguiente) se SALTAN (no se escriben): los coge la pasada siguiente.
Uso: markouts_desde_registro.py [--dry]   (env MDR_DL, MDR_VOL, MDR_OUT, MDR_L5)"""
import os, sys, json, gzip, subprocess, datetime as dt, bisect, glob, tempfile, fcntl

DL = os.environ.get('MDR_DL', '/root/polymarket-research-datalogs')
VOL = os.environ.get('MDR_VOL', '/mnt/HC_Volume_106538179/m5_registro')
L5 = os.environ.get('MDR_L5', '/mnt/HC_Volume_106538179/libro5_ms')
IN = os.path.join(DL, 'puja_fin_reconstruido.jsonl')
OUT = os.environ.get('MDR_OUT', os.path.join(DL, 'puja_fin_markouts_m5registro.jsonl'))
MARK_S = (5, 30, 120)
STALE_S = 30.0
HUECO_S = 60.0       # tras el fallback, si el ultimo dato conocido tiene mas edad que esto: hueco de datos -> markout missing (None), nunca el valor viejo


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


def necesita_fb(rec, xs):
    """True si algun markout aplicable de algun relleno tiene q ausente o stale (> STALE_S)."""
    fin = float(rec['slug'].rsplit('-', 1)[1]) + 300.0; ts = [x[0] for x in xs]
    for r in rec['rellenos']:
        if r.get('tardio'): continue
        for s_ in MARK_S:
            if r['t_deteccion'] + s_ > fin: continue
            m, edad = mid_en(xs, ts, r['t_deteccion'] + s_) if xs else (None, None)
            if m is None or edad > STALE_S: return True
    return False


def calcular(rec, xs, xs5=None):
    """rec = un puja_fin reconstruido; xs = serie [(recepcion_s, mid)] del token (m5_registro.q); xs5 = serie libro5_ms (fallback,
    solo se usa donde q falta o esta stale y libro5 es mas fresco). Devuelve lista de filas por relleno."""
    fin = float(rec['slug'].rsplit('-', 1)[1]) + 300.0
    ts = [x[0] for x in xs]; ts5 = [x[0] for x in xs5] if xs5 else []; out = []
    for r in rec['rellenos']:
        t0 = r['t_deteccion']; f = {'slug': rec['slug'], 'oid': r['oid'], 'lado': rec['lado'], 'acc': r['acc'], 'precio': r['precio'],
                                    't_deteccion': t0, 'fuente_mid': 'm5_registro.q', 'n_q_serie': len(xs), 'n_libro5_serie': len(xs5) if xs5 else 0}
        for s in MARK_S:
            aplica = t0 + s <= fin and not r.get('tardio')
            m, edad = (mid_en(xs, ts, t0 + s) if (aplica and xs) else (None, None)); fuente = 'm5_registro.q' if m is not None else None
            if aplica and xs5 and (m is None or edad > STALE_S):
                m5, e5 = mid_en(xs5, ts5, t0 + s)
                if m5 is not None and (m is None or e5 < edad): m, edad, fuente = m5, e5, 'libro5_ms'
            hueco = m is not None and edad > HUECO_S
            f[f'mid_ultimo_conocido_{s}s'] = m if hueco else None
            if hueco: m, fuente = None, 'hueco_sin_dato'
            f[f'hueco_{s}s'] = bool(hueco)
            f[f'mid_{s}s'] = m
            f[f'markout_{s}s'] = (m - r['precio']) / r['precio'] if m is not None else None
            f[f'edad_q_{s}s'] = edad
            f[f'stale_{s}s'] = (edad > STALE_S) if edad is not None else None
            f[f'fuente_{s}s'] = fuente
        out.append(f)
    return out


def _grep_f(path, tokens, extra=()):
    """Lineas de `path` (gz) que contienen alguno de los tokens (grep -F -f, una sola pasada). `extra` = patrones literales adicionales."""
    if not os.path.exists(path) or not (tokens or extra): return []
    with tempfile.NamedTemporaryFile('w', suffix='.pats', delete=False) as pf:
        pf.write('\n'.join(list(tokens) + list(extra)) + '\n'); pn = pf.name
    try:
        p = subprocess.run(f"zcat '{path}' | grep -a -F -f '{pn}'", shell=True, capture_output=True, text=True)
        return p.stdout.splitlines()
    finally: os.unlink(pn)


def _info(rec):
    ini = int(rec['slug'].rsplit('-', 1)[1])
    return rec['slug'].split('-')[0].upper(), dt.datetime.utcfromtimestamp(ini + 300).strftime('%Y-%m-%d %H:%M:%S+00:00'), ini


def tokens_lote(recs, dias_ok):
    """slug -> token, buscando filas k (una sola lectura por fichero-dia)."""
    want = {}                                            # (COIN, fin_str, lado) -> slug
    for rec in recs:
        c, fin, ini = _info(rec); want[(c, fin, rec['lado'])] = rec['slug']
    dset = sorted({d for rec in recs for d in dias(_info(rec)[2], _info(rec)[2] + 300)} & dias_ok); out = {}
    for d in dset:
        for l in _lineas(os.path.join(VOL, f'm5_registro_{d}.csv.gz'), "-a -e '^k,'"):
            c = l.split(',')
            if len(c) >= 8 and (c[3], c[6], c[7]) in want: out[want[(c[3], c[6], c[7])]] = c[2]
    return out


def series_lote(recs, slug_tok, dias_ok):
    """slug -> serie q [(recepcion_s, mid)]; UN grep -F -f por fichero-dia para todos los tokens."""
    tok_slugs = {}
    for rec in recs:
        if rec['slug'] in slug_tok: tok_slugs.setdefault(slug_tok[rec['slug']], []).append(rec['slug'])
    por_dia = {}
    for rec in recs:
        if rec['slug'] not in slug_tok: continue
        ini = _info(rec)[2]
        for d in dias(ini, ini + 500): por_dia.setdefault(d, set()).add(slug_tok[rec['slug']])
    xs = {t: [] for t in tok_slugs}
    for d, toks in sorted(por_dia.items()):
        if d not in dias_ok: continue
        for l in _grep_f(os.path.join(VOL, f'm5_registro_{d}.csv.gz'), toks):
            c = l.split(',')
            if c[0] != 'q' or len(c) < 8 or c[2] not in xs: continue
            try: b, a, rc = float(c[3]), float(c[4]), float(c[7]) / 1000.0
            except ValueError: continue
            if b > 0 and a > 0 and b <= a: xs[c[2]].append((rc, (b + a) / 2))
    for v in xs.values(): v.sort()
    return {s: xs[t] for t, ss in tok_slugs.items() for s in ss}


def _mejor(lado_dict, f):
    return f(p for p, s in lado_dict.items() if s > 0) if any(s > 0 for s in lado_dict.values()) else None


def _libro5_parse(lineas, toks):
    """Reconstruye el mid por token desde filas B/d/G de libro5 (orden de fichero = orden de seq dentro de un pid).
    G de token o '*' => sin continuidad hasta el siguiente B. Emite UN mid por instante de recepcion (el estado final del lote)."""
    toks = list(toks); book = {t: None for t in toks}; out = {t: [] for t in toks}; ult = {}      # ult[t] = (recepcion, mid) pendiente

    def _mid(t):
        bk = book[t]
        if not bk: return None
        bb = max((p for p, s in bk[0].items() if s > 0), default=None); aa = min((p for p, s in bk[1].items() if s > 0), default=None)
        return (bb + aa) / 2 if bb and aa and bb <= aa else None

    def _vol(t):
        u = ult.pop(t, None)
        if u and u[1] is not None: out[t].append(u)

    def _lado(sx):
        return {float(x.split(':')[0]): float(x.split(':')[1]) for x in sx.split(';') if ':' in x}

    for l in lineas:
        c = l.split(',')
        if len(c) < 8: continue
        tp, tk = c[0], c[2]
        if tp == 'G':
            for t in (toks if tk == '*' else ([tk] if tk in out else [])): _vol(t); book[t] = None
            continue
        if tk not in out or tp not in ('B', 'd'): continue
        try:
            rc = float(c[6]) / 1000.0
            if tp == 'B': book[tk] = (_lado(c[3]), _lado(c[4]))
            elif book[tk]: book[tk][0 if c[3] == 'B' else 1][float(c[4])] = float(c[5])
            else: continue
        except ValueError:
            book[tk] = None; continue
        if tk in ult and ult[tk][0] != rc: _vol(tk)
        ult[tk] = (rc, _mid(tk))
    for t in toks: _vol(t)
    for v in out.values(): v.sort()
    return out


def series_libro5(recs, slug_tok):
    """slug -> serie libro5 [(recepcion_s, mid)] para los mercados indicados. Un grep -F -f por fichero libro5 del dia (varios pid)."""
    tok_slugs = {}; por_dia = {}
    for rec in recs:
        t = slug_tok.get(rec['slug'])
        if not t: continue
        tok_slugs.setdefault(t, []).append(rec['slug']); ini = _info(rec)[2]
        for d in dias(ini, ini + 500, atras=300): por_dia.setdefault(d, set()).add(t)
    res = {t: [] for t in tok_slugs}
    for d, toks in sorted(por_dia.items()):
        for f in sorted(glob.glob(os.path.join(L5, f'libro5_ms_{d}_*.csv.gz'))):
            # cada fichero (pid) arranca sin estado: el servidor manda B al suscribir; sin B previo no hay mid
            for t, v in _libro5_parse(_grep_f(f, toks, extra=(',*,',)), list(toks)).items(): res[t] += v
    for v in res.values(): v.sort()
    return {s: res[t] for t, ss in tok_slugs.items() for s in ss}


def _dias_ok(recs):
    """Ficheros-dia m5_registro existentes."""
    out = set()
    for rec in recs:
        ini = _info(rec)[2]
        for d in dias(ini, ini + 500):
            if os.path.exists(os.path.join(VOL, f'm5_registro_{d}.csv.gz')): out.add(d)
    return out


def completo(rec, dias_ok):
    """El dia del fin del markout (ini+300+120+margen) y el del mercado deben estar archivados."""
    ini = _info(rec)[2]
    return all(d in dias_ok for d in dias(ini, ini + 500, atras=0))


def cargar_hechos(con_filas=False):
    hechos, malas, filas = set(), 0, {}
    if os.path.exists(OUT):
        for l in open(OUT):
            try: d = json.loads(l); hechos.add((d['slug'], d['oid'])); filas[(d['slug'], d['oid'])] = d
            except Exception: malas += 1 if l.strip() else 0
    return (hechos, malas, filas) if con_filas else (hechos, malas)


def _legado_stale(d):
    """Fila escrita ANTES de fallback+hueco (sin campo hueco_*) con algun markout stale: se recalcula (y queda con hueco_*)."""
    return 'hueco_5s' not in d and any(d.get(f'stale_{s}s') for s in MARK_S)


def escribir(filas, reemplazar=()):
    """Anade bajo flock, idempotente por (slug,oid) releido dentro del lock; fsync. Devuelve (nuevas, duplicadas).
    `reemplazar` = claves (slug,oid) de filas LEGADAS (stale, sin fallback) que se sustituyen por la fila recalculada: reescritura
    atomica (tmp + os.replace) con copia .bak previa; el resto de lineas, intactas."""
    if not filas: return 0, 0
    with open(OUT + '.lock', 'w') as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        ya, _, ex = cargar_hechos(True); nuevas = []; rep = {}
        for f in filas:
            k = (f['slug'], f['oid'])
            if k in reemplazar and k in ya and _legado_stale(ex[k]): rep[k] = f
            elif k not in ya: nuevas.append(f); ya.add(k)
        if rep:
            import shutil; shutil.copy2(OUT, OUT + '.bak_prefallback')
            tmp = OUT + '.tmp'
            with open(tmp, 'w') as fh:
                for l in open(OUT):
                    try: d = json.loads(l)
                    except Exception: continue
                    k = (d['slug'], d['oid']); fh.write(json.dumps(rep.get(k, d)) + '\n')
                fh.flush(); os.fsync(fh.fileno())
            os.replace(tmp, OUT)
        if nuevas:
            with open(OUT, 'a') as fh:
                if fh.tell() and open(OUT, 'rb').read()[-1:] != b'\n': fh.write('\n')      # cola a medias
                for f in nuevas: fh.write(json.dumps(f) + '\n')
                fh.flush(); os.fsync(fh.fileno())
    return len(nuevas) + len(rep), len(filas) - len(nuevas) - len(rep)


def procesar(recs, dry=False, fallback=True):
    """UNA pasada: recs sin markouts hechos -> series por dia -> (fallback libro5 donde falte) -> filas. Devuelve (nuevas, resumen)."""
    hechos, malas, ex = cargar_hechos(True)
    recalc = {k for k, d in ex.items() if fallback and _legado_stale(d)}          # filas pre-fallback con markouts stale
    pend = [r for r in recs if r['rellenos'] and (not all((r['slug'], x['oid']) in hechos for x in r['rellenos'])
                                                  or any((r['slug'], x['oid']) in recalc for x in r['rellenos']))]
    ok = _dias_ok(pend); lista = [r for r in pend if completo(r, ok)]
    resumen = dict(recs=len(recs), sin_rellenos=sum(1 for r in recs if not r['rellenos']), ya_hechos=len(recs) - len(pend) - sum(1 for r in recs if not r['rellenos']), a_recalcular_stale=len(recalc),
                   pendientes=len(pend), esperan_archivo_dia=len(pend) - len(lista), lineas_out_malas=malas, sin_token=[], fallback_libro5=[])
    slug_tok = tokens_lote(lista, ok); xs = series_lote(lista, slug_tok, ok)
    resumen['sin_token'] = [r['slug'] for r in lista if r['slug'] not in slug_tok]
    fb = [r for r in lista if r['slug'] in slug_tok and fallback and necesita_fb(r, xs.get(r['slug'], []))]
    xs5 = series_libro5(fb, slug_tok) if fb else {}
    resumen['fallback_libro5'] = [r['slug'] for r in fb]
    nuevas = []
    for rec in lista:
        tok = slug_tok.get(rec['slug'])
        for f in calcular(rec, xs.get(rec['slug'], []) if tok else [], xs5.get(rec['slug'])):
            f['token'] = tok; f['reconstruido_utc'] = dt.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'); nuevas.append(f)
    nuevas = [f for f in nuevas if (f['slug'], f['oid']) not in hechos or (f['slug'], f['oid']) in recalc]   # legada: se sustituye siempre (queda con fuente_*, no se reintenta)
    if not dry: resumen['escritas'], resumen['duplicadas_descartadas'] = escribir(nuevas, reemplazar=recalc)
    resumen['calculadas'] = len(nuevas)
    return nuevas, resumen


def por_slug(filas):
    """Una fila por slug en puja_fin_reconstruido (que es solo-anade): la que trae markouts (no 'missing') gana a una 'missing'; a igualdad, la ultima."""
    mejor = {}
    for i, r in enumerate(filas):
        k = (r.get('markouts') not in (None, 'missing'), i)
        if r['slug'] not in mejor or k > mejor[r['slug']][0]: mejor[r['slug']] = (k, r)
    return [v[1] for v in mejor.values()]


def main(dry=False):
    recs = por_slug([json.loads(l) for l in open(IN) if l.strip()])
    nuevas, res = procesar(recs, dry=dry)
    for f in nuevas: print(json.dumps(f))
    print(json.dumps(res), file=sys.stderr)
    return nuevas


if __name__ == '__main__':
    main(dry='--dry' in sys.argv)
