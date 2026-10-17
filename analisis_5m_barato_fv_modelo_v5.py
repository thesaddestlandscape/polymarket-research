#!/usr/bin/env python3
"""5m barato H34 — FV v5 (16-Oct): corrige los fallos de diseño de FV v4 (red-team 16-Oct, H07). SOLO LECTURA / dry-run.

QUÉ ARREGLA (cada punto = un hallazgo del red-team sobre v4):
  1. Reproducible: HGB con random_state fijo y early_stopping=False, hilos=1; el modelo se entrena UNA vez sobre DESC y se
     serializa con su hash en datalogs/m5barato_mision/fv5_modelo_<hash>/ (modelo.pkl + meta.json). El juicio OOS y el
     forward usan SOLO ese modelo congelado: `juzgar` nunca reentrena. Hiperparámetros elegidos solo en DESC con
     validación temporal (entrena 05-10, valida 11-12; el modelo final se reajusta en 05-12 con lo elegido).
  2. Multimoneda: dataset y modelo de BTC, ETH, SOL, XRP, DOGE, BNB (mismo constructor de v4, generalizado; lector con orden
     estable por recepción: los tramos del registro no son cronológicos). Decisiones de diseño en BTC (la selección de
     hiperparámetros usa R² de validación de BTC); cada moneda se juzga con su propio gate en OOS.
  3. Benchmarks correctos: Brier y MSE de FV frente a mid(t), mid(t+70 ms) (latencia maker) y mid(t+355 ms) (tomador), con
     IC90 por días, sobre la MISMA muestra común; y FV vs mid(t+355) como predictor de mid(t+3 s). Placebos: permutación
     dentro de (día, moneda), inversión, FV=mid(t) y FV=mid(t+L) (los propios benchmarks).
  4. Tomador (uso SECUNDARIO): M elegido en DESC desde una rejilla fija {0,02; 0,03; 0,05; 0,08}; si la curva EV(M) en DESC
     no es monótona (no decreciente con n>=30), tomador = NO_APTO y no hay M congelado. En OOS: sin top3, mediana, sin mejor
     día, por hora/T, por tipo de evento (Binance>=2 bps vs 15m vs otro), Up vs Down, bootstrap por mercado, por CIERRE
     (las monedas del mismo cierre son una apuesta) y por días, profundidad nivel 1 al llegar (q trae tamaños) contra el
     stake, y entrada con límite=ask(t) (descarta el 59 % de "ask cayendo hacia nosotros"). Se elige la primera entrada
     CRONOLÓGICA por mercado-lado (v4 elegía por orden de fichero, no de tiempo).
  5. Uso PRINCIPAL: señal FV(t) para la guarda de cancelación del maker H26 (ver INTERFAZ).
  6. Gz truncados: no se silencian; el día queda PARTIAL (truncado=True, líneas leídas y error en el meta); por defecto el
     juicio y el entrenamiento EXCLUYEN los días truncados (--incluir-truncados para forzar).

INTERFAZ PARA EL SIMULADOR MAKER H26 (importable sin efectos secundarios):
    import analisis_5m_barato_fv_modelo_v5 as F5
    mdl = F5.FVModelo.cargar("<hash>")                       # o ruta al directorio fv5_modelo_<hash>; verifica el hash
    ctx = F5.contexto_dia("2026-10-14", monedas=("BTC",))     # lee el registro ms del día (mismo lector que el dataset)
    s = F5.fv_en(ctx, mdl, "BTC", cierre_s, ts_ms)            # cierre_s: cierre del 5m en epoch s; ts_ms: np.array de
                                                              # instantes de RECEPCIÓN (ms) donde se quiere FV
    s["fv_up"], s["dhat"]  -> arrays (NaN donde no hay rasgos: sin libro 5m/15m válido, <20 ticks Binance, sigma 0)
    FV del token Down = 1 - fv_up.   Solo usa información con recepción <= t (sin look-ahead).
    F5.cancelar_guardia(fv_up, "Up"|"Down", precio_nuestro, g)  -> bool array: cancelar si FV_lado - precio < g
    F5.SenalFV("fv5_senal_<hash>_<D>.csv.gz").en(mercado, t_ms) -> (fv_up, edad_ms) asof sobre la rejilla 1 s + eventos
    Archivo de señal (comando `senal`): moneda,mercado,cierre,t,tipo,fv_up,dhat por punto del dataset (rejilla 1 s,
    eventos Binance >= 2 bps y cambios del mid15 >= 0,01). Para precisión de ms usar fv_en, no el archivo.
    La cota de la señal: FV mejora al mid solo si el informe dice que bate a mid(t+L); el valor económico para el maker
    lo mide el simulador H26 (aquí solo hay un diagnóstico AUC de la guarda, sección 3 del informe).

MODOS (CLI):
    dataset  --dias D,D   construye/reutiliza fv5_dataset_D.csv.gz (+ .meta.json con cobertura) [--monedas] [--recorte H0-H1]
    entrenar              DESC -> fv5_modelo_<hash>/ ; imprime HASH y si coincide byte a byte con una corrida previa
    juzgar   --modelo H   informe OOS (no reentrena) [--oos-desde 2026-10-13 --oos-hasta 2026-10-15]
    senal    --modelo H   exporta fv5_senal_<hash>_<D>.csv.gz
    todo                  dataset DESC+OOS, entrenar y juzgar (reanudable: reutiliza cachés por día)
Contrato de trabajos largos: run_manifest.json en OUT/fv5_runs/<job_id>/ (job, sha del script, args, entradas con tamaño y
mtime, fechas pedidas, estado COMPLETE/PARTIAL/FAILED/BLOCKED, resumen parcial tras cada día); caché atómica por día
(clave = día; reanudar no duplica filas); logs con marca UTC por stdout; línea COBERTURA en el informe. BLOCKED si
MemAvailable < 1,5 GB o franja 06:00-09:00Z (solo modos que construyen/entrenan).
Uso: OMP_NUM_THREADS=1 nice -n 19 ionice -c3 python3 analisis_5m_barato_fv_modelo_v5.py todo
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse  # noqa: E402
import gzip  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import pickle  # noqa: E402
import resource  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
import zlib  # noqa: E402
from array import array  # noqa: E402
from collections import Counter, defaultdict  # noqa: E402
from datetime import date, datetime, timedelta, timezone  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analisis_5m_barato_fv_modelo_v4 as F4  # noqa: E402  (se reutilizan _top, _phi, _Phi, COLS, ic90_dias, constantes)
import vigia_5m_barato_forward as V  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402
from comision_cripto import FEE_CRIPTO  # noqa: E402

VERSION = "v5.0"
VERSION_DATASET = "ds5.0"
OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
MONEDAS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")
COIN_ID = {c: i for i, c in enumerate(MONEDAS)}
SEED = 20261016
DESC_TRAIN = [f"2026-10-{d:02d}" for d in range(5, 11)]
DESC_VAL = ["2026-10-11", "2026-10-12"]
OOS_DESDE, OOS_HASTA = "2026-10-13", "2026-10-15"
GRID_STRIDE = 4                          # entrenamiento: 1 de cada 4 filas de rejilla (RAM); los eventos van todos
REJILLA_M = (0.02, 0.03, 0.05, 0.08)     # congelada de antemano
N_MIN_M = 30                             # n mínimo (mercado-lado) para que un punto cuente en la curva EV(M)
MONOTONIA_TOL = 0.0
STAKE_EUR = 2.0
PROF_MIN = 0.80                          # fracción de entradas con profundidad nivel 1 >= stake (umbral informativo)
BN_BPS = 2.0                             # "evento Binance" = |mov 500 ms| >= 2 bps (igual que el constructor v4)
LAT_MAKER, LAT_TOMADOR = 70, F4.LAT_MS
COBERTURA_MIN = 0.90                     # fracción de mercados esperados (288/día/moneda) para no marcar cobertura baja
EXTRA = ["moneda", "bn500", "m5_70", "m5_355", "bsz_lat", "asz_lat"]
COLS = F4.COLS + EXTRA
RASGOS_BASE = [r for r in F4.RASGOS]
RASGOS = RASGOS_BASE + ["coin_id"]
MIN_MEM_MB = 1500
FRANJA_BLOQ = (6, 9)                     # UTC, [6, 9)

# candidatos de hiperparámetros: lista FIJA, elegida solo en DESC por R² de validación en eventos de BTC
CANDIDATOS = [
    ("ridge_btc", "btc", {"kind": "ridge", "alpha": 10.0}),
    ("hgb_d3_l500_i150_btc", "btc", {"kind": "hgb", "max_depth": 3, "min_samples_leaf": 500, "max_iter": 150}),
    ("hgb_d3_l500_i300_btc", "btc", {"kind": "hgb", "max_depth": 3, "min_samples_leaf": 500, "max_iter": 300}),
    ("hgb_d3_l500_i150_pool", "pool", {"kind": "hgb", "max_depth": 3, "min_samples_leaf": 500, "max_iter": 150}),
    ("hgb_d3_l500_i300_pool", "pool", {"kind": "hgb", "max_depth": 3, "min_samples_leaf": 500, "max_iter": 300}),
    ("hgb_d4_l2000_i300_pool", "pool", {"kind": "hgb", "max_depth": 4, "min_samples_leaf": 2000, "max_iter": 300}),
]


def nanmedia(v, f=np.nanmean):
    v = [x for x in v if x == x]
    return float(f(v)) if v else float("nan")


def log(msg):
    print(f"[{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}] {msg}", flush=True)


def escribir_atomico(ruta, texto):
    ruta = Path(ruta)
    tmp = ruta.with_name(ruta.name + ".tmp")
    with open(tmp, "w") as fh:
        fh.write(texto)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, ruta)


def sha_fichero(p, bloque=1 << 20):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for b in iter(lambda: fh.read(bloque), b""):
            h.update(b)
    return h.hexdigest()


def rss_mb():
    return round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 1)


# ====================================================================================================================
# 1. LECTOR DEL REGISTRO (generalización multimoneda del de v4) Y CONTEXTO
# ====================================================================================================================
def leer_registro(dia, monedas=MONEDAS):
    """-> (meta, libros, bx, inc) o None si falta algún fichero del día.
    meta: token YES -> (moneda, marco, id mercado, cierre s). libros: token -> V.Libro ordenado de forma estable por
    RECEPCIÓN. bx: moneda -> (t_recepción ms, precio) ordenados. inc: integridad (truncado, líneas, inválidas).
    A diferencia de v4, un gz truncado NO se traga: queda en inc['truncado'] y en inc['archivos']."""
    sim2c = {V.SIM[c]: c for c in monedas}
    meta, libros = {}, {}
    bx = {c: (array("q"), array("d")) for c in monedas}
    inc = {"truncado": False, "archivos": {}, "lineas": 0, "q_invalidas": 0, "x_invalidas": 0, "k_invalidas": 0}
    for pref in ("m15", "m5"):
        f = VOL / f"{pref}_registro" / f"{pref}_registro_{dia}.csv.gz"
        if not f.exists():
            return None
        n = 0
        try:
            with gzip.open(f, "rt", errors="replace") as fh:
                for ln in fh:
                    n += 1
                    tp = ln[:2]
                    if tp == "k,":
                        c = ln.rstrip("\n").split(",")
                        if len(c) >= 8 and c[3] in monedas and c[4] in ("5min", "15min") and c[7] == "YES":
                            try:
                                meta[c[2]] = (c[3], c[4], c[5], int(datetime.fromisoformat(c[6]).timestamp()))
                            except ValueError:
                                inc["k_invalidas"] += 1
                        continue
                    if tp == "x," and pref == "m5":
                        c = ln.split(",")
                        co = sim2c.get(c[2]) if len(c) > 7 else None
                        if co is not None:
                            try:
                                bx[co][0].append(int(c[7]))     # RECEPCIÓN (c[6] = E de Binance mezcla relojes)
                                bx[co][1].append(float(c[3]))
                            except (ValueError, IndexError):
                                inc["x_invalidas"] += 1
                        continue
                    if tp != "q,":
                        continue
                    c = ln.rstrip("\n").split(",")
                    m = meta.get(c[2])
                    if not m:
                        continue
                    try:
                        tr = int(c[7])
                        ini = m[3] - (300 if m[1] == "5min" else 900) - 5
                        if not (ini * 1000 <= tr <= m[3] * 1000):
                            continue
                        g = lambda x: None if x in ("", "None") else float(x)  # noqa: E731
                        libros.setdefault(c[2], V.Libro()).add(tr, (g(c[3]), g(c[4]), g(c[5]) or 0.0, g(c[6]) or 0.0,
                                                                     int(c[1])))
                    except (ValueError, IndexError):
                        inc["q_invalidas"] += 1
        except (EOFError, OSError, zlib.error) as e:
            inc["truncado"] = True
            inc["archivos"][pref] = {"lineas_leidas": n, "error": f"{type(e).__name__}: {e}"}
        inc["lineas"] += n
    for L in libros.values():
        L.ordenar()
    inc["q_filas"] = sum(len(L.t) for L in libros.values())
    bxo = {}
    for co, (t_, p_) in bx.items():
        bt = np.frombuffer(t_, dtype=np.int64)
        bp = np.frombuffer(p_, dtype=np.float64)
        o = np.argsort(bt, kind="stable")
        bxo[co] = (bt[o], bp[o])
    return meta, libros, bxo, inc


def contexto_dia(dia, monedas=MONEDAS):
    """Contexto reutilizable (también por el simulador maker): registro + refs TWAP + pares 5m/15m."""
    r = leer_registro(dia, monedas)
    if r is None:
        return None
    meta, libros, bx, inc = r
    tw = V.twap_refs([(date.fromisoformat(dia) - timedelta(days=1)).isoformat(), dia])
    por = defaultdict(dict)
    for tk, (coin, marco, mkt, cie) in meta.items():
        if marco == "5min" or cie % 900 == 0:
            por[(coin, cie)][marco] = (tk, mkt)
    return {"dia": dia, "meta": meta, "libros": libros, "bx": bx, "inc": inc, "tw": tw, "por": por,
            "d0": int(datetime.fromisoformat(dia + "T00:00:00+00:00").timestamp())}


def mercado_de(ctx, coin, cie):
    """(L5, L15, r5, mercado) del 5m que cierra en cie, o None. c15 = cierre del 15m que contiene al 5m."""
    toks = ctx["por"].get((coin, cie))
    if not toks or "5min" not in toks:
        return None
    c15 = cie + (-cie) % 900
    tk15 = ctx["por"].get((coin, c15), {}).get("15min")
    r5 = ctx["tw"].get(coin, {}).get(cie - 300)
    L5 = ctx["libros"].get(toks["5min"][0])
    L15 = ctx["libros"].get(tk15[0]) if tk15 else None
    return L5, L15, r5, toks["5min"][1]


def rasgos_punto(bt, bp, L5, L15, r5, cie, t):
    """Rasgos de v4 (idénticos) en el instante de recepción t, solo con datos <= t. -> (vals, bn500) o None.
    vals = [T, mid5, bid5, ask5, spr5, imb5, edad5, mid15, d15_500, d15_1000, z, pbin, sens, rb100..rb1000]."""
    a5, a15 = F4._top(L5, t), F4._top(L15, t)
    i = int(np.searchsorted(bt, t, side="right")) - 1
    if not a5 or not a15 or i < 0:
        return None
    p_now = bp[i]
    j = int(np.searchsorted(bt, t - 120_000, side="right"))
    if i - j < 20:
        return None
    ts = bt[j:i + 1]
    idx = np.searchsorted(ts, np.arange(ts[0], ts[-1], 1000))
    serie = bp[j:i + 1][np.clip(idx, 0, i - j)]
    rets = np.diff(np.log(serie)) * 1e4
    sig = float(np.std(rets)) if len(rets) > 10 else 0.0
    T = (cie * 1000 - t) / 1000.0
    if sig <= 0:
        return None
    dist = (p_now / r5 - 1) * 1e4
    z = dist / (sig * math.sqrt(T))
    sens = F4._phi(z) / (sig * math.sqrt(T))
    rbs, bn500 = [], 0.0
    for x in F4.RB:
        k = int(np.searchsorted(bt, t - x, side="right")) - 1
        pa = bp[k] if k >= 0 else None
        raw = (p_now / pa - 1) * 1e4 if pa else 0.0
        if x == 500:
            bn500 = float(raw)
        rbs.append(raw * sens if pa else 0.0)
    m15a, m15b = F4._top(L15, t - 500), F4._top(L15, t - 1000)
    vals = [round(T, 3), a5[0], a5[1], a5[2], round(a5[2] - a5[1], 4),
            round((a5[3] - a5[4]) / (a5[3] + a5[4]), 4) if a5[3] + a5[4] > 0 else 0.0, t - a5[5], a15[0],
            round(a15[0] - m15a[0], 4) if m15a else 0.0, round(a15[0] - m15b[0], 4) if m15b else 0.0,
            round(z, 4), round(F4._Phi(z), 5), round(sens, 6)] + [round(v, 6) for v in rbs]
    return vals, round(bn500, 4)


def puntos_mercado(bt, bp, L5, L15, cie):
    """Puntos de decisión (t ms de recepción, tipo): rejilla 1 s, eventos Binance y cambios del mid15 (== v4)."""
    t_ini, t_fin = (cie - 298) * 1000, (cie - 10) * 1000
    pts = [(t, "grid") for t in range(t_ini, t_fin + 1, 1000)]
    i0, i1 = int(np.searchsorted(bt, t_ini)), int(np.searchsorted(bt, t_fin))
    ult = -10**15
    j = i0
    for i in range(i0, i1):
        t = int(bt[i])
        while bt[j] < t - 500:
            j += 1
        if t - ult >= 2000 and abs(bp[i] / bp[j] - 1) * 1e4 >= F4.MOV_BPS:
            pts.append((t, "evento"))
            ult = t
    k0 = int(np.searchsorted(np.frombuffer(L15.t, dtype=np.int64), t_ini))
    prev = None
    ult15 = -10**15
    for k in range(k0, len(L15.t)):
        t = L15.t[k]
        if t > t_fin:
            break
        q = L15.fila(k)
        if q[0] is None or q[1] is None or q[0] >= q[1]:
            continue
        m = (q[0] + q[1]) / 2
        if prev is not None and abs(m - prev) >= 0.01 and t - ult15 >= 2000:
            pts.append((t, "evento15"))
            ult15 = t
        prev = m
    return pts


# ====================================================================================================================
# 2. DATASET POR DÍA (caché atómica + meta de cobertura)
# ====================================================================================================================
def rutas_dataset(dia, out, recorte=None):
    tag = "" if recorte is None else f"_r{recorte[0]}-{recorte[1]}"
    return out / f"fv5_dataset_{dia}{tag}.csv.gz", out / f"fv5_dataset_{dia}{tag}.meta.json"


def construir_dia(dia, monedas=MONEDAS, out=None, recorte=None, rehacer=False):
    """-> (ruta_csv, meta) | (None, meta con estado MISSING). Idempotente: si la caché (csv + meta, misma versión y monedas
    suficientes) existe, se reutiliza; una caída a mitad deja solo un .tmp (nunca un csv a medias)."""
    out = Path(out or OUT)
    c, mj = rutas_dataset(dia, out, recorte)
    if c.exists() and mj.exists() and not rehacer:
        m = json.loads(mj.read_text())
        if m.get("version_dataset") == VERSION_DATASET and set(monedas) <= set(m.get("monedas", [])):
            return c, m
    t0 = time.time()
    ctx = contexto_dia(dia, monedas)
    if ctx is None:
        return None, {"dia": dia, "estado": "MISSING", "motivo": "falta m5_registro o m15_registro"}
    inc = ctx["inc"]
    d0 = ctx["d0"]
    cierres = sorted({cie for (_, cie) in ctx["por"] if d0 < cie <= d0 + 86400})
    mids5 = {v["5min"][1] for (_, cie), v in ctx["por"].items() if "5min" in v and d0 < cie <= d0 + 86400}
    des = desenlaces(mids5)
    out.mkdir(parents=True, exist_ok=True)
    tmp = c.with_name(c.name + ".tmp")
    cob = {}
    with gzip.open(tmp, "wt") as fh:
        fh.write(",".join(COLS) + "\n")
        for coin in monedas:
            bt, bp = ctx["bx"][coin]
            k = cob[coin] = Counter()
            k["bx_ticks"] = len(bt)
            for cie in sorted(cc for (cn, cc) in ctx["por"] if cn == coin):
                if not (d0 < cie <= d0 + 86400) or "5min" not in ctx["por"][(coin, cie)]:
                    continue
                if recorte is not None and not (d0 + recorte[0] * 3600 <= cie <= d0 + recorte[1] * 3600):
                    continue
                k["mercados_5m"] += 1
                L5, L15, r5, mkt = mercado_de(ctx, coin, cie)
                res = des.get(mkt)
                if r5 is None:
                    k["sin_ref"] += 1
                if res is None:
                    k["sin_desenlace"] += 1
                if L5 is None:
                    k["sin_libro5"] += 1
                if L15 is None:
                    k["sin_libro15"] += 1
                if r5 is None or res is None or L5 is None or L15 is None:
                    continue
                y = 1 if res == "YES" else 0
                filas_mkt = 0
                for t, tipo in puntos_mercado(bt, bp, L5, L15, cie):
                    rp = rasgos_punto(bt, bp, L5, L15, r5, cie, t)
                    if rp is None:
                        k["puntos_sin_rasgos"] += 1
                        continue
                    vals, bn500 = rp
                    futs = []
                    for h in F4.HS:
                        f5 = F4._top(L5, t + h)
                        futs.append(f5[0] if f5 else "")
                    lat = F4._top(L5, t + LAT_TOMADOR)
                    p70 = F4._top(L5, t + LAT_MAKER)
                    row = [dia, mkt, cie, t, tipo] + vals + [lat[2] if lat else "", lat[1] if lat else ""] + futs + [y] \
                        + [coin, bn500, p70[0] if p70 else "", lat[0] if lat else "", lat[3] if lat else "",
                           lat[4] if lat else ""]
                    fh.write(",".join(str(v) for v in row) + "\n")
                    k["filas"] += 1
                    k["tipo_" + tipo] += 1
                    filas_mkt += 1
                if filas_mkt:
                    k["mercados_con_filas"] += 1
    os.replace(tmp, c)
    esperado = 288 if recorte is None else None
    baja = [co for co in monedas if esperado and cob[co]["mercados_con_filas"] < COBERTURA_MIN * esperado]
    meta = {"dia": dia, "version": VERSION, "version_dataset": VERSION_DATASET, "monedas": list(monedas),
            "recorte": recorte, "mercados_esperados_por_moneda": esperado, "cobertura": {co: dict(v) for co, v in cob.items()},
            "monedas_cobertura_baja": baja, "truncado": inc["truncado"], "archivos_truncados": inc["archivos"],
            "lineas_leidas": inc["lineas"], "q_invalidas": inc["q_invalidas"], "x_invalidas": inc["x_invalidas"],
            "k_invalidas": inc["k_invalidas"], "q_filas_en_memoria": inc["q_filas"], "estado": "PARTIAL" if (inc["truncado"] or baja) else "COMPLETE",
            "segundos": round(time.time() - t0, 1), "rss_pico_mb": rss_mb(), "sha256": sha_fichero(c),
            "filas": sum(v["filas"] for v in cob.values())}
    escribir_atomico(mj, json.dumps(meta, indent=1))
    return c, meta


# ====================================================================================================================
# 3. CARGA PARA MODELADO
# ====================================================================================================================
def cargar(dias, out, monedas=MONEDAS, grid_stride=1, solo_eventos=False, incluir_truncados=False, construir=True,
           recorte=None, info=None):
    """DataFrame de los días pedidos (construye los que falten si construir=True). Excluye días truncados salvo
    incluir_truncados. `info` (lista) recibe el meta de cada día (incl. los excluidos, con 'excluido')."""
    import pandas as pd
    dfs = []
    for d in dias:
        c, mj = rutas_dataset(d, Path(out), recorte)
        if construir:
            c, m = construir_dia(d, monedas, out, recorte)
        elif c.exists() and mj.exists():
            m = json.loads(mj.read_text())
        else:
            c, m = None, {"dia": d, "estado": "MISSING", "motivo": "sin caché"}
        if info is not None:
            info.append(dict(m))
        if c is None:
            continue
        if m.get("truncado") and not incluir_truncados:
            if info is not None:
                info[-1]["excluido"] = "gz truncado"
            continue
        for ch in pd.read_csv(c, chunksize=250_000):
            ch = ch[ch["moneda"].isin(monedas)]
            if solo_eventos:
                ch = ch[ch["tipo"] != "grid"]
            elif grid_stride > 1:
                ch = ch[(ch["tipo"] != "grid") | ((ch["t"] // 1000) % grid_stride == 0)]
            dfs.append(ch)
    if not dfs:
        return None
    df = pd.concat(dfs, ignore_index=True)
    df["pbin_m_mid"] = df["pbin"] - df["mid5"]
    df["m15_m_mid"] = df["mid15"] - df["mid5"]
    df["edad_raw"] = df["edad5"]
    df["edad5"] = np.log1p(df["edad5"].clip(lower=0))
    df["coin_id"] = df["moneda"].map(COIN_ID).astype(int)
    df["dy"] = df["m5_3000"] - df["mid5"]
    return df


# ====================================================================================================================
# 4. MODELO (reproducible, congelado, con hash)
# ====================================================================================================================
def _estimador(cfg):
    from sklearn.ensemble import HistGradientBoostingRegressor
    from sklearn.linear_model import Ridge
    if cfg["kind"] == "ridge":
        return Ridge(alpha=cfg["alpha"])
    return HistGradientBoostingRegressor(
        loss="squared_error", learning_rate=0.05, max_depth=cfg["max_depth"], min_samples_leaf=cfg["min_samples_leaf"],
        max_iter=cfg["max_iter"], early_stopping=False, random_state=SEED,
        categorical_features=[RASGOS.index("coin_id")] if cfg.get("pool") else None)


def _rasgos_de(cfg, ambito):
    return RASGOS if (ambito == "pool" and cfg["kind"] == "hgb") else RASGOS_BASE


def _X(df, rasgos):
    return df[rasgos].fillna(0.0).to_numpy(dtype=np.float64)


def r2(y, p):
    return float(1 - np.mean((y - p) ** 2) / np.mean(y ** 2)) if len(y) else float("nan")


def ajustar(df, nombre, ambito, cfg):
    """Ajuste determinista de un candidato. btc = solo filas BTC; pool = todas las monedas (coin_id categórica)."""
    cfg = dict(cfg, pool=(ambito == "pool"))
    rasgos = _rasgos_de(cfg, ambito)
    d = df[df["dy"].notna()]
    if ambito == "btc":
        d = d[d["moneda"] == "BTC"]
    est = _estimador(cfg)
    from threadpoolctl import threadpool_limits
    with threadpool_limits(limits=1):        # el reparto de hilos podría cambiar el orden de las sumas: 1 hilo = al bit
        est.fit(_X(d, rasgos), d["dy"].to_numpy(dtype=np.float64))
    return {"est": est, "rasgos": rasgos, "nombre": nombre, "ambito": ambito, "cfg": cfg, "n_train": int(len(d))}


def predecir(mod, df):
    return mod["est"].predict(_X(df, mod["rasgos"]))


class FVModelo:
    """Predictor cargable del modelo congelado. dhat(df) -> Δ̂ (cambio previsto del mid5 a +3 s); FV_up = clip(mid5+Δ̂)."""
    def __init__(self, mod, meta, ruta):
        self.mod, self.meta, self.ruta = mod, meta, ruta

    @classmethod
    def cargar(cls, ref, out=None):
        p = Path(ref)
        if not p.is_dir():
            p = Path(out or OUT) / f"fv5_modelo_{ref}"
        raw = (p / "modelo.pkl").read_bytes()
        h = hashlib.sha256(raw).hexdigest()[:16]
        meta = json.loads((p / "meta.json").read_text())
        if h != meta["hash"] or not p.name.endswith(h):
            raise ValueError(f"modelo corrupto o renombrado: hash {h} != {meta['hash']} ({p})")
        return cls(pickle.loads(raw), meta, p)

    @property
    def hash(self):
        return self.meta["hash"]

    def dhat(self, df):
        return predecir(self.mod, df)

    def fv_up(self, df, dhat=None):
        d = self.dhat(df) if dhat is None else dhat
        return np.clip(df["mid5"].to_numpy() + d, 0.01, 0.99)


def df_de_vals(vals_list, coin):
    """Construye el DataFrame mínimo para predecir a partir de rasgos_punto()."""
    import pandas as pd
    cols = F4.COLS[5:22]
    d = pd.DataFrame(vals_list, columns=cols)
    d["pbin_m_mid"] = d["pbin"] - d["mid5"]
    d["m15_m_mid"] = d["mid15"] - d["mid5"]
    d["edad5"] = np.log1p(d["edad5"].clip(lower=0))
    d["coin_id"] = COIN_ID[coin]
    return d


def fv_en(ctx, modelo, coin, cierre_s, ts_ms):
    """FV(t) del 5m de `coin` que cierra en `cierre_s`, en cada instante de recepción de ts_ms. Sin look-ahead."""
    ts_ms = np.asarray(ts_ms, dtype=np.int64)
    out = {"fv_up": np.full(len(ts_ms), np.nan), "dhat": np.full(len(ts_ms), np.nan)}
    mk = mercado_de(ctx, coin, int(cierre_s))
    if mk is None or mk[0] is None or mk[1] is None or mk[2] is None:
        return out
    L5, L15, r5, _ = mk
    bt, bp = ctx["bx"][coin]
    filas, pos = [], []
    for i, t in enumerate(ts_ms):
        rp = rasgos_punto(bt, bp, L5, L15, r5, int(cierre_s), int(t))
        if rp is not None:
            filas.append(rp[0])
            pos.append(i)
    if filas:
        d = df_de_vals(filas, coin)
        dh = modelo.dhat(d)
        out["dhat"][pos] = dh
        out["fv_up"][pos] = np.clip(d["mid5"].to_numpy() + dh, 0.01, 0.99)
    return out


def cancelar_guardia(fv_up, lado, precio, g):
    """Guarda de cancelación del maker: True (cancelar) si FV_lado - precio nuestro < g. NaN (sin FV) -> True (fail-closed)."""
    fv = np.asarray(fv_up, dtype=float)
    f = fv if lado == "Up" else 1.0 - fv
    return ~np.isfinite(f) | ((f - np.asarray(precio, dtype=float)) < g)


class SenalFV:
    """Lectura asof del archivo de señal fv5_senal_<hash>_<D>.csv.gz (rejilla 1 s + eventos)."""
    def __init__(self, ruta):
        import pandas as pd
        d = pd.read_csv(ruta).sort_values(["mercado", "t"], kind="mergesort")
        self._t, self._f = {}, {}
        for m, g in d.groupby("mercado"):
            self._t[m] = g["t"].to_numpy(dtype=np.int64)
            self._f[m] = g["fv_up"].to_numpy()

    def en(self, mercado, t_ms):
        t = self._t.get(int(mercado))
        if t is None:
            return float("nan"), None
        i = int(np.searchsorted(t, t_ms, side="right")) - 1
        return (float(self._f[int(mercado)][i]), int(t_ms - t[i])) if i >= 0 else (float("nan"), None)


# ====================================================================================================================
# 5. MÉTRICAS: información, tomador, guarda
# ====================================================================================================================
def ic90(v, B=5000):
    r = F4.ic90_dias(list(v))
    return None if r is None else (round(r[0], 5), round(r[1], 5))


def boot_cluster(o, clave, B=2000):
    g = o.groupby(clave)["pnl"].agg(["sum", "count"])
    if len(g) < 3:
        return None
    s, c = g["sum"].to_numpy(), g["count"].to_numpy()
    idx = np.random.default_rng(1).integers(0, len(s), (B, len(s)))
    b = s[idx].sum(1) / c[idx].sum(1)
    return round(float(np.percentile(b, 5)), 3), round(float(np.percentile(b, 95)), 3)


def econ_tomador(df, dhat, M, solo_eventos=True, limite_t0=False, stake=STAKE_EUR):
    """Tomador al ask REAL a +355 ms: comprar el lado con FV_lado - ask(t+355) >= M. Primera entrada CRONOLÓGICA por
    mercado-lado. Comisión: comision_cripto (acierto/(p(1+fee(1-p))) - 1). limite_t0: solo si ask(llegada) <= ask(decisión)."""
    import pandas as pd
    fv = np.clip(df["mid5"].to_numpy() + np.asarray(dhat), 0.01, 0.99)
    base = np.ones(len(df), dtype=bool) if not solo_eventos else (df["tipo"].to_numpy() != "grid")
    pie = []
    for lado in ("Up", "Down"):
        if lado == "Up":
            ask, f, ask0, sz, gana = df["ask5_lat"].to_numpy(), fv, df["ask5"].to_numpy(), df["asz_lat"].to_numpy(), \
                df["y"].to_numpy() == 1
        else:
            ask, f, ask0, sz, gana = 1 - df["bid5_lat"].to_numpy(), 1 - fv, 1 - df["bid5"].to_numpy(), \
                df["bsz_lat"].to_numpy(), df["y"].to_numpy() == 0
        with np.errstate(invalid="ignore"):
            ok = base & np.isfinite(ask) & (ask > 0) & (ask < 1) & ((f - ask) >= M)
            if limite_t0:
                ok &= ask <= ask0 + 1e-9
        ix = np.where(ok)[0]
        if len(ix) == 0:
            continue
        pie.append(pd.DataFrame({
            "i": ix, "dia": df["dia"].to_numpy()[ix], "moneda": df["moneda"].to_numpy()[ix],
            "mercado": df["mercado"].to_numpy()[ix], "cierre": df["cierre"].to_numpy()[ix], "lado": lado,
            "t": df["t"].to_numpy()[ix], "tipo": df["tipo"].to_numpy()[ix], "T": df["T"].to_numpy()[ix],
            "bn500": df["bn500"].to_numpy()[ix], "ask": ask[ix], "ask0": ask0[ix], "f": f[ix], "sz": sz[ix],
            "gana": gana[ix].astype(int)}))
    cols = ["i", "dia", "moneda", "mercado", "cierre", "lado", "t", "tipo", "T", "bn500", "ask", "ask0", "f", "sz", "gana"]
    if not pie:
        return pd.DataFrame(columns=cols + ["pnl", "evt", "depth_val", "dask", "hora"])
    o = pd.concat(pie, ignore_index=True).sort_values(["t", "i"], kind="mergesort")
    o = o.drop_duplicates(subset=["mercado", "lado"], keep="first").reset_index(drop=True)
    o["pnl"] = o["gana"] / (o["ask"] * (1 + FEE_CRIPTO * (1 - o["ask"]))) - 1.0
    o["evt"] = np.where(o["bn500"].abs() >= BN_BPS, "BN", np.where(o["tipo"] == "evento15", "15M", "otro"))
    o["depth_val"] = o["sz"] * o["ask"]
    o["dask"] = o["ask"] - o["ask0"]
    o["hora"] = (o["t"] // 3_600_000) % 24
    return o


def evaluar_curva(res):
    """res {M: (n, EV)} -> (monotona, M_max_valido). Monótona: EV no decreciente en los M con n >= N_MIN_M (>=2 puntos)."""
    pts = [(M, n, ev) for M, (n, ev) in sorted(res.items()) if n >= N_MIN_M]
    mono = len(pts) >= 2 and all(b[2] >= a[2] - MONOTONIA_TOL for a, b in zip(pts, pts[1:]))
    return mono, (pts[-1][0] if pts else None)


def curva_M(df, dhat, grid=REJILLA_M, **kw):
    """-> ({M: (n, EV)}, monotona, M_max_valido) con el tomador sobre la rejilla fija de M."""
    res = {}
    for M in grid:
        o = econ_tomador(df, dhat, M, **kw)
        res[M] = (int(len(o)), float(o["pnl"].mean()) if len(o) else float("nan"))
    mono, mmax = evaluar_curva(res)
    return res, mono, mmax


def linea_stats(o, tag):
    """Resumen de un conjunto de entradas (unidad mercado-lado) con n, EV, sin top3, mediana, sin mejor día, ICs."""
    if len(o) == 0:
        return f"{tag}: n=0"
    s = o["pnl"].sort_values(ascending=False)
    pdia = o.groupby("dia")["pnl"].agg(["count", "mean", "sum"])
    mejor = pdia["sum"].idxmax()
    sin_mejor = o[o["dia"] != mejor]["pnl"].mean() if len(pdia) > 1 else float("nan")
    sin3 = s.iloc[3:].mean() if len(s) > 3 else float("nan")
    return (f"{tag}: n={len(o)} mercados={o['mercado'].nunique()} EV/€ {o['pnl'].mean():+.3f} hit {o['gana'].mean():.3f} "
            f"ask_med {o['ask'].mean():.3f} | sin_top3 {sin3:+.3f} mediana {o['pnl'].median():+.3f} sin_mejor_día {sin_mejor:+.3f} | "
            f"IC90 mercado {boot_cluster(o, 'mercado')} cierre {boot_cluster(o, 'cierre')} días {ic90(pdia['mean'])} | "
            + " ".join(f"{d[5:]}:{int(r['count'])}/{r['mean']:+.3f}" for d, r in pdia.iterrows()))


def _w_mercado(df):
    return 1.0 / df.groupby("mercado")["mercado"].transform("count").to_numpy()


INFO_COLS = ["moneda", "dia", "n", "n_mercados", "r2_3s", "r2_355", "brier_fv", "brier_mid0", "brier_mid70", "brier_mid355",
             "mse_fv", "mse_mid355", "mse_mid0", "mse_mid70"]


def por_dia(t):
    """Una fila por día (media ponderada por n entre las monedas de la tabla) como lista de dicts."""
    res = []
    for _, g in t.groupby("dia"):
        w = g["n"].to_numpy(dtype=float)
        res.append({c: float(np.average(g[c].to_numpy(dtype=float), weights=w)) for c in INFO_COLS[4:]})
    return res


def info_por_dia(ev, dhat):
    """Métricas de información por (moneda, día) sobre eventos, MUESTRA COMÚN con m5_70, m5_355, m5_3000 disponibles."""
    import pandas as pd
    fv = np.clip(ev["mid5"].to_numpy() + dhat, 0.01, 0.99)
    filas = []
    ev = ev.assign(_fv=fv, _dh=dhat)
    com = ev[ev[["m5_70", "m5_355", "m5_3000"]].notna().all(axis=1)]
    for (co, d), g in com.groupby(["moneda", "dia"]):
        w = _w_mercado(g)
        y = g["y"].to_numpy()
        br = lambda x: float(np.sum(w * (np.asarray(x) - y) ** 2) / w.sum())  # noqa: E731
        m3, m355, m70, m0 = (g[c].to_numpy() for c in ("m5_3000", "m5_355", "m5_70", "mid5"))
        fvg = g["_fv"].to_numpy()
        filas.append({"moneda": co, "dia": d, "n": len(g), "n_mercados": g["mercado"].nunique(),
                      "r2_3s": r2(m3 - m0, g["_dh"].to_numpy()),
                      "r2_355": r2(m355 - m0, g["_dh"].to_numpy()),
                      "brier_fv": br(fvg), "brier_mid0": br(m0), "brier_mid70": br(m70), "brier_mid355": br(m355),
                      "mse_fv": float(np.mean((m3 - fvg) ** 2)), "mse_mid355": float(np.mean((m3 - m355) ** 2)),
                      "mse_mid0": float(np.mean((m3 - m0) ** 2)), "mse_mid70": float(np.mean((m3 - m70) ** 2))})
    return pd.DataFrame(filas, columns=INFO_COLS)


def resumen_info(t, etiqueta):
    """Texto de una tabla info_por_dia para una moneda (o 'POOL' = todas)."""
    if t is None or len(t) == 0:
        return [f"  {etiqueta}: sin datos"]
    n = int(t["n"].sum())
    dd = por_dia(t)
    pd_ = lambda c: [x[c] for x in dd]  # noqa: E731
    dif = lambda a, b: [x[a] - x[b] for x in dd]  # noqa: E731
    mm = lambda c: round(float(np.mean(pd_(c))), 6)  # noqa: E731
    mdif = lambda a, b: float(np.mean(dif(a, b)))  # noqa: E731
    return [f"  {etiqueta}: n_eventos={n} días={len(dd)} | R² uncentrado Δ̂→Δmid3s {mm('r2_3s'):+.4f} IC90 {ic90(pd_('r2_3s'))}; "
            f"Δ̂→Δmid(+355) {mm('r2_355'):+.4f}",
            f"      Brier: FV {mm('brier_fv'):.5f} | mid(t) {mm('brier_mid0'):.5f} | mid(+70) {mm('brier_mid70'):.5f} | mid(+355) "
            f"{mm('brier_mid355'):.5f}",
            f"      ΔBrier FV−mid(t) {mdif('brier_fv', 'brier_mid0'):+.5f} IC90 {ic90(dif('brier_fv', 'brier_mid0'))} | "
            f"FV−mid(+70) {mdif('brier_fv', 'brier_mid70'):+.5f} IC90 {ic90(dif('brier_fv', 'brier_mid70'))} | "
            f"FV−mid(+355) {mdif('brier_fv', 'brier_mid355'):+.5f} IC90 {ic90(dif('brier_fv', 'brier_mid355'))}",
            f"      MSE vs mid(+3s): FV {mm('mse_fv'):.6f} | mid(t) {mm('mse_mid0'):.6f} | mid(+70) {mm('mse_mid70'):.6f} | "
            f"mid(+355) {mm('mse_mid355'):.6f}; FV−mid(+355) {mdif('mse_fv', 'mse_mid355'):+.7f} IC90 "
            f"{ic90(dif('mse_fv', 'mse_mid355'))} (negativo = FV predice mejor que el libro al llegar)"]


def auc(score, evento):
    from scipy.stats import rankdata
    evento = np.asarray(evento, dtype=bool)
    n1, n0 = int(evento.sum()), int((~evento).sum())
    if n1 == 0 or n0 == 0:
        return float("nan")
    r = rankdata(score)
    return float((r[evento].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def guarda_diag(ev, dhat, gs=(0.0, 0.01, 0.02)):
    """Diagnóstico de la guarda del maker: puja en el mejor bid del lado. 'adverso' = el mid(+3s) cae por debajo de nuestro
    precio. Puntuación de peligro = precio − FV_lado. Línea base A = mid−precio (solo semi-spread), B = precio − (mid+rb500)
    (FV ingenuo con el último movimiento de Binance). AUC por (moneda,día), IC90 por días de la diferencia."""
    fv = np.clip(ev["mid5"].to_numpy() + dhat, 0.01, 0.99)
    d = ev.assign(_fv=fv)
    d = d[d["m5_3000"].notna()]
    out = {}
    for co, gc in list(d.groupby("moneda")) + [("POOL", d)]:
        difs_fv, difs_b, aucs_fv, base_rates, flags = [], [], [], [], {g: [] for g in gs}
        for dia, g in gc.groupby("dia"):
            fvg = g["_fv"].to_numpy()
            # lado Up: puja en bid5; lado Down: puja en 1-ask5 (en términos del token Down)
            pr_up, pr_dn = g["bid5"].to_numpy(), 1 - g["ask5"].to_numpy()
            m3 = g["m5_3000"].to_numpy()
            adv = np.concatenate([m3 < pr_up, (1 - m3) < pr_dn])
            s_fv = np.concatenate([pr_up - fvg, pr_dn - (1 - fvg)])
            rb = g["rb500"].to_numpy()
            s_b = np.concatenate([pr_up - (g["mid5"].to_numpy() + rb), pr_dn - (1 - g["mid5"].to_numpy() - rb)])
            a_f, a_b = auc(s_fv, adv), auc(s_b, adv)
            if a_f == a_f and a_b == a_b:
                aucs_fv.append(a_f)
                difs_fv.append(a_f - 0.5)
                difs_b.append(a_f - a_b)
            base_rates.append(float(adv.mean()))
            for gg in gs:
                fl = -s_fv < gg
                flags[gg].append((int(fl.sum()), float(adv[fl].mean()) if fl.any() else float("nan"),
                                  float(adv[~fl].mean()) if (~fl).any() else float("nan"), len(adv)))
        out[co] = {"auc_fv": float(np.mean(aucs_fv)) if aucs_fv else float("nan"), "ic_auc_fv_vs_azar": ic90(difs_fv),
                   "ic_auc_fv_menos_naive": ic90(difs_b), "tasa_adverso": float(np.mean(base_rates)) if base_rates else float("nan"),
                   "flags": {g: v for g, v in flags.items()}, "dias": len(aucs_fv)}
    return out


# ====================================================================================================================
# 6. ENTRENAR / JUZGAR
# ====================================================================================================================
def entrenar(out, monedas=MONEDAS, desc_train=DESC_TRAIN, desc_val=DESC_VAL, incluir_truncados=False,
             val_desde_cierre=None, construir=True):
    """Elige hiperparámetros en DESC (entrena desc_train, valida desc_val en eventos de BTC) y reajusta el elegido sobre
    todo DESC. Serializa en fv5_modelo_<hash>/. Devuelve (ruta, meta)."""
    info = []
    dias = list(dict.fromkeys(list(desc_train) + list(desc_val)))
    df = cargar(dias, out, monedas, grid_stride=GRID_STRIDE, incluir_truncados=incluir_truncados, construir=construir,
                info=info)
    if df is None or df.empty:
        raise RuntimeError("DESC sin filas: nada que entrenar")
    if val_desde_cierre is not None:      # SOLO humo de un día: corte temporal dentro del día
        tr, va = df[df["cierre"] < val_desde_cierre], df[df["cierre"] >= val_desde_cierre]
    else:
        tr, va = df[df["dia"].isin(desc_train)], df[df["dia"].isin(desc_val)]
    log(f"DESC: train {len(tr)} filas, val {len(va)} filas; RSS {rss_mb()} MB")
    vev = va[(va["tipo"] != "grid") & va["dy"].notna()]
    vbtc = vev[vev["moneda"] == "BTC"]
    if vbtc.empty:
        raise RuntimeError("validación sin eventos de BTC: no se puede elegir (diseño en BTC)")
    tabla, ajustes = [], {}
    for nombre, ambito, cfg in CANDIDATOS:
        t0 = time.time()
        mod = ajustar(tr, nombre, ambito, cfg)
        ajustes[nombre] = mod
        r_btc = r2(vbtc["dy"].to_numpy(), predecir(mod, vbtc))
        r_all = r2(vev["dy"].to_numpy(), predecir(mod, vev))
        tabla.append({"candidato": nombre, "ambito": ambito, "r2_val_btc_eventos": r_btc, "r2_val_todas_eventos": r_all,
                      "n_train": mod["n_train"], "n_val_btc": int(len(vbtc)), "segundos": round(time.time() - t0, 1)})
        log(f"  candidato {nombre}: R² val BTC {r_btc:+.4f} (n={len(vbtc)}), todas {r_all:+.4f}, {tabla[-1]['segundos']} s")
    mejor = max(tabla, key=lambda x: (x["r2_val_btc_eventos"] if x["r2_val_btc_eventos"] == x["r2_val_btc_eventos"] else -9))
    elegido = mejor["candidato"]
    mval = ajustes[elegido]
    curva, mono, mmax = curva_M(vbtc, predecir(mval, vbtc))
    ev_mmax = curva[mmax][1] if mmax is not None else float("nan")
    apto = bool(mono and mmax is not None and ev_mmax > 0)
    M_cong = mmax if apto else None
    log(f"ELEGIDO en DESC: {elegido}; curva M (BTC val) {curva}; monótona={mono}; tomador={'APTO M=' + str(M_cong) if apto else 'NO_APTO'}")
    # reajuste final sobre TODO DESC con lo elegido
    ambito, cfg = next((a, c) for n, a, c in CANDIDATOS if n == elegido)
    final = ajustar(df, elegido, ambito, cfg)
    raw = pickle.dumps(final, protocol=4)
    h = hashlib.sha256(raw).hexdigest()[:16]
    ruta = Path(out) / f"fv5_modelo_{h}"
    previo = (ruta / "modelo.pkl").read_bytes() if (ruta / "modelo.pkl").exists() else None
    ruta.mkdir(parents=True, exist_ok=True)
    meta = {"hash": h, "version": VERSION, "seed": SEED, "elegido": elegido, "ambito": ambito, "cfg": final["cfg"],
            "rasgos": final["rasgos"], "n_train_final": final["n_train"], "desc_train": list(desc_train),
            "desc_val": list(desc_val), "val_desde_cierre": val_desde_cierre,
            "cumple_protocolo": bool(list(desc_train) == DESC_TRAIN and list(desc_val) == DESC_VAL and val_desde_cierre is None),
            "tabla_candidatos": tabla, "curva_M_desc_val_btc": {str(k): v for k, v in curva.items()},
            "curva_monotona": bool(mono), "M_congelado": M_cong, "tomador_apto": apto, "rejilla_M": list(REJILLA_M),
            "n_min_M": N_MIN_M, "grid_stride_train": GRID_STRIDE,
            "monedas": list(monedas), "dias_info": [{k: m.get(k) for k in ("dia", "estado", "excluido", "sha256", "filas")}
                                                    for m in info],
            "sklearn": __import__("sklearn").__version__, "numpy": np.__version__,
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "creado_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    if previo is not None:
        meta["reproducido_byte_a_byte"] = (previo == raw)
        log(f"modelo {h} ya existía: mismo contenido byte a byte = {previo == raw}")
    else:
        meta["reproducido_byte_a_byte"] = None
        (ruta / "modelo.pkl").write_bytes(raw)
    escribir_atomico(ruta / "meta.json", json.dumps(meta, indent=1))
    return ruta, meta


def ventana_fecha(desde, hasta):
    d, out = date.fromisoformat(desde), []
    while d <= date.fromisoformat(hasta):
        out.append(d.isoformat())
        d += timedelta(days=1)
    return out


def juzgar(modelo, out, dias, monedas=MONEDAS, incluir_truncados=False, construir=True, permitir_desc=False):
    """Informe OOS con el modelo CONGELADO (no reentrena). Devuelve (lineas, resumen_json)."""
    import pandas as pd
    if not permitir_desc and any(d in (list(modelo.meta["desc_train"]) + list(modelo.meta["desc_val"])) for d in dias):
        raise ValueError("juzgar: algún día pedido pertenece al DESC del modelo (usar --permitir-desc solo en humo)")
    info = []
    df = cargar(dias, out, monedas, solo_eventos=True, incluir_truncados=incluir_truncados, construir=construir, info=info)
    ok_dias = [m["dia"] for m in info if m.get("estado") in ("COMPLETE", "PARTIAL") and not m.get("excluido")]
    L = []
    esp = 288 * len(monedas) * len(dias)
    got = sum(sum(v.get("mercados_con_filas", 0) for v in m.get("cobertura", {}).values()) for m in info if not m.get("excluido"))
    trunc = [m["dia"] for m in info if m.get("truncado")]
    baja = {m["dia"]: m.get("monedas_cobertura_baja") for m in info if m.get("monedas_cobertura_baja")}
    perdidos = [m["dia"] for m in info if m.get("estado") == "MISSING"]
    sin = {k: sum(sum(v.get(k, 0) for v in m.get("cobertura", {}).values()) for m in info)
           for k in ("sin_ref", "sin_desenlace", "sin_libro5", "sin_libro15", "puntos_sin_rasgos")}
    veredicto = "COMPLETE" if (not trunc and not baja and not perdidos and df is not None) else "PARTIAL"
    L.append(f"COBERTURA: días pedidos {len(dias)} usados {len(ok_dias)} | mercados-moneda con filas {got}/{esp} esperados | "
             f"faltan (sin registro): {perdidos or 'ninguno'} | gz TRUNCADOS: {trunc or 'ninguno'}"
             f"{' (EXCLUIDOS)' if trunc and not incluir_truncados else ''} | cobertura baja: {baja or 'ninguna'} | "
             f"descartados por falta de ref/desenlace/libro: {sin} | VEREDICTO {veredicto}")
    L.append(f"FV v5 — modelo {modelo.hash} ({modelo.meta['elegido']}, protocolo DESC "
             f"{'OK' if modelo.meta['cumple_protocolo'] else 'NO (humo)'}); DESC train {modelo.meta['desc_train'][0]}.."
             f"{modelo.meta['desc_train'][-1]} val {modelo.meta['desc_val']}; juicio {dias[0]}..{dias[-1]}; monedas {list(monedas)}")
    if df is None or df.empty:
        L.append("sin filas OOS: nada que juzgar")
        return L, {"veredicto": veredicto, "modelo": modelo.hash}
    df = df[df["moneda"].isin(monedas)].reset_index(drop=True)
    dh = modelo.dhat(df)
    rng = np.random.default_rng(SEED + 3)
    dh_perm = dh.copy()
    for _, ix in df.groupby(["dia", "moneda"]).indices.items():
        dh_perm[ix] = rng.permutation(dh[ix])
    resumen = {"modelo": modelo.hash, "veredicto": veredicto, "dias": dias}
    # ---- 2. información
    L.append("\n== 2. INFORMACIÓN (eventos; muestra común con mid(+70), mid(+355), mid(+3s); ponderado 1/mercado)")
    infos = {"REAL": info_por_dia(df, dh), "PERMUTADO": info_por_dia(df, dh_perm), "INVERTIDO": info_por_dia(df, -dh)}
    for co in list(monedas) + ["POOL"]:
        tr_ = infos["REAL"] if co == "POOL" else infos["REAL"][infos["REAL"]["moneda"] == co]
        L += resumen_info(tr_, f"{co} REAL")
        if co in ("BTC", "POOL"):
            for pl in ("PERMUTADO", "INVERTIDO"):
                tp_ = infos[pl] if co == "POOL" else infos[pl][infos[pl]["moneda"] == co]
                L += resumen_info(tp_, f"{co} placebo {pl}")
    # ---- 3. guarda
    L.append("\n== 3. GUARDA DEL MAKER (diagnóstico; el valor económico lo mide el simulador H26): puja en el mejor bid, "
             "adverso = mid(+3s) por debajo de nuestro precio; AUC de (precio−FV) y diferencia frente al FV ingenuo mid+rb500")
    gd = guarda_diag(df, dh)
    for co, v in gd.items():
        fl = " | ".join(f"g={g}: marcadas {sum(x[0] for x in vv)}/{sum(x[3] for x in vv)} P(adv|marca) "
                        f"{nanmedia([x[1] for x in vv]):.3f} P(adv|no) {nanmedia([x[2] for x in vv]):.3f}"
                        for g, vv in v["flags"].items() if vv)
        L.append(f"  {co}: días={v['dias']} AUC_FV {v['auc_fv']:.4f} (IC90 AUC−0,5 por días {v['ic_auc_fv_vs_azar']}); "
                 f"AUC_FV−AUC_naive IC90 {v['ic_auc_fv_menos_naive']}; tasa adverso {v['tasa_adverso']:.3f} | {fl}")
    resumen["guarda"] = {co: {k: v[k] for k in ("auc_fv", "ic_auc_fv_vs_azar", "ic_auc_fv_menos_naive")} for co, v in gd.items()}
    # ---- 4. tomador
    L.append("\n== 4. TOMADOR (uso secundario): ask REAL a +355 ms, comisión comision_cripto, 1ª entrada cronológica por mercado-lado")
    M = modelo.meta["M_congelado"]
    L.append(f"  DESC: curva M (BTC val) {modelo.meta['curva_M_desc_val_btc']} monótona={modelo.meta['curva_monotona']} -> "
             f"{'APTO, M congelado = ' + str(M) if modelo.meta['tomador_apto'] else 'NO_APTO (sin M congelado: lo siguiente es DIAGNÓSTICO a M=0,05, no un juicio)'}")
    Mj = M if M is not None else 0.05
    curva, mono, _ = curva_M(df, dh)
    L.append(f"  OOS curva EV(M) (n, EV/€): { {k: (v[0], round(v[1], 3)) for k, v in curva.items()} } monótona OOS={mono}")
    o = econ_tomador(df, dh, Mj)
    L.append("  " + linea_stats(o, f"M={Mj} TODAS las monedas"))
    resumen["tomador"] = {"M": Mj, "congelado": M is not None, "n": int(len(o)), "ev": float(o["pnl"].mean()) if len(o) else None}
    for co in monedas:
        L.append("    " + linea_stats(o[o["moneda"] == co], f"{co}"))
    ob = o[o["moneda"] == "BTC"]
    if len(o):
        L.append("  Cortes (todas las monedas):")
        for k, g in o.groupby("evt"):
            L.append("    tipo " + linea_stats(g, f"{k}"))
        for k, g in o.groupby("lado"):
            L.append("    lado " + linea_stats(g, f"{k}"))
        o["hb"] = (o["hora"] // 6) * 6
        for k, g in o.groupby("hb"):
            L.append("    hora UTC " + linea_stats(g, f"{int(k):02d}-{int(k) + 5:02d}"))
        o["Tb"] = pd.cut(o["T"], [0, 30, 60, 120, 200, 300])
        for k, g in o.groupby("Tb", observed=True):
            L.append("    T(s) " + linea_stats(g, f"{k}"))
        hs = o.groupby("hora")["pnl"].sum()
        L.append(f"    horas con PnL>0 {(hs > 0).sum()}/{len(hs)}; EV sin las 3 mejores horas "
                 f"{o[~o['hora'].isin(hs.nlargest(3).index)]['pnl'].mean():+.3f}")
        okp = o["depth_val"] >= STAKE_EUR
        L.append(f"  Profundidad nivel 1 al llegar (registro q): con depth>=stake {STAKE_EUR} €: {okp.mean():.3f} de las entradas "
                 f"(n={int(okp.sum())}/{len(o)}); " + linea_stats(o[okp], "EV solo con profundidad suficiente"))
        L.append("  Ask de llegada vs decisión: " + " | ".join(
            f"{nm}: n={len(g)} EV {g['pnl'].mean():+.3f}" for nm, g in
            (("llegada<decisión (cae hacia nosotros)", o[o["dask"] < -1e-9]), ("igual", o[o["dask"].abs() <= 1e-9]),
             ("llegada>decisión", o[o["dask"] > 1e-9])) if len(g)))
        ol = econ_tomador(df, dh, Mj, limite_t0=True)
        L.append("  " + linea_stats(ol, "variante límite=ask(t) (no paga más que lo visto en la decisión)"))
        og = econ_tomador(df, dh, Mj, solo_eventos=False)
        L.append(f"  (info) incluyendo rejilla: n={len(og)} EV {og['pnl'].mean() if len(og) else float('nan'):+.3f}")
    # placebos económicos
    L.append("  Placebos económicos a M=%s:" % Mj)
    pls = {"FV=mid(t)": np.zeros(len(df)), "invertido": -dh}
    for nm, p in pls.items():
        op = econ_tomador(df, p, Mj)
        L.append(f"    {nm}: n={len(op)} EV {op['pnl'].mean() if len(op) else float('nan'):+.3f}")
    evp = []
    for k in range(20):
        r_ = np.random.default_rng(SEED + 100 + k)
        pp = dh.copy()
        for _, ix in df.groupby(["dia", "moneda"]).indices.items():
            pp[ix] = r_.permutation(dh[ix])
        op = econ_tomador(df, pp, Mj)
        evp.append(op["pnl"].mean() if len(op) else float("nan"))
    L.append(f"    permutado dentro de (día, moneda) x20: EV medio {nanmedia(evp):+.3f} rango [{nanmedia(evp, np.min):+.3f}, {nanmedia(evp, np.max):+.3f}]")
    po = econ_tomador(df, np.nan_to_num((df["m5_3000"] - df["mid5"]).to_numpy(), nan=0.0), Mj)
    L.append(f"    oráculo FV=mid(t+3s) (COTA SUPERIOR de lo que daría saber el futuro a 3 s): n={len(po)} "
             f"EV {po['pnl'].mean() if len(po) else float('nan'):+.3f}. 'FV=mid+L' (mid(+70), mid(+355)) como predictor: ver Brier/MSE de la sección 2.")
    # ---- 5. gates H34 (banderas, NO veredicto)
    L.append("\n== 5. GATES H34 (banderas informativas; no declaran rentabilidad)")
    if len(o):
        pdia = o.groupby("dia")["pnl"].mean()
        s = o["pnl"].sort_values(ascending=False)
        icd = ic90(pdia)
        hs = o.groupby("hora")["pnl"].sum()
        sin_bn = o[o["evt"] != "BN"]
        icb = ic90([x["brier_fv"] - x["brier_mid355"] for x in por_dia(infos["REAL"])]) if len(infos["REAL"]) else None
        flags = [
            ("≥5 días de OOS", len(pdia) >= 5, f"{len(pdia)} días"),
            ("IC90 por días >0", bool(icd and icd[0] > 0), f"{icd}"),
            ("EV sin top3 >0", bool(len(s) > 3 and s.iloc[3:].mean() > 0), f"{s.iloc[3:].mean() if len(s) > 3 else float('nan'):+.3f}"),
            ("curva M monótona (DESC y OOS)", bool(modelo.meta["curva_monotona"] and mono), f"DESC {modelo.meta['curva_monotona']} OOS {mono}"),
            ("sin depender de pocas horas (EV sin 3 mejores horas >0)", bool(o[~o['hora'].isin(hs.nlargest(3).index)]['pnl'].mean() > 0), ""),
            (f"profundidad nivel 1 ≥ stake en ≥{PROF_MIN:.0%}", bool((o["depth_val"] >= STAKE_EUR).mean() >= PROF_MIN),
             f"{(o['depth_val'] >= STAKE_EUR).mean():.3f}"),
            ("EV sin eventos Binance >0 (distinto del cementerio 'valor tras salto')", bool(len(sin_bn) and sin_bn["pnl"].mean() > 0),
             f"n={len(sin_bn)} EV {sin_bn['pnl'].mean() if len(sin_bn) else float('nan'):+.3f}"),
            ("EV real > máx placebo permutado", bool(len(o) and o["pnl"].mean() > nanmedia(evp, np.max)), f"{nanmedia(evp, np.max):+.3f}"),
            ("ΔBrier FV−mid(+355) IC90 por días <0", bool(icb and icb[1] < 0), f"{icb}"),
            ("tomador APTO en DESC", bool(modelo.meta["tomador_apto"]), ""),
        ]
        for nm, ok_, det in flags:
            L.append(f"  [{'SÍ' if ok_ else 'NO'}] {nm} {det}")
        resumen["gates"] = {nm: bool(ok_) for nm, ok_, _ in flags}
    else:
        L.append("  sin entradas del tomador: gates no evaluables")
    L.append("\nLIMITES: n de días OOS pequeño (IC por días indicativo con <5); duplicados de overlap de tramos no deduplicados "
             "(igual que v4); ref5 llega 1,3-1,8 s tras la apertura y la rejilla empieza a T=298 s (2,0 s): p90 cubierto; "
             "tomador usa el ask del nivel 1 al llegar (+355 ms) sin modelo de cola ni de profundidad multinivel; "
             "ninguna cifra es un juicio de rentabilidad: eso corresponde al validador estadístico y al red-team.")
    return L, resumen


def exportar_senal(modelo, out, dias, monedas=MONEDAS, construir=True, incluir_truncados=False):
    """fv5_senal_<hash>_<D>.csv.gz: moneda,mercado,cierre,t,tipo,fv_up,dhat sobre todos los puntos del dataset del día."""
    rutas = []
    for d in dias:
        df = cargar([d], out, monedas, construir=construir, incluir_truncados=incluir_truncados)
        if df is None:
            continue
        dh = modelo.dhat(df)
        fv = np.clip(df["mid5"].to_numpy() + dh, 0.01, 0.99)
        s = df[["moneda", "mercado", "cierre", "t", "tipo"]].assign(fv_up=np.round(fv, 6), dhat=np.round(dh, 6))
        dst = Path(out) / f"fv5_senal_{modelo.hash}_{d}.csv.gz"
        tmp = dst.with_name(dst.name + ".tmp")
        s.to_csv(tmp, index=False, compression="gzip")
        os.replace(tmp, dst)
        rutas.append(dst)
    return rutas


# ====================================================================================================================
# 7. CLI, manifiesto y guardas de recursos
# ====================================================================================================================
def mem_disponible_mb():
    try:
        for ln in open("/proc/meminfo"):
            if ln.startswith("MemAvailable"):
                return int(ln.split()[1]) // 1024
    except OSError:
        pass
    return None


def bloqueo(ahora=None, sin_guardas=False):
    """Motivo de BLOCKED o None: sin franja 06-09Z y con MemAvailable >= 1,5 GB (todo modo puede construir datasets)."""
    if sin_guardas:
        return None
    h = (ahora or datetime.now(timezone.utc)).hour
    if FRANJA_BLOQ[0] <= h < FRANJA_BLOQ[1]:
        return f"franja {FRANJA_BLOQ[0]:02d}-{FRANJA_BLOQ[1]:02d}Z: no se lanzan trabajos pesados"
    m = mem_disponible_mb()
    if m is not None and m < MIN_MEM_MB:
        return f"MemAvailable {m} MB < {MIN_MEM_MB} MB"
    return None


class Manifiesto:
    def __init__(self, out, modo, args, dias):
        self.dir = Path(out) / "fv5_runs" / f"fv5_{modo}_{time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())}_{os.getpid()}"
        self.dir.mkdir(parents=True, exist_ok=True)
        self.m = {"job_id": self.dir.name, "modo": modo, "script": Path(__file__).name,
                  "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "version": VERSION,
                  "args": {k: v for k, v in vars(args).items()}, "dias_pedidos": list(dias), "dias_ok": [], "dias_parciales": [],
                  "dias_ausentes": [], "dias_fallidos": {}, "entradas": {}, "inicio_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                  "fin_utc": None, "estado": "RUNNING", "comando": " ".join(sys.argv)}
        self.guardar()

    def entradas(self, dias):
        for d in dias:
            for pref in ("m15", "m5"):
                f = VOL / f"{pref}_registro" / f"{pref}_registro_{d}.csv.gz"
                if f.exists():
                    s = f.stat()
                    self.m["entradas"][f"{pref}_{d}"] = {"bytes": s.st_size, "mtime": s.st_mtime_ns}
        self.guardar()

    def guardar(self):
        escribir_atomico(self.dir / "run_manifest.json", json.dumps(self.m, indent=1, default=str))

    def cerrar(self, estado):
        self.m["estado"] = estado
        self.m["fin_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        self.m["rss_pico_mb"] = rss_mb()
        self.guardar()


def construir_dias(dias, monedas, out, man, recorte=None):
    for d in dias:
        try:
            c, m = construir_dia(d, monedas, out, recorte)
        except Exception as e:      # un día roto no tumba el resto ni deja el manifiesto en RUNNING
            man.m["dias_fallidos"][d] = f"{type(e).__name__}: {e}"
            log(f"  {d}: FALLIDO {man.m['dias_fallidos'][d]}")
            man.guardar()
            continue
        if c is None:
            man.m["dias_ausentes"].append(d)
            log(f"  {d}: AUSENTE (sin registro)")
        else:
            (man.m["dias_parciales"] if m["estado"] == "PARTIAL" else man.m["dias_ok"]).append(d)
            log(f"  {d}: {m['estado']} filas={m['filas']} truncado={m['truncado']} cobertura_baja={m['monedas_cobertura_baja']} "
                f"{m['segundos']} s RSS {m['rss_pico_mb']} MB")
        man.guardar()                                  # resumen parcial tras cada día


def estado_final(man):
    f = man.m
    if f["dias_fallidos"] and not (f["dias_ok"] or f["dias_parciales"]):
        return "FAILED"
    return "COMPLETE" if not (f["dias_fallidos"] or f["dias_parciales"] or f["dias_ausentes"]) else "PARTIAL"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("modo", choices=["dataset", "entrenar", "juzgar", "senal", "todo"])
    ap.add_argument("--dias")
    ap.add_argument("--monedas", default=",".join(MONEDAS))
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--modelo")
    ap.add_argument("--oos-desde", default=OOS_DESDE)
    ap.add_argument("--oos-hasta", default=None)
    ap.add_argument("--recorte")
    ap.add_argument("--incluir-truncados", action="store_true")
    ap.add_argument("--permitir-desc", action="store_true", help="SOLO humo: juzgar días del DESC del modelo")
    ap.add_argument("--desc-train", help="SOLO humo: sustituye DESC_TRAIN")
    ap.add_argument("--desc-val", help="SOLO humo: sustituye DESC_VAL")
    ap.add_argument("--val-desde-cierre", type=int, help="SOLO humo de un día: corte temporal de validación (cierre epoch s)")
    ap.add_argument("--sin-guardas", action="store_true", help="SOLO humo/tests: ignora franja y RAM")
    a = ap.parse_args(argv)
    out = Path(a.out)
    monedas = tuple(a.monedas.split(","))
    hasta = a.oos_hasta or (date.today() - timedelta(days=1)).isoformat()
    dtr = a.desc_train.split(",") if a.desc_train else DESC_TRAIN
    dva = a.desc_val.split(",") if a.desc_val else DESC_VAL
    oos = ventana_fecha(a.oos_desde, hasta)
    recorte = tuple(int(x) for x in a.recorte.split("-")) if a.recorte else None
    dias = a.dias.split(",") if a.dias else (dtr + dva + oos if a.modo in ("todo",) else
                                              oos if a.modo in ("juzgar", "senal") else dtr + dva)
    man = Manifiesto(out, a.modo, a, dias)
    motivo = bloqueo(sin_guardas=a.sin_guardas)
    if motivo:
        log(f"BLOCKED: {motivo}")
        man.m["motivo_bloqueo"] = motivo
        man.cerrar("BLOCKED")
        print(f"ESTADO BLOCKED ({motivo}) manifiesto {man.dir / 'run_manifest.json'}")
        return 2
    man.entradas(dias)
    log(f"INICIO {a.modo} dias={dias} monedas={monedas} out={out} RSS {rss_mb()} MB; MemAvailable {mem_disponible_mb()} MB")
    try:
        if a.modo == "dataset":
            construir_dias(dias, monedas, out, man, recorte)
        elif a.modo == "entrenar":
            ruta, meta = entrenar(out, monedas, dtr, dva, a.incluir_truncados, a.val_desde_cierre)
            man.m["modelo"] = meta["hash"]
            print(f"HASH {meta['hash']} {ruta} reproducido_byte_a_byte={meta['reproducido_byte_a_byte']}")
        elif a.modo == "senal":
            mdl = FVModelo.cargar(a.modelo, out)
            for r_ in exportar_senal(mdl, out, dias, monedas, incluir_truncados=a.incluir_truncados):
                log(f"señal {r_}")
        elif a.modo in ("juzgar", "todo"):
            if a.modo == "todo":
                construir_dias(dias, monedas, out, man)
                ruta, meta = entrenar(out, monedas, dtr, dva, a.incluir_truncados, a.val_desde_cierre, construir=False)
                man.m["modelo"] = meta["hash"]
                log(f"HASH {meta['hash']} reproducido_byte_a_byte={meta['reproducido_byte_a_byte']}")
                mdl = FVModelo.cargar(ruta, out)
            else:
                mdl = FVModelo.cargar(a.modelo, out)
            oos = a.dias.split(",") if (a.dias and a.modo == "juzgar") else oos
            lineas, res = juzgar(mdl, out, oos, monedas, a.incluir_truncados, construir=(a.modo == "juzgar"),
                                 permitir_desc=a.permitir_desc)
            txt = "\n".join(lineas)
            print(txt)
            escribir_atomico(out / f"fv5_informe_{mdl.hash}_{oos[0]}_{oos[-1]}.txt", txt + "\n")
            escribir_atomico(out / f"fv5_informe_{mdl.hash}_{oos[0]}_{oos[-1]}.json", json.dumps(res, indent=1, default=str))
            man.m["informe"] = str(out / f"fv5_informe_{mdl.hash}_{oos[0]}_{oos[-1]}.txt")
            if res.get("veredicto") == "PARTIAL":
                man.m["dias_parciales"] = man.m["dias_parciales"] or ["ver línea COBERTURA del informe"]
    except Exception as e:
        man.m["excepcion"] = f"{type(e).__name__}: {e}"
        man.cerrar("FAILED")
        log(f"FAILED {man.m['excepcion']}")
        raise
    est = estado_final(man)
    man.cerrar(est)
    log(f"FIN estado={est} RSS pico {rss_mb()} MB; manifiesto {man.dir / 'run_manifest.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
