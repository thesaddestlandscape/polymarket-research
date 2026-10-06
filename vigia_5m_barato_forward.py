#!/usr/bin/env python3
"""vigia_5m_barato_forward.py -- VIGÍA FORWARD, SOLO OBSERVACIÓN / DRY-RUN (06-Oct, Javi: "construir un vigía forward
de alpha para la pata 5m"). NUNCA firma, envía ni modifica nada: lee el registro ms y escribe CSV/JSON en datalogs.

HIPÓTESIS CONGELADA (cambiarla = nueva VERSION + nuevo periodo fuera de muestra; ver CONFIG y su hash):
  Par de cada cierre C: mercado 15m que cierra en C y mercado 5m que cierra en C (último tramo del 15m). Referencias de
  apertura = TWAP60 oficial (PolyBolt canal twap60 = media RTDS [e-62, e-3]) en C-900 (15m) y C-300 (5m); |gap|>=1 bps.
  Lado implicado s: si ref15 > ref5, "Up en 15m" implica "Up en 5m" => P(Up5) >= P(Up15) => s = Up; si no, s = Down
  (Down15 implica Down5). El bid del 15m en el lado s es una cota inferior de mercado de P(s en 5m).
  margen_neto = bid15(s) - ask5(s) - fee(ask5(s)), fee(p) = 0,07·p·(1-p) por acción (comisión de tomador cripto),
  redondeado a 4 decimales. SEÑAL si margen_neto >= 0,05, con t >= (C-300) s + 1,5 s (referencia ya publicada) y
  t < C - 10 s.
  EVENTO: primer instante (hora de RECEPCIÓN de la fila q que lo crea) con SEÑAL; termina cuando la señal falta >= 2 s
  seguidos (re-armado); el siguiente es otro event_id. Métrica OFICIAL = PRIMER evento de cada (cierre, moneda).
  EJECUCIÓN VIRTUAL: orden de compra a precio límite p_lim = mayor precio de rejilla (0,01) con
  bid15(t0) - p - fee(p) >= 0,05; llega a t0 + L (oficial L = 215 ms; diagnóstico 150..300 y jitter). Se llena contra
  el NIVEL 1 del libro del 5m a t0+L (último cambio con recepción <= t0+L): si ask <= p_lim, acciones = min(objetivo,
  tamaño del nivel 1) al precio de ese ask. El registro solo graba el nivel 1: lo que no cabe en él es NO LLENADO
  (nunca se supone un precio peor ni mejor). STAKE oficial 2 EUR -> acciones objetivo = max(5, 2/ask0).
  PnL = acciones_llenas x (pago oficial - precio - fee(precio)). Desenlace OFICIAL por id de mercado (gamma closed).
  Sin datos para reconstruir el ask a t0+L -> clase UNKNOWN (ni gana ni pierde).
BENCHMARKS (misma maquinaria): B2 = regla espejo en el 15m (comprar el 15m del lado contrario a s cuando
  bid5 - ask15 - fee >= 0,05); B3 = comprar el 5m del lado s cada 10 s sin umbral; B4 = control emparejado: mismas
  muestras de B3 con margen_neto < 0,01, misma moneda y tramo de precio de 5c, otra ventana (en el informe).
Subcomandos: procesar --dia YYYY-MM-DD (eventos del día UTC) | informe [--telegram]. Cron diario (crontab).
Salidas: /root/polymarket-research-datalogs/vigia_5m_barato/ (eventos_D.csv, controles_D.csv, calidad_D.csv,
  manifiesto.json con hash de config y código, informe.json, informe.txt).
"""
import argparse
import bisect
import collections
import csv
import glob
import gzip
import hashlib
import json
import math
import random
import statistics as st
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DL = Path("/root/polymarket-research-datalogs")
SALIDA = DL / "vigia_5m_barato"
PRICES = REPO / "data" / "prices"

CONFIG = {
    "version": 1,
    "umbral_margen_neto": 0.05,
    "fee_tomador": 0.07,
    "stake_eur": 2.0,
    "min_acciones": 5.0,
    "latencia_oficial_ms": 215,
    "latencias_diagnostico_ms": [150, 175, 200, 215, 225, 250, 275, 300],
    # jitter de la cadena real: POST /order medido 05-Oct (8 FOK, incluye 150 ms del exchange): mediana 226, p95 702,
    # máx 1.040 + ~25 ms de WS/decisión. Cuantiles (ms desde t0) usados para muestrear la latencia de cada evento.
    "jitter_cuantiles_ms": {"p50": 215, "p75": 250, "p90": 350, "p95": 700, "p99": 1000},
    "rearme_ms": 2000,
    "ref_conocible_ms": 1500,
    "fin_margen_s": 10,
    "gap_min_bps": 1.0,
    "control_cada_ms": 10000,
    "congelado_utc": "2026-10-06T12:00:00+00:00",
}
TRAMOS_PRECIO = [(0.0, 0.1), (0.1, 0.2), (0.2, 0.3), (0.3, 0.4), (0.4, 0.5), (0.5, 0.6), (0.6, 0.7), (0.7, 0.8),
                 (0.8, 0.9), (0.9, 1.0)]
MARGENES_DESC = [0.01, 0.02, 0.03, 0.04, 0.05, 0.075, 0.10]
STAKES_CAP = [0.5, 1, 2, 5, 10, 25, 50, 100]
SIM = {"BTC": "BTCUSDT", "ETH": "ETHUSDT", "SOL": "SOLUSDT", "XRP": "XRPUSDT", "DOGE": "DOGEUSDT", "BNB": "BNBUSDT"}


def fee(p):
    return CONFIG["fee_tomador"] * p * (1 - p)


def margen(bid_otro, ask):
    return round(bid_otro - ask - fee(ask), 4)


def p_limite(bid_otro):
    """Mayor precio de rejilla 0,01 que aún cumple la regla."""
    p = math.floor(bid_otro * 100) / 100
    while p > 0 and margen(bid_otro, p) < CONFIG["umbral_margen_neto"]:
        p = round(p - 0.01, 2)
    return p if p > 0 else None


def hash_config():
    h = hashlib.sha256(json.dumps(CONFIG, sort_keys=True).encode())
    h.update(Path(__file__).read_bytes())
    return h.hexdigest()[:16]


def manifiesto(dia):
    SALIDA.mkdir(parents=True, exist_ok=True)
    f = SALIDA / "manifiesto.json"
    m = json.loads(f.read_text()) if f.exists() else {"versiones": {}}
    hc = hash_config()
    v = m["versiones"].setdefault(str(CONFIG["version"]), {"hash": hc, "inicio_utc": datetime.now(timezone.utc).isoformat(),
                                                             "config": CONFIG, "dias": []})
    if v["hash"] != hc:
        raise SystemExit(f"🛑 el código/config de la versión {CONFIG['version']} cambió (hash {v['hash']} -> {hc}). "
                         f"Regla congelada: subir CONFIG['version'] y documentar qué queda invalidado.")
    if dia not in v["dias"]:
        v["dias"].append(dia)
    f.write_text(json.dumps(m, indent=1))


def twap_refs(dias):
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


class Libro:
    """Serie del nivel 1 de un token con hora de recepción: (t, bid, ask, bid_sz, ask_sz, t_exch)."""
    def __init__(self):
        self.t, self.v = [], []

    def add(self, t, fila):
        self.t.append(t)
        self.v.append(fila)

    def en(self, t):
        i = bisect.bisect_right(self.t, t) - 1
        return (self.t[i], self.v[i]) if i >= 0 else (None, None)


def rasgos_libro(L, T, t, pref):
    """Microestructura de un token en t (solo datos con recepción <= t)."""
    f = {}
    tq, q = L.en(t)
    if q is None:
        return {f"{pref}_{k}": None for k in ("bid", "ask", "bid_sz", "ask_sz", "spread", "mid", "microprecio",
                                              "edad_ask_ms", "edad_bid_ms", "cambios_1s", "cancel_1s", "trades_1s",
                                              "vol_firmado_1s", "ultimo_trade_ms", "vel_mid_1s", "acel_mid")}
    bid, ask, bsz, asz = q[0], q[1], q[2], q[3]
    f[f"{pref}_bid"], f[f"{pref}_ask"], f[f"{pref}_bid_sz"], f[f"{pref}_ask_sz"] = bid, ask, bsz, asz
    f[f"{pref}_spread"] = None if (bid is None or ask is None) else round(ask - bid, 4)
    mid = None if (bid is None or ask is None) else (bid + ask) / 2
    f[f"{pref}_mid"] = mid
    f[f"{pref}_microprecio"] = None if (mid is None or not (bsz + asz)) else round((bid * asz + ask * bsz) / (bsz + asz), 4)
    i = bisect.bisect_right(L.t, t) - 1
    j = i
    while j > 0 and L.v[j - 1][1] == ask and L.v[j - 1][3] == asz:
        j -= 1
    f[f"{pref}_edad_ask_ms"] = t - L.t[j]
    j = i
    while j > 0 and L.v[j - 1][0] == bid:
        j -= 1
    f[f"{pref}_edad_bid_ms"] = t - L.t[j]
    i0 = bisect.bisect_left(L.t, t - 1000)
    f[f"{pref}_cambios_1s"] = i + 1 - i0
    canc = 0
    for k in range(max(i0, 1), i + 1):
        if L.v[k][1] == L.v[k - 1][1] and L.v[k][3] < L.v[k - 1][3]:
            canc += 1           # menos tamaño al mismo ask (cancelación o consumo; se separa con trades abajo)
    tt = [x for x in T if t - 1000 <= x[0] <= t]
    f[f"{pref}_trades_1s"] = len(tt)
    canc_sin_trade = canc - min(canc, len(tt))
    f[f"{pref}_cancel_1s"] = canc_sin_trade
    f[f"{pref}_vol_firmado_1s"] = round(sum(x[3] if x[2] == "BUY" else -x[3] for x in tt), 2)
    k = bisect.bisect_right([x[0] for x in T], t) - 1
    f[f"{pref}_ultimo_trade_ms"] = (t - T[k][0]) if k >= 0 else None
    _, q1 = L.en(t - 1000)
    _, q2 = L.en(t - 2000)
    m1 = None if (not q1 or q1[0] is None or q1[1] is None) else (q1[0] + q1[1]) / 2
    m2 = None if (not q2 or q2[0] is None or q2[1] is None) else (q2[0] + q2[1]) / 2
    f[f"{pref}_vel_mid_1s"] = None if (mid is None or m1 is None) else round(mid - m1, 4)
    f[f"{pref}_acel_mid"] = None if (mid is None or m1 is None or m2 is None) else round((mid - m1) - (m1 - m2), 4)
    return f


def ejecutar(L, T, t0, lat, p_lim, acc_obj):
    """Ejecución virtual a t0+lat contra el nivel 1 del 5m. -> dict con precio, acciones, clase causal."""
    te = t0 + lat
    tq, q = L.en(te)
    if q is None or tq is None or te - tq > 60_000:
        return {"clase": "UNKNOWN", "precio": None, "acciones": 0.0, "disp": None}
    ask, asz = q[1], q[3]
    _, q0 = L.en(t0)
    ask0 = q0[1] if q0 else None
    if ask is not None and p_lim is not None and ask <= p_lim + 1e-9:
        acc = min(acc_obj, asz)
        clase = "A_sigue_barato" if ask0 is not None and ask <= ask0 + 1e-9 else "D_otro_nivel_barato"
        if acc < acc_obj:
            clase += "_parcial"
        return {"clase": clase, "precio": ask, "acciones": acc, "disp": asz}
    # no ejecutable: ¿consumido o cancelado el nivel original?
    consumido = any(t0 <= x[0] <= te and ask0 is not None and abs(x[1] - ask0) < 1e-9 for x in T)
    return {"clase": "C_consumido" if consumido else "B_cancelado_o_repreciado", "precio": ask, "acciones": 0.0,
            "disp": asz}


def procesar(dia):
    manifiesto(dia)
    d = date.fromisoformat(dia)
    t_lo = int(datetime(d.year, d.month, d.day, tzinfo=timezone.utc).timestamp())
    t_hi = t_lo + 86400
    fich = sorted((f for f in glob.glob(str(DL / "maker_ms_*.csv.gz"))
                   if Path(f).name[9:19] in (dia, (d + timedelta(days=1)).isoformat())),
                  key=lambda f: Path(f).stat().st_mtime)
    tw = twap_refs([(d - timedelta(days=1)).isoformat(), dia])
    meta, idx = {}, collections.defaultdict(dict)
    libros, trades = collections.defaultdict(Libro), collections.defaultdict(list)
    binance = collections.defaultdict(list)
    calidad = collections.Counter()
    ult_t = {}
    for f in fich:
        try:
            for ln in gzip.open(f, "rt"):
                c = ln.rstrip("\n").split(",")
                tp = c[0]
                if tp == "k":
                    if c[4] in ("5min", "15min"):
                        cie = int(datetime.fromisoformat(c[6]).timestamp())
                        meta[c[2]] = (c[3], c[4], c[5], cie, c[7])
                        idx[(c[3], cie)][(c[4], c[7])] = c[2]
                elif tp == "q":
                    m = meta.get(c[2])
                    if not m or not (t_lo <= m[3] <= t_hi + 900) or (m[1] == "5min" and m[3] % 900):
                        continue                          # solo 15m y los 5m que cierran con un 15m
                    try:
                        tr = int(c[7]) if len(c) > 7 and c[7] else int(c[1])
                        if not ((m[3] - 300) * 1000 - 5000 <= tr <= m[3] * 1000):
                            continue                      # solo el último tramo de 5 min (+5 s de historia)
                        g = lambda x: None if x in ("", "None") else float(x)
                        fila = (g(c[3]), g(c[4]), g(c[5]) or 0.0, g(c[6]) or 0.0, int(c[1]))
                    except (ValueError, IndexError):
                        calidad["q_ilegible"] += 1
                        continue
                    if (fila[0] is not None and not 0 < fila[0] < 1) or (fila[1] is not None and not 0 < fila[1] < 1):
                        calidad["precio_imposible"] += 1
                        continue
                    if fila[2] < 0 or fila[3] < 0:
                        calidad["tamano_negativo"] += 1
                        continue
                    if fila[0] is not None and fila[1] is not None:
                        if fila[0] > fila[1]:
                            calidad["libro_cruzado_bid>ask"] += 1
                        elif fila[0] == fila[1]:
                            calidad["libro_bloqueado_bid=ask(transitorio)"] += 1
                    if c[2] in ult_t and tr < ult_t[c[2]]:
                        calidad["recepcion_no_monotona"] += 1
                    ult_t[c[2]] = max(tr, ult_t.get(c[2], 0))
                    libros[c[2]].add(tr, fila)
                elif tp == "t":
                    m = meta.get(c[2])
                    if not m or not (t_lo <= m[3] <= t_hi + 900) or (m[1] == "5min" and m[3] % 900):
                        continue
                    try:
                        tr = int(c[6]) if len(c) > 6 and c[6] else int(c[1])
                        if not ((m[3] - 300) * 1000 - 5000 <= tr <= m[3] * 1000):
                            continue
                        trades[c[2]].append((tr, float(c[3]), c[4], float(c[5])))
                    except (ValueError, IndexError):
                        calidad["t_ilegible"] += 1
                elif tp == "x":
                    try:
                        binance[c[2]].append((int(c[7]), float(c[3]), float(c[4])))
                    except (ValueError, IndexError):
                        calidad["x_ilegible"] += 1
        except (EOFError, OSError) as e:
            calidad[f"fichero_truncado:{Path(f).name}"] += 1
    for L in libros.values():
        o = sorted(range(len(L.t)), key=L.t.__getitem__)
        L.t = [L.t[i] for i in o]
        L.v = [L.v[i] for i in o]
    for k in trades:
        trades[k].sort(key=lambda x: x[0])
    for k in binance:
        binance[k].sort()
    eventos, controles = [], []
    rng = random.Random(int(t_lo))
    q_ = CONFIG["jitter_cuantiles_ms"]
    jit = [q_["p50"]] * 50 + [q_["p75"]] * 25 + [q_["p90"]] * 15 + [q_["p95"]] * 5 + [q_["p99"]] * 5

    def bin_estado(mo, t):
        v = binance.get(SIM.get(mo), [])
        ts = [x[0] for x in v]
        i = bisect.bisect_right(ts, t) - 1
        if i < 0:
            return {"bin_precio": None, "bin_ret_1s_bps": None, "bin_ret_5s_bps": None, "bin_trades_1s": 0,
                    "bin_ms_desde_ultimo": None}
        def ret(w):
            j = bisect.bisect_right(ts, t - w) - 1
            return None if j < 0 else round((v[i][1] / v[j][1] - 1) * 1e4, 3)
        return {"bin_precio": v[i][1], "bin_ret_1s_bps": ret(1000), "bin_ret_5s_bps": ret(5000),
                "bin_trades_1s": i + 1 - bisect.bisect_left(ts, t - 1000), "bin_ms_desde_ultimo": t - v[i][0]}

    n_pares = 0
    for (mo, cie), toks in idx.items():
        if not (t_lo < cie <= t_hi):
            continue
        need = [("5min", "YES"), ("5min", "NO"), ("15min", "YES"), ("15min", "NO")]
        if not all(x in toks for x in need):
            calidad["par_incompleto"] += 1
            continue
        r15, r5 = tw.get(mo, {}).get(cie - 900), tw.get(mo, {}).get(cie - 300)
        if r15 is None or r5 is None:
            calidad["par_sin_ref"] += 1
            continue
        gap = (r5 / r15 - 1) * 1e4
        if abs(gap) < CONFIG["gap_min_bps"]:
            calidad["par_gap<min"] += 1
            continue
        n_pares += 1
        s = "YES" if r15 > r5 else "NO"           # lado implicado (YES = Up)
        o = "NO" if s == "YES" else "YES"
        for regla, tok_c, tok_o, marco_c in (("B1_5m", toks[("5min", s)], toks[("15min", s)], "5min"),
                                             ("B2_15m", toks[("15min", o)], toks[("5min", o)], "15min")):
            Lc, Lo = libros.get(tok_c), libros.get(tok_o)
            if not Lc or not Lo or not Lc.t or not Lo.t:
                calidad[f"{regla}_sin_libro"] += 1
                continue
            t_ini = (cie - 300) * 1000 + CONFIG["ref_conocible_ms"]
            t_fin = (cie - CONFIG["fin_margen_s"]) * 1000
            instantes = sorted({t for t in Lc.t + Lo.t if t_ini <= t < t_fin})
            # huecos de datos en la ventana
            for L_, nom in ((Lc, "compra"), (Lo, "otro")):
                ts_ = [t for t in L_.t if t_ini <= t < t_fin]
                if ts_ and max(b - a for a, b in zip([t_ini] + ts_, ts_ + [t_fin])) > 60_000:
                    calidad[f"hueco_>60s_{nom}"] += 1
            n_ev, activo, ult_senal = 0, False, None
            for t in instantes:
                _, qc = Lc.en(t)
                _, qo = Lo.en(t)
                senal = (qc and qo and qc[1] is not None and qo[0] is not None and
                         margen(qo[0], qc[1]) >= CONFIG["umbral_margen_neto"])
                if senal:
                    ult_senal = t
                    if activo:
                        continue
                    activo = True
                    n_ev += 1
                    ask0, bid_o = qc[1], qo[0]
                    plim = p_limite(bid_o)
                    acc_obj = max(CONFIG["min_acciones"], CONFIG["stake_eur"] / ask0)
                    fila = {"event_id": f"{regla}_{mo}_{cie}_{n_ev}", "regla": regla, "es_primero": int(n_ev == 1),
                            "moneda": mo, "cierre": cie, "marco_compra": marco_c, "lado": "Up" if (s if regla == "B1_5m" else o) == "YES" else "Down",
                            "market_compra": meta[tok_c][2], "market_otro": meta[tok_o][2],
                            "ref15": r15, "ref5": r5, "gap_bps": round(gap, 3),
                            "t_deteccion": t, "resto_s": round(cie - t / 1000, 2),
                            "pct_contrato_5m": round(1 - (cie - t / 1000) / 300, 3),
                            "ask_compra_t0": ask0, "bid_otro_t0": bid_o,
                            "margen_bruto": round(bid_o - ask0, 4), "margen_neto": margen(bid_o, ask0),
                            "dist_a_1": round(1 - ask0, 4), "p_limite": plim, "acciones_objetivo": round(acc_obj, 3)}
                    fila.update(rasgos_libro(Lc, trades.get(tok_c, []), t, "c"))
                    fila.update(rasgos_libro(Lo, trades.get(tok_o, []), t, "o"))
                    fila.update(bin_estado(mo, t))
                    for lat in CONFIG["latencias_diagnostico_ms"]:
                        ex = ejecutar(Lc, trades.get(tok_c, []), t, lat, plim, acc_obj)
                        fila[f"L{lat}_clase"], fila[f"L{lat}_precio"] = ex["clase"], ex["precio"]
                        fila[f"L{lat}_acciones"], fila[f"L{lat}_disp_nivel1"] = round(ex["acciones"], 3), ex["disp"]
                    lj = rng.choice(jit)
                    ex = ejecutar(Lc, trades.get(tok_c, []), t, lj, plim, acc_obj)
                    fila["jitter_ms"], fila["jitter_clase"], fila["jitter_precio"] = lj, ex["clase"], ex["precio"]
                    fila["jitter_acciones"] = round(ex["acciones"], 3)
                    for sk in STAKES_CAP:
                        ex = ejecutar(Lc, trades.get(tok_c, []), t, CONFIG["latencia_oficial_ms"], plim,
                                      max(CONFIG["min_acciones"], sk / ask0))
                        fila[f"cap{sk}_acciones"], fila[f"cap{sk}_precio"] = round(ex["acciones"], 3), ex["precio"]
                    eventos.append(fila)
                elif activo and ult_senal is not None and t - ult_senal >= CONFIG["rearme_ms"]:
                    activo = False
            # controles (B3/B4): solo para la regla principal
            if regla != "B1_5m":
                continue
            for tc in range(t_ini, t_fin, CONFIG["control_cada_ms"]):
                _, qc = Lc.en(tc)
                _, qo = Lo.en(tc)
                if not qc or not qo or qc[1] is None or qo[0] is None:
                    continue
                ask0 = qc[1]
                acc_obj = max(CONFIG["min_acciones"], CONFIG["stake_eur"] / ask0)
                ex = ejecutar(Lc, trades.get(tok_c, []), tc, CONFIG["latencia_oficial_ms"], 0.99, acc_obj)
                controles.append({"moneda": mo, "cierre": cie, "market_compra": meta[tok_c][2],
                                  "lado": "Up" if s == "YES" else "Down", "t": tc, "ask0": ask0,
                                  "margen_neto": margen(qo[0], ask0), "clase": ex["clase"], "precio": ex["precio"],
                                  "acciones": round(ex["acciones"], 3)})
    SALIDA.mkdir(parents=True, exist_ok=True)
    for nombre, filas in (("eventos", eventos), ("controles", controles)):
        p = SALIDA / f"{nombre}_{dia}.csv"
        if filas:
            campos = list(dict.fromkeys(k for f_ in filas for k in f_))
            with open(p, "w", newline="") as fo:
                w = csv.DictWriter(fo, fieldnames=campos)
                w.writeheader()
                w.writerows(filas)
        elif p.exists():
            p.unlink()
    with open(SALIDA / f"calidad_{dia}.csv", "w", newline="") as fo:
        w = csv.writer(fo)
        w.writerow(["dia", "incidencia", "n"])
        for k, v in sorted(calidad.items()):
            w.writerow([dia, k, v])
    print(f"{dia}: pares {n_pares}, eventos {len(eventos)} (primeros B1 {sum(1 for e in eventos if e['regla'] == 'B1_5m' and e['es_primero'])}), "
          f"controles {len(controles)}, incidencias de calidad {dict(calidad)}")


# ------------------------------------------------------------------------------------------------ informe
def ic_dias(por_dia, n_boot=4000):
    ks = [k for k in por_dia if por_dia[k][1] > 0]
    if len(ks) < 3:
        return None
    rng = random.Random(17)
    m = []
    for _ in range(n_boot):
        mu = [por_dia[k] for k in (rng.choice(ks) for _ in ks)]
        m.append(sum(x[0] for x in mu) / sum(x[1] for x in mu))
    m.sort()
    return {"ic90": (round(m[int(.05 * n_boot)], 4), round(m[int(.95 * n_boot)], 4)),
            "ic95": (round(m[int(.025 * n_boot)], 4), round(m[int(.975 * n_boot)], 4))}


def pnl_de(e, des, pref):
    """PnL de un evento a la latencia `pref` (L215, jitter, cap10...)."""
    acc = float(e.get(f"{pref}_acciones") or 0)
    pr = e.get(f"{pref}_precio")
    clase = e.get(f"{pref}_clase", "")
    if clase == "UNKNOWN" or e["market_compra"] not in des:
        return None
    if acc <= 0 or pr in (None, "", "None"):
        return (0.0, 0.0)
    pr = float(pr)
    gana = (des[e["market_compra"]] == "YES") == (e["lado"] == "Up")
    return (acc * ((1.0 if gana else 0.0) - pr - fee(pr)), acc * (pr + fee(pr)))


def resumen(evs, des, pref, etiqueta):
    filas = [(e, pnl_de(e, des, pref)) for e in evs]
    unk = sum(1 for _, p in filas if p is None)
    ok = [(e, p) for e, p in filas if p is not None]
    ej = [(e, p) for e, p in ok if p[1] > 0]
    out = {"etiqueta": etiqueta, "senales": len(evs), "unknown": unk, "ejecutables": len(ej),
           "fill_rate": round(len(ej) / max(1, len(ok)), 3),
           "parciales": sum(1 for e, _ in ej if "parcial" in str(e.get(f"{pref}_clase", "")))}
    if not ej:
        return out
    pn = [p[0] for _, p in ej]
    rk = sum(p[1] for _, p in ej)
    por_dia = collections.defaultdict(lambda: [0.0, 0.0])
    for e, p in ej:
        dd = datetime.fromtimestamp(int(e["cierre"]), timezone.utc).date().isoformat()
        por_dia[dd][0] += p[0]
        por_dia[dd][1] += p[1]
    ganan = [x for x in pn if x > 0]
    pierden = [x for x in pn if x <= 0]
    acum, pico, dd_ = 0.0, 0.0, 0.0
    for x in sorted(((int(e["t_deteccion"]), p[0]) for e, p in ej)):
        acum += x[1]
        pico = max(pico, acum)
        dd_ = max(dd_, pico - acum)
    q = sorted(pn)
    pct = lambda p_: round(q[min(len(q) - 1, int(len(q) * p_))], 3)
    roi_d = sorted(v[0] / v[1] for v in por_dia.values() if v[1] > 0)
    mejor_dia = max(por_dia, key=lambda k: por_dia[k][0])
    sin_mejor = [p for e, p in ej if datetime.fromtimestamp(int(e["cierre"]), timezone.utc).date().isoformat() != mejor_dia]
    top5 = sorted(pn, reverse=True)[:max(1, len(pn) // 20)]
    sin_btc = [p for e, p in ej if e["moneda"] != "BTC"]
    out.update({
        "dias": len(por_dia), "pnl_neto": round(sum(pn), 3), "riesgo": round(rk, 3), "ev_por_eur": round(sum(pn) / rk, 4),
        "acierto": round(len(ganan) / len(pn), 3), "media_gana": round(st.mean(ganan), 3) if ganan else None,
        "media_pierde": round(st.mean(pierden), 3) if pierden else None,
        "mediana_gana": round(st.median(ganan), 3) if ganan else None,
        "mediana_pierde": round(st.median(pierden), 3) if pierden else None,
        "mediana_pnl": round(st.median(pn), 3), "P25": pct(.25), "P75": pct(.75), "P90": pct(.9), "P95": pct(.95),
        "P99": pct(.99), "max_drawdown": round(dd_, 3), "peor": round(min(pn), 3), "mejor": round(max(pn), 3),
        "pnl_por_dia": round(sum(pn) / len(por_dia), 3), "dias_positivos": sum(1 for v in por_dia.values() if v[0] > 0),
        "roi_diario_media": round(st.mean(roi_d), 4), "roi_diario_mediana": round(st.median(roi_d), 4),
        "roi_diario_sd": round(st.pstdev(roi_d), 4) if len(roi_d) > 1 else None,
        "roi_diario_P5": round(roi_d[int(len(roi_d) * .05)], 4), "roi_diario_P95": round(roi_d[int(len(roi_d) * .95) - 1 if len(roi_d) > 1 else 0], 4),
        "ic_dias": ic_dias(por_dia),
        "ev_sin_mejor_dia": round(sum(p[0] for p in sin_mejor) / max(1e-9, sum(p[1] for p in sin_mejor)), 4) if sin_mejor else None,
        "pnl_sin_top5pct": round(sum(pn) - sum(top5), 3),
        "ev_sin_btc": round(sum(p[0] for p in sin_btc) / max(1e-9, sum(p[1] for p in sin_btc)), 4) if sin_btc else None,
        "pct_pnl_mejor_dia": round(por_dia[mejor_dia][0] / sum(pn), 3) if sum(pn) > 0 else None,
    })
    return out


def red_team(prim, des):
    """Estrés sobre los eventos oficiales a 215 ms (además de la curva de latencia). Nunca cambia la regla."""
    out = {}
    def ev_con(f_acc=1.0, f_fee=1.0, tick=0.0, quitar_top=0.0, quitar_mejor_dia=False, pref="L215"):
        filas = []
        for e in prim:
            if e["market_compra"] not in des or e.get(f"{pref}_clase") == "UNKNOWN":
                continue
            acc = float(e.get(f"{pref}_acciones") or 0)
            disp = e.get(f"{pref}_disp_nivel1")
            if disp not in (None, "", "None"):
                acc = min(acc, float(disp) * f_acc)
            pr = e.get(f"{pref}_precio")
            if acc <= 0 or pr in (None, "", "None"):
                continue
            pr = min(0.99, float(pr) + tick)
            g = (des[e["market_compra"]] == "YES") == (e["lado"] == "Up")
            fe = f_fee * fee(pr)
            filas.append((datetime.fromtimestamp(int(e["cierre"]), timezone.utc).date().isoformat(),
                          acc * ((1.0 if g else 0.0) - pr - fe), acc * (pr + fe)))
        if not filas:
            return None
        if quitar_top:
            filas.sort(key=lambda x: -x[1])
            filas = filas[max(1, int(len(filas) * quitar_top)):]
        if quitar_mejor_dia:
            pd_ = collections.defaultdict(float)
            for d, p, _ in filas:
                pd_[d] += p
            md = max(pd_, key=pd_.get)
            filas = [x for x in filas if x[0] != md]
        rk = sum(x[2] for x in filas)
        return round(sum(x[1] for x in filas) / rk, 4) if rk else None
    out["base_L215"] = ev_con()
    out["lat_+35ms(L250)"] = ev_con(pref="L250")
    out["lat_+60ms(L275)"] = ev_con(pref="L275")
    out["lat_+85ms(L300)"] = ev_con(pref="L300")
    out["profundidad_-25%"] = ev_con(f_acc=0.75)
    out["profundidad_-50%"] = ev_con(f_acc=0.5)
    out["fee_x1,5"] = ev_con(f_fee=1.5)
    out["precio_1tick_peor"] = ev_con(tick=0.01)
    out["precio_2ticks_peor"] = ev_con(tick=0.02)
    out["sin_top1%"] = ev_con(quitar_top=0.01)
    out["sin_mejor_dia"] = ev_con(quitar_mejor_dia=True)
    return out


def rolling(prim, des):
    pd_ = collections.defaultdict(lambda: [0.0, 0.0])
    for e in prim:
        p = pnl_de(e, des, "L215")
        if p and p[1] > 0:
            pd_[datetime.fromtimestamp(int(e["cierre"]), timezone.utc).date().isoformat()][0] += p[0]
            pd_[datetime.fromtimestamp(int(e["cierre"]), timezone.utc).date().isoformat()][1] += p[1]
    dias = sorted(pd_)
    out = {"pnl_diario": {d: round(pd_[d][0], 3) for d in dias}}
    acum = 0.0
    out["pnl_acumulado"] = {}
    for d in dias:
        acum += pd_[d][0]
        out["pnl_acumulado"][d] = round(acum, 3)
    for w in (3, 5, 10):
        if len(dias) >= w:
            u = dias[-w:]
            out[f"rolling_{w}d_ev"] = round(sum(pd_[d][0] for d in u) / max(1e-9, sum(pd_[d][1] for d in u)), 4)
    if dias:
        out["mejor_dia"] = max(dias, key=lambda d: pd_[d][0])
        out["peor_dia"] = min(dias, key=lambda d: pd_[d][0])
        out["prob_dia_perdedor"] = round(sum(1 for d in dias if pd_[d][0] < 0) / len(dias), 3)
    return out


def informe(telegram=False):
    sys.path.insert(0, str(REPO))
    from analisis_maker_cancelacion_binance import desenlaces
    E, C = [], []
    for f in sorted(SALIDA.glob("eventos_*.csv")):
        E += list(csv.DictReader(open(f)))
    for f in sorted(SALIDA.glob("controles_*.csv")):
        C += list(csv.DictReader(open(f)))
    if not E:
        print("sin eventos")
        return
    des = desenlaces({e["market_compra"] for e in E} | {c["market_compra"] for c in C})
    cong = int(datetime.fromisoformat(CONFIG["congelado_utc"]).timestamp() * 1000)
    rep = {"generado_utc": datetime.now(timezone.utc).isoformat(), "version": CONFIG["version"], "hash": hash_config(),
           "congelado_utc": CONFIG["congelado_utc"], "periodos": {}}
    lineas = [f"🧊 Vigía 5m barato (DRY-RUN, v{CONFIG['version']}, regla congelada margen_neto>=0,05, L=215 ms, stake 2€)"]
    for periodo, filtro in (("PRE_congelacion", lambda e: int(e["t_deteccion"]) < cong),
                            ("OOS_forward", lambda e: int(e["t_deteccion"]) >= cong)):
        P = {}
        prim = [e for e in E if e["regla"] == "B1_5m" and e["es_primero"] == "1" and filtro(e)]
        b2 = [e for e in E if e["regla"] == "B2_15m" and e["es_primero"] == "1" and filtro(e)]
        P["B1_oficial_L215"] = resumen(prim, des, "L215", "B1 5m regla congelada, L=215")
        P["B1_jitter"] = resumen(prim, des, "jitter", "B1 con latencia muestreada (jitter)")
        P["B1_todos_los_eventos_L215"] = resumen([e for e in E if e["regla"] == "B1_5m" and filtro(e)], des, "L215",
                                                 "B1 incluyendo re-armes (descriptivo)")
        P["B2_15m_L215"] = resumen(b2, des, "L215", "B2 regla espejo en 15m")
        P["latencia"] = {f"L{L}": resumen(prim, des, f"L{L}", f"L={L}") for L in CONFIG["latencias_diagnostico_ms"]}
        P["capacidad"] = {f"{sk}EUR": resumen(prim, des, f"cap{sk}", f"stake {sk}") for sk in STAKES_CAP}
        P["por_moneda"] = {m: resumen([e for e in prim if e["moneda"] == m], des, "L215", m)
                           for m in sorted({e["moneda"] for e in prim})}
        P["por_precio"] = {f"{lo:.2f}-{hi:.2f}": resumen([e for e in prim if lo <= float(e["ask_compra_t0"]) < hi], des, "L215", "")
                           for lo, hi in TRAMOS_PRECIO}
        P["por_margen_desc"] = {}
        for mg in MARGENES_DESC:
            P["por_margen_desc"][f">={mg}"] = resumen([e for e in prim if float(e["margen_neto"]) >= mg], des, "L215", "")
        P["por_lado"] = {l: resumen([e for e in prim if e["lado"] == l], des, "L215", l) for l in ("Up", "Down")}
        P["por_resto"] = {f"{a}-{b}s": resumen([e for e in prim if a <= float(e["resto_s"]) < b], des, "L215", "")
                          for a, b in ((0, 60), (60, 120), (120, 180), (180, 240), (240, 300))}
        P["por_hora"] = {h: resumen([e for e in prim if datetime.fromtimestamp(int(e["t_deteccion"]) / 1000, timezone.utc).hour // 4 * 4 == h], des, "L215", "")
                         for h in range(0, 24, 4)}
        P["clases_causales_L215"] = dict(collections.Counter(e["L215_clase"] for e in prim))
        # supervivencia del ask y precio esperado vs latencia
        sup = {}
        for L in CONFIG["latencias_diagnostico_ms"]:
            v = [e for e in prim if e[f"L{L}_clase"] != "UNKNOWN"]
            sup[f"L{L}"] = {"p_ask_original_sigue": round(sum(1 for e in v if e[f"L{L}_clase"].startswith("A")) / max(1, len(v)), 3),
                            "p_ejecutable": round(sum(1 for e in v if float(e[f"L{L}_acciones"] or 0) > 0) / max(1, len(v)), 3),
                            "p_profundidad_stake": round(sum(1 for e in v if float(e[f"L{L}_acciones"] or 0) >= float(e["acciones_objetivo"]) - 1e-6) / max(1, len(v)), 3),
                            "precio_medio_ejecucion": round(st.mean([float(e[f"L{L}_precio"]) for e in v if float(e[f"L{L}_acciones"] or 0) > 0]), 4)
                            if any(float(e[f"L{L}_acciones"] or 0) > 0 for e in v) else None}
        P["supervivencia"] = sup
        # edad del ask vs supervivencia a +215
        ed = collections.defaultdict(lambda: [0, 0])
        for e in prim:
            if e["L215_clase"] == "UNKNOWN" or e["c_edad_ask_ms"] in ("", "None"):
                continue
            a = float(e["c_edad_ask_ms"])
            k = "<250ms" if a < 250 else "250ms-1s" if a < 1000 else "1-5s" if a < 5000 else ">=5s"
            ed[k][0] += 1
            ed[k][1] += int(float(e["L215_acciones"] or 0) > 0)
        P["edad_ask_vs_ejecutable"] = {k: f"{v[1]}/{v[0]}" for k, v in ed.items()}
        # benchmarks B3/B4
        Cp = [c for c in C if filtro({"t_deteccion": c["t"]})]
        def pnl_c(c):
            if c["market_compra"] not in des or c["clase"] == "UNKNOWN" or float(c["acciones"] or 0) <= 0 or c["precio"] in ("", "None"):
                return None
            pr = float(c["precio"])
            g = (des[c["market_compra"]] == "YES") == (c["lado"] == "Up")
            return (float(c["acciones"]) * ((1.0 if g else 0.0) - pr - fee(pr)), float(c["acciones"]) * (pr + fee(pr)))
        b3 = [p for p in (pnl_c(c) for c in Cp) if p]
        P["B3_5m_sin_umbral"] = {"n": len(b3), "ev_por_eur": round(sum(p[0] for p in b3) / max(1e-9, sum(p[1] for p in b3)), 4) if b3 else None}
        ctl = [c for c in Cp if float(c["margen_neto"]) < 0.01]
        emp, pe, pc = 0, [], []
        for e in prim:
            pe_ = pnl_de(e, des, "L215")
            if not pe_ or pe_[1] <= 0:
                continue
            a0 = float(e["ask_compra_t0"])
            cand = [c for c in ctl if c["moneda"] == e["moneda"] and c["cierre"] != e["cierre"]
                    and abs(float(c["ask0"]) - a0) <= 0.025]
            cand = [(abs(int(c["t"]) - int(e["t_deteccion"])), c) for c in cand]
            cand = [c for _, c in sorted(cand, key=lambda x: x[0])[:5]]
            pcs = [p for p in (pnl_c(c) for c in cand) if p]
            if pcs:
                emp += 1
                pe.append(pe_)
                pc.append((sum(p[0] for p in pcs) / len(pcs), sum(p[1] for p in pcs) / len(pcs)))
        P["B4_control_emparejado"] = {"n_emparejados": emp,
                                      "ev_evento": round(sum(p[0] for p in pe) / max(1e-9, sum(p[1] for p in pe)), 4) if pe else None,
                                      "ev_control": round(sum(p[0] for p in pc) / max(1e-9, sum(p[1] for p in pc)), 4) if pc else None}
        # gates y alertas
        r = P["B1_oficial_L215"]
        ic = (r.get("ic_dias") or {}).get("ic90")
        gates = {"G1_n>=40": r.get("ejecutables", 0) >= 40, "G2_dias>=10": r.get("dias", 0) >= 10,
                 "G3_EV>=0,10": (r.get("ev_por_eur") or -9) >= 0.10, "G4_IC90_diario>0": bool(ic and ic[0] > 0),
                 "G5_sin_mejor_dia>0": (r.get("ev_sin_mejor_dia") or -9) > 0, "G6_sin_top5%>0": (r.get("pnl_sin_top5pct") or -9) > 0,
                 "G7_sin_BTC>0": (r.get("ev_sin_btc") or -9) > 0, "G8_reconstruccion": r.get("unknown", 1) == 0,
                 "G9_latencia_real": True, "G10_OOS": periodo == "OOS_forward"}
        P["gates"] = gates
        alertas = []
        if r.get("pct_pnl_mejor_dia") and r["pct_pnl_mejor_dia"] > 0.5:
            alertas.append(f"concentración: {r['pct_pnl_mejor_dia']:.0%} del PnL en un día")
        mon = {m: v.get("pnl_neto", 0) for m, v in P["por_moneda"].items()}
        if r.get("pnl_neto", 0) > 0 and mon and max(mon.values()) > 0.6 * r["pnl_neto"]:
            alertas.append(f"concentración por moneda: {max(mon, key=mon.get)}")
        if (r.get("pnl_sin_top5pct") or 0) <= 0 < (r.get("pnl_neto") or 0):
            alertas.append("el PnL depende del 5 % mejor de operaciones")
        l250, l300 = P["latencia"]["L250"].get("ev_por_eur"), P["latencia"]["L300"].get("ev_por_eur")
        if r.get("ev_por_eur") and l300 is not None and r["ev_por_eur"] > 0 and l300 <= 0:
            alertas.append("el edge desaparece al subir la latencia a 300 ms")
        P["alertas"] = alertas
        P["stress"] = red_team(prim, des)
        # deriva (solo alerta, nunca cambia la regla): últimos 3 días vs anteriores
        dias_ev = sorted({datetime.fromtimestamp(int(e["cierre"]), timezone.utc).date().isoformat() for e in prim})
        if len(dias_ev) >= 6:
            ult = set(dias_ev[-3:])
            a_ = resumen([e for e in prim if datetime.fromtimestamp(int(e["cierre"]), timezone.utc).date().isoformat() in ult], des, "L215", "")
            b_ = resumen([e for e in prim if datetime.fromtimestamp(int(e["cierre"]), timezone.utc).date().isoformat() not in ult], des, "L215", "")
            P["deriva"] = {"ultimos3": {k: a_.get(k) for k in ("ev_por_eur", "fill_rate", "ejecutables")},
                           "anteriores": {k: b_.get(k) for k in ("ev_por_eur", "fill_rate", "ejecutables")}}
            if (b_.get("ev_por_eur") or 0) > 0 and (a_.get("ev_por_eur") or 0) < 0.5 * (b_.get("ev_por_eur") or 0):
                alertas.append("DRIFT DETECTED: EV de los 3 últimos días < 50 % del anterior")
            if (a_.get("fill_rate") or 1) < 0.7 * (b_.get("fill_rate") or 0):
                alertas.append("DRIFT DETECTED: caída del fill rate")
        P["rolling"] = rolling(prim, des)
        st_ = P["stress"]
        if r.get("ev_por_eur") and st_.get("precio_1tick_peor") is not None and r["ev_por_eur"] > 0 >= st_["precio_1tick_peor"]:
            alertas.append("el resultado se pierde con 1 tick peor de precio")
        rep["periodos"][periodo] = P
        lineas.append(f"\n[{periodo}] señales {r.get('senales', 0)} | ejecutables a +215 ms {r.get('ejecutables', 0)} "
                      f"(fill {r.get('fill_rate', 0):.0%}, desconocidas {r.get('unknown', 0)}) | PnL neto {r.get('pnl_neto', 0):+.2f} € "
                      f"| EV/€ {r.get('ev_por_eur', 0) or 0:+.3f} | días {r.get('dias', 0)} (+{r.get('dias_positivos', 0)}) "
                      f"| IC90 diario {ic} | sin BTC {r.get('ev_sin_btc')} | sin mejor día {r.get('ev_sin_mejor_dia')}")
        lineas.append("   latencia→EV: " + " ".join(f"{k}:{(v.get('ev_por_eur') or 0):+.2f}/{v.get('ejecutables', 0)}" for k, v in P["latencia"].items()))
        lineas.append(f"   jitter EV {P['B1_jitter'].get('ev_por_eur')} | B2 15m EV {P['B2_15m_L215'].get('ev_por_eur')} | "
                      f"B3 sin umbral EV {P['B3_5m_sin_umbral'].get('ev_por_eur')} | B4 evento {P['B4_control_emparejado']['ev_evento']} "
                      f"vs control {P['B4_control_emparejado']['ev_control']} (n={emp})")
        lineas.append("   red team EV/€: " + " ".join(f"{k}:{v}" for k, v in P["stress"].items()))
        lineas.append("   gates: " + " ".join(f"{k}{'✅' if v else '❌'}" for k, v in gates.items()))
        if alertas:
            lineas.append("   ⚠️ " + " | ".join(alertas))
    oos = rep["periodos"]["OOS_forward"]
    g = oos["gates"]
    veredicto = "GREEN" if all(g.values()) else ("YELLOW" if g["G1_n>=40"] and g["G3_EV>=0,10"] else "EN_CURSO")
    rep["veredicto"] = veredicto
    lineas.append(f"\nVEREDICTO (solo OOS): {veredicto}. Nada pasa a dinero sin todos los gates + /code-review + OK de Javi.")
    (SALIDA / "informe.json").write_text(json.dumps(rep, indent=1, ensure_ascii=False, default=str))
    txt = "\n".join(lineas)
    (SALIDA / "informe.txt").write_text(txt)
    print(txt)
    if telegram:
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram(txt[:3900])
        except Exception as e:
            print(f"(Telegram falló: {e})")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("procesar")
    p1.add_argument("--dia", default=(datetime.now(timezone.utc).date() - timedelta(days=1)).isoformat())
    p2 = sub.add_parser("informe")
    p2.add_argument("--telegram", action="store_true")
    a = ap.parse_args()
    if a.cmd == "procesar":
        procesar(a.dia)
    else:
        informe(a.telegram)


if __name__ == "__main__":
    main()
