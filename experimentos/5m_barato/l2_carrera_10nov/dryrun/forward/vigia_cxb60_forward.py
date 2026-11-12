#!/usr/bin/env python3
"""vigia_cxb60_forward.py {--heartbeat | --diario} -- seguimiento de OPERACION y CALIDAD del forward B-CXB (PREREG_CXB_MULTIVARIANTE_FORWARD.md §7). Solo lectura; 0 ordenes; sin red salvo Telegram.
NO LEE EL EV NI NINGUNA PUERTA (prereg §6: "el EV diario no se lee para decidir"): no importa el informe, no calcula G1-G9, y de res_ solo mira si `pnl` existe (cobertura de desenlace), nunca su valor.

--heartbeat (cron */5, ligero, sin pandas):  heartbeat < 5 min y status RUNNING; el pid sale del run_id del heartbeat (el runner arranca por la screen `cxb60dry`, no hay cxb60.pid) y debe ser el runner;
   UNA sola instancia escribiendo en el OUT (dos instancias = kill de integridad del prereg §6); lag del flujo < 600 s; RSS < 3.000 MB. Registra D_dep la primera vez que el manifiesto cumple §3.
   Latch por firma ESTABLE (tipo de problema + dia UTC; nunca valores recalculados): un aviso por episodio.
--diario (cron tras el resolvedor): dias validos / no validos con su motivo por poblacion (primaria ETH+SOL+XRP; BTC aparte), cobertura de desenlace por poblacion calculada desde res_, cobertura por moneda,
   mercados `incompleto_arranque` y con `hueco_feed`, gmap de sa_r1 de D-1 (y gmap BTC con su cobertura), contador de dias validos y fecha prevista de la mirada 1, sello_print de ambos escenarios,
   integridad del manifiesto (VERSION, hash). Escribe OUT/forward_diario_<hoy>.json y avisa por Telegram si ALGO falla (un mensaje por dia y firma).
--diario ademas envia UN resumen corto por Telegram al dia (marcador OUT/resumen_enviado_<hoy>; si el envio falla se reintenta en la siguiente ejecucion y se deja OUT/ALERTA_resumen_no_enviado_<hoy>.txt): heartbeat, dias validos, cobertura,
   gmap de D-1 y «G3 en seguimiento (trivial vs GEO1)». SIN EV ni puertas (prereg §6).
Salida: 0 sano, 1 problema detectado (ya avisado), 2 uso/CXB60_DIR invalido. CXB60_DIR / CXB60_GMAP_DIR / CXB60_SIN_TELEGRAM / CXB60_TAG (prefijo de todo Telegram, p. ej. '[TEST CXB]') / CXB60_HOY (fecha UTC simulada del --diario)
solo para pruebas y ensayos."""
import os, sys, json, time, gzip, zlib, glob, argparse, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
OUT = os.environ.get('CXB60_DIR', '/root/polymarket-research-datalogs/cxb60_dryrun').rstrip('/') + '/'
GMAP = os.environ.get('CXB60_GMAP_DIR', '/root/polymarket-research-datalogs/cxb60_dryrun_gmap').rstrip('/') + '/'
RUNNER = 'cxb60_dryrun_fase0.py'
HB_MAX_S = 300; LAG_MAX_S = 600; RSS_MAX_MB = 3000


# ======================================================================================== procesos
def runners_vivos(proc='/proc'):
    """PIDs de procesos PYTHON que ejecutan el runner. Exige argv[0] = python* y un elemento del argv con basename == runner: no confunde la screen ni el `bash -c` envoltorio (su cmd es un solo elemento)."""
    pids = []
    for p in os.listdir(proc):
        if not p.isdigit(): continue
        try: a = open(f'{proc}/{p}/cmdline', 'rb').read().split(b'\0')
        except OSError: continue
        a = [x.decode('utf-8', 'replace') for x in a if x]
        if a and os.path.basename(a[0]).startswith('python') and any(os.path.basename(x) == RUNNER for x in a[1:]): pids.append(int(p))
    return sorted(pids)


def pid_de_run_id(run_id):
    """run_id = <AAAAMMDDTHHMMSSZ>_<pid> (lo escribe el runner)."""
    try: return int(str(run_id).rsplit('_', 1)[1])
    except (IndexError, ValueError): return None


# ======================================================================================== comprobaciones de operacion
def problemas_heartbeat(out=None, ahora=None, vivos=None):
    """Lista de (tipo, texto) ordenada; vacia = sano. `vivos` inyectable en tests."""
    out = out or OUT; ahora = time.time() if ahora is None else ahora; pr = []
    try: hb = json.load(open(out + 'heartbeat.json'))
    except (OSError, ValueError): return [('sin_heartbeat', 'sin heartbeat.json legible')]
    edad = ahora - hb.get('wall', 0)
    if edad > HB_MAX_S: pr.append(('heartbeat_viejo', f'heartbeat de hace {edad / 60:.0f} min'))
    if hb.get('status') != 'RUNNING': pr.append(('status', f"status {hb.get('status')}"))
    vivos = runners_vivos() if vivos is None else vivos; pid = pid_de_run_id(hb.get('run_id'))
    if pid is None or pid not in vivos: pr.append(('pid_ausente', f"el pid del run_id ({pid}) no es un runner vivo"))
    if len(vivos) > 1: pr.append(('instancias_multiples', f'{len(vivos)} runners vivos {vivos}: kill de integridad (dos escritores en el mismo OUT)'))
    if len(vivos) == 0 and not any(t == 'pid_ausente' for t, _ in pr): pr.append(('pid_ausente', 'ningun runner vivo'))
    if hb.get('lag_s') is not None and hb['lag_s'] > LAG_MAX_S: pr.append(('lag', f"lag del flujo {hb['lag_s']:.0f} s (maker_ms sin crecer?)"))
    if hb.get('rss_mb') is not None and hb['rss_mb'] >= RSS_MAX_MB: pr.append(('rss', f"RSS {hb['rss_mb']:.0f} MB >= {RSS_MAX_MB}"))
    return pr


def hueco_e_incompletos(out, dia):
    """(mercados mkt, con hueco_feed, por moneda) leyendo SOLO las filas 'mkt' del dec_ en streaming (tolera cola de gz truncada)."""
    n = h = 0; por = {}
    p = out + f'dec_{dia}.csv.gz'
    if not os.path.exists(p): return None
    try:
        with gzip.open(p, 'rt', encoding='utf-8', errors='replace') as fh:
            for ln in fh:
                if ln.startswith('mkt,'):
                    n += 1; c = ln.split(',', 6)[5]; v = por.setdefault(c, [0, 0]); v[0] += 1
                    if '"hueco_feed":true' in ln: h += 1; v[1] += 1
    except (EOFError, zlib.error, OSError): pass                       # cola escribiendose: lo leido vale
    return dict(mercados=n, con_hueco_feed=h, por_moneda={c: dict(mercados=a, con_hueco_feed=b) for c, (a, b) in por.items()})


# ======================================================================================== avisos
def avisar(texto):
    tag = os.environ.get('CXB60_TAG', '').strip(); texto = (tag + ' ' + texto) if tag else texto
    if os.environ.get('CXB60_SIN_TELEGRAM'): print('AVISO (seco, sin Telegram): ' + texto); return True
    try: sys.path.insert(0, '/root/polymarket-research'); from shadow_digest import enviar_telegram; return bool(enviar_telegram(texto))
    except Exception as e: print('no pude avisar', repr(e)[:200]); return False


def avisa_con_latch(out, nombre, problemas, prefijo):
    """problemas = [(tipo, texto)]. Un aviso por episodio: la firma es tipo(s)+dia UTC (estable, sin valores). Se limpia cuando vuelve a estar sano."""
    f = out + f'{nombre}_latch.json'
    try: st = json.load(open(f))
    except (OSError, ValueError): st = {}
    firma = ('+'.join(sorted({t for t, _ in problemas})) + ':' + time.strftime('%Y%m%d', time.gmtime())) if problemas else None
    if problemas and st.get('firma') != firma:
        ok = avisar(prefijo + ' ' + '; '.join(x for _, x in problemas))
        if ok: json.dump(dict(firma=firma, t=time.time()), open(f, 'w'))              # si el aviso falla, NO se enlata: se reintenta en el siguiente ciclo
    elif not problemas and st.get('firma'): json.dump({}, open(f, 'w'))


def resumen_diario(rep, ayer, n_hb):
    """Texto corto del resumen diario (<= 9 lineas). SOLO operacion y calidad: heartbeat, dias validos, cobertura de DESENLACE (fraccion de rellenos con desenlace, no su valor), gmap de D-1, mirada prevista y la nota de G3.
    Nada de EV ni de puertas (prereg §6)."""
    hb = rep.get('heartbeat') or {}; po = rep.get('poblaciones') or {}; cm = rep.get('contador_mirada_1') or {}; f1 = lambda v: 'n/d' if v is None else f'{v:.1f}'
    pct = lambda v: 'n/a' if v is None else f'{100 * v:.1f} %'
    def cob(pob):
        a = (po.get(pob) or {}).get('cobertura_desenlace_agregada'); return pct(a.get('cobertura')) if a else 'n/a (sin dias validos)'
    def gm(pob):
        g = (po.get(pob) or {}).get('gmap_dia_anterior'); return 'n/a (D-1 < 1er dia contable)' if g is None else ('OK' if g else 'FALTA')
    cb = rep.get('gmap_btc_cobertura'); n_pr = (po.get('primaria') or {}).get('n_dias_validos', 0); n_bt = (po.get('BTC') or {}).get('n_dias_validos', 0)
    nv = {pob: sorted((po.get(pob) or {}).get('dias_no_validos', {})) for pob in ('primaria', 'BTC')}
    L = [f'cxb60 forward diario {rep["hoy"]} (dry-run B-CXB, 0 ordenes)',
         'heartbeat: ' + ('OK' if n_hb == 0 and hb else 'PROBLEMA (aviso aparte)') + f' | {hb.get("status")} | lag {f1(hb.get("lag_s"))} s | RSS {f1(hb.get("rss_mb"))} MB',
         f'dias validos acumulados: primaria {n_pr}/{cm.get("necesarios", "?")} | BTC {n_bt} | no validos: primaria {nv["primaria"] or "ninguno"}, BTC {nv["BTC"] or "ninguno"}',
         f'cobertura de desenlace (dias validos): primaria {cob("primaria")} | BTC {cob("BTC")}',
         f'gmap D-1 ({ayer}): primaria {gm("primaria")} | BTC {gm("BTC")}' + (f' | fuente BTC D-1 cobertura {pct(cb.get("cobertura_desenlace"))}' if cb else ''),
         f'1er dia contable {rep.get("primer_dia_contable") or "n/d"} | mirada 1 prevista {cm.get("fecha_prevista", "n/d")} (D_dep+35: {cm.get("plazo_D_dep_mas_35", "n/d")})',
         'G3 en seguimiento (trivial vs GEO1)',
         f'problemas detectados: {len(rep.get("problemas") or []) or "ninguno"}',
         'Sin EV ni puertas entre miradas (prereg §6).']
    return '\n'.join(L)


def enviar_resumen(out, hoy, rep, ayer, n_hb):
    """Un resumen por dia UTC (marcador). True si ya estaba enviado o se envio ahora; False si el envio FALLO (se reintenta en la proxima ejecucion y queda un fichero ALERTA para el vigia de loggers/auditoria)."""
    marca = out + f'resumen_enviado_{hoy}'
    if os.path.exists(marca): return True
    if avisar(resumen_diario(rep, ayer, n_hb)): open(marca, 'w').write(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + '\n'); return True
    open(out + f'ALERTA_resumen_no_enviado_{hoy}.txt', 'a').write(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + ' el resumen diario NO llego a Telegram\n'); print('RESUMEN NO ENVIADO a Telegram', file=sys.stderr); return False


# ======================================================================================== modos
def modo_heartbeat(out=None):
    out = out or OUT; import forward_gates as FG
    pr = problemas_heartbeat(out)
    if not pr:
        try: FG.registrar_d_dep(out)                                      # idempotente; solo escribe la primera vez que el manifiesto cumple el prereg §3
        except Exception as e: print('registrar_d_dep:', repr(e)[:200])
    avisa_con_latch(out, 'vigia_hb', pr, 'cxb60 forward:'); print('PROBLEMA: ' + '; '.join(x for _, x in pr) if pr else 'sano'); return 1 if pr else 0


def modo_diario(out=None, gmap=None, hoy=None):
    out = out or OUT; gmap = gmap or GMAP; hoy = hoy or os.environ.get('CXB60_HOY') or dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d'); import forward_gates as FG
    ayer = (dt.date.fromisoformat(hoy) - dt.timedelta(days=1)).isoformat(); pr = list(problemas_heartbeat(out)); n_hb = len(pr); rep = dict(hoy=hoy, ts_utc=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), nota='seguimiento de operacion/calidad; NO contiene EV ni puertas (prereg §6)')
    try: hb = json.load(open(out + 'heartbeat.json')); rep['heartbeat'] = {k: hb.get(k) for k in ('status', 'run_id', 'lag_s', 'rss_mb', 'rss_pico_mb', 'W_utc')}; rep['heartbeat']['edad_s'] = round(time.time() - hb.get('wall', 0))
    except (OSError, ValueError): rep['heartbeat'] = None
    dd, creado = FG.registrar_d_dep(out); rep['D_dep'] = dd
    for k, v in (('integridad', FG.integridad(out)),):
        rep[k] = v; pr += [('integridad', x) for x in v]
    rep['sello_print'] = {'primario': (json.load(open(out + 'run_manifest.json')) if os.path.exists(out + 'run_manifest.json') else {}).get('sello_print'), 'c59': (json.load(open(out + 'c59/run_manifest.json')) if os.path.exists(out + 'c59/run_manifest.json') else {}).get('sello_print')}
    if not dd: rep['aviso'] = 'D_dep no registrado (el runner aun no ha dejado un manifiesto RUNNING v3 con el hash congelado)'; pr.append(('sin_D_dep', rep['aviso']))
    else:
        desde = dd['primer_dia_contable']; rep['primer_dia_contable'] = desde; rep['poblaciones'] = {}
        for pob in ('primaria', 'BTC'):
            P = FG.POBLACIONES[pob]; validos, det = FG.evaluar_dias(out, pob, gmap, desde, ayer); rows = {}
            for d, x in det.items():
                rows[d] = dict(valido=x['valido'], motivos=x['motivos'], desenlace=x.get('desenlace'), cobertura_por_moneda=(x.get('coverage') or {}).get('por_moneda'), saltados=(x.get('coverage') or {}).get('saltados'), feed=hueco_e_incompletos(out, d))
            ag = FG.cobertura_agregada(det, validos) if validos else None
            rep['poblaciones'][pob] = dict(dias_validos=validos, n_dias_validos=len(validos), dias_no_validos={d: x['motivos'] for d, x in det.items() if not x['valido']}, cobertura_desenlace_agregada=ag, por_dia=rows,
                                           gmap_dia_anterior=FG.gmap_existe(ayer, pob, gmap) if ayer >= desde else None)
            if ayer in det and not det[ayer]['valido'] and pob == 'primaria': pr.append(('dia_no_valido', f'{ayer} NO valido ({pob}): ' + ', '.join(det[ayer]['motivos'])))
            if ayer >= desde and not FG.gmap_existe(ayer, pob, gmap) and (pob == 'primaria' or ayer in det): pr.append((f'gmap_{pob}', f'falta el gmap {pob} de {ayer}'))
            if pob == 'primaria' and ayer >= desde and ayer not in det: pr.append(('sin_coverage_ayer', f'no hay coverage_{ayer}.json (el runner no cerro el dia?)'))
        try: cb = json.load(open(gmap + f'cob_btc_{ayer}.json')); rep['gmap_btc_cobertura'] = cb; (cb.get('cobertura_desenlace') or 0) < FG.COB_AGREGADA_MIN and pr.append(('gmap_btc_cobertura', f"gmap BTC {ayer}: cobertura {cb.get('cobertura_desenlace')}"))
        except (OSError, ValueError): rep['gmap_btc_cobertura'] = None; ayer >= desde and pr.append(('gmap_btc_cobertura', f'sin cob_btc_{ayer}.json (la fuente BTC no corrio)'))
        n = rep['poblaciones']['primaria']['n_dias_validos']; rep['contador_mirada_1'] = dict(dias_validos=n, necesarios=FG.G1_DIAS, falta=max(0, FG.G1_DIAS - n),
                                                                                         fecha_prevista=(dt.date.fromisoformat(hoy) + dt.timedelta(days=max(0, FG.G1_DIAS - n))).isoformat() if n < FG.G1_DIAS else 'ya procede la mirada 1',
                                                                                         plazo_D_dep_mas_35=(dt.date.fromisoformat(dd['D_dep']) + dt.timedelta(days=FG.PLAZO_DIAS)).isoformat(), nota='fecha prevista = suponiendo un dia valido por dia natural')
    rep['problemas'] = [dict(tipo=t, texto=x) for t, x in pr]
    tmp = out + f'forward_diario_{hoy}.json.tmp'; json.dump(rep, open(tmp, 'w'), indent=1, default=str); os.replace(tmp, out + f'forward_diario_{hoy}.json')
    avisa_con_latch(out, 'vigia_diario', pr, 'cxb60 forward (diario):')
    enviado = enviar_resumen(out, hoy, rep, ayer, n_hb)
    print(json.dumps({k: rep[k] for k in ('hoy', 'D_dep', 'contador_mirada_1', 'problemas') if k in rep}, default=str)); return 1 if (pr or not enviado) else 0


def main(argv=None):
    ap = argparse.ArgumentParser(); g = ap.add_mutually_exclusive_group(required=True); g.add_argument('--heartbeat', action='store_true'); g.add_argument('--diario', action='store_true'); a = ap.parse_args(argv)
    if not os.path.isdir(OUT): print('CXB60_DIR no existe:', OUT, file=sys.stderr); return 2
    return modo_heartbeat() if a.heartbeat else modo_diario()


if __name__ == '__main__': sys.exit(main())
