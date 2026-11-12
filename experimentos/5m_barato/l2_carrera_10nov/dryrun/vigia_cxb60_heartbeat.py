#!/usr/bin/env python3
"""vigia_cxb60_heartbeat.py (PLAN C6, NO instalado) -- cron */5: avisa por Telegram si heartbeat.json del dry-run B-CXB60 tiene >5 min, el proceso del pid guardado no vive, el status no es RUNNING, o el lag del flujo W supera 600 s.
Solo lectura; 0 ordenes. Latch por firma estable (estado+dia, NO valores recalculados) para no spamear: un aviso por episodio. Salida 0 sano / 1 problema."""
import os, sys, json, time
D = os.environ.get('CXB60_DIR', '/root/polymarket-research-datalogs/cxb60_dryrun').rstrip('/') + '/'; LATCH = D + 'vigia_latch.json'      # CXB60_DIR / CXB60_SIN_TELEGRAM solo para pruebas en seco


def main():
    prob = None
    try: hb = json.load(open(D + 'heartbeat.json'))
    except (OSError, ValueError): hb = None; prob = 'sin heartbeat.json'
    if hb:
        edad = time.time() - hb['wall']
        pid = None
        try: pid = int(open(D + 'cxb60.pid').read().strip())
        except (OSError, ValueError): pass
        vive = pid is not None and os.path.exists(f'/proc/{pid}') and 'cxb60_dryrun_fase0.py' in open(f'/proc/{pid}/cmdline').read().replace('\0', ' ')
        if edad > 300: prob = f'heartbeat de hace {edad / 60:.0f} min'
        elif hb['status'] != 'RUNNING': prob = f"status {hb['status']}"
        elif not vive: prob = 'pid ausente o no es el dry-run'
        elif hb.get('lag_s') is not None and hb['lag_s'] > 600: prob = f"lag del flujo {hb['lag_s']:.0f} s (maker_ms sin crecer?)"
    firma = prob.split(' ')[0] + time.strftime('%Y%m%d', time.gmtime()) if prob else None
    st = json.load(open(LATCH)) if os.path.exists(LATCH) else {}
    if prob and st.get('firma') != firma:
        if os.environ.get('CXB60_SIN_TELEGRAM'): print('AVISO (seco, sin Telegram): cxb60 dry-run: ' + prob)
        else:
            try:
                sys.path.insert(0, '/root/polymarket-research'); from shadow_digest import enviar_telegram; enviar_telegram('cxb60 dry-run: ' + prob)
            except Exception as e: print('no pude avisar', e)
        json.dump(dict(firma=firma, t=time.time()), open(LATCH, 'w'))
    if not prob and st.get('firma'): json.dump({}, open(LATCH, 'w'))
    print('PROBLEMA:' if prob else 'sano', prob or ''); sys.exit(1 if prob else 0)


if __name__ == '__main__': main()
