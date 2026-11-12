#!/usr/bin/env python3
"""forward_gates.py -- veredicto POR PUERTA del forward B-CXB, tal como esta escrito en PREREG_CXB_MULTIVARIANTE_FORWARD.md (congelado 12-Nov-2026, sha256 en el .sha256 vecino).

QUE ES Y QUE NO: un evaluador de solo lectura que implementa §3-§6 del prereg SIN modificar ningun fichero congelado (runner, motor, resolvedor, informe):
  - los dias validos y las coberturas se calculan AQUI desde los res_<D>.csv.gz de CADA poblacion (el campo `cobertura_desenlace_rellenos` del informe esta contaminado por BTC: no se usa);
  - la estadistica (EV ponderado, IC90 por dias y por cierres, sin los 2 mejores dias, placebo, c59) la calcula el informe congelado, ejecutado sobre un directorio de STAGING con enlaces simbolicos
    solo a los dias validos (asi un dia no valido no entra y la mitad del G9 se hace con la misma funcion congelada);
  - las puertas G1-G9 y el veredicto se aplican aqui con los umbrales del prereg (G5: S>=100 y p<=0,025, NO el `ok` del informe).
LO QUE NO HACE: no corre ninguna puerta fuera de una mirada (§6: "entre miradas no se calculan puertas"). `--mirada N` exige el numero de dias validos del prereg (N=1: >=10; N=2: >=20 y mirada 1 = INSUFFICIENT),
no sobrescribe una mirada ya hecha y escribe OUT/forward_gates_mirada<N>.json. `--ensayo-tecnico` (sin minimo de dias, no escribe en OUT, sale marcado) existe solo para probar el cableado.
PASS = DRY_RUN_VALIDATED es un INDICE sobre ordenes virtuales: no autoriza ningun envio. 0 ordenes, sin red, sin credenciales.

Decisiones de lectura del prereg declaradas (todas literales; ninguna relaja nada):
  - G3 se aplica como PUERTA (prereg §4: "PASS = todas"; H1 pide mejorar tambien a GEO1). Su valor se publica aparte para que el validador lo lea sin mezclarlo con el resto.
  - G6 en BTC: solo la parte del dia (prereg §4: "En BTC solo se aplica la parte del dia"); la parte de moneda se publica como n/a.
  - "pnl positivo": si ningun dia tiene pnl positivo, la cuota del mejor dia no esta definida (None) y la parte del dia de G6 se cumple por vacuidad (G2 ya falla en ese caso).
  - Un dia sin ningun relleno en la poblacion no tiene cobertura definida (None): se acepta por vacuidad pero se marca `sin_rellenos`. Un dia con rellenos y cobertura < 0,95 NO es valido.
  - FAIL por placebo (p >= 0,50) exige ademas S >= 100; con menos semillas el caso es INSUFFICIENT."""
import os, sys, json, glob, shutil, tempfile, subprocess, argparse, datetime as dt

HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
DRY = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'          # .../dryrun/
DL = '/root/polymarket-research-datalogs/'
OUT_DEF = DL + 'cxb60_dryrun/'
GMAP_DIR_DEF = DL + 'cxb60_dryrun_gmap/'
HASH_REF = '534b476093a8294bf28f7ebf62e3e825dcbd57bb98d43dd9fa6a7bc844d03c0b'
# ---- umbrales del prereg (NO se tocan despues de ver datos)
COB_DIA_MIN = 0.95; COB_AGREGADA_MIN = 0.99; HUECO_MAX = 0.05
G1_N_REL = 40; G1_N_CIERRES = 30; G1_DIAS = 10; DIAS_MIRADA2 = 20
G5_S_MIN = 100; G5_P_MAX = 0.025; FAIL_P = 0.50
G6_MONEDA = 0.60; G6_DIA = 0.25; G8_MIN = -0.05; PLAZO_DIAS = 35
POBLACIONES = {'primaria': dict(coins=('ETH', 'SOL', 'XRP'), clave='dia_valido', gmap='gmap_{d}.json', informe_args=[]),
               'BTC': dict(coins=('BTC',), clave='dia_valido_btc', gmap='gmap_btc_{d}.json', informe_args=['--coins', 'BTC', '--clave-valido', 'dia_valido_btc'])}


# ======================================================================================== cobertura y dias validos (por poblacion, desde res_)
def cobertura_desenlace_dia(res_path, coins):
    """Rellenos (q>1e-9) de las monedas de la poblacion y cuantos tienen pnl (= desenlace oficial). Lee solo 3 columnas, en trozos. None si no hay fichero."""
    import pandas as pd
    if not os.path.exists(res_path): return None
    rel = res = 0
    for ch in pd.read_csv(res_path, usecols=['coin', 'q', 'pnl'], dtype={'coin': str}, chunksize=400000):
        f = ch[(ch.q > 1e-9) & ch.coin.isin(coins)]; rel += len(f); res += int(f.pnl.notna().sum())
    return dict(rellenos=rel, resueltos=res, sin_desenlace=rel - res, cobertura=(res / rel) if rel else None, sin_rellenos=(rel == 0))


def gmap_existe(d, pob, gmap_dir):
    p = gmap_dir.rstrip('/') + '/' + POBLACIONES[pob]['gmap'].format(d=d)
    try: return os.path.getsize(p) > 2          # getsize sigue enlaces simbolicos: un enlace roto da OSError
    except OSError: return False


def dias_candidatos(out, desde='0000', hasta='9999'):
    return sorted(d for d in (os.path.basename(f)[9:19] for f in glob.glob(out + 'coverage_*.json')) if desde <= d <= hasta)


def evaluar_dias(out, pob, gmap_dir, desde='0000', hasta='9999', coverage_dir=None):
    """(validos, detalle) con detalle[d] = dict(valido, motivos[], cobertura_desenlace, rellenos...). Un dia es valido si (prereg §3): coverage `clave` true (dia completo y monedas >= 0,95), existe el gmap
    oficial de la poblacion, existe res_<D> y la cobertura de desenlace de sus rellenos >= 0,95. Un dia no valido nunca se rellena con ceros."""
    P = POBLACIONES[pob]; validos, det = [], {}
    for d in dias_candidatos(out, desde, hasta):
        mot = []; info = dict(motivos=mot)
        try: cov = json.load(open(out + f'coverage_{d}.json'))
        except (OSError, ValueError): cov = None
        if cov is None: mot.append('coverage_ilegible')
        else:
            info['coverage'] = dict(dia_completo=cov.get('dia_completo'), por_moneda={c: v.get('cobertura') for c, v in cov.get('por_moneda', {}).items() if c in P['coins']}, saltados=cov.get('saltados'))
            if not cov.get(P['clave']): mot.append(f"{P['clave']}=false")
        if not gmap_existe(d, pob, gmap_dir): mot.append('sin_gmap_oficial')
        cd = cobertura_desenlace_dia(out + f'res_{d}.csv.gz', P['coins'])
        if cd is None: mot.append('sin_res (resolvedor no ha corrido)')
        else:
            info['desenlace'] = cd
            if cd['cobertura'] is not None and cd['cobertura'] < COB_DIA_MIN: mot.append(f"cobertura_desenlace {cd['cobertura']:.3f} < {COB_DIA_MIN}")
        info['valido'] = not mot; det[d] = info
        if not mot: validos.append(d)
    return validos, det


def cobertura_agregada(det, validos):
    r = sum(det[d]['desenlace']['rellenos'] for d in validos); s = sum(det[d]['desenlace']['resueltos'] for d in validos)
    return dict(rellenos=r, resueltos=s, cobertura=(s / r) if r else None)


# ======================================================================================== staging + informe congelado
def preparar_stage(out, dias, dest):
    """Directorio con enlaces simbolicos solo a los dias dados (escenario primario y OUT/c59). El informe congelado lo lee como si fuese OUT."""
    os.makedirs(dest + 'c59', exist_ok=True)
    for base, sub in ((out, ''), (out + 'c59/', 'c59/')):
        for d in dias:
            for pref in ('res_', 'dec_', 'coverage_'):
                ext = '.json' if pref == 'coverage_' else '.csv.gz'; src = base + f'{pref}{d}{ext}'
                if os.path.exists(src) and not (pref == 'coverage_' and sub): os.symlink(src, dest + sub + f'{pref}{d}{ext}')
    return dest


def correr_informe(stage, pob, desde='0000', timeout=3600):
    """Ejecuta cxb60_informe.py (CONGELADO, solo lectura) sobre `stage` y devuelve su JSON. Se usa `sys.executable -I`; el informe vive en dryrun/."""
    salida = stage + 'informe.json'
    cmd = [sys.executable, '-I', DRY + 'cxb60_informe.py', '--out', stage, '--salida', salida] + POBLACIONES[pob]['informe_args']
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if r.returncode != 0 or not os.path.exists(salida): raise RuntimeError('el informe congelado fallo: ' + (r.stderr or r.stdout)[-600:])
    return json.load(open(salida))


# ======================================================================================== puertas (funcion PURA sobre los JSON del informe)
def _sg(x): return (x > 0) - (x < 0)


def _g(inf, *ks, d=None):
    for k in ks:
        if not isinstance(inf, dict) or k not in inf: return d
        inf = inf[k]
    return inf


def evaluar_puertas(inf, mitades, pob, n_dias_validos):
    """inf = JSON del informe sobre todos los dias validos; mitades = (inf_primera, inf_segunda). Devuelve {G1..G9: {ok, ...valores}}. Falta de dato => ok False (nunca por defecto)."""
    c = _g(inf, 'variantes', 'CXB60', d={}) or {}; G = {}
    n_rel, n_cie = c.get('n_rellenos'), c.get('n_cierres_con_relleno')
    G['G1'] = dict(n_rellenos=n_rel, n_cierres_con_relleno=n_cie, dias_validos=n_dias_validos, ok_n_rellenos=bool(n_rel is not None and n_rel >= G1_N_REL), ok_n_cierres=bool(n_cie is not None and n_cie >= G1_N_CIERRES), ok_dias=bool(n_dias_validos >= G1_DIAS))
    G['G1']['ok'] = G['G1']['ok_n_rellenos'] and G['G1']['ok_n_cierres'] and G['G1']['ok_dias']
    ev, icd, icc = c.get('ev_cond_fill_ponderado_eur'), c.get('ic90_por_dia'), c.get('ic90_por_cierre')
    G['G2'] = dict(ev=ev, ic90_dias=icd, ic90_cierres=icc, ok=bool(ev is not None and ev > 0 and icd and icd[0] > 0 and icc and icc[0] > 0))
    lo = _g(inf, 'puertas_diagnostico', 'G3_incremental_vs_GEO1_dias', 'ic90_inferior'); dm = _g(inf, 'puertas_diagnostico', 'G3_incremental_vs_GEO1_dias', 'delta_pnl_medio_dia')
    G['G3'] = dict(delta_pnl_medio_dia=dm, ic90_inferior=lo, ok=bool(lo is not None and lo > 0), nota='puerta del prereg (§4); el informe la marca "diagnostico"')
    s4 = c.get('ev_cond_sin_2_mejores_dias'); G['G4'] = dict(ev_sin_2_mejores_dias=s4, ok=bool(s4 is not None and s4 > 0))
    S, p = _g(inf, 'placebo', 'semillas'), _g(inf, 'placebo', 'p_valor')
    G['G5'] = dict(semillas=S, p=p, umbral_p=G5_P_MAX, ok=bool(S is not None and p is not None and S >= G5_S_MIN and p <= G5_P_MAX), nota='regla del prereg (S>=100, p<=0,025), no el ok del informe')
    pm = _g(inf, 'por_moneda', 'CXB60', d={}) or {}; ct = sum(v.get('coste', 0) for v in pm.values()); sh = (max((v.get('coste', 0) for v in pm.values()), default=0) / ct) if ct > 0 else None
    dia_sh = c.get('max_dia_share_pnl_positivo'); ok_dia = dia_sh is None or dia_sh <= G6_DIA
    if pob == 'BTC': G['G6'] = dict(moneda='n/a (una sola moneda; prereg §4)', max_dia_share_pnl_positivo=dia_sh, ok=bool(ok_dia and ct > 0))
    else: G['G6'] = dict(max_moneda_share_coste=None if sh is None else round(sh, 3), max_dia_share_pnl_positivo=dia_sh, ok=bool(sh is not None and sh <= G6_MONEDA and ok_dia))
    e59 = _g(inf, 'puertas_diagnostico', 'G7_sello_cinta_pesimista_c59', 'ev_c59')
    G['G7'] = dict(ev_c19=ev, ev_c59=e59, ok=bool(ev is not None and e59 is not None and _sg(ev) == _sg(e59)))
    e100 = _g(inf, 'variantes', 'CXB100', 'ev_cond_fill_ponderado_eur'); G['G8'] = dict(ev_CXB100=e100, ok=bool(e100 is not None and e100 >= G8_MIN))
    m = [_g(h, 'variantes', 'CXB60', 'ev_cond_fill_ponderado_eur') for h in mitades]
    G['G9'] = dict(ev_primera_mitad=m[0], ev_segunda_mitad=m[1], ok=bool(all(x is not None and x > 0 for x in m)))
    return G


def veredicto(G, calidad_ok, inf):
    """PASS / FAIL / INSUFFICIENT (prereg §5). Calidad agregada fallida => INSUFFICIENT (nada se excluye a posteriori)."""
    if not calidad_ok: return 'INSUFFICIENT', 'calidad agregada (cobertura de desenlace < 0,99 o huecos de feed > 5 %)'
    if all(g['ok'] for g in G.values()): return 'PASS', 'todas las puertas G1-G9'
    icd = _g(inf, 'variantes', 'CXB60', 'ic90_por_dia'); S, p = _g(inf, 'placebo', 'semillas'), _g(inf, 'placebo', 'p_valor')
    if G['G1']['ok']:
        if icd and icd[1] < 0: return 'FAIL', 'G1 cumplida y extremo superior del IC90 por dias del EV de CXB60 < 0'
        if S is not None and S >= G5_S_MIN and p is not None and p >= FAIL_P: return 'FAIL', 'G1 cumplida y placebo p >= 0,50 (CXB60 no mejora la mediana del placebo)'
    return 'INSUFFICIENT', 'puertas que fallan: ' + ','.join(k for k, g in G.items() if not g['ok'])


def pospuesta_por_n(G, n_dias):
    """Mirada 1: si lo unico que falla es la parte de n de G1 y aun no hay 20 dias validos, se pospone (el disparador es n, no el resultado)."""
    fallan = [k for k, g in G.items() if not g['ok']]
    return bool(fallan == ['G1'] and G['G1']['ok_dias'] and not (G['G1']['ok_n_rellenos'] and G['G1']['ok_n_cierres']) and n_dias < DIAS_MIRADA2)


# ======================================================================================== orquestacion
def evaluar_poblacion(out, pob, gmap_dir, desde, hasta, trabajo, informe=correr_informe):
    """Todo el calculo de UNA poblacion. Devuelve dict serializable. `informe` es inyectable en tests."""
    P = POBLACIONES[pob]; validos, det = evaluar_dias(out, pob, gmap_dir, desde, hasta)
    res = dict(poblacion=pob, monedas=list(P['coins']), desde=desde, hasta=hasta, dias_validos=validos, n_dias_validos=len(validos), dias_no_validos={d: v['motivos'] for d, v in det.items() if not v['valido']}, detalle_dias=det)
    if not validos: res.update(veredicto='INSUFFICIENT', motivo='sin dias validos', puertas={}); return res
    ca = cobertura_agregada(det, validos); res['cobertura_desenlace_agregada'] = ca
    k = (len(validos) + 1) // 2; partes = {'todos': validos, 'primera': validos[:k], 'segunda': validos[k:]}; inf = {}
    for nombre, ds in partes.items():
        if not ds: inf[nombre] = {}; continue
        st = preparar_stage(out, ds, trabajo + f'{pob}_{nombre}/'); inf[nombre] = informe(st, pob, desde)
    huecos = sum((inf['todos'].get('mercados_con_hueco_feed') or {}).values()); proc = sum((inf['todos'].get('mercados_procesados_por_moneda') or {}).values())
    hr = (huecos / proc) if proc else None
    calidad = dict(cobertura_desenlace_agregada=ca['cobertura'], umbral_cobertura=COB_AGREGADA_MIN, hueco_feed_ratio=hr, umbral_hueco=HUECO_MAX, mercados_procesados=proc, mercados_con_hueco_feed=huecos)
    calidad['ok'] = bool(ca['cobertura'] is not None and ca['cobertura'] >= COB_AGREGADA_MIN and hr is not None and hr <= HUECO_MAX)
    G = evaluar_puertas(inf['todos'], (inf['primera'], inf['segunda']), pob, len(validos)); v, motivo = veredicto(G, calidad['ok'], inf['todos'])
    res.update(calidad=calidad, puertas=G, veredicto=v, motivo=motivo, pospuesta_por_n=pospuesta_por_n(G, len(validos)) if v == 'INSUFFICIENT' else False,
               sello_print={'primario': inf['todos'].get('sello_print'), 'c59': 'ws_ex-59-1 (OUT/c59, G7)'}, mitades=dict(primera=partes['primera'], segunda=partes['segunda']),
               exclusiones_desenlace_informe=inf['todos'].get('exclusiones_desenlace'), nota_cobertura_informe='el campo cobertura_desenlace_rellenos del informe NO se usa (contaminado por BTC)')
    return res


def integridad(out):
    """Avisos (no puertas): hash de referencia y sellos del manifiesto de ambos escenarios."""
    av = []
    for sub, sello in (('', 'ws_ex-19-1'), ('c59/', 'ws_ex-59-1')):
        try: m = json.load(open(out + sub + 'run_manifest.json'))
        except (OSError, ValueError): av.append(f'sin run_manifest en {out + sub}'); continue
        if m.get('sello_print') != sello: av.append(f"sello_print {m.get('sello_print')} != {sello} en {sub or 'primario'}")
        if m.get('job') != 'cxb60_dryrun_v3': av.append(f"VERSION {m.get('job')} != cxb60_dryrun_v3")
        if (m.get('hash_check') or {}).get('sha256_referencia') != HASH_REF: av.append('hash_check.sha256_referencia distinto del congelado')
    return av


def lee_d_dep(out):
    try: return json.load(open(out + 'forward_d_dep.json'))
    except (OSError, ValueError): return None


CUTOFF_UTC = '2026-11-12T11:24:00Z'          # hora del congelado (mtime de PREREG_CXB_MULTIVARIANTE_FORWARD.sha256)


def registrar_d_dep(out, cutoff=CUTOFF_UTC):
    """Prereg §3: D_dep = fecha UTC del PRIMER run_manifest RUNNING de cxb60_dryrun_v3 con hash_check.sha256_referencia = 534b4760... posterior al cutoff; primer dia contable = D_dep+1.
    Se escribe UNA vez (nunca se sobrescribe). Devuelve (dict o None, creado: bool). Si el manifiesto aun no cumple, no escribe nada."""
    ya = lee_d_dep(out)
    if ya: return ya, False
    try: m = json.load(open(out + 'run_manifest.json'))
    except (OSError, ValueError): return None, False
    ini = m.get('inicio'); co = dt.datetime.fromisoformat(cutoff.replace('Z', '+00:00')).timestamp()
    if not (m.get('job') == 'cxb60_dryrun_v3' and (m.get('hash_check') or {}).get('sha256_referencia') == HASH_REF and m.get('status') == 'RUNNING' and isinstance(ini, (int, float)) and ini > co): return None, False
    d = dt.datetime.fromtimestamp(ini, dt.timezone.utc); rec = dict(D_dep=d.strftime('%Y-%m-%d'), primer_dia_contable=(d + dt.timedelta(days=1)).strftime('%Y-%m-%d'), run_id=m.get('run_id'),
                                                               inicio_utc=d.strftime('%Y-%m-%dT%H:%M:%SZ'), sha256_referencia=HASH_REF, cutoff_utc=cutoff, regla='primer run_manifest RUNNING v3 con el hash congelado, posterior al cutoff (prereg §3)')
    tmp = out + 'forward_d_dep.json.tmp'; json.dump(rec, open(tmp, 'w'), indent=1); os.replace(tmp, out + 'forward_d_dep.json'); return rec, True


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0]); ap.add_argument('--out', default=OUT_DEF); ap.add_argument('--gmap-dir', default=GMAP_DIR_DEF)
    ap.add_argument('--mirada', type=int, choices=(1, 2)); ap.add_argument('--ensayo-tecnico', action='store_true', help='sin minimo de dias ni escritura en OUT: solo prueba el cableado')
    ap.add_argument('--desde', default=None, help='primer dia contable (D_dep+1); por defecto el de forward_d_dep.json'); ap.add_argument('--hasta', default='9999'); ap.add_argument('--salida', default=None)
    ap.add_argument('--hoy', default=None, help=argparse.SUPPRESS); a = ap.parse_args(argv); out = a.out.rstrip('/') + '/'
    if not a.mirada and not a.ensayo_tecnico: print('Falta --mirada N (el prereg prohibe calcular puertas entre miradas) o --ensayo-tecnico.', file=sys.stderr); return 2
    dd = lee_d_dep(out); desde = a.desde or (dd or {}).get('primer_dia_contable')
    if not desde: print('Sin --desde y sin forward_d_dep.json: no se sabe cual es el primer dia contable.', file=sys.stderr); return 2
    hoy = a.hoy or dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d'); trabajo = tempfile.mkdtemp(prefix='fwd_gates_', dir=DL if os.path.isdir(DL) else None) + '/'
    try:
        h1 = evaluar_poblacion(out, 'primaria', a.gmap_dir, desde, a.hasta, trabajo); n = h1['n_dias_validos']; res = dict(prereg='PREREG_CXB_MULTIVARIANTE_FORWARD.md', mirada=a.mirada, ensayo_tecnico=a.ensayo_tecnico, ts_utc=hoy, desde=desde, D_dep=(dd or {}).get('D_dep'), H1=h1, avisos_integridad=integridad(out))
        if dd and dd.get('D_dep') and (dt.date.fromisoformat(hoy) - dt.date.fromisoformat(dd['D_dep'])).days > PLAZO_DIAS and h1['veredicto'] != 'PASS': res['plazo'] = f'INSUFFICIENT_OPERATIVO: pasaron >{PLAZO_DIAS} dias desde D_dep'
        if a.mirada and not a.ensayo_tecnico:
            minimo = G1_DIAS if a.mirada == 1 else DIAS_MIRADA2
            if n < minimo: print(f'Mirada {a.mirada} no procede: {n} dias validos < {minimo} (prereg §6; entre miradas no se calculan puertas).', file=sys.stderr); return 2
            f = out + f'forward_gates_mirada{a.mirada}.json'
            if os.path.exists(f): print(f'{f} ya existe: no hay una tercera mirada ni se repite una (prereg §6).', file=sys.stderr); return 2
            if a.mirada == 2:
                try: m1 = json.load(open(out + 'forward_gates_mirada1.json'))['H1']['veredicto']
                except (OSError, ValueError, KeyError): m1 = None
                if m1 != 'INSUFFICIENT': print(f'Mirada 2 solo si la 1 dio INSUFFICIENT (dio {m1}).', file=sys.stderr); return 2
        if h1['veredicto'] == 'PASS':
            b = evaluar_poblacion(out, 'BTC', a.gmap_dir, desde, a.hasta, trabajo); res['H2_BTC'] = b
        else: res['H2_BTC'] = 'EXPLORATORIO (H1 no es PASS; prereg §1: no se contrasta H2 ni se declara REJECTED)'
        txt = json.dumps(res, indent=1, default=str)
        if a.salida: open(a.salida, 'w').write(txt)
        elif a.mirada and not a.ensayo_tecnico: open(out + f'forward_gates_mirada{a.mirada}.json', 'w').write(txt)
        if a.ensayo_tecnico: print('ENSAYO TECNICO: NO es una mirada, no cuenta, no se guarda en OUT.')
        print(f"H1 {h1['veredicto']} ({h1.get('motivo')}); dias validos {n}")
        for k, g in h1.get('puertas', {}).items(): print(f"  {k}: {'OK ' if g['ok'] else 'NO '} " + ', '.join(f'{x}={y}' for x, y in g.items() if x not in ('ok', 'nota')))
        return 0
    finally: shutil.rmtree(trabajo, ignore_errors=True)


if __name__ == '__main__': sys.exit(main())
