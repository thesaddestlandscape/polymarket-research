#!/usr/bin/env python3
"""verificar_diario_cxb60.py -- comprobacion POST-10:55Z (R3, 12-Nov) del cron diario del forward B-CXB. SOLO LECTURA sobre el datalog; 0 ordenes; no toca crons, screens ni el conjunto congelado.
Uso (11:05Z, p. ej. el 13-Nov):  cd /root/polymarket-research && .venv/bin/python -I experimentos/5m_barato/l2_carrera_10nov/dryrun/forward/verificar_diario_cxb60.py
  opciones: --hoy YYYY-MM-DD (defecto: hoy UTC) | --ahora ISO (ensayos) | --desde HH:MM (ventana del cron, defecto 10:55) | --out/--gmap/--log (rutas) | --sin-telegram | --tag '[TEST CXB]' | --siempre (avisa tambien si todo OK)
Comprueba, para hoy (D) y D-1:
  C1 el cron corrio: forward_diario_<D>.json existe, parsea, es de la fecha D y se escribio DESPUES de <D> 10:55Z (y no en el futuro).
  C2 contenido: sin `problemas`, sin fallos de integridad, D_dep registrado, heartbeat con status sano y edad < 15 min.
  C3 fuente BTC de D-1 (si existe dec_<D-1>): gmap_btc_<D-1>.json (>2 bytes) y cob_btc_<D-1>.json con cobertura_desenlace >= 0,99, ambos escritos hoy tras 10:55Z.
  C4 resolvedores de D-1 (primario y, si hay c59/dec_<D-1>, c59): res_<D-1>.csv.gz existe, es gz integro con filas y se regenero hoy tras 10:55Z.
  C5 Telegram: marcador resumen_enviado_<D> presente, sin ALERTA_resumen_no_enviado_<D>.txt ni marcadores cron_aviso_*_<D> (cada uno = un fallo ya avisado por el cron).
  C6 logs: ultimas 400 lineas de logs/cxb60_forward_cron.log sin Traceback/MemoryError/Error/FALLO (aviso, no fallo: el log no lleva marca de tiempo por linea).
Si falla algo (C1-C5) => Telegram (un aviso por dia y firma; marcador verif_aviso_<D>_<firma>). Salida: 0 todo OK, 1 hay fallos, 2 uso."""
import os, sys, json, gzip, time, zlib, hashlib, argparse, importlib.util, datetime as dt

R = '/root/polymarket-research'
OUT0 = os.environ.get('CXB60_DIR', '/root/polymarket-research-datalogs/cxb60_dryrun').rstrip('/') + '/'
GMAP0 = os.environ.get('CXB60_GMAP_DIR', '/root/polymarket-research-datalogs/cxb60_dryrun_gmap').rstrip('/') + '/'
LOG0 = os.environ.get('CXB60_LOG', R + '/logs/cxb60_forward_cron.log')
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
PATRON_LOG = ('Traceback', 'MemoryError', 'Error', 'FALLO', 'FALLÓ')


def _fg():
    sp = importlib.util.spec_from_file_location('forward_gates_v', HERE + 'forward_gates.py'); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m


def _epoch(d, hhmm):
    h, m = (int(x) for x in hhmm.split(':')); return dt.datetime(*(int(x) for x in d.split('-')), h, m, tzinfo=dt.timezone.utc).timestamp()


def _gz_ok(p):
    """(ok, n_lineas): gz integro leido ENTERO (una cola truncada = no ok) con al menos una fila de datos."""
    n = 0
    try:
        with gzip.open(p, 'rt', encoding='utf-8', errors='replace') as fh:
            for _ in fh: n += 1
    except (EOFError, zlib.error, OSError): return False, n
    return n >= 2, n


def comprobar(hoy, ahora, out, gmap, log, desde='10:55'):
    """Devuelve (fallos[(codigo, texto)], avisos[texto], detalle dict). No escribe nada."""
    FG = _fg(); fallos = []; avisos = []; det = {}; t0 = _epoch(hoy, desde); ayer = (dt.date.fromisoformat(hoy) - dt.timedelta(days=1)).isoformat()
    def fresco(p): return os.path.exists(p) and t0 <= os.path.getmtime(p) <= ahora + 120
    # C1/C2 ------------------------------------------------------------------------------------------------------------------------------------------------
    pj = out + f'forward_diario_{hoy}.json'; rep = None
    if not os.path.exists(pj): fallos.append(('C1_sin_forward_diario', f'NO existe {pj}: el cron de las 10:55Z no escribio el informe'))
    else:
        try: rep = json.load(open(pj))
        except (OSError, ValueError): fallos.append(('C1_forward_diario_ilegible', f'{pj} ilegible/corrupto'))
        if rep is not None:
            if rep.get('hoy') != hoy: fallos.append(('C1_fecha', f"forward_diario dice hoy={rep.get('hoy')} y se esperaba {hoy}"))
            if not fresco(pj): fallos.append(('C1_viejo', f'{pj} no se escribio tras {hoy} {desde}Z (mtime {dt.datetime.fromtimestamp(os.path.getmtime(pj), dt.timezone.utc):%Y-%m-%d %H:%M}Z)'))
            pr = rep.get('problemas') or []
            if pr: fallos.append(('C2_problemas', f'{len(pr)} problema(s) en el informe: ' + '; '.join(f"{p.get('tipo')}: {str(p.get('texto'))[:90]}" for p in pr[:5])))
            if rep.get('integridad'): fallos.append(('C2_integridad', f"integridad: {rep.get('integridad')}"))
            if not rep.get('D_dep'): fallos.append(('C2_sin_D_dep', 'D_dep no registrado'))
            hb = rep.get('heartbeat') or {}
            if hb.get('status') != 'RUNNING': fallos.append(('C2_heartbeat', f'heartbeat ausente o status != RUNNING: {hb}'))
            elif (hb.get('edad_s') is None) or hb.get('edad_s') > 900: fallos.append(('C2_heartbeat', f"heartbeat viejo en el momento del informe: edad_s={hb.get('edad_s')}"))
            det['informe'] = dict(D_dep=rep.get('D_dep'), contador_mirada_1=rep.get('contador_mirada_1'), heartbeat=hb)
    # C3 fuente BTC / C4 resolvedores de D-1 ---------------------------------------------------------------------------------------------------------------
    if os.path.exists(out + f'dec_{ayer}.csv.gz'):
        pg, pc = gmap + f'gmap_btc_{ayer}.json', gmap + f'cob_btc_{ayer}.json'
        if not (os.path.exists(pg) and os.path.getsize(pg) > 2): fallos.append(('C3_gmap_btc', f'falta/vacio {pg}'))
        elif not fresco(pg): fallos.append(('C3_gmap_btc_viejo', f'{pg} no se regenero hoy tras {desde}Z'))
        if not os.path.exists(pc): fallos.append(('C3_cob_btc', f'falta {pc}'))
        else:
            try: cb = json.load(open(pc)); cv = cb.get('cobertura_desenlace')
            except (OSError, ValueError): cb, cv = {}, None
            det['fuente_btc'] = cb
            if cv is None or cv < FG.COB_AGREGADA_MIN: fallos.append(('C3_cobertura_btc', f'cobertura de desenlace BTC {ayer} = {cv} < {FG.COB_AGREGADA_MIN}'))
            if not fresco(pc): fallos.append(('C3_cob_btc_viejo', f'{pc} no se regenero hoy tras {desde}Z'))
        for etiqueta, base in (('primario', out), ('c59', out + 'c59/')):
            if etiqueta == 'c59' and not os.path.exists(base + f'dec_{ayer}.csv.gz'): continue
            p = base + f'res_{ayer}.csv.gz'
            if not os.path.exists(p): fallos.append((f'C4_sin_res_{etiqueta}', f'falta {p}: el resolvedor {etiqueta} de {ayer} no escribio nada')); continue
            ok, n = _gz_ok(p); det[f'res_{etiqueta}'] = dict(filas=n, integro=ok)
            if not ok: fallos.append((f'C4_res_{etiqueta}_corrupto', f'{p} no es un gz integro con filas (n={n})'))
            if not fresco(p): fallos.append((f'C4_res_{etiqueta}_viejo', f'{p} no se regenero hoy tras {desde}Z'))
    else: avisos.append(f'dec_{ayer}.csv.gz no existe: D-1 no tiene segmentos y el cron no resuelve nada (normal solo si el dry-run no corrio ese dia)')
    # C5 Telegram ------------------------------------------------------------------------------------------------------------------------------------------
    if not os.path.exists(out + f'resumen_enviado_{hoy}'): fallos.append(('C5_sin_resumen', f'sin marcador resumen_enviado_{hoy}: el resumen diario NO llego a Telegram'))
    if os.path.exists(out + f'ALERTA_resumen_no_enviado_{hoy}.txt'): fallos.append(('C5_alerta_resumen', f'existe ALERTA_resumen_no_enviado_{hoy}.txt (envio fallido)'))
    marc = sorted(x for x in os.listdir(out) if x.startswith('cron_aviso_') and x.endswith(f'_{hoy}')) if os.path.isdir(out) else []
    if marc: fallos.append(('C5_cron_aviso', f'el cron ya envio avisos de fallo hoy: {marc}'))
    # C6 logs ----------------------------------------------------------------------------------------------------------------------------------------------
    try:
        L = open(log, errors='replace').read().splitlines()[-400:]; malas = [l for l in L if any(p in l for p in PATRON_LOG)]
        if malas: avisos.append(f'log del cron ({len(malas)} lineas con error en las ultimas 400; sin marca de tiempo por linea, puede ser antiguo): ' + ' | '.join(l[:100] for l in malas[-3:]))
        det['log_lineas_error_ult400'] = len(malas)
    except OSError: avisos.append(f'no se pudo leer {log}')
    return fallos, avisos, det


def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument('--hoy'); ap.add_argument('--ahora'); ap.add_argument('--desde', default='10:55'); ap.add_argument('--out', default=OUT0); ap.add_argument('--gmap', default=GMAP0); ap.add_argument('--log', default=LOG0)
    ap.add_argument('--sin-telegram', action='store_true'); ap.add_argument('--tag', default=''); ap.add_argument('--siempre', action='store_true'); a = ap.parse_args(argv)
    ahora = dt.datetime.fromisoformat(a.ahora.replace('Z', '+00:00')).timestamp() if a.ahora else time.time(); hoy = a.hoy or dt.datetime.fromtimestamp(ahora, dt.timezone.utc).strftime('%Y-%m-%d')
    out = a.out.rstrip('/') + '/'; gmap = a.gmap.rstrip('/') + '/'
    if not os.path.isdir(out): print('CXB60_DIR no existe:', out, file=sys.stderr); return 2
    fallos, avisos, det = comprobar(hoy, ahora, out, gmap, a.log, a.desde)
    print(f'VERIFICACION cxb60 forward diario {hoy} (D-1 = {(dt.date.fromisoformat(hoy) - dt.timedelta(days=1)).isoformat()}): ' + ('TODO OK' if not fallos else f'{len(fallos)} FALLO(S)'))
    for c, t in fallos: print(f'  FALLO {c}: {t}')
    for t in avisos: print(f'  aviso: {t}')
    print('  detalle:', json.dumps(det, default=str)[:600])
    if fallos or a.siempre:
        firma = '+'.join(sorted(c for c, _ in fallos)) if fallos else 'ok'; marca = out + f'verif_aviso_{hoy}_{hashlib.sha256(firma.encode()).hexdigest()[:10]}'
        if os.path.exists(marca): print('  (aviso de Telegram ya enviado hoy para esta firma)'); return 1 if fallos else 0
        texto = ((a.tag + ' ') if a.tag else '') + f'cxb60 forward {hoy}: ' + ('verificacion 11:05Z OK' if not fallos else 'FALTA ALGO tras el cron de las 10:55Z: ' + '; '.join(f'{c}: {t[:110]}' for c, t in fallos[:4]) + (f' (+{len(fallos) - 4} mas)' if len(fallos) > 4 else '') + ' | comando: verificar_diario_cxb60.py')
        ok = False
        if a.sin_telegram: print('AVISO (seco, sin Telegram): ' + texto); ok = True
        else:
            try: sys.path.insert(0, R); from shadow_digest import enviar_telegram; ok = enviar_telegram(texto) is True
            except Exception as e: print('no pude avisar:', repr(e)[:200], file=sys.stderr)
        if ok and not a.sin_telegram:                                                    # el ensayo en seco no deja marcadores en el datalog
            try: open(marca, 'w').write(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + '\n')
            except OSError: pass
        else: print('  AVISO A TELEGRAM FALLIDO: se reintentara en la proxima ejecucion', file=sys.stderr)
    return 1 if fallos else 0


if __name__ == '__main__': sys.exit(main())
