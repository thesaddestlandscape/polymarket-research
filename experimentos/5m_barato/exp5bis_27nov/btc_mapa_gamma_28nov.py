#!/usr/bin/env python3
"""btc_mapa_gamma_28nov.py DIA1 [DIA2 ...]  (28-Nov, ANEXO3 §3 (i)-(iv), tarea 9). Solo LEE: gamma_slug_cache.json (ya validado: endDate exacto, 2 tokens, version) + cadena_v2v3 (estado por moneda). 0 red, 0 ordenes.
CAUSA DEL SIN_MAPA/DATA_BLOCKED de BTC (medida 28-Nov, sin_mapar_A_{18,24,25,26}.json): gamma devuelve los 384 slugs BTC/dia (5m 288 + 15m 96) con endDate exacto, pero el mapa token->moneda del pipeline (sa_ms/ms_D.npz + onchain_v3_token_mapa.json) NO trae tokens BTC
(npz solo ETH/SOL/XRP; la cache extra solo 6 tokens BTC de un dia): en_mapa 0-3/384. Es un hueco del MAPA, no del logger ni de la cadena (BTC 24-Nov: 7.954 filas F V3, join 0,999 con 6 tokens).
ARREGLO: `mapa_extra_btc(dia)` = tokens BTC 5m de gamma (por slug de la rejilla) como `extra_mapa` de cadena_v2v3.estado_dia_moneda (hecho para ello). Solo AÑADE tokens de BTC: el estado de ETH/SOL/XRP no puede cambiar (se comprueba en `compara_otras_monedas`).
Salida: datalogs/exp5bis_27nov/paso3/estado_monedas_btc_DIA.json (estado BTC con mapa gamma + comparacion de las otras monedas con estado_monedas_DIA.json previo). Pesado (~1 GB, minutos por dia): por scripts/cron_pesado.sh, ulimit -v 3000000."""
import sys, os, json, hashlib
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sin_mapar_A_28nov as S
import cadena_v2v3 as CV
SU = '/root/polymarket-research-dev-bk/experimentos/5m_barato/b_k_ejecutor/suelo_p5/manifest_suelo_%s.json'
OTRAS = ('eth', 'sol', 'xrp', 'bnb', 'doge', 'hype')


def mapa_extra_btc(dia, cache=None, marcos=('5m',)):
    """{token: 'btc'} con los tokens de gamma de la rejilla del dia (solo 5m por defecto: libro5_tx y B son 5m). Slugs sin registro valido NO aportan (siguen contando sin mapar en la metrica A)."""
    cache = S.carga_cache() if cache is None else cache; m = {}
    for marco in marcos:
        for slug, _, _ in S.rejilla(dia, 'btc', marco):
            r = cache.get(slug)
            if r:
                for t in r['tokens']: m[t] = 'btc'
    return m


def compara_otras_monedas(nuevo, previo):
    """Las otras monedas deben salir IDENTICAS (estado, filas, join) al anadir BTC al mapa. -> (ok, diferencias)."""
    dif = []
    for c in OTRAS:
        a, b = nuevo.get(c), previo.get(c)
        if (a is None) != (b is None): dif.append((c, 'presencia')); continue
        if a is None: continue
        for k in ('estado', 'filas_F_v2', 'filas_F_v3', 'join', 'join_cadena_a_prints', 'pares_libro5tx'):
            if a.get(k) != b.get(k): dif.append((c, k, a.get(k), b.get(k)))
    return (not dif), dif


def main(dias):
    for dia in dias:
        extra = mapa_extra_btc(dia)
        try: mc = json.load(open(SU % dia)).get('estado') == 'COMPLETE'
        except Exception: mc = False
        prev = CV.BASE + f'exp5bis_27nov/estado_monedas_{dia}.json'
        previo = json.load(open(prev)) if os.path.exists(prev) else {}
        # el mapa extra del pipeline (BNB/DOGE/HYPE/BTC de la cache v3) se conserva y se le suma el de BTC de gamma
        cache3 = json.load(open(CV.BASE + 'onchain_v3_token_mapa.json')) if os.path.exists(CV.BASE + 'onchain_v3_token_mapa.json') else {}
        base = {t: v[0] for t, v in cache3.items() if v[0] in ('bnb', 'doge', 'hype', 'btc') and v[1] in ('5m',)}
        base.update(extra)
        r = CV.estado_dia_moneda(dia, mc, extra_mapa=base)
        ok, dif = compara_otras_monedas(r, previo) if previo else (None, ['sin estado previo'])
        b = r.get('btc', {})
        out = dict(dia=dia, tokens_btc_gamma_5m=len(extra), sha16_mapa_btc=hashlib.sha256(json.dumps(sorted(extra)).encode()).hexdigest()[:16], btc=b, otras_monedas_identicas=ok, diferencias=dif, manifest_complete=mc)
        tmp = S.OUT3 + f'estado_monedas_btc_{dia}.json.tmp'; json.dump(out, open(tmp, 'w'), indent=1, default=str); os.replace(tmp, S.OUT3 + f'estado_monedas_btc_{dia}.json')
        print(dia, 'BTC', b.get('estado'), 'F v2/v3', b.get('filas_F_v2'), b.get('filas_F_v3'), 'join', b.get('join'), 'tokens gamma', len(extra), 'otras identicas', ok, flush=True)


if __name__ == '__main__':
    main(sys.argv[1:])
