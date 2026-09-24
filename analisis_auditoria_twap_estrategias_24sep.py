#!/usr/bin/env python3
"""analisis_auditoria_twap_estrategias_24sep.py -- auditoría de TODAS las estrategias shadow
5/15min (las ~33 sin regla TWAP + las de ballenas, y como referencia las ya corregidas)
frente a la regla REAL de resolución (TWAP60 Chainlink al cierre vs TWAP60 en la apertura).

Pendiente del 24-Sep (Javi): "revisaste las de arquetipo A... te quedaban otras 26 más las
de ballenas para ver si nos daba más ventaja y edge, porque las mediciones actuales no eran
correctas".

Para cada señal (PRIMERA predicción por strategy+market_id+decision, 5/15min, 6 monedas):
  ref   = media Chainlink (hora del oráculo, ws_timestamp_ms) en [apertura-60, apertura]
  proy  = >60 s al cierre: último tick <= t; último minuto: media conocida + spot*resto
  z     = |ln(proy/ref)| / (sigma_1s * sqrt(T_eff_s)), sigma_1s de los últimos 300 s,
          T_eff igual que shadow_predict._t_efectivo_twap_h (suelo 15 s)
  coincide = dirección de la señal == signo(proy-ref)
Precio de entrada:
  mkt = precio de la señal (precio_yes_mercado) -- el que usa results.csv
  ask = best_ask REAL de nuestro token en libro_book_ws (datalogs), primera fila con
        ts >= t y <= t+60 s (orden temporal estricto, sin look-ahead). Sin profundidad:
        el log agregado no la trae -> es cota optimista de fill-ability.
Token YES/NO sin API: el token ganador acaba con best_bid alto; outcome_real dice si es YES.
PnL a 1 EUR, fee cripto 7 % sobre la ganancia (NUNCA pnl_neto, que es stake Kelly).
Salida: data/shadow/auditoria_twap_estrategias_24sep.json + resumen por stdout.
Streaming y día a día (RAM justa en el VPS).
"""
import bisect
import csv
import gzip
import json
import math
import random
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
RESULTS = REPO / "data/shadow/results.csv"
OUT = REPO / ("data/shadow/auditoria_twap_estrategias_24sep.json" if not __import__("os").environ.get("DESDE") else f"data/shadow/auditoria_twap_estrategias_forward_{__import__('os').environ['DESDE']}.json")
DESDE = __import__("os").environ.get("DESDE", "2026-09-04")   # forward: DESDE=2026-09-25
DUR = {"5min": 300, "15min": 900}
ACTIVOS = {"BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"}
FEE = 0.07
ASK_MAX_S = 60
TWAP_YA = ("UPDOWN_GBM", "GBM_LATE")   # familias ya corregidas el 24-Sep (referencia)
csv.field_size_limit(10_000_000)


def ts(s):
    d = datetime.fromisoformat(s.replace("Z", "+00:00"))
    return (d if d.tzinfo else d.replace(tzinfo=timezone.utc)).timestamp()


def abrir(p):
    return gzip.open(p, "rt") if str(p).endswith(".gz") else open(p)


def fichero(base, d):
    for suf in (".csv", ".csv.gz"):
        p = base / f"{d}{suf}" if False else Path(f"{base}_{d}{suf}")
        if p.exists():
            return p
    return None


def pnl1(entry, ac):
    return (1 - entry) / entry * (1 - FEE) if ac else -1.0


def cargar_senales():
    vistos, sen = set(), []
    with open(RESULTS, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            pt = r.get("prediction_timestamp") or ""
            if pt < DESDE:
                continue
            sub = r.get("subtype") or ""
            if "#" not in sub:
                continue
            act, marco = sub.split("#")[0], sub.split("#")[-1]
            if marco not in DUR or act not in ACTIVOS or r.get("acierto") not in ("0", "1"):
                continue
            dec = r.get("decision")
            if dec not in ("BUY_YES", "BUY_NO"):
                continue
            k = (r["strategy"], r["market_id"], dec)
            if k in vistos:
                continue
            vistos.add(k)
            try:
                py = float(r["precio_yes_mercado"])
                t, fin = ts(pt), ts(r["end_date"])
            except (ValueError, KeyError):
                continue
            sen.append((r["strategy"], act, marco, r["market_id"], dec, t, fin, py,
                        int(r["acierto"]), (r.get("outcome_real") or "").upper()))
    return sen


def chainlink(dia):
    serie = defaultdict(lambda: ([], []))
    d0 = datetime.fromisoformat(dia)
    for d in ((d0 - timedelta(days=1)).date().isoformat(), dia):
        p = fichero(REPO / "data/prices/chainlink", d)
        if not p:
            continue
        with abrir(p) as f:
            for r in csv.DictReader(f):
                try:
                    t = int(r["ws_timestamp_ms"]) / 1000
                    v = float(r["price_usd"])
                except (ValueError, TypeError, KeyError):
                    continue
                if d != dia and t < d0.replace(tzinfo=timezone.utc).timestamp() - 1800:
                    continue
                serie[r["asset"]][0].append(t)
                serie[r["asset"]][1].append(v)
    out = {}
    for a, (xs, ys) in serie.items():
        o = sorted(dict(zip(xs, ys)).items())
        out[a] = ([x for x, _ in o], [y for _, y in o])
    return out


def media(s, t0, t1):
    xs, ys = s
    i, j = bisect.bisect_left(xs, t0), bisect.bisect_right(xs, t1)
    return (sum(ys[i:j]) / (j - i), j - i) if j > i else (None, 0)


def estado_twap(s, t, ini, fin):
    ref, nr = media(s, ini - 60, ini)
    if ref is None or nr < 10 or t < ini:
        return None
    xs, ys = s
    i = bisect.bisect_right(xs, t) - 1
    if i < 0 or t - xs[i] > 10:
        return None
    spot = ys[i]
    resto = max(0.0, fin - t)
    if resto > 60:
        proy = spot
    else:
        m, n = media(s, fin - 60, t)
        if m is None or n < 10:
            return None
        tr = max(0.0, t - (fin - 60))
        proy = (m * tr + spot * resto) / (tr + resto) if (tr + resto) > 0 else m
    j = bisect.bisect_left(xs, t - 300)
    rets = [math.log(ys[k + 1] / ys[k]) / math.sqrt(max(xs[k + 1] - xs[k], 1e-3))
            for k in range(j, i) if ys[k] > 0 and ys[k + 1] > 0]
    if len(rets) < 30:
        return None
    mu = sum(rets) / len(rets)
    sig = math.sqrt(sum((x - mu) ** 2 for x in rets) / (len(rets) - 1))
    teff = max(resto - 40 if resto > 60 else resto ** 3 / (3 * 3600), 15.0)
    z = abs(math.log(proy / ref)) / (sig * math.sqrt(teff)) if sig > 0 else None
    return ("BUY_YES" if proy > ref else "BUY_NO"), z, resto


def libro(dia, mids):
    """{market_id: {asset_id: ([t], [ask], ultimo_bid)}} del log agregado del websocket."""
    L = defaultdict(lambda: defaultdict(lambda: ([], [], None)))
    for d in (dia, (datetime.fromisoformat(dia) + timedelta(days=1)).date().isoformat()):
        p = fichero(DATALOGS / "libro_book_ws", d)
        if not p:
            continue
        with abrir(p) as f:
            for r in csv.DictReader(f):
                m = r.get("market_id")
                if m not in mids:
                    continue
                try:
                    t = ts(r["timestamp_utc"])
                    ask = float(r["best_ask_ultimo"]) if r["best_ask_ultimo"] else None
                    bid = float(r["best_bid_ultimo"]) if r["best_bid_ultimo"] else None
                except (ValueError, KeyError):
                    continue
                xs, asks, _ = L[m][r["asset_id"]]
                xs.append(t)
                asks.append(ask)
                L[m][r["asset_id"]] = (xs, asks, bid)
    return L


def token_yes(tok, outcome):
    """asset_id del YES: el que acaba con bid más alto es el ganador."""
    if len(tok) != 2 or outcome not in ("YES", "NO", "UP", "DOWN"):
        return None
    (a1, v1), (a2, v2) = tok.items()
    b1, b2 = v1[2] or 0, v2[2] or 0
    if abs(b1 - b2) < 0.5:
        return None
    gan, per = (a1, a2) if b1 > b2 else (a2, a1)
    return gan if outcome in ("YES", "UP") else per


def ask_tras(serie, t):
    xs, asks, _ = serie
    i = bisect.bisect_left(xs, t)
    while i < len(xs) and xs[i] - t <= ASK_MAX_S:
        a = asks[i]
        if a is not None and 0.01 < a < 0.99:
            return a
        i += 1
    return None


def zb(z):
    if z is None:
        return "z?"
    return "z<0.5" if z < 0.5 else "z0.5-1" if z < 1 else "z1-2" if z < 2 else "z>=2"


def resumen(xs):
    n = len(xs)
    fa = [x for x in xs if x["pa"] is not None]
    dias = defaultdict(float)
    for x in fa:
        dias[x["dia"]] += x["pa"]
    out = {"n": n, "hit": round(sum(x["ac"] for x in xs) / n, 3) if n else None,
           "eur_mkt": round(sum(x["pm"] for x in xs) / n, 3) if n else None,
           "n_ask": len(fa), "eur_ask": round(sum(x["pa"] for x in fa) / len(fa), 3) if fa else None,
           "dias": len(dias), "dias_pos": sum(1 for v in dias.values() if v > 0)}
    if len(fa) >= 20:
        fa_o = sorted(fa, key=lambda x: x["t"])
        h = len(fa_o) // 2
        out["mitades_ask"] = [round(sum(x["pa"] for x in fa_o[:h]) / h, 3),
                              round(sum(x["pa"] for x in fa_o[h:]) / (len(fa_o) - h), 3)]
        # IC90 bootstrap por días (bloques = días independientes)
        porlado = defaultdict(list)
        for x in fa:
            porlado[x["dia"]].append(x["pa"])
        ds = list(porlado.values())
        rng = random.Random(7)
        meds = []
        for _ in range(1000):
            m = [v for _ in ds for v in rng.choice(ds)]
            meds.append(sum(m) / len(m))
        meds.sort()
        out["ic90_ask_dias"] = [round(meds[50], 3), round(meds[949], 3)]
    return out


def main():
    sen = cargar_senales()
    print(f"señales 5/15min desde {DESDE}: {len(sen)}", flush=True)
    por_dia = defaultdict(list)
    for s in sen:
        por_dia[datetime.fromtimestamp(s[5], timezone.utc).date().isoformat()].append(s)
    filas = []
    for dia in sorted(por_dia):
        cl = chainlink(dia)
        mids = {s[3] for s in por_dia[dia]}
        L = libro(dia, mids)
        for (st, act, marco, mid, dec, t, fin, py, ac, outc) in por_dia[dia]:
            ser = cl.get(act)
            e = estado_twap(ser, t, fin - DUR[marco], fin) if ser else None
            entry = py if dec == "BUY_YES" else 1 - py
            if not (0.01 < entry < 0.99):
                continue
            ty = token_yes(L.get(mid, {}), outc)
            pa = None
            if ty:
                tn = next((a for a in L[mid] if a != ty), None)
                tok = ty if dec == "BUY_YES" else tn
                a = ask_tras(L[mid][tok], t) if tok else None
                pa = pnl1(a, ac) if a else None
            filas.append({"st": st, "act": act, "marco": marco, "dia": dia, "t": t, "ac": ac,
                          "dec": dec, "bpy": f"{int(py / 0.05 + 1e-9) * 0.05:.2f}",
                          "pm": pnl1(entry, ac), "pa": pa,
                          "coinc": (None if e is None else e[0] == dec),
                          "z": None if e is None else e[1],
                          "resto": None if e is None else e[2]})
        print(f"  {dia}: {len(por_dia[dia])} señales, chainlink={sorted(cl)}, mercados libro={len(L)}",
              flush=True)
        del cl, L
    grupos = defaultdict(list)
    for x in filas:
        # 24-Sep (Javi: "¿nos pasa en más estrategias?"): mismo micro-bucket que gate_bucket_propio
        # (precio_yes_mercado, paso 0,05) para cruzar sus bueno_confirmado con el ask real.
        grupos[("BUCKET", f"{x['st']}#{x['act']}#{x['marco']}#{x['dec']}", x["bpy"])].append(x)
        base = (x["st"], x["act"], x["marco"])
        grupos[base + ("TODO",)].append(x)
        if x["coinc"] is None:
            grupos[base + ("sin_twap",)].append(x)
            continue
        c = "coincide" if x["coinc"] else "contra"
        grupos[base + (c,)].append(x)
        grupos[base + (c, zb(x["z"]))].append(x)
        if x["coinc"] and x["z"] is not None and x["z"] >= 1:
            grupos[base + ("coincide_z>=1",)].append(x)
        grupos[(x["st"], "ALL", x["marco"], c)].append(x)
        if x["coinc"] and x["z"] is not None and x["z"] >= 1:
            grupos[(x["st"], "ALL", x["marco"], "coincide_z>=1")].append(x)
        grupos[(x["st"], "ALL", x["marco"], "TODO")].append(x)
    res = {"|".join(k): resumen(v) for k, v in grupos.items() if len(v) >= 10}
    OUT.write_text(json.dumps({"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                               "desde": DESDE, "n_filas": len(filas), "grupos": res},
                              indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"filas={len(filas)} grupos={len(res)} -> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
