"""tokmap.py - mapa token -> (coin, marco, mid, fin_epoch, lado). Fuentes: (1) filas k de los maker_ms CRUDOS (datalogs, ~5 d) con cache por
fichero (idempotente: clave nombre+tamano+mtime; ficheros escritos hace <20 min se saltan); (2) si no queda crudo para el dia, el
m15_registro .csv.gz del volumen (solo .gz completo; el .tmp truncado se ignora); (3) 4h y diario via gamma (slug), cacheado por dia.
Un crudo con gzip corrupto aporta las k previas al corte y queda anotado en el indice (truncado=true): NUNCA se declara completo."""
import json, subprocess, datetime as dt, time, glob, os, re
from pathlib import Path
import infra_lib as L
TM = lambda: L.INFRA / 'tokmap'
def _k_de(fichero):
    p = subprocess.run(f"gzip -dc '{fichero}' 2>/dev/null | grep -a '^k,'", shell=True, capture_output=True, text=True)
    return p.stdout.splitlines()
def _parsea(lineas):
    out = {}
    for ln in lineas:
        c = ln.split(',')
        if len(c) < 8 or c[0] != 'k': continue
        try: fin = int(dt.datetime.fromisoformat(c[6]).timestamp())
        except Exception: continue
        out[c[2]] = [c[3], c[4], c[5], fin, c[7]]
    return out
def escanea(fichero, fresco_min=20):
    """Cache de k de UN crudo. Devuelve (dict, info)."""
    fichero = Path(fichero); st = fichero.stat(); d = TM(); d.mkdir(parents=True, exist_ok=True)
    idx = L.read_json(d / 'indice.json', {}); key = fichero.name; meta = idx.get(key)
    if meta and meta['size'] == st.st_size and int(meta['mtime']) == int(st.st_mtime):
        return json.loads((d / (key + '.k.json')).read_text()), meta
    if time.time() - st.st_mtime < fresco_min * 60:
        return {}, dict(skipped='en_escritura')
    # integridad: 'unexpected end of file' = cola cortada por un reinicio (NORMAL en los maker_ms, solo se pierden los ultimos segundos);
    # cualquier otro error (invalid ... / crc) = corrupcion A MEDIA CORRIENTE: ahi se pierden k posteriores -> truncado real.
    pt = subprocess.run(f"gzip -t '{fichero}'", shell=True, capture_output=True, text=True); err = pt.stderr.lower()
    ok = pt.returncode == 0 or ('unexpected end of file' in err and 'invalid' not in err and 'crc' not in err and 'not in gzip' not in err)
    tm = _parsea(_k_de(fichero))
    (d / (key + '.k.json.tmp')).write_text(json.dumps(tm)); os.replace(d / (key + '.k.json.tmp'), d / (key + '.k.json'))
    meta = dict(size=st.st_size, mtime=int(st.st_mtime), n_tokens=len(tm), gzip_ok=ok, cola_cortada=(pt.returncode != 0 and ok), truncado=(not ok), gzip_err=pt.stderr.strip()[:120], escaneado=L.now())
    idx = L.read_json(d / 'indice.json', {}); idx[key] = meta; L.atomic_json(d / 'indice.json', idx)
    return tm, meta
def tokens_dia(dia, marcos=('5min', '15min', '60min')):
    """Union de k de los crudos D-1, D, D+1. Devuelve (tokens{marco->{tok:info}}, info)."""
    d0 = dt.date.fromisoformat(dia); res = {m: {} for m in marcos}; info = dict(ficheros=0, truncados=[], en_escritura=[], fuente='crudo')
    for k in (-1, 0, 1):
        dd = (d0 + dt.timedelta(days=k)).isoformat()
        for f in sorted(glob.glob(str(L.ROOT / f'maker_ms_{dd}_*.csv.gz'))):
            tm, meta = escanea(f)
            if meta.get('skipped'): info['en_escritura'].append(Path(f).name); continue
            info['ficheros'] += 1
            if meta.get('truncado'): info['truncados'].append(Path(f).name)
            for t, v in tm.items():
                if v[1] in res: res[v[1]][t] = v
    # registro del volumen (m15_registro guarda las k de TODOS los marcos): union siempre, solo .gz completos (el .tmp truncado se ignora)
    info['registro'] = []
    for k in (-1, 0, 1):
        dd = (d0 + dt.timedelta(days=k)).isoformat(); f = L.VOL / 'm15_registro' / f'm15_registro_{dd}.csv.gz'
        if f.exists():
            tm, meta = escanea(f, fresco_min=0); info['registro'].append(f.name); info['ficheros'] += 1
            if meta.get('truncado'): info['truncados'].append(f.name)
            for t, v in tm.items():
                if v[1] in res: res[v[1]][t] = v
    if info['ficheros'] == 0: info['fuente'] = 'ninguna'
    return res, info
# ---- 4h y diario via gamma (slugs) ----
G = 'https://gamma-api.polymarket.com/markets'
COIN4 = {'btc': 'BTC', 'eth': 'ETH', 'sol': 'SOL', 'xrp': 'XRP', 'doge': 'DOGE', 'bnb': 'BNB'}
NOM = {'bitcoin': 'BTC', 'ethereum': 'ETH', 'solana': 'SOL', 'xrp': 'XRP', 'dogecoin': 'DOGE', 'bnb': 'BNB'}
MES = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
def _parse_gamma(m, coin, marco, out):
    tk = json.loads(m['clobTokenIds']) if isinstance(m['clobTokenIds'], str) else m['clobTokenIds']
    oc = json.loads(m['outcomes']) if isinstance(m['outcomes'], str) else m['outcomes']
    fin = int(dt.datetime.fromisoformat(m['endDate'].replace('Z', '+00:00')).timestamp())
    up = [i for i, o in enumerate(oc) if str(o).lower() in ('up', 'yes')]; ui = up[0] if up else 0
    for i, t in enumerate(tk): out[t] = [coin, marco, str(m['id']), fin, 'YES' if i == ui else 'NO']
def _slug(S, slug):
    """gamma: mercado abierto (sin closed) y, si no sale, cerrado (closed=true: si no, gamma no devuelve los cerrados por slug)."""
    n = 0
    for par in ({}, {'closed': 'true'}):
        r = S.get(G, params=dict(slug=slug, **par), timeout=20); r.raise_for_status(); n += 1
        j = r.json()
        if isinstance(j, list) and j: return j, n
    return [], n
def gamma_dia(dia, session=None):
    """Tokens 4h/24h con trading en el dia. Cache datalogs/mapa_infra/tokmap/gamma_D.json. Lanza si hay errores de red (no cachea)."""
    f = TM() / f'gamma_{dia}.json'; c = L.read_json(f)
    if c and c.get('completo'): return c['tokens'], c
    import requests; S = session or requests.Session(); out = {}; n_req = 0; vacios = 0
    d0 = dt.datetime.fromisoformat(dia).replace(tzinfo=dt.timezone.utc); t0 = int(d0.timestamp())
    for c4, C in COIN4.items():
        for te in range(t0, t0 + 86400 + 8 * 3600 + 1, 14400):
            ok = False
            for ts in (te, te - 14400):
                j, n = _slug(S, f'{c4}-updown-4h-{ts}'); n_req += n
                if isinstance(j, list) and j and int(dt.datetime.fromisoformat(j[0]['endDate'].replace('Z', '+00:00')).timestamp()) == te:
                    _parse_gamma(j[0], C, '240min', out); ok = True; break
            vacios += (not ok)
    for k in (-1, 0, 1, 2):
        d = d0.date() + dt.timedelta(days=k)
        for n, C in NOM.items():
            j, nn = _slug(S, f'{n}-up-or-down-on-{MES[d.month - 1]}-{d.day}-{d.year}'); n_req += nn
            if isinstance(j, list) and j: _parse_gamma(j[0], C, '24h', out)
            else: vacios += 1
    meta = dict(completo=True, n_req=n_req, slugs_vacios=vacios, n_tokens=len(out), generado=L.now(), tokens=out)
    L.atomic_json(f, meta); return out, meta
