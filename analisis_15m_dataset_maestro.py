#!/usr/bin/env python3
"""analisis_15m_dataset_maestro.py -- DATASET MAESTRO del mercado de 15 min como activo autónomo (06-Oct, Javi: "tratemos
el 15m como un mercado autónomo y busquemos cualquier variable observable que prediga su próximo movimiento o su fair
value con ventaja suficiente para sobrevivir a nuestra latencia real").

Fuente: registro ms (maker_ms_*.csv.gz; desde 05-Oct 16:06Z). Para cada mercado 15m (cripto Up/Down) una REJILLA cada
REJILLA_MS durante toda su vida (inicio+5 s .. cierre-5 s). Rasgos en t con SOLO datos cuya hora de RECEPCIÓN <= t:
  libro 15m YES y NO (nivel 1: bid, ask, tamaños, spread, mid, microprecio, desequilibrio), edad del ask/bid/mid,
  cambios de top y cancelaciones (menos tamaño al mismo precio sin operación) en 1 s / 5 s, operaciones y volumen firmado
  (lado del tomador) en 1 s / 5 s / 30 s, velocidad y aceleración del mid (1 s, 5 s), tiempo desde la última operación;
  tiempo desde apertura y hasta cierre;
  referencia: Chainlink spot (ticks RTDS source=chainlink, por hora de RECEPCIÓN) vs referencia oficial de apertura
  (TWAP60 PolyBolt en el inicio), z = ln(S/ref)/(σ_1s·sqrt(T_rest)) con σ de los últimos 300 s, FV = Φ(z),
  mispricing = FV - ask_YES y (1-FV) - ask_NO; retornos de Chainlink 5 s / 30 s;
  5m concurrente (el que cubre t): mid YES y su variación 1 s / 5 s;
  Binance: retorno del aggTrade 1 s / 5 s / 30 s, nº de operaciones 1 s.
Objetivos (FUTURO, solo para evaluar): mid YES a +0,5/1/2/5/10/30 s; ask YES y ask NO a +150/200/215/250/300 ms; bid YES
y bid NO a +215 ms + H (H = 5/30/60 s) para la ida y vuelta; desenlace oficial (YES/NO).
Salida: CSV (uno por ejecución). Uso: --desde 2026-10-05T16:10 --out <csv> [--rejilla 500]
"""
import argparse
import bisect
import collections
import csv
import glob
import gzip
import math
import statistics as st
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")
PRICES = Path(__file__).resolve().parent / "data" / "prices"
SIM = {"BTC": "BTCUSDT", "ETH": "ETHUSDT", "SOL": "SOLUSDT", "XRP": "XRPUSDT", "DOGE": "DOGEUSDT", "BNB": "BNBUSDT"}
LAT = [150, 200, 215, 250, 300]
HMID = [500, 1000, 2000, 5000, 10000, 30000]
HRT = [5000, 30000, 60000]


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


class Serie:
    """Serie compacta (arrays): tiempos int64 y, para el libro, bid/ask en céntimos int16 (-1 = sin nivel) y tamaños
    float32; para precios simples (Binance/Chainlink) valores float64. s.v[i] / s[i] devuelven el valor como antes."""
    def __init__(self, libro=False):
        from array import array
        self.libro = libro
        self.t = array("q")
        if libro:
            self.b, self.a, self.bs, self.as_ = array("h"), array("h"), array("f"), array("f")
        else:
            self.p = array("d")

    def add_libro(self, t, bid, ask, bsz, asz):
        self.t.append(t)
        self.b.append(-1 if bid is None else int(round(bid * 100)))
        self.a.append(-1 if ask is None else int(round(ask * 100)))
        self.bs.append(bsz)
        self.as_.append(asz)

    def add(self, t, p):
        self.t.append(t)
        self.p.append(p)

    def ordenar(self):
        from array import array
        n = len(self.t)
        if all(self.t[i] <= self.t[i + 1] for i in range(n - 1)):
            return
        o = sorted(range(n), key=self.t.__getitem__)
        self.t = array("q", (self.t[i] for i in o))
        if self.libro:
            self.b = array("h", (self.b[i] for i in o))
            self.a = array("h", (self.a[i] for i in o))
            self.bs = array("f", (self.bs[i] for i in o))
            self.as_ = array("f", (self.as_[i] for i in o))
        else:
            self.p = array("d", (self.p[i] for i in o))

    @property
    def v(self):
        return self

    def __len__(self):
        return len(self.t)

    def __getitem__(self, i):
        if isinstance(i, slice):
            return [self[k] for k in range(*i.indices(len(self.t)))]
        if self.libro:
            b, a = self.b[i], self.a[i]
            return (None if b < 0 else b / 100, None if a < 0 else a / 100, float(self.bs[i]), float(self.as_[i]))
        return self.p[i]

    def idx(self, t):
        return bisect.bisect_right(self.t, t) - 1

    def en(self, t):
        i = self.idx(t)
        return self[i] if i >= 0 else None


def cargar(desde_ms):
    meta = {}
    q = collections.defaultdict(lambda: Serie(libro=True))
    tr = collections.defaultdict(list)
    bn = collections.defaultdict(Serie)
    for f in sorted(glob.glob(str(DL / "maker_ms_*.csv.gz")), key=lambda f: Path(f).stat().st_mtime):
        try:
            for ln in gzip.open(f, "rt"):
                c = ln.rstrip("\n").split(",")
                tp = c[0]
                if tp == "k":
                    if c[4] in ("5min", "15min"):
                        meta[c[2]] = (c[3], c[4], c[5], int(datetime.fromisoformat(c[6]).timestamp()), c[7])
                elif tp == "q":
                    m = meta.get(c[2])
                    if not m:
                        continue
                    t = int(c[7]) if len(c) > 7 and c[7] else int(c[1])
                    if t < desde_ms - 60_000:
                        continue
                    g = lambda x: None if x in ("", "None") else float(x)
                    q[c[2]].add_libro(t, g(c[3]), g(c[4]), g(c[5]) or 0.0, g(c[6]) or 0.0)
                elif tp == "t":
                    if c[2] in meta:
                        t = int(c[6]) if len(c) > 6 and c[6] else int(c[1])
                        if t >= desde_ms - 60_000:
                            tr[c[2]].append((t, float(c[3]), 1 if c[4] == "BUY" else -1, float(c[5])))
                elif tp == "x":
                    if len(c) > 7 and c[7]:
                        t = int(c[7])
                        if t >= desde_ms - 60_000:
                            bn[c[2]].add(t, float(c[3]))
        except (EOFError, OSError):
            pass
    for d in (q, bn):
        for s in d.values():
            s.ordenar()
    for k in tr:
        tr[k].sort()
    return meta, q, tr, bn


def cargar_chainlink(dias):
    cl = collections.defaultdict(Serie)
    for d in dias:
        for suf in (".csv", ".csv.gz"):
            f = PRICES / f"chainlink_{d}{suf}"
            if not f.exists():
                continue
            with (gzip.open(f, "rt") if suf.endswith("gz") else open(f)) as fh:
                for r in csv.DictReader(fh):
                    if r.get("source", "chainlink") != "chainlink":
                        continue
                    t = int(datetime.fromisoformat(r["timestamp_utc"]).timestamp() * 1000)   # RECEPCIÓN
                    cl[r["asset"]].add(t, float(r["price_usd"]))
    for s in cl.values():
        s.ordenar()
    return cl


def refs(dias):
    tw = collections.defaultdict(dict)
    for d in dias:
        for suf in (".csv", ".csv.gz"):
            f = PRICES / f"polybolt_{d}{suf}"
            if f.exists():
                with (gzip.open(f, "rt") if suf.endswith("gz") else open(f)) as fh:
                    for r in csv.DictReader(fh):
                        if r["canal"] == "twap60" and r.get("source", "chainlink") == "chainlink":
                            e = int(r["event_ts_ms"]) // 1000
                            if e % 300 == 0:
                                tw[r["asset"]][e] = float(r["value"])
    return tw


OPCIONALES = ["dist_ref_bps", "z", "fv_yes", "misp_yes", "misp_no", "sigma_bps_s", "cl_ret_5s_bps", "cl_ret_30s_bps",
              "cl_edad_ms", "m5_mid", "m5_vel_1s", "m5_vel_5s", "bn_ret_1s_bps", "bn_ret_5s_bps", "bn_ret_30s_bps",
              "bn_ntr_1s"]


def libro_rasgos(s, T, t, pref, ts):
    out = {}
    i = s.idx(t)
    if i < 0:
        return None
    bid, ask, bsz, asz = s.v[i]
    if bid is None or ask is None:
        return None
    mid = (bid + ask) / 2
    out[f"{pref}_bid"], out[f"{pref}_ask"], out[f"{pref}_bsz"], out[f"{pref}_asz"] = bid, ask, bsz, asz
    out[f"{pref}_spread"] = round(ask - bid, 4)
    out[f"{pref}_mid"] = mid
    out[f"{pref}_micro"] = round((bid * asz + ask * bsz) / (bsz + asz), 4) if bsz + asz > 0 else mid
    out[f"{pref}_imb"] = round((bsz - asz) / (bsz + asz), 4) if bsz + asz > 0 else 0.0
    j = i
    while j > 0 and s.v[j - 1][1] == ask:
        j -= 1
    out[f"{pref}_edad_ask"] = t - s.t[j]
    j = i
    while j > 0 and s.v[j - 1][0] == bid:
        j -= 1
    out[f"{pref}_edad_bid"] = t - s.t[j]
    j = i
    while j > 0 and s.v[j - 1][0] == bid and s.v[j - 1][1] == ask:
        j -= 1
    out[f"{pref}_edad_mid"] = t - s.t[j]
    for w in (1000, 5000):
        i0 = bisect.bisect_left(s.t, t - w)
        out[f"{pref}_cambios_{w // 1000}s"] = i + 1 - i0
        canc = sum(1 for k in range(max(i0, 1), i + 1) if s.v[k][1] == s.v[k - 1][1] and s.v[k][3] < s.v[k - 1][3])
        out[f"{pref}_menos_ask_{w // 1000}s"] = canc
    k1 = bisect.bisect_right(ts, t)
    for w in (1000, 5000, 30000):
        k0 = bisect.bisect_left(ts, t - w)
        out[f"{pref}_ntr_{w // 1000}s"] = k1 - k0
        out[f"{pref}_flujo_{w // 1000}s"] = round(sum(x[2] * x[3] for x in T[k0:k1]), 2)
    out[f"{pref}_desde_trade"] = (t - ts[k1 - 1]) if k1 > 0 else None
    for w in (1000, 5000):
        v0 = s.en(t - w)
        out[f"{pref}_vel_{w // 1000}s"] = None if (not v0 or v0[0] is None or v0[1] is None) else round(mid - (v0[0] + v0[1]) / 2, 4)
    v1, v2 = s.en(t - 1000), s.en(t - 2000)
    if v1 and v2 and None not in (v1[0], v1[1], v2[0], v2[1]):
        m1, m2 = (v1[0] + v1[1]) / 2, (v2[0] + v2[1]) / 2
        out[f"{pref}_acel"] = round((mid - m1) - (m1 - m2), 4)
    else:
        out[f"{pref}_acel"] = None
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-05T16:10")
    ap.add_argument("--out", required=True)
    ap.add_argument("--rejilla", type=int, default=500)
    a = ap.parse_args()
    desde = int(datetime.fromisoformat(a.desde).replace(tzinfo=timezone.utc).timestamp() * 1000)
    meta, q, tr, bn = cargar(desde)
    dias = sorted({datetime.fromtimestamp(desde / 1000 - 86400 * k, timezone.utc).date().isoformat() for k in (0, 1)} |
                  {datetime.now(timezone.utc).date().isoformat()})
    cl = cargar_chainlink(dias)
    tw = refs(dias)
    porm = collections.defaultdict(dict)        # (moneda, marco, mid, cierre) -> {lado: token}
    for tok, (mo, marco, mid, cie, lado) in meta.items():
        porm[(mo, marco, mid, cie)][lado] = tok
    tmax = max(s.t[-1] for s in q.values() if s.t)
    m15 = [(k, v) for k, v in porm.items() if k[1] == "15min" and len(v) == 2 and (k[3] - 900) * 1000 >= desde
           and k[3] * 1000 < tmax]
    des = desenlaces({k[2] for k, _ in m15})
    m5 = collections.defaultdict(list)           # moneda -> [(ini, fin, token_yes)]
    for k, v in porm.items():
        if k[1] == "5min" and "YES" in v:
            m5[k[0]].append((k[3] - 300, k[3], v["YES"]))
    campos, fo, w = None, open(a.out, "w", newline=""), None
    n = 0
    for (mo, _, mid, cie), toks in sorted(m15, key=lambda x: x[0][3]):
        if mid not in des:
            continue
        sy, sn = q.get(toks["YES"]), q.get(toks["NO"])
        if not sy or not sn or len(sy.t) < 20:
            continue
        ref = tw.get(mo, {}).get(cie - 900)
        cls = cl.get(mo)
        bns = bn.get(SIM[mo])
        Ty, Tn = tr.get(toks["YES"], []), tr.get(toks["NO"], [])
        tsy, tsn = [x[0] for x in Ty], [x[0] for x in Tn]
        cand5 = [x for x in m5.get(mo, []) if x[1] > cie - 900 and x[0] < cie]
        for t in range((cie - 900) * 1000 + 5000, cie * 1000 - 5000, a.rejilla):
            fy = libro_rasgos(sy, Ty, t, "y", tsy)
            fn = libro_rasgos(sn, Tn, t, "n", tsn)
            if not fy or not fn:
                continue
            f = {"moneda": mo, "market": mid, "cierre": cie, "t": t, "desenlace": des[mid],
                 "dia": datetime.fromtimestamp(t / 1000, timezone.utc).date().isoformat(),
                 "hora": datetime.fromtimestamp(t / 1000, timezone.utc).hour,
                 "t_desde_inicio_s": round(t / 1000 - (cie - 900), 1), "t_hasta_cierre_s": round(cie - t / 1000, 1)}
            f.update(fy)
            f.update(fn)
            f["suma_asks"] = round(fy["y_ask"] + fn["n_ask"], 4)
            # referencia / fair value
            if cls and ref:
                S = cls.en(t)
                i = cls.idx(t)
                if S is not None:
                    f["dist_ref_bps"] = round((S / ref - 1) * 1e4, 3)
                    i0 = bisect.bisect_left(cls.t, t - 300_000)
                    pr = cls.v[i0:i + 1]
                    rets = [math.log(pr[k + 1] / pr[k]) for k in range(len(pr) - 1) if pr[k] > 0 and pr[k + 1] != pr[k]]
                    dur = max(1.0, (cls.t[i] - cls.t[i0]) / 1000)
                    if len(rets) >= 20:
                        sig_s = math.sqrt(sum(r * r for r in rets) / dur)        # varianza por segundo
                        Tr = max(1.0, cie - t / 1000)
                        z = math.log(S / ref) / (sig_s * math.sqrt(Tr)) if sig_s > 0 else 0.0
                        f["z"] = round(z, 4)
                        f["fv_yes"] = round(phi(z), 4)
                        f["misp_yes"] = round(f["fv_yes"] - fy["y_ask"], 4)
                        f["misp_no"] = round(1 - f["fv_yes"] - fn["n_ask"], 4)
                        f["sigma_bps_s"] = round(sig_s * 1e4, 4)
                    for wv in (5000, 30000):
                        S0 = cls.en(t - wv)
                        f[f"cl_ret_{wv // 1000}s_bps"] = None if not S0 else round((S / S0 - 1) * 1e4, 3)
                    f["cl_edad_ms"] = t - cls.t[i]
            # 5m concurrente
            act = [x for x in cand5 if x[0] * 1000 <= t < x[1] * 1000]
            if act and q.get(act[0][2]):
                s5 = q[act[0][2]]
                v = s5.en(t)
                if v and v[0] is not None and v[1] is not None:
                    m5_ = (v[0] + v[1]) / 2
                    f["m5_mid"] = m5_
                    for wv in (1000, 5000):
                        v0 = s5.en(t - wv)
                        f[f"m5_vel_{wv // 1000}s"] = None if (not v0 or v0[0] is None or v0[1] is None) else round(m5_ - (v0[0] + v0[1]) / 2, 4)
            # Binance
            if bns and bns.t:
                i = bns.idx(t)
                if i >= 0:
                    for wv in (1000, 5000, 30000):
                        j = bns.idx(t - wv)
                        f[f"bn_ret_{wv // 1000}s_bps"] = None if j < 0 else round((bns.v[i] / bns.v[j] - 1) * 1e4, 3)
                    f["bn_ntr_1s"] = i + 1 - bisect.bisect_left(bns.t, t - 1000)
            # objetivos (FUTURO)
            for h in HMID:
                v = sy.en(t + h)
                f[f"Y_mid_{h}"] = None if (not v or v[0] is None or v[1] is None) else (v[0] + v[1]) / 2
            for L in LAT:
                vy, vn = sy.en(t + L), sn.en(t + L)
                f[f"Y_askY_{L}"] = vy[1] if vy else None
                f[f"Y_askYsz_{L}"] = vy[3] if vy else None
                f[f"Y_askN_{L}"] = vn[1] if vn else None
                f[f"Y_askNsz_{L}"] = vn[3] if vn else None
            for H in HRT:
                vy, vn = sy.en(t + 215 + H), sn.en(t + 215 + H)
                f[f"Y_bidY_{H}"] = vy[0] if vy else None
                f[f"Y_bidN_{H}"] = vn[0] if vn else None
            if w is None:
                campos = list(f.keys()) + [k for k in OPCIONALES if k not in f]
                w = csv.DictWriter(fo, fieldnames=campos, extrasaction="ignore")
                w.writeheader()
            w.writerow(f)
            n += 1
    fo.close()
    print(f"mercados 15m: {len(m15)} | con desenlace: {sum(1 for k, _ in m15 if k[2] in des)} | filas: {n} -> {a.out}")


if __name__ == "__main__":
    main()
