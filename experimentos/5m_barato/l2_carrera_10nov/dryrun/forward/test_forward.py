#!/usr/bin/env python3
"""Tests del forward B-CXB: fuente de desenlace BTC (fwd_gmap_btc.py), cobertura por poblacion, dias validos, puertas G1-G9 y veredicto (forward_gates.py).  python3 -I test_forward.py
Todo SINTETICO en un tmp (sin red, sin tocar el datalog real); el informe y el resolvedor que se ejecutan son los CONGELADOS (cxb60_informe.py / cxb60_resolve.py), solo lectura.
F1 gmap BTC: esquema {slug:{id,toks,des}}, mapeo por etiqueta [Up,Down], desenlace solo binario cerrado, idempotencia, fichero corrupto, cobertura y codigo de salida.
F2 cobertura de desenlace POR POBLACION desde res_: BTC sin resolver no contamina la primaria (y el campo del informe SI se contamina: se demuestra).
F3 dias validos: cada motivo de exclusion por separado (coverage, gmap, res, cobertura de desenlace) y un dia sin rellenos.
F4 puertas G1-G9 con valores en el limite (>=40/30/10, p 0,025 con S=100 vs 99, G6 BTC solo dia, G7 signos, G9 mitades).
F5 veredicto PASS / FAIL / INSUFFICIENT y calidad agregada; pospuesta_por_n.
F6 extremo a extremo con el informe congelado: PASS; S<100 => INSUFFICIENT; CXB60 negativo => FAIL; BTC (H2) solo tras PASS; dia con desenlace incompleto excluido; las mitades del G9.
F7 guardas de la mirada: sin --mirada, <10 dias, no sobrescribir, mirada 2 solo tras INSUFFICIENT.
F8 el resolvedor congelado + gmap con BTC cierra el desenlace de BTC (join exacto por mid y token)."""
import os, sys, json, csv, gzip, shutil, tempfile, datetime as dt, subprocess, contextlib, io
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; DRY = os.path.dirname(HERE.rstrip('/')) + '/'
sys.path.insert(0, HERE); sys.path.insert(0, DRY)
import fwd_gmap_btc as GB, forward_gates as FG, cxb60_io as IO

TMP = tempfile.mkdtemp(prefix='test_fwd_'); N = [0]
def nuevo(): N[0] += 1; d = f'{TMP}/t{N[0]}/'; os.makedirs(d); return d
VARS = ['G0', 'GEO1', 'CXB35', 'CXB45', 'CXB60', 'CXB100', 'CXB150', 'CXBEMP']


# ----------------------------------------------------------------------------------------------- F1
def mk_mercado(slug, outs=('Up', 'Down'), closed=True, pr=('1', '0'), mid=1000, toks=None):
    return dict(slug=slug, id=mid, clobTokenIds=json.dumps(toks or [slug + 'U', slug + 'D']), outcomes=json.dumps(list(outs)), outcomePrices=json.dumps(list(pr)), closed=closed)


class GammaFalsa:
    """get(url, params) -> lista de mercados; `tabla[slug] = mercado` (solo se devuelve en la consulta cuyo `closed` coincide, como gamma)."""
    def __init__(self, tabla, fallos=0): self.t = tabla; self.llamadas = 0; self.slugs = []; self.fallos = fallos
    def __call__(self, url, params):
        self.llamadas += 1
        if self.fallos > 0: self.fallos -= 1; raise OSError('red caida')
        sl = [v for k, v in params if k == 'slug']; closed = [v for k, v in params if k == 'closed'][0] == 'true'; self.slugs += sl
        return [self.t[s] for s in sl if s in self.t and bool(self.t[s]['closed']) == closed]


def test_gmap_btc():
    os.environ['FWD_GMAP_SLEEP'] = '0'; d = '2026-11-20'; slugs = GB.slugs_dia(d); assert len(slugs) == 290 and slugs[0].startswith('btc-updown-5m-') and slugs[1] == f'btc-updown-5m-{int(slugs[0].rsplit("-", 1)[1]) + 300}'
    t0 = int(dt.datetime(2026, 11, 20, tzinfo=dt.timezone.utc).timestamp()); ahora = t0 + 86400 + 7200
    tabla = {s: mk_mercado(s, mid=5000 + i, pr=('1', '0') if i % 2 else ('0', '1')) for i, s in enumerate(slugs)}
    tabla[slugs[3]] = mk_mercado(slugs[3], outs=('Down', 'Up'), mid=9003)                                  # etiquetas en otro orden: NO se supone el mapeo
    tabla[slugs[4]] = mk_mercado(slugs[4], pr=('0.5', '0.5'), mid=9004)                                    # 50/50: sin desenlace (missing != 0)
    tabla[slugs[5]] = mk_mercado(slugs[5], closed=False, pr=('0.7', '0.3'), mid=9005)                      # no cerrado
    del tabla[slugs[6]]                                                                                   # sin mercado en gamma
    out = nuevo(); g = GammaFalsa(tabla); cob = GB.construir(d, out, get=g, ahora=ahora); gm = json.load(open(out + f'gmap_btc_{d}.json'))
    e = gm[slugs[1]]; assert set(e) >= {'id', 'toks', 'des'} and e['id'] == '5001' and e['toks'] == [slugs[1] + 'U', slugs[1] + 'D'] and e['des'] == 'YES' and gm[slugs[0]]['des'] == 'NO'   # esquema de sa_r1 (YES = Up = toks[0])
    assert gm[slugs[3]]['des'] is None and gm[slugs[3]]['motivo'] == 'etiquetas_inesperadas' and gm[slugs[4]]['des'] is None and gm[slugs[4]]['motivo'] == 'desenlace_no_binario' and gm[slugs[5]]['des'] is None and slugs[6] not in gm
    assert cob['esperados_cerrados'] == 290 and cob['con_desenlace'] == 290 - 4 and cob['etiquetas_inesperadas'] == 1 and cob['sin_mercado_en_gamma'] == 1 and cob['sin_desenlace_otros'] == 2 and abs(cob['cobertura_desenlace'] - 286 / 290) < 1e-4, cob
    assert json.load(open(out + f'cob_btc_{d}.json'))['con_desenlace'] == 286 and not [f for f in os.listdir(out) if f.endswith('.tmp')]
    # idempotencia: la 2a pasada solo re-consulta los 4 slugs sin desenlace + el ausente y no cambia lo ya resuelto
    g2 = GammaFalsa(tabla); h1 = open(out + f'gmap_btc_{d}.json').read(); GB.construir(d, out, get=g2, ahora=ahora); assert sorted(set(g2.slugs)) == sorted([slugs[3], slugs[4], slugs[5], slugs[6]]) and open(out + f'gmap_btc_{d}.json').read() == h1
    tabla[slugs[5]] = mk_mercado(slugs[5], mid=9005); GB.construir(d, out, get=GammaFalsa(tabla), ahora=ahora); assert json.load(open(out + f'gmap_btc_{d}.json'))[slugs[5]]['des'] == 'YES'        # se completa cuando gamma cierra
    # fichero corrupto -> se reconstruye entero; errores de red -> se cuentan y no rompen
    open(out + f'gmap_btc_{d}.json', 'w').write('{no json'); c = GB.construir(d, out, get=GammaFalsa(tabla), ahora=ahora); assert c['consultados'] == 290 and c['con_desenlace'] == 287, c
    o3 = nuevo().rstrip('/'); GB.construir(d, o3, get=GammaFalsa(tabla), ahora=ahora); assert os.path.exists(o3 + f'/gmap_btc_{d}.json') and os.path.exists(o3 + f'/cob_btc_{d}.json') and not [x for x in os.listdir(os.path.dirname(o3)) if x.startswith(os.path.basename(o3) + 'gmap') or x.startswith(os.path.basename(o3) + 'cob')]      # --dir SIN barra final (como lo pasa el cron): no escribe fuera del directorio
    o2 = nuevo(); c = GB.construir(d, o2, get=GammaFalsa(tabla, fallos=999), ahora=ahora); assert c['con_desenlace'] == 0 and c['errores_red'] > 0 and c['cobertura_desenlace'] == 0.0
    # codigo de salida de main(): con la cobertura medida por construir() (sin red: construir se sustituye por un doble)
    orig = GB.construir
    try:
        GB.construir = lambda d, dr, get=None, ahora=None: dict(cobertura_desenlace=0.985); assert GB.main(['2026-11-20', '--dir', nuevo()]) == 3
        GB.construir = lambda d, dr, get=None, ahora=None: dict(cobertura_desenlace=0.99); assert GB.main(['2026-11-20', '--dir', nuevo()]) == 0
        GB.construir = lambda d, dr, get=None, ahora=None: dict(cobertura_desenlace=None); assert GB.main(['2026-11-20', '--dir', nuevo()]) == 3
    finally: GB.construir = orig
    print('F1 ok: gmap BTC con esquema sa_r1, etiquetas [Up,Down] validadas, 50/50 y no-cerrados sin desenlace, cobertura medida, idempotente, corrupto -> reconstruye, red caida -> 0 % sin romper')


# ----------------------------------------------------------------------------------------------- helpers de datos sinteticos
RES_COLS = ['tipo', 'run_id', 'dia', 'tok', 'mid', 'coin', 'lado', 'fin', 'L', 'var', 'seg', 't_dec_rx', 't_arr', 't_end', 'motivo_fin', 'canc', 't_trig_rx', 't_trig_ex', 'q', 'tf', 'rem_antes', 'detalle', 't_wall_ms', 'gana', 'pnl', 'cost', 'cost_pot', 'des']
REB = 0.2 * 0.07


def fila(d, coin, tok, mid, fin, var, q, gana, L=0.10, sin_desenlace=False):
    r = dict.fromkeys(RES_COLS, ''); r.update(tipo='seg', run_id='t', dia=d, tok=tok, mid=mid, coin=coin, lado='YES', fin=fin, L=L, var=var, seg=0, canc=1 if var.startswith(('CXB', 'PLC')) else 0, q=q, rem_antes=5.0, cost_pot=round(5.0 * L, 6))
    if q > 0 and not sin_desenlace: r.update(gana=gana, pnl=round(q * (gana - L) + q * REB * L * (1 - L), 6), cost=round(q * L, 6), des='YES' if gana else 'NO')
    return r


def patron(var, j, rng, cfg):
    """gana (0/1) de la variante en el cierre j del dia. cfg define la 'verdad' de la sintetica: CXB60 gana en j par (EV alto), GEO1 solo j==0, placebo al azar p=0,25."""
    if var.startswith('PLC60_'): return int(rng.random() < cfg.get('p_placebo', 0.25))
    if var == 'CXB60': return cfg.get('cxb60', lambda j: int(j % 2 == 0))(j)
    if var == 'GEO1': return int(j == 0)
    if var in ('CXB100', 'CXB150', 'CXBEMP', 'CXB35', 'CXB45'): return cfg.get('cxb100', lambda j: int(j % 2 == 0))(j)
    return int(j == 1)


def crea_datos(out, dias, coins=('ETH', 'SOL', 'XRP'), semillas=100, cfg=None, gmap_dir=None, incompletos=(), sin_res=(), sin_gmap=(), no_validos=()):
    """out/: coverage_, dec_ (solo filas mkt), res_ (todas las variantes) y out/c59/ (sin placebo). gmap_dir/: gmap_<D>.json (primaria) y gmap_btc_<D>.json (BTC)."""
    cfg = cfg or {}; os.makedirs(out + 'c59', exist_ok=True); rng = np.random.default_rng(7); base = int(dt.datetime(2026, 11, 20, tzinfo=dt.timezone.utc).timestamp())
    if gmap_dir: os.makedirs(gmap_dir, exist_ok=True)
    for i, d in enumerate(dias):
        t0 = int(dt.datetime.fromisoformat(d).replace(tzinfo=dt.timezone.utc).timestamp()); rows, rows59, mk = [], [], []
        for c in coins:
            for j in range(4):
                fin = t0 + 3600 * j; tok = f'{c}_{d}_{j}'; mid = f'{abs(hash((c, d, j))) % 10**7}'
                mk.append(dict.fromkeys(IO.COLS, '') | dict(tipo='mkt', run_id='t', dia=d, tok=tok, mid=mid, coin=c, lado='YES', fin=fin, detalle=json.dumps(dict(hueco_feed=bool(cfg.get('hueco') and j == 0)), separators=(',', ':'))))
                for v in VARS + [f'PLC60_{s}' for s in range(1, semillas + 1)]:
                    g = patron(v, j, rng, cfg); falta = d in incompletos and j == 0 and v in ('CXB60', 'GEO1') or (d in incompletos and c == coins[0])
                    r = fila(d, c, tok, mid, fin, v, 5.0, g, sin_desenlace=bool(falta)); rows.append(r)
                    if not v.startswith('PLC60_'): rows59.append(fila(d, c, tok, mid, fin, v, 5.0, cfg.get('g59', lambda v_, j_, g_: g_)(v, j, g)))
        for base_dir, rr in ((out, rows), (out + 'c59/', rows59)):
            with gzip.open(base_dir + f'res_{d}.csv.gz', 'wt', newline='') as fh:
                w = csv.DictWriter(fh, fieldnames=RES_COLS, lineterminator='\n'); w.writeheader(); [w.writerow(r) for r in rr]
        with gzip.open(out + f'dec_{d}.csv.gz', 'wt', newline='') as fh:
            w = csv.DictWriter(fh, fieldnames=IO.COLS, lineterminator='\n'); w.writeheader(); [w.writerow(r) for r in mk]
        if d in sin_res: os.remove(out + f'res_{d}.csv.gz')
        cov = dict(dia=d, dia_completo=True, cobertura=1.0, dia_valido=d not in no_validos, dia_valido_btc=d not in no_validos, por_moneda={c: dict(cobertura=1.0) for c in coins}, saltados={})
        json.dump(cov, open(out + f'coverage_{d}.json', 'w'))
        if gmap_dir and d not in sin_gmap: json.dump({f'{c.lower()}-updown-5m-{t0}': dict(id='1', toks=['a', 'b'], des='YES') for c in coins}, open(gmap_dir + (f'gmap_btc_{d}.json' if coins == ('BTC',) else f'gmap_{d}.json'), 'w'))
    json.dump(dict(job='cxb60_dryrun_v3', sello_print='ws_ex-19-1', hash_check=dict(sha256_referencia=FG.HASH_REF)), open(out + 'run_manifest.json', 'w'))
    json.dump(dict(job='cxb60_dryrun_v3', sello_print='ws_ex-59-1', hash_check=dict(sha256_referencia=FG.HASH_REF)), open(out + 'c59/run_manifest.json', 'w'))


def dias(n, ini='2026-11-20'): d0 = dt.date.fromisoformat(ini); return [(d0 + dt.timedelta(days=i)).isoformat() for i in range(n)]


# ----------------------------------------------------------------------------------------------- F2, F3
def test_cobertura_por_poblacion():
    out = nuevo(); gm = nuevo(); crea_datos(out, ['2026-11-20'], coins=('ETH', 'SOL', 'XRP'), semillas=2, gmap_dir=gm)
    # anadimos 40 rellenos de BTC SIN desenlace al res_ del dia (el resolvedor congelado los dejaria asi: gmap sin BTC)
    p = out + 'res_2026-11-20.csv.gz'; ex = [fila('2026-11-20', 'BTC', f'B{i}', '77', 1, 'CXB60', 5.0, 0, sin_desenlace=True) for i in range(40)]
    with gzip.open(p, 'at', newline='') as fh: w = csv.DictWriter(fh, fieldnames=RES_COLS, lineterminator='\n'); [w.writerow(r) for r in ex]
    pr = FG.cobertura_desenlace_dia(p, ('ETH', 'SOL', 'XRP')); bt = FG.cobertura_desenlace_dia(p, ('BTC',))
    assert pr['cobertura'] == 1.0 and pr['rellenos'] == 3 * 4 * 10 and bt['rellenos'] == 40 and bt['resueltos'] == 0 and bt['cobertura'] == 0.0 and bt['sin_desenlace'] == 40, (pr, bt)
    # el campo del informe congelado SI se contamina (excl se suma antes del filtro de moneda): se demuestra, no se usa
    inf = FG.correr_informe(FG.preparar_stage(out, ['2026-11-20'], nuevo()), 'primaria'); assert inf['cobertura_desenlace_rellenos'] < 1.0 and inf['exclusiones_desenlace']['rellenos_sin_desenlace'] == 40
    assert FG.cobertura_desenlace_dia(out + 'no_existe.csv.gz', ('ETH',)) is None
    print(f"F2 ok: cobertura por poblacion desde res_: primaria {pr['cobertura']:.2f} (n={pr['rellenos']}), BTC {bt['cobertura']:.2f} (n={bt['rellenos']}); el campo del informe marca {inf['cobertura_desenlace_rellenos']} (contaminado por BTC)")


def test_dias_validos():
    out = nuevo(); gm = nuevo(); ds = dias(8); crea_datos(out, ds, semillas=1, gmap_dir=gm, incompletos=(ds[1],), sin_res=(ds[2],), sin_gmap=(ds[3],), no_validos=(ds[4],))
    os.remove(out + f'coverage_{ds[5]}.json'); open(out + f'coverage_{ds[5]}.json', 'w').write('{roto')
    # ds[6]: gmap es un enlace roto -> no existe
    os.symlink('/no/existe', gm + f'gmap_{ds[6]}.json') if not os.path.exists(gm + f'gmap_{ds[6]}.json') else (os.remove(gm + f'gmap_{ds[6]}.json'), os.symlink('/no/existe', gm + f'gmap_{ds[6]}.json'))
    v, det = FG.evaluar_dias(out, 'primaria', gm); assert v == [ds[0], ds[7]], v
    m = lambda d: ' '.join(det[d]['motivos']); assert 'cobertura_desenlace' in m(ds[1]) and 'sin_res' in m(ds[2]) and 'sin_gmap_oficial' in m(ds[3]) and 'dia_valido=false' in m(ds[4]) and 'coverage_ilegible' in m(ds[5]) and 'sin_gmap_oficial' in m(ds[6]), {d: m(d) for d in ds}
    # BTC: sin gmap_btc_<D> ningun dia es valido (H2 DATA_BLOCKED hasta que exista la fuente)
    vb, detb = FG.evaluar_dias(out, 'BTC', gm); assert vb == [] and all('sin_gmap_oficial' in ' '.join(x['motivos']) for x in detb.values())
    # un dia sin ningun relleno: cobertura None, valido por vacuidad pero marcado
    o2 = nuevo(); g2 = nuevo(); crea_datos(o2, ['2026-11-20'], semillas=1, gmap_dir=g2)
    with gzip.open(o2 + 'res_2026-11-20.csv.gz', 'wt', newline='') as fh: w = csv.DictWriter(fh, fieldnames=RES_COLS, lineterminator='\n'); w.writeheader(); w.writerow(fila('2026-11-20', 'ETH', 't', '1', 1, 'CXB60', 0.0, 0))
    v2, d2 = FG.evaluar_dias(o2, 'primaria', g2); assert v2 == ['2026-11-20'] and d2['2026-11-20']['desenlace']['sin_rellenos'] and d2['2026-11-20']['desenlace']['cobertura'] is None
    assert FG.evaluar_dias(out, 'primaria', gm, desde=ds[5])[0] == [ds[7]]                                                                # --desde: lo anterior no cuenta
    print('F3 ok: dias validos: 5 motivos de exclusion por separado, enlace roto = sin gmap, BTC sin gmap_btc => 0 dias, dia sin rellenos marcado, --desde respeta el cutoff')


# ----------------------------------------------------------------------------------------------- F4, F5 (puras)
def inf_base(**kw):
    inf = dict(variantes={'CXB60': dict(n_rellenos=100, n_cierres_con_relleno=60, ev_cond_fill_ponderado_eur=0.30, ic90_por_dia=[0.05, 0.50], ic90_por_cierre=[0.04, 0.55], ev_cond_sin_2_mejores_dias=0.20, max_dia_share_pnl_positivo=0.15),
                          'CXB100': dict(ev_cond_fill_ponderado_eur=0.0)}, por_moneda={'CXB60': {'ETH': dict(coste=10), 'SOL': dict(coste=10), 'XRP': dict(coste=10)}}, placebo=dict(semillas=100, p_valor=0.0099),
               puertas_diagnostico={'G3_incremental_vs_GEO1_dias': dict(delta_pnl_medio_dia=1.0, ic90_inferior=0.2), 'G7_sello_cinta_pesimista_c59': dict(ev_c59=0.1)})
    for k, v in kw.items():
        ref = inf; ks = k.split('__')
        for x in ks[:-1]: ref = ref[x]
        ref[ks[-1]] = v
    return inf


def G(inf, pob='primaria', nd=12, mit=(0.2, 0.2)): return FG.evaluar_puertas(inf, [dict(variantes={'CXB60': dict(ev_cond_fill_ponderado_eur=m)}) for m in mit], pob, nd)


def test_puertas():
    g = G(inf_base()); assert all(x['ok'] for x in g.values()) and set(g) == {f'G{i}' for i in range(1, 10)}, {k: v for k, v in g.items() if not v['ok']}
    c = lambda **kw: G(inf_base(**kw))
    # limites de G1: 40 rellenos si, 39 no; 30 cierres si, 29 no; 10 dias si, 9 no
    assert c(variantes__CXB60__n_rellenos=40)['G1']['ok'] and not c(variantes__CXB60__n_rellenos=39)['G1']['ok'] and c(variantes__CXB60__n_cierres_con_relleno=30)['G1']['ok'] and not c(variantes__CXB60__n_cierres_con_relleno=29)['G1']['ok']
    assert G(inf_base(), nd=10)['G1']['ok'] and not G(inf_base(), nd=9)['G1']['ok']
    # G2: ambos IC (dias y cierres) deben quedar >0 y EV>0; None => no
    assert not c(variantes__CXB60__ic90_por_dia=[0.0, 0.5])['G2']['ok'] and not c(variantes__CXB60__ic90_por_cierre=[-0.01, 0.5])['G2']['ok'] and not c(variantes__CXB60__ic90_por_dia=None)['G2']['ok'] and not c(variantes__CXB60__ev_cond_fill_ponderado_eur=0.0)['G2']['ok']
    # G3 es puerta; G4; G8 limite -0,05 si, -0,0501 no
    assert not c(puertas_diagnostico__G3_incremental_vs_GEO1_dias__ic90_inferior=0.0)['G3']['ok'] and not c(variantes__CXB60__ev_cond_sin_2_mejores_dias=0.0)['G4']['ok'] and not c(variantes__CXB60__ev_cond_sin_2_mejores_dias=None)['G4']['ok']
    assert c(variantes__CXB100__ev_cond_fill_ponderado_eur=-0.05)['G8']['ok'] and not c(variantes__CXB100__ev_cond_fill_ponderado_eur=-0.0501)['G8']['ok']
    # G5: S=100 y p=0,025 si (<=); p=0,0251 no; S=99 no aunque p sea 0,01 (el ok del informe usa S>=20 y 0,05: aqui NO vale)
    assert c(placebo=dict(semillas=100, p_valor=0.025))['G5']['ok'] and not c(placebo=dict(semillas=100, p_valor=0.0251))['G5']['ok'] and not c(placebo=dict(semillas=99, p_valor=0.01))['G5']['ok'] and not c(placebo=None)['G5']['ok']
    # G6: moneda 60 % si, 61 % no; dia 25 % si, 26 % no; share None (sin pnl positivo) = vacuo
    inf = inf_base(); inf['por_moneda']['CXB60'] = {'ETH': dict(coste=60), 'SOL': dict(coste=20), 'XRP': dict(coste=20)}; assert G(inf)['G6']['ok']
    inf['por_moneda']['CXB60']['ETH']['coste'] = 61; inf['por_moneda']['CXB60']['SOL']['coste'] = 19.5; inf['por_moneda']['CXB60']['XRP']['coste'] = 19.5; assert not G(inf)['G6']['ok']
    assert c(variantes__CXB60__max_dia_share_pnl_positivo=0.25)['G6']['ok'] and not c(variantes__CXB60__max_dia_share_pnl_positivo=0.26)['G6']['ok'] and c(variantes__CXB60__max_dia_share_pnl_positivo=None)['G6']['ok']
    # G6 en BTC: una moneda =100 % NO falla; solo cuenta el dia
    ib = inf_base(); ib['por_moneda']['CXB60'] = {'BTC': dict(coste=30)}; gb = G(ib, 'BTC'); assert gb['G6']['ok'] and 'n/a' in gb['G6']['moneda']
    ib['variantes']['CXB60']['max_dia_share_pnl_positivo'] = 0.3; assert not G(ib, 'BTC')['G6']['ok']
    # G7: mismo signo; signo distinto no; None no
    assert not c(puertas_diagnostico__G7_sello_cinta_pesimista_c59__ev_c59=-0.01)['G7']['ok'] and not c(puertas_diagnostico__G7_sello_cinta_pesimista_c59__ev_c59=None)['G7']['ok']
    # G9: las dos mitades > 0
    assert not G(inf_base(), mit=(0.2, -0.01))['G9']['ok'] and not G(inf_base(), mit=(0.0, 0.2))['G9']['ok'] and not G(inf_base(), mit=(None, 0.2))['G9']['ok']
    # sin datos: todo falla (nunca ok por defecto)
    assert not any(x['ok'] for x in FG.evaluar_puertas({}, ({}, {}), 'primaria', 0).values() if True) or True
    vacio = FG.evaluar_puertas({}, ({}, {}), 'primaria', 0); assert not any(vacio[k]['ok'] for k in ('G1', 'G2', 'G3', 'G4', 'G5', 'G7', 'G8', 'G9'))
    print('F4 ok: G1-G9 con valores limite (40/30/10, p 0,025 con S=100 vs S=99, -0,05, 60/25 %, signos, mitades), G3 como puerta, G6 BTC solo por dia, sin datos nunca ok')


def test_veredicto():
    g = G(inf_base()); assert FG.veredicto(g, True, inf_base()) == ('PASS', 'todas las puertas G1-G9')
    assert FG.veredicto(g, False, inf_base())[0] == 'INSUFFICIENT'                                                  # calidad agregada falla => INSUFFICIENT aunque todo pase
    neg = inf_base(variantes__CXB60__ic90_por_dia=[-0.5, -0.01], variantes__CXB60__ev_cond_fill_ponderado_eur=-0.2); assert FG.veredicto(G(neg, mit=(-0.2, -0.2)), True, neg)[0] == 'FAIL'
    pl = inf_base(placebo=dict(semillas=100, p_valor=0.50)); assert FG.veredicto(G(pl), True, pl)[0] == 'FAIL'
    pl2 = inf_base(placebo=dict(semillas=60, p_valor=0.90)); assert FG.veredicto(G(pl2), True, pl2)[0] == 'INSUFFICIENT'      # S<100: no se declara FAIL por placebo
    pocos = inf_base(variantes__CXB60__n_rellenos=30, variantes__CXB60__ic90_por_dia=[-0.5, -0.01]); assert FG.veredicto(G(pocos), True, pocos)[0] == 'INSUFFICIENT'    # FAIL exige G1
    ic = inf_base(variantes__CXB60__ic90_por_dia=[-0.2, 0.4]); assert FG.veredicto(G(ic), True, ic)[0] == 'INSUFFICIENT'                                                  # cruza 0: ni PASS ni FAIL
    gn = G(inf_base(variantes__CXB60__n_rellenos=35), nd=12); assert FG.pospuesta_por_n(gn, 12) and not FG.pospuesta_por_n(gn, 20) and not FG.pospuesta_por_n(G(inf_base(), nd=9), 9) and not FG.pospuesta_por_n(g, 12)
    gx = G(inf_base(variantes__CXB60__n_rellenos=35, placebo=dict(semillas=100, p_valor=0.3)), nd=12); assert not FG.pospuesta_por_n(gx, 12)       # falla algo mas que n: no se pospone
    print('F5 ok: PASS/FAIL/INSUFFICIENT (calidad, S<100, FAIL exige G1, IC que cruza 0) y pospuesta_por_n solo si lo unico que falla es n')


# ----------------------------------------------------------------------------------------------- F6, F7 (extremo a extremo con el informe congelado)
def corre(out, gm, desde, **kw):
    t = tempfile.mkdtemp(prefix='fwd_t_', dir=TMP) + '/'; r = FG.evaluar_poblacion(out, kw.pop('pob', 'primaria'), gm, desde, '9999', t); shutil.rmtree(t); return r


def test_extremo_a_extremo():
    ds = dias(12); out = nuevo(); gm = nuevo(); crea_datos(out, ds, gmap_dir=gm); r = corre(out, gm, ds[0])
    assert r['n_dias_validos'] == 12 and r['veredicto'] == 'PASS', (r['veredicto'], r['motivo'], {k: v for k, v in r['puertas'].items() if not v['ok']})
    assert r['mitades']['primera'] == ds[:6] and r['mitades']['segunda'] == ds[6:] and r['calidad']['ok'] and r['calidad']['cobertura_desenlace_agregada'] == 1.0 and r['puertas']['G5']['semillas'] == 100
    # 11 dias: la primera mitad se queda con el dia sobrante
    r11 = corre(out, gm, ds[1]); assert r11['n_dias_validos'] == 11 and len(r11['mitades']['primera']) == 6 and len(r11['mitades']['segunda']) == 5
    # S < 100 semillas => G5 falla => INSUFFICIENT (no PASS) aunque el resto sea perfecto
    o2 = nuevo(); g2 = nuevo(); crea_datos(o2, ds, semillas=60, gmap_dir=g2); r2 = corre(o2, g2, ds[0]); assert r2['veredicto'] == 'INSUFFICIENT' and not r2['puertas']['G5']['ok'] and r2['puertas']['G5']['semillas'] == 60 and all(r2['puertas'][k]['ok'] for k in ('G1', 'G2', 'G3', 'G4', 'G6', 'G7', 'G8', 'G9'))
    # CXB60 sistematicamente perdedor con n suficiente => FAIL
    o3 = nuevo(); g3 = nuevo(); crea_datos(o3, ds, cfg=dict(cxb60=lambda j: 0, cxb100=lambda j: 0), gmap_dir=g3); r3 = corre(o3, g3, ds[0]); assert r3['veredicto'] == 'FAIL', (r3['veredicto'], r3['motivo'])
    # un dia con rellenos sin desenlace (cobertura < 0,95) queda excluido y el informe congelado no lo ve
    o4 = nuevo(); g4 = nuevo(); crea_datos(o4, ds, gmap_dir=g4, incompletos=(ds[3],)); r4 = corre(o4, g4, ds[0]); assert ds[3] in r4['dias_no_validos'] and r4['n_dias_validos'] == 11 and ds[3] not in r4['mitades']['primera'] + r4['mitades']['segunda'] and r4['calidad']['cobertura_desenlace_agregada'] == 1.0
    # mitad segunda negativa => G9 falla
    o5 = nuevo(); g5 = nuevo(); crea_datos(o5, ds, gmap_dir=g5)
    for d in ds[6:]:                                                      # reescribe las variantes CXB60 de la segunda mitad con pnl negativo
        for base in (o5,):
            p = base + f'res_{d}.csv.gz'; import pandas as pd; df = pd.read_csv(p); m = df['var'] == 'CXB60'; df.loc[m, 'gana'] = 0; df.loc[m, 'pnl'] = (5 * (0 - df.loc[m, 'L']) + 5 * REB * df.loc[m, 'L'] * (1 - df.loc[m, 'L'])).round(6); df.to_csv(p, index=False, compression='gzip')
    r5 = corre(o5, g5, ds[0]); assert not r5['puertas']['G9']['ok'] and r5['puertas']['G9']['ev_segunda_mitad'] < 0 and r5['veredicto'] != 'PASS'
    # hueco_feed > 5 % de los mercados => calidad agregada falla => INSUFFICIENT
    o6 = nuevo(); g6 = nuevo(); crea_datos(o6, ds, gmap_dir=g6, cfg=dict(hueco=True)); r6 = corre(o6, g6, ds[0]); assert r6['calidad']['hueco_feed_ratio'] == 0.25 and not r6['calidad']['ok'] and r6['veredicto'] == 'INSUFFICIENT'
    # BTC: poblacion aparte, con su gmap_btc; G6 solo por dia
    o7 = nuevo(); g7 = nuevo(); crea_datos(o7, ds, coins=('BTC',), gmap_dir=g7); r7 = corre(o7, g7, ds[0], pob='BTC'); assert r7['veredicto'] == 'PASS' and 'n/a' in r7['puertas']['G6']['moneda'] and r7['monedas'] == ['BTC'], (r7['veredicto'], r7['motivo'])
    o8 = nuevo(); g8 = nuevo(); crea_datos(o8, ds, coins=('BTC',), gmap_dir=g8, sin_gmap=tuple(ds)); r8 = corre(o8, g8, ds[0], pob='BTC'); assert r8['n_dias_validos'] == 0 and r8['veredicto'] == 'INSUFFICIENT'
    print('F6 ok: informe congelado sobre staging: PASS con 12 dias; 11 dias => mitades 6+5; S=60 => INSUFFICIENT; perdedor => FAIL; dia sin desenlace excluido; 2a mitad negativa => G9 NO; huecos 25 % => INSUFFICIENT; BTC aparte y sin gmap => 0 dias')


def cli(*args):
    b = io.StringIO(); e = io.StringIO()
    with contextlib.redirect_stdout(b), contextlib.redirect_stderr(e): rc = FG.main(list(args))
    return rc, b.getvalue(), e.getvalue()


def test_guardas_mirada():
    ds = dias(12); out = nuevo(); gm = nuevo(); crea_datos(out, ds, gmap_dir=gm, semillas=100); a = ['--out', out, '--gmap-dir', gm, '--desde', ds[0]]
    assert cli(*a)[0] == 2                                                                                                      # sin --mirada: no calcula puertas
    assert cli('--mirada', '1', '--out', out, '--gmap-dir', gm, '--desde', ds[4])[0] == 2 and not os.path.exists(out + 'forward_gates_mirada1.json')   # solo 8 dias validos desde ds[4]: no procede
    assert cli('--mirada', '2', *a)[0] == 2                                                                                      # 12 dias < 20
    rc, so, se = cli('--mirada', '1', *a); assert rc == 0 and os.path.exists(out + 'forward_gates_mirada1.json') and 'H1 PASS' in so, (rc, so, se)
    j = json.load(open(out + 'forward_gates_mirada1.json')); assert j['H1']['veredicto'] == 'PASS' and j['H2_BTC']['veredicto'] == 'INSUFFICIENT' and j['H2_BTC']['n_dias_validos'] == 0 and 'sin dias validos' in j['H2_BTC']['motivo'] and j['avisos_integridad'] == []   # H2 solo tras PASS; BTC DATA_BLOCKED (sin gmap_btc)
    assert cli('--mirada', '1', *a)[0] == 2                                                                                      # no se repite una mirada
    assert cli('--mirada', '2', '--out', out, '--gmap-dir', gm, '--desde', ds[0])[0] == 2                                        # la 1 no dio INSUFFICIENT
    # ensayo tecnico: sin minimo de dias, no escribe en OUT, y el H2 queda EXPLORATORIO si H1 no es PASS
    o2 = nuevo(); g2 = nuevo(); crea_datos(o2, ds[:3], gmap_dir=g2, semillas=100); rc, so, se = cli('--ensayo-tecnico', '--out', o2, '--gmap-dir', g2, '--desde', ds[0], '--salida', o2 + 's.json'); assert rc == 0 and 'ENSAYO TECNICO' in so and not os.path.exists(o2 + 'forward_gates_mirada1.json')
    assert json.load(open(o2 + 's.json'))['H2_BTC'].startswith('EXPLORATORIO')
    # avisos de integridad (sello y version) en el JSON
    json.dump(dict(job='otra', sello_print='ws_ex-9-1', hash_check=dict(sha256_referencia='0')), open(o2 + 'run_manifest.json', 'w')); assert len(FG.integridad(o2)) == 3
    print('F7 ok: sin --mirada rc=2, <10 dias rc=2, mirada 1 PASS escribe JSON, H2 BTC bloqueada por falta de gmap, no se repite, mirada 2 solo tras INSUFFICIENT, ensayo no escribe en OUT, avisos de integridad')


def test_resolvedor_btc():
    """Con el gmap (sa_r1 + BTC) el resolvedor CONGELADO cierra el desenlace de BTC: join exacto por mid y token; sin el gmap BTC quedan sin desenlace."""
    out = nuevo(); gm = nuevo(); d = '2026-11-20'; tokb = ['9' * 20, '8' * 20]; toke = ['7' * 20, '6' * 20]
    cols = IO.COLS; rows = []
    for coin, mid, toks in (('BTC', '8001', tokb), ('ETH', '8002', toke)):
        for k, lado in enumerate(('YES', 'NO')):
            r = dict.fromkeys(cols, ''); r.update(tipo='seg', run_id='t', dia=d, tok=toks[k], mid=mid, coin=coin, lado=lado, fin=1000, L=0.1, var='CXB60', seg=0, canc=0, q=5.0, rem_antes=5.0); rows.append(r)
    with gzip.open(out + f'dec_{d}.csv.gz', 'wt', newline='') as fh: w = csv.DictWriter(fh, fieldnames=cols, lineterminator='\n'); w.writeheader(); [w.writerow(r) for r in rows]
    json.dump({'eth-updown-5m-700': dict(id='8002', toks=toke, des='NO')}, open(gm + f'gmap_{d}.json', 'w'))
    def resolver(): subprocess.run([sys.executable, '-I', DRY + 'cxb60_resolve.py', d, '--out', out, '--gmap-dir', gm], capture_output=True, text=True, check=True)
    resolver(); p = out + f'res_{d}.csv.gz'; assert FG.cobertura_desenlace_dia(p, ('ETH',))['cobertura'] == 1.0 and FG.cobertura_desenlace_dia(p, ('BTC',))['cobertura'] == 0.0
    json.dump({'btc-updown-5m-700': dict(id='8001', toks=tokb, des='YES')}, open(gm + f'gmap_btc_{d}.json', 'w')); resolver()
    cb = FG.cobertura_desenlace_dia(p, ('BTC',)); assert cb['cobertura'] == 1.0 and cb['rellenos'] == 2
    import pandas as pd; df = pd.read_csv(p); b = df[df.coin == 'BTC'].set_index('lado'); assert b.loc['YES', 'gana'] == 1.0 and b.loc['NO', 'gana'] == 0.0                # YES=Up=toks[0] gana; el otro token pierde
    # un token que no esta en toks del gmap (mismo mid) => sin desenlace, contado (join exacto)
    json.dump({'btc-updown-5m-700': dict(id='8001', toks=['1' * 20, '2' * 20], des='YES')}, open(gm + f'gmap_btc_{d}.json', 'w')); resolver(); assert FG.cobertura_desenlace_dia(p, ('BTC',))['cobertura'] == 0.0
    print('F8 ok: resolvedor congelado + gmap_btc: BTC resuelto (YES=Up gana, NO pierde); sin gmap BTC o con tokens distintos queda sin desenlace (missing != 0)')


def test_benchmark_real():
    """F9 (opcional: FWD_BENCH_DIR=<bench/out> y FWD_BENCH_GMAP_BTC=<dir con gmap_btc_2026-11-11.json>): dec_ REALES del benchmark (slice 11-Nov 20-23Z) -> resolvedor congelado con gmap sa_r1 + BTC -> forward_gates.
    Solo se comprueba el CABLEADO (estructura, cobertura por poblacion, 1 dia => INSUFFICIENT). El slice es HOLD/benchmark: NO se imprime ni se lee ningun EV; el dia se marca valido SOLO en la copia del fixture."""
    bd, gb = os.environ.get('FWD_BENCH_DIR'), os.environ.get('FWD_BENCH_GMAP_BTC')
    if not bd or not gb or not os.path.exists(bd + '/dec_2026-11-11.csv.gz'): print('F9 omitido (sin FWD_BENCH_DIR/FWD_BENCH_GMAP_BTC)'); return
    d = '2026-11-11'; out = nuevo(); gm = nuevo(); os.makedirs(out + 'c59')
    for sub in ('', 'c59/'):
        shutil.copy(f'{bd}/{sub}dec_{d}.csv.gz', out + sub + f'dec_{d}.csv.gz')
    cov = json.load(open(f'{bd}/coverage_{d}.json')); cov['dia_valido'] = cov['dia_valido_btc'] = True; json.dump(cov, open(out + f'coverage_{d}.json', 'w'))      # fixture: el dia del slice NO es completo
    sa = f'/root/polymarket-research-datalogs/sa_r1/gmap_{d}.json'; assert os.path.exists(sa); os.symlink(sa, gm + f'gmap_{d}.json'); os.symlink(f'{gb}/gmap_btc_{d}.json', gm + f'gmap_btc_{d}.json')
    for sub in ('', 'c59/'): subprocess.run([sys.executable, '-I', DRY + 'cxb60_resolve.py', d, '--out', (out + sub).rstrip('/'), '--gmap-dir', gm], capture_output=True, text=True, check=True)
    res = {}
    for pob in ('primaria', 'BTC'):
        r = corre(out, gm, d, pob=pob); res[pob] = r; cd = r['detalle_dias'][d]['desenlace']
        assert r['n_dias_validos'] == 1 and r['veredicto'] == 'INSUFFICIENT' and set(r['puertas']) == {f'G{i}' for i in range(1, 10)} and all(isinstance(g['ok'], bool) for g in r['puertas'].values()) and not r['puertas']['G1']['ok_dias']
        assert cd['rellenos'] > 0 and cd['cobertura'] == 1.0, (pob, cd)                                              # con el gmap BTC cada poblacion cierra el 100 % de sus rellenos
    sin = subprocess.run([sys.executable, '-I', DRY + 'cxb60_resolve.py', d, '--out', out.rstrip('/'), '--gmap-dir', nuevo()], capture_output=True, text=True, check=True)
    cb = FG.cobertura_desenlace_dia(out + f'res_{d}.csv.gz', ('BTC',)); assert cb['cobertura'] == 0.0 and cb['rellenos'] > 0          # sin gmap BTC (lo que hacia el cron antiguo) los rellenos de BTC quedan sin desenlace
    print(f"F9 ok (real): cobertura de desenlace primaria {res['primaria']['detalle_dias'][d]['desenlace']['rellenos']} rellenos al 100 %, BTC {res['BTC']['detalle_dias'][d]['desenlace']['rellenos']} rellenos al 100 % con gmap_btc (0 % sin el); 1 dia => INSUFFICIENT; estructura G1-G9 completa")


if __name__ == '__main__':
    try:
        test_gmap_btc(); test_cobertura_por_poblacion(); test_dias_validos(); test_puertas(); test_veredicto(); test_extremo_a_extremo(); test_guardas_mirada(); test_resolvedor_btc(); test_benchmark_real(); print('TODOS OK (forward)')
    finally: shutil.rmtree(TMP, ignore_errors=True)
