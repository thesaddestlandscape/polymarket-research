#!/usr/bin/env python3
"""wallet_first_buy_fwd_tracker.py -- "seguir wallets informadas EMPEZANDO a comprar", validación
FORWARD diaria (25-Sep, Javi: "construye"). Solo lectura del firehose; nunca envía órdenes.

Idea: no copiar a las ballenas "a nuestro precio" con un rezago de horas, sino entrar L segundos
después de la PRIMERA compra de una wallet en un mercado 5/15min (evento = (wallet, mercado, lado),
primera compra), al precio del siguiente trade tras L s (proxy del ask), reteniendo a resolución
(fee 7 % sobre ganancia). Seleccionar wallets con datos ANTERIORES y medirlas después:
  - Entrenamiento: agregados por wallet (n, suma EV, suma EV^2 con L=1 s) de los TRAIN_DIAS días previos.
  - Selección CONGELADA antes del día de test: n>=MIN_N, EV medio>0 y t>=T_MIN.
  - Test: eventos de esas wallets el día D, EV a L=0,3/1/3 s.
Hallazgo del backtest de 25-Sep (21-24 Sep, 18k wallets, 1,3M eventos): las wallets seleccionadas dan
+0,10 EUR/EUR forward (t=4, iid) PERO: top5 wallets = 84 % del EV, sin ellas +0,02 (t=1,1); t por
clúster de mercado = 1,6; el EV vive en longshots (pf<0,3: +0,3..+1,4; pf 0,4-0,9: -0,03..-0,11) y
en tickets <10 $. Es decir, NO robusto todavía. Este tracker lo mide día a día con esas métricas
honestas; solo se plantea un ejecutor si el pool de días de test lo supera (ver veredicto).
Salidas (data/shadow/wallet_first_buy/): agg_YYYY-MM-DD.json, test_YYYY-MM-DD.csv;
data/shadow/wallet_first_buy_fwd.json y su historial jsonl. Uso: [--dia YYYY-MM-DD] [--backfill FROM TO].
"""
import bisect
import collections
import csv
import gzip
import json
import math
import os
import re
import statistics
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from bootstrap_dias import bootstrap_ic90_dias as _bootstrap_ic90_dias  # noqa: E402
# /code-review 28-Sep: extraído a bootstrap_dias.py -- esta misma función vivía
# duplicada byte a byte en buscador_grietas_polymarket.py, riesgo real de que un
# fix al percentil se aplicara en una copia y no en la otra.

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
DIR = REPO / "data" / "shadow" / "wallet_first_buy"
OUT = REPO / "data" / "shadow" / "wallet_first_buy_fwd.json"
HIST = REPO / "data" / "shadow" / "wallet_first_buy_fwd_historial.jsonl"
FEE = 0.07
LS = [0.3, 1.0, 3.0]
LSEL = 1.0
TRAIN_DIAS, MIN_N, T_MIN = 3, 15, 2.0
PF_LO, PF_HI = 0.03, 0.97
VEREDICTO_MIN_DIAS, VEREDICTO_T_CLUSTER, VEREDICTO_EX_TOP5, VEREDICTO_MERCADOS = 3, 2.5, 0.03, 300
VEREDICTO_T_SIN_TOP5 = 2.0   # t por clúster de mercado del EV SIN las 5 mejores wallets ex post
# 28-Sep: mismos umbrales que el resto del proyecto (n>=15 mínimo absoluto de CLAUDE.md,
# n>=40 estándar de promoción) -- la cobertura de ask real es MUCHO menor que la del proxy
# (el observador solo lleva corriendo desde 25-Sep), así que el piso de n es más bajo que
# VEREDICTO_MERCADOS, pero nunca se salta.
VEREDICTO_N_ASK_REAL_MIN = 40


def _ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


def _pnl(p, ac):
    return (1 - p) / p * (1 - FEE) if ac else -1.0


def _tstat(v):
    n = len(v)
    if n < 2:
        return 0.0
    sd = statistics.pstdev(v)
    return (sum(v) / n) / (sd / math.sqrt(n)) if sd > 0 else 0.0


def _abrir_dia(dia):
    f = DATALOGS / f"polymarket_activity_{dia}.csv"
    if f.exists():
        return open(f, encoding="utf-8", errors="replace", newline="")
    f = DATALOGS / f"polymarket_activity_{dia}.csv.gz"
    return gzip.open(f, "rt", encoding="utf-8", errors="replace", newline="") if f.exists() else None


def procesar_dia(dia):
    """Eventos de primera compra del día con precio de seguimiento a cada L y ganador inferido de
    los trades finales del mercado (>=3 trades en los últimos 20 s, mediana de p_Up)."""
    fh = _abrir_dia(dia)
    if fh is None:
        return None
    mk = collections.defaultdict(list)
    first = {}
    with fh:
        for r in csv.DictReader(fh):
            if r["marco"] not in ("5min", "15min") or not r["market_slug"]:
                continue
            try:
                t, p = _ts(r["timestamp_utc"]), float(r["price"])
                m = re.search(r"-(\d{10})$", r["market_slug"])
            except (ValueError, KeyError, TypeError):
                continue
            if not m:
                continue
            k = r["market_slug"]
            end = int(m.group(1)) + (300 if r["marco"] == "5min" else 900)
            mk[k].append((t, p if r["outcome"] == "Up" else 1 - p, end))
            if r["side"] == "BUY":
                key = (k, r["wallet"].lower(), r["outcome"])
                if key not in first or t < first[key][0]:
                    try:
                        u = float(r["usd_value"] or 0)
                    except ValueError:
                        u = 0.0
                    first[key] = (t, p, u, r["activo"], r["marco"])
    ser, win = {}, {}
    for k, v in mk.items():
        v.sort()
        end = v[0][2]
        late = sorted(b for a, b, _ in v if a >= end - 20)
        win[k] = None if len(late) < 3 else ("Up" if late[len(late) // 2] > 0.5 else "Down" if late[len(late) // 2] < 0.5 else None)
        ser[k] = ([a for a, _, _ in v], [b for _, b, _ in v], end)
    filas = []
    for (k, w, o), (t, p, u, act, marco) in first.items():
        ts_, ups, end = ser[k]
        tte = end - t
        if tte < 15 or win[k] is None:
            continue
        pf = {}
        for L in LS:
            i = bisect.bisect_left(ts_, t + L)
            pf[L] = None
            if i < len(ts_) and ts_[i] - (t + L) <= 3 and ts_[i] < end - 5:
                pf[L] = ups[i] if o == "Up" else 1 - ups[i]
        filas.append({"wallet": w, "slug": k, "outcome": o, "activo": act, "marco": marco, "tte": round(tte, 1),
                      "usd": round(u, 2), "ac": win[k] == o, "p_paid": p, **{f"pf_{L}": pf[L] for L in LS}})
    return filas


def _agregados(filas):
    agg = collections.defaultdict(lambda: [0, 0.0, 0.0])
    for r in filas:
        p = r[f"pf_{LSEL}"]
        if p is not None and PF_LO <= p < PF_HI:
            e = _pnl(p, r["ac"])
            a = agg[r["wallet"]]
            a[0] += 1; a[1] += e; a[2] += e * e
    return {w: [n, round(s, 4), round(q, 4)] for w, (n, s, q) in agg.items()}


def _seleccion(dia):
    tot = collections.defaultdict(lambda: [0, 0.0, 0.0])
    usados = []
    for k in range(1, 9):
        d = (date.fromisoformat(dia) - timedelta(days=k)).isoformat()
        f = DIR / f"agg_{d}.json"
        if f.exists() and len(usados) < TRAIN_DIAS:
            for w, (n, s, q) in json.loads(f.read_text()).items():
                a = tot[w]; a[0] += n; a[1] += s; a[2] += q
            usados.append(d)
    sel = set()
    for w, (n, s, q) in tot.items():
        if n < MIN_N or s <= 0:
            continue
        m = s / n
        var = max(q / n - m * m, 0.0)
        if var > 0 and m / math.sqrt(var / n) >= T_MIN:
            sel.add(w)
    return sel, usados, sum(1 for a in tot.values() if a[0] >= MIN_N)


def _stats(rows, campo):
    v = [(_pnl(r[campo], r["ac"]), r) for r in rows if r.get(campo) is not None and PF_LO <= r[campo] < PF_HI]
    if not v:
        return None
    e = [x for x, _ in v]
    bm, bw = collections.defaultdict(list), collections.defaultdict(list)
    for x, r in v:
        bm[r["slug"]].append(x); bw[r["wallet"]].append(x)
    mm = [sum(a) / len(a) for a in bm.values()]
    tot = sum(e)
    top = sorted(bw.values(), key=lambda a: -sum(a))
    top5 = {id(a) for a in top[:5]}
    excl = {w for w, a in bw.items() if id(a) in top5}
    resto = [x for x, r in v if r["wallet"] not in excl]
    bm_r = collections.defaultdict(list)
    for x, r in v:
        if r["wallet"] not in excl:
            bm_r[r["slug"]].append(x)
    mm_r = [sum(a) / len(a) for a in bm_r.values()]
    return {"n": len(e), "ev": round(tot / len(e), 4), "t_iid": round(_tstat(e), 2), "n_mercados": len(bm),
            "t_cluster_mercado": round(_tstat(mm), 2), "wallets": len(bw),
            "top5_share": round(sum(sum(a) for a in top[:5]) / tot, 2) if tot > 0 else None,
            "ev_sin_top5": round(sum(resto) / len(resto), 4) if resto else None,
            "t_cluster_sin_top5": round(_tstat(mm_r), 2) if mm_r else None}


def _por_precio(rows, campo):
    g = collections.defaultdict(list)
    for r in rows:
        p = r.get(campo)
        if p is not None and PF_LO <= p < PF_HI:
            g[f"{int(p * 10) / 10:.1f}"].append(_pnl(p, r["ac"]))
    return {k: {"n": len(v), "ev": round(sum(v) / len(v), 3)} for k, v in sorted(g.items()) if len(v) >= 20}


def _por_dia(rows, campo):
    """{dia: [pnl, ...]} -- solo filas con `campo` válido en rango, EXACTAMENTE
    el mismo universo que _stats(rows, campo) usa (mismo filtro PF_LO<=x<PF_HI),
    para que días/bootstrap/split-half nunca cuenten un universo distinto al de
    ev/t_cluster de la misma llamada."""
    por_dia = collections.defaultdict(list)
    for r in rows:
        p = r.get(campo)
        if p is not None and PF_LO <= p < PF_HI:
            por_dia[r["_dia"]].append(_pnl(p, r["ac"]))
    return por_dia



def _split_half_dias(por_dia: dict) -> list | None:
    """[ev_mitad1, ev_mitad2] ordenando los días cronológicamente y partiendo
    por la mitad -- None si hay <2 días. Mismo criterio que robustez_dias()
    en el resto del proyecto: una racha buena escondida en 1-2 días dentro de
    un agregado más largo no debe pasar por robusta."""
    dias_ord = sorted(por_dia)
    if len(dias_ord) < 2:
        return None
    corte = len(dias_ord) // 2
    m1 = [x for d in dias_ord[:corte] for x in por_dia[d]]
    m2 = [x for d in dias_ord[corte:] for x in por_dia[d]]
    if not m1 or not m2:
        return None
    return [round(sum(m1) / len(m1), 4), round(sum(m2) / len(m2), 4)]


def _gate(rows, campo) -> dict:
    """Gate riguroso ÚNICO, reusado igual para el agregado y para cada
    segmento (longshot/resto) -- mismos umbrales VEREDICTO_* siempre, nunca
    una vara más floja para un sub-corte. Añade lo que _stats() no cubre:
    días independientes, bootstrap IC90 por días y split-half por días
    (mismo nivel de rigor que el resto del proyecto exige antes de hablar
    de "candidata", CLAUDE.md: n>=40, IC90 bootstrap por días>0, ambas
    mitades>0)."""
    s = _stats(rows, campo)
    por_dia = _por_dia(rows, campo)
    dias = len(por_dia)
    ic90 = _bootstrap_ic90_dias(por_dia)
    mitades = _split_half_dias(por_dia)
    robusto = bool(
        s and s["n"] >= VEREDICTO_N_ASK_REAL_MIN and dias >= VEREDICTO_MIN_DIAS
        and s["n_mercados"] >= VEREDICTO_MERCADOS
        and s["t_cluster_mercado"] >= VEREDICTO_T_CLUSTER
        and (s["ev_sin_top5"] or -1) >= VEREDICTO_EX_TOP5
        and (s["t_cluster_sin_top5"] or -9) >= VEREDICTO_T_SIN_TOP5
        and ic90 is not None and ic90[0] > 0
        and mitades is not None and mitades[0] > 0 and mitades[1] > 0
    )
    return {**(s or {"n": 0}), "dias": dias, "ic90_dias": ic90, "mitades_dias": mitades, "robusto": robusto}


# 28-Sep (hallazgo real, Javi cruzando a mano el digest del 27-Sep contra el
# ask real): el veredicto y el mensaje de Telegram se calculaban SOLO con
# pf_1.0 -- el precio del siguiente trade tras 1s, un PROXY, nunca el ask
# real del libro. Verificado con datos reales (pool 22-27-Sep, cruzado
# contra wallet_first_buy_follow_fase0.py, el observador que SÍ lee el
# libro real con profundidad): el resultado se INVIERTE casi del todo --
# longshot(pf<0.3), que el proxy daba como el foco entero del edge
# (EV/€=+0.60), da EV/€=-0.08 al ask real (n=1.542, y 66% de esas señales
# ni siquiera tienen ask fillable); resto(pf>=0.3), que el proxy descartaba
# como plano (-0.007), da EV/€=+0.11 al ask real (n=9.302, hit=69%, 3/3
# días con datos positivos, 227 wallets, top5 solo 28.6% del volumen, sigue
# positivo sin ellas +0.034). Mismo patrón ya visto en A3 (arquetipo A: el
# proxy de precio infla justo donde la selección adversa es peor). Fix:
# el veredicto y los números que van a Telegram usan SIEMPRE el ask real
# cuando hay cobertura -- nunca el proxy pf_1.0 para decidir nada, aunque
# siga registrado como dato secundario/informativo.
FOLLOW_ASK_REAL = DATALOGS / "wallet_first_buy_follow_fase0.csv"
RATIO_MIN_ASK = 5.0
# /code-review 28-Sep: offset_s en wallet_first_buy_follow_fase0.csv es SIEMPRE una de las
# constantes fijas {0.3, 1.0, 3.0} (la propia variable de bucle de ese observador, nunca un
# tiempo medido con jitter real) -- este tope no absorbe "jitter", corta exactamente entre
# el poll de 1.0s (distancia 0) y los de 0.3s/3.0s (distancia 0.7/2.0) cuando el de 1.0s
# falta, para que min(...) nunca los confunda en silencio.
MAX_DESVIO_OFFSET_S = 0.5


def _clave(wallet: str, slug: str, outcome) -> tuple | None:
    """Clave de join wallet+mercado+LADO -- nunca solo (wallet,slug).
    /code-review 28-Sep, hallazgo real y grave, verificado contra datos
    reales: 18.979/51.505 (36,8%) de las claves (wallet,slug) en
    wallet_first_buy_follow_fase0.csv tienen compras en AMBOS lados
    (Up y Down) del mismo mercado -- sin `outcome` en la clave, el ask
    del lado EQUIVOCADO podía asignarse en silencio a una fila (ej. Down
    a 0,02 asignado a un evento que era realmente Up a 0,98), corrompiendo
    exactamente el número que este fix existe para arreglar. `outcome`
    ausente (filas legacy de antes de este fix, test_*.csv sin esa
    columna) -> None, fail-closed, esa fila nunca hace match."""
    if not outcome:
        return None
    return (wallet, slug, outcome)


def _cargar_indice_ask_real(claves_necesarias: set) -> dict:
    """(wallet, slug, outcome) -> [(offset_s, ask, ratio_vs_stake), ...]
    desde wallet_first_buy_follow_fase0.py (observador en tiempo real,
    SOLO cubre wallets que ya estaban en watchlist.json el día que se
    observaron -- no hay backfill posible para días anteriores a que este
    observador arrancara, 25-Sep).

    /code-review 28-Sep, hallazgo real: la primera versión decía en el
    docstring "no crece sin límite como results.csv" -- FALSO, según el
    propio docstring de wallet_first_buy_follow_fase0.py crece ~11MB/día
    sin rotación, mismo patrón que ya causó incidentes reales en este
    proyecto (results.csv, sports activity_ws_*.csv). Fix aplicado: filtra
    desde la primera línea a `claves_necesarias` (las (wallet,slug,outcome)
    que realmente aparecen en el pool de este run, unos pocos miles) --
    nunca MATERIALIZA filas de wallets/mercados irrelevantes en memoria,
    igual que el patrón ya aplicado hoy mismo en analisis_fade_regimen_
    arquetipoA.py y buscador_edge_perdido.py.

    /code-review 28-Sep, segunda ronda, riesgo ACEPTADO y documentado (no
    resuelto): el filtro de arriba acota la MEMORIA, no el TIEMPO de
    lectura -- csv.DictReader recorre el fichero entero línea a línea en
    cada corrida diaria, y como ese fichero crece ~11MB/día sin rotación,
    el coste de I/O de esta corrida crece igual, sin límite, con el
    tiempo. Hoy (38MB/4 días) tarda segundos, aceptable para un cron
    diario -- pero la rotación real (fichero por día, o backfill con
    fecha en el nombre) le corresponde a wallet_first_buy_follow_fase0.py,
    no a este lector -- cambiar esa pieza sin verificar todos sus
    consumidores no compensa el ahorro de unos segundos hoy. Vigilar el
    tamaño del fichero cada barrido de salud (ya cubierto por el chequeo
    genérico de disco) y atajarlo ahí si empieza a doler de verdad."""
    idx = collections.defaultdict(list)
    if not claves_necesarias or not FOLLOW_ASK_REAL.exists():
        return idx
    with open(FOLLOW_ASK_REAL, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            clave = _clave(r["wallet"], r["slug"], r.get("outcome"))
            if clave is None or clave not in claves_necesarias:
                continue
            try:
                off = float(r["offset_s"])
            except (ValueError, KeyError, TypeError):
                continue
            idx[clave].append((off, r.get("ask"), r.get("ratio_vs_stake")))
    return idx


def _anotar_ask_real(rows: list, idx: dict, campo: str = "ask_real_1.0") -> None:
    """Añade `campo` a cada fila de `rows` IN-PLACE: el ask real fillable
    del MISMO lado (wallet,slug,outcome) más cercano a LSEL=1.0 s (dentro
    de MAX_DESVIO_OFFSET_S), o None si no hay match/no es fillable/el más
    cercano está demasiado lejos/falta outcome -- fail-closed, nunca cae
    de vuelta al proxy pf_1.0 en silencio, nunca mezcla el lado Up con el
    Down, y nunca etiqueta un ask de 0.3s o 3.0s como si fuera el de 1.0s.

    /code-review 28-Sep, decisión deliberada tras verificar los datos:
    SOLO se mira la lectura más cercana a 1.0s, nunca se cae a la de 0.3s
    o 3.0s si la de 1.0s no es fillable (ratio_vs_stake<5) -- aunque esa
    otra SÍ lo fuera. Verificado que esto pasa en 3.888/70.913 claves
    (5,5%), y el 87% de esos casos es libro insuficiente justo en el
    segundo 1 (recuperado a 0,3s o 3s) -- NO fallo técnico. Se decide NO
    rellenar con el ask de otro instante a propósito: es el MISMO
    criterio que ya usa todo el proyecto (veto_profundidad, ratio_vs_
    stake>=5 en cada ejecutor) -- un libro insuficiente en el momento
    exacto es una señal real de iliquidez, no un hueco a tapar con el
    precio de otro segundo. Rellenar aquí reintroduciría precisamente el
    tipo de mezcla de instantes que el propio MAX_DESVIO_OFFSET_S existe
    para evitar."""
    for r in rows:
        r[campo] = None
        clave = _clave(r.get("wallet"), r.get("slug"), r.get("outcome"))
        if clave is None:
            continue
        cands = idx.get(clave)
        if not cands:
            continue
        off, ask, ratio = min(cands, key=lambda c: abs(c[0] - LSEL))
        if abs(off - LSEL) > MAX_DESVIO_OFFSET_S:
            continue
        try:
            ask_f, ratio_f = float(ask), float(ratio or 0)
        except (TypeError, ValueError):
            continue
        # /code-review 28-Sep, hallazgo real: este rango (0.01,0.99) era más ancho que
        # [PF_LO,PF_HI)=[0.03,0.97) que usan _stats/_por_precio -- n_con_ask_real (conteo
        # de cobertura) podía incluir filas que _stats() excluía después, dos "n" distintos
        # sin reconciliar en el mismo mensaje. Mismo rango aquí que en _stats -- una sola
        # definición de "fillable y en rango válido", nunca dos.
        # /code-review 28-Sep: PF_LO<=x<PF_HI (semiabierto), IDÉNTICO a _stats()/_por_precio()
        # -- con "<" estricto en el extremo bajo se rechazaba un ask exactamente en PF_LO
        # (0,03) que _stats() sí habría aceptado, rompiendo la "única definición" que
        # este mismo fix afirma tener.
        if ratio_f >= RATIO_MIN_ASK and PF_LO <= ask_f < PF_HI:
            r[campo] = ask_f


def ejecutar(dia, enviar=True):
    DIR.mkdir(parents=True, exist_ok=True)
    filas = procesar_dia(dia)
    if filas is None:
        print(f"sin datos de {dia}")
        return None
    sel, usados, n_train_w = _seleccion(dia)          # selección con datos ANTERIORES a `dia` (congelada)
    (DIR / f"agg_{dia}.json").write_text(json.dumps(_agregados(filas)))
    test = [r for r in filas if r["wallet"] in sel]
    campos = ["wallet", "slug", "outcome", "activo", "marco", "tte", "usd", "ac", "p_paid"] + [f"pf_{L}" for L in LS]
    with open(DIR / f"test_{dia}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for r in test:
            w.writerow({c: r[c] for c in campos})
    dia_res = {"dia": dia, "train_dias": usados, "wallets_train_n>=15": n_train_w, "seleccionadas": len(sel),
               "eventos_dia_total": len(filas), "test": {str(L): _stats(test, f"pf_{L}") for L in LS}}
    pool = []
    for f in sorted(DIR.glob("test_*.csv")):
        dia_fichero = f.stem[len("test_"):]   # test_YYYY-MM-DD.csv -- un fichero = un día exacto
        for r in csv.DictReader(open(f, encoding="utf-8")):
            for L in LS:
                r[f"pf_{L}"] = float(r[f"pf_{L}"]) if r[f"pf_{L}"] != "" else None
            r["ac"] = r["ac"] == "True"
            r["_dia"] = dia_fichero
            pool.append(r)
    dias_test = \
        sum(1 for f in DIR.glob("test_*.csv") if f.stat().st_size > 200)   # solo días con wallets seleccionadas
    pool_res = {str(L): _stats(pool, f"pf_{L}") for L in LS}   # proxy pf -- informativo, NUNCA decide el veredicto

    # Ask real (ver docstring de _anotar_ask_real): fuente de verdad para el veredicto y Telegram.
    claves_necesarias = {c for r in pool if (c := _clave(r.get("wallet"), r.get("slug"), r.get("outcome"))) is not None}
    idx_ask_real = _cargar_indice_ask_real(claves_necesarias)
    _anotar_ask_real(pool, idx_ask_real, "ask_real_1.0")
    n_con_ask_real = sum(1 for r in pool if r.get("ask_real_1.0") is not None)

    # 28-Sep (petición explícita Javi, "resuélvelo ya"): el veredicto agregado mezclaba
    # longshot(pf<0.3) y resto(pf>=0.3), que van en direcciones opuestas -- un segmento
    # bueno puede quedar enterrado por uno malo (o viceversa) en el número agregado. Se
    # aplica el MISMO gate riguroso (_gate(), umbrales VEREDICTO_* sin excepción) al
    # agregado Y a cada segmento por separado -- nunca una vara más floja para el
    # sub-corte, y con bootstrap IC90 por días + split-half por días añadidos (antes
    # solo t_cluster/ex-top5, sin ese nivel extra de rigor).
    gate_agregado = _gate(pool, "ask_real_1.0")
    gate_longshot = _gate([r for r in pool if r.get("pf_1.0") is not None and r["pf_1.0"] < 0.3], "ask_real_1.0")
    gate_resto = _gate([r for r in pool if r.get("pf_1.0") is not None and r["pf_1.0"] >= 0.3], "ask_real_1.0")
    comp = {"longshot_pf<0.3": gate_longshot, "resto_pf>=0.3": gate_resto}

    if gate_agregado["n"] < VEREDICTO_N_ASK_REAL_MIN:
        veredicto = f"SIN COBERTURA SUFICIENTE de ask real (n={n_con_ask_real}, mínimo {VEREDICTO_N_ASK_REAL_MIN}) -- esperar más días de wallet_first_buy_follow_fase0.py"
    else:
        partes = [f"agregado {'CANDIDATA robusta' if gate_agregado['robusto'] else 'NO robusta'}"]
        for nombre, g in (("longshot(pf<0.3)", gate_longshot), ("resto(pf>=0.3)", gate_resto)):
            if g["n"] >= VEREDICTO_N_ASK_REAL_MIN:
                partes.append(f"{nombre} {'CANDIDATA robusta' if g['robusto'] else 'no robusta'} "
                              f"(n={g['n']}, dias={g['dias']}, t_cl={g.get('t_cluster_mercado')}, "
                              f"IC90={g.get('ic90_dias')})")
        veredicto = " | ".join(partes)
    informe = {"actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "ultimo_dia": dia_res,
               "pool": {"dias_test": dias_test, "por_L_proxy_pf": pool_res, "por_precio_L1_proxy": _por_precio(pool, "pf_1.0"),
                        "composicion_L1_ask_real": comp,
                        "ask_real": {"n_fillable": n_con_ask_real, "gate_agregado": gate_agregado}},
               "veredicto": veredicto}
    OUT.write_text(json.dumps(informe, indent=1, ensure_ascii=False))
    # Watchlist para el día SIGUIENTE (selección congelada con los TRAIN_DIAS días que acaban en `dia`,
    # incluido): la lee wallet_first_buy_follow_fase0.py (observador en tiempo real).
    try:
        dia_sig = (date.fromisoformat(dia) + timedelta(days=1)).isoformat()
        sel_sig, usados_sig, _ = _seleccion(dia_sig)
        tot = collections.defaultdict(lambda: [0, 0.0, 0.0])
        for d in usados_sig:
            for w, (n, sm, q) in json.loads((DIR / f"agg_{d}.json").read_text()).items():
                if w in sel_sig:
                    a = tot[w]; a[0] += n; a[1] += sm; a[2] += q
        (DIR / "watchlist.json").write_text(json.dumps(
            {"para_dia": dia_sig, "train_dias": usados_sig,
             "wallets": {w: {"n": v[0], "ev_medio": round(v[1] / v[0], 4)} for w, v in tot.items()}}))
    except Exception as e:
        print(f"(watchlist no escrita: {e})")
    with open(HIST, "a", encoding="utf-8") as f:
        f.write(json.dumps({"dia": dia, "ultimo_dia": dia_res, "gate_agregado": gate_agregado,
                            "gate_longshot": gate_longshot, "gate_resto": gate_resto,
                            "pool_proxy_pf1_informativo": pool_res.get(str(LSEL)),
                            "veredicto": veredicto}, ensure_ascii=False) + "\n")
    t1_proxy = dia_res["test"][str(LSEL)] or {}
    msg = [f"🐋 Wallets 'primera compra' -- forward {dia} (sel. con {len(usados)} días previos: {len(sel)} wallets)",
           f"cobertura ask real: {n_con_ask_real} señales fillable en {gate_agregado['dias']} día(s) "
           f"(de {len(pool)} en el pool, {dias_test} días de test -- el resto sin match/no fillable en "
           f"wallet_first_buy_follow_fase0.py)"]
    if gate_agregado["n"]:
        msg.append(f"AGREGADO al ask real: n={gate_agregado['n']} mercados={gate_agregado['n_mercados']} "
                   f"EV/€={gate_agregado['ev']} t_cluster={gate_agregado['t_cluster_mercado']} "
                   f"top5={gate_agregado['top5_share']} sin_top5={gate_agregado['ev_sin_top5']} "
                   f"IC90_dias={gate_agregado['ic90_dias']} -> {'CANDIDATA' if gate_agregado['robusto'] else 'no robusto'}")
        for nombre, g in (("longshot(pf<0.3)", gate_longshot), ("resto(pf>=0.3)", gate_resto)):
            if not g["n"]:
                msg.append(f"  {nombre}: sin señales")
                continue
            msg.append(f"  {nombre}: n={g['n']} EV/€={g.get('ev')} dias={g['dias']} t_cluster={g.get('t_cluster_mercado')} "
                       f"sin_top5={g.get('ev_sin_top5')} IC90_dias={g.get('ic90_dias')} mitades={g.get('mitades_dias')} "
                       f"-> {'CANDIDATA robusta' if g['robusto'] else 'no robusta'}")
    else:
        msg.append("AL ASK REAL: sin datos suficientes todavía")
    msg.append(f"(informativo, NUNCA decide el veredicto -- precio de trade, no ask real) proxy pf_1.0 pool: "
               f"n={pool_res[str(LSEL)] and pool_res[str(LSEL)]['n']} EV/€={pool_res[str(LSEL)] and pool_res[str(LSEL)]['ev']} "
               f"| día {dia}: n={t1_proxy.get('n')} EV/€={t1_proxy.get('ev')}")
    msg.append(f"veredicto: {veredicto}")
    print("\n".join(msg))
    if enviar:
        try:
            sys.path.insert(0, str(REPO))
            from shadow_digest import enviar_telegram
            enviar_telegram("\n".join(msg))
        except Exception as e:
            print(f"(Telegram falló: {e})")
    return informe


def main():
    a = sys.argv[1:]
    if "--backfill" in a:
        i = a.index("--backfill")
        d0, d1 = date.fromisoformat(a[i + 1]), date.fromisoformat(a[i + 2])
        while d0 <= d1:
            ejecutar(d0.isoformat(), enviar=False)
            d0 += timedelta(days=1)
        return 0
    if "--sin-telegram" in a:
        dia = a[a.index("--dia") + 1] if "--dia" in a else (datetime.now(timezone.utc).date() - timedelta(days=1)).isoformat()
        ejecutar(dia, enviar=False)
        return 0
    dia = a[a.index("--dia") + 1] if "--dia" in a else (datetime.now(timezone.utc).date() - timedelta(days=1)).isoformat()
    ejecutar(dia)
    return 0


if __name__ == "__main__":
    sys.exit(main())
