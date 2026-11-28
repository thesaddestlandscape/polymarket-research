#!/usr/bin/env python3
"""estado_monedas_cli.py DIA1 DIA2: aplica cadena_v2v3.estado_dia_moneda (definicion UNICA §2) a cada dia con el mapa sa_ms + cache gamma (onchain_v3_token_mapa.json). manifest_complete: de suelo_p5/manifest_suelo_D.json::estado.
Escribe datalogs/exp5bis_27nov/estado_monedas_<D>.json. Pesado (~1 GB, minutos): por cron_pesado."""
import sys, os, json, datetime as dt
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cadena_v2v3 as CV
SU = '/root/polymarket-research-dev-bk/experimentos/5m_barato/b_k_ejecutor/suelo_p5/manifest_suelo_%s.json'
cache = json.load(open(CV.BASE + 'onchain_v3_token_mapa.json')) if os.path.exists(CV.BASE + 'onchain_v3_token_mapa.json') else {}
extra = {t: v[0] for t, v in cache.items() if v[0] in ('bnb', 'doge', 'hype', 'btc') and v[1] in ('5m',)}      # solo 5m (el motor y las ordenes de B son 5m)
d, d1 = dt.date.fromisoformat(sys.argv[1]), dt.date.fromisoformat(sys.argv[2])
while d <= d1:
    ds = d.isoformat()
    try: mc = json.load(open(SU % ds)).get('estado') == 'COMPLETE'
    except Exception: mc = False
    try: r = CV.estado_dia_moneda(ds, mc, extra_mapa=extra)
    except Exception as e: r = dict(error=f'{type(e).__name__}: {e}')
    json.dump(r, open(CV.BASE + f'exp5bis_27nov/estado_monedas_{ds}.json', 'w'), indent=1)
    print(ds, 'manifest', mc, {c: (v['estado'], v['filas_F_v2'], v['filas_F_v3'], None if v['join'] is None else round(v['join'], 3), None if v['join_cadena_a_prints'] is None else round(v['join_cadena_a_prints'], 3)) for c, v in r.items() if c != '_global' and 'estado' in v} if 'error' not in r else r, flush=True)
    d += dt.timedelta(days=1)
