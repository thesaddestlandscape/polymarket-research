#!/usr/bin/env python3
"""(1) Quién se lleva el ask y cuántos ms antes que nosotros — releído de cron2_out_*.json (intento previo, misma extracción).
Relojes: rx = recepción local; ex = sello del exchange (WS). Nuestro print propio llega a rx ≈ envío + 237..252 ms (F1 15-Oct, 3 órdenes);
el retraso mínimo de un tomador (cualquiera) se acota con 145 ms (FOK no casable 213 vs GTC 68 ms, 07-Oct) — SUPUESTO para terceros."""
import json, collections, sys
def pct(x):
    x = sorted(v for v in x if v is not None); n = len(x)
    if not n: return 'n=0'
    q = lambda p: x[min(n - 1, int(p * n))]
    return f'n={n} P10/25/50/75/90={q(.1)}/{q(.25)}/{q(.5)}/{q(.75)}/{q(.9)} min={x[0]} max={x[-1]}'
for fn in ('primeros', 'todos'):
    R = json.load(open(f'/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/salidas/cron2_out_{fn}.json'))
    R = [r for r in R if r.get('trigger') and r.get('max_gap_q5_120s', 0) <= 60000 and r.get('max_gap_q15_120s', 0) <= 60000]
    print(f'\n######## {fn}: n={len(R)} (sin huecos de feed >60 s)')
    for nom, sel in (('NO_EJEC (B/C a L215)', lambda r: r['cls215'][:1] in 'BC'), ('EJEC (A/D)', lambda r: r['cls215'][:1] in 'AD')):
        S = [r for r in R if sel(r)]
        cons = [r for r in S if r.get('gone_rx_t0_ms') is not None and r.get('trades_n_T_gone', 0) > 0 and r['gone_rx_t0_ms'] <= 215]
        canc = [r for r in S if r.get('gone_rx_t0_ms') is not None and r.get('trades_n_T_gone', 0) == 0 and r['gone_rx_t0_ms'] <= 215]
        print(f'== {nom}: n={len(S)} gana {sum(1 for r in S if r["gana"])} | nivel consumido por compras antes de 215 ms: {len(cons)} (gana {sum(1 for r in cons if r["gana"])}) | cancelado/recotizado sin compras: {len(canc)} (gana {sum(1 for r in canc if r["gana"])})')
        if not cons: continue
        x_ex = [r['cons_ex_trig_ms'] for r in cons]; x_rx = [r['cons_rx_t0_ms'] for r in cons]
        print('   1ª compra competidora, ex - trigger_ex (ms):', pct(x_ex))
        print('   1ª compra competidora, rx - t0 (ms):', pct(x_rx))
        print('   feed trigger (t0 - trigger_ex):', pct([r['feed_ms'] for r in cons]))
        for lim in (50, 100, 145, 175, 215):
            print(f'     ex-trig < {lim} ms: {sum(1 for v in x_ex if v < lim)}/{len(x_ex)}  | rx-t0 < {lim}: {sum(1 for v in x_rx if v < lim)}/{len(x_rx)}')
        # ventaja frente a NUESTRO print (rx t0 + 245 ms, mediana F1)
        print('   ventaja sobre nuestro print (245 - (rx-t0)) ms:', pct([245 - v for v in x_rx]))
        # cota de envío del competidor: envío <= casado_ex - 145 ms; relativo al trigger_ex
        print('   cota superior del ENVÍO competidor rel. al trigger_ex (casado_ex - 145):', pct([v - 145 for v in x_ex]),
              '| enviado ANTES del trigger (cota):', sum(1 for v in x_ex if v - 145 < 0), '/', len(x_ex))
        print('   ... rel. a NUESTRA detección t0 (casado_rx - 20 feed mín - 145):', pct([v - 165 for v in x_rx]),
              '| enviado antes de que lo viéramos:', sum(1 for v in x_rx if v - 165 < 0), '/', len(x_rx))
        print('   trigger de esos:', collections.Counter(r['trigger'] for r in cons), '| binance onset>=1bp previo:', sum(1 for r in cons if r.get('binE_onset_vs_trig_ms') is not None))
        print('   wallets:', collections.Counter((r.get('wallet') or 'missing')[:10] for r in cons).most_common(8))
        print('   compra competidora previa al trigger (3 s, <=plim):', sum(1 for r in cons if r['cons_pre_n'] > 0), '/', len(cons))
