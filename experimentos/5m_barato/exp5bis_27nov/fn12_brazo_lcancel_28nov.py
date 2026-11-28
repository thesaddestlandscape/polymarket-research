#!/usr/bin/env python3
"""fn12_brazo_lcancel_28nov.py (28-Nov, paso 3 item 1, ANEXO3 §1). v2 (FORMULA C, ANEXO5): `tabla_c()` recalcula los 12 en TODOS los brazos con t_end_rx = t_trig_rx + D_det_a_DELETE + L_cancel_rx[moneda] leyendo latencias_vigentes.json (central por moneda, 119 no medido, 147 heredado, estres 202/1320; ex->rx con el offset medido de la moneda; 74/111 solo como columnas informativas heredadas), denominador 12, por moneda y clase de suelo; hash de fuente (fn_lista de fn5bis_dia + ordenes_K6_base) y de codigo. La tabla v1 (brazos ex-clock sobre t_cancel_dec, sin D_det) se conserva abajo solo como historico. Brazo de sensibilidad L_cancel de los 12 FN dudosos (fn_lista 18+24-Nov de exp5bis). Solo LEE los pkl/json del 27-Nov; 0 red, 0 ordenes, no mueve t_end del motor.
Definicion (dato, no hipotesis): la orden del motor (ordenes_K6_base_DIA.pkl) deja de existir en t_cancel_dec + LC; el replay uso LC=33 (ex_canc, 'repega'/'cancela_banda') o 91 ('regla'): se EMPAREJA por (mid,lado,ventana de rx del FN) como diag_fn_motor.py.
Con un LC alternativo X la orden vive hasta t_eff = t_cancel_dec + X. El FN 'flipa' (el print habria rellenado nuestra orden: el precio del print < L => el tomador barrio TODO el nivel L) si casado_est < t_eff.
casado_est = tev+20 (cota baja, 'lo') / tev+41 (cota alta, 'hi'), en el reloj de recepcion (campos casado_rx_est_{lo,hi}_menos_t_end_ms del fn_lista; tev = evento exchange del tx; NO se usa bloque).
flip_seguro = casado_hi < t_eff ; flip_posible = casado_lo < t_eff <= casado_hi (depende de rx-casado, 20-41 ms); sin_flip = casado_lo >= t_eff.
Brazos: base_motor (33/91 tal como corrio), 74/111/147 (L_cancel paquete_l 13-Nov por clase, ANEXO V2 §3), ESTRES 202 (p50) y 1320 (p90) = cancel_ex-envio P1b-28N (informativo: ver diagnostico_latencia_p1b: es lag de publicacion del WS, no tiempo efectivo; cota HTTP DELETE p50 65 no flipa nada).
El 'offset_arr' no depende de LC (el casado es anterior a t_arr): se reporta 'ambigua irreducible'. El 'no_armable' no cuenta. Clase de suelo: la columna `clase` del pkl (todas 'lo'; 0 'hi' => sin sensibilidad hi posible)."""
import hashlib, json, os, sys
import pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
O = '/root/polymarket-research-datalogs/exp5bis_27nov/'
BRAZOS = [74, 111, 147, 202, 1320]


def tabla(dias=('2026-11-18', '2026-11-24'), O=O):
    rows = []
    for dia in dias:
        R = pd.read_pickle(O + f'ordenes_K6_base_{dia}.pkl'); d = json.load(open(O + f'fn5bis_dia_{dia}.json'))
        for f in d['fn_lista']:
            if f['clase_fn'] == 'no_FN_no_armable': continue
            m = R[(R.mid == f['mid']) & (R.lado == f['lado']) & (R.t_arr - 300 <= f['rx']) & (f['rx'] <= R.t_end + 300)]
            if len(m) != 1: raise SystemExit(f'emparejado ambiguo {dia} {f["mid"]} {f["lado"]}: {len(m)} ordenes')
            r = m.iloc[0]; lo = f['casado_rx_est_lo_menos_t_end_ms']; hi = f['casado_rx_est_hi_menos_t_end_ms']
            base = int(r.t_end - r.t_cancel_dec)
            fila = dict(dia=dia, coin=f['coin'], mid=f['mid'], lado=f['lado'], L=float(r.L), price_print=float(f['price']), qty_print=float(f['qty']), size=float(r['size']), clase=r.clase, motivo_fin=r.motivo_fin,
                        causa=f['causa'], duro=bool(f['price'] < float(r.L) - 0.0006), lc_base=base, casado_lo_menos_tend=lo, casado_hi_menos_tend=hi)
            for X in BRAZOS:
                if f['causa'].startswith('offset_arr'):
                    fila[f'L{X}'] = 'ambigua_irreducible'; continue
                ext = X - base                                   # prolongacion de la vida de la orden respecto del replay
                fila[f'L{X}'] = 'flip_seguro' if hi < ext else ('flip_posible' if lo < ext else 'sin_flip')
            rows.append(fila)
    return pd.DataFrame(rows)


def resumen(T):
    out = {}
    for X in BRAZOS:
        c = T[f'L{X}'].value_counts().to_dict(); out[f'L{X}'] = {k: int(v) for k, v in c.items()}
        out[f'L{X}']['denominador'] = int(len(T))
    out['por_moneda_L147'] = {cn: T[T.coin == cn]['L147'].value_counts().to_dict() for cn in sorted(T.coin.unique())}
    out['clases'] = T.clase.value_counts().to_dict()
    return out


# ------------------------------------------------------------------------------------------------ v2: FORMULA C
FIJOS_EX = (('L119_no_medido', 119.0), ('L147_heredado', 147.0), ('estres_202', 202.0), ('estres_1320', 1320.0))
HEREDADOS_INFORMATIVOS = (('L74_heredado', 74.0), ('L111_heredado', 111.0))


def _sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def clasifica(lo, hi, ext, causa):
    """ext = prolongacion (ms) de la vida de la orden respecto del t_end del replay. flip_seguro: el casado MAS TARDIO (hi) cae antes del nuevo t_end; flip_posible: solo el mas temprano (lo)."""
    if causa.startswith('offset_arr'):
        return 'ambigua_irreducible'
    return 'flip_seguro' if hi < ext else ('flip_posible' if lo < ext else 'sin_flip')


def tabla_c(LV, dias=('2026-11-18', '2026-11-24'), O=O):
    """-> DataFrame de los 12 FN dudosos con una columna por brazo de la formula C. `ext = (D_det + L_cancel_rx) - base`, base = t_end - t_cancel_dec del replay (33/91 ms)."""
    rows = []
    dd = LV['D_det_a_DELETE']['p50']
    for dia in dias:
        R = pd.read_pickle(O + f'ordenes_K6_base_{dia}.pkl'); d = json.load(open(O + f'fn5bis_dia_{dia}.json'))
        for f in d['fn_lista']:
            if f['clase_fn'] == 'no_FN_no_armable': continue
            m = R[(R.mid == f['mid']) & (R.lado == f['lado']) & (R.t_arr - 300 <= f['rx']) & (f['rx'] <= R.t_end + 300)]
            if len(m) != 1: raise SystemExit(f'emparejado ambiguo {dia} {f["mid"]} {f["lado"]}: {len(m)} ordenes')
            r = m.iloc[0]; lo = f['casado_rx_est_lo_menos_t_end_ms']; hi = f['casado_rx_est_hi_menos_t_end_ms']; base = int(r.t_end - r.t_cancel_dec); coin = f['coin'].upper()
            cc = LV['L_cancel_central'][coin]; off = (cc['rx_ms'] - cc['ex_ms']) if cc['rx_ms'] is not None else None
            fila = dict(dia=dia, coin=coin, mid=f['mid'], lado=f['lado'], L=float(r.L), price_print=float(f['price']), qty_print=float(f['qty']), size=float(r['size']), clase=r.clase, motivo_fin=r.motivo_fin,
                        causa=f['causa'], duro=bool(f['price'] < float(r.L) - 0.0006), lc_base=base, casado_lo_menos_tend=lo, casado_hi_menos_tend=hi)
            arms = [('central_rx', cc['rx_ms'])] + [(n, (x + off) if off is not None else None) for n, x in FIJOS_EX + HEREDADOS_INFORMATIVOS]
            for n, lcrx in arms:
                fila[n] = 'missing' if lcrx is None else clasifica(lo, hi, dd + lcrx - base, f['causa'])
                fila['L_' + n] = lcrx
            rows.append(fila)
    return pd.DataFrame(rows)


def resumen_c(T, LV, fuentes):
    brazos = ['central_rx'] + [n for n, _ in FIJOS_EX] + [n for n, _ in HEREDADOS_INFORMATIVOS]
    out = dict(formula='C', denominador=int(len(T)), latencias_vigentes_sha256=LV['sha256_contenido'], fuentes=fuentes, clases_suelo=T.clase.value_counts().to_dict(), por_coin_n=T.coin.value_counts().to_dict(),
               D_det_a_DELETE_ms=LV['D_det_a_DELETE']['p50'], brazos={})
    for b in brazos:
        out['brazos'][b] = dict(total={k: int(v) for k, v in T[b].value_counts().items()}, por_moneda={c: {k: int(v) for k, v in T[T.coin == c][b].value_counts().items()} for c in sorted(T.coin.unique())},
                                por_clase={c: {k: int(v) for k, v in T[T.clase == c][b].value_counts().items()} for c in sorted(T.clase.unique())}, L_cancel_rx_por_moneda={c: (None if T[T.coin == c]['L_' + b].isna().all() else round(float(T[T.coin == c]['L_' + b].iloc[0]), 3)) for c in sorted(T.coin.unique())})
        out['brazos'][b]['rotulo'] = 'central medido por moneda' if b == 'central_rx' else ('informativo heredado (74/111: fuera como central)' if b in dict(HEREDADOS_INFORMATIVOS) else 'brazo fijo heredado/no medido/estres (ex -> rx con el offset central de la moneda)')
    return out


def main_c(dias=('2026-11-18', '2026-11-24')):
    import latencias_vigentes as LVm
    LV = LVm.carga(); T = tabla_c(LV, dias)
    fuentes = {os.path.basename(f): _sha(f) for dia in dias for f in (O + f'ordenes_K6_base_{dia}.pkl', O + f'fn5bis_dia_{dia}.json')}
    fuentes['fn12_brazo_lcancel_28nov.py'] = _sha(os.path.abspath(__file__))
    R = resumen_c(T, LV, fuentes)
    T.to_csv(O + 'paso3/fn12_formulaC.csv', index=False); json.dump(R, open(O + 'paso3/fn12_formulaC.json', 'w'), indent=1, sort_keys=True, default=int)
    pd.set_option('display.width', 250); print(T[['dia', 'coin', 'clase', 'causa', 'duro', 'lc_base', 'casado_lo_menos_tend', 'casado_hi_menos_tend', 'central_rx', 'L119_no_medido', 'L147_heredado', 'estres_202', 'estres_1320']].to_string()); print(json.dumps({b: v['total'] for b, v in R['brazos'].items()}, indent=1))
    return T, R


if __name__ == '__main__':
    if '--v1' not in sys.argv:
        main_c(); sys.exit(0)
    T = tabla(); R = resumen(T)
    T.to_csv(O + 'paso3/fn12_brazo_lcancel.csv', index=False); json.dump(R, open(O + 'paso3/fn12_brazo_lcancel.json', 'w'), indent=1, default=int)
    pd.set_option('display.width', 250); print(T.drop(columns=['mid', 'causa']).to_string()); print(json.dumps(R, indent=1, default=int))
