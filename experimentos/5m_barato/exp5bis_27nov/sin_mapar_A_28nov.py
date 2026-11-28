#!/usr/bin/env python3
"""sin_mapar_A_28nov.py DIA1 [DIA2 ...] [--coins eth,sol,xrp,btc]   (28-Nov, paso 3 item 5, ANEXO2 §2 / ANEXO3 §5). Solo LEE: gamma publico (GET /markets?slug=..., closed=true) y el mapa token->moneda del dia (cadena_v2v3). 0 ordenes, 0 firma, sin credenciales.
Universo = rejilla de slugs `{coin}-updown-5m-{epoch}` (288/dia) y `{coin}-updown-15m-{epoch}` (96/dia) del dia UTC. Un slug cuenta como MAPEADO solo si (1) gamma lo devuelve con `endDate` EXACTO = epoch + 300|900 s (trampa 17-Nov: slugs viejos devuelven otro mercado) y 2 clobTokenIds,
y (2) al menos uno de sus tokens esta en el mapa del pipeline (sa_ms + extra). gamma vacio / fallo / 429 / endDate distinto => SIN MAPAR (nunca se omite). Metrica A = sin_mapar / esperados (<= 0,10 por moneda-dia, 5m+15m juntos; se publican tambien 5m y 15m por separado);
dia-moneda sin A<=0,10 => SIN_MAPA (nunca COMPLETE). Metrica B (join libro5_tx<->cadena >= 0,90) la da cadena_v2v3.estado_dia_moneda; aqui se combina: estado_final = SIN_MAPA si A>0,10, si no el de B.
Cache gamma por slug en datalogs/exp5bis_27nov/paso3/gamma_slug_cache.json (solo registros validados; escritura atomica) y mapa token->(moneda, marco, slug, version) con sha16 en sin_mapar_A_DIA.json. Version del mercado = la de gamma por mercado (no por moneda)."""
import sys, os, json, time, hashlib, datetime as dt
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
OUT3 = '/root/polymarket-research-datalogs/exp5bis_27nov/paso3/'
CACHE = OUT3 + 'gamma_slug_cache.json'
GAMMA = 'https://gamma-api.polymarket.com/markets'
MARCOS = {'5m': 300, '15m': 900}
SIN_MAPAR_MAX = 0.10
LOTE = 40


def epoch_dia(dia):
    return int(dt.datetime.fromisoformat(dia).replace(tzinfo=dt.timezone.utc).timestamp())


def rejilla(dia, coin, marco):
    """-> [(slug, epoch_inicio, endDate_esperado_epoch)] de TODO el dia (288 para 5m, 96 para 15m)."""
    d = MARCOS[marco]; e0 = epoch_dia(dia)
    return [(f'{coin}-updown-{marco}-{e}', e, e + d) for e in range(e0, e0 + 86400, d)]


def _end_epoch(s):
    try:
        return int(dt.datetime.fromisoformat(str(s).replace('Z', '+00:00')).timestamp())
    except (ValueError, TypeError):
        return None


def valida_registro(m, end_esp):
    """Registro gamma valido o None: endDate exacto, 2 clobTokenIds, version v1|v2. Devuelve dict(tokens, version, end)."""
    try:
        toks = m.get('clobTokenIds'); toks = json.loads(toks) if isinstance(toks, str) else toks
        v = m.get('version')
        if len(toks) != 2 or _end_epoch(m.get('endDate')) != end_esp or v not in ('v1', 'v2'): return None
        return dict(tokens=[str(t) for t in toks], version=v, end=end_esp)
    except (TypeError, ValueError, AttributeError):
        return None


def gamma_http(slugs, timeout=10):
    import requests
    r = requests.get(GAMMA, params=[('slug', s) for s in slugs] + [('closed', 'true'), ('limit', str(len(slugs) + 5))], timeout=timeout)
    if r.status_code != 200: raise RuntimeError(f'gamma {r.status_code}')
    return r.json()


def resuelve(items, cache, get=gamma_http, espera=0.25):
    """items [(slug, end_esperado)] -> (dict slug -> registro valido | None, fallos_http). Los ya validados en cache no se piden; lo no resuelto NO se cachea (puede aparecer luego)."""
    fallos = 0; pend = [(s, e) for s, e in items if s not in cache]
    for i in range(0, len(pend), LOTE):
        lote = pend[i:i + LOTE]; end = dict(lote)
        try:
            for m in get([s for s, _ in lote]):
                r = valida_registro(m, end.get(m.get('slug')))
                if r is not None and m.get('slug') in end: cache[m['slug']] = r
        except Exception:
            fallos += len(lote)                                                       # fallo de red/429: esos slugs cuentan SIN MAPAR (no se omiten)
        time.sleep(espera)
    return {s: cache.get(s) for s, _ in items}, fallos


def metrica_A(dia, coin, mapa_tokens, cache, get=gamma_http, espera=0.25):
    """mapa_tokens: set de token_id del pipeline para la moneda. -> dict por marco y combinado + tokens mapeados {token: [coin, marco, slug, version]}."""
    res = {}; tok_mapa = {}; esp = map_ = 0
    for marco in MARCOS:
        g = rejilla(dia, coin, marco); rs, fallos = resuelve([(s, e) for s, _, e in g], cache, get, espera)
        n = len(g); ok_gamma = sum(1 for s, _, _ in g if rs.get(s)); en_mapa = 0
        for s, _, _ in g:
            r = rs.get(s)
            if r and any(t in mapa_tokens for t in r['tokens']):
                en_mapa += 1
                for t in r['tokens']: tok_mapa[t] = [coin, marco, s, r['version']]
        res[marco] = dict(esperados=n, gamma_valido=ok_gamma, en_mapa=en_mapa, sin_mapar=n - en_mapa, frac_sin_mapar=round((n - en_mapa) / n, 4), fallos_http=fallos, sin_gamma=n - ok_gamma)
        esp += n; map_ += en_mapa
    res['combinado'] = dict(esperados=esp, en_mapa=map_, sin_mapar=esp - map_, frac_sin_mapar=round((esp - map_) / esp, 4))
    res['A_ok'] = res['combinado']['frac_sin_mapar'] <= SIN_MAPAR_MAX
    return res, tok_mapa


def estado_final(A_ok, estado_B):
    """A manda: sin A<=0,10 => SIN_MAPA aunque B sea COMPLETE; si A pasa, el estado es el de B."""
    return 'SIN_MAPA' if not A_ok else estado_B


def carga_cache():
    try: return json.load(open(CACHE))
    except (OSError, ValueError): return {}


def guarda_cache(c):
    os.makedirs(OUT3, exist_ok=True); tmp = CACHE + '.tmp'; json.dump(c, open(tmp, 'w')); os.replace(tmp, CACHE)


def main(argv):
    coins = ['eth', 'sol', 'xrp', 'btc']; dias = []
    i = 0
    while i < len(argv):
        if argv[i] == '--coins': coins = argv[i + 1].split(','); i += 2
        else: dias.append(argv[i]); i += 1
    import cadena_v2v3 as CV
    cache = carga_cache()
    for dia in dias:
        mapa = CV.mapa_token_moneda(dia, extra=None, marco=None)                      # sa_ms 5min+15min
        try: ext = json.load(open(CV.BASE + 'onchain_v3_token_mapa.json'))
        except (OSError, ValueError): ext = {}
        por_moneda = {}
        for c in coins:
            toks = {t for t, m in mapa.items() if m == c} | {t for t, v in ext.items() if v[0] == c}
            A, tm = metrica_A(dia, c, toks, cache)
            por_moneda[c] = dict(A=A, tokens_mapeados=len(tm), sha16_mapa=hashlib.sha256(json.dumps(tm, sort_keys=True).encode()).hexdigest()[:16])
            guarda_cache(cache)
        try: est = json.load(open(CV.BASE + f'exp5bis_27nov/estado_monedas_{dia}.json'))
        except (OSError, ValueError): est = {}
        for c, v in por_moneda.items(): v['estado_B'] = (est.get(c) or {}).get('estado'); v['estado_final'] = estado_final(v['A']['A_ok'], v['estado_B'] or 'SIN_B')
        os.makedirs(OUT3, exist_ok=True)
        json.dump(dict(dia=dia, generado=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), criterio='A<=0,10 (5m+15m, por moneda-dia) y B join>=0,90', por_moneda=por_moneda), open(OUT3 + f'sin_mapar_A_{dia}.json', 'w'), indent=1)
        print(dia, {c: (v['A']['combinado']['frac_sin_mapar'], v['estado_B'], v['estado_final']) for c, v in por_moneda.items()})


if __name__ == '__main__':
    main(sys.argv[1:])
