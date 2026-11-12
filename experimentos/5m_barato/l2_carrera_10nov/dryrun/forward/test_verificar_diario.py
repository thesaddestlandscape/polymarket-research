#!/usr/bin/env python3
"""Tests de verificar_diario_cxb60.py (R3). python3 -I test_verificar_diario.py  -- sintetico en tmp; sin Telegram real ni red."""
import os, sys, json, gzip, shutil, tempfile, time, datetime as dt, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
sp = importlib.util.spec_from_file_location('verif', HERE + 'verificar_diario_cxb60.py'); VD = importlib.util.module_from_spec(sp); sp.loader.exec_module(VD)
TMP = tempfile.mkdtemp(prefix='test_verif_')
HOY, AYER = '2026-11-13', '2026-11-12'; T = dt.datetime(2026, 11, 13, 11, 5, tzinfo=dt.timezone.utc).timestamp()     # "ahora" = 11:05Z
T_CRON = dt.datetime(2026, 11, 13, 10, 58, tzinfo=dt.timezone.utc).timestamp()


def gz(p, filas=3, cola_rota=False):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with gzip.open(p, 'wt') as f:
        for i in range(filas): f.write(f'a,b,{i}\n')
    if cola_rota: open(p, 'ab').write(b'')
    if cola_rota: raw = open(p, 'rb').read(); open(p, 'wb').write(raw[:-6])


def escribir(p, txt, mt=T_CRON):
    os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(txt); os.utime(p, (mt, mt))


def montar(nombre, **quitar):
    d = os.path.join(TMP, nombre); out = d + '/out/'; gm = d + '/gmap/'; os.makedirs(out); os.makedirs(gm); log = d + '/cron.log'; open(log, 'w').write('sano\nsano\n')
    rep = dict(hoy=HOY, problemas=[], integridad=[], D_dep={'D_dep': AYER}, heartbeat=dict(status='RUNNING', edad_s=30), contador_mirada_1=dict(dias_validos=0))
    gz(out + f'dec_{AYER}.csv.gz'); gz(out + f'c59/dec_{AYER}.csv.gz')
    escribir(out + f'forward_diario_{HOY}.json', json.dumps(rep)); escribir(gm + f'gmap_btc_{AYER}.json', '{"s": {"id": 1}}'); escribir(gm + f'cob_btc_{AYER}.json', json.dumps(dict(cobertura_desenlace=1.0)))
    gz(out + f'res_{AYER}.csv.gz'); gz(out + f'c59/res_{AYER}.csv.gz'); os.utime(out + f'res_{AYER}.csv.gz', (T_CRON, T_CRON)); os.utime(out + f'c59/res_{AYER}.csv.gz', (T_CRON, T_CRON)); escribir(out + f'resumen_enviado_{HOY}', 'x\n')
    return out, gm, log, rep


def cods(out, gm, log): f, a, d = VD.comprobar(HOY, T, out, gm, log); return sorted(c for c, _ in f), a


def test_todo_ok():
    out, gm, log, _ = montar('ok'); f, a = cods(out, gm, log); assert f == [], f
    print('V1 ok: fixture completo (informe, fuente BTC, 2 resolvedores, resumen enviado, log limpio) => 0 fallos')


def test_cada_pieza_ausente_falla_con_su_codigo():
    casos = {'C1_sin_forward_diario': lambda o, g, l: os.remove(o + f'forward_diario_{HOY}.json'), 'C3_gmap_btc': lambda o, g, l: os.remove(g + f'gmap_btc_{AYER}.json'), 'C3_cob_btc': lambda o, g, l: os.remove(g + f'cob_btc_{AYER}.json'),
             'C4_sin_res_primario': lambda o, g, l: os.remove(o + f'res_{AYER}.csv.gz'), 'C4_sin_res_c59': lambda o, g, l: os.remove(o + f'c59/res_{AYER}.csv.gz'), 'C5_sin_resumen': lambda o, g, l: os.remove(o + f'resumen_enviado_{HOY}'),
             'C5_alerta_resumen': lambda o, g, l: escribir(o + f'ALERTA_resumen_no_enviado_{HOY}.txt', 'x'), 'C5_cron_aviso': lambda o, g, l: escribir(o + f'cron_aviso_hb_crash_{HOY}', 'x'),
             'C3_cobertura_btc': lambda o, g, l: escribir(g + f'cob_btc_{AYER}.json', json.dumps(dict(cobertura_desenlace=0.5))), 'C4_res_primario_corrupto': lambda o, g, l: gz(o + f'res_{AYER}.csv.gz', cola_rota=True)}
    for i, (cod, f_) in enumerate(casos.items()):
        out, gm, log, _ = montar(f'a{i}'); f_(out, gm, log); os.utime(out + f'res_{AYER}.csv.gz', (T_CRON, T_CRON)) if os.path.exists(out + f'res_{AYER}.csv.gz') else None
        f, a = cods(out, gm, log); assert cod in f, (cod, f)
    print('V2 ok: %d piezas ausentes/corruptas => cada una da su codigo de fallo (cron no corrio, fuente BTC, resolvedores, Telegram, cobertura)' % len(casos))


def test_viejo_problemas_y_heartbeat():
    out, gm, log, rep = montar('viejo'); old = T_CRON - 86400
    for p in (out + f'forward_diario_{HOY}.json', gm + f'gmap_btc_{AYER}.json', gm + f'cob_btc_{AYER}.json', out + f'res_{AYER}.csv.gz', out + f'c59/res_{AYER}.csv.gz'): os.utime(p, (old, old))      # artefactos de AYER: el cron de hoy no corrio
    f, _ = cods(out, gm, log); assert {'C1_viejo', 'C3_gmap_btc_viejo', 'C3_cob_btc_viejo', 'C4_res_primario_viejo', 'C4_res_c59_viejo'} <= set(f), f
    out, gm, log, rep = montar('prob'); rep['problemas'] = [dict(tipo='gmap_BTC', texto='falta el gmap')]; rep['heartbeat'] = dict(status='RUNNING', edad_s=5000); rep['D_dep'] = None; rep['hoy'] = '2026-11-12'
    escribir(out + f'forward_diario_{HOY}.json', json.dumps(rep)); f, _ = cods(out, gm, log); assert {'C2_problemas', 'C2_heartbeat', 'C2_sin_D_dep', 'C1_fecha'} <= set(f), f
    out, gm, log, rep = montar('futuro'); os.utime(out + f'forward_diario_{HOY}.json', (T + 7200, T + 7200)); assert 'C1_viejo' in cods(out, gm, log)[0]       # mtime en el futuro tampoco vale
    print('V3 ok: artefactos de ayer / informe con problemas / heartbeat viejo / sin D_dep / fecha equivocada / mtime futuro => fallos')


def test_sin_dec_de_ayer_y_log():
    out, gm, log, _ = montar('sindec'); os.remove(out + f'dec_{AYER}.csv.gz'); os.remove(out + f'res_{AYER}.csv.gz'); f, a = cods(out, gm, log); assert f == [] and any('no existe' in x for x in a), (f, a)
    out, gm, log, _ = montar('log'); open(log, 'w').write('sano\nTraceback (most recent call last):\nMemoryError\n'); f, a = cods(out, gm, log); assert f == [] and any('Traceback' in x or 'MemoryError' in x for x in a)
    print('V4 ok: sin dec_D-1 no se exige fuente/resolvedor (aviso); errores en el log => aviso (no fallo)')


def test_telegram_y_marcador():
    import types; enviados = []
    sys.modules['shadow_digest'] = types.SimpleNamespace(enviar_telegram=lambda t: enviados.append(t) or True); sys.path.insert(0, '/nonexistent')
    out, gm, log, _ = montar('tg'); os.remove(out + f'resumen_enviado_{HOY}'); VD.R = '/nonexistent'
    args = ['--hoy', HOY, '--ahora', '2026-11-13T11:05:00Z', '--out', out, '--gmap', gm, '--log', log, '--tag', '[TEST CXB]']
    assert VD.main(args) == 1 and len(enviados) == 1 and enviados[0].startswith('[TEST CXB]') and 'C5_sin_resumen' in enviados[0]
    assert VD.main(args) == 1 and len(enviados) == 1                                   # mismo dia y misma firma: no repite
    escribir(out + f'forward_diario_{HOY}.json', '{"hoy": "x"}'); assert VD.main(args) == 1 and len(enviados) == 2                  # firma distinta: avisa de nuevo
    out, gm, log, _ = montar('tg_ok'); args2 = ['--hoy', HOY, '--ahora', '2026-11-13T11:05:00Z', '--out', out, '--gmap', gm, '--log', log]
    assert VD.main(args2) == 0 and len(enviados) == 2                                  # todo OK: silencio por defecto
    assert VD.main(args2 + ['--siempre']) == 0 and len(enviados) == 3 and 'OK' in enviados[-1]
    sys.modules['shadow_digest'] = types.SimpleNamespace(enviar_telegram=lambda t: False)                                # Telegram falla: no se marca como avisado
    out, gm, log, _ = montar('tg_fail'); os.remove(out + f'resumen_enviado_{HOY}'); a3 = ['--hoy', HOY, '--ahora', '2026-11-13T11:05:00Z', '--out', out, '--gmap', gm, '--log', log]
    assert VD.main(a3) == 1 and not [x for x in os.listdir(out) if x.startswith('verif_aviso_')]
    out, gm, log, _ = montar('tg_seco'); os.remove(out + f'resumen_enviado_{HOY}'); assert VD.main(['--hoy', HOY, '--ahora', '2026-11-13T11:05:00Z', '--out', out, '--gmap', gm, '--log', log, '--sin-telegram']) == 1 and not [x for x in os.listdir(out) if x.startswith('verif_aviso_')]     # en seco no escribe marcadores
    assert VD.main(['--hoy', HOY, '--out', TMP + '/no_existe']) == 2
    print('V5 ok: fallo => Telegram (con tag) una vez por dia y firma; OK => silencio (--siempre avisa); Telegram caido => sin marcador, reintento; out inexistente => rc 2')


if __name__ == '__main__':
    try:
        for n, f in list(globals().items()):
            if n.startswith('test_') and callable(f): f()
        print('TODOS OK (verificar_diario)')
    finally: shutil.rmtree(TMP, ignore_errors=True)
