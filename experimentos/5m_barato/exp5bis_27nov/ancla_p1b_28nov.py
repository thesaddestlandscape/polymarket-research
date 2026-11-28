#!/usr/bin/env python3
"""ancla_p1b_28nov.py -- ANCLA de mercado de la latencia alta/cancel de P1b/paquete_l, LEIDA DIRECTAMENTE de libro5_ms (28-Nov, ANEXO5 / REDTEAM_28nov D). Sustituye a lee_d / diagnostico_latencia_p1b `salto` (sin seq, sin lado, primer salto).
Solo LEE ficheros (ledger.jsonl de un run + libro5_ms_*.csv.gz). 0 red, 0 ordenes, no importa paquete_l ni ejecutor alguno. Pesado: 1 run = lectura secuencial de un gz de ~0,3-0,7 GB -> `nice -n 19 ionice -c3`, `ulimit -v 3000000`, nunca 22:00-02:45Z ni 06:00-09:00Z.

CRITERIO (REDTEAM_28nov A/D, cerrado antes de mirar resultados):
  * Filas `d` del libro5_ms (tipo,t_ms,token,lado,precio,tamano,recepcion,seq) con token = el de la intencion, LADO B, PRECIO 0,01. Se ordenan por `seq` (NO por t_ms/tamano/rx); delta = tamano_i - tamano_{i-1} del nivel, en CENTIMOS enteros
    (la 1.a fila de un token es snapshot, no delta). Filas duplicadas (token, seq) se cuentan y se descartan; inversiones seq-vs-orden del fichero se cuentan.
  * Firma de la orden: s = `size` de la fila `intencion` (en centimos). Alta = delta == +s; cancel = delta == -s. Run con firma de tamano (size 5,01-7,49 unico por intencion): coincidencia casi nula por azar. Run SIN firma (todas 5,00, runs anteriores al 28-Nov tarde): ruido +-5.
  * Ventana alta [t_envio-5 ms, t_ack+500 ms]. Ventana cancel [t_envio del PRIMER intento -5, max(ack|envio) de TODOS los intentos +500] (REINTENTOS de cancel incluidos). Exactamente 1 candidato => ANCLA; 0 => CENSURADA_0; >=2 => CENSURADA_MULTI.
    Una censurada NO se excluye: cuenta en el denominador y entra en Kaplan-Meier como observacion censurada por la derecha (0 candidatos: en t_ack+500-t_envio; multi: en el primer candidato, la cota inferior valida de T).
  * Reloj: t_ms = sello del canal de MERCADO (exchange); recepcion = rx local; t_envio/t_ack = reloj local (chrony). lat_ex = t_ms - t_envio ; lat_rx = recepcion - t_envio. Un efecto en [t_envio-5, t_envio) es `adelantado` (se cuenta y entra; jitter de reloj).
  * Clase de suelo POR ANCLA (lo/hi/mixta/indet): suelo_causal.clase_de_ventanas (sellado, solo import) sobre rx-ex de TODAS las filas `d` de los tokens de esa MONEDA en el run, 10 min causales anteriores a la recepcion del efecto (bins de 10 s completos). Sin filas suficientes => indet ('sin clase', no se inventa).
  * Aceptacion (REDTEAM A, declarada): censura <= 10 %/moneda; anclas vs todas en ack HTTP: |dp50| <= 10 ms, |dp90| <= 50 ms, Mann-Whitney p > 0,1.
SALIDA: JSON determinista (sin sellos de tiempo; ordenado) con sha256 de TODAS las entradas (ledger, prefijo de gz leido, flujo de filas usado), del codigo (este fichero y suelo_causal) y parametros. Dos ejecuciones => bytes identicos (`--verifica-repro`).
Uso: python3 -I ancla_p1b_28nov.py --run DIR [--run DIR ...] [--libro-dir D | --libro F ...] --out J [--verifica-repro]"""
import argparse
import bisect
import collections
import datetime as dt
import glob
import gzip
import hashlib
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIBRO_DIR = '/mnt/HC_Volume_106538179/libro5_ms'
SUELO_DIR = '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov'
MARGEN_INI_MS = 5
MARGEN_FIN_MS = 500
PARADA_MS = 120_000                    # se deja de leer 2 min despues del ultimo evento del run
PRECIO = 0.01
VENTANA_SUELO_S = 600
ACEPTA = dict(censura_max=0.10, dp50_max=10.0, dp90_max=50.0, mw_p_min=0.1)
VERSION = 'ancla_p1b_28nov_v1'


# ------------------------------------------------------------------------------------------------ utilidades
def sha256_fichero(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def cuantil(x, p):
    x = sorted(x)
    return None if not x else round(float(x[min(len(x) - 1, int(p * len(x)))]), 3)


def resumen(x):
    return dict(n=len(x), p10=cuantil(x, .1), p50=cuantil(x, .5), p90=cuantil(x, .9))


def km_cuantil(obs, p):
    """Kaplan-Meier. obs = [(t, evento_bool)]; cuantil p de T = menor t con S(t) <= 1-p; None si S no llega (censura excesiva). Empates: eventos antes que censuras en el mismo t."""
    obs = sorted(obs, key=lambda z: (z[0], not z[1]))
    n = len(obs)
    if n == 0:
        return None
    S, riesgo = 1.0, n
    i = 0
    while i < n:
        t = obs[i][0]
        d = c = 0
        while i < n and obs[i][0] == t:
            d += 1 if obs[i][1] else 0
            c += 0 if obs[i][1] else 1
            i += 1
        if d:
            S *= 1.0 - d / riesgo
            if S <= 1.0 - p + 1e-12:
                return round(float(t), 3)
        riesgo -= d + c
    return None


def mw_p(a, b):
    try:
        from scipy.stats import mannwhitneyu
        if len(a) < 3 or len(b) < 3:
            return None
        return float(mannwhitneyu(a, b, alternative='two-sided').pvalue)
    except Exception:
        return None


class _HashRaw(io.RawIOBase):
    """Fichero crudo que hashea EXACTAMENTE los bytes comprimidos entregados al lector (prefijo leido): reproducible aunque el gz siga creciendo."""
    def __init__(self, path):
        self.f = open(path, 'rb')
        self.h = hashlib.sha256()
        self.n = 0

    def readable(self):
        return True

    def readinto(self, b):
        d = self.f.read(len(b))
        self.h.update(d)
        self.n += len(d)
        b[:len(d)] = d
        return len(d)

    def close(self):
        self.f.close()
        super().close()


def lee_ledger(d):
    """-> dict(intenciones{oid:fila}, posts{oid:fila ok con t_send/t_ack}, cancels{oid:[filas por intento]}, corruptas)."""
    I, P, C, corr = {}, {}, collections.defaultdict(list), 0
    with open(os.path.join(d, 'ledger.jsonl')) as f:
        for ln in f:
            try:
                r = json.loads(ln)
            except ValueError:
                corr += 1
                continue
            k = r.get('k')
            if k == 'intencion':
                I[r['oid_local']] = r
            elif k == 'post' and r.get('t_send_ns') and r.get('t_ack_ns'):
                P[r['oid_local']] = r
            elif k == 'cancel' and r.get('t_send_ns'):
                C[r['oid']].append(r)
    for v in C.values():
        v.sort(key=lambda r: (r.get('intento') or 0, r['t_send_ns']))
    return dict(intenciones=I, posts=P, cancels=dict(C), corruptas=corr)


def localiza_ficheros(libro_dir, t0_ms, t1_ms):
    """Ficheros libro5_ms_FECHA_PID.csv.gz que cubren [t0,t1]: por cada dia tocado, los ficheros ordenados por su 1.a fila; se eligen los que empiezan <= t1 y cuyo SIGUIENTE empieza > t0 (el ultimo cubre hasta el infinito)."""
    dias = {dt.datetime.fromtimestamp(t / 1000, dt.timezone.utc).strftime('%Y-%m-%d') for t in (t0_ms, t1_ms)}
    ini = []
    for dia in sorted(dias):
        for p in sorted(glob.glob(os.path.join(libro_dir, f'libro5_ms_{dia}_*.csv.gz'))):
            try:
                with gzip.open(p, 'rt') as f:
                    next(f)
                    t = int(next(f).split(',', 2)[1])
                ini.append((t, p))
            except (OSError, EOFError, StopIteration, ValueError):
                continue
    ini.sort()
    out = []
    for i, (t, p) in enumerate(ini):
        sig = ini[i + 1][0] if i + 1 < len(ini) else float('inf')
        if t <= t1_ms and sig > t0_ms:
            out.append(p)
    return out


def lee_libro(paths, tokens, t_max_ms):
    """Lee los ficheros y devuelve (niveles{tok:[(seq,t_ms,size_cent,rx)]} del nivel B 0,01, todas{tok:[(rx,d)]} para la clase de suelo, info). Parada: t_ms > t_max_ms+PARADA_MS. gz truncado/en escritura => se lee lo que haya (EOFError)."""
    niveles = collections.defaultdict(list)
    todas = collections.defaultdict(list)
    info = dict(ficheros=[], filas_d_tokens=0, filas_nivel=0, duplicadas=0, inversiones_seq=0, filas_corruptas=0)
    hflujo = hashlib.sha256()
    vistos = set()
    for p in paths:
        raw = _HashRaw(p)
        fi = dict(fichero=os.path.basename(p), llego_a_eof=False, parada_por_tiempo=False)
        ult_seq = None
        try:
            with io.TextIOWrapper(gzip.GzipFile(fileobj=io.BufferedReader(raw)), encoding='utf-8', newline='') as f:
                next(f, None)
                for ln in f:
                    c = ln.rstrip('\n').split(',')
                    if len(c) < 8 or c[0] != 'd':
                        continue
                    try:
                        t_ms = int(c[1])
                    except ValueError:
                        info['filas_corruptas'] += 1
                        continue
                    if t_ms > t_max_ms + PARADA_MS:
                        fi['parada_por_tiempo'] = True
                        break
                    tok = c[2]
                    if tok not in tokens:
                        continue
                    try:
                        rx = int(c[6]); seq = int(c[7])
                    except ValueError:
                        info['filas_corruptas'] += 1
                        continue
                    info['filas_d_tokens'] += 1
                    todas[tok].append((rx, rx - t_ms))
                    if c[3] != 'B' or abs(float(c[4]) - PRECIO) > 1e-9:
                        continue
                    if (tok, seq) in vistos:
                        info['duplicadas'] += 1
                        continue
                    vistos.add((tok, seq))
                    if ult_seq is not None and seq < ult_seq:
                        info['inversiones_seq'] += 1
                    ult_seq = seq
                    cent = int(round(float(c[5]) * 100))
                    niveles[tok].append((seq, t_ms, cent, rx))
                    info['filas_nivel'] += 1
                    hflujo.update(f'{tok},{seq},{t_ms},{cent},{rx}\n'.encode())
                else:
                    fi['llego_a_eof'] = True
        except (EOFError, OSError):
            fi['llego_a_eof'] = True
        fi['bytes_leidos'] = raw.n
        fi['sha256_prefijo_leido'] = raw.h.hexdigest()
        raw.close()
        info['ficheros'].append(fi)
    info['sha256_flujo_filas'] = hflujo.hexdigest()
    for v in niveles.values():
        v.sort()                                                                        # por seq (no por t_ms)
    for v in todas.values():
        v.sort()
    return dict(niveles), dict(todas), info


def eventos_delta(niv):
    """{tok: [(t_ms, delta_centimos, rx, seq)]} en orden de seq. La 1.a fila es snapshot."""
    out = {}
    for tok, v in niv.items():
        ev = []
        for i in range(1, len(v)):
            d = v[i][2] - v[i - 1][2]
            if d:
                ev.append((v[i][1], d, v[i][3], v[i][0]))
        out[tok] = ev
    return out


def clase_suelo(todas_coin, t_rx_ms, SC):
    """lo/hi/mixta/indet con suelo_causal.clase_de_ventanas sobre rx-ex de las filas `d` de la moneda; solo bins de 10 s completos < t_rx (causal)."""
    if SC is None:
        return 'sin_clase', {}
    import numpy as np
    B = t_rx_ms // SC.BIN_MS
    lo1, lo2, hi = (B - 60) * SC.BIN_MS, (B - 30) * SC.BIN_MS, B * SC.BIN_MS
    rxs = todas_coin['rx']
    i0, i1, i2 = bisect.bisect_left(rxs, lo1), bisect.bisect_left(rxs, lo2), bisect.bisect_left(rxs, hi)

    def hist(a, b):
        d = np.asarray(todas_coin['d'][a:b], dtype=np.int64) - SC.D_LO
        d = d[(d >= 0) & (d < SC.ND)]
        return np.bincount(d, minlength=SC.ND).astype(np.int64)
    return SC.clase_de_ventanas(hist(i0, i1), hist(i1, i2))


def agrupa_coin(todas, coin_de):
    """{coin: {'rx':[...], 'd':[...]}} ordenado por rx."""
    tmp = collections.defaultdict(list)
    for tok, v in todas.items():
        tmp[coin_de.get(tok)].extend(v)
    out = {}
    for c, v in tmp.items():
        v.sort()
        out[c] = dict(rx=[z[0] for z in v], d=[z[1] for z in v])
    return out


def importa_suelo():
    try:
        if SUELO_DIR not in sys.path:
            sys.path.append(SUELO_DIR)
        import suelo_causal as SC
        return SC, sha256_fichero(os.path.join(SUELO_DIR, 'suelo_causal.py'))
    except Exception:
        return None, 'missing'


def candidatos(ev, ini, fin, delta):
    return [e for e in ev if ini <= e[0] <= fin and e[1] == delta]


def ancla_orden(oid, led, ev_tok, SC=None, todas_coin=None):
    """Filas ancla (alta y cancel) de UNA intencion. Devuelve lista de dicts (siempre 1 por tipo que tenga envio): estado ancla|censurada_0|censurada_multi."""
    i, p = led['intenciones'][oid], led['posts'].get(oid)
    out = []
    if not p:
        return out
    s = int(round(float(i['size']) * 100))
    ts, ta = p['t_send_ns'] / 1e6, p['t_ack_ns'] / 1e6
    tipos = [('alta', +s, ts, ta, ta - ts)]
    cs = led['cancels'].get(oid) or []
    if cs:
        s0 = cs[0]['t_send_ns'] / 1e6
        ult = max(((c.get('t_ack_ns') or c['t_send_ns']) / 1e6) for c in cs)
        ok = [c for c in cs if c.get('ok') and c.get('t_ack_ns')]
        tipos.append(('cancel', -s, s0, ult, ((ok[0]['t_ack_ns'] - ok[0]['t_send_ns']) / 1e6) if ok else None))
    for tipo, delta, t0, t_ack, http in tipos:
        ini, fin = t0 - MARGEN_INI_MS, t_ack + MARGEN_FIN_MS
        m = candidatos(ev_tok, ini, fin, delta)
        f = dict(oid=oid, coin=i['coin'], tok=i['tok'], tipo=tipo, size_cent=s, n_intentos=(len(cs) if tipo == 'cancel' else 1), ack_http_ms=(round(http, 3) if http is not None else None), n_candidatos=len(m))
        if len(m) == 1:
            t, d, rx, seq = m[0]
            f.update(estado='ancla', lat_ex_ms=round(t - t0, 3), lat_rx_ms=round(rx - t0, 3), lat_ex_menos_ack_ms=round(t - t_ack, 3), seq=seq, t_ex_ms=t, rx_ms=rx, adelantado=bool(t < t0))
            if tipo == 'cancel' and ok:
                f['lat_ex_desde_envio_ok_ms'] = round(t - ok[0]['t_send_ns'] / 1e6, 3)
            if SC is not None and todas_coin is not None:
                cl, dg = clase_suelo(todas_coin.get(i['coin'], dict(rx=[], d=[])), rx, SC)
                f['clase'] = cl
                f['suelo_p5'] = dg.get('p5')
            else:
                f['clase'] = 'sin_clase'
        elif len(m) == 0:
            f.update(estado='censurada_0', censura_ms=round(fin - t0, 3))
        else:
            f.update(estado='censurada_multi', censura_ms=round(min(z[0] for z in m) - t0, 3))
        out.append(f)
    return out


def agrega(filas, led, coin_de_oid):
    """Resumen por tipo y moneda (y TODAS): conteos, cuantiles de anclas (ex/rx), Kaplan-Meier, aceptacion, por clase de suelo."""
    res = {}
    todas_post = collections.defaultdict(list)
    for oid, p in led['posts'].items():
        c = coin_de_oid.get(oid)
        if c:
            for k in (c, 'TODAS'):
                todas_post[k].append((p['t_ack_ns'] - p['t_send_ns']) / 1e6)
    for tipo in ('alta', 'cancel'):
        for coin in ('BTC', 'ETH', 'SOL', 'XRP', 'TODAS'):
            F = [f for f in filas if f['tipo'] == tipo and (coin == 'TODAS' or f['coin'] == coin)]
            if not F:
                continue
            A = [f for f in F if f['estado'] == 'ancla']
            cen = [f for f in F if f['estado'] != 'ancla']
            obs = [(f['lat_ex_ms'], True) for f in A] + [(f['censura_ms'], False) for f in cen]
            r = dict(esperado=len(F), anclas=len(A), censuradas_0=sum(1 for f in F if f['estado'] == 'censurada_0'), censuradas_multi=sum(1 for f in F if f['estado'] == 'censurada_multi'),
                     adelantadas=sum(1 for f in A if f['adelantado']), tasa_censura=round(len(cen) / len(F), 4),
                     lat_ex=resumen([f['lat_ex_ms'] for f in A]), lat_rx=resumen([f['lat_rx_ms'] for f in A]),
                     km_ex=dict(p50=km_cuantil(obs, .5), p90=km_cuantil(obs, .9)),
                     por_clase={cl: dict(resumen([f['lat_ex_ms'] for f in A if f.get('clase') == cl]), lat_rx=resumen([f['lat_rx_ms'] for f in A if f.get('clase') == cl])) for cl in sorted({f.get('clase') for f in A})})
            if tipo == 'alta':
                ack_a = [f['ack_http_ms'] for f in A if f['ack_http_ms'] is not None]
                ack_t = todas_post.get(coin, [])
            else:
                ack_a = [f['ack_http_ms'] for f in A if f['ack_http_ms'] is not None]
                ack_t = [f['ack_http_ms'] for f in F if f['ack_http_ms'] is not None]
            p = mw_p(ack_a, ack_t)
            d50 = None if not ack_a or not ack_t else round(cuantil(ack_a, .5) - cuantil(ack_t, .5), 3)
            d90 = None if not ack_a or not ack_t else round(cuantil(ack_a, .9) - cuantil(ack_t, .9), 3)
            ok = (r['tasa_censura'] <= ACEPTA['censura_max'] and d50 is not None and abs(d50) <= ACEPTA['dp50_max'] and abs(d90) <= ACEPTA['dp90_max'] and p is not None and p > ACEPTA['mw_p_min'])
            r['aceptacion'] = dict(censura_ok=r['tasa_censura'] <= ACEPTA['censura_max'], dp50_ack=d50, dp90_ack=d90, mw_p=(None if p is None else round(p, 4)), n_ack_ancladas=len(ack_a), n_ack_todas=len(ack_t),
                                   ack_http_todas=resumen(ack_t), ack_http_ancladas=resumen(ack_a), cumple=bool(ok))
            res.setdefault(tipo, {})[coin] = r
    return res


def analiza_run(d, libro_dir=LIBRO_DIR, libro=None, SC=None):
    led = lee_ledger(d)
    I, P = led['intenciones'], led['posts']
    if not P:
        return dict(run=os.path.basename(d.rstrip('/')), estado='BLOCKED', motivo='ledger sin posts con t_send/t_ack')
    tiempos = [p['t_send_ns'] / 1e6 for p in P.values()] + [p['t_ack_ns'] / 1e6 for p in P.values()]
    for cs in led['cancels'].values():
        tiempos += [c['t_send_ns'] / 1e6 for c in cs] + [c['t_ack_ns'] / 1e6 for c in cs if c.get('t_ack_ns')]
    t0, t1 = min(tiempos), max(tiempos)
    toks = {i['tok'] for oid, i in I.items() if oid in P}
    paths = list(libro) if libro else localiza_ficheros(libro_dir, int(t0), int(t1))
    if not paths:
        return dict(run=os.path.basename(d.rstrip('/')), estado='BLOCKED', motivo='sin fichero libro5_ms que cubra el run', t0_ms=int(t0), t1_ms=int(t1))
    niv, todas, info = lee_libro(paths, toks, t1)
    ev = eventos_delta(niv)
    coin_de = {i['tok']: i['coin'] for i in I.values()}
    tc = agrupa_coin(todas, coin_de) if SC is not None else None
    filas = []
    for oid in sorted(P, key=lambda o: P[o]['t_send_ns']):
        if oid in I:
            filas += ancla_orden(oid, led, ev.get(I[oid]['tok'], []), SC, tc)
    coin_de_oid = {oid: I[oid]['coin'] for oid in P if oid in I}
    sizes = collections.Counter(round(float(I[o]['size']), 2) for o in P if o in I)
    return dict(run=os.path.basename(d.rstrip('/')), estado='COMPLETE',
                entradas=dict(ledger_sha256=sha256_fichero(os.path.join(d, 'ledger.jsonl')), ledger_filas_corruptas=led['corruptas'], t_primer_evento_ms=int(t0), t_ultimo_evento_ms=int(t1), libro=info),
                cobertura=dict(intenciones=len(I), posts_ok=len(P), cancels_con_reintentos=sum(1 for c in led['cancels'].values() if len(c) > 1), tokens=len(toks), firma_tamano=bool(len(sizes) > 1), sizes_distintos=len(sizes), sizes_repetidos=sum(1 for v in sizes.values() if v > 1)),
                resumen=agrega(filas, led, coin_de_oid), anclas=filas)


def analiza(runs, libro_dir=LIBRO_DIR, libro=None):
    SC, sc_sha = importa_suelo()
    R = [analiza_run(d, libro_dir, libro, SC) for d in runs]
    out = dict(version=VERSION, parametros=dict(margen_ini_ms=MARGEN_INI_MS, margen_fin_ms=MARGEN_FIN_MS, precio=PRECIO, lado='B', parada_ms=PARADA_MS, aceptacion=ACEPTA, ventana_suelo_s=VENTANA_SUELO_S),
               codigo=dict(ancla_p1b_28nov_sha256=sha256_fichero(os.path.abspath(__file__)), suelo_causal_sha256=sc_sha), runs=R)
    out['sha256_resultado'] = hashlib.sha256(json.dumps(out, sort_keys=True).encode()).hexdigest()
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument('--run', action='append', required=True)
    ap.add_argument('--libro-dir', default=LIBRO_DIR)
    ap.add_argument('--libro', action='append')
    ap.add_argument('--out', required=True)
    ap.add_argument('--verifica-repro', action='store_true', help='ejecuta DOS veces y exige bytes identicos')
    ns = ap.parse_args(argv)
    res = analiza(ns.run, ns.libro_dir, ns.libro)
    txt = json.dumps(res, indent=1, sort_keys=True)
    if ns.verifica_repro:
        txt2 = json.dumps(analiza(ns.run, ns.libro_dir, ns.libro), indent=1, sort_keys=True)
        if txt2 != txt:
            print('NO REPRODUCIBLE: dos ejecuciones difieren', file=sys.stderr)
            return 4
        print('REPRO OK: dos ejecuciones identicas', hashlib.sha256(txt.encode()).hexdigest())
    tmp = ns.out + '.tmp'
    with open(tmp, 'w') as f:
        f.write(txt)
    os.replace(tmp, ns.out)
    for r in res['runs']:
        print('==', r['run'], r['estado'], r.get('motivo', ''))
        for tipo, d in (r.get('resumen') or {}).items():
            for c, x in d.items():
                print(f"  {tipo:6s} {c:5s} esp={x['esperado']:3d} anclas={x['anclas']:3d} cens={x['tasa_censura']:.2f} ex p50/p90={x['lat_ex']['p50']}/{x['lat_ex']['p90']} rx p50={x['lat_rx']['p50']} KM p50={x['km_ex']['p50']} acept={x['aceptacion']['cumple']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
