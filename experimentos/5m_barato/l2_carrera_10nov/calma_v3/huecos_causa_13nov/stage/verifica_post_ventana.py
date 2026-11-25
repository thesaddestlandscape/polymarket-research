#!/usr/bin/env python3
"""verifica_post_ventana.py -- comprobacion POST-VENTANA de la cache de tokens de libro_estado_ws (SOLO LECTURA, stdlib).
Tras la ventana de 429 de gamma (23:46-00:01 por defecto) compara contra la ventana de referencia (19:45-20:01):
  1. cache de disco (datalogs/libro_tokens_cache.json) contra gamma /markets/{id} para TODAS las claves cacheadas (<=6 req/s, tope y corte en 429);
  2. libro5_ms (todas las pids de los dias D y D+1): filas B/d/T por minuto, tokens distintos por minuto, minutos sin filas, mayor hueco (s),
     filas G por motivo (arranque/baja/caida/traspaso...);
  3. libro5_tx: filas por minuto, minutos vacios, mayor hueco (s);
  4. log de observadores: lineas 'conectado [grupo], N tokens' (n_tokens suscritos) y avisos (refresco fallido, parcial, cuarentena, ALARMA, sesion caida).
No escribe nada (salvo --json RUTA si se pide), no toca procesos, no usa .env. Lanzar con nice -n 19 ionice -c3 y ulimit -v 3000000.
Uso: verifica_post_ventana.py [--fecha YYYY-MM-DD] [--nueva 23:46-00:01] [--ref 19:45-20:01] [--sin-gamma] [--json RUTA]
  --fecha = dia UTC en que EMPIEZA la ventana nueva (por defecto: ayer si ahora<12:00Z, si no hoy); la ref es del mismo dia.
Veredicto en la ultima linea: VEREDICTO OK | VEREDICTO ALERTA (con motivos)."""
import argparse, collections, glob, gzip, json, os, re, statistics, subprocess, sys, time, urllib.error, urllib.request
from datetime import datetime, timedelta, timezone

LIBRO5_MS = '/mnt/HC_Volume_106538179/libro5_ms'
LIBRO5_TX = '/mnt/HC_Volume_106538179/libro5_tx'
CACHE = '/root/polymarket-research-datalogs/libro_tokens_cache.json'
LOGOBS = '/root/polymarket-research/logs/observadores_fase0.log'
GAMMA = 'https://gamma-api.polymarket.com/markets/'
MAX_GAMMA = 1500
RATE = 6.0


def ventana(dia, txt):
    a, b = txt.split('-')
    ha, ma = map(int, a.split(':')); hb, mb = map(int, b.split(':'))
    base = datetime.strptime(dia, '%Y-%m-%d').replace(tzinfo=timezone.utc)
    ini = base + timedelta(hours=ha, minutes=ma)
    fin = base + timedelta(hours=hb, minutes=mb)
    if fin <= ini: fin += timedelta(days=1)
    return int(ini.timestamp()) * 1000, int(fin.timestamp()) * 1000


def prefijos(wins):
    """Prefijos de 9 digitos de t_ms (tramos de 10 s) que cubren las ventanas -> regex para grep (el filtrado fino se hace despues)."""
    ps = set()
    for a, b in wins:
        for p in range(a // 10000, b // 10000 + 1): ps.add(str(p))
    return sorted(ps)


def filas_ms(archivo, wins):
    """Genera (tipo, t_ms, token, c1) de las filas cuyo t_ms cae en alguna ventana; zcat | grep en C (ficheros de GB), tolera gz truncado."""
    pat = '^[BdTG],(' + '|'.join(prefijos(wins)) + ')'
    z = subprocess.Popen(['nice', '-n', '19', 'ionice', '-c3', 'zcat', archivo], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    g = subprocess.Popen(['nice', '-n', '19', 'grep', '-aE', pat], stdin=z.stdout, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    z.stdout.close()
    for raw in g.stdout:
        p = raw.decode('utf-8', 'replace').rstrip('\n').split(',')
        if len(p) < 4 or not p[1].isdigit(): continue
        t = int(p[1])
        if any(a <= t < b for a, b in wins): yield p[0], t, p[2], p[3]
    g.wait(); z.wait()


def abrir_txt(f):
    return gzip.open(f, 'rt', errors='replace') if f.endswith('.gz') else open(f, errors='replace')


def filas_tx(archivo, wins):
    try:
        with abrir_txt(archivo) as fh:
            for l in fh:
                p = l.split(',', 2)
                if p and p[0].isdigit():
                    t = int(p[0])
                    if any(a <= t < b for a, b in wins): yield t
    except (EOFError, OSError):
        return


def resumen_serie(seg, a, b):
    """seg: Counter segundo->n. -> (filas por minuto {min:n}, minutos sin filas, mayor hueco en s)."""
    s0, s1 = a // 1000, b // 1000
    por_min = collections.Counter()
    for s, n in seg.items(): por_min[(s - s0) // 60] += n
    nmin = (s1 - s0 + 59) // 60
    vacios = [m for m in range(nmin) if por_min.get(m, 0) == 0]
    pres = sorted(seg)
    hueco = 0
    prev = s0
    for s in pres + [s1]:
        hueco = max(hueco, s - prev); prev = s
    return dict(por_min), vacios, hueco


def analizar_ms(dias, wins):
    """wins: {'ref': (a,b), 'nueva': (a,b)} -> metricas por ventana."""
    todas = [(a, b) for a, b in wins.values()]
    lo = min(a for a, _ in todas) / 1000
    arch = []
    for d in dias:
        for f in sorted(glob.glob(f'{LIBRO5_MS}/libro5_ms_{d}_*.csv.gz')):
            try:
                if os.path.getmtime(f) < lo: continue       # cerrado antes de la ventana
            except OSError: continue
            arch.append(f)
    res = {k: {'tipos': collections.Counter(), 'g': collections.Counter(), 'seg': collections.Counter(), 'tok_min': collections.defaultdict(set),
               'tokens': set(), 'ficheros': set()} for k in wins}
    for f in arch:
        for ty, t, tok, c1 in filas_ms(f, todas):
            for k, (a, b) in wins.items():
                if a <= t < b:
                    r = res[k]; r['tipos'][ty] += 1; r['ficheros'].add(os.path.basename(f))
                    if ty == 'G': r['g'][c1] += 1
                    else:
                        r['seg'][t // 1000] += 1; r['tok_min'][(t // 1000 - a // 1000) // 60].add(tok); r['tokens'].add(tok)
    out = {}
    for k, (a, b) in wins.items():
        r = res[k]; pm, vac, hueco = resumen_serie(r['seg'], a, b)
        tm = {m: len(v) for m, v in r['tok_min'].items()}
        nmin = (b - a) // 60000
        out[k] = {'ficheros': sorted(r['ficheros']), 'filas': dict(r['tipos']), 'G_por_motivo': dict(r['g']), 'tokens_distintos': len(r['tokens']),
                  'filas_por_min_mediana': statistics.median([pm.get(m, 0) for m in range(nmin)]) if nmin else 0,
                  'tokens_por_min_mediana': statistics.median([tm.get(m, 0) for m in range(nmin)]) if nmin else 0,
                  'tokens_por_min_min': min([tm.get(m, 0) for m in range(nmin)]) if nmin else 0,
                  'minutos_sin_filas': vac, 'mayor_hueco_s': hueco, 'tokens_por_min': [tm.get(m, 0) for m in range(nmin)]}
    return out


def analizar_tx(dias, wins):
    out = {}
    arch = []
    for d in dias: arch += sorted(glob.glob(f'{LIBRO5_TX}/libro5_tx_{d}_*'))
    for k, (a, b) in wins.items():
        seg = collections.Counter(); n = 0
        for f in arch:
            for t in filas_tx(f, [(a, b)]): seg[t // 1000] += 1; n += 1
        pm, vac, hueco = resumen_serie(seg, a, b)
        nmin = (b - a) // 60000
        out[k] = {'filas': n, 'filas_por_min_mediana': statistics.median([pm.get(m, 0) for m in range(nmin)]) if nmin else 0,
                  'minutos_sin_filas': vac, 'mayor_hueco_s': hueco}
    return out


def analizar_log(wins):
    """n_tokens suscritos (suma de la ultima linea 'conectado [g], N tokens' de cada grupo hasta el fin de la ventana) y avisos dentro de ella."""
    pat_t = re.compile(r'^\[(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)')
    pat_c = re.compile(r'conectado \[([^\]]+)\], (\d+) tokens')
    claves = ('refresco de universo fall', 'universo parcial', 'cuarentena', 'ALARMA', 'sesion caida', 'sesión caída', 'cache de tokens')
    ult = {k: {} for k in wins}; av = {k: collections.Counter() for k in wins}; muestra = {k: [] for k in wins}
    try:
        fh = open(LOGOBS, errors='replace')
    except OSError:
        return {k: {'error': 'sin log'} for k in wins}
    with fh:
        for l in fh:
            m = pat_t.match(l)
            if not m: continue
            t = int(datetime.strptime(m.group(1), '%Y-%m-%dT%H:%M:%S').replace(tzinfo=timezone.utc).timestamp()) * 1000
            for k, (a, b) in wins.items():
                if t < b:
                    c = pat_c.search(l)
                    if c: ult[k][c.group(1)] = int(c.group(2))
                if a <= t < b:
                    for cl in claves:
                        if cl in l:
                            av[k][cl] += 1
                            if len(muestra[k]) < 6: muestra[k].append(l.strip()[:200])
    return {k: {'n_tokens_suscritos_por_ultimo_conectado': sum(ult[k].values()), 'grupos': dict(sorted(ult[k].items())), 'avisos': dict(av[k]), 'muestra': muestra[k]} for k in wins}


def gamma_vs_cache(sin_gamma, cache=CACHE):
    try:
        j = json.load(open(cache))
        merc = j['mercados']
    except Exception as e:
        return {'error': f'cache ilegible: {type(e).__name__}: {e}'}
    ahora = time.time()
    claves = sorted(merc)
    out = {'n_cache': len(claves), 'sc_en_cache': sum(1 for v in merc.values() if v.get('sc')), 'contrastados': sum(1 for v in merc.values() if v.get('ctr')),
           'verificados': 0, 'coinciden': 0, 'discrepancias': [], 'sin_dato': [], 'errores': 0, 'cortado_por': None}
    if sin_gamma:
        out['cortado_por'] = '--sin-gamma'
        return out
    t0 = time.time(); seguidos = 0
    for i, mid in enumerate(claves):
        if i >= MAX_GAMMA: out['cortado_por'] = f'tope {MAX_GAMMA}'; break
        espera = t0 + i / RATE - time.time()
        if espera > 0: time.sleep(espera)
        try:
            r = urllib.request.urlopen(urllib.request.Request(GAMMA + mid, headers={'User-Agent': 'verifica_post_ventana'}), timeout=8)
            g = json.loads(r.read())
            seguidos = 0
        except urllib.error.HTTPError as e:
            if e.code == 429:
                out['cortado_por'] = f'429 de gamma tras {out["verificados"]} verificados'; break
            out['errores'] += 1; seguidos += 1
            if e.code == 404: out['sin_dato'].append(mid)
            if seguidos >= 20: out['cortado_por'] = '20 errores seguidos'; break
            continue
        except Exception:
            out['errores'] += 1; seguidos += 1
            if seguidos >= 20: out['cortado_por'] = '20 errores seguidos'; break
            continue
        try:
            tk = g['clobTokenIds']; oc = g['outcomes']
            tk = json.loads(tk) if isinstance(tk, str) else tk
            oc = json.loads(oc) if isinstance(oc, str) else oc
            o = [str(x).strip().lower() for x in oc]
            if o[0] in ('yes', 'up') and o[1] in ('no', 'down'): par = (str(tk[0]), str(tk[1]))
            elif o[0] in ('no', 'down') and o[1] in ('yes', 'up'): par = (str(tk[1]), str(tk[0]))
            else: raise ValueError('outcomes')
        except Exception:
            out['sin_dato'].append(mid); continue
        out['verificados'] += 1
        v = merc[mid]
        if par == (str(v.get('yes')), str(v.get('no'))): out['coinciden'] += 1
        else: out['discrepancias'].append({'mid': mid, 'cache': [v.get('yes'), v.get('no')], 'gamma': list(par), 'sc': bool(v.get('sc')), 'activo_marco': f"{v.get('activo')}#{v.get('marco')}"})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fecha'); ap.add_argument('--nueva', default='23:46-00:01'); ap.add_argument('--ref', default='19:45-20:01')
    ap.add_argument('--sin-gamma', action='store_true'); ap.add_argument('--json'); ap.add_argument('--cache', default=CACHE)
    a = ap.parse_args()
    ahora = datetime.now(timezone.utc)
    dia = a.fecha or (ahora - timedelta(days=1 if ahora.hour < 12 else 0)).strftime('%Y-%m-%d')
    wins = {'ref': ventana(dia, a.ref), 'nueva': ventana(dia, a.nueva)}
    dias = [dia, (datetime.strptime(dia, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')]
    rep = {'fecha': dia, 'ahora_utc': ahora.isoformat(timespec='seconds'), 'ventanas': {k: [datetime.fromtimestamp(x / 1000, timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ') for x in v] for k, v in wins.items()}}
    print(f'[{rep["ahora_utc"]}] verifica_post_ventana fecha={dia} ref={a.ref} nueva={a.nueva}', flush=True)
    rep['cache_vs_gamma'] = gamma_vs_cache(a.sin_gamma, a.cache); print('cache_vs_gamma:', json.dumps({k: (v if k not in ('discrepancias', 'sin_dato') else v[:10]) for k, v in rep['cache_vs_gamma'].items()}), flush=True)
    rep['libro5_ms'] = analizar_ms(dias, wins)
    for k in ('ref', 'nueva'): print(f'libro5_ms[{k}]:', json.dumps({x: y for x, y in rep['libro5_ms'][k].items() if x != 'tokens_por_min'}), flush=True)
    rep['libro5_tx'] = analizar_tx(dias, wins)
    for k in ('ref', 'nueva'): print(f'libro5_tx[{k}]:', json.dumps(rep['libro5_tx'][k]), flush=True)
    rep['log_observadores'] = analizar_log(wins)
    for k in ('ref', 'nueva'): print(f'log[{k}]:', json.dumps(rep['log_observadores'][k]), flush=True)
    motivos = []
    c = rep['cache_vs_gamma']
    if c.get('error'): motivos.append(c['error'])
    elif c['discrepancias']: motivos.append(f"{len(c['discrepancias'])} discrepancias cache!=gamma")
    elif c['verificados'] == 0 and not a.sin_gamma: motivos.append('0 claves verificadas contra gamma (' + str(c.get('cortado_por')) + ')')
    r, n = rep['libro5_ms']['ref'], rep['libro5_ms']['nueva']
    if not r['filas']: motivos.append('sin filas de libro5_ms en la ventana de referencia (comparacion imposible)')
    else:
        if not n['filas']: motivos.append('SIN filas de libro5_ms en la ventana nueva')
        else:
            if n['tokens_por_min_mediana'] < 0.8 * r['tokens_por_min_mediana']: motivos.append(f"tokens/min mediana {n['tokens_por_min_mediana']} < 80% de la ref {r['tokens_por_min_mediana']}")
            if len(n['minutos_sin_filas']) > len(r['minutos_sin_filas']): motivos.append(f"minutos sin filas {n['minutos_sin_filas']} (ref {r['minutos_sin_filas']})")
            if n['mayor_hueco_s'] > max(30, 2 * r['mayor_hueco_s']): motivos.append(f"mayor hueco {n['mayor_hueco_s']} s (ref {r['mayor_hueco_s']} s)")
            if n['G_por_motivo'].get('baja', 0) > 2 * r['G_por_motivo'].get('baja', 0) + 10: motivos.append(f"filas G baja {n['G_por_motivo'].get('baja', 0)} (ref {r['G_por_motivo'].get('baja', 0)})")
    tr, tn = rep['libro5_tx']['ref'], rep['libro5_tx']['nueva']
    if tn['mayor_hueco_s'] > max(60, 2 * tr['mayor_hueco_s']): motivos.append(f"libro5_tx mayor hueco {tn['mayor_hueco_s']} s (ref {tr['mayor_hueco_s']} s)")
    rep['motivos'] = motivos
    if a.json:
        with open(a.json, 'w') as f: json.dump(rep, f)
    print('VEREDICTO ' + ('OK' if not motivos else 'ALERTA: ' + '; '.join(motivos)))
    return 1 if motivos else 0


if __name__ == '__main__':
    sys.exit(main())
