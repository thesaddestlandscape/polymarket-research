#!/usr/bin/env python3
"""rf5_gates.py -- puertas PURAS de RF5E-COMB-23NOV-v1 segun ADENDA_RF5_CRITERIOS_v2 (C1 cobertura/horas, C3 desenlace con peor caso) y tabla de suelo sucesora (iii). Sin IO pesado, sin red, 0 ordenes. Fail-closed: dato ausente = no valido.
evalua_c1: (i) con_tx/units >= 0,90 sobre TODAS las unidades (sin filtrar horas) en d-1,d,d+1; (ii) f_horas(d) >= 22/24 (bad_d); (iii) horas leidas de d-1 y d+1 (lista con sha) sanas. Fallo = INCOMPLETE terminal.
evalua_c3: por moneda ETH/SOL/XRP, lados mercado-lado CON RELLENO con desenlace oficial / lados con relleno, por lados y ponderado por EUR; >= 0,99 en las tres; si no PENDIENTE (terminal en D+3)."""
import os, json, hashlib
HV = os.path.dirname(os.path.abspath(__file__)) + '/'
COV_MIN = 0.90; HORAS_MIN = 22; C3_MIN = 0.99; COINS3 = ('ETH', 'SOL', 'XRP'); HL = HV + 'horas_leidas_d1.json'

def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()

def lee_horas_leidas(path=None):
    """{'dm1': [horas], 'dp1': [horas], 'sha256': sha del fichero}. Falta/ilegible => ValueError (fail-closed)."""
    p = path or HL; j = json.load(open(p)); a, b = j['d-1'], j['d+1']
    if not (isinstance(a, list) and isinstance(b, list) and all(isinstance(x, int) and 0 <= x <= 23 for x in a + b)): raise ValueError('horas_leidas_d1.json invalido')
    return dict(dm1=sorted(a), dp1=sorted(b), sha256=sha(p))

def f_horas(bad_hours): return (24 - len(set(bad_hours))) / 24.0

def evalua_c1(dias, cov, bad, hl, cov_min=COV_MIN, horas_min=HORAS_MIN):
    """dias = (d-1, d, d+1); cov = {x: dict(units, con_tx)} sobre TODAS las unidades; bad = {x: [horas malas]|None}; hl = lee_horas_leidas(). Devuelve dict(ok, motivos, detalle). Falta un dato => no ok (nunca 'bueno por defecto')."""
    dm1, d, dp1 = dias; mot = []; det = dict(cov={}, f_horas=None, horas_leidas=hl, horas_leidas_malas=[])
    for x in dias:
        c = cov.get(x)
        if not c or not c.get('units'): mot.append(f'(i) {x}: sin unidades/cobertura'); det['cov'][x] = None; continue
        v = c['con_tx'] / c['units']; det['cov'][x] = dict(units=c['units'], con_tx=c['con_tx'], cov=v)
        if v < cov_min: mot.append(f'(i) {x}: con_tx/units {v:.3f} < {cov_min} (sobre TODAS las unidades, sin filtrar horas)')
    if bad.get(d) is None: mot.append(f'(ii) {d}: sin bad_d')
    else:
        det['f_horas'] = f_horas(bad[d]); det['horas_malas_d'] = sorted(set(bad[d]))
        if 24 - len(set(bad[d])) < horas_min: mot.append(f'(ii) f_horas({d}) = {24 - len(set(bad[d]))}/24 < {horas_min}/24 (malas {sorted(set(bad[d]))})')
    for x, hs, nom in ((dm1, hl['dm1'], 'd-1'), (dp1, hl['dp1'], 'd+1')):
        if bad.get(x) is None: mot.append(f'(iii) {x}: sin bad_{nom}'); continue
        m = sorted(set(bad[x]) & set(hs)); det['horas_leidas_malas'] += [(x, h) for h in m]
        if m: mot.append(f'(iii) {nom} {x}: horas leidas por la simulacion no sanas {m}')
    return dict(ok=not mot, motivos=mot, detalle=det)

def evalua_c3(lados, coins=COINS3, umbral=C3_MIN):
    """lados: iterable de dict(coin, mid, k, coste, sin_res) = lados mercado-lado CON RELLENO (union de politicas; un lado una vez). Devuelve dict(estado 'OK'|'PENDIENTE', por_moneda, peor_caso).
    Por moneda: lados_relleno, resueltos, sin_resolver, coste_total, coste_sin_resolver, frac_lados, frac_eur. Una moneda sin lados con relleno = sin evidencia => PENDIENTE (fail-closed)."""
    seen = {}; 
    for r in lados:
        k = (str(r['mid']), int(r['k']))
        if k not in seen: seen[k] = dict(r)
    pm = {}
    for c in coins:
        L = [r for r in seen.values() if str(r['coin']).upper() == c]; n = len(L); sr = [r for r in L if r['sin_res']]; ct = float(sum(r['coste'] for r in L)); cs = float(sum(r['coste'] for r in sr))
        pm[c] = dict(lados_relleno=n, resueltos=n - len(sr), sin_resolver=len(sr), coste_total=ct, coste_sin_resolver=cs, frac_lados=((n - len(sr)) / n if n else None), frac_eur=((ct - cs) / ct if ct > 0 else None))
    ok = all(v['frac_lados'] is not None and v['frac_eur'] is not None and v['frac_lados'] >= umbral and v['frac_eur'] >= umbral for v in pm.values())
    return dict(estado=('OK' if ok else 'PENDIENTE'), por_moneda=pm, umbral=umbral, peor_caso='todo lado con relleno sin resolver cuenta como -coste (pnl = -coste en la simulacion con desenlace 0 de marcador)')

def terminal_c3(d, hoy, dmas):
    """el desenlace pendiente es terminal cuando hoy >= D+3 (ultimo intento = la pasada de D+3)."""
    return hoy >= dmas(d, 3)

# ------------------------------------------------------------------ tabla de suelo sucesora (iii)
def lee_tabla_suelo(cortes, base=None):
    """cortes['tabla_suelo_sucesora'] = {'ruta':..., 'sha256':...} o una LISTA de ellos (extensiones firmadas por el chief, una por tramo de dias; ruta relativa a HV o absoluta) -> (DataFrame concatenado, info[list]).
    None si no hay entrada; ValueError si falta un fichero o un sha no coincide (fail-closed). Un dia con filas en >1 tabla => ValueError (ambiguo)."""
    t = cortes.get('tabla_suelo_sucesora')
    if not t: return None, None
    import pandas as pd
    ts = t if isinstance(t, list) else [t]; dfs = []; infos = []
    for e in ts:
        p = e['ruta'] if os.path.isabs(e['ruta']) else (base or HV) + e['ruta']
        if not os.path.exists(p): raise ValueError('tabla suelo sucesora no existe: ' + p)
        if sha(p) != e['sha256']: raise ValueError('tabla suelo sucesora: sha != cortes (' + p + ')')
        dfs.append(pd.read_csv(p, dtype={'dia': str, 'coin': str})); infos.append(dict(ruta=p, sha256=e['sha256']))
    df = pd.concat(dfs, ignore_index=True)
    if df.duplicated(['dia', 'coin', 'w0_ms']).any(): raise ValueError('tabla suelo sucesora: ventanas duplicadas entre tablas')
    return df, infos

def suelo_dia(df, d, coins=COINS3, n_val=24, frac=0.5):
    """(iii): para el dia d y cada moneda, celdas clasificadas lo+hi+indet >= 24 y frac_lo >= 0,5; hi/indet cuentan como DATA_BLOCKED en el reparto. Dia sin filas en la tabla => 'suelo_pendiente' (no VALIDO). df None => suelo_pendiente.
    Devuelve dict(estado 'OK'|'suelo_pendiente'|'DATA_BLOCKED', por_moneda)."""
    if df is None: return dict(estado='suelo_pendiente', por_moneda={})
    X = df[df.dia == d]
    if not len(X): return dict(estado='suelo_pendiente', por_moneda={})
    pm = {}; ok = True
    for c in coins:
        g = X[X.coin.str.upper() == c]; vc = g.clase_estrato.value_counts().to_dict(); lo, hi, ind = int(vc.get('lo', 0)), int(vc.get('hi', 0)), int(vc.get('indet', 0)); ncl = lo + hi + ind
        v = ncl >= n_val and (lo / ncl if ncl else 0.0) >= frac; pm[c] = dict(n_lo=lo, n_hi=hi, n_indet=ind, n_clasificadas=ncl, frac_lo=(lo / ncl if ncl else None), valido=bool(v)); ok &= bool(v)
    return dict(estado=('OK' if ok else 'DATA_BLOCKED'), por_moneda=pm)
