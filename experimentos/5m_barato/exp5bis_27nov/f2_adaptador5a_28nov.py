#!/usr/bin/env python3
"""f2_adaptador5a_28nov.py DIA  (28-Nov, paso 3 item 3a, ANEXO3 §3 / ANEXO_V2 §5). PESADO: lanzar por scripts/cron_pesado.sh con ulimit -v 7000000, nice 19, fuera de 22:00-02:45Z. 0 ordenes, 0 red. Escribe SOLO en datalogs/exp5bis_27nov/paso3/.
ADAPTADOR 5a = re-evaluacion de las colocaciones CXB60 del dry-run (dec_DIA 'seg', cola de decisiones recibidas por RX) con el motor passT_v4 (E.run_segment, el MISMO de fn5bis_etapa1/SIM-L) y latencias de paquete_l 13-Nov:
  FORMULA C (28-Nov, REDTEAM C / ANEXO5; sustituye a la de 27-Nov L1 34/47 + L_cancel 74/111/147, que mezclaba el reloj ex del canal de usuario con t_trig rx y no sumaba decision->envio):
    t_arr_rx = t_dec_rx + D_post + L_alta_rx[moneda]            t_end_rx = t_trig_rx + D_det_a_DELETE + L_cancel_rx[moneda]   (solo filas con cancelacion cancel_bid<L y trig presente; el resto conserva su t_end grabado)
    todo leido de latencias_vigentes.json (fuente unica, sha en la salida). Brazos: central_rx por moneda (ETH/SOL/XRP; BTC no medido => 'missing', nunca 0), central con D_post p90, 119 (no medido), 147 (heredado = p90 de ALTA B2), estres 202/1320 (canal usuario P1b-28N); los valores ex-clock
    de los brazos fijos se pasan a rx sumando el (rx-ex) central de la moneda. 74 queda FUERA como central (y como brazo). Brazo 'grabado' (t_arr/t_end del dry-run) = identidad bit a bit con el replay 1c (sin guarda).
  [formula anterior, solo historico] t_arr' = t_dec_rx + L1 (34 principal / 47 robusto); t_end' = t_trig_rx + L_cancel (74 / 111 / 147).
  Es un re-TIEMPO de las decisiones grabadas (no re-decide el gate CXB60: el flujo de decisiones por RX es el grabado; declarado). L3a/L3b no intervienen en CXB60 (son del ejecutor B).
IDENTIDAD PREVIA OBLIGATORIA (brazo 'grabado': t_arr/t_end del dry-run): cada fila q_v4 debe coincidir BIT A BIT con f2_cxb60_seg_DIA.pkl (replay 1c) y los conteos por unidad (mercado,lado) deben coincidir; si no => BLOCKED y se escribe el motivo, sin tablas de brazos.
SOLO CONTEOS por unidad (mercado, lado): rellenos passT_v4 por brazo y pareado v3(grabado) vs v4; EV/pnl PRECINTADO hasta la mirada 1 (como fn5bis_etapa1; no se lee res_*.csv.gz). Moneda: la del dry-run (BTC no esta en el motor: BLOQUEADO por contrato)."""
import sys, os, json, time, gzip, csv
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE) + '/capacidad_b_27nov')
import numpy as np, pandas as pd
OUT5 = '/root/polymarket-research-datalogs/exp5bis_27nov/'
OUT3 = OUT5 + 'paso3/'
DEC = '/root/polymarket-research-datalogs/cxb60_dryrun/'
V3_DESDE = '2026-11-23'                                                          # Protocol V2 por mercado (cadena_v2v3.V3_DESDE)
L1S = (34, 47)
LCS = (74, 111, 147)                                                               # formula ANTERIOR (27-Nov): conservada solo para los tests historicos
FIJOS_EX = (('L119_no_medido', 119.0), ('L147_heredado', 147.0), ('estres_202', 202.0), ('estres_1320', 1320.0))
MONEDAS_MOTOR = ('ETH', 'SOL', 'XRP')


def lee_seg(dia, var='CXB60'):
    """Filas 'seg' del dry-run con todos los campos necesarios. Una fila corrupta se cuenta y se informa, no se descarta en silencio."""
    filas, corruptas = [], 0
    with gzip.open(DEC + f'dec_{dia}.csv.gz', 'rt', newline='') as f:
        rd = csv.reader(f); h = next(rd); ix = {c: i for i, c in enumerate(h)}
        for r in rd:
            if r[ix['tipo']] != 'seg' or r[ix['var']] != var: continue
            try:
                trig = r[ix['t_trig_rx']]
                filas.append(dict(tok=r[ix['tok']], mid=r[ix['mid']], coin=r[ix['coin']], lado=r[ix['lado']], L=float(r[ix['L']]), t_dec=int(r[ix['t_dec_rx']]), t_arr=int(r[ix['t_arr']]), t_end=int(r[ix['t_end']]),
                                  t_trig=(int(trig) if trig not in ('', None) else None), motivo=r[ix['motivo_fin']], rem=float(r[ix['rem_antes']]), q3=float(r[ix['q']] or 0.0), fin=int(r[ix['fin']])))
            except (ValueError, IndexError):
                corruptas += 1
    return filas, corruptas


def tiempos(f, L1=None, LC=None):
    """-> (t_arr, t_end) del brazo. L1/LC None = valores grabados (identidad). El cancel solo se re-tiempa si la fila tiene disparo (t_trig) y termino por cancelacion."""
    t_arr = f['t_arr'] if L1 is None else f['t_dec'] + L1
    t_end = f['t_end'] if (LC is None or f['t_trig'] is None or not f['motivo'].startswith('cancel')) else f['t_trig'] + LC
    return int(t_arr), int(t_end)


def tiempos_c(f, P):
    """Formula C. P = dict(d_post, l_alta_rx, d_det, l_cancel_rx) (ms). -> (t_arr_rx, t_end_rx). El cancel solo se re-tiempa con disparo (t_trig) y fin por cancelacion; si no, t_end grabado."""
    t_arr = f['t_dec'] + P['d_post'] + P['l_alta_rx']
    t_end = f['t_end'] if (f['t_trig'] is None or not f['motivo'].startswith('cancel')) else f['t_trig'] + P['d_det'] + P['l_cancel_rx']
    return int(round(t_arr)), int(round(t_end))


def brazos_c(LV):
    """{nombre: {moneda: P | None}} de las latencias vigentes (latencias_vigentes.carga()). None = moneda sin central medido (BTC) => la fila sale 'missing'."""
    dp50, dp90, dd = LV['D_post']['p50'], LV['D_post']['p90'], LV['D_det_a_DELETE']['p50']
    out = {}
    def central(c, dpost, lc=None):
        la, lcn, lce = LV['L_alta_central'][c], LV['L_cancel_central'][c], LV['L_cancel_central'][c]
        if la['rx_ms'] is None or lcn['rx_ms'] is None: return None
        return dict(d_post=dpost, l_alta_rx=la['rx_ms'], d_det=dd, l_cancel_rx=(lcn['rx_ms'] if lc is None else lc + (lcn['rx_ms'] - lcn['ex_ms'])))
    for nombre, dpost, lc in [('central_rx', dp50, None), ('central_dpost_p90', dp90, None)] + [(n, dp50, x) for n, x in FIJOS_EX]:
        out[nombre] = {c: central(c, dpost, lc) for c in MONEDAS_MOTOR}
    return out


def corre(E, filas, L1=None, LC=None, fc=None):
    """fc = callable moneda -> P (formula C) o None (moneda sin latencia medida: 'missing'). Sin fc: L1/LC (formula anterior) o grabado (L1=LC=None)."""
    q = []
    for f in filas:
        k = E.D.tokidx.get(f['tok'])
        if k is None: q.append(np.nan); continue                                    # fuera del motor (p.ej. BTC): 'missing', nunca 0
        if fc is not None:
            P = fc(f['coin'])
            if P is None: q.append(np.nan); continue
            ta, te = tiempos_c(f, P); q.append(float(E.run_segment(int(k), float(f['L']), ta, te, float(f['rem']), 'BASE')[0]) if ta < te else 0.0); continue
        ta, te = tiempos(f, L1, LC)
        identidad = L1 is None and LC is None                                     # brazo grabado: SIN guarda (igual que replay_dryrun, para la identidad bit a bit)
        q.append(float(E.run_segment(int(k), float(f['L']), ta, te, float(f['rem']), 'BASE')[0]) if (identidad or ta < te) else 0.0)
    return np.array(q)


def unidades(filas, q, umbral=1e-3):
    df = pd.DataFrame(dict(coin=[f['coin'] for f in filas], mid=[f['mid'] for f in filas], lado=[f['lado'] for f in filas], q=q, q3=[f['q3'] for f in filas]))
    df = df[df.q.notna()]
    return df.groupby(['coin', 'mid', 'lado']).agg(v3=('q3', lambda x: bool((x > 1e-9).any())), v4=('q', lambda x: bool((x > umbral).any()))).reset_index()


def conteos(u):
    out = {}
    for c, x in u.groupby('coin'):
        out[c] = dict(unidades=int(len(x)), v3=int(x.v3.sum()), v4=int(x.v4.sum()), ambos=int((x.v3 & x.v4).sum()), v3_no_v4_si=int((~x.v3 & x.v4).sum()), v3_si_v4_no=int((x.v3 & ~x.v4).sum()))
    return out


def construye_motor(dia):
    import piloto_m1_m4 as P
    P.puerta(P.RAM_MIN_RUN)
    sys.path.insert(0, P.BK); sys.path.insert(0, P.BKE)
    import experimento_maker_bk as BKm
    sys.path.insert(0, str(BKm.D_RF5)); sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim')
    import eng_v5 as EV
    return EV.build(dia)


def identidad_previa(E, filas, qg, dia):
    pk = OUT5 + f'f2_cxb60_seg_{dia}.pkl'
    ident = dict(referencia=pk, referencia_sha256=_sha(pk))
    if not os.path.exists(pk):
        ident.update(ok=False, motivo='BLOCKED: falta f2_cxb60_seg (replay 1c) de ese dia'); return ident
    ref = pd.read_pickle(pk)
    propios = [(f, x) for f, x in zip(filas, qg) if not np.isnan(x)]                        # el replay 1c solo guarda filas con ficha en el motor
    if len(ref) != len(propios):
        ident.update(ok=False, motivo=f'BLOCKED: filas {len(propios)} != replay 1c {len(ref)}'); return ident
    dif = int(sum(1 for (f, x), r in zip(propios, ref.q_v4.values) if x != float(r)))
    ident.update(filas=len(ref), filas_distintas_bit_a_bit=dif, ok=(dif == 0), motivo=('OK' if dif == 0 else f'BLOCKED: {dif} filas q_v4 distintas del replay 1c'))
    if dif == 0:
        u = unidades(filas, qg); cu = conteos(u)
        u_ref = ref.groupby(['coin', 'mid', 'lado']).agg(v3=('q_v3', lambda x: bool((x > 1e-9).any())), v4=('q_v4', lambda x: bool((x > 1e-3).any()))).reset_index()
        ident['conteos_adaptador'] = cu; ident['conteos_replay_1c'] = conteos(u_ref); ident['conteos_identicos'] = (cu == conteos(u_ref))
        ident['ok'] = bool(ident['conteos_identicos']); ident['motivo'] = 'OK' if ident['ok'] else 'BLOCKED: conteos por unidad distintos'
    return ident


def _sha(p):
    import hashlib
    try: return hashlib.sha256(open(p, 'rb').read()).hexdigest()
    except OSError: return 'missing'


def compute(dia, LV):
    """UNA ejecucion completa (motor nuevo, filas, identidad, brazos). -> dict SIN sellos de tiempo (determinista) con `hash_tabla`."""
    E, info = construye_motor(dia)
    filas, corruptas = lee_seg(dia)
    res = dict(dia=dia, job='f2_adaptador5a_28nov', formula='C', filas_seg=len(filas), filas_corruptas=corruptas, motor_info=info, latencias_vigentes_sha256=LV['sha256_contenido'],
               politica='re-tiempo (formula C: D_post + L_alta_rx; D_det + L_cancel_rx por moneda) de las decisiones grabadas; SOLO CONTEOS (EV precintado)')
    qg = corre(E, filas)
    ident = identidad_previa(E, filas, qg, dia)
    res['identidad_previa'] = ident
    res['cobertura_por_moneda'] = {c: dict(filas=sum(1 for f in filas if f['coin'] == c), en_motor=int(sum(1 for f, x in zip(filas, qg) if f['coin'] == c and not np.isnan(x)))) for c in sorted({f['coin'] for f in filas})}
    if ident.get('ok'):
        arms = {}
        for nombre, por_coin in brazos_c(LV).items():
            q = corre(E, filas, fc=lambda c, pc=por_coin: pc.get(c))
            arms[nombre] = dict(parametros={c: p for c, p in por_coin.items()}, conteos=conteos(unidades(filas, q)), filas_missing=int(np.isnan(q).sum()))
        res['brazos'] = arms
    avisos = []
    if dia >= V3_DESDE:
        avisos.append(f'CINTA SOLO V2 (cadena V3 no integrada en el motor eng_v5/tape): dia >= {V3_DESDE}: SOL/XRP (y demas mercados V2 de protocolo) salen con v4 ~ 0 por CEGUERA, NO por ausencia de relleno: missing != 0. Los conteos de SOL/XRP de este dia NO son evaluables hasta M4 (cinta V2+V3, cobertura >= 0,90 por moneda-dia).')
    res['avisos'] = avisos
    import hashlib
    res['hash_tabla'] = hashlib.sha256(json.dumps(dict(identidad=ident.get('conteos_adaptador'), brazos=res.get('brazos'), cobertura=res['cobertura_por_moneda']), sort_keys=True, default=str).encode()).hexdigest()
    return res


def main(dia, veces=2):
    import latencias_vigentes as LVm
    os.makedirs(OUT3, exist_ok=True)
    LV = LVm.carga()                                                                      # fail-closed si el JSON fue editado a mano
    t0 = time.time()
    R = [compute(dia, LV) for _ in range(veces)]
    res = dict(R[0]); res['hash_tabla_ejecuciones'] = [r['hash_tabla'] for r in R]; res['estable_dos_ejecuciones'] = len(set(res['hash_tabla_ejecuciones'])) == 1 and veces >= 2
    res['segundos'] = round(time.time() - t0, 1)                                           # (el tiempo y la hora van FUERA del hash)
    res['generado'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    tmp = OUT3 + f'f2_adaptador5a_C_{dia}.json.tmp'
    json.dump(res, open(tmp, 'w'), indent=1, sort_keys=True, default=str); os.replace(tmp, OUT3 + f'f2_adaptador5a_C_{dia}.json')
    print('adaptador 5a (formula C)', dia, 'identidad:', res['identidad_previa'].get('motivo'), 'estable:', res['estable_dos_ejecuciones'], res['hash_tabla'][:16], round(time.time() - t0), 's')


if __name__ == '__main__':
    main(sys.argv[1])
