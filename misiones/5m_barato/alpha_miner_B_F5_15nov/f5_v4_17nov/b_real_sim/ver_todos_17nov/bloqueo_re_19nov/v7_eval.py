"""v7_eval.py -- PREREG_V7 (53e9febb): FP/predicciones en ordenes reales de B sin relleno y reproduccion en rellenos reales. Solo lectura, no EV."""
import json, os, csv, collections, numpy as np, pandas as pd
import sys; A1 = 'A1' in sys.argv[1:]; STRICT = 'STRICT' in sys.argv[1:]; WS = 'WS' in sys.argv[1:]
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OWN = '0x659a40ff9920febc5a66836213040924343d297f'; TOLP = 0.001
def parse(inp):
    b = bytes.fromhex(inp[10:]); w = lambda i: int.from_bytes(b[i:i + 32], 'big')
    off_t, off_m, tfill, off_f = w(32), w(64), w(96), w(128)
    def order(s):
        f = [w(s + 32 * k) for k in range(12)]
        return dict(maker='0x' + f[1].to_bytes(32, 'big')[12:].hex(), tokenId=str(f[3]), mA=f[4], tA=f[5], side=f[6])
    to = order(off_t); n = w(off_m); mk = [order(off_m + 32 + w(off_m + 32 * (1 + i))) for i in range(n)]
    nf = w(off_f); fl = [w(off_f + 32 * (1 + i)) for i in range(nf)]
    return to, mk, tfill, fl
CD = {}
for f in ('/root/polymarket-research-datalogs/cola_posicion/calldata_b.jsonl', H + '../calldata_extra.jsonl', H + 'out/calldata_v7.jsonl'):
    if os.path.exists(f):
        for l in open(f):
            try: d = json.loads(l); CD[d['tx']] = d['input']
            except Exception: pass
comp = json.load(open(H + 'out/v7_pares.json'))
O0 = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', usecols=['oid', 'tok', 't_ini', 't_fin'], dtype={'tok': str}).set_index('oid')
O = O0.tok.to_dict(); TI = O0.t_ini.to_dict(); TF = O0.t_fin.to_dict()
# rellenos reales: filas maker propias (hash = oid) -> tx y ts
fills = collections.defaultdict(list)
for r in csv.DictReader(open('/root/polymarket-research-datalogs/cola_posicion/b_tx_all.csv')):
    if r['maker'] == OWN: fills[r['hash']].append((float(r['ts']), r['tx']))
T2 = pd.read_pickle(H + '../tomador_202.pkl')[['oid', 'causa']].set_index('oid').causa.to_dict()
res = collections.Counter(); ex = []
for r in csv.DictReader(open(H + ('out/v7_cand_ws.csv' if WS else 'out/v7_cand.csv'))):
    oid, tx, ts, L = r['oid'], r['tx'], float(r['ts']), float(r['L']); own = O.get(oid)
    fl = sorted(fills.get(oid, [])); same = any(t == tx for _, t in fl); first = fl[0][0] if fl else None
    if not same and first is not None and ts > first + 0.3: res['tras_relleno_excl'] += 1; continue
    if WS and not same and not (TI[oid] + 0.1 <= float(r['ts_ws']) <= TF[oid] - 0.1): res['fuera_vida_ws'] += 1; continue
    if STRICT and not same and not (TI[oid] + 3.1 <= ts <= TF[oid] + 1.4): res['fuera_estricto'] += 1; continue
    inp = CD.get(tx)
    if inp is None or not inp.startswith('0x3c2b4399'): res['missing_calldata'] += 1; continue
    to, mk, tfill, fls = parse(inp)
    if to['tokenId'] == own and to['side'] == 1: eq = to['tA'] / to['mA']; tsz = to['mA'] / 1e6
    elif to['tokenId'] == comp.get(own) and to['side'] == 0: eq = 1 - to['mA'] / to['tA']; tsz = to['tA'] / 1e6
    else: res['tomadora_no_es_del_par_o_dir'] += 1; continue
    rem = 1 - tfill / to['mA'] if to['mA'] else 0.0; R = tsz * rem
    if A1 and to['side'] == 0:
        got = 0.0
        for o, q in zip(mk, fls):
            if o['side'] == 0 and o['mA']: got += q * o['tA'] / o['mA'] / 1e6   # maker compra propio (mint): acciones = fl*tA/mA
            elif o['side'] == 1: got += q / 1e6                                  # maker vende comp: fl en acciones
        R = tsz - got
    cruza = eq <= L + TOLP; tt = float(r['min_eq']) < L - TOLP
    k = 'REAL' if same else ('REAL_300ms' if first is not None and abs(ts - first) <= 0.3 else 'SIN')
    if same:
        res['real_tx'] += 1; res['real_cruza'] += cruza
        c1 = str(T2.get(oid, '')).startswith('1_'); res['real_c1'] += c1; res['real_c1_cruza'] += (c1 and cruza)
        continue
    if not cruza: res[k + '_no_cruza'] += 1; continue
    if tt: res[k + '_TT_contradiccion'] += 1; continue
    if R <= 0.01: res[k + '_cruza_sin_resto'] += 1; continue
    res['pred'] += 1; res['pred_' + k] += 1
    if k == 'SIN': ex.append((oid, tx, L, round(eq, 4), round(R, 2), r['dir']))
fp = res['pred_SIN']; pr = res['pred']
print(dict(res))
print(f"V7 predicciones {pr} | FP (orden real viva sin relleno en 300 ms) {fp} | FP/pred = {fp/max(pr,1):.3f} | criterio: <=0,10 acepta, >=0,30 refuta")
print(f"reproduccion rellenos reales: cruza {res['real_cruza']}/{res['real_tx']} ; clase 1: {res['real_c1_cruza']}/{res['real_c1']}")
pd.DataFrame(ex, columns=['oid', 'tx', 'L', 'eq', 'R', 'dir']).to_csv(H + f"out/v7_fp{'_A1' if A1 else ''}{'_STRICT' if STRICT else ''}{'_WS' if WS else ''}.csv", index=False)
