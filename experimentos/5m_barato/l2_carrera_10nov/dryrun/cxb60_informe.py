#!/usr/bin/env python3
"""cxb60_informe.py [--out DIR] [--c59-dir DIR] [--desde YYYY-MM-DD] [--hasta YYYY-MM-DD] [--incluir-no-validos] [--semillas-boot N] -- INFORME de población completa del dry-run B-CXB60 (C5 de INTEGRIDAD_CXB60_DRYRUN_12nov.md).
Lee res_<D>.csv.gz (lo escribe cxb60_resolve.py), las filas 'mkt' de dec_<D>.csv.gz y coverage_<D>.json. Solo lectura; 0 ordenes; sin red. Escribe informe_cxb60.json y un resumen de texto en stdout.
DEFINICIONES (todas con el desenlace OFICIAL; missing != 0):
  colocacion = fila 'seg' (una orden virtual maker de rem_antes acciones a L); P(fill) = colocaciones con q>0 / colocaciones  (y por cantidad: sum q / sum rem_antes)
  EV INCONDICIONAL = sum(pnl) / sum(cost_pot)  con cost_pot = rem_antes*L de TODAS las colocaciones (con y sin relleno)  [indice por euro comprometido]
  EV | fill ponderado por EUR = sum(pnl)/sum(cost) sobre rellenos (cost = q*L)   [= metrica de las puertas G2 del prereg]    EV | fill por unidad = media de pnl_i/cost_i
  pnl por mercado = sum(pnl) / mercados(token) procesados (no colocado = 0, contrafactual: no se compra)
  Una (tok,L,var) con algun relleno SIN desenlace se excluye entera de numerador y denominador y se cuenta (supervivencia: se reporta la cobertura).
  Unidades de n efectivo: CIERRE (fin) y DIA UTC; IC90 = bootstrap de razon sum(pnl)/sum(cost) con remuestreo de clusters (semilla fija). Sin los 2 mejores dias; por moneda; por L.
  Dias validos = coverage_<D>.json::dia_valido (dia completo y las 3 monedas >= 0,95); el resto se lista y NO cuenta salvo --incluir-no-validos.
  Placebo: p = (1+#{EV_placebo >= EV_CXB60})/(1+S), EV|fill ponderado, S = semillas presentes (prereg: >=100; si S<100 se marca). Coste CPU del placebo: ver cpu_advance_us del heartbeat (pendiente de medir en real: se anota `coste_placebo`).
Las puertas se evaluan solo como DIAGNOSTICO: el prereg NO esta congelado y el informe no sustituye al validador estadistico."""
import os, sys, io, csv, json, glob, gzip, argparse, collections
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import cxb60_io as IO
DL = '/root/polymarket-research-datalogs/'; NUM = ['q', 'rem_antes', 'L', 'fin', 'canc']


def mkt_rows(path):
    """Solo las filas 'mkt' del dec_ (streaming de lineas; no materializa los seg/nof)."""
    txt, ok = IO.miembros_validos(path)
    for ln in txt.split('\n'):
        if ln.startswith('mkt,'): yield next(csv.reader([ln]))


def carga_dia(out, dia):
    """DataFrame de colocaciones resueltas del dia (solo columnas necesarias) + n de mercados procesados por moneda + contadores de exclusion."""
    p = out + f'res_{dia}.csv.gz'
    if not os.path.exists(p): return None
    df = pd.read_csv(p, usecols=['tok', 'coin', 'var', 'L', 'fin', 'q', 'rem_antes', 'pnl', 'cost', 'cost_pot', 'canc'], dtype={'tok': 'category', 'coin': 'category', 'var': 'category'})
    fill = df.q > 1e-9; sin = fill & df.pnl.isna(); mal = df[sin].groupby(['tok', 'L', 'var'], observed=True).size().index
    k = pd.MultiIndex.from_frame(df[['tok', 'L', 'var']]); excl = k.isin(mal); ex = dict(colocaciones_excluidas=int(excl.sum()), rellenos_sin_desenlace=int(sin.sum()), rellenos=int(fill.sum()))
    df = df[~excl].copy(); df['fill'] = (df.q > 1e-9).astype(int); df['dia'] = dia; df['pnl'] = df.pnl.fillna(0.0); df['cost'] = df.cost.fillna(0.0); df['var'] = df['var'].astype(str); df['coin'] = df['coin'].astype(str)
    nm = collections.Counter(); hf = collections.Counter()
    for r in mkt_rows(out + f'dec_{dia}.csv.gz'):
        nm[r[5]] += 1; hf[r[5]] += int('"hueco_feed":true' in r[21])
    return df, dict(mercados_procesados=dict(nm), mercados_con_hueco_feed=dict(hf)), ex


def agrega(df):
    return df.groupby(['dia', 'var', 'coin', 'L', 'fin'], as_index=False).agg(n_col=('fill', 'size'), n_fill=('fill', 'sum'), q=('q', 'sum'), rem=('rem_antes', 'sum'), pnl=('pnl', 'sum'), cost=('cost', 'sum'), cost_pot=('cost_pot', 'sum'))


def ratio(a, num, den): d = a[den].sum(); return float(a[num].sum() / d) if d > 0 else None


def boot(a, unidad, num='pnl', den='cost', B=2000, seed=12345):
    g = a.groupby(unidad)[[num, den]].sum(); x = g[num].values; y = g[den].values; n = len(x)
    if n < 3: return None
    r = np.random.default_rng(seed); idx = r.integers(0, n, (B, n)); sy = y[idx].sum(1); ok = sy > 0; e = x[idx].sum(1)[ok] / sy[ok]
    return [round(float(np.percentile(e, 5)), 4), round(float(np.percentile(e, 95)), 4)] if len(e) else None


def resumen_var(a, nmerc):
    f = a
    r = dict(n_colocaciones=int(f.n_col.sum()), n_rellenos=int(f.n_fill.sum()), P_fill_colocaciones=round(float(f.n_fill.sum() / max(f.n_col.sum(), 1)), 4), P_fill_cantidad=round(float(f.q.sum() / max(f.rem.sum(), 1e-9)), 4),
             ev_incondicional_por_eur=ratio(f, 'pnl', 'cost_pot'), ev_cond_fill_ponderado_eur=ratio(f, 'pnl', 'cost'), pnl_total=round(float(f.pnl.sum()), 3), coste_rellenos=round(float(f.cost.sum()), 3), coste_potencial=round(float(f.cost_pot.sum()), 3),
             pnl_por_mercado=round(float(f.pnl.sum() / max(nmerc, 1)), 5), mercados_procesados=int(nmerc))
    for k in ('ev_incondicional_por_eur', 'ev_cond_fill_ponderado_eur'): r[k] = round(r[k], 4) if r[k] is not None else None
    fl = f[f.cost > 0]; r['ev_cond_fill_por_unidad_media_filas'] = round(float((fl.pnl / fl.cost).mean()), 4) if len(fl) else None
    r['ic90_por_cierre'] = boot(f, 'fin'); r['ic90_por_dia'] = boot(f, 'dia'); r['n_cierres_con_relleno'] = int((f.groupby('fin').n_fill.sum() > 0).sum()); r['n_dias'] = int(f.dia.nunique())
    d = f.groupby('dia')[['pnl', 'cost']].sum().sort_values('pnl', ascending=False); r['dias_pnl'] = {k: round(float(v), 3) for k, v in d.pnl.items()}
    if len(d) > 2: rest = d.iloc[2:]; r['ev_cond_sin_2_mejores_dias'] = round(float(rest.pnl.sum() / rest.cost.sum()), 4) if rest.cost.sum() > 0 else None
    else: r['ev_cond_sin_2_mejores_dias'] = None
    pos = d.pnl[d.pnl > 0].sum(); r['max_dia_share_pnl_positivo'] = round(float(d.pnl.max() / pos), 3) if pos > 0 and d.pnl.max() > 0 else None
    return r


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--out', default=DL + 'cxb60_dryrun/'); ap.add_argument('--c59-dir', default=None); ap.add_argument('--desde', default='0000'); ap.add_argument('--hasta', default='9999'); ap.add_argument('--incluir-no-validos', action='store_true')
    ap.add_argument('--coins', default='ETH,SOL,XRP', help='poblacion del informe (primario ETH,SOL,XRP; la subvariante BTC se informa APARTE con --coins BTC --clave-valido dia_valido_btc)'); ap.add_argument('--clave-valido', default='dia_valido')
    ap.add_argument('--salida', default=None); a = ap.parse_args(); out = a.out.rstrip('/') + '/'; c59 = (a.c59_dir or out + 'c59').rstrip('/') + '/'
    dias_res = sorted(os.path.basename(f)[4:14] for f in glob.glob(out + 'res_*.csv.gz')); dias_res = [d for d in dias_res if a.desde <= d <= a.hasta]
    cov = {}; invalidos = {}
    for d in dias_res:
        try: cov[d] = json.load(open(out + f'coverage_{d}.json'))
        except (OSError, ValueError): cov[d] = None
        if cov[d] is None or not cov[d].get(a.clave_valido): invalidos[d] = None if cov[d] is None else dict(cobertura=cov[d]['cobertura'], por_moneda={c: v['cobertura'] for c, v in cov[d]['por_moneda'].items()}, dia_completo=cov[d]['dia_completo'])
    usar = [d for d in dias_res if a.incluir_no_validos or d not in invalidos]; frames = []; nmerc = {}; excl = collections.Counter(); hueco = collections.Counter()
    coins = set(a.coins.split(','))
    for d in usar:
        r = carga_dia(out, d)
        if r is None: continue
        df, m, ex = r; df = df[df['coin'].isin(coins)]; m = dict(m, mercados_procesados={c: n for c, n in m['mercados_procesados'].items() if c in coins}, mercados_con_hueco_feed={c: n for c, n in m['mercados_con_hueco_feed'].items() if c in coins}); frames.append(agrega(df[~df['var'].str.startswith('PLC60_')])); pl = df[df['var'].str.startswith('PLC60_')]; frames.append(pl.assign(fin=0, coin='*', L=0.0).pipe(agrega)) if len(pl) else None
        for c, n in m['mercados_procesados'].items(): nmerc[c] = nmerc.get(c, 0) + n
        hueco.update(m['mercados_con_hueco_feed']); excl.update(ex)
    inf = dict(dias_en_res=dias_res, dias_usados=usar, dias_no_validos_excluidos=invalidos if not a.incluir_no_validos else 'incluidos por --incluir-no-validos', exclusiones_desenlace=dict(excl), mercados_con_hueco_feed=dict(hueco), mercados_procesados_por_moneda=nmerc,
               sello_print='ws_ex-19-1 (primario)', cobertura_desenlace_rellenos=round(1 - excl['rellenos_sin_desenlace'] / max(excl['rellenos'], 1), 4) if excl['rellenos'] else None, veredicto_gates='DIAGNOSTICO_NO_CONGELADO (el prereg es borrador; este informe no declara PASS)')
    if not frames: inf['estado'] = 'SIN_DATOS'; print(json.dumps(inf, indent=1)); return
    A = pd.concat(frames, ignore_index=True); tot_m = sum(nmerc.values()); variantes = {}
    base = A[~A['var'].str.startswith('PLC60_')]
    for v, g in base.groupby('var'): variantes[v] = resumen_var(g, tot_m)
    por_moneda = {}; por_L = {}
    for v in ('CXB60', 'GEO1', 'G0'):
        g = base[base['var'] == v]
        if not len(g): continue
        por_moneda[v] = {c: dict(coste=round(float(x.cost.sum()), 2), pnl=round(float(x.pnl.sum()), 3), ev_cond=round(ratio(x, 'pnl', 'cost'), 4) if x.cost.sum() > 0 else None, n_rellenos=int(x.n_fill.sum()), mercados=nmerc.get(c, 0), ev_incond=round(ratio(x, 'pnl', 'cost_pot'), 4) if x.cost_pot.sum() > 0 else None) for c, x in g.groupby('coin')}
        por_L[v] = {str(L): dict(coste=round(float(x.cost.sum()), 2), pnl=round(float(x.pnl.sum()), 3), ev_cond=round(ratio(x, 'pnl', 'cost'), 4) if x.cost.sum() > 0 else None, n_rellenos=int(x.n_fill.sum())) for L, x in g.groupby('L')}
    inf.update(variantes=variantes, por_moneda=por_moneda, por_L=por_L, poblacion=sorted(coins), clave_valido=a.clave_valido)
    # ---- dosis-respuesta en l (descriptiva, NO puerta salvo G8): EV ponderado por EUR, IC90 por dias, delta pnl vs GEO1 por dia, y tendencia (Spearman sobre l nominal; CXBEMP aparte)
    dr = {}; g1 = base[base['var'] == 'GEO1'].groupby('dia').pnl.sum()
    for v in ('CXB35', 'CXB45', 'CXB60', 'CXB100', 'CXB150', 'CXBEMP'):
        g = base[base['var'] == v]
        if not len(g): continue
        dd = (g.groupby('dia').pnl.sum() - g1).dropna(); r_ = np.random.default_rng(12345); lo_ = float(np.percentile(dd.values[r_.integers(0, len(dd), (2000, len(dd)))].mean(1), 5)) if len(dd) >= 3 else None
        dr[v] = dict(l_ms=int(v[3:]) if v[3:].isdigit() else 'emp(3+pool p50 41, p90 96)', n_rellenos=int(g.n_fill.sum()), ev_cond_pond=round(ratio(g, 'pnl', 'cost'), 4) if g.cost.sum() > 0 else None, ic90_dias=boot(g, 'dia'), delta_pnl_dia_vs_GEO1=round(float(dd.mean()), 4) if len(dd) else None, delta_ic90_inferior=round(lo_, 4) if lo_ is not None else None)
    nom = [(v_['l_ms'], v_['ev_cond_pond']) for v_ in dr.values() if isinstance(v_['l_ms'], int) and v_['ev_cond_pond'] is not None]
    if len(nom) >= 4:
        xs = pd.Series([x for x, _ in nom]).rank().values; ys = pd.Series([y for _, y in nom]).rank().values; dr['_tendencia_spearman_ev_vs_l'] = dict(rho=round(float(np.corrcoef(xs, ys)[0, 1]), 3), n_puntos=len(nom), nota='5 puntos: descriptivo; EV baja al subir l si rho<0')
    inf['dosis_respuesta_l'] = dr
    # ---- placebo (placebo agregado por var: coin='*', fin=0)
    pl = A[A['var'].str.startswith('PLC60_')]; seeds = {v: ratio(g, 'pnl', 'cost') for v, g in pl.groupby('var')}; prim = variantes.get('CXB60', {}).get('ev_cond_fill_ponderado_eur')
    if seeds and prim is not None:
        S = len(seeds); n_ge = sum(1 for e in seeds.values() if e is not None and e >= prim); ev = np.array([e for e in seeds.values() if e is not None])
        inf['placebo'] = dict(semillas=S, ev_cond_placebo_media=round(float(ev.mean()), 4), ev_cond_placebo_p5_p95=[round(float(np.percentile(ev, 5)), 4), round(float(np.percentile(ev, 95)), 4)], p_valor=round((1 + n_ge) / (1 + S), 4), semillas_suficientes_prereg=bool(S >= 100), coste_placebo='ver cpu_advance_us de heartbeat.json (medido en el replay: CXB60_CONDICIONES_L_CALMA_12nov.md)')
    # ---- puertas (diagnostico)
    c = variantes.get('CXB60'); gt = {}
    if c:
        gt['G1_n40_y_10_dias'] = dict(n_rellenos=c['n_rellenos'], dias=c['n_dias'], ok=bool(c['n_rellenos'] >= 40 and c['n_dias'] >= 10))
        gt['G2_ev_ponderado_ic90_dias_y_cierres_gt0'] = dict(ev=c['ev_cond_fill_ponderado_eur'], ic90_dias=c['ic90_por_dia'], ic90_cierres=c['ic90_por_cierre'], ok=bool(c['ic90_por_dia'] and c['ic90_por_dia'][0] > 0 and c['ic90_por_cierre'] and c['ic90_por_cierre'][0] > 0))
        g0 = base[base['var'] == 'GEO1']; c0 = base[base['var'] == 'CXB60']
        if len(g0):
            d = (c0.groupby('dia').pnl.sum() - g0.groupby('dia').pnl.sum()).dropna(); r = np.random.default_rng(12345); idx = r.integers(0, len(d), (2000, len(d))) if len(d) else None
            lo = float(np.percentile(d.values[idx].mean(1), 5)) if len(d) >= 3 else None; gt['G3_incremental_vs_GEO1_dias'] = dict(delta_pnl_medio_dia=round(float(d.mean()), 4) if len(d) else None, ic90_inferior=round(lo, 4) if lo is not None else None, ok=bool(lo is not None and lo > 0))
        gt['G4_ev_sin_2_mejores_dias'] = dict(ev=c['ev_cond_sin_2_mejores_dias'], ok=bool(c['ev_cond_sin_2_mejores_dias'] is not None and c['ev_cond_sin_2_mejores_dias'] > 0))
        if 'placebo' in inf: gt['G5_placebo'] = dict(p=inf['placebo']['p_valor'], semillas=inf['placebo']['semillas'], ok=bool(inf['placebo']['p_valor'] <= 0.05 and inf['placebo']['semillas'] >= 20))
        pm = por_moneda.get('CXB60', {}); ct = sum(v['coste'] for v in pm.values()) or 1; gt['G6_concentracion'] = dict(max_moneda_share_coste=round(max((v['coste'] for v in pm.values()), default=0) / ct, 3), max_dia_share_pnl_positivo=c['max_dia_share_pnl_positivo'],
                                                                                         ok=bool(max((v['coste'] for v in pm.values()), default=0) / ct <= 0.60 and (c['max_dia_share_pnl_positivo'] is None or c['max_dia_share_pnl_positivo'] <= 0.25)))
        if os.path.isdir(c59):
            f59 = []
            for d in usar:
                r = carga_dia(c59, d)
                if r is not None: f59.append(agrega(r[0][r[0]['coin'].isin(coins)]))
            if f59:
                x = pd.concat(f59); x = x[x['var'] == 'CXB60']; e59 = ratio(x, 'pnl', 'cost'); gt['G7_sello_cinta_pesimista_c59'] = dict(ev_c59=round(e59, 4) if e59 is not None else None, ev_c19=c['ev_cond_fill_ponderado_eur'], n_rellenos_c59=int(x.n_fill.sum()), mismo_signo=bool(e59 is not None and c['ev_cond_fill_ponderado_eur'] is not None and np.sign(e59) == np.sign(c['ev_cond_fill_ponderado_eur'])))
                inf['c59'] = {v: round(ratio(g, 'pnl', 'cost'), 4) if g.cost.sum() > 0 else None for v, g in pd.concat(f59).groupby('var')}
        c1 = variantes.get('CXB100'); gt['G8_ev_CXB100_no_peor_que_-0.05'] = dict(ev=c1['ev_cond_fill_ponderado_eur'] if c1 else None, ok=bool(c1 and c1['ev_cond_fill_ponderado_eur'] is not None and c1['ev_cond_fill_ponderado_eur'] >= -0.05))
    inf['puertas_diagnostico'] = gt; salida = a.salida or out + ('informe_cxb60.json' if a.coins == 'ETH,SOL,XRP' else 'informe_cxb60_' + a.coins.replace(',', '_') + '.json'); json.dump(inf, open(salida, 'w'), indent=1, default=str)
    print(f'INFORME dias usados {len(usar)} (no validos {len(invalidos)}), mercados procesados {tot_m}, cobertura desenlace {inf["cobertura_desenlace_rellenos"]}')
    for v in ('G0', 'GEO1', 'CXB35', 'CXB45', 'CXB60', 'CXB100', 'CXB150', 'CXBEMP'):
        if v in variantes: x = variantes[v]; print(f'  {v:7s} col {x["n_colocaciones"]:6d} fills {x["n_rellenos"]:5d} P(fill) {x["P_fill_colocaciones"]:.3f} EV_incond {x["ev_incondicional_por_eur"]} EV|fill_pond {x["ev_cond_fill_ponderado_eur"]} IC90 dias {x["ic90_por_dia"]} cierres {x["ic90_por_cierre"]} sin2mejores {x["ev_cond_sin_2_mejores_dias"]}')
    print('  salida', salida)


if __name__ == '__main__': main()
