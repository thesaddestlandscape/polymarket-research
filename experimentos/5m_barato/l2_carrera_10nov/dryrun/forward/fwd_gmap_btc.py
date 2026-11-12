#!/usr/bin/env python3
"""fwd_gmap_btc.py [DIA ...] [--dir DIR] -- fuente de desenlace OFICIAL de BTC 5m para el forward B-CXB (PREREG_CXB_MULTIVARIANTE_FORWARD.md, H2).

Por que existe: el gmap del cron sa_r1 (r1_fwd_extract.py) solo trae eth/sol/xrp; sin BTC el resolvedor congelado deja los rellenos de BTC "sin desenlace".
Esquema IDENTICO al de sa_r1: {slug: {id, toks, des}} con toks = [token YES(Up), token NO(Down)] y des 'YES' | 'NO' | None; se escribe en DIR/gmap_btc_<D>.json
y el resolvedor lo carga con `cxb60_resolve.py <D> --gmap-dir DIR` (junto a los gmap_<D>.json de sa_r1, enlazados en el mismo DIR por el cron del forward).
Diferencias deliberadas con sa_r1 (mas estricto, nunca mas laxo):
  - solo se acepta un mercado si sus `outcomes` son exactamente [Up, Down] (si no, des=None y se cuenta en `etiquetas_inesperadas`: el mapeo token<->YES/NO NO se supone);
  - el desenlace exige closed=true y outcomePrices con un 1 y un 0 (>=0,999 / <=0,001); un 50/50 u otra cosa queda en None (missing != 0);
  - se mide y se escribe la COBERTURA (DIR/cob_btc_<D>.json): esperados cerrados / con desenlace / etiquetas inesperadas / sin mercado.
Idempotente: relee el fichero del dia y solo vuelve a consultar los slugs sin desenlace; escritura atomica. Solo GET publicos a gamma-api (sin credenciales, 0 ordenes).
Salida: 0 si cobertura de desenlace de los mercados cerrados >= 0,99; 3 si no (el cron avisa); 2 error de uso."""
import os, sys, json, time, argparse
from datetime import datetime, timedelta, timezone

DL = '/root/polymarket-research-datalogs/'
DIR_DEF = DL + 'cxb60_dryrun_gmap/'
GAMMA = 'https://gamma-api.polymarket.com/markets'
COIN = 'btc'
LOTE = 40
COB_MIN = 0.99
MARGEN_CIERRE_S = 600          # un mercado cuenta como "esperado cerrado" 10 min despues de su fin (gamma tarda en marcar closed)


def slugs_dia(d, coin=COIN):
    """Mismos slugs que sa_r1: un mercado cada 300 s desde t0-300 hasta t0+86400+300 (cubre los cierres del dia UTC D)."""
    t0 = int(datetime.fromisoformat(d).replace(tzinfo=timezone.utc).timestamp())
    return [f'{coin}-updown-5m-{s}' for s in range(t0 - 300, t0 + 86400 + 300, 300)]


def _lista(x):
    """gamma devuelve unas listas como cadena JSON y otras como lista."""
    if isinstance(x, str):
        try: x = json.loads(x)
        except ValueError: return None
    return x if isinstance(x, list) else None


def entrada_de_mercado(m):
    """Un mercado de gamma -> (entrada {id,toks,des[,motivo]}, motivo_o_None). NUNCA supone el orden de los tokens: lo valida por etiqueta."""
    toks = _lista(m.get('clobTokenIds')); outs = _lista(m.get('outcomes')); pr = _lista(m.get('outcomePrices'))
    if not toks or len(toks) != 2 or m.get('id') is None: return None, 'sin_tokens'
    e = dict(id=str(m['id']), toks=[str(t) for t in toks], des=None)
    if outs is None or [str(o).strip().lower() for o in outs] != ['up', 'down']:
        e['motivo'] = 'etiquetas_inesperadas'; return e, 'etiquetas_inesperadas'
    if m.get('closed') and pr and len(pr) == 2:
        try: a, b = float(pr[0]), float(pr[1])
        except (TypeError, ValueError): return e, 'precios_ilegibles'
        if a >= 0.999 and b <= 0.001: e['des'] = 'YES'
        elif b >= 0.999 and a <= 0.001: e['des'] = 'NO'
        else: e['motivo'] = 'desenlace_no_binario'; return e, 'desenlace_no_binario'
    return e, None


def consulta(get, slugs):
    """get(url, params_list) -> lista JSON de mercados. Devuelve ({slug: entrada}, Counter de motivos, n_errores_red). Prefiere SIEMPRE la entrada con desenlace."""
    out, motivos, errores = {}, {}, 0
    for k in range(0, len(slugs), LOTE):
        trozo = slugs[k:k + LOTE]
        for closed in ('true', 'false'):         # gamma no devuelve cerrados sin closed=true (trampa documentada)
            try: r = get(GAMMA, [('slug', s) for s in trozo] + [('closed', closed), ('limit', str(LOTE))])
            except Exception as e:
                errores += 1; print('gamma err', repr(e)[:160], file=sys.stderr); continue
            for m in (r if isinstance(r, list) else []):
                sl = m.get('slug')
                if sl not in trozo: continue
                e, mot = entrada_de_mercado(m)
                if e is None: motivos[sl] = mot; continue
                if sl not in out or (e['des'] and not out[sl]['des']): out[sl] = e; motivos[sl] = mot
        time.sleep(float(os.environ.get('FWD_GMAP_SLEEP', '0.15')))
    return out, motivos, errores


def construir(d, dir_out=DIR_DEF, get=None, ahora=None):
    """Construye/actualiza dir_out/gmap_btc_<d>.json y cob_btc_<d>.json. Devuelve la cobertura (dict)."""
    dir_out = str(dir_out).rstrip('/') + '/'                 # 12-Nov (ensayo del diario): el cron pasa $G SIN barra final y `dir_out + 'gmap_btc_..'` escribia FUERA del directorio (cxb60_dryrun_gmapgmap_btc_*.json)
    os.makedirs(dir_out, exist_ok=True); f = dir_out + f'gmap_btc_{d}.json'
    try: viejo = json.load(open(f)) if os.path.exists(f) else {}
    except (OSError, ValueError): viejo = {}               # fichero corrupto: se reconstruye entero
    if get is None:
        import requests; ses = requests.Session(); get = lambda url, params: ses.get(url, params=params, timeout=25).json()
    slugs = slugs_dia(d); pend = [s for s in slugs if s not in viejo or viejo[s].get('des') is None]
    nuevo, motivos, errores = consulta(get, pend) if pend else ({}, {}, 0)
    gm = dict(viejo); gm.update(nuevo)                    # `pend` solo tenia slugs sin desenlace: lo nuevo nunca pisa un desenlace ya conocido
    tmp = f + '.tmp'; json.dump(gm, open(tmp, 'w')); os.replace(tmp, f)
    ahora = time.time() if ahora is None else ahora
    cerrados = [s for s in slugs if int(s.rsplit('-', 1)[1]) + 300 + MARGEN_CIERRE_S <= ahora]
    con_des = [s for s in cerrados if s in gm and gm[s].get('des')]
    et = [s for s in cerrados if s in gm and gm[s].get('motivo') == 'etiquetas_inesperadas']
    sin_mercado = [s for s in cerrados if s not in gm]
    cob = dict(dia=d, fuente='gamma-api /markets (solo lectura)', slugs_dia=len(slugs), esperados_cerrados=len(cerrados), con_desenlace=len(con_des), etiquetas_inesperadas=len(et), sin_mercado_en_gamma=len(sin_mercado),
               sin_desenlace_otros=len(cerrados) - len(con_des) - len(et) - len(sin_mercado), cobertura_desenlace=round(len(con_des) / len(cerrados), 4) if cerrados else None, errores_red=errores, consultados=len(pend),
               ts_utc=datetime.fromtimestamp(ahora, timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
    tmp = dir_out + f'cob_btc_{d}.json.tmp'; json.dump(cob, open(tmp, 'w'), indent=1); os.replace(tmp, dir_out + f'cob_btc_{d}.json')
    return cob


def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument('dias', nargs='*'); ap.add_argument('--dir', default=DIR_DEF); a = ap.parse_args(argv)
    dias = a.dias or [(datetime.now(timezone.utc) - timedelta(days=k)).strftime('%Y-%m-%d') for k in (1, 2)]
    rc = 0
    for d in dias:
        try: datetime.fromisoformat(d)
        except ValueError: print('dia invalido', d, file=sys.stderr); return 2
        c = construir(d, a.dir); print(json.dumps(c))
        if c['cobertura_desenlace'] is None or c['cobertura_desenlace'] < COB_MIN: rc = 3
    return rc


if __name__ == '__main__': sys.exit(main())
