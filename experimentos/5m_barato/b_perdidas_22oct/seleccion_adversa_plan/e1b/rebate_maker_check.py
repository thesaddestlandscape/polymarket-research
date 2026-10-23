#!/usr/bin/env python3
"""rebate_maker_check.py [--telegram] -- SOLO LECTURA. Conciliacion del Maker Rebate (20 % de la comision del tomador, crypto) de la wallet DEDICADA de B:
 1. ACUMULADO segun la API publica sin autenticacion  GET clob.polymarket.com/rebates/current?date=D&maker_address=W  (docs.polymarket.com/programs/maker-rebates)
 2. ESPERADO por formula: 0,2 x 0,07 x C x p x (1-p) por cada relleno maker de movimientos.csv (contabilidad_wallet_dedicada, rol 'maker...')
 3. COBRADO: data-api /activity (tipos MAKER_REBATE, REWARD) y entradas pUSD de movimientos.csv que no sean DEPOSITO/REDENCION
Reglas del programa (docs): pago diario en pUSD, minimo $1 de rebate ACUMULADO para que se emita el pago. Sin claves, sin .env, sin firmar.
Salida: stdout + datalogs/e1b/rebate_check.json. Telegram solo si aparece el primer cobro (latch)."""
import sys, os, json, time, datetime
import pandas as pd, requests

WALLET = '0x659a40FF9920fEBc5a66836213040924343d297F'
CONT = '/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/movimientos.csv'
OUT = os.environ.get('E1B_DIR', '/root/polymarket-research-datalogs/e1b/').rstrip('/') + '/'
DESDE = '2026-10-20'      # primer dia de B real (movimientos.csv)


def main():
    hoy = datetime.datetime.now(datetime.timezone.utc).date(); d = datetime.date.fromisoformat(DESDE); acc = {}; err = []
    while d <= hoy:
        try:
            r = requests.get('https://clob.polymarket.com/rebates/current', params={'date': d.isoformat(), 'maker_address': WALLET}, timeout=25)
            j = r.json() if r.text.strip() not in ('', 'null') else None
            acc[d.isoformat()] = {'mercados': len(j or []), 'rebate_usdc': round(sum(float(x['rebated_fees_usdc']) for x in (j or [])), 6)}
        except Exception as e: err.append((d.isoformat(), repr(e)[:80]))
        d += datetime.timedelta(days=1); time.sleep(0.4)
    m = pd.read_csv(CONT); c = m[(m.tipo == 'COMPRA') & m.rol.fillna('').str.startswith('maker')].copy(); c['dia'] = c.fecha_utc.str[:10]
    c['esperado'] = 0.2 * 0.07 * c['size'] * c.precio * (1 - c.precio); esp = c.groupby('dia').esperado.sum().round(6).to_dict()
    otros = m[~m.tipo.isin(['COMPRA', 'DEPOSITO', 'REDENCION', 'VENTA'])]
    cobros = []
    for t in ('MAKER_REBATE', 'REWARD'):
        try:
            r = requests.get('https://data-api.polymarket.com/activity', params={'user': WALLET, 'type': t, 'limit': 50}, timeout=25).json()
            cobros += [{'tipo': t, 'ts': x.get('timestamp'), 'usdc': x.get('usdcSize')} for x in r]
        except Exception as e: err.append((t, repr(e)[:80]))
    tot_acc = sum(v['rebate_usdc'] for v in acc.values()); tot_esp = sum(esp.values())
    res = {'wallet': WALLET, 'consultado': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'acumulado_api_por_dia': acc, 'esperado_formula_por_dia': esp,
           'total_acumulado_api': round(tot_acc, 6), 'total_esperado_dias_cerrados_en_api': round(sum(esp.get(k, 0) for k, v in acc.items() if v['mercados']), 6),
           'dias_sin_fila_en_api': [k for k, v in acc.items() if not v['mercados']], 'minimo_pago_usdc': 1.0, 'supera_minimo': tot_acc >= 1.0,
           'cobros_data_api': cobros, 'entradas_pusd_no_redencion_ni_deposito': len(otros), 'cobrado_usdc': round(sum((x['usdc'] or 0) for x in cobros) + float(otros.importe_pusd.sum()), 6),
           'movimientos_hasta': m.fecha_utc.max(), 'errores': err}
    os.makedirs(OUT, exist_ok=True); tmp = OUT + 'rebate_check.json.tmp'; json.dump(res, open(tmp, 'w'), indent=1); os.replace(tmp, OUT + 'rebate_check.json')
    print(json.dumps(res, indent=1))
    if '--telegram' in sys.argv and res['cobrado_usdc'] > 0 and not os.path.exists(OUT + 'rebate_cobrado_latch'):
        sys.path.insert(0, '/root/polymarket-research'); from shadow_digest import enviar_telegram
        enviar_telegram(f"💧 Maker rebate de B: PRIMER COBRO detectado {res['cobrado_usdc']} pUSD (acumulado API {tot_acc:.3f}). Ver {OUT}rebate_check.json"); open(OUT + 'rebate_cobrado_latch', 'w').write(res['consultado'])
    return 0


if __name__ == '__main__': sys.exit(main())
