# Validación independiente de H43 (R5K) para un día. Solo lectura. Sin reutilizar scripts del análisis original.
# Uso: python3 -I h43_run.py YYYY-MM-DD
import gzip, sys, csv, json, math
from collections import defaultdict
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
D = sys.argv[1]
SRC = f"/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{D}.csv.gz"
BAND_LO, BAND_HI = 0.10, 0.30           # (0.10, 0.30]
CUM_T = (60.0, 300.0)                   # T in (60, 300]
HAR_T = (60.0, 270.0)                   # T in (60, 270]
UMBRAL = 5000.0
K = 50.0

# 1) mapa token -> (mercado, lado, fin_epoch) desde registro (k rows BTC 5min), 09..15 Oct
MAP = {}
with open('map_raw.csv') as f:
    for r in csv.reader(f):
        # token, mercado, fin_iso, lado, ms
        from datetime import datetime
        MAP[r[0]] = (r[1], r[3], datetime.fromisoformat(r[2]).timestamp())
# 2) desenlaces: caché maker_ms (YES/NO, 100 % cobertura de los 2020 mercados BTC 5m)
OUT = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
def opp(l): return 'NO' if l == 'YES' else 'YES'

# 3) streaming de filas maker del día (tipo F, taker != EXCH) sobre tokens del mapa
acq = defaultdict(list)   # (mkt, s) -> [(ord, T, p, sh, is_acq, in_band_vol)]
tx_sum = defaultdict(lambda: [0.0, 0.0])   # tx -> [sum maker sh, sum taker sh]
tk_sh_total = 0.0; mk_sh_total = 0.0
n_maker = n_taker = n_bad = 0
mk_markets = set()
with gzip.open(SRC, 'rt') as f:
    next(f)
    for line in f:
        c = line.rstrip('\n').split(',')
        if c[0] != 'F':
            continue
        tok = c[9]
        if tok not in MAP:
            continue
        side = c[8]
        ma = float(c[10]); ta = float(c[11])
        if c[7] == EXCH:   # fila del tomador: solo para la comprobación de conservación
            n_taker += 1
            sh = ta if side == '0' else ma
            tk_sh_total += sh
            tx_sum[c[3]][1] += sh
            continue
        n_maker += 1
        sh = ta if side == '0' else ma
        usd = ma if side == '0' else ta
        if sh <= 0 or usd <= 0:
            n_bad += 1
            continue
        mk_sh_total += sh
        tx_sum[c[3]][0] += sh
        q = usd / sh                           # precio del token de la fila
        mkt, lado_t, fin = MAP[tok]
        mk_markets.add(mkt)
        T = fin - float(c[2])
        order = (int(c[1]), int(c[4]))
        if side == '0':                        # compra del token -> adquiere lado_t a q
            x, p, is_acq = lado_t, q, True
        else:                                  # venta del token -> adquiere opuesto a 1-q
            x, p, is_acq = opp(lado_t), 1.0 - q, True
        # precio equivalente para cada lado s (sólo para la variante de volumen bidireccional)
        for s in ('YES', 'NO'):
            ps = q if s == lado_t else 1.0 - q
            vol_in = BAND_LO < ps <= BAND_HI
            if s == x:
                acq[(mkt, s)].append((order, T, p, sh, True, vol_in))
            elif vol_in:
                acq[(mkt, s)].append((order, T, ps, sh, False, vol_in))

# 4) unidades por variante
def run(variant):
    units = []
    for (mkt, s), lst in acq.items():
        if mkt not in OUT:
            continue
        lst.sort(key=lambda e: e[0])
        cum = 0.0; crossed = False; need = K; take = []; skip_unit = False
        for order, T, p, sh, is_acq, vol_in in lst:
            if not crossed:
                if variant == 'CUMV':
                    cum_ok = vol_in and CUM_T[0] < T <= CUM_T[1]
                else:
                    cum_ok = is_acq and (BAND_LO < p <= BAND_HI) and CUM_T[0] < T <= CUM_T[1]
                if not cum_ok:
                    continue
                new = cum + sh
                if new >= UMBRAL:
                    if variant == 'ENTRY' and T > HAR_T[1]:
                        skip_unit = True
                        break
                    crossed = True
                    overflow = new - UMBRAL
                    cum = UMBRAL
                    cand = min(overflow, sh)
                else:
                    cum = new
                    continue
            else:
                cand = sh
            # harvest
            hi_t = 300.0 if variant == 'PRIM300' else HAR_T[1]
            if not is_acq or not (HAR_T[0] < T <= hi_t):
                continue
            if variant != 'HNB' and not (BAND_LO < p <= BAND_HI):
                continue
            if variant == 'HNB' and not (BAND_LO < p <= 1.0):
                pass
            take_here = min(cand, need)
            if take_here <= 0:
                continue
            take.append((p, take_here))
            need -= take_here
            cand = 0.0
            if need <= 1e-9:
                break
        if skip_unit or not crossed:
            continue
        got = sum(t for _, t in take)
        if got <= 0:
            units.append((mkt, s, 0.0, 0.0, got, 'SIN_HARVEST'))
            continue
        cost = sum(t * p for p, t in take)
        win = OUT[mkt]
        w = win if win in ('YES', 'NO') else None
        if w is None:
            units.append((mkt, s, None, None, got, 'SIN_DESENLACE'))
            continue
        ganado = 1.0 if s == w else 0.0
        pnl = sum(t * (ganado - p) for p, t in take)
        units.append((mkt, s, pnl, cost, got, 'COMPLETA' if need <= 1e-9 else 'INCOMPLETA'))
    return units

res = {'dia': D, 'fuente': SRC, 'n_maker_rows_btc5m': n_maker, 'n_taker_rows_btc5m': n_taker, 'n_maker_bad': n_bad,
       'mercados_con_filas': len(mk_markets), 'shares_maker_total': round(mk_sh_total, 2),
       'shares_taker_total': round(tk_sh_total, 2)}
# conservación por tx
mism = sum(1 for v in tx_sum.values() if abs(v[0] - v[1]) > 1e-6 * max(1.0, v[1]))
res['tx_con_shares_maker_distintas_de_taker'] = mism
res['tx_total'] = len(tx_sum)
for variant in ('PRIMARIA', 'HNB', 'CUMV', 'PRIM300', 'ENTRY'):
    us = run(variant)
    comp = [u for u in us if u[5] == 'COMPLETA']
    inc = [u for u in us if u[5] == 'INCOMPLETA']
    sin_des = [u for u in us if u[5] == 'SIN_DESENLACE']
    sin_h = [u for u in us if u[5] == 'SIN_HARVEST']
    pn = sum(u[2] for u in comp); co = sum(u[3] for u in comp)
    mk_comp = len({u[0] for u in comp})
    res[variant] = {
        'n_unidades_completas': len(comp), 'n_mercados_distintos_completas': mk_comp,
        'n_incompletas': len(inc), 'n_sin_desenlace': len(sin_des), 'n_sin_harvest': len(sin_h),
        'coste_eur_usd': round(co, 4), 'pnl': round(pn, 4),
        'EV_ponderado': round(pn / co, 4) if co > 0 else None,
        'EV_media_unidad': round(sum(u[2] / u[3] for u in comp) / len(comp), 4) if comp else None,
        'n_cruces_5000': len(us),
    }
    if variant == 'PRIMARIA':
        with gzip.open(f'unidades_{D}_{variant}.csv.gz', 'wt') as g:
            w = csv.writer(g); w.writerow(['mkt', 's', 'pnl', 'coste', 'acc_harvest', 'estado'])
            for u in us: w.writerow(u)
print(json.dumps(res, indent=1, ensure_ascii=False))
