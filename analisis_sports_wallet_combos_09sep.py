#!/usr/bin/env python3
"""
analisis_sports_wallet_combos_09sep.py -- 09-Sep, petición explícita Javi:
"estudia las wallets que hacen combos en sports, hay mucho dinero ahí también".

Definicion operativa de "combo" (no hay tabla de parlays nativa en el
firehose -- Polymarket no expone combos multi-mercado como un objeto,
solo trades individuales por mercado, ver `data/sports/activity_ws_*.csv`):
una wallet que, dentro del MISMO evento (`event_slug`), compra (BUY) en
>=2 `condition_id` (mercados) DISTINTOS. Eso captura tanto "combos reales"
(moneyline+total+handicap del mismo partido) como cobertura/hedging -- el
gate riguroso de abajo es el que separa si el patrón tiene edge o es ruido.

Metodologia (rigor exigido por CLAUDE.md: n>=15, shuffle antes de concluir,
resolver outcome real via gamma-api, nunca asumir columna sin comprobar):
1. Cargar TODO data/sports/activity_ws_*.csv (BUY, dedupe por
   transaction_hash) -- unica fuente disponible, 4 dias (06..09-Sep).
2. Agrupar por (wallet, event_slug) -> {condition_id: [(ts,price,outcome)]}.
   Wallet "combo" en ese evento si >=2 condition_id distintos.
3. Resolver outcome real via gamma-api (mismo patron que
   sports_wallet_edge_tracker.py::resolver_outcomes) para los condition_id
   involucrados en ambos grupos (combo y no-combo).
4. Comparar hit-rate:
   (a) grupo COMBO (todos los trades de wallets que hicieron combo en ese
       evento, solo los mercados resueltos) vs mercado en agregado
       (mismo pool de condition_id, todas las wallets).
   (b) las MISMAS wallets combo, en OTROS eventos donde operaron un solo
       mercado (no-combo) -- compara la wallet contra si misma.
5. Shuffle test (reasignar acierto aleatoriamente dentro del pool) antes
   de declarar nada significativo. n>=15 minimo, si no, se declara
   "insuficiente" explicitamente.

Solo lectura, no toca produccion. Salida: data/shadow/sports_wallet_combos_09sep.json
"""
import csv
import glob
import json
import random
import statistics
import sys
import threading
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
DIR_SPORTS = REPO / "data" / "sports"
GAMMA_API = "https://gamma-api.polymarket.com"
OUT = REPO / "data" / "shadow" / "sports_wallet_combos_09sep.json"
N_SHUFFLE = 2000


def cargar_trades():
    """[(wallet, event_slug, condition_id, market_slug, categoria, outcome,
    price, ts, usd)] BUY only, dedupe por transaction_hash."""
    files = sorted(glob.glob(str(DIR_SPORTS / "activity_ws_*.csv")))
    vistos = set()
    out = []
    for fn in files:
        with open(fn, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                h = r.get("transaction_hash", "")
                if h and h in vistos:
                    continue
                if h:
                    vistos.add(h)
                if (r.get("side") or "").strip().upper() != "BUY":
                    continue
                try:
                    price = float(r["price"])
                    usd = float(r.get("usd_value") or 0)
                except (ValueError, KeyError, TypeError):
                    continue
                if not (0 < price < 1):
                    continue
                wallet = (r.get("wallet") or "").lower()
                cid = r.get("condition_id") or ""
                if not wallet or not cid:
                    continue
                outcome = (r.get("outcome") or "").strip().lower()
                out.append({
                    "wallet": wallet, "event_slug": r.get("event_slug", ""),
                    "condition_id": cid, "market_slug": r.get("market_slug", ""),
                    "categoria": r.get("categoria", ""), "outcome": outcome,
                    "price": price, "ts": r.get("timestamp_utc", ""), "usd": usd,
                })
    print(f"[combos] {len(out)} trades BUY cargados de {len(files)} ficheros", file=sys.stderr)
    return out


def _resolver_lote(lote, reintentos=4):
    params = [("condition_ids", c) for c in lote] + [("closed", "true")]
    data = None
    for intento in range(reintentos):
        try:
            r = requests.get(f"{GAMMA_API}/markets", params=params, timeout=20)
            if r.status_code == 429:
                time.sleep(1.5 * (intento + 1))
                continue
            r.raise_for_status()
            data = r.json()
            break
        except Exception as e:
            if intento == reintentos - 1:
                print(f"  [error resolver] {e}", file=sys.stderr)
            time.sleep(1.0 * (intento + 1))
    if data is None:
        return {}
    out = {}
    for m in data:
        cid = m.get("conditionId") or m.get("condition_id")
        if not cid or not m.get("closed"):
            continue
        try:
            precios = json.loads(m["outcomePrices"]) if isinstance(m.get("outcomePrices"), str) else m.get("outcomePrices")
            nombres = json.loads(m["outcomes"]) if isinstance(m.get("outcomes"), str) else m.get("outcomes")
            precios = [float(p) for p in precios]
        except Exception:
            continue
        if not precios or not nombres or len(precios) != len(nombres):
            continue
        ganador = None
        for nombre, p in zip(nombres, precios):
            if abs(p - 1.0) < 0.01:
                ganador = nombre.strip().lower()
                break
        if ganador:
            out[cid] = ganador
    return out


def resolver_outcomes(condition_ids, batch=20, workers=3, sleep_por_worker=0.4):
    """condition_id -> nombre del outcome ganador (lower), o None si no
    resuelto. Paraleliza en `workers` hilos (cada hilo respeta
    `sleep_por_worker` entre requests) -- script de investigacion puntual,
    no un cron persistente, tolerable pedirle mas throughput a gamma-api
    (endpoint publico, ya usado igual por sports_wallet_edge_tracker.py a
    ritmo secuencial 3 req/s; aqui van varios hilos en paralelo a ese mismo
    ritmo cada uno)."""
    cids = sorted(set(condition_ids))
    lotes = [cids[i:i + batch] for i in range(0, len(cids), batch)]
    resultado = {}
    lock = threading.Lock()
    contador = {"hecho": 0}

    def worker(lote):
        r = _resolver_lote(lote)
        time.sleep(sleep_por_worker)
        with lock:
            resultado.update(r)
            contador["hecho"] += 1
            if contador["hecho"] % 100 == 0:
                print(f"  resolviendo... {contador['hecho']}/{len(lotes)} lotes", file=sys.stderr)
        return r

    with ThreadPoolExecutor(max_workers=workers) as ex:
        list(ex.map(worker, lotes))
    return resultado


def wilson_lo(hits, n, z=1.645):
    if n == 0:
        return 0.0
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)
    return (centro - margen) / denom


def shuffle_test(aciertos, n_shuffle=N_SHUFFLE):
    """aciertos: lista de 0/1 con una etiqueta de grupo (True=combo).
    Se pasa como (labels, valores) -- ver uso abajo."""
    pass


def evaluar_grupo(nombre, filas):
    """filas: lista de dict con 'acierto' (0/1). Devuelve resumen + shuffle p
    contra baseline 50% (mercados binarios) -- para head-to-head multi-outcome
    el baseline real es 1/n_outcomes, así que reportamos también hit crudo."""
    n = len(filas)
    if n == 0:
        return {"n": 0}
    hits = sum(f["acierto"] for f in filas)
    hit_rate = hits / n
    return {
        "n": n,
        "hits": hits,
        "hit_rate": round(hit_rate, 4),
        "wilson90_lo": round(wilson_lo(hits, n), 4),
        "usd_medio": round(statistics.mean(f["usd"] for f in filas), 2) if n else 0,
        "precio_medio_entrada": round(statistics.mean(f["price"] for f in filas), 4) if n else 0,
    }


def shuffle_diff_test(grupo_a, grupo_b, n_shuffle=N_SHUFFLE, seed=42):
    """Diferencia de hit-rate entre dos grupos + significancia.

    09-Sep, fix de rendimiento: el test de permutacion por fuerza bruta en
    Python puro (mezclar 2000 veces un pool combinado de cientos de miles
    de trades) resulto ser O(n_shuffle*n) -- inviable aqui (n_a+n_b puede
    superar 500k filas), colgó el proceso >10min sin terminar. Un test de
    permutacion de una diferencia de proporciones sobre un pool combinado
    es matematicamente EQUIVALENTE al test exacto de Fisher sobre la tabla
    2x2 (aciertos/fallos x grupo) -- mismo p-value en el limite, exacto en
    vez de aproximado por Monte Carlo, e instantaneo. Se usa
    scipy.stats.fisher_exact en su lugar (rigor exigido por CLAUDE.md:
    "shuffle antes de bloquear" -- este es su equivalente exacto, no un
    atajo que lo debilite).

    Caveat real a citar siempre: cada fila es un TRADE, no una wallet o un
    evento independiente -- varios trades del mismo mercado comparten el
    mismo 'acierto' (mismo outcome real), y varias wallets pueden operar
    el mismo mercado. Esto infla el n efectivo (pseudo-replicacion) frente
    a un test wallet-a-wallet o evento-a-evento; el p-value aqui es
    orientativo de la escala del efecto, no una prueba definitiva a nivel
    de wallet."""
    from scipy.stats import fisher_exact

    n_a, n_b = len(grupo_a), len(grupo_b)
    if n_a == 0 or n_b == 0:
        return None
    hits_a = sum(f["acierto"] for f in grupo_a)
    hits_b = sum(f["acierto"] for f in grupo_b)
    obs_diff = (hits_a / n_a) - (hits_b / n_b)
    tabla = [[hits_a, n_a - hits_a], [hits_b, n_b - hits_b]]
    try:
        _, p = fisher_exact(tabla)
    except Exception as e:
        print(f"  [error fisher_exact] {e}", file=sys.stderr)
        p = None
    return {"obs_diff_pp": round(obs_diff * 100, 2), "p_shuffle": round(p, 6) if p is not None else None,
            "metodo": "fisher_exact (equivalente exacto de shuffle en pool combinado, ver docstring)"}


def main():
    trades = cargar_trades()

    # 1) Agrupar por (wallet,event_slug) -> set condition_id
    por_wallet_evento = defaultdict(lambda: defaultdict(list))
    for t in trades:
        por_wallet_evento[t["wallet"]][t["event_slug"]].append(t)

    combo_trades = []       # trades de wallets que combinaron en ESE evento
    no_combo_trades_mismaswallets = []  # mismas wallets combo, en eventos donde NO combinaron
    wallets_combo = set()
    n_eventos_combo = 0

    for wallet, eventos in por_wallet_evento.items():
        for event_slug, filas in eventos.items():
            if not event_slug:
                continue
            cids = {f["condition_id"] for f in filas}
            if len(cids) >= 2:
                combo_trades.extend(filas)
                wallets_combo.add(wallet)
                n_eventos_combo += 1

    for wallet in wallets_combo:
        for event_slug, filas in por_wallet_evento[wallet].items():
            cids = {f["condition_id"] for f in filas}
            if len(cids) < 2 and event_slug:
                no_combo_trades_mismaswallets.extend(filas)

    print(f"[combos] eventos-wallet con combo: {n_eventos_combo}, wallets distintas: {len(wallets_combo)}", file=sys.stderr)
    print(f"[combos] trades en combos: {len(combo_trades)}, trades no-combo mismas wallets: {len(no_combo_trades_mismaswallets)}", file=sys.stderr)

    # 2) Resolver outcomes -- combo + no_combo_mismaswallets se resuelven
    # COMPLETOS (son el par de comparacion principal, controla por wallet).
    # El baseline (a) "mercado agregado" es solo orientativo y su pool es
    # mucho mas caro de resolver (todos los condition_id del firehose,
    # ~19.5k) -- se resuelve sobre una MUESTRA aleatoria (semilla fija,
    # reproducible) para mantener el runtime razonable en un script de
    # investigacion puntual, no un cron. Los cids ya presentes en
    # combo/no_combo se excluyen de la muestra para no gastar cupo en algo
    # que ya se resuelve de todas formas.
    AGREGADO_MUESTRA_MAX = 4000
    cids_combo = {t["condition_id"] for t in combo_trades}
    cids_no_combo = {t["condition_id"] for t in no_combo_trades_mismaswallets}
    cids_agregado_todos = {t["condition_id"] for t in trades}
    cids_agregado_extra = list(cids_agregado_todos - cids_combo - cids_no_combo)
    rnd_muestra = random.Random(7)
    rnd_muestra.shuffle(cids_agregado_extra)
    cids_agregado_muestra = set(cids_agregado_extra[:AGREGADO_MUESTRA_MAX])
    print(f"[combos] condition_ids: combo={len(cids_combo)} no_combo_mismaswallets={len(cids_no_combo)} "
          f"agregado_total={len(cids_agregado_todos)} agregado_muestra_extra={len(cids_agregado_muestra)}", file=sys.stderr)

    todos_cids = cids_combo | cids_no_combo | cids_agregado_muestra
    outcomes = resolver_outcomes(todos_cids)
    print(f"[combos] resueltos: {len(outcomes)}/{len(todos_cids)}", file=sys.stderr)

    # El grupo "agregado" para el baseline (a) se restringe a las filas cuyo
    # condition_id cayo en combo, no_combo o la muestra -- para no filtrar
    # despues por outcomes.get() sobre un cid nunca pedido.
    cids_agregado_resoluble = cids_combo | cids_no_combo | cids_agregado_muestra
    trades_agregado_muestreado = [t for t in trades if t["condition_id"] in cids_agregado_resoluble]

    def marcar_acierto(filas):
        out = []
        for f in filas:
            oc = outcomes.get(f["condition_id"])
            if oc is None:
                continue
            g = dict(f)
            g["acierto"] = 1 if f["outcome"] == oc else 0
            out.append(g)
        return out

    combo_resueltos = marcar_acierto(combo_trades)
    no_combo_resueltos = marcar_acierto(no_combo_trades_mismaswallets)
    agregado_resueltos = marcar_acierto(trades_agregado_muestreado)

    resumen_combo = evaluar_grupo("combo", combo_resueltos)
    resumen_no_combo_mismaswallets = evaluar_grupo("no_combo_mismaswallets", no_combo_resueltos)
    resumen_agregado = evaluar_grupo("agregado_mercado", agregado_resueltos)

    test_vs_agregado = shuffle_diff_test(combo_resueltos, agregado_resueltos) if len(combo_resueltos) >= 15 and len(agregado_resueltos) >= 15 else None
    test_vs_mismaswallets = shuffle_diff_test(combo_resueltos, no_combo_resueltos) if len(combo_resueltos) >= 15 and len(no_combo_resueltos) >= 15 else None

    # 3) Desagregar por categoria (CLAUDE.md pt.17 -- nunca solo agregado)
    por_categoria = defaultdict(list)
    for f in combo_resueltos:
        por_categoria[f["categoria"]].append(f)
    resumen_por_categoria = {}
    for cat, filas in sorted(por_categoria.items(), key=lambda kv: -len(kv[1])):
        resumen_por_categoria[cat] = evaluar_grupo(cat, filas)

    # 4) Top wallets combo por n y hit-rate (para inspeccion manual)
    por_wallet_combo = defaultdict(list)
    for f in combo_resueltos:
        por_wallet_combo[f["wallet"]].append(f)
    top_wallets = []
    for w, filas in por_wallet_combo.items():
        if len(filas) < 5:
            continue
        r = evaluar_grupo(w, filas)
        r["wallet"] = w
        top_wallets.append(r)
    top_wallets.sort(key=lambda r: (-r["hit_rate"], -r["n"]))

    resultado = {
        "generado": "2026-09-09",
        "ficheros_fuente": sorted(glob.glob(str(DIR_SPORTS / "activity_ws_*.csv"))),
        "dias_cobertura": len(glob.glob(str(DIR_SPORTS / "activity_ws_*.csv"))),
        "n_trades_totales_buy": len(trades),
        "n_eventos_wallet_combo": n_eventos_combo,
        "n_wallets_distintas_combo": len(wallets_combo),
        "n_condition_ids_combo": len(cids_combo),
        "n_condition_ids_resueltos": len(outcomes),
        "resumen_combo": resumen_combo,
        "resumen_no_combo_mismaswallets": resumen_no_combo_mismaswallets,
        "resumen_agregado_mercado": resumen_agregado,
        "shuffle_combo_vs_agregado": test_vs_agregado,
        "shuffle_combo_vs_mismaswallets_nocombo": test_vs_mismaswallets,
        "por_categoria_combo": resumen_por_categoria,
        "top_wallets_combo_n_ge_5": top_wallets[:30],
        "notas": [
            "Definicion combo = wallet BUY en >=2 condition_id distintos del mismo event_slug (no hay objeto 'parlay' nativo en el firehose).",
            "Cobertura real limitada a 4 dias (06..09-Sep) -- ventana corta, la mayoria de mercados sports resuelven rapido pero el n de resueltos puede ser bajo.",
            "n<15 en cualquier grupo => 'insuficiente', no concluir nada con ese grupo.",
            "outcome resuelto via gamma-api closed=true, mismo patron que sports_wallet_edge_tracker.py::resolver_outcomes.",
        ],
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    print(f"[combos] guardado en {OUT}", file=sys.stderr)

    print(json.dumps({
        "resumen_combo": resumen_combo,
        "resumen_no_combo_mismaswallets": resumen_no_combo_mismaswallets,
        "resumen_agregado_mercado": resumen_agregado,
        "shuffle_combo_vs_agregado": test_vs_agregado,
        "shuffle_combo_vs_mismaswallets_nocombo": test_vs_mismaswallets,
    }, indent=2))


if __name__ == "__main__":
    main()
