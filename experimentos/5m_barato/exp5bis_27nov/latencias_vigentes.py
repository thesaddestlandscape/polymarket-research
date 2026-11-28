#!/usr/bin/env python3
"""latencias_vigentes.py -- FUENTE UNICA de las latencias vigentes del paso 3 (28-Nov, ANEXO5 / REDTEAM F). Genera y valida `latencias_vigentes.json`; el adaptador 5a, FN12 y el kill P1b SOLO leen de aqui (`carga()`), nunca de cifras copiadas en los anexos.
Construye desde: (1) las salidas de `ancla_p1b_28nov.py` (ancla de MERCADO leida de libro5_ms, con censura) de los runs P1b B y A del 28-Nov, (2) los ledger.jsonl de esos runs (ack HTTP POST/DELETE crudos, decision->envio, disparo->DELETE),
(3) los informes_final de paquete_l 13-Nov (ensayo_real_B2/B3/B5, canal de USUARIO; solo referencia y origen de los brazos heredados 74/111/147). Cada fuente lleva su sha256. Nada se inventa: lo no medido es `null` / 'no_medido'.
Reloj: t_envio/t_ack = reloj local (chrony); ex = sello de mercado (exchange) del libro5_ms; rx = recepcion local. rx-ex del suelo: clase lo/hi/mixta/indet por ANCLA (suelo_causal; ver ancla_p1b_28nov).
Uso: python3 -I latencias_vigentes.py --ancla J [--ancla J ...] --out latencias_vigentes.json   |   from latencias_vigentes import carga"""
import argparse
import collections
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
JSON_VIGENTE = os.path.join(HERE, 'latencias_vigentes.json')
PAQUETE_L_DIR = '/root/polymarket-research-datalogs/paquete_l'
INFORMES_13NOV = ('ensayo_real_B2', 'ensayo_real_B3', 'ensayo_real_B5')
ANEXOS = ('CONTRATO_5BIS_EXP5B_27nov.ANEXO3_28nov.md', 'CONTRATO_5BIS_EXP5B_27nov.ANEXO4_28nov.md')
DOCS = '/root/polymarket-research/misiones/5m_barato/docs/'
MONEDAS = ('BTC', 'ETH', 'SOL', 'XRP')
VERSION = 'latencias_vigentes_28nov_v1'
# Brazos de L_cancel: CENTRAL = medido por moneda (se rellena); el resto con su ORIGEN verificado en el codigo/informes (ANEXO5 §A). Decision de Javi 28-Nov.
BRAZOS_HEREDADOS = {
    '74': dict(rol='intermedio_heredado_fuera_como_central', origen='p90 del pool 13-Nov n=313 de cancel_ex_menos_envio (comentario passT_v5.py:19 "sens. 74 = p90"); NO recomputable desde los informes por run (min/max por run 41-111)', canal='usuario'),
    '111': dict(rol='heredado', origen='p90 de cancel_ex_menos_envio de ensayo_real_B2 (111,4 ms, n=105; informe_final.json anclas_detalle)', canal='usuario'),
    '119': dict(rol='no_medido', origen='p90 "mercado todas" del ANEXO4 A (P1b B 28-Nov) REFUTADO por el validador: mezcla + primer salto contaminado; unicas p90 global 58-59. Se conserva como brazo de trazabilidad, rotulado no medido', canal='mercado'),
    '147': dict(rol='heredado', origen='p90 de ALTA (alta_ex_menos_envio) de ensayo_real_B2 (146,6 ms, n=107) -- NO es una cancelacion (ADENDA p3_agrega_v12.py:68); se mantiene como brazo de estres de cola', canal='usuario'),
    '202': dict(rol='estres_informativo', origen='cancel_ex_menos_envio p50 del canal de USUARIO en P1b B 28-Nov (ANEXO3 §0); una franja nocturna; no es sello de mercado', canal='usuario'),
    '1320': dict(rol='estres_informativo', origen='cancel_ex_menos_envio p90 del canal de USUARIO en P1b B 28-Nov (ANEXO3 §0)', canal='usuario'),
}


def sha256_fichero(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def _sha_o_missing(p):
    try:
        return sha256_fichero(p)
    except OSError:
        return 'missing'


def cuantil(x, p):
    x = sorted(x)
    return None if not x else round(float(x[min(len(x) - 1, int(p * len(x)))]), 3)


def resumen(x):
    return dict(n=len(x), p10=cuantil(x, .1), p50=cuantil(x, .5), p90=cuantil(x, .9))


def _ledger_ack(run_dir):
    """-> {coin: dict(post_http[], delete_http[], d_post[], d_det_delete[])} del ledger crudo (reloj local). Un cancel con reintentos aporta SOLO su intento 1 a delete_http y d_det_delete (como el kill)."""
    I, P, C = {}, {}, collections.defaultdict(list)
    with open(os.path.join(run_dir, 'ledger.jsonl')) as f:
        for ln in f:
            try:
                r = json.loads(ln)
            except ValueError:
                continue
            k = r.get('k')
            if k == 'intencion':
                I[r['oid_local']] = r
            elif k == 'post' and r.get('t_send_ns') and r.get('t_ack_ns') and r.get('clase') == 'ok':
                P[r['oid_local']] = r
            elif k == 'cancel' and r.get('t_send_ns'):
                C[r['oid']].append(r)
    out = collections.defaultdict(lambda: collections.defaultdict(list))
    for oid, p in P.items():
        i = I.get(oid)
        if not i:
            continue
        for c in (i['coin'], 'TODAS'):
            out[c]['post_http'].append((p['t_ack_ns'] - p['t_send_ns']) / 1e6)
            if i.get('t_decision_ns'):
                out[c]['d_post'].append((p['t_send_ns'] - i['t_decision_ns']) / 1e6)
        cs = sorted(C.get(oid, []), key=lambda r: r.get('intento') or 0)
        if cs and cs[0].get('t_ack_ns') and cs[0].get('ok'):
            for c in (i['coin'], 'TODAS'):
                out[c]['delete_http'].append((cs[0]['t_ack_ns'] - cs[0]['t_send_ns']) / 1e6)
                if cs[0].get('t_trig_rx_ns'):
                    out[c]['d_det_delete'].append((cs[0]['t_send_ns'] - cs[0]['t_trig_rx_ns']) / 1e6)
    return out


def _km(obs, p):
    sys.path.insert(0, HERE)
    import ancla_p1b_28nov as A
    return A.km_cuantil(obs, p)


def informe_13nov(base=PAQUETE_L_DIR):
    out = []
    for r in INFORMES_13NOV:
        p = os.path.join(base, r, 'informe_final.json')
        try:
            d = json.load(open(p))
            ad = d['anclas_detalle']
            out.append(dict(run=r, fichero=p, sha256=sha256_fichero(p), status=d.get('status'), canal='usuario', reloj='ex(usuario)-envio',
                            alta_ex_menos_envio={k: ad['alta_ex_menos_envio'].get(k) for k in ('n', 'p50', 'p90')}, cancel_ex_menos_envio={k: ad['cancel_ex_menos_envio'].get(k) for k in ('n', 'p50', 'p90')}))
        except (OSError, KeyError, ValueError):
            out.append(dict(run=r, fichero=p, sha256='missing'))
    return out


def construye(ancla_jsons, paquete_dir=PAQUETE_L_DIR):
    """ancla_jsons: lista de rutas de salida de ancla_p1b_28nov. -> dict latencias_vigentes (sin sha propio)."""
    anclas_por = collections.defaultdict(lambda: collections.defaultdict(list))        # (tipo,coin)->filas
    fuentes, runs, esp = [], [], collections.defaultdict(int)
    ack = collections.defaultdict(lambda: collections.defaultdict(list))
    clases = collections.defaultdict(lambda: collections.Counter())
    for j in ancla_jsons:
        A = json.load(open(j))
        fuentes.append(dict(tipo='ancla_p1b_28nov', fichero=j, sha256=sha256_fichero(j), codigo_sha256=A['codigo']['ancla_p1b_28nov_sha256'], sha256_resultado=A['sha256_resultado']))
        for r in A['runs']:
            if r.get('estado') != 'COMPLETE':
                runs.append(dict(run=r.get('run'), estado=r.get('estado'), motivo=r.get('motivo')))
                continue
            rd = os.path.join(paquete_dir, r['run'])
            fuentes.append(dict(tipo='ledger_p1b', fichero=os.path.join(rd, 'ledger.jsonl'), sha256=r['entradas']['ledger_sha256']))
            for f in r['anclas']:
                esp[(f['tipo'], f['coin'])] += 1
                anclas_por[(f['tipo'], f['coin'])]['filas'].append(f)
                clases[(f['tipo'], f['coin'])][f.get('clase') if f['estado'] == 'ancla' else 'censurada'] += 1
            runs.append(dict(run=r['run'], estado='COMPLETE', intenciones=r['cobertura']['intenciones'], firma_tamano=r['cobertura']['firma_tamano'], libro=[dict(fichero=x['fichero'], sha256_prefijo_leido=x['sha256_prefijo_leido'], bytes_leidos=x['bytes_leidos']) for x in r['entradas']['libro']['ficheros']]))
            for c, d in _ledger_ack(rd).items():
                for k, v in d.items():
                    ack[c][k] += v
    por_moneda = {}
    for coin in MONEDAS:
        m = {}
        for tipo in ('alta', 'cancel'):
            F = anclas_por.get((tipo, coin), {}).get('filas', [])
            if not F:
                m[tipo] = None
                continue
            A_ = [f for f in F if f['estado'] == 'ancla']
            lo = [f for f in A_ if f.get('clase') == 'lo']
            hi = [f for f in A_ if f.get('clase') == 'hi']
            obs = [(f['lat_ex_ms'], True) for f in A_] + [(f['censura_ms'], False) for f in F if f['estado'] != 'ancla']
            cens = (len(F) - len(A_)) / len(F)
            m[tipo] = dict(esperado=len(F), anclas=len(A_), tasa_censura=round(cens, 4), clases=dict(sorted(clases[(tipo, coin)].items())),
                           lo=dict(ex=resumen([f['lat_ex_ms'] for f in lo]), rx=resumen([f['lat_rx_ms'] for f in lo])),
                           hi=(dict(ex=resumen([f['lat_ex_ms'] for f in hi]), rx=resumen([f['lat_rx_ms'] for f in hi])) if hi else None),
                           todas_las_anclas=dict(ex=resumen([f['lat_ex_ms'] for f in A_]), rx=resumen([f['lat_rx_ms'] for f in A_])),
                           km_ex=dict(p50=_km(obs, .5), p90=_km(obs, .9)),
                           calidad=('ACEPTADA' if cens <= 0.10 else f'PROVISIONAL (censura {cens:.0%} > 10 %: ancla no unica; el p50 observado esta sesgado hacia casos rapidos, usar KM/brazos)'))
        m['ack_http'] = {k: resumen(v) for k, v in sorted(ack.get(coin, {}).items()) if k in ('post_http', 'delete_http')}
        m['d_post_decision_a_envio'] = resumen(ack.get(coin, {}).get('d_post', []))
        m['d_det_a_delete'] = resumen(ack.get(coin, {}).get('d_det_delete', []))
        por_moneda[coin] = m
    todas = {k: resumen(v) for k, v in sorted(ack.get('TODAS', {}).items())}
    # central de L_cancel por moneda (decision de Javi 28-Nov): p50 observado de las anclas de clase 'lo', en cada reloj; BTC no medido hasta el ensayo dedicado.
    central = {}
    for coin in MONEDAS:
        c = por_moneda[coin].get('cancel')
        ok = coin != 'BTC' and c is not None and c['lo']['ex']['n'] >= 10
        central[coin] = dict(ex_ms=(c['lo']['ex']['p50'] if ok else None), rx_ms=(c['lo']['rx']['p50'] if ok else None), n=(c['lo']['ex']['n'] if c else 0), calidad=(c['calidad'] if ok else 'no_medido (BTC: ancla no unica; esperar al ensayo con firma de tamano)' if coin == 'BTC' else 'n<10'))
    alta_central = {}
    for coin in MONEDAS:
        c = por_moneda[coin].get('alta')
        ok = coin != 'BTC' and c is not None and c['lo']['ex']['n'] >= 10
        alta_central[coin] = dict(ex_ms=(c['lo']['ex']['p50'] if ok else None), rx_ms=(c['lo']['rx']['p50'] if ok else None), n=(c['lo']['ex']['n'] if c else 0), calidad=(c['calidad'] if ok else 'no_medido' if coin == 'BTC' else 'n<10'))
    dp = todas.get('d_post') or {}
    out = dict(version=VERSION, reloj='t_envio/t_ack=local (chrony); ex=sello mercado libro5_ms; rx=recepcion local; formula C: t_arr_rx = t_dec_rx + D_post + L_alta_rx ; t_end_rx = t_trig_rx + D_det_a_DELETE + L_cancel_rx',
               runs=runs, fuentes=sorted(fuentes, key=lambda z: (z['tipo'], z['fichero'])), por_moneda=por_moneda, todas_monedas_ledger=todas,
               D_post=dict(p50=dp.get('p50'), p90=dp.get('p90'), n=dp.get('n'), origen='ledger P1b: t_send - t_decision (decision -> envio del POST), todas las monedas, runs de las fuentes'),
               D_det_a_DELETE=dict(p50=(todas.get('d_det_delete') or {}).get('p50'), p90=(todas.get('d_det_delete') or {}).get('p90'), n=(todas.get('d_det_delete') or {}).get('n'),
                                   origen='ledger P1b: cancel.t_send - cancel.t_trig_rx del disparo PROGRAMADO (hold): cota inferior del motor real (no incluye deteccion); el motor la medira cuando exista'),
               L_alta_central=alta_central, L_cancel_central=central, brazos_L_cancel=BRAZOS_HEREDADOS,
               referencia_13nov_paquete_l=dict(informes=informe_13nov(paquete_dir), L1_principal_ms=34, L1_robusto_ms=47, L3a_ms=57, L3b_fallback_ms=59, origen='ANEXO_V2 §3 / ANEXO3 §0; canal de USUARIO, reloj ex(usuario); referencia, NO sustituye a la medicion de mercado'),
               anexos=[dict(fichero=a, sha256=_sha_o_missing(DOCS + a)) for a in ANEXOS],
               codigo=dict(latencias_vigentes_py_sha256=sha256_fichero(os.path.abspath(__file__))))
    return out


def sello(d):
    x = dict(d)
    x.pop('sha256_contenido', None)
    return hashlib.sha256(json.dumps(x, sort_keys=True).encode()).hexdigest()


def escribe(d, out):
    d = dict(d)
    d['sha256_contenido'] = sello(d)
    tmp = out + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(d, f, indent=1, sort_keys=True)
    os.replace(tmp, out)
    return d


class LatenciasInvalidas(RuntimeError):
    pass


def carga(path=JSON_VIGENTE):
    """Carga y VALIDA latencias_vigentes.json (sha del contenido; version). Fail-closed: LatenciasInvalidas si falta o no coincide."""
    try:
        d = json.load(open(path))
    except (OSError, ValueError) as e:
        raise LatenciasInvalidas(f'latencias_vigentes ilegible: {e}')
    if d.get('version') != VERSION or d.get('sha256_contenido') != sello(d):
        raise LatenciasInvalidas('latencias_vigentes: version o sha256_contenido no validos (fichero editado a mano?)')
    return d


def l_cancel_rx(d, coin):
    """L_cancel_rx central de `coin` (ms) o None si no medido (el consumidor decide: brazo 'no medido', nunca 0)."""
    return (d['L_cancel_central'].get(coin) or {}).get('rx_ms')


def l_alta_rx(d, coin):
    return (d['L_alta_central'].get(coin) or {}).get('rx_ms')


def main(argv=None):
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument('--ancla', action='append', required=True)
    ap.add_argument('--out', default=JSON_VIGENTE)
    ns = ap.parse_args(argv)
    d = escribe(construye(ns.ancla), ns.out)
    print('latencias_vigentes', ns.out, d['sha256_contenido'][:16])
    for c in MONEDAS:
        print(c, 'L_alta_rx', d['L_alta_central'][c], '| L_cancel', d['L_cancel_central'][c])
    print('D_post', d['D_post'], '| D_det_a_DELETE', d['D_det_a_DELETE'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
