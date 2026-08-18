#!/usr/bin/env python3
"""sports_wallet_edge_tracker.py — inteligencia de wallets para sports/
esports, port del modelo de cripto (wallet_edge_tracker.py), 18-Ago,
petición explícita Javi: "filtrar por ballenas, wallets expertas y
wallets informadas por cada categoría y mercado existente en sports,
tal y como hacemos en cripto... desgregar también aquí".

SEPARACIÓN ESTRICTA de cripto (decisión explícita Javi, 18-Ago): mismo
repo, pero código y datos 100% separados. Prefijo `sports_` en todo
fichero nuevo, `data/sports/` para toda salida -- nunca `data/shadow/`
ni `data/live/` (esos son de cripto). Único punto compartido: la
conexión websocket ya abierta por `fetch_polymarket_activity_ws.py`
(screen `polyactivity`) -- se LEE su output rotado en
`/root/polymarket-research-datalogs/`, nunca se importa lógica de
estrategias cripto ni se escribe en sus ficheros.

Pipeline (idéntico en espíritu a wallet_edge_tracker.py, aplicado por
categoría/deporte/liga en vez de por activo/marco):
1. Extraer trades whale-tier (≥$1000, único filtro posible sin
   suscripción de pago) de 21 días de polymarket_activity_*.csv rotado,
   dedupe por transaction_hash.
2. Clasificar en categoría fina — deportes explícitos (UFC/Boxing/NBA/
   WNBA/NFL/MLB/NHL/Tennis/Golf/F1/Cricket/Rugby/Cycling/Darts/Snooker)
   + esports (LoL/Valorant/CS/Dota/Overwatch/RainbowSix/RocketLeague/
   StarCraft/PUBG) + fútbol auto-segmentado por liga (`Soccer-{prefijo
   de event_slug}`, nunca un bucket único "Soccer" — bug real corregido
   el mismo día, escondía 30+ ligas sin desagregar).
3. Resolver outcome real vía gamma-api (`condition_ids` + `closed=true`
   en batch de 20) -- el campo `outcome` del trade es el NOMBRE del
   contendiente/equipo en mercados head-to-head, no "Yes"/"No"; se
   compara contra el array `outcomes` de gamma-api, nunca se asume
   binario.
4. Por (wallet, categoría): edge_pp=(hit−precio_medio)×100, shuffle
   test contra Binomial(n,precio_medio), corrección BH-FDR DENTRO de
   cada categoría -- misma metodología exacta que wallet_edge_tracker.py.
5. Especialistas: wallets con ≥80% de su actividad concentrada en 1
   categoría (mismo criterio que wallet_especialistas_observer.py).

Salida: data/sports/wallet_edge_score_por_categoria.json. Puramente de
descubrimiento/análisis -- no ejecuta ni simula ninguna orden.
"""
import csv
import glob
import gzip
import json
import math
import re
import sys
import time
from collections import defaultdict, Counter
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import requests

DATALOGS = "/root/polymarket-research-datalogs"  # solo lectura -- rotación
# del firehose ya escrito por fetch_polymarket_activity_ws.py (screen
# polyactivity, infraestructura de red COMPARTIDA con cripto a propósito,
# ver decisión Javi 18-Ago) -- este script nunca escribe ahí ni importa
# ningún módulo de estrategias cripto.
DIR_SPORTS = Path(__file__).resolve().parent / "data" / "sports"  # TODO lo
# que este script produce vive aquí, separado de data/shadow (cripto).
GAMMA_API = "https://gamma-api.polymarket.com"
N_MIN = 15
FDR = 0.10
N_SHUFFLE = 3000

CATEGORIAS = [
    ("UFC", re.compile(r'\bUFC\b', re.I)),
    ("Boxing", re.compile(r'\bboxing\b|\bWBC\b|\bWBA\b|\bIBF\b', re.I)),
    ("NBA", re.compile(r'\bNBA\b', re.I)),
    ("WNBA", re.compile(r'\bWNBA\b', re.I)),
    ("NFL", re.compile(r'\bNFL\b', re.I)),
    ("MLB", re.compile(r'\bMLB\b', re.I)),
    ("NHL", re.compile(r'\bNHL\b', re.I)),
    ("Tennis", re.compile(r'\bATP\b|\bWTA\b|\bITF\b|\btennis\b', re.I)),
    ("Golf", re.compile(r'\bPGA\b|\bLIV Golf\b|\bgolf\b', re.I)),
    ("F1", re.compile(r'\bF1\b|Formula 1|Formula One|Drivers[\' ]?Championship', re.I)),
    ("Cricket", re.compile(r'\bcricket\b|IPL|Premier League:.*vs.*Kingsmen|Caribbean Premier League', re.I)),
    ("Rugby", re.compile(r'\brugby\b', re.I)),
    ("Cycling", re.compile(r'\bcycling\b|\bTour de France\b|\bVuelta\b|\bGiro\b', re.I)),
    ("Darts", re.compile(r'\bdarts\b', re.I)),
    ("Snooker", re.compile(r'\bsnooker\b', re.I)),
    ("LoL", re.compile(r'\bLoL\b|League of Legends', re.I)),
    ("Valorant", re.compile(r'\bValorant\b', re.I)),
    ("CS", re.compile(r'\bCS:?GO\b|\bCS2\b|Counter-Strike', re.I)),
    ("Dota", re.compile(r'\bDota\b', re.I)),
    ("Overwatch", re.compile(r'\bOverwatch\b', re.I)),
    ("RainbowSix", re.compile(r'Rainbow Six|\bR6\b', re.I)),
    ("RocketLeague", re.compile(r'Rocket League', re.I)),
    ("StarCraft", re.compile(r'StarCraft', re.I)),
    ("PUBG", re.compile(r'\bPUBG\b', re.I)),
]

# Ligas de soccer/futbol -- auto-descubiertas por el prefijo del event_slug
# (mismo espiritu que "activo" en cripto, en vez de listar cada liga a
# mano y arriesgar dejarse alguna, 18-Ago: hallazgo real, "Soccer" como
# bucket unico escondia 30+ ligas distintas -- MLS, La Liga (lal), Serie A
# (itc), Bundesliga2 (bl2), Eredivisie (ere), Ligue1 (frtc), etc). Solo se
# usa para titulos "Will {equipo} win on {fecha}" que no matchean ninguna
# categoria explicita de arriba -- evita que NFL/NBA future-champion
# markets ("Will the Packers win the 2027 NFL...") caigan aqui por error,
# esos ya los captura la categoria NFL/NBA por keyword antes de llegar a
# este fallback.
_WILL_WIN_RE = re.compile(r'\bwill\b.*\bwin on\b', re.I)
_SLUG_PREFIX_RE = re.compile(r'^([a-z0-9]+)-')


def clasificar(title, event_slug=""):
    for nombre, rx in CATEGORIAS:
        if rx.search(title):
            return nombre
    if _WILL_WIN_RE.search(title):
        m = _SLUG_PREFIX_RE.match(event_slug or "")
        liga = m.group(1) if m else "otra"
        return f"Soccer-{liga}"
    return None


def cargar_trades_whale(vistos: set | None = None):
    """[(wallet, condition_id, categoria, outcome, price, ts, usd), ...]
    dedupe por transaction_hash. `vistos` opcional (18-Ago) -- compartido
    con cargar_trades_completo() para dedupe CRUZADO entre las dos
    fuentes (un trade whale puede aparecer en ambas)."""
    files = sorted(glob.glob(f"{DATALOGS}/polymarket_activity_*.csv*"))
    if vistos is None:
        vistos = set()
    out = []
    for path in files:
        opener = gzip.open if path.endswith(".gz") else open
        with opener(path, "rt") as f:
            for r in csv.DictReader(f):
                if r.get("activo"):
                    continue
                h = r.get("transaction_hash", "")
                if h in vistos:
                    continue
                vistos.add(h)
                if (r.get("side") or "").strip().upper() != "BUY":
                    continue
                title = r.get("title", "")
                cat = clasificar(title, r.get("event_slug", ""))
                if cat is None:
                    continue
                try:
                    price = float(r["price"])
                    usd = float(r.get("usd_value") or 0)
                except (ValueError, KeyError):
                    continue
                if not (0 < price < 1):
                    continue
                outcome = (r.get("outcome") or "").strip().lower()
                out.append({
                    "wallet": r["wallet"].lower(), "condition_id": r["condition_id"],
                    "categoria": cat, "outcome": outcome, "price": price,
                    "ts": r.get("timestamp_utc", ""), "usd": usd,
                })
    return out


def cargar_trades_completo(vistos_hash: set):
    """18-Ago (tarde, petición explícita Javi tras el repaso a fondo del
    sniper): cargar_trades_whale() solo veía trades >=$1000 del firehose
    COMPARTIDO de cripto (filtro whale de fetch_polymarket_activity_ws.py)
    -- la inmensa mayoría de actividad sports/esports (trades pequeños)
    nunca llegaba ahí, sesgando el descubrimiento hacia generalistas de
    alto volumen. sports_activity_ws.py (mismo día, conexión propia sin
    ese filtro) ya lleva acumulando -- se fusiona aquí con el histórico
    whale (21 días) para ampliar cobertura sin perder profundidad
    histórica. Mismo formato de fila que cargar_trades_whale(), dedupe
    cruzado por transaction_hash (un trade whale puede aparecer en AMBAS
    fuentes)."""
    files = sorted(glob.glob(str(DIR_SPORTS / "activity_ws_*.csv")))
    out = []
    for path in files:
        with open(path, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                h = r.get("transaction_hash", "")
                if h in vistos_hash:
                    continue
                vistos_hash.add(h)
                if (r.get("side") or "").strip().upper() != "BUY":
                    continue
                cat = r.get("categoria", "")
                if not cat:
                    continue
                try:
                    price = float(r["price"])
                    usd = float(r.get("usd_value") or 0)
                except (ValueError, KeyError):
                    continue
                if not (0 < price < 1):
                    continue
                outcome = (r.get("outcome") or "").strip().lower()
                out.append({
                    "wallet": r["wallet"].lower(), "condition_id": r["condition_id"],
                    "categoria": cat, "outcome": outcome, "price": price,
                    "ts": r.get("timestamp_utc", ""), "usd": usd,
                })
    return out


def resolver_outcomes(condition_ids):
    """condition_id -> "yes"/"no" (lado ganador, normalizado) o None si no
    resuelto todavia. Batch de 20 por request (limite practico de query
    string), 3 req/s."""
    cids = sorted(set(condition_ids))
    resultado = {}
    BATCH = 20
    import json as _json
    for i in range(0, len(cids), BATCH):
        lote = cids[i:i + BATCH]
        params = [("condition_ids", c) for c in lote] + [("closed", "true")]
        try:
            r = requests.get(f"{GAMMA_API}/markets", params=params, timeout=20)
            r.raise_for_status()
            data = r.json()
        except Exception as e:
            print(f"  [error resolver] lote {i}: {e}", file=sys.stderr)
            continue
        for m in data:
            cid = m.get("conditionId") or m.get("condition_id")
            if not cid or not m.get("closed"):
                continue
            try:
                precios = _json.loads(m["outcomePrices"]) if isinstance(m.get("outcomePrices"), str) else m.get("outcomePrices")
                nombres = _json.loads(m["outcomes"]) if isinstance(m.get("outcomes"), str) else m.get("outcomes")
                precios = [float(p) for p in precios]
            except Exception:
                continue
            if not precios or not nombres or len(precios) != len(nombres):
                continue
            # nombre del outcome ganador (precio ~1.0) -- funciona igual para
            # binarios "Yes"/"No" que para head-to-head (nombre del luchador/equipo)
            ganador = None
            for nombre, p in zip(nombres, precios):
                if abs(p - 1.0) < 0.01:
                    ganador = nombre.strip().lower()
                    break
            if ganador:
                resultado[cid] = ganador
        time.sleep(0.3)
        if (i // BATCH) % 20 == 0:
            print(f"  resolviendo... {i}/{len(cids)}", file=sys.stderr)
    return resultado


def _shuffle_pvalue(n, precio_medio, hit_real, seed, n_shuffle=N_SHUFFLE):
    rng = np.random.default_rng(seed=seed)
    aciertos_sim = rng.binomial(n, precio_medio, size=n_shuffle)
    hit_sim = aciertos_sim / n
    dist_real = abs(hit_real - precio_medio)
    dist_sim = np.abs(hit_sim - precio_medio)
    return float(np.mean(dist_sim >= dist_real))


def _benjamini_hochberg(pvals, fdr=FDR):
    m = len(pvals)
    if m == 0:
        return []
    orden = sorted(range(m), key=lambda i: pvals[i])
    keep = [False] * m
    corte = -1
    for rank, idx in enumerate(orden, start=1):
        if pvals[idx] <= (rank / m) * fdr:
            corte = rank
    if corte > 0:
        for idx in orden[:corte]:
            keep[idx] = True
    return keep


def main():
    print("Cargando trades whale-tier de 21 dias de firehose (histórico)...")
    vistos = set()
    trades = cargar_trades_whale(vistos)
    print(f"trades whale-tier clasificados: {len(trades)}")
    print("Cargando trades completos de sports_activity_ws.py (sin filtro whale)...")
    trades_completo = cargar_trades_completo(vistos)
    print(f"trades adicionales (no-whale) clasificados: {len(trades_completo)}")
    trades = trades + trades_completo
    print(f"total combinado: {len(trades)}")
    por_cat = Counter(t["categoria"] for t in trades)
    print("por categoria:", dict(por_cat))

    print("\nResolviendo outcomes via gamma-api...")
    outcomes = resolver_outcomes([t["condition_id"] for t in trades])
    print(f"mercados resueltos: {len(outcomes)}")

    filas = []
    for t in trades:
        oc = outcomes.get(t["condition_id"])
        if oc is None:
            continue
        acierto = 1 if t["outcome"] == oc else 0
        filas.append({**t, "acierto": acierto})
    print(f"trades con outcome resuelto: {len(filas)}")
    if not filas:
        return

    # A) especialistas: >=80% de actividad (todas, no solo resueltas) en 1 categoria
    por_wallet_cat_n = defaultdict(Counter)
    for t in trades:
        por_wallet_cat_n[t["wallet"]][t["categoria"]] += 1
    especialistas = {}
    for w, cats in por_wallet_cat_n.items():
        total = sum(cats.values())
        top_cat, top_n = cats.most_common(1)[0]
        if total >= 5 and top_n / total >= 0.8:
            especialistas[w] = (top_cat, top_n, total)
    print(f"\nwallets especialistas (>=80% en 1 categoria, n>=5): {len(especialistas)}")

    # B) edge por (wallet, categoria), BH-FDR DENTRO de cada categoria
    print("\n=== EDGE VALIDADO POR WALLET x CATEGORIA (BH-FDR por categoria) ===")
    por_cat_wallet = defaultdict(lambda: defaultdict(list))
    for f in filas:
        por_cat_wallet[f["categoria"]][f["wallet"]].append(f)

    todas_significativas = []
    for cat, por_wallet in sorted(por_cat_wallet.items()):
        candidatas = {w: fs for w, fs in por_wallet.items() if len(fs) >= N_MIN}
        if not candidatas:
            continue
        filas_cat = []
        for w, fs in candidatas.items():
            n = len(fs)
            hit = sum(f["acierto"] for f in fs) / n
            precio_medio = sum(f["price"] for f in fs) / n
            seed = (hash((cat, w)) ^ n) & 0xFFFFFFFF
            p = _shuffle_pvalue(n, precio_medio, hit, seed)
            filas_cat.append({"categoria": cat, "wallet": w, "n": n, "hit": round(hit, 4),
                               "precio_medio": round(precio_medio, 4),
                               "edge_pp": round((hit - precio_medio) * 100, 3), "p_shuffle": p})
        pvals = [f["p_shuffle"] for f in filas_cat]
        keep = _benjamini_hochberg(pvals)
        n_sig = sum(keep)
        print(f"  {cat}: {len(candidatas)} wallets con n>={N_MIN}, {n_sig} significativas BH-FDR")
        for f, sig in zip(filas_cat, keep):
            if sig:
                f["especialista"] = f["wallet"] in especialistas
                todas_significativas.append(f)

    print(f"\n=== {len(todas_significativas)} (wallet,categoria) con edge validado BH-FDR ===")
    for f in sorted(todas_significativas, key=lambda x: -x["edge_pp"]):
        marca = " [ESPECIALISTA]" if f.get("especialista") else ""
        print(f"  {f['wallet'][:14]} {f['categoria']:10s} n={f['n']:4d} hit={f['hit']*100:.1f}% "
              f"precio_medio={f['precio_medio']:.3f} edge_pp={f['edge_pp']:+.2f} "
              f"p={f['p_shuffle']:.4f}{marca}")

    salida = {
        "actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "ventana_dias": 21,
        "n_trades_whale_clasificados": len(trades),
        "n_trades_resueltos": len(filas),
        "n_wallets_especialistas": len(especialistas),
        "por_categoria_n_trades": dict(por_cat),
        "wallets_validadas": [
            {"wallet": f["wallet"], "categoria": f["categoria"], "n": f["n"],
             "hit": f["hit"], "precio_medio": f["precio_medio"], "edge_pp": f["edge_pp"],
             "p_shuffle": round(f["p_shuffle"], 4), "especialista": bool(f.get("especialista"))}
            for f in todas_significativas
        ],
    }
    out_path = DIR_SPORTS / "wallet_edge_score_por_categoria.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(salida, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGuardado en {out_path}")


if __name__ == "__main__":
    main()
