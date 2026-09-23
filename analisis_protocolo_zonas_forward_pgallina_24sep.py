"""Protocolo completo de promoción (CLAUDE.md) sobre las 2 zonas forward P-GALLINA ya live.
Unidad estadística: MERCADO (condition_id), deduplicado — el ejecutor opera una vez por mercado.
Precio: ask de DECISIÓN, solo filas fillable en decisión (sigue_fillable_decision=1, ratio>=5), post-TWAP.
PnL por 1€ neto de fee (misma fórmula que el buscador/gate)."""
import csv, sys, math, random, statistics as st, collections
sys.path.insert(0, '/root/polymarket-research')  # uso: python3 analisis_protocolo_zonas_forward_pgallina_24sep.py
import buscador_edge_perdido as B, shadow_postmortem as sp
from gate_dias_independientes import robustez_dias

ZONAS = [("DISPERSO", "BTC", "5min", "Up", 0.75, 0.80), ("SNIPER", "ETH", "5min", "Down", 0.70, 0.75)]
CUT = "2026-09-17T00:00:00"   # train 10-16 / forward 17-23 (mismo corte que el análisis original)
rng = random.Random(7)
FEE = 1 - (B._pnl_neto_pgallina(0.5, True) / 1.0)  # (1-0.5)/0.5*(1-fee) -> fee

det = collections.defaultdict(lambda: [0, 0])   # zona -> [detectadas_en_zona(ask det), fillable_decision]
filas = collections.defaultdict(dict)          # zona -> condition_id -> fila (primera en el tiempo)
with open(B.BW_FASE0, encoding='utf-8') as f:
    for r in csv.DictReader(f):
        if r.get('acierto') not in ('0', '1'):
            continue
        ts = r.get('resolved_ts') or r.get('trade_timestamp', '')
        if sp.es_pre_twap(r['marco'], ts):
            continue
        for z in ZONAS:
            arq, act, mar, lado, lo, hi = z
            if (r['arquetipo'], r['activo'], r['marco'], r['lado_wallet']) != (arq, act, mar, lado):
                continue
            try:
                ad = float(r['mejor_ask_deteccion'])
            except (ValueError, KeyError):
                ad = None
            if ad is not None and lo <= ad < hi:
                det[z][0] += 1
                det[z][1] += r.get('sigue_fillable_decision') == '1'
            if r.get('sigue_fillable_decision') != '1':
                continue
            try:
                a = float(r['mejor_ask_decision']); ra = float(r['ratio_vs_stake_decision'])
            except (ValueError, KeyError):
                continue
            if not (lo <= a < hi) or ra < 5:
                continue
            cid = r['condition_id']
            t = r.get('trade_timestamp', '')
            prev = filas[z].get(cid)
            if prev is None or t < prev['t']:
                filas[z][cid] = {'t': t, 'a': a, 'win': r['acierto'] == '1', 'wallet': r['wallet'],
                                 'pnl': B._pnl_neto_pgallina(a, r['acierto'] == '1')}


def wilson_lo(k, n, z=1.645):
    if n == 0:
        return 0
    p = k / n; d = 1 + z * z / n
    return (p + z * z / (2 * n) - z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / d


def boot(v, it=2000):
    b = sorted(st.mean(rng.choices(v, k=len(v))) for _ in range(it)); return b[int(.05 * it)], b[int(.95 * it)]


def boot_dias(rows, it=2000):
    d = collections.defaultdict(list)
    for x in rows: d[x['t'][:10]].append(x['pnl'])
    dias = list(d.values()); res = []
    for _ in range(it):
        s = [p for g in rng.choices(dias, k=len(dias)) for p in g]; res.append(st.mean(s))
    res.sort(); return res[int(.05 * it)], res[int(.95 * it)]


def p_mercado_calibrado(rows, it=5000):
    """Null zero-intelligence: el mercado está calibrado (P(win)=ask). ¿Cuántas veces sale un pnl medio >= observado?"""
    obs = st.mean(x['pnl'] for x in rows); c = 0
    for _ in range(it):
        s = st.mean(B._pnl_neto_pgallina(x['a'], rng.random() < x['a']) for x in rows)
        c += s >= obs
    return (c + 1) / (it + 1)


def g_kelly(v, f=0.10):
    return st.mean(math.log(1 + f * p) for p in v)


def informe(z, rows, etq):
    n = len(rows)
    if n == 0:
        print(f"  {etq}: n=0"); return {}
    v = [x['pnl'] for x in rows]; k = sum(x['win'] for x in rows)
    pa = st.mean(x['a'] for x in rows)
    # breakeven: hit h tal que h*w + (1-h)*(-1) = 0, w medio
    w = st.mean((1 - x['a']) / x['a'] * (1 - FEE) for x in rows); be = 1 / (1 + w)
    wl = wilson_lo(k, n)
    # IC: correlación punto-biserial entre (prob implícita de nuestro lado ~ confianza) y acierto no aplica
    # (una sola dirección, precio casi constante). Proxy honesto: margen hit - breakeven, y 2*(hit-ask).
    ic_proxy = 2 * (k / n - pa)
    bi = boot(v); bd = boot_dias(rows); pm = p_mercado_calibrado(rows)
    h = n // 2; o = sorted(rows, key=lambda x: x['t'])
    m1 = st.mean(x['pnl'] for x in o[:h]) if h else float('nan'); m2 = st.mean(x['pnl'] for x in o[h:])
    rob = robustez_dias([(x['t'], x['pnl']) for x in rows])
    g = g_kelly(v)
    dd = collections.Counter(x['t'][:10] for x in rows)
    wc = collections.Counter(x['wallet'] for x in rows)
    print(f"  {etq}: n_mercados={n} dias={len(dd)} hit={k/n:.3f} ask_medio={pa:.3f} breakeven={be:.3f} "
          f"Wilson90lo={wl:.3f} margen={k/n-be:+.3f} IC_proxy={ic_proxy:+.3f}")
    print(f"     pnl/tr={st.mean(v):+.3f} total={sum(v):+.2f}  CI90 boot={bi[0]:+.3f},{bi[1]:+.3f}  CI90 boot-por-día={bd[0]:+.3f},{bd[1]:+.3f}")
    print(f"     p(mercado calibrado)={pm:.4f}  split-half={m1:+.3f}/{m2:+.3f}  g(f=10%)={g:+.5f}")
    print(f"     robustez días: {rob}  top1 wallet={wc.most_common(1)[0][1]/n:.0%} ({len(wc)} wallets)")
    return dict(n=n, hit=k / n, be=be, wl=wl, ic=ic_proxy, bi=bi, bd=bd, pm=pm, m1=m1, m2=m2, rob=rob, g=g)


for z in ZONAS:
    rows = sorted(filas[z].values(), key=lambda x: x['t'])
    print("=" * 110)
    print(f"ZONA {z[0]}#{z[1]}#{z[2]}#BUY_{z[3]} [{z[4]:.2f},{z[5]:.2f})  por ask DECISIÓN, fillable, dedup por mercado")
    dt, df = det[z]
    print(f"  fill-ability (filas con ask detección en zona -> siguen fillable en decisión): {df}/{dt} = {df/max(dt,1):.1%}")
    R = {}
    R['total'] = informe(z, rows, 'TOTAL  ')
    R['train'] = informe(z, [x for x in rows if x['t'][:19] < CUT], 'TRAIN  ')
    R['fwd'] = informe(z, [x for x in rows if x['t'][:19] >= CUT], 'FORWARD')
    f = R['fwd'] or {}
    checks = [
        ("n>=40 forward (mercados)", f.get('n', 0) >= 40),
        ("IC_proxy>=0.08 forward", f.get('ic', -1) >= 0.08),
        ("Wilson90lo > breakeven forward", f.get('wl', 0) > f.get('be', 1)),
        ("p<0.05 vs mercado calibrado forward", f.get('pm', 1) < 0.05),
        ("CI90 bootstrap forward >0", f.get('bi', (-1,))[0] > 0),
        ("CI90 bootstrap POR DÍA forward >0", f.get('bd', (-1,))[0] > 0),
        ("split-half forward ambas >0", f.get('m1', -1) > 0 and f.get('m2', -1) > 0),
        ("robustez días (total, sin 2 mejores>=0,10)", R['total'].get('rob', {}).get('robusto', False)),
        ("g(f=10%)>0 total", R['total'].get('g', -1) > 0),
        ("g(f=10%)>0 forward", f.get('g', -1) > 0),
    ]
    print("  CHECKS:")
    for nom, ok in checks:
        print(f"     {'✅' if ok else '❌'} {nom}")
    print(f"  => {sum(ok for _, ok in checks)}/{len(checks)} pasan")
