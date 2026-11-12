#!/usr/bin/env python3
"""plan_paquete_l.py [--n 40] [--precio 0.01] [--size 5] [--tope-usd 2.0] [--seed 20261112] [--plan] [--analiza GLOB] -- PLAN y ANALISIS del paquete de anclas directas de l (G, 12-Nov). ESTE SCRIPT NO ENVIA NINGUNA ORDEN, no firma, no importa py-clob-client,
no lee .env, no abre red: solo (a) genera y valida el PLAN determinista (tope de ordenes/coste/precio/permanencia) y (b) analiza los cancel_evid* que produzca el emisor aprobado. El EMISOR real es OTRO componente (propuesta: el `--paquete-pruebas` de
sonda1.py con wallet dedicada, ya con registro de canal de usuario `cancel_evidencia.py`), que exige /code-review y la confirmacion final de Javi ANTES de lanzarse; aqui no hay codigo de envio.
PROTOCOLO (fijado a priori): <= n=40 GTC post-only BUY, precio 0,01 (no cruza: ask >= 0,02; coste maximo por orden = size*precio = 0,05 $; 40 ordenes = 2,00 $ <= tope), una orden viva a la vez, en mercados BTC 5m con >= 60 s de vida restante; permanencia
`mantener_s` ~ U(1,0; 2,5) s decidida por el plan (semilla fija; NO depende de datos), tras ella DELETE; solo se registran canal de USUARIO (PLACEMENT/CANCELLATION con ts del exchange) + t_envio/t_ack/t_pre/t_resp locales; kill: cualquier relleno, 2 rechazos
seguidos, saldo que cae, ack>1 s, o coste >= tope. Ancla valida solo si existen PLACEMENT y CANCELLATION propios con ts_ex_ms y cancel_try con t_pre/t_resp para el mismo oid (join por oid exacto). Estadistico: n, p10/p50/p90, IC90 bootstrap de la mediana y p90;
objetivo n >= 30 anclas de cancelacion (si con n=40 ordenes salen < 30 validas, se declara INSUFFICIENT y no se repite sin nueva decision). Epoca de reloj y version de codigo en el manifiesto."""
import os, sys, json, glob, gzip, hashlib, collections, argparse
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = H + 'out/'
RNG = np.random.default_rng(20261112)


def plan(n, precio, size, tope, seed):
    r = np.random.default_rng(seed); coste_orden = round(size * precio, 4); assert precio <= 0.02 + 1e-12 and 0 < n <= 40 and coste_orden * n <= tope + 1e-9, ('plan fuera de topes', n, precio, size, tope)
    o = [dict(i=i, lado='YES' if i % 2 == 0 else 'NO', precio=precio, size=size, tipo='GTC_post_only_BUY', mantener_s=round(float(r.uniform(1.0, 2.5)), 3), min_vida_mercado_s=60) for i in range(n)]
    return dict(version='plan_paquete_l_v1', n_ordenes=n, coste_total_max_usd=round(coste_orden * n, 4), tope_usd=tope, seed=seed, ordenes=o, kill=['relleno', '2_rechazos_seguidos', 'saldo_cae', 'ack_ms>1000', 'coste>=tope'], ENVIO='NO IMPLEMENTADO AQUI: emisor pendiente de /code-review + OK Javi')


def pct(v):
    v = np.asarray(v, float)
    if len(v) == 0: return dict(n=0)
    r = dict(n=int(len(v)), p10=float(np.percentile(v, 10)), p50=float(np.median(v)), p90=float(np.percentile(v, 90)))
    if len(v) >= 5: s = v[RNG.integers(0, len(v), (2000, len(v)))]; r['p50_ic90'] = [float(np.percentile(np.median(s, 1), 5)), float(np.percentile(np.median(s, 1), 95))]; r['p90_ic90'] = [float(np.percentile(np.percentile(s, 90, axis=1), 5)), float(np.percentile(np.percentile(s, 90, axis=1), 95))]
    return r


def analiza(pat):
    """Anclas directas de TODOS los ficheros cancel_evid que casen con pat (deduplica por oid): alta_ex_menos_envio, cancel_ex_menos_envio, ack_menos_ex. Misma definicion que anclas_l_real.usuario_sonda."""
    ev = []
    for f in sorted(glob.glob(pat)):
        op = gzip.open if f.endswith('.gz') else open
        for l in op(f, 'rt'):
            try: ev.append(json.loads(l))
            except ValueError: pass
    alta = {e['oid']: e for e in ev if e.get('k') == 'alta'}; uo = collections.defaultdict(dict)
    for e in ev:
        if e.get('k') == 'user_order' and e.get('mine'): uo[e['oid']].setdefault(e['tipo'], e)
    cc = {e['oid']: e for e in ev if e.get('k') == 'cancel_try' and e.get('canceled')}; R = dict(alta_ex_menos_envio=[], cancel_ex_menos_envio=[], cancel_ack_menos_ex=[], cancel_ex_menos_alta_ex=[])
    for oid, a in alta.items():
        p = uo.get(oid, {}).get('PLACEMENT'); c = uo.get(oid, {}).get('CANCELLATION')
        if p: R['alta_ex_menos_envio'].append(p['ts_ex_ms'] - a['t_envio_ms'])
        if c and oid in cc: R['cancel_ex_menos_envio'].append(c['ts_ex_ms'] - cc[oid]['t_pre_ms']); R['cancel_ack_menos_ex'].append(cc[oid]['t_resp_ms'] - c['ts_ex_ms'])
        if p and c: R['cancel_ex_menos_alta_ex'].append(c['ts_ex_ms'] - p['ts_ex_ms'])
    return {k: pct(v) for k, v in R.items()}


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--n', type=int, default=40); ap.add_argument('--precio', type=float, default=0.01); ap.add_argument('--size', type=float, default=5.0); ap.add_argument('--tope-usd', type=float, default=2.0); ap.add_argument('--seed', type=int, default=20261112)
    ap.add_argument('--plan', action='store_true'); ap.add_argument('--analiza', default=None); a = ap.parse_args(); os.makedirs(OUT, exist_ok=True)
    if a.plan or not a.analiza:
        p = plan(a.n, a.precio, a.size, a.tope_usd, a.seed); p['sha256_plan'] = hashlib.sha256(json.dumps(p['ordenes'], sort_keys=True).encode()).hexdigest()[:16]; json.dump(p, open(OUT + 'paquete_l_plan.json', 'w'), indent=1); print('plan escrito', OUT + 'paquete_l_plan.json', 'n', p['n_ordenes'], 'coste max', p['coste_total_max_usd'], '$', 'sha', p['sha256_plan'])
    if a.analiza: print(json.dumps(analiza(a.analiza), indent=1))
