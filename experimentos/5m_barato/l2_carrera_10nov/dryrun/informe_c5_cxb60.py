#!/usr/bin/env python3
"""informe_c5_cxb60.py [--out DIR] [--coins ETH,SOL,XRP] [--desde D] [--hasta D] [--clave-valido dia_valido] [--salida F.json] -- C5 de INTEGRIDAD_CXB60_DRYRUN_12nov.md. SCRIPT NUEVO: cxb60_informe.py/cxb60_resolve.py estan
congelados y NO se tocan; este lee res_<D>.csv.gz (lo regenera cxb60_resolve.py), las filas 'mkt' de dec_<D>.csv.gz y coverage_<D>.json. Solo lectura; 0 ordenes; sin red. Diferencias con cxb60_informe.py:
  * NO descarta dias con cobertura <0,95 ni rellenos sin desenlace: los reporta (dia x moneda) y da el EV en dos vistas: TODOS los dias y SOLO dias validos (coverage_<D>[clave_valido]).
  * rellenos sin desenlace: conteo, coste y COTAS (peor: pierden todo el coste; mejor: ganan) ademas del EV sobre los resueltos (missing != 0: no entran como 0 en el numerador resuelto).
DEFINICIONES (desenlace OFICIAL; pnl = q*(gana-L)+rebate 0,2*0,07*L*(1-L) como el resolvedor; cost = q*L; cost_pot = rem_antes*L):
  colocacion virtual = fila `seg` (con o sin relleno).  mercado-lado = token (`tok`) procesado = fila `mkt` del dec_.  NO colocado/sin relleno = pnl 0 (contrafactual: no se compra).
  EV_incond_por_colocacion = sum(pnl_resuelto)/n_colocaciones (EUR por colocacion virtual);  EV_incond_por_mercado_lado = sum(pnl_resuelto)/n_mercados_lado procesados (EUR por mercado-lado, los sin colocacion cuentan 0);
  EV_incond_por_eur = sum(pnl)/sum(cost_pot);  P_fill = rellenos/colocaciones (y por cantidad); EV|fill ponderado por EUR = sum(pnl)/sum(cost) sobre rellenos RESUELTOS (la metrica correcta, trampa 17-Oct); por unidad = media pnl_i/cost_i.
  n efectivo = cierres (campo fin) con relleno y dias con relleno (varias monedas en un cierre = una apuesta); IC90 = bootstrap de la razon con clusters por cierre / por dia (semilla fija). Sin los 2 mejores dias (por pnl).
  Placebo PLC60_k: EV|fill ponderado de cada semilla; p = (1+#{placebo>=CXB60})/(1+S).
Es DIAGNOSTICO: el prereg lo congela el chief; esto no declara PASS ni rentabilidad."""
import os, sys, csv, json, glob, argparse, collections
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import cxb60_io as IO
REB = 0.2 * 0.07
DL = '/root/polymarket-research-datalogs/'
COLS = ['tok', 'coin', 'var', 'L', 'seg', 'fin', 'q', 'rem_antes', 'pnl', 'cost', 'cost_pot']


def n_mercados_lado(dec_path):
    """{coin: n_tokens procesados} y {coin: n con hueco_feed} desde las filas 'mkt' del dec_ (tolera cola gz truncada)."""
    txt, _ = IO.miembros_validos(dec_path); nm = collections.Counter(); hf = collections.Counter(); toks = set()
    for ln in txt.split('\n'):
        if not ln.startswith('mkt,'): continue
        r = next(csv.reader([ln])); k = (r[3], r[5])
        if k in toks: continue
        toks.add(k); nm[r[5]] += 1; hf[r[5]] += int('"hueco_feed":true' in r[21] or '"hueco_feed": true' in r[21])
    return dict(nm), dict(hf)


def carga_res(path):
    """DataFrame de colocaciones del dia. Cuenta duplicados (tok,L,var,seg) y los descarta (se queda el primero), como el resolvedor."""
    df = pd.read_csv(path, usecols=COLS, dtype={'tok': str, 'coin': 'category', 'var': 'category'}); n0 = len(df)
    df = df.drop_duplicates(['tok', 'L', 'var', 'seg'], keep='first'); return df, n0 - len(df)


def boot(x, y, cl, B=2000, seed=12345):
    """IC90 bootstrap de sum(x)/sum(y) remuestreando clusters `cl`. None si <3 clusters."""
    g = pd.DataFrame(dict(x=x, y=y, c=cl)).groupby('c')[['x', 'y']].sum(); a = g.x.values; b = g.y.values; n = len(a)
    if n < 3: return None
    idx = np.random.default_rng(seed).integers(0, n, (B, n)); sy = b[idx].sum(1); ok = sy > 0
    e = a[idx].sum(1)[ok] / sy[ok]
    return [round(float(np.percentile(e, 5)), 4), round(float(np.percentile(e, 95)), 4)] if len(e) else None


def resumen_var(f, nmerc):
    """f: filas seg (todas las colocaciones) de UNA variante, ya con columna dia. Devuelve dict de metricas C5."""
    col = len(f); fill = f.q > 1e-9; res = f[fill & f.pnl.notna()]; sin = f[fill & f.pnl.isna()]
    noresueltas_nofill = int((~fill & f.pnl.isna()).sum())          # colocaciones sin relleno y sin desenlace: pnl 0 por definicion (no hay compra), se cuentan aparte
    pnl = float(res.pnl.sum()); cost = float(res.cost.sum()); pot = float(f.cost_pot.sum())
    r = dict(n_colocaciones=col, n_rellenos=int(fill.sum()), n_rellenos_resueltos=len(res), rellenos_sin_desenlace=len(sin), coste_rellenos_sin_desenlace=round(float((sin.q * sin.L).sum()), 3),
             cobertura_resolucion_rellenos=round(len(res) / max(int(fill.sum()), 1), 4) if fill.sum() else None, colocaciones_nofill_sin_desenlace=noresueltas_nofill,
             P_fill_colocaciones=round(float(fill.sum() / max(col, 1)), 4), P_fill_cantidad=round(float(f.q.sum() / max(f.rem_antes.sum(), 1e-9)), 4),
             pnl_total=round(pnl, 3), coste_rellenos=round(cost, 3), coste_potencial=round(pot, 3), mercados_lado_procesados=int(nmerc),
             EV_incond_por_colocacion_eur=round(pnl / col, 6) if col else None, EV_incond_por_mercado_lado_eur=round(pnl / nmerc, 6) if nmerc else None, EV_incond_por_eur_comprometido=round(pnl / pot, 4) if pot > 0 else None,
             EV_cond_fill_ponderado_eur=round(pnl / cost, 4) if cost > 0 else None, EV_cond_fill_por_unidad_media=round(float((res.pnl / res.cost).mean()), 4) if len(res) and (res.cost > 0).all() else None)
    if len(sin):                                                    # cotas: los sin desenlace pierden todo / ganan todo (informativo, NO se mezclan en el EV resuelto)
        cs = float((sin.q * sin.L).sum()); reb = float((sin.q * REB * sin.L * (1 - sin.L)).sum()); peor = pnl - cs + reb; mejor = pnl + float((sin.q * (1 - sin.L)).sum()) + reb
        r['EV_cond_fill_cota_peor'] = round(peor / (cost + cs), 4); r['EV_cond_fill_cota_mejor'] = round(mejor / (cost + cs), 4)
    r['n_efectivo'] = dict(cierres_con_relleno=int(res.fin.nunique()), dias_con_relleno=int(res.dia.nunique()), mercados_lado_con_relleno=int(res.tok.nunique()), dias_en_poblacion=int(f.dia.nunique()))
    r['ic90_cond_por_cierre'] = boot(res.pnl.values, res.cost.values, res.fin.values); r['ic90_cond_por_dia'] = boot(res.pnl.values, res.cost.values, res.dia.values)
    d = res.groupby('dia')[['pnl', 'cost']].sum().sort_values('pnl', ascending=False); r['pnl_por_dia'] = {k: round(float(v), 3) for k, v in d.pnl.items()}
    if len(d) > 2:
        rest = d.iloc[2:]; r['EV_cond_sin_2_mejores_dias'] = round(float(rest.pnl.sum() / rest.cost.sum()), 4) if rest.cost.sum() > 0 else None
        dias_rest = set(rest.index); fr = f[f.dia.isin(dias_rest)]; r['EV_incond_por_eur_sin_2_mejores_dias'] = round(float(fr[fr.q > 1e-9].pnl.sum() / fr.cost_pot.sum()), 4) if fr.cost_pot.sum() > 0 else None
    else: r['EV_cond_sin_2_mejores_dias'] = None; r['EV_incond_por_eur_sin_2_mejores_dias'] = None; r['nota_2_mejores_dias'] = f'solo {len(d)} dia(s) con relleno resuelto: no aplicable'
    # por unidad mercado-lado (una observacion por token; trampa 17-Oct): razon por token, media y ponderada
    t = res.groupby('tok')[['pnl', 'cost']].sum(); r['por_mercado_lado'] = dict(n=len(t), EV_ponderado_eur=round(float(t.pnl.sum() / t.cost.sum()), 4) if len(t) and t.cost.sum() > 0 else None, EV_media_de_razones=round(float((t.pnl / t.cost).mean()), 4) if len(t) else None)
    return r


def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument('--out', default=DL + 'cxb60_dryrun/'); ap.add_argument('--coins', default='ETH,SOL,XRP'); ap.add_argument('--desde', default='0000'); ap.add_argument('--hasta', default='9999')
    ap.add_argument('--clave-valido', default='dia_valido', help="dia_valido (ETH+SOL+XRP) | dia_valido_btc | dia_valido_4monedas"); ap.add_argument('--salida', default=None); a = ap.parse_args(argv)
    out = a.out.rstrip('/') + '/'; coins = a.coins.split(','); dias = sorted(os.path.basename(f)[4:14] for f in glob.glob(out + 'res_*.csv.gz')); dias = [d for d in dias if a.desde <= d <= a.hasta]
    man = {}
    try: man = json.load(open(out + 'run_manifest.json'))
    except (OSError, ValueError): pass
    inf = dict(job='informe_c5_cxb60', out=out, poblacion=coins, clave_valido=a.clave_valido, sello_print=man.get('sello_print', 'desconocido'), run_manifest_status=man.get('status'), dias_con_res=dias,
               veredicto='DIAGNOSTICO (no declara PASS ni rentabilidad; el prereg lo congela el chief)')
    cov_dia = {}; frames = {'todos': [], 'validos': []}; nm_tot = {'todos': collections.Counter(), 'validos': collections.Counter()}; dup = 0; hueco = collections.Counter(); sin_desen = {}
    for d in dias:
        try: cv = json.load(open(out + f'coverage_{d}.json'))
        except (OSError, ValueError): cv = None
        valido = bool(cv and cv.get(a.clave_valido)); cov_dia[d] = dict(valido=valido, cobertura=cv.get('cobertura') if cv else None, dia_completo=cv.get('dia_completo') if cv else None,
                                                                        por_moneda={c: dict(cobertura=v.get('cobertura'), ok_095=v.get('ok_095'), procesados=v.get('procesados'), esperados=v.get('esperados_teoricos')) for c, v in (cv or {}).get('por_moneda', {}).items() if c in coins},
                                                                        motivo_no_valido=None if valido else ('sin coverage_<D>.json' if cv is None else [c for c, v in cv['por_moneda'].items() if c in coins and not v.get('ok_095')] or ('dia incompleto' if not cv.get('dia_completo') else 'otro')))
        df, nd = carga_res(out + f'res_{d}.csv.gz'); dup += nd; df = df[df.coin.isin(coins)].copy(); df['dia'] = d; df['var'] = df['var'].astype(str); df['coin'] = df['coin'].astype(str)
        nm, hf = n_mercados_lado(out + f'dec_{d}.csv.gz'); nm = {c: n for c, n in nm.items() if c in coins}; hueco.update({c: n for c, n in hf.items() if c in coins})
        f_ = (df.q > 1e-9); sd = df[f_ & df.pnl.isna()]; sin_desen[d] = dict(rellenos=int(f_.sum()), sin_desenlace=len(sd), por_moneda=sd.coin.value_counts().to_dict())
        cov_dia[d]['mercados_lado_procesados'] = nm; cov_dia[d]['rellenos_sin_desenlace'] = len(sd)
        for k in ('todos',) + (('validos',) if valido else ()): frames[k].append(df); nm_tot[k].update(nm)
    inf.update(cobertura_por_dia_y_moneda=cov_dia, rellenos_sin_desenlace_por_dia=sin_desen, duplicados_descartados=dup, mercados_con_hueco_feed=dict(hueco),
               dias_validos=[d for d in dias if cov_dia[d]['valido']], dias_no_validos=[d for d in dias if not cov_dia[d]['valido']])
    for k in ('todos', 'validos'):
        if not frames[k]: inf[k] = dict(estado='SIN_DATOS'); continue
        A = pd.concat(frames[k], ignore_index=True); nmerc = sum(nm_tot[k].values()); base = A[~A['var'].str.startswith('PLC60_')]; v = {}
        for var, g in base.groupby('var'): v[var] = resumen_var(g, nmerc)
        pl = A[A['var'].str.startswith('PLC60_')]; pe = {}
        for var, g in pl.groupby('var'):
            rs = g[(g.q > 1e-9) & g.pnl.notna()]; pe[var] = float(rs.pnl.sum() / rs.cost.sum()) if len(rs) and rs.cost.sum() > 0 else None
        pe = {x: y for x, y in pe.items() if y is not None}; ref = v.get('CXB60', {}).get('EV_cond_fill_ponderado_eur')
        plc = dict(S=len(pe), S_minimo_prereg=100, ev_cond_pond_p5_p50_p95=[round(float(np.percentile(list(pe.values()), q)), 4) for q in (5, 50, 95)] if pe else None,
                   p_valor=round((1 + sum(1 for y in pe.values() if ref is not None and y >= ref)) / (1 + len(pe)), 4) if ref is not None and pe else None)
        por_coin = {}
        for var in ('CXB60', 'GEO1', 'G0'):
            g = base[base['var'] == var]
            por_coin[var] = {c: dict(n_colocaciones=len(x), n_rellenos=int((x.q > 1e-9).sum()), pnl=round(float(x[(x.q > 1e-9)].pnl.sum()), 3), coste=round(float(x[(x.q > 1e-9) & x.pnl.notna()].cost.sum()), 3), mercados_lado=int(nm_tot[k].get(c, 0))) for c, x in g.groupby('coin')}
        inf[k] = dict(mercados_lado_procesados=int(nmerc), dias=sorted(A.dia.unique().tolist()), variantes=v, por_moneda=por_coin, placebo_PLC60=plc)
    s = json.dumps(inf, indent=1, default=str)
    if a.salida: open(a.salida + '.tmp', 'w').write(s); os.replace(a.salida + '.tmp', a.salida)
    print(s); return 0


if __name__ == '__main__': sys.exit(main())
