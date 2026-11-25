#!/usr/bin/env python3
"""etapa0_paquete_l_repro.py -- ADDENDUM1 B-2 del PREREG_REPLAY_BRECHA_B_16nov. SOLO LECTURA de las tandas B2/B3/B5 (13-Nov).
Reconstruye los valores individuales de cancel_ex_menos_envio y alta_ex_menos_envio con la logica que produjo `anclas_detalle`
(paquete_l.py::Paquete._anclas_detalle -> vendor plan_paquete_l.analiza, cargado con verificacion de sha por pl_core.cargar_vendor)
y comprueba n/p10/p50/p90 EXACTOS (|d| <= 1e-9) contra informe_final.json. Moneda por oid via ledger.jsonl (pl_core.anclas_de_eventos).
Uso: nice -n 19 ionice -c3 /usr/bin/python3 -I etapa0_paquete_l_repro.py. Escribe l_pool_vigente_13nov.json en este directorio."""
import os, sys, json, glob, gzip, hashlib, collections, datetime as dt
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)) + '/'
PL = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/paquete_l/'
DLP = '/root/polymarket-research-datalogs/paquete_l/'
sys.path.insert(0, PL)
import pl_core as C                                    # solo stdlib en su cabecera; no envia nada
V = C.cargar_vendor('plan_paquete_l')                 # ejecuta EXACTAMENTE los bytes con sha de VENDOR_HASHES.json
TANDAS = ('B2', 'B3', 'B5'); CAMPOS = ('n', 'p10', 'p50', 'p90'); TOL = 1e-9


def eventos(pat):                                      # copia literal de la lectura de analiza
    ev = []
    for f in sorted(glob.glob(pat)):
        op = gzip.open if f.endswith('.gz') else open
        for l in op(f, 'rt'):
            try: ev.append(json.loads(l))
            except ValueError: pass
    return ev


def valores(ev):                                       # mismo bucle que analiza, guardando el oid (orden = recorrido de `alta`)
    alta = {e['oid']: e for e in ev if e.get('k') == 'alta'}; uo = collections.defaultdict(dict)
    for e in ev:
        if e.get('k') == 'user_order' and e.get('mine'): uo[e['oid']].setdefault(e['tipo'], e)
    cc = {e['oid']: e for e in ev if e.get('k') == 'cancel_try' and e.get('canceled')}; canc, alt = [], []
    for oid, a in alta.items():
        p = uo.get(oid, {}).get('PLACEMENT'); c = uo.get(oid, {}).get('CANCELLATION')
        if p: alt.append((oid, p['ts_ex_ms'] - a['t_envio_ms']))
        if c and oid in cc: canc.append((oid, c['ts_ex_ms'] - cc[oid]['t_pre_ms'], cc[oid]['t_resp_ms'] - c['ts_ex_ms']))
    return canc, alt


def comp(a, b): return {k: dict(rec=a.get(k), inf=b.get(k), ok=(a.get(k) is not None and b.get(k) is not None and abs(float(a[k]) - float(b[k])) <= TOL)) for k in CAMPOS}


def main():
    out = dict(job='etapa0_paquete_l_repro', inicio_utc=dt.datetime.now(dt.timezone.utc).isoformat(), codigo_sha256=hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
               vendor_plan_paquete_l_sha256=V.__vendor_sha__, tandas={}, pool=[])
    puerta = True; puerta_alta = True
    for t in TANDAS:
        d = DLP + f'ensayo_real_{t}/'; pat = d + 'cancel_evid/cancel_evid_*.jsonl*'
        inf = json.load(open(d + 'informe_final.json')); ad = inf['anclas_detalle']
        ev = eventos(pat); canc, alt = valores(ev); va = V.analiza(pat)
        filas = C.leer_ledger_solo_lectura(d + 'ledger.jsonl')
        coin_c = {r['clave']: r['coin'] for r in filas if r.get('k') == 'intencion'}; coin_o = {r['oid']: coin_c.get(r['clave'], '?') for r in filas if r.get('k') == 'post' and r.get('oid')}
        anc, por = C.anclas_de_eventos(ev, filas)
        mine_c = V.pct([v for _, v, _ in canc]); mine_a = V.pct([v for _, v in alt])
        cc = comp(mine_c, ad['cancel_ex_menos_envio']); ca = comp(mine_a, ad['alta_ex_menos_envio']); cv = comp(va['cancel_ex_menos_envio'], ad['cancel_ex_menos_envio'])
        ok_c = all(x['ok'] for x in cc.values()) and all(x['ok'] for x in cv.values()); ok_a = all(x['ok'] for x in ca.values())
        puerta &= ok_c; puerta_alta &= ok_a
        alt_d = dict(alt)
        for oid, v, ack in canc: out['pool'].append(dict(tanda=t, oid=oid, coin=coin_o.get(oid, '?'), cancel_ex_menos_envio=v, cancel_ack_menos_ex=ack, alta_ex_menos_envio=alt_d.get(oid)))
        por_c = collections.Counter(coin_o.get(oid, '?') for oid, _, _ in canc)
        out['tandas'][t] = dict(ficheros_evid=[os.path.basename(f) for f in sorted(glob.glob(pat))], sha16_evid=[hashlib.sha256(open(f, 'rb').read()).hexdigest()[:16] for f in sorted(glob.glob(pat))],
                                sha16_ledger=hashlib.sha256(open(d + 'ledger.jsonl', 'rb').read()).hexdigest()[:16], sha16_informe=hashlib.sha256(open(d + 'informe_final.json', 'rb').read()).hexdigest()[:16],
                                cancel_ex_menos_envio=cc, cancel_via_vendor=cv, alta_ex_menos_envio=ca, cancel_reproduce=ok_c, alta_reproduce=ok_a,
                                anclas_directas=dict(rec=anc, inf=inf['cobertura']['anclas_directas'], por_moneda_rec=por, por_moneda_inf=inf['cobertura']['anclas_por_moneda']),
                                cancel_por_moneda=dict(por_c))
    v_all = [r['cancel_ex_menos_envio'] for r in out['pool']]; v_sb = [r['cancel_ex_menos_envio'] for r in out['pool'] if r['coin'] in ('ETH', 'SOL', 'XRP')]
    out['resumen'] = dict(puerta_B2_cancel=('PASA: l = MIX' if puerta else 'FALLA: l = 46 fija'), alta_reproduce=puerta_alta,
                          n_pool=len(v_all), n_sinBTC=len(v_sb), monedas_desconocidas=sum(1 for r in out['pool'] if r['coin'] not in ('BTC', 'ETH', 'SOL', 'XRP')),
                          pool_pct=V.pct(v_all), pool_sinBTC_pct=V.pct(v_sb),
                          nota='percentiles del pool y del pool sin BTC: descriptivos (los IC del vendor usan su RNG de modulo); l_i = 3 + v_j (ADDENDUM1 B-2.5)')
    out['fin_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
    tmp = H + 'l_pool_vigente_13nov.json.tmp'; json.dump(out, open(tmp, 'w'), indent=1); os.replace(tmp, H + 'l_pool_vigente_13nov.json')
    print(json.dumps(dict(resumen=out['resumen'], tandas={t: dict(cancel=v['cancel_reproduce'], alta=v['alta_reproduce'], anclas=v['anclas_directas'], cancel_por_moneda=v['cancel_por_moneda']) for t, v in out['tandas'].items()}), default=str))


if __name__ == '__main__':
    main()
