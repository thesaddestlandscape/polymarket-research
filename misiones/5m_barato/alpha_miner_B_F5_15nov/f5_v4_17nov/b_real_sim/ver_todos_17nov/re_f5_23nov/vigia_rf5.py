#!/usr/bin/env python3
"""vigia_rf5.py [--telegram] [--aviso-fallo] -- vigia diario de RF5E-COMB-23NOV-v1 (prereg 16be06b6). Solo lee manifests/heartbeat/ficheros de fuente: NO calcula EV, NO toca nada.
Estados por dia >=18-Nov: COMPLETE | INCOMPLETE (+motivo; terminal) | PENDING (<=48 h) | BLOCKED | FAILED | SIN_MANIFEST. Avisos (latch por firma SIN valores recalculados cada ciclo):
  R1 el runner lleva >26 h sin correr (heartbeat.json); R2 a una fuente de un dia NO cerrado le quedan <=2 dias de retencion; R3 volumen HC < 15 GB libres; R4 PENDING >48 h; R5 dias FAILED/BLOCKED; R6 el juez Calma v4 (run_k6.sh, cron 11:50Z) lleva >26 h sin correr (heartbeat_k6.json; solo si ya hay algun dia COMPLETE); R7 manifest rf5K6 FAILED/BLOCKED.
Tambien resume el estado de BTC (c4_btc_estado.json: n de 10 condiciones).
Resumen diario: cuenta de dias validos (COMPLETE con criterio (iv) y (iii)) y estado por dia. Helper de Telegram: shadow_digest.enviar_telegram. Con --telegram envia; sin el, imprime. RF5_SIN_TELEGRAM=1: solo imprime."""
import os, sys, json, time, shutil, glob
HV = os.path.dirname(os.path.abspath(__file__)) + '/'
OUT = os.environ.get('RF5_OUT', HV + 'out_rf5_ciego/'); LATCH = OUT + 'vigia_latch.json'
VOL = os.environ.get('RF5_VOL', '/mnt/HC_Volume_106538179'); MIN_LIBRE_GB = 15.0; HB_MAX_H = 26.0; PEND_MAX_H = 48.0; QUEDAN_MAX_D = 2
DESDE = '2026-11-18'; DLR = '/root/polymarket-research-datalogs/'
# fuente -> (patron, dias de retencion desde la fecha del NOMBRE; None = sin retencion conocida). Verificado 23-Nov en scripts/comprimir_data_historica.sh y archivo_volumen.py. Solo las fuentes con retencion son riesgo;
# libro5_ms crudo (14 d) NO es entrada de este pipeline (solo rasgos L2 de R1v2) y maker_ms de datalogs se COPIA al volumen a +4 d (no se pierde). Las demas se vigilan solo por existencia (informativo).
FUENTES = {'maker_ms (copia volumen, mtime +30 d)': (VOL + '/maker_ms_crudo/maker_ms_{d}_*.csv.gz', 30), 'm5_registro': (VOL + '/m5_registro/m5_registro_{d}.csv.gz', 60),
           'sa_ms v1': (DLR + 'sa_ms/ms_{d}.npz', None), 'sa_ms2': (DLR + 'sa_ms2/ms2_{d}.npz', None), 'libro5_tx': (VOL + '/libro5_tx/libro5_tx_{d}_*.csv*', None), 'onchain keep': (VOL + '/mover_09nov/keep_onchain_re_as_b/onchain_fills_{d}*.csv.gz', None)}

def hoy(): return time.strftime('%Y-%m-%d', time.gmtime())
def dmas(d, n): return time.strftime('%Y-%m-%d', time.gmtime(time.mktime(time.strptime(d, '%Y-%m-%d')) + n * 86400 + 7200))
def ddif(a, b): return int(round((time.mktime(time.strptime(a, '%Y-%m-%d')) - time.mktime(time.strptime(b, '%Y-%m-%d'))) / 86400))

def lee_estado(out=None):
    out = out or OUT; est = {}
    for f in sorted(glob.glob(out + 'manifest_rf5dia_*.json')):
        try: m = json.load(open(f)); est[m['dia']] = m
        except Exception: est[os.path.basename(f)[len('manifest_rf5dia_'):-5]] = dict(status='FAILED', motivo='manifest ilegible')
    return est

def dias_calendario(hasta=None, desde=DESDE):
    hasta = hasta or hoy(); d = desde; L = []
    while d < hasta: L.append(d); d = dmas(d, 1)
    return L

def es_valido(m): return m.get('status') == 'COMPLETE' and m.get('criterio_iv_ok') is True and m.get('criterio_iii_suelo') == 'OK'

def edad_pend_h(m, ahora=None):
    """horas desde que el dia se vio PENDING por primera vez (primer_visto lo conserva el runner entre intentos)."""
    import calendar
    t = m.get('primer_visto') or m.get('t_ini') or m.get('t_fin')
    return 0.0 if not t else ((ahora or time.time()) - calendar.timegm(time.strptime(t[:19], '%Y-%m-%dT%H:%M:%S'))) / 3600.0

def retencion_riesgo(est, hoy_=None, fuentes=None, desde=DESDE):
    """Dias NO cerrados (sin manifest o PENDING/BLOCKED/FAILED) y sus d-1,d,d+1: fuentes CON retencion cuyo fichero existe y se borra (fecha del nombre + retencion) en <=2 dias. Devuelve [(dia, fuente, quedan_dias)]."""
    hoy_ = hoy_ or hoy(); fuentes = fuentes or FUENTES; out = set()
    for d in dias_calendario(desde=desde, hasta=dmas(hoy_, 1)):
        m = est.get(d)
        if m and m.get('status') in ('COMPLETE', 'INCOMPLETE'): continue
        for x in (dmas(d, -1), d, dmas(d, 1)):
            for nom, (pat, ret) in fuentes.items():
                if ret is None or not glob.glob(pat.format(d=x)): continue
                quedan = ddif(dmas(x, ret), hoy_)
                if quedan <= QUEDAN_MAX_D: out.add((d, nom, quedan))
    return sorted(out)

def avisos(est, hb, libre_gb, hoy_=None, ahora=None, fuentes=None):
    """Lista de (firma_estable, texto). Las firmas no incluyen valores que cambien cada ciclo."""
    A = []; ahora = ahora or time.time()
    if hb is None or (ahora - hb.get('epoch', 0)) / 3600.0 > HB_MAX_H: A.append(('R1_runner_parado', f"RF5: el runner lleva >{HB_MAX_H:.0f} h sin correr (heartbeat {None if hb is None else hb.get('t')}). Revisar cron run_rf5.sh / out_rf5_ciego/run_*.log."))
    for d, nom, q in retencion_riesgo(est, hoy_, fuentes): A.append((f'R2_{d}_{nom}', f"RF5: al dia {d} (aun sin cerrar) le quedan <={QUEDAN_MAX_D} d de retencion en la fuente '{nom}'. Copiar sin perdida a datalogs del volumen."))
    if libre_gb < MIN_LIBRE_GB: A.append(('R3_volumen', f"RF5: volumen HC con {libre_gb:.1f} GB libres (<{MIN_LIBRE_GB:.0f}); libro5_ms/libro5_tx se pausan por debajo de 10 GB."))
    for d in dias_calendario(hasta=hoy_):
        m = est.get(d)
        if m and m.get('status') == 'PENDING' and edad_pend_h(m, ahora) > PEND_MAX_H: A.append((f'R4_pending_{d}', f"RF5: dia {d} PENDING >{PEND_MAX_H:.0f} h ({m.get('motivo')})."))
        if m and m.get('status') in ('FAILED', 'BLOCKED'): A.append((f"R5_{d}_{m['status']}", f"RF5: dia {d} {m['status']}: {str(m.get('motivo'))[:200]}"))
    return A

def avisos_k6(est, hb6, out=None, ahora=None):
    """R6/R7 del juez Calma v4. Firmas estables (sin valores recalculados). Solo avisa por latido si ya existe algun dia COMPLETE (si no, el job no tiene nada que hacer)."""
    A = []; ahora = ahora or time.time(); out = out or OUT
    if any(m.get('status') == 'COMPLETE' for m in est.values()) and (hb6 is None or (ahora - hb6.get('epoch', 0)) / 3600.0 > HB_MAX_H): A.append(('R6_k6_parado', f"RF5: el juez Calma v4 (run_k6.sh 11:50Z) lleva >{HB_MAX_H:.0f} h sin correr (heartbeat_k6 {None if hb6 is None else hb6.get('t')})."))
    for f in sorted(glob.glob(out + 'manifest_rf5K6_*.json')):
        try: m = json.load(open(f))
        except Exception: m = dict(status='FAILED', job=os.path.basename(f))
        if m.get('status') in ('FAILED', 'BLOCKED'): A.append((f"R7_{os.path.basename(f)}_{m['status']}", f"RF5 K6: {m.get('job')} {m['status']}: {str(m.get('motivo') or m.get('err'))[:160]}"))
    return A

DESDE_NULO = '2026-11-24'; NULO_FAMS = ('K', 'K6', 'A'); NULO_MAX_H = 30.0
def lee_nulo_estado(out=None):
    """SOLO conteos (nulo_inc/nulo_inc_estado.json: replicas hechas por familia y dia); nunca abre las replicas precintadas."""
    try: return json.load(open((out or OUT) + 'nulo_inc/nulo_inc_estado.json'))
    except Exception: return {}

def avisos_nulo(est, hbn, ne, ahora=None):
    """R8 dia COMPLETE >= 24-Nov sin ninguna replica del nulo tras >30 h desde su cierre; R9 familia/dia BLOCKED; R10 el cron del nulo incremental (run_nulo_inc.sh) lleva >26 h sin correr con trabajo pendiente. Firmas estables."""
    import calendar
    A = []; ahora = ahora or time.time(); pend = False
    for d, m in sorted(est.items()):
        if d < DESDE_NULO or m.get('status') != 'COMPLETE': continue
        t = m.get('t_fin'); edad = 0.0 if not t else (ahora - calendar.timegm(time.strptime(t[:19], '%Y-%m-%dT%H:%M:%S'))) / 3600.0
        for fam in NULO_FAMS:
            e = (ne.get(fam) or {}).get(d)
            if e is None or e.get('estado') != 'COMPLETO': pend = True
            if e is None and edad > NULO_MAX_H: A.append((f'R8_nulo_{fam}_{d}_sin_replicas', f"RF5 nulo incremental: dia {d} COMPLETE hace >{NULO_MAX_H:.0f} h sin replicas de la familia {fam}. Revisar cron run_nulo_inc.sh / out_rf5_ciego/nulo_inc/."))
            if e is not None and str(e.get('estado', '')).startswith('BLOCKED'): A.append((f'R9_nulo_{fam}_{d}_BLOCKED', f"RF5 nulo incremental: {fam} {d} {str(e.get('estado'))[:120]}"))
    if pend and (hbn is None or (ahora - hbn.get('epoch', 0)) / 3600.0 > HB_MAX_H): A.append(('R10_nulo_parado', f"RF5 nulo incremental: run_nulo_inc.sh lleva >{HB_MAX_H:.0f} h sin correr con replicas pendientes (heartbeat {None if hbn is None else hbn.get('t')})."))
    return A

def resumen_nulo(ne):
    if not ne: return 'Nulo incremental: sin replicas todavia (solo conteos).'
    return 'Nulo incremental (replicas hechas/K_max; solo conteos): ' + '; '.join(f"{fam}: " + ', '.join(f"{d[5:]} {v['n']}/{v['K_max']}" for d, v in sorted(ne[fam].items())) for fam in NULO_FAMS if fam in ne)

def resumen_btc(out=None):
    try: j = json.load(open((out or OUT) + 'c4_btc_estado.json')); return f"BTC: {j['estado'].split(' ')[0]} ({j['n_ok']}/10 condiciones C4)"
    except Exception: return 'BTC: DATA_BLOCKED_BTC (c4_btc_estado.json no disponible)'

def resumen_texto(est, hoy_=None):
    cal = dias_calendario(hasta=hoy_); lineas = []; nv = 0
    for d in cal:
        m = est.get(d); st = 'SIN_MANIFEST' if not m else m.get('status')
        if m and es_valido(m): nv += 1
        extra = '' if not m else (' VALIDO' if es_valido(m) else (f" ({str(m.get('motivo'))[:70]})" if m.get('motivo') else (' (COMPLETE; (iii) suelo pendiente)' if st == 'COMPLETE' else '')))
        lineas.append(f'  {d}: {st}{extra}')
    return f"RF5E-COMB (prereg 16be06b6): dias validos {nv}/10 para la mirada 1. Solo conteos hasta entonces.\n" + '\n'.join(lineas)

def envia(texto, telegram):
    if not telegram or os.environ.get('RF5_SIN_TELEGRAM'): print('[SIN TELEGRAM]', texto); return True
    sys.path.insert(0, '/root/polymarket-research'); from shadow_digest import enviar_telegram; return bool(enviar_telegram(texto))

def main(argv):
    tg = '--telegram' in argv
    if '--aviso-runner' in argv: envia('🚨 RF5E-COMB: run_rf5.sh terminó con error (algún día FAILED o fallo de entorno). Ver out_rf5_ciego/run_*.log y el estado por día.', tg); return 1
    if '--aviso-k6' in argv: envia('🚨 RF5E-COMB: run_k6.sh (juez Calma v4) terminó con error (algún día FAILED o fallo de entorno). Ver out_rf5_ciego/run_k6_*.log.', tg); return 1
    if '--aviso-nulo' in argv: envia('🚨 RF5E-COMB: run_nulo_inc.sh (nulo incremental) terminó con error (algún día BLOCKED o fallo de entorno). Ver out_rf5_ciego/nulo_inc/ y run_nulo_inc_*.log.', tg); return 1
    if '--aviso-suelo' in argv: envia('🚨 RF5E-COMB: suelo_diario.sh (tabla de suelo sucesora, cron 04:40Z) FALLÓ. La tabla del día no se propone al chief. Ver suelo_sucesora/suelo_diario.log.', tg); return 1
    if '--aviso-fallo' in argv: envia('🚨 vigia_rf5 FALLO (excepcion al leer el estado de RF5E-COMB). Ver logs/vigia_rf5.log.', tg); return 1
    est = lee_estado(); hb = json.load(open(OUT + 'heartbeat.json')) if os.path.exists(OUT + 'heartbeat.json') else None; libre = shutil.disk_usage(VOL).free / 1e9
    latch = json.load(open(LATCH)) if os.path.exists(LATCH) else {}; nuevos = []; vivos = set()
    hb6 = json.load(open(OUT + 'heartbeat_k6.json')) if os.path.exists(OUT + 'heartbeat_k6.json') else None
    hbn = json.load(open(OUT + 'heartbeat_nulo_inc.json')) if os.path.exists(OUT + 'heartbeat_nulo_inc.json') else None; ne = lee_nulo_estado()
    for firma, txt in avisos(est, hb, libre) + avisos_k6(est, hb6) + avisos_nulo(est, hbn, ne):
        vivos.add(firma)
        if firma not in latch: nuevos.append(txt); latch[firma] = time.strftime('%FT%TZ', time.gmtime())
    for f in list(latch):                                     # firma resuelta => se limpia (si reaparece, vuelve a avisar)
        if f not in vivos: del latch[f]
    json.dump(latch, open(LATCH + '.tmp', 'w')); os.replace(LATCH + '.tmp', LATCH)
    envia(resumen_texto(est) + '\n' + resumen_btc() + '\n' + resumen_nulo(ne) + (f'\nVolumen HC libre: {libre:.0f} GB' if True else '') + ('\n\nAVISOS NUEVOS:\n' + '\n'.join(nuevos) if nuevos else ''), tg)
    return 0

if __name__ == '__main__': sys.exit(main(sys.argv[1:]))
