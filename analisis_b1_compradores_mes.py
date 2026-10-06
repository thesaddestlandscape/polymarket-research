#!/usr/bin/env python3
"""analisis_b1_compradores_mes.py -- ¿quién gana de verdad con los niveles baratos de B1? sobre TODO el último mes
(06-Oct, Javi: "mira en todos los datos del último mes"). Reglas fijadas ANTES de mirar resultados.

Sin libro para el mes, el episodio se define por OPERACIONES (evidencia más débil que el libro, se dice en la salida):
  par garantizado de cada cierre C (15m que cierra en C y 5m que empieza en C-300): ref_largo = TWAP60 oficial en C-900,
  ref_corto = en C-300 (PolyBolt twap60 desde el 24-Sep; antes, media de ticks RTDS chainlink con ws_timestamp en
  [e-62, e-3] s, VALIDADA en los días con ambas); |gap| >= 1 bps; ref_l < ref_c -> A = 15m Up, B = 5m Down; si no al revés.
  COMPRA B1: compra (fila BUY del firehose) de A o de B en [C-300+1,5 s, C) cuya pareja (una compra de la otra pata a
  ±VENTANA ms, recepción) deja precio_A + precio_B + fee(A) + fee(B) < 1 - 0,0005. Ventana principal 1.000 ms; robustez
  250/500/2.000 (todas reportadas).
  PnL a resolución con desenlace OFICIAL: acciones x (pago - precio); el firehose no dice quién fue tomador -> se dan el
  BRUTO y el neto con comisión de tomador 0,07·p·(1-p) (cota pesimista).
  Wallets: PnL B1 vs PnL del resto de su actividad en mercados 5m/15m del mes (compras y ventas a resolución), por día,
  ventana (cierre), persistencia, sin la mejor ventana, walk-forward primera mitad -> segunda mitad del mes.
Uso: python3 analisis_b1_compradores_mes.py [--desde 2026-09-16] [--hasta 2026-10-06]
"""
import argparse
import bisect
import collections
import csv
import glob
import gzip
import statistics as st
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_precierre_rejilla_ask_real import desenlaces  # noqa: E402  (slug -> "Up"/"Down", caché + gamma closed=true)

csv.field_size_limit(10 ** 7)
DL = Path("/root/polymarket-research-datalogs")
PR = Path(__file__).resolve().parent / "data" / "prices"
VENTANAS = [1000, 250, 500, 2000]
FEE = 0.07


def fee(p):
    return FEE * p * (1 - p)


def abrir(p):
    return gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")


def refs_dia(d, pb, acum):
    """Solo en los segundos e múltiplos de 300: PolyBolt twap60 oficial y suma/recuento de ticks RTDS chainlink con
    ws_timestamp en [e-62, e-3] (cada tick cae como mucho en una ventana: 59 s < 300 s)."""
    for suf in (".csv", ".csv.gz"):
        f = PR / f"polybolt_{d}{suf}"
        if f.exists():
            for r in csv.DictReader(abrir(f)):
                if r["canal"] == "twap60" and r.get("source", "chainlink") == "chainlink":   # sin columna source antes del 02-Oct (twap60 siempre Chainlink)
                    e = int(r["event_ts_ms"]) // 1000
                    if e % 300 == 0:
                        pb[(r["asset"], e)] = float(r["value"])
        f = PR / f"chainlink_{d}{suf}"
        if f.exists():
            vistos = set()
            for r in csv.DictReader(abrir(f)):
                if r.get("source", "chainlink") != "chainlink" or not r.get("ws_timestamp_ms"):
                    continue
                ts = int(r["ws_timestamp_ms"]) // 1000
                if (r["asset"], ts) in vistos:
                    continue                    # un tick por segundo y moneda
                vistos.add((r["asset"], ts))
                e = -(-(ts + 3) // 300) * 300
                if ts >= e - 62:
                    x = acum[(r["asset"], e)]
                    x[0] += float(r["price_usd"])
                    x[1] += 1


def twap_rtds(acum, asset, e):
    x = acum.get((asset, e))
    return x[0] / x[1] if x and x[1] >= 20 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-09-16")
    ap.add_argument("--hasta", default="2026-10-06")
    a = ap.parse_args()
    d0, d1 = date.fromisoformat(a.desde), date.fromisoformat(a.hasta)
    dias = [(d0 + timedelta(days=i)).isoformat() for i in range((d1 - d0).days + 1)]
    # ---- referencias
    PB, RT = {}, collections.defaultdict(lambda: [0.0, 0])
    valid = []
    for d in dias + [(d0 - timedelta(days=1)).isoformat()]:
        refs_dia(d, PB, RT)

    def ref(asset, e):
        if (asset, e) in PB:
            return PB[(asset, e)], "polybolt"
        r = twap_rtds(RT, asset, e)
        return (r, "rtds") if r is not None else (None, None)

    for (asset, e), v in list(PB.items())[::20]:
        r = twap_rtds(RT, asset, e)
        if r is not None:
            valid.append(abs(r / v - 1) * 1e4)
    if valid:
        print(f"validación TWAP60 reconstruido (RTDS) vs oficial (PolyBolt): n={len(valid)} error mediano "
              f"{st.median(valid):.3f} bps, P99 {sorted(valid)[int(len(valid) * .99)]:.3f} bps")
    # ---- firehose: compras/ventas en 5m/15m
    comp = {V: [] for V in VENTANAS}
    n_pares_tot, fuentes, n_des = 0, collections.Counter(), [0, 0]
    for d in dias:   # día a día (OOM con todo el mes en memoria, 06-Oct); se pierde el cierre de 00:00 (~1/96)
        ops = collections.defaultdict(list)
        fs = [DL / f"polymarket_activity_{d}{s}" for s in (".csv", ".csv.gz")]
        f = next((x for x in fs if x.exists()), None)
        if not f:
            print(f"  sin firehose {d}")
            continue
        try:
            for r in csv.DictReader(abrir(f)):
                if r["side"] != "BUY" or r["marco"] not in ("5min", "15min") or not r["market_slug"]:
                    continue
                try:
                    ini = int(r["market_slug"].rsplit("-", 1)[1])
                    t = int(datetime.fromisoformat(r["timestamp_utc"]).timestamp() * 1000)
                    if r["marco"] == "5min" and (ini + 300) % 900 != 0:
                        continue                    # solo el 5m que cierra con un 15m
                    if r["marco"] == "15min" and t < (ini + 600) * 1000:
                        continue                    # solo el último tramo de 5 min del 15m
                    ops[r["market_slug"]].append((t, r["wallet"].lower(), r["outcome"], r["side"], float(r["price"]),
                                                  float(r["size"]), r["activo"], r["marco"]))
                except (ValueError, KeyError):
                    continue
        except (EOFError, OSError) as e:
            print(f"  aviso {f.name}: {type(e).__name__}")

        # ---- pares y compras B1
        def info(slug):
            try:
                mo, _, mk, ini = slug.split("-")[0], slug.split("-")[1], slug.split("-")[2], int(slug.split("-")[-1])
            except (ValueError, IndexError):
                return None
            return mo.upper(), ("5min" if mk == "5m" else "15min" if mk == "15m" else None), ini

        s15 = {}
        for s in ops:
            i = info(s)
            if i and i[1] == "15min":
                s15[(i[0], i[2] + 900)] = s
        s5 = {}
        for s in ops:
            i = info(s)
            if i and i[1] == "5min":
                s5[(i[0], i[2] + 300)] = s
        pares = []
        for (mo, C), sl in s15.items():
            sc = s5.get((mo, C))
            if not sc:
                continue
            rl, fl = ref(mo, C - 900)
            rc, fc = ref(mo, C - 300)
            if rl is None or rc is None:
                fuentes["sin_ref"] += 1
                continue
            if abs((rc / rl - 1) * 1e4) < 1:
                fuentes["gap<1bps"] += 1
                continue
            fuentes[f"{fl}/{fc}"] += 1
            A, B = (("Up", "Down") if rl < rc else ("Down", "Up"))
            pares.append((mo, C, sl, sc, A, B))
        n_pares_tot += len(pares)
        des = desenlaces({x for p in pares for x in (p[2], p[3])})
        n_des[0] += sum(1 for p in pares if p[2] in des and p[3] in des)
        n_des[1] += len(pares)
        for mo, C, sl, sc, A, B in pares:
            if sl not in des or sc not in des:
                continue
            lo, hi = (C - 300) * 1000 + 1500, C * 1000
            ba = [x for x in ops[sl] if x[3] == "BUY" and x[2] == A and lo <= x[0] < hi]
            bb = [x for x in ops[sc] if x[3] == "BUY" and x[2] == B and lo <= x[0] < hi]
            if not ba or not bb:
                continue
            for V in VENTANAS:
                for pata, mias, otras, slug, lado in (("A", ba, bb, sl, A), ("B", bb, ba, sc, B)):
                    ts = [x[0] for x in otras]
                    for x in mias:
                        i, j = bisect.bisect_left(ts, x[0] - V), bisect.bisect_right(ts, x[0] + V)
                        mejor = min((o[4] for o in otras[i:j]), default=None)
                        if mejor is None:
                            continue
                        neto = 1 - x[4] - mejor - fee(x[4]) - fee(mejor)
                        if neto < 0.0005:
                            continue
                        pg = 1.0 if des[slug] == lado else 0.0
                        comp[V].append({"wallet": x[1], "ventana": f"{mo}_{C}", "dia": datetime.fromtimestamp(C, timezone.utc).date().isoformat(),
                                        "moneda": mo, "pata": pata, "precio": x[4], "shares": x[5], "t": x[0], "neto": neto,
                                        "bruto": x[5] * (pg - x[4]), "neto_tom": x[5] * (pg - x[4] - fee(x[4])),
                                        "riesgo": x[5] * x[4]})
        print(f"  {d}: pares {len(pares)}, compras B1 (±1 s) acumuladas {len(comp[1000])}", flush=True)
        del ops
    print(f"pares 5m>15m con ref: {n_pares_tot} | fuentes de ref: {dict(fuentes)} | desenlace oficial {n_des[0]}/{n_des[1]}")
    for V in VENTANAS:
        P = comp[V]
        if not P:
            print(f"±{V} ms: sin compras B1")
            continue
        rk = sum(c["riesgo"] for c in P)
        print(f"±{V:4} ms: compras B1 {len(P)} en {len({c['ventana'] for c in P})} ventanas, {len({c['dia'] for c in P})} días, "
              f"{len({c['wallet'] for c in P})} wallets | PnL bruto {sum(c['bruto'] for c in P):+.0f} $ "
              f"({sum(c['bruto'] for c in P) / rk:+.1%}) neto tomador {sum(c['neto_tom'] for c in P):+.0f} $ "
              f"({sum(c['neto_tom'] for c in P) / rk:+.1%}) sobre {rk:.0f} $")
    P = comp[1000]
    if not P:
        return
    import pickle
    pickle.dump(comp, open(DL / "b1_compras_mes.pkl", "wb"))
    robustez(P)
    # precio vs selección: por descuento del par y pata
    print("\n== ¿Gana el PRECIO? Todas las compras B1 (±1 s), por descuento del par ==")
    for lo, hi in ((0, .01), (.01, .02), (.02, .03), (.03, .05), (.05, .10), (.10, 9)):
        s = [c for c in P if lo <= c["neto"] < hi]
        if s:
            r = sum(c["riesgo"] for c in s)
            print(f"   [{lo:.2f},{hi:.2f}) n={len(s):6} P(gana) {sum(c['bruto'] > 0 for c in s) / len(s):.0%} "
                  f"bruto {sum(c['bruto'] for c in s) / r:+.1%} neto_tom {sum(c['neto_tom'] for c in s) / r:+.1%} "
                  f"ventanas {len({c['ventana'] for c in s})} días {len({c['dia'] for c in s})}")
    for p_ in "AB":
        s = [c for c in P if c["pata"] == p_]
        r = sum(c["riesgo"] for c in s)
        print(f"   pata {p_}: n={len(s)} bruto {sum(c['bruto'] for c in s) / r:+.1%} neto_tom {sum(c['neto_tom'] for c in s) / r:+.1%}")
    por_dia = collections.defaultdict(list)
    for c in P:
        por_dia[c["dia"]].append(c)
    print("   por día (bruto/riesgo): " + " ".join(f"{d[5:]}:{sum(c['bruto'] for c in v) / sum(c['riesgo'] for c in v):+.0%}" for d, v in sorted(por_dia.items())))
    # ---- wallets
    porw = collections.defaultdict(list)
    for c in P:
        porw[c["wallet"]].append(c)
    # pares cubiertos por la misma wallet en la misma ventana
    print(f"\n== Wallets: {len(porw)} compradoras; en >=3 ventanas: {sum(1 for v in porw.values() if len({c['ventana'] for c in v}) >= 3)}; "
          f"en >=5 ventanas y >=3 días: {sum(1 for v in porw.values() if len({c['ventana'] for c in v}) >= 5 and len({c['dia'] for c in v}) >= 3)} ==")
    mitad = sorted({c["dia"] for c in P})
    corte = mitad[len(mitad) // 2]
    filas = []
    for w, cs in porw.items():
        nv = len({c["ventana"] for c in cs})
        if nv < 5:
            continue
        pv = collections.defaultdict(float)
        for c in cs:
            pv[c["ventana"]] += c["bruto"]
        b = sum(c["bruto"] for c in cs)
        r = sum(c["riesgo"] for c in cs)
        mejor = max(pv.values())
        dias_pos = sum(1 for d in {c["dia"] for c in cs} if sum(c["bruto"] for c in cs if c["dia"] == d) > 0)
        ambas = sum(1 for v in {c["ventana"] for c in cs} if {"A", "B"} <= {c["pata"] for c in cs if c["ventana"] == v})
        f1 = [c for c in cs if c["dia"] < corte]
        f2 = [c for c in cs if c["dia"] >= corte]
        roi = lambda s: sum(c["bruto"] for c in s) / sum(c["riesgo"] for c in s) if s and sum(c["riesgo"] for c in s) else None
        filas.append((w, len(cs), nv, len({c["dia"] for c in cs}), dias_pos, b, b / r, b - mejor, ambas, roi(f1), roi(f2),
                      sum(c["neto_tom"] for c in cs)))
    filas.sort(key=lambda x: -x[6])
    print("  wallet      compras ventanas días días+  bruto   ROI    sin_mejor  vent_ambas  ROI_1ªmitad ROI_2ªmitad  neto_tom")
    for x in filas[:15]:
        f = lambda v: "   -  " if v is None else f"{v:+6.1%}"
        print(f"  {x[0][:10]} {x[1]:7} {x[2]:8} {x[3]:4} {x[4]:5} {x[5]:+7.1f} {x[6]:+6.1%} {x[7]:+9.1f} {x[8]:9}   "
              f"{f(x[9])}     {f(x[10])}  {x[11]:+8.1f}")
    # walk-forward agregado
    buenas = {x[0] for x in filas if x[9] is not None and x[9] > 0}
    malas = {x[0] for x in filas if x[9] is not None and x[9] <= 0}
    s2b = [c for c in P if c["dia"] >= corte and c["wallet"] in buenas]
    s2m = [c for c in P if c["dia"] >= corte and c["wallet"] in malas]
    s2r = [c for c in P if c["dia"] >= corte and c["wallet"] not in buenas | malas]
    roi = lambda s: f"{sum(c['bruto'] for c in s) / sum(c['riesgo'] for c in s):+.1%} (n={len(s)})" if s else "-"
    print(f"\n  WALK-FORWARD (corte {corte}): wallets con ROI B1 >0 en la 1ª mitad -> 2ª mitad {roi(s2b)} | con ROI <=0 -> "
          f"{roi(s2m)} | resto de compradores {roi(s2r)}")


def robustez(P):
    """Desglose de las compras B1 por pata x precio de compra x moneda, IC90 bootstrap por DÍAS y concentración."""
    import random
    def ic(s):
        dias = collections.defaultdict(lambda: [0.0, 0.0])
        for c in s:
            dias[c["dia"]][0] += c["bruto"]
            dias[c["dia"]][1] += c["riesgo"]
        ks = list(dias)
        if len(ks) < 5:
            return None
        rng, m = random.Random(5), []
        for _ in range(2000):
            mu = [dias[k] for k in (rng.choice(ks) for _ in ks)]
            m.append(sum(x[0] for x in mu) / max(1e-9, sum(x[1] for x in mu)))
        m.sort()
        return m[100], m[1900]
    print("\n== Robustez: ROI bruto por pata x precio de compra (IC90 por días; % del PnL de la pata en el 1 % de compras más rentables) ==")
    for pata in "AB":
        for lo, hi in ((0, .10), (.10, .30), (.30, .50), (.50, .70), (.70, .90), (.90, 1.0)):
            s = [c for c in P if c["pata"] == pata and lo <= c["precio"] < hi]
            if len(s) < 50:
                continue
            r = sum(c["riesgo"] for c in s)
            b = sum(c["bruto"] for c in s)
            top = sorted((c["bruto"] for c in s), reverse=True)[:max(1, len(s) // 100)]
            i_ = ic(s)
            print(f"   pata {pata} precio [{lo:.2f},{hi:.2f}) n={len(s):6} ROI {b / r:+6.1%} IC90 "
                  f"{'-' if i_ is None else f'[{i_[0]:+.1%},{i_[1]:+.1%}]'} | top 1 % = {sum(top) / b if b > 0 else float('nan'):.0%} del PnL"
                  f" | días + {sum(1 for d in {c['dia'] for c in s} if sum(c['bruto'] for c in s if c['dia'] == d) > 0)}/{len({c['dia'] for c in s})}")
    print("   pata B por moneda: " + " | ".join(
        f"{m}: {sum(c['bruto'] for c in P if c['pata'] == 'B' and c['moneda'] == m) / max(1e-9, sum(c['riesgo'] for c in P if c['pata'] == 'B' and c['moneda'] == m)):+.1%}"
        for m in sorted({c["moneda"] for c in P})))


if __name__ == "__main__":
    main()

