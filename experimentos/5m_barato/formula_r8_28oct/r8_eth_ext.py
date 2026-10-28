import sys, os
E4 = '/root/polymarket-research/experimentos/5m_barato/'
for d in ('formula_r5_28oct', 'formula_r4_28oct', 'formula_r3_28oct'): sys.path.insert(0, E4 + d)
import r5
r5.EXT = E4 + 'formula_r8_28oct/ext_eth/'; r5.TMP = E4 + 'formula_r8_28oct/ext_eth/tmp/'
r5.AWK = r5.AWK.replace('"BTC"', '"ETH"').replace('BTCUSDT', 'ETHUSDT')
days = sorted(f[2:12] for f in os.listdir(E4 + 'formula_r6_28oct/fills') if f.startswith('f_'))
for d in days:
    try: r5.ext(d)
    except Exception as e: print(d, 'ERROR', repr(e), flush=True)
