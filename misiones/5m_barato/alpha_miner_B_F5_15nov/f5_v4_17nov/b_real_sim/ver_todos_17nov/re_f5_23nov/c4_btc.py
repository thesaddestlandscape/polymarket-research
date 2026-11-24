#!/usr/bin/env python3
"""c4_btc.py [--json RUTA] -- (E7, ADENDA_RF5_CRITERIOS_v2 3c / C4) verificacion AUTOMATICA de las 10 condiciones de desbloqueo de BTC. BTC sigue DATA_BLOCKED_BTC mientras alguna falle; el estado y la causa de cada una van a out_rf5_ciego/c4_btc_estado.json.
Solo lee ficheros (existencia, sha, contenidos); NO calcula EV, NO toca nada, 0 ordenes, 0 red. Las condiciones que exigen firma del chief (4, 5, 6) se leen de firmas_btc.json {cond4_adenda_cortes|cond5_contrato_e1b_12_2: {ruta, sha256}} (ruta relativa a HV o absoluta): sin fichero o sha distinto => PENDIENTE_FIRMA.
(1) btc_ms de 03-Nov a ayer (todos con tokens BTC 5min);(2) tape/bad BTC 03..17 con sha anotado;(3) B base BTC con passT_v4 en 03..17 leyendo solo f5t (salida base_btc_D.ok de un job BTC: aun NO hay simulador BTC);(4) adenda p20/p80 BTC firmada;(5) CONTRATO_E1B 12.2 BTC firmado;
(6) tabla de suelo sucesora con BTC lo-valido en todos sus dias (sha ya verificado por rf5_gates);(7) C1/C3 de BTC y 03..17 (c1c3_btc_D.json con ok:true);(8) equivalencia bit a bit lowmem vs ms_extract (equiv_lowmem_D.json igual:true y sha de los scripts vigentes);
(9) Binance BTC (m5_registro, filas x BTCUSDT) para todos los dias 03..ayer;(10) maker_ms con tokens BTC 5min en todos los dias 03..17 (de btc_ms)."""
import os, sys, json, glob, time, hashlib, subprocess, calendar
import numpy as np
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
DL = os.environ.get('RF5_DL', '/root/polymarket-research-datalogs/'); VOL = os.environ.get('RF5_VOL', '/mnt/HC_Volume_106538179'); OUT = os.environ.get('RF5_OUT', HV + 'out_rf5_ciego/'); BTCD = os.environ.get('RF5_BTC_OUT', DL + 'rf5_btc/')
DESDE = '2026-11-03'; HASTA_COEFS = '2026-11-17'

def dias(a, b):
    out = []; t = calendar.timegm(time.strptime(a, '%Y-%m-%d'))
    while time.strftime('%Y-%m-%d', time.gmtime(t)) <= b: out.append(time.strftime('%Y-%m-%d', time.gmtime(t))); t += 86400
    return out

def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def st(ok, detalle, falta=None): return dict(estado=('OK' if ok else 'PENDIENTE'), detalle=detalle, faltan=falta or [])

def tokens_btc5(p):
    try: z = np.load(p, allow_pickle=True); return sum(1 for r in z['tmap'] if str(r[0]).upper() == 'BTC' and r[1] == '5min')
    except Exception: return -1

def btc_en_m5(d, vol=None):
    p = (vol or VOL) + f'/m5_registro/m5_registro_{d}.csv.gz'
    if not os.path.exists(p): return False
    r = subprocess.run(['bash', '-c', f"zcat '{p}' 2>/dev/null | awk -F, '$1==\"x\" && $3==\"BTCUSDT\"{{print 1; exit}}'"], capture_output=True, text=True); return r.stdout.strip() == '1'

def firma(nombre, f):
    e = f.get(nombre)
    if not e: return False, 'sin firma del chief'
    p = e['ruta'] if os.path.isabs(e['ruta']) else HV + e['ruta']
    if not os.path.exists(p): return False, f'no existe {p}'
    return (sha(p) == e['sha256']), ('sha coincide' if sha(p) == e['sha256'] else f'sha != firmado ({p})')

def evalua(hasta, dl=None, btcd=None, vol=None, firmas=None, cortes=None, out=None, m5fn=None):
    dl = dl or DL; btcd = btcd or BTCD; vol = vol or VOL; m5fn = m5fn or (lambda d: btc_en_m5(d, vol)); res = {}
    todos = dias(DESDE, hasta); coefs = dias(DESDE, HASTA_COEFS)
    falta1 = [d for d in todos if tokens_btc5(dl + f'sa_ms/btc_ms_{d}.npz') <= 0]; res['1_btc_ms'] = st(not falta1, f'{len(todos) - len(falta1)}/{len(todos)} dias {DESDE}..{hasta} con btc_ms y tokens BTC 5min', falta1)
    ref = {}; refp = HV + 'TAPES_SHA256_btc.txt'
    if os.path.exists(refp):
        for l in open(refp):
            if len(l.split()) == 2: ref[l.split()[1]] = l.split()[0]
    falta2 = []
    for d in coefs:
        for f in (btcd + f'tape_btc_{d}.pkl', btcd + f'bad_btc_{d}.json'):
            if not os.path.exists(f) or ref.get(f) != sha(f): falta2.append(os.path.basename(f))
    res['2_tape_bad_btc'] = st(not falta2, f'tape/bad BTC 03..17 con sha anotado: faltan {len(falta2)}', falta2)
    f3 = [d for d in coefs if not os.path.exists(btcd + f'base_btc_{d}.ok')]; res['3_base_btc_passT_v4'] = st(not f3, 'sin simulador BTC de B base (EV.build solo ETH/SOL/XRP): hace falta un job BTC que lea SOLO f5t' if f3 else 'ok', f3)
    fi = firmas if firmas is not None else (json.load(open(HV + 'firmas_btc.json')) if os.path.exists(HV + 'firmas_btc.json') else {})
    for k, nom in (('4_adenda_p20_p80_btc', 'cond4_adenda_cortes'), ('5_contrato_e1b_12_2_btc', 'cond5_contrato_e1b_12_2')):
        ok, det = firma(nom, fi); res[k] = st(ok, det) if ok else dict(estado='PENDIENTE_FIRMA', detalle=det, faltan=[])
    try:
        import rf5_gates as GT; cx = cortes if cortes is not None else __import__('rf5_core').lee_cortes(); df, info = GT.lee_tabla_suelo(cx); ndias = sorted(df.dia.unique()) if df is not None else []
        mal = [d for d in ndias if not GT.suelo_dia(df, d, coins=('BTC',))['por_moneda'].get('BTC', {}).get('valido')]; res['6_tabla_suelo_btc_lo_valido'] = st(bool(ndias) and not mal, f'{len(ndias)} dias en la tabla firmada; BTC no valido en {len(mal)}', mal)
    except Exception as ex: res['6_tabla_suelo_btc_lo_valido'] = st(False, f'tabla suelo no legible: {ex!r}')
    f7 = []
    for d in coefs:
        p = btcd + f'c1c3_btc_{d}.json'
        try: ok7 = bool(json.load(open(p)).get('ok'))
        except Exception: ok7 = False
        if not ok7: f7.append(d)
    res['7_c1_c3_btc'] = st(not f7, 'C1/C3 de BTC en 03..17 (c1c3_btc_D.json ok:true)', f7)
    ev = sorted(glob.glob(btcd + 'equiv_lowmem_*.json')); ok8 = False; det8 = 'sin ensayo de equivalencia'
    if ev:
        try:
            j = json.load(open(ev[-1]))
            ok8 = bool(j.get('igual')) and j.get('sha_lowmem') == (sha('/root/polymarket-research/experimentos/5m_barato/b_seleccion_adversa/scripts/ms_extract_lowmem.py')); det8 = f"{os.path.basename(ev[-1])}: igual={j.get('igual')}"
        except Exception as ex: det8 = f'ilegible {ex!r}'
    res['8_equivalencia_lowmem'] = st(ok8, det8)
    f9 = [d for d in todos if not m5fn(d)]; res['9_binance_btc_m5_registro'] = st(not f9, f'{len(todos) - len(f9)}/{len(todos)} dias con filas x BTCUSDT', f9)
    f10 = [d for d in coefs if tokens_btc5(dl + f'sa_ms/btc_ms_{d}.npz') <= 0]; res['10_maker_ms_tokens_btc5_03_17'] = st(not f10, 'tokens BTC 5min en btc_ms 03..17', f10)
    ok = all(v['estado'] == 'OK' for v in res.values()); return dict(estado=('BTC_DESBLOQUEABLE (falta solo la firma del chief para abrir EV)' if ok else 'DATA_BLOCKED_BTC'), n_ok=sum(v['estado'] == 'OK' for v in res.values()), n=10, condiciones=res, hasta=hasta, t=time.strftime('%FT%TZ', time.gmtime()))

if __name__ == '__main__':
    hoy = time.strftime('%Y-%m-%d', time.gmtime()); ayer = time.strftime('%Y-%m-%d', time.gmtime(time.time() - 86400)); r = evalua(ayer); p = (sys.argv[sys.argv.index('--json') + 1] if '--json' in sys.argv else OUT + 'c4_btc_estado.json')
    os.makedirs(os.path.dirname(p), exist_ok=True); json.dump(r, open(p + '.tmp', 'w'), indent=1); os.replace(p + '.tmp', p); print(r['estado'], r['n_ok'], '/ 10')
