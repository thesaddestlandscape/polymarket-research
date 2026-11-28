#!/usr/bin/env python3
"""fn5bis_core.py (27-Nov, engineer 5m barato; CONTRATO_5BIS_EXP5B_27nov.md §1a/§1b). Funciones PURAS/ligeras (sin motor): cadena on-chain + libro5_tx + clasificacion FN/FP + calibracion P(relleno). 0 ordenes, 0 red.
Definiciones (todas declaradas en el informe):
 - fila de MAKER ajeno = tipo F con side=0 (maker BUY), token_id del token de la orden, cuyo order_hash NO es el de la orden del tomador (hash de una fila M) y ni maker ni taker llevan prefijo de wallet propia.
   (la fila F del tomador lleva taker=exchange y el mismo hash que su fila M: se excluye).  Precio = maker_amt/taker_amt (USDC/acciones), cantidad = taker_amt (acciones).
 - reloj del evento = recepcion del print de libro5_tx por tx (min sobre fichas); bloque NUNCA. Ventana nominal [t_arr, t_end]; borde = +-300 ms.
 - 'duro' = precio < L-tol (el tomador barrio TODO el nivel L, incluida nuestra orden); 'nivel' = |precio-L|<=tol (depende de la cola: ambiguo); tol=0,0006.
 - tipo de casado (por tx, fila M): misma ficha (M en el token de la orden, SELL) | cruzado (M en la ficha complementaria, BUY) | otro."""
import os, gzip, glob, csv, collections
import numpy as np, pandas as pd
ONCH_DIRS = ('/root/polymarket-research-datalogs/', '/mnt/HC_Volume_106538179/datalogs_auto/', '/mnt/HC_Volume_106538179/protegido_forward_11nov/')
TXD = '/mnt/HC_Volume_106538179/libro5_tx/'
PROPIAS = ('0x659a40ff9920febc5a66836213040924343d297f',)          # wallet dedicada de B (docs). Prefijos 0x659a / 0xb6ed: el piloto 25-Nov los trata como propios (wallets de pruebas): se EXCLUYEN de la referencia y se cuentan.
PREF_PROPIOS = ('0x659a', '0xb6ed')
TOL = 0.0006; BORDE = 300; OFFSET = 100


def ruta_onchain(dia):
    for d in ONCH_DIRS:
        p = d + f'onchain_fills_{dia}.csv.gz'
        if os.path.exists(p): return p
    raise FileNotFoundError(f'sin onchain_fills_{dia}')


def carga_cadena(dia, tokens, ruta=None, rutas=None):
    """Dos pasadas por la cadena del dia (V2 + V3 si existe; ANEXO_V2 §1: se exigen ambas desde 23-Nov, via cadena_v2v3.rutas_cadena). RAM acotada: solo filas de los tokens de las ordenes y las M de SUS tx.
    -> (E: DataFrame filas de makers ajenos [tx, li, token, price, qty, maker], Mk: dict tx -> [(token, side)] del tomador, cont: contadores)."""
    import cadena_v2v3 as CV
    tokens = set(tokens); cont = collections.Counter(); Fch = []
    rutas = [('v2', ruta)] if ruta else (rutas or CV.rutas_cadena(dia))
    cols = ['tipo', 'tx', 'log_index', 'order_hash', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt']
    for ver, rt in rutas:
        for ch in pd.read_csv(rt, usecols=cols, dtype=str, chunksize=400000):
            ch['maker'] = ch.maker.fillna('').str.lower(); ch['taker'] = ch.taker.fillna('').str.lower()
            cont['M_filas'] += int((ch.tipo == 'M').sum())
            f = ch[ch.tipo == 'F']; cont['F_filas'] += len(f); cont['F_filas_' + ver] += len(f)
            propias = f.maker.str.startswith(PREF_PROPIOS) | f.taker.str.startswith(PREF_PROPIOS)
            cont['F_filas_con_prefijo_propio'] += int(propias.sum()); cont['F_maker_wallet_B_exacta'] += int((f.maker == PROPIAS[0]).sum())
            g = f[(f.side == '0') & f.token_id.isin(tokens)]
            if len(g): Fch.append(g.assign(propia=propias.loc[g.index], ver=ver))
    F = pd.concat(Fch, ignore_index=True) if Fch else pd.DataFrame(columns=cols + ['propia', 'ver'])
    cont['F_maker_BUY_en_tokens_de_ordenes'] = len(F)
    txs = set(F.tx); Mh = set(); Mk = collections.defaultdict(list)
    for ver, rt in rutas:
        for ch in pd.read_csv(rt, usecols=cols, dtype=str, chunksize=400000):
            m = ch[(ch.tipo == 'M') & ch.tx.isin(txs)]
            Mh.update(m.order_hash.tolist())
            for tx, tk, sd in zip(m.tx, m.token_id, m.side): Mk[tx].append((tk, sd))
    es_tomador = F.order_hash.isin(Mh); cont['F_filas_del_tomador_excluidas'] = int(es_tomador.sum()); cont['F_filas_propias_excluidas'] = int((F.propia & ~es_tomador).sum())
    F = F[~es_tomador & ~F.propia].copy()
    ma = F.maker_amt.astype(float); ta = F.taker_amt.astype(float)
    E = pd.DataFrame(dict(tx=F.tx.values, li=F.log_index.astype(int).values, token=F.token_id.values, price=np.where(ta > 0, ma / np.where(ta > 0, ta, 1), np.nan), qty=ta.values, maker=F.maker.str[:10].values))
    cont['E_filas_makers_ajenos'] = len(E)
    return E, dict(Mk), dict(cont)


def carga_rx(dia, txs, tokens_comp=None):
    """tx -> recepcion (ms) del print de libro5_tx (min). Lee dia-1, dia, dia+1. Solo guarda las tx pedidas. -> (dict tx->rx, dict tx->set(tokens vistos))."""
    import datetime as dt
    txs = set(txs); rx = {}; tk = collections.defaultdict(set); tev = {}
    d0 = dt.date.fromisoformat(dia)
    for d in ((d0 + dt.timedelta(days=i)).isoformat() for i in (-1, 0, 1)):
        for f in sorted(glob.glob(TXD + f'libro5_tx_{d}_*.csv.gz')):
            with gzip.open(f, 'rt') as fh:
                for ln in fh:
                    c = ln.rstrip('\n').split(',')
                    if len(c) >= 4 and c[2] in txs:
                        try: t = int(c[3])
                        except ValueError: continue
                        if c[2] not in rx or t < rx[c[2]]: rx[c[2]] = t
                        try:
                            te = int(c[0])
                            if c[2] not in tev or te < tev[c[2]]: tev[c[2]] = te
                        except ValueError: pass
                        tk[c[2]].add(c[1])
    carga_rx.tev = tev                                           # diagnostico: ts de exchange del print (t_ev); NO decide ventanas
    return rx, tk


def tipo_casado(Mk, tx, token, token_comp):
    """misma_ficha: la fila M (tomador) es sobre la misma ficha; cruzado: sobre la complementaria; otro/sin_M."""
    ms = Mk.get(tx)
    if not ms: return 'sin_M'
    if any(t == token for t, _ in ms): return 'misma_ficha'
    if token_comp and any(t == token_comp for t, _ in ms): return 'cruzado'
    return 'otro'


def eventos_de_orden(r, Ev_by_tok):
    """Filas de makers ajenos de la ficha de la orden en [t_arr-BORDE, t_end+BORDE] con precio <= L+TOL. -> DataFrame con tipo duro/nivel y flag nominal."""
    e = Ev_by_tok.get(str(r['token']))
    if e is None or not len(e): return None
    e = e[(e.rx >= r['t_arr'] - BORDE) & (e.rx <= r['t_end'] + BORDE) & (e.price <= r['L'] + TOL)]
    if not len(e): return None
    e = e.copy(); e['duro'] = e.price < r['L'] - TOL; e['nominal'] = (e.rx > r['t_arr'] + OFFSET) & (e.rx <= r['t_end'])          # nominal = FIRME: el print (recepcion ~ casado+20 ms) cae >100 ms despues de la llegada y antes del fin
    arr = (e.rx >= r['t_arr']) & (e.rx <= r['t_arr'] + OFFSET); pos = (e.rx > r['t_end']) & (e.rx <= r['t_end'] + OFFSET); pre = (e.rx < r['t_arr']) & (e.rx >= r['t_arr'] - OFFSET)
    e['ventana'] = np.where(e.nominal, 'nominal', np.where(arr, 'offset_arr', np.where(pos, 'offset_post', np.where(pre, 'offset_pre', 'fuera'))))          # offset = incertidumbre rx-ex (40-60 ms) + print ~20 ms: <=100 ms es AMBIGUO, >100 ms es orden ya cancelada/aun no armada (motor correcto)
    return e


def clasifica_fn(ev_duro_row, size_acc, tipo, ventana):
    """Causa primaria de un FN duro (precedencia fija): offset_post/offset_pre (<=100 ms fuera de la ventana nominal: AMBIGUO por incertidumbre de reloj) | barrido_parcial<5 | cruzado | misma_ficha_otro."""
    if ventana != 'nominal': return ventana + '<=100ms'
    if ev_duro_row['qty'] < size_acc - 1e-9: return 'barrido_parcial<%g' % size_acc
    if tipo == 'cruzado': return 'cruzado'
    return 'misma_ficha_otro' if tipo == 'misma_ficha' else 'otro_%s' % tipo


def audita_dia(R, E, Mk, rx, cont, dia, size_def=5.0, tev=None, status=None):
    """R: ordenes K6 (ordenes_K6_base_DIA.pkl). Unidad: (dia, mercado, lado). Devuelve dict con FN/FP duros y de nivel, causas, lista de cada FN/FP, y filas por orden para la calibracion (1b)."""
    E = E.copy(); E['rx'] = E.tx.map(rx).astype(float)
    sin_reloj = int(E.rx.isna().sum()); Ev = {tk: g.sort_values('rx') for tk, g in E.dropna(subset=['rx']).groupby('token')}
    R = R.reset_index(drop=True).copy(); R['motor'] = R.q.astype(float) > 1e-3
    out_ord = []; fn = []; fp = []; units = {}
    for i, r in R.iterrows():
        e = eventos_de_orden(r, Ev)
        duro = e[e.duro] if e is not None else None; niv = e[~e.duro] if e is not None else None
        out_ord.append(dict(i=i, mid=r['mid'], lado=r['lado'], coin=r['coin'], L=float(r['L']), clase=r.get('clase', ''), t_arr=int(r['t_arr']), t_end=int(r['t_end']), size=float(r['size']), motor=bool(r['motor']),
                            tf=(int(r['tf']) if r['motor'] else None), n_duro_nom=int(duro.nominal.sum()) if duro is not None else 0, n_duro_borde=int((~duro.nominal).sum()) if duro is not None else 0,
                            n_nivel_nom=int(niv.nominal.sum()) if niv is not None else 0, n_nivel_borde=int((~niv.nominal).sum()) if niv is not None else 0))
        u = units.setdefault((r['mid'], r['lado']), dict(coin=r['coin'], orders=[], duro=[], nivel=[], motor=False, tf=None))
        u['orders'].append(i)
        if r['motor']: u['motor'] = True; u['tf'] = int(r['tf']) if u['tf'] is None else min(u['tf'], int(r['tf']))
        comp = str(r.get('token_comp', '')) or None
        for tab, dst in ((duro, u['duro']), (niv, u['nivel'])):
            if tab is not None:
                for x in tab.itertuples():
                    dst.append(dict(i=i, price=x.price, qty=x.qty, rx=x.rx, nominal=bool(x.nominal), ventana=x.ventana, txf=x.tx, tx=x.tx, tipo=tipo_casado(Mk, x.tx, str(r['token']), comp), L=float(r['L']), size=float(r['size']), t_arr=int(r['t_arr']), t_end=int(r['t_end']), status=(str(status.status_motor.iloc[i]) if status is not None else None)))
    res = dict(unidades=len(units), unidades_con_orden=len(units), ordenes=len(R), sin_reloj_filas_ajenas=sin_reloj, E_filas=len(E))
    c_fn = collections.Counter(); c_noarm = collections.Counter(); c_amb = collections.Counter(); c_ok = collections.Counter(); c_fn_niv = collections.Counter()
    for (mid, lado), u in units.items():
        cl = u['coin']; nom = [d for d in u['duro'] if d['ventana'] == 'nominal']; amb = [d for d in u['duro'] if d['ventana'] in ('offset_post', 'offset_pre', 'offset_arr')]; fuera = [d for d in u['duro'] if d['ventana'] == 'fuera']
        if not u['motor']:
            if nom or amb:
                x = sorted(nom or amb, key=lambda d: d['rx'])[0]
                causa = clasifica_fn(x, x['size'], x['tipo'], x['ventana'])
                noarm = bool(nom) and x.get('status') not in (None, 'ok')
                if noarm: causa = 'no_armable_' + str(x['status'])                  # el motor descarta la orden al llegar (ask<=L: seria taker / sin libro): una orden post-only no reposaria; NO es un relleno perdido
                (c_noarm if noarm else (c_fn if nom else c_amb))[(cl, causa)] += 1
                fn.append(dict(dia=dia, mid=mid, lado=lado, coin=cl, causa=causa, clase_fn=('no_FN_no_armable' if noarm else ('FN_nominal' if nom else 'FN_offset_ambiguo')), price=x['price'], qty=x['qty'], L=x['L'], rx=x['rx'], tx=x['tx'][:12], tx_full=x['tx'], t_arr=x['t_arr'], t_end=x['t_end'], tipo=x['tipo'], ventana=x['ventana'], dt_vs_t_arr_ms=int(x['rx'] - x['t_arr']), dt_vs_t_end_ms=int(x['rx'] - x['t_end']), lag_rx_menos_t_ev_ms=(int(x['rx'] - tev[x['txf']]) if tev and x['txf'] in tev else None),
                    casado_rx_est_lo_menos_t_end_ms=(int(tev[x['txf']] + 20 - x['t_end']) if tev and x['txf'] in tev else None), casado_rx_est_hi_menos_t_end_ms=(int(tev[x['txf']] + 41 - x['t_end']) if tev and x['txf'] in tev else None)))
            elif fuera: c_ok[cl] += 1
            if [d for d in u['nivel'] if d['ventana'] == 'nominal']: c_fn_niv[cl] += 1
        if u['motor']:
            ev_t = [d for d in (u['duro'] + u['nivel'])]
            ok = [d for d in ev_t if u['tf'] is not None and abs(d['rx'] - u['tf']) <= BORDE]
            if not ok: fp.append(dict(dia=dia, mid=mid, lado=lado, coin=cl, tf=u['tf'], n_filas_ajenas_en_ventana=len(ev_t)))
    res['unidades_con_relleno_motor'] = sum(1 for u in units.values() if u['motor'])
    res['unidades_con_evidencia_dura'] = sum(1 for u in units.values() if any(d['ventana'] == 'nominal' for d in u['duro']))
    res['unidades_con_evidencia_dura_solo_fuera_de_ventana_(motor_correcto)'] = sum(1 for u in units.values() if u['duro'] and not any(d['ventana'] != 'fuera' for d in u['duro']))
    res['unidades_con_evidencia_nivel'] = sum(1 for u in units.values() if any(d['ventana'] == 'nominal' for d in u['nivel']))
    res['FN_duros_unidades'] = sum(c_fn.values()); res['FN_duros_por_moneda_causa'] = {f'{a}|{b}': n for (a, b), n in sorted(c_fn.items())}
    res['no_FN_no_armables_unidades_(motor descarta la orden al llegar)'] = sum(c_noarm.values()); res['no_FN_no_armables_por_moneda_causa'] = {f'{a}|{b}': n for (a, b), n in sorted(c_noarm.items())}
    res['FN_offset_ambiguos_unidades'] = sum(c_amb.values()); res['FN_offset_ambiguos_por_moneda_causa'] = {f'{a}|{b}': n for (a, b), n in sorted(c_amb.items())}
    res['no_FN_motor_correcto_unidades_(sweep 100-300 ms fuera de la ventana: orden ya cancelada o no armada)'] = sum(c_ok.values())
    res['FN_nivel_ambiguos_unidades(motor sin relleno y fila ajena EN el nivel; depende de la cola)'] = sum(c_fn_niv.values())
    res['FP_unidades(motor rellena y 0 filas ajenas a precio<=L en +-300 ms del tf)'] = len(fp)
    res['recall_duro'] = (None if not res['unidades_con_evidencia_dura'] else 1.0 - res['FN_duros_unidades'] / res['unidades_con_evidencia_dura'])
    res['cadena'] = cont
    tipos = collections.Counter(d['tipo'] for u in units.values() for d in (u['duro'] + u['nivel']) if d['ventana'] == 'nominal'); res['filas_ajenas_en_ventana_por_tipo_casado'] = dict(tipos)
    return res, fn, fp, pd.DataFrame(out_ord), units


def calibracion_1b(O, dia):
    """Sustituto de M4 (§1b): por (mercado, lado, nivel L) de TODAS las ordenes armadas: motor_fill (alguna orden del nivel con q>0) vs observado (fila ajena en el nivel con precio==L o por debajo, en ventana nominal) y 'duro' (barrido). -> DataFrame de celdas."""
    O = O.copy(); O['obs_nivel'] = (O.n_nivel_nom > 0) | (O.n_duro_nom > 0); O['obs_duro'] = O.n_duro_nom > 0
    g = O.groupby(['mid', 'lado', 'coin', 'L']).agg(clase=('clase', 'first'), motor=('motor', 'max'), obs_nivel=('obs_nivel', 'max'), obs_duro=('obs_duro', 'max'), ordenes=('i', 'count')).reset_index()
    g['dia'] = dia
    return g


def resumen_calibracion(G):
    def r(x):
        n = len(x)
        if not n: return dict(n=0)
        m, o, d = x.motor.astype(float), x.obs_nivel.astype(float), x.obs_duro.astype(float)
        return dict(n=int(n), P_motor=float(m.mean()), P_obs_nivel_o_debajo=float(o.mean()), P_obs_duro=float(d.mean()), sesgo_motor_menos_obs=float((m - o).mean()), brier_motor_vs_obs=float(((m - o) ** 2).mean()),
                    concordancia=float((m == o).mean()), motor1_obs1=int(((m == 1) & (o == 1)).sum()), motor1_obs0=int(((m == 1) & (o == 0)).sum()), motor0_obs1=int(((m == 0) & (o == 1)).sum()), motor0_obs0=int(((m == 0) & (o == 0)).sum()),
                    recall_duro=(float(m[d == 1].mean()) if (d == 1).any() else None), n_duro=int((d == 1).sum()))
    out = {'total': r(G)}
    for c, x in G.groupby('coin'): out[f'coin={c}'] = r(x)
    for c, x in G.groupby('clase'): out[f'clase={c}'] = r(x)
    G = G.assign(banda=pd.cut(G.L, [0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.45], right=False).astype(str))
    for c, x in G.groupby('banda'): out[f'L={c}'] = r(x)
    for (c, d), x in G.groupby(['coin', 'dia']): out[f'coin={c}|dia={d}'] = r(x)
    return out
