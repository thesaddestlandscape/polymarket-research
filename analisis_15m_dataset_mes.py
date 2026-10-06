#!/usr/bin/env python3
"""analisis_15m_dataset_mes.py -- dataset del 15m para TODO el último mes (06-Oct, Javi: "coge los datos de un mes entero,
como con B1"). Complementa al dataset ms (analisis_15m_dataset_maestro.py, ~20 h, ejecución exacta a +215 ms).

Fuentes (día a día, sin cargar el mes entero en memoria):
  libro_ambos_lados_D (datalogs): FOTOS del libro de ambos lados (ask/bid YES y NO, sin tamaños) de cada mercado, cada
    ~45 s por mercado de 15m. Es el ask REAL de la foto, no un print.
  polymarket_activity_D (firehose): operaciones con lado/resultado/tamaño y hora de RECEPCIÓN -> flujo agresor previo.
  chainlink_D (ticks RTDS source=chainlink, por hora de recepción) -> subyacente, z y fair value; referencia oficial de
    apertura = TWAP60 de PolyBolt (desde 24-Sep) o reconstruido de RTDS [e-62, e-3] (validado 0,005 bps de mediana).
  Desenlace oficial por id de mercado (gamma closed=true).
Unidad = una FOTO de un mercado 15m con su ventana ya abierta (t >= inicio + 2 s). Rasgos en t (solo datos <= t):
  precios de la foto, spread, suma de asks, velocidad del mid vs la foto anterior (~45 s) y la de hace ~90 s; tiempo
  desde inicio / hasta cierre; Chainlink: distancia a la referencia, σ de 300 s, z, FV, mispricing vs ask, retornos 30/
  60/300 s, edad del último tick; flujo del firehose 10/60/300 s (USD comprado de YES menos de NO; nº de operaciones);
  5m concurrente: mid de su última foto y su variación.
Ejecución (dos cotas, nunca una sola): OPTIMISTA = ask de la propia foto (como si llegásemos al instante);
  PESIMISTA = ask de la SIGUIENTE foto del mismo mercado (~45 s después). PnL a resolución con comisión 0,07·p·(1-p).
  Ida y vuelta: vender al bid de la primera foto >= t+60 s y >= t+300 s.
Salida: CSV por día en --dir (m15mes_D.csv). Uso: --desde 2026-09-16 --hasta 2026-10-05 --dir <carpeta>
"""
import argparse
import bisect
import collections
import csv
import gzip
import math
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_b1_compradores_mes import refs_dia, twap_rtds  # noqa: E402

csv.field_size_limit(10 ** 7)
DL = Path("/root/polymarket-research-datalogs")
PR = Path(__file__).resolve().parent / "data" / "prices"


def abrir(p):
    return gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")


def fich(base, nombre, d):
    for suf in (".csv", ".csv.gz"):
        f = base / f"{nombre}_{d}{suf}"
        if f.exists():
            return f
    return None


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def ts_ms(s):
    return int(datetime.fromisoformat(s).timestamp() * 1000)


def procesar_dia(d, PB, RT, out_dir):
    fl = fich(DL, "libro_ambos_lados", d)
    if not fl:
        print(f"  {d}: sin libro_ambos_lados")
        return 0
    fotos = collections.defaultdict(list)   # market_id -> [(t, ask_y, ask_n, bid_y, bid_n)]
    info = {}
    f5 = collections.defaultdict(list)       # (moneda, fin_s del 5m) -> [(t, mid5)]
    g = lambda x: float(x) if x not in ("", None) else None
    for r in csv.DictReader(abrir(fl)):
        if r["marco"] not in ("15min", "5min"):
            continue
        try:
            t = ts_ms(r["timestamp_utc"])
            fin = int(datetime.fromisoformat(r["end_date"]).timestamp())
        except (ValueError, KeyError):
            continue
        ay, an, by, bn = g(r["ask_yes"]), g(r["ask_no"]), g(r["bid_yes"]), g(r["bid_no"])
        if r["marco"] == "15min":
            fotos[r["market_id"]].append((t, ay, an, by, bn))
            info[r["market_id"]] = (r["activo"], fin, r["condition_id"])
        elif by is not None and ay is not None:
            f5[(r["activo"], fin)].append((t, (by + ay) / 2))
    for v in list(fotos.values()) + list(f5.values()):
        v.sort()
    # firehose: flujo por condition_id
    flujo = collections.defaultdict(list)    # condition_id -> [(t, usd firmado (+YES/Up), n)]
    conds = {v[2] for v in info.values()}
    ff = fich(DL, "polymarket_activity", d)
    if ff:
        try:
            for r in csv.DictReader(abrir(ff)):
                if r["condition_id"] not in conds or r["side"] != "BUY":
                    continue
                try:
                    t = ts_ms(r["timestamp_utc"])
                    usd = float(r["usd_value"] or 0)
                except ValueError:
                    continue
                flujo[r["condition_id"]].append((t, usd if r["outcome"] in ("Up", "Yes") else -usd))
        except (EOFError, OSError):
            pass
    for v in flujo.values():
        v.sort()
    # Chainlink del día (y del anterior por la cola)
    cl = collections.defaultdict(lambda: ([], []))
    for dd in ((date.fromisoformat(d) - timedelta(days=1)).isoformat(), d):
        fc = fich(PR, "chainlink", dd)
        if not fc:
            continue
        for r in csv.DictReader(abrir(fc)):
            if r.get("source", "chainlink") != "chainlink":
                continue
            try:
                c = cl[r["asset"]]
                c[0].append(ts_ms(r["timestamp_utc"]))
                c[1].append(float(r["price_usd"]))
            except (ValueError, KeyError):
                continue
    for k in list(cl):
        o = sorted(range(len(cl[k][0])), key=cl[k][0].__getitem__)
        cl[k] = ([cl[k][0][i] for i in o], [cl[k][1][i] for i in o])
    des = desenlaces(set(fotos))
    out = out_dir / f"m15mes_{d}.csv"
    campos = None
    n = 0
    with open(out, "w", newline="") as fo:
        w = None
        for mid, fs in fotos.items():
            mo, fin, cond = info[mid]
            if mid not in des:
                continue
            ini = fin - 900
            ref = PB.get((mo, ini)) or twap_rtds(RT, mo, ini)
            if ref is None:
                continue
            ts_f = [x[0] for x in fs]
            c = cl.get(mo)
            fl_ = flujo.get(cond, [])
            tfl = [x[0] for x in fl_]
            for i, (t, ay, an, by, bn) in enumerate(fs):
                if t < ini * 1000 + 2000 or t >= fin * 1000:
                    continue
                if ay is None or an is None or by is None or bn is None:
                    continue
                row = {"dia": d, "moneda": mo, "market": mid, "cierre": fin, "t": t, "desenlace": des[mid],
                       "hora": datetime.fromtimestamp(t / 1000, timezone.utc).hour,
                       "t_desde_inicio_s": round(t / 1000 - ini, 1), "t_hasta_cierre_s": round(fin - t / 1000, 1),
                       "ask_y": ay, "ask_n": an, "bid_y": by, "bid_n": bn, "mid": (ay + by) / 2,
                       "spread_y": round(ay - by, 4), "suma_asks": round(ay + an, 4)}
                for k, lag in ((1, "vel1"), (2, "vel2")):
                    j = i - k
                    row[lag] = None if j < 0 or fs[j][1] is None or fs[j][3] is None else round(row["mid"] - (fs[j][1] + fs[j][3]) / 2, 4)
                if c and c[0]:
                    k = bisect.bisect_right(c[0], t) - 1
                    if k >= 0:
                        S = c[1][k]
                        row["cl_edad_ms"] = t - c[0][k]
                        row["dist_ref_bps"] = round((S / ref - 1) * 1e4, 3)
                        k0 = bisect.bisect_left(c[0], t - 300_000)
                        pr = c[1][k0:k + 1]
                        rets = [math.log(pr[q + 1] / pr[q]) for q in range(len(pr) - 1) if pr[q] > 0 and pr[q + 1] != pr[q]]
                        dur = max(1.0, (c[0][k] - c[0][k0]) / 1000)
                        if len(rets) >= 20:
                            sg = math.sqrt(sum(x * x for x in rets) / dur)
                            Tr = max(1.0, fin - t / 1000)
                            z = math.log(S / ref) / (sg * math.sqrt(Tr)) if sg > 0 else 0.0
                            row["z"], row["fv_yes"], row["sigma_bps_s"] = round(z, 4), round(phi(z), 4), round(sg * 1e4, 4)
                            row["misp_yes"] = round(row["fv_yes"] - ay, 4)
                            row["misp_no"] = round(1 - row["fv_yes"] - an, 4)
                        for wv in (30, 60, 300):
                            k2 = bisect.bisect_right(c[0], t - wv * 1000) - 1
                            row[f"cl_ret_{wv}s_bps"] = None if k2 < 0 else round((S / c[1][k2] - 1) * 1e4, 3)
                k1 = bisect.bisect_right(tfl, t)
                for wv in (10, 60, 300):
                    k0 = bisect.bisect_left(tfl, t - wv * 1000)
                    row[f"flujo_{wv}s"] = round(sum(x[1] for x in fl_[k0:k1]), 2)
                    row[f"ntr_{wv}s"] = k1 - k0
                fin5 = (t // 300_000 + 1) * 300                  # el 5m activo en t cierra en el siguiente múltiplo
                s5 = f5.get((mo, fin5), [])
                k5 = bisect.bisect_right(s5, (t, 9.9)) - 1
                if k5 >= 0:
                    row["m5_mid"] = s5[k5][1]
                    k6 = bisect.bisect_right(s5, (t - 40_000, 9.9)) - 1
                    row["m5_vel"] = round(s5[k5][1] - s5[k6][1], 4) if k6 >= 0 else None
                # ejecución: optimista (propia foto) y pesimista (siguiente foto)
                nx = fs[i + 1] if i + 1 < len(fs) and fs[i + 1][0] < fin * 1000 else None
                row["ask_y_sig"] = nx[1] if nx else None
                row["ask_n_sig"] = nx[2] if nx else None
                row["seg_hasta_sig"] = round((nx[0] - t) / 1000, 1) if nx else None
                for H, nom in ((60, "60"), (300, "300")):
                    j = bisect.bisect_left(ts_f, t + H * 1000)
                    v = fs[j] if j < len(fs) and fs[j][0] < fin * 1000 else None
                    row[f"bid_y_{nom}"] = v[3] if v else None
                    row[f"bid_n_{nom}"] = v[4] if v else None
                if w is None:
                    campos = list(row.keys()) + [k for k in ("cl_edad_ms", "dist_ref_bps", "z", "fv_yes", "sigma_bps_s",
                                                             "misp_yes", "misp_no", "cl_ret_30s_bps", "cl_ret_60s_bps",
                                                             "cl_ret_300s_bps", "m5_mid", "m5_vel") if k not in row]
                    w = csv.DictWriter(fo, fieldnames=campos, extrasaction="ignore")
                    w.writeheader()
                w.writerow(row)
                n += 1
    print(f"  {d}: mercados 15m {len(fotos)}, con desenlace {sum(1 for m in fotos if m in des)}, filas {n}", flush=True)
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-09-16")
    ap.add_argument("--hasta", default="2026-10-05")
    ap.add_argument("--dir", required=True)
    a = ap.parse_args()
    d0, d1 = date.fromisoformat(a.desde), date.fromisoformat(a.hasta)
    dias = [(d0 + timedelta(days=i)).isoformat() for i in range((d1 - d0).days + 1)]
    PB, RT = {}, collections.defaultdict(lambda: [0.0, 0])
    for d in [(d0 - timedelta(days=1)).isoformat()] + dias:
        refs_dia(d, PB, RT)
    out = Path(a.dir)
    out.mkdir(parents=True, exist_ok=True)
    tot = sum(procesar_dia(d, PB, RT, out) for d in dias)
    print(f"total filas {tot} -> {out}")


if __name__ == "__main__":
    main()
