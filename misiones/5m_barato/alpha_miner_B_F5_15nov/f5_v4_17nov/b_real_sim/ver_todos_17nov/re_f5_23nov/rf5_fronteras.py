#!/usr/bin/env python3
"""rf5_fronteras.py -- FRONTERAS Y REGLA DE MIRADA de RF5E-COMB-23NOV-v1 segun ADENDA_RF5_INTERINA_24nov SEC.6 (decisiones de firma de Javi 24-Nov: POCOCK de Lan-DeMets; prevalece sobre OBF del sec.1). Constantes TRANSCRITAS de la adenda, sin recalcular.
Mirada 1 = 6.o dia VALIDO por orden de calendario (entran EXACTAMENTE los 6 primeros validos; t = 6/10 por construccion); final = 10.o dia valido; mas alla del 10.o: prereg nuevo (no hay mirada 20 d). Sin futilidad vinculante.
Estos parametros NO viven en rf5_cortes.json (sha 4e88fb3c, no se toca): viven aqui (codigo hasheado en HASHES v3). Besag-Clifford (ADENDA_RF5_NULO_INCREMENTAL_24nov sec.3, sustituye a 1500/2000 de la interina): K_max = 500 K1-K4, 500 familia A, 1500 K6 (final 0,00470 exige >= 1064); h = 20; semilla 20261124. Puro: sin IO, sin red, 0 ordenes."""
import numpy as np
SEMILLA = 20261124; H_BC = 20; K_MAX = {'K': 250, 'K6': 1100, 'A': 500}      # enmienda Javi 24-Nov (v3.1): resolucion K_max >= 5/umbral comprobada en test_rf5_fronteras
MIRADA1_DIAS = 6; FINAL_DIAS = 10
# umbrales nominales UNILATERALES (p <= umbral => cumple), adenda sec.6 D1
UMBRAL = {1: {'p_max_K1_K4': 0.02834, 'K6_alfa001': 0.00709, 'K6_alfa005': 0.03543, 'p_max_A': 0.03543, 'ic_unil': 0.03543, 'vs_azar': 0.07085},
          2: {'p_max_K1_K4': 0.02171, 'K6_alfa001': 0.00470, 'K6_alfa005': 0.02792, 'p_max_A': 0.02792, 'ic_unil': 0.02792, 'vs_azar': 0.06165}}      # clave 2 = FINAL (10 dias)
T_MULT = {1: 2.288, 2: 2.194}              # t de Student unilateral, gl = n-1 (5 y 9), adenda sec.6 (2,2876 / 2,1945)
IC_NIVEL = {1: 0.929, 2: 0.944}; DIAS_POS_MIN = {1: 4 / 6, 2: 6 / 10}      # % de dias con Delta>0: >=4/6 en la mirada 1, >=6/10 en la final
MIRADA_NOMBRE = {1: 'MIRADA_1', 2: 'FINAL'}

def pendiente(m):
    """un dia del calendario sin estado terminal (desenlace hasta D+3, BLOCKED/FAILED/PENDING, suelo pendiente): mientras exista uno ANTERIOR al 6.o valido no se mira. m = resumen de estado (rf5_run.estado)."""
    st = m.get('status')
    if st in (None, 'PENDING', 'BLOCKED', 'FAILED'): return True
    return st == 'COMPLETE' and (m.get('iv') is None or m.get('iii') in (None, 'suelo_pendiente'))

def es_valido(m): return m.get('status') == 'COMPLETE' and m.get('iv') is True and m.get('iii') == 'OK'

def decide_mirada(estado):
    """estado = {dia: resumen}. Devuelve dict(mirada 0|1|2, nombre, dias [los EXACTOS que entran], espera [dias pendientes anteriores], motivo). 0 = solo conteos.
    Valido = COMPLETE + iv + iii OK. Con >=10 validos => FINAL con los 10 primeros; con 6..9 => mirada 1 con los 6 primeros (aunque haya un 7.o); <6 => 0. Un dia pendiente ANTERIOR al ultimo dia que entraria => espera (no se mira)."""
    dv = sorted(d for d, m in estado.items() if es_valido(m)); n = len(dv)
    if n < MIRADA1_DIAS: return dict(mirada=0, nombre='SOLO_CONTEOS', dias=[], espera=[], motivo=f'{n} < {MIRADA1_DIAS} dias validos')
    m = 2 if n >= FINAL_DIAS else 1; dias = dv[:(FINAL_DIAS if m == 2 else MIRADA1_DIAS)]
    esp = sorted(d for d, mm in estado.items() if d < dias[-1] and d not in dias and pendiente(mm))
    if esp: return dict(mirada=0, nombre='ESPERA_PENDIENTES', dias=[], espera=esp, motivo=f'dias anteriores sin estado terminal: {esp}')
    return dict(mirada=m, nombre=MIRADA_NOMBRE[m], dias=dias, espera=[], motivo=None)

def ic_t_dias(vals, mirada):
    """IC por DIAS con t de Student (gl = n-1), unilateral al nivel de la mirada (nada de bootstrap percentil por dias con n<10). Devuelve (media, limite_inferior, limite_superior_al_mismo_nivel); NaN si n<2 o varianza 0."""
    v = np.asarray(vals, float); v = v[np.isfinite(v)]; n = len(v)
    if n < 2: return (float('nan'),) * 3
    from scipy import stats
    s = float(np.std(v, ddof=1)); mu = float(np.mean(v))
    if s == 0: return (mu, float('nan'), float('nan'))
    q = float(stats.t.ppf(1 - UMBRAL[mirada]['ic_unil'], n - 1)); e = q * s / np.sqrt(n); return (mu, mu - e, mu + e)

def umbral_p(familia, mirada, k6_alfa=None):
    """umbral p vinculante. familia: 'K1_K4' | 'K6' | 'A'. K6: k6_alfa 0.01 (0.05 si K1 rechazada, grafo Bretz firmado)."""
    u = UMBRAL[mirada]
    if familia == 'K1_K4': return u['p_max_K1_K4']
    if familia == 'A': return u['p_max_A']
    if familia == 'K6':
        if k6_alfa not in (0.01, 0.05): raise ValueError('k6_alfa debe ser 0.01 o 0.05')
        return u['K6_alfa001'] if k6_alfa == 0.01 else u['K6_alfa005']
    raise ValueError(familia)

def k_max(familia): return K_MAX[familia]

def resolucion_ok(familia, mirada, k6_alfa=None, k=None):
    """adenda sec.1: K_max >= 5/umbral para poder rechazar con >=4 excedencias."""
    f = {'K1_K4': 'K', 'K': 'K', 'K6': 'K6', 'A': 'A'}[familia]; km = k or K_MAX[f]; return bool(km >= 5.0 / umbral_p(familia if familia != 'K' else 'K1_K4', mirada, k6_alfa))
