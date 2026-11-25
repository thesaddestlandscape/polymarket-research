#!/usr/bin/env python3
"""sembrar_cache_tokens.py -- UNA SOLA VEZ (idempotente): siembra datalogs/libro_tokens_cache.json con el universo VIGENTE ahora, resuelto
con el MISMO codigo de la cache (libro_estado_ws del directorio de este script): tokens por gamma + contraste CLOB (-> ctr:true) y fallback
a una sola fuente (-> sc:true). Sirve para que el arranque en frio del despliegue publique ya el universo sin gamma ni leer el CSV.
No toca ningun proceso, main ni dev; solo escribe la cache (flock + fusion con lo que haya; tombstones respetados). Ritmo <=5 req/s.
Lee el universo de la COLA del CSV de hoy (y la de ayer si estamos en las primeras 2 h tras las 00:00Z), sin importar fetch_libro_ambos_lados
real (un stub con las mismas funciones puras de shadow_predict): no importa live_trade ni lee credenciales.
Uso: sembrar_cache_tokens.py [--cache RUTA] [--max N] [--solo-informe] [--tasa 5]
Salida: tamano, n de mercados, contrastados, sin contraste, vencidos(0), y la prueba de arranque en frio. Exit 0 ok / 2 gamma caida (429) / 3 fallo."""
import argparse, importlib.util, json, os, sys, time, types
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = os.environ.get('REPO_SEMBRAR', '/root/polymarket-research')


def cargar_modulos(repo):
    sys.path.insert(1, repo)
    from shadow_predict import _parse_updown_tipo, identificar_activo          # funciones puras sobre texto (mismas que usa el lector real)
    fl = types.ModuleType('fetch_libro_ambos_lados')
    fl._parse_updown_tipo, fl.identificar_activo = _parse_updown_tipo, identificar_activo
    fl.ACTIVOS = {"BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"}; fl.MARCOS_TRACKEADOS = {5, 15, 60}
    sys.modules['fetch_libro_ambos_lados'] = fl
    sp = importlib.util.spec_from_file_location('libro_estado_ws_stage', str(AQUI / 'libro_estado_ws.py'))
    L = importlib.util.module_from_spec(sp); sp.loader.exec_module(L)
    return L


GUARDA_CADA = 25          # guardado incremental de la cache cada N mercados resueltos (un timeout del llamador no pierde lo ya sembrado)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--cache'); ap.add_argument('--max', type=int, default=400); ap.add_argument('--solo-informe', action='store_true'); ap.add_argument('--tasa', type=float, default=5.0)
    ap.add_argument('--markets-dir')
    ap.add_argument('--presupuesto-s', type=float, default=240.0, help='tiempo maximo del bucle de resolucion: debe ser < el timeout del llamador (el deploy usa 300 s)')
    a = ap.parse_args(argv)
    L = cargar_modulos(REPO)
    if a.cache:
        L.TOK_CACHE_PATH = Path(a.cache)
        lock = L.TOK_CACHE_PATH.with_name(L.TOK_CACHE_PATH.name + '.lock')         # _cache_guardar deriva el lock de TOK_CACHE_PATH (se lee en cada llamada)
        if lock.parent != Path(a.cache).parent or not lock.name.startswith(Path(a.cache).name):
            print(f'ABORTO: la ruta derivada del lock ({lock}) no cuelga de --cache {a.cache}', flush=True); return 3
    L.TOK_MARKETS_DIR = Path(a.markets_dir) if a.markets_dir else Path(REPO) / 'data' / 'markets'      # (en el stage __file__ no esta en la raiz del repo)
    ahora = time.time(); ahora_dt = datetime.fromtimestamp(ahora, timezone.utc)
    hoy_f = L.TOK_MARKETS_DIR / ahora_dt.strftime('%Y-%m-%d.csv')
    hoy = {}
    if hoy_f.exists():
        hoy = L._leer_cola_csv(hoy_f, ahora_dt)
    univ = L._universo_csv(lambda: hoy, ahora)                                  # + cola de ayer si procede
    print(f'[{ahora_dt:%FT%TZ}] universo vigente en las colas de los CSV: {len(univ)} mercados (hoy {len(hoy)})', flush=True)
    cand = sorted(univ.items(), key=lambda kv: kv[1][3])[:a.max]
    sess = L._sesion_datos(); est = {'sonda': False}; ok = sc = fall = 0; t0 = time.time(); gamma_caida = False; sin_tiempo = False
    sembrados = []                                                                # mids resueltos y puestos en ESTA ejecucion
    escribe = not a.solo_informe
    for i, (mid, (activo, marco, cid, edt)) in enumerate(cand):
        if L._GAMMA['score'] >= L.TOK_GAMMA_SCORE_MAX:
            gamma_caida = True; break
        if time.time() - t0 >= a.presupuesto_s:
            sin_tiempo = True; break
        espera = t0 + i * 2.0 / a.tasa - time.time()                           # 2 llamadas por mercado (gamma + clob)
        if espera > 0: time.sleep(min(espera, max(0.0, a.presupuesto_s - (time.time() - t0))))
        yes, no, src, kind = L._resolver_mercado(sess, mid, cid, est, time.time() + 12.0)
        if kind is None:
            with L._TOK_LOCK: L._poner(mid, yes, no, activo, marco, cid, edt, src)
            ok += 1; sc += bool(src); sembrados.append(mid)
            if escribe and ok % GUARDA_CADA == 0:                              # guardado incremental (fusiona con el disco, nunca pisa)
                L._CACHE['sucio'] = True; L._CACHE['prox_intento'] = 0.0; L._cache_guardar()
        else:
            fall += 1
    print(f'resueltos {ok} (contrastados {ok - sc}, sin contraste {sc}), fallidos {fall}, de {len(cand)} candidatos, gamma_caida={gamma_caida}, sin_tiempo={sin_tiempo}, {time.time() - t0:.0f}s', flush=True)
    if a.solo_informe:
        print('SOLO INFORME: no se escribe'); return 2 if gamma_caida else 0
    if ok:
        L._CACHE['sucio'] = True; L._CACHE['prox_intento'] = 0.0; L._cache_guardar()
        if L._CACHE['n_err']:
            print('FALLO escribiendo la cache', flush=True); return 3
    # prueba de arranque en frio con la cache escrita: estado limpio + _cache_cargar + publicar
    p = L.TOK_CACHE_PATH
    try: tam = p.stat().st_size
    except OSError: print('no hay fichero de cache'); return 3
    j = json.loads(p.read_text()); ahora2 = time.time()
    venc = sum(1 for v in j['mercados'].values() if datetime.fromisoformat(v['edt']).timestamp() <= ahora2)
    for d in (L._TOK, L._MKT, L._TOK_FALLO, L._CACHE_ENTRIES, L._SC_SRC, L._TOMB): d.clear()
    L._SIN_CONTRASTE.clear()
    n = L._cache_cargar(ahora2)
    # el rc depende de lo SEMBRADO en esta ejecucion: cada mercado sembrado y aun vigente debe estar en el fichero (los vencidos de otras ejecuciones no cuentan)
    vigentes = [m for m in sembrados if univ[m][3].timestamp() > ahora2]                  # edt es datetime (_leer_cola_csv)
    faltan = [m for m in vigentes if m not in j['mercados']]
    ctr = sum(1 for v in j['mercados'].values() if v.get('ctr')); scn = sum(1 for v in j['mercados'].values() if v.get('sc'))
    print(f'CACHE {p}: {tam} bytes, {len(j["mercados"])} mercados, ctr:true {ctr}, sc:true {scn}, vencidos en fichero {venc} (informativo), tombstones {len(j.get("tombstones", {}))}; '
          f'sembrados ahora {ok}, vigentes {len(vigentes)}, ausentes del fichero {len(faltan)}; arranque en frio carga {n} y deja {len(L._SIN_CONTRASTE)} sin contraste', flush=True)
    if gamma_caida and not ok: return 2
    if not ok or faltan or not n: return 3
    return 0


if __name__ == '__main__':
    sys.exit(main())
