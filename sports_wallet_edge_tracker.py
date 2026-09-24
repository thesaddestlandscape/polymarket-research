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
    ("NCAAF", re.compile(r'\bNCAAF\b|College Football', re.I)),
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
    # 02-Sep: premios individuales de fútbol -- ni título ni slug llevan
    # sigla de liga (ej. "ballon-dor-winner-2026"), no cubiertos por
    # ningún fallback de arriba/abajo. Lista finita y estable, cero
    # riesgo de colisión con política.
    ("Soccer_Awards", re.compile(
        r"ballon d.?or|golden boot|fifa best|uefa player of the year", re.I)),
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

# 02-Sep noche, petición explícita Javi tras "puede haber eventos que nos
# hemos perdido su seguimiento para live?": medido con el firehose whale
# REAL de hoy (polymarket_activity_2026-09-02.csv, filas sports puras) --
# **36,9% del volumen ($11,9M de $32,4M) devolvía cat=None** y se
# descartaba en silencio en 3 puntos (aquí, sports_activity_ws.py,
# sports_wallet_mirror_sniper.py -- este último YA con dinero real,
# DRY_RUN=False desde 31-Ago). Causa: NFL/MLB por nombre de equipo sin
# sigla de liga ("Patriots vs. Seahawks"), y sobre todo el fallback
# `_WILL_WIN_RE` de abajo solo cubría fútbol con patrón "will X win on Y"
# -- CUALQUIER otro partido real ("X vs Y", el 99% del volumen de fútbol/
# béisbol/cricket/etc real) nunca llegaba a clasificarse.
#
# Fix, verificado con `sports_spread_observer_fase0.py` (observador FASE
#0 sin dinero real, mismo día): sobre TODO el universo abierto de sports
# de gamma-api (tag_slug=sports+tennis, ~20k mercados), el prefijo de
# slug de Polymarket agrupa 100+ ligas reales (fútbol mundial completo,
# NPB/KBO/CPBL béisbol, cricket T20 por serie, lacrosse, tenis de mesa
# por jugador, esports) con CERO falsos positivos detectados en la
# auditoría manual completa de esa corrida. Se generaliza aquí el mismo
# mecanismo -- antes solo activo para el patrón "will X win on Y", ahora
# para cualquier título con " vs "/" vs. " -- con 2 guardas de seguridad
# baratas (`_NO_ES_DEPORTE_RE`) porque esta función es el ÚNICO filtro
# que separa sports del resto de la plataforma (política/legal/crypto)
# en el firehose sin filtrar de `sports_activity_ws.py`: un catch-all
# ciego podría colar un mercado no-deportivo ("X vs Y" de un caso legal,
# un debate político) al sniper de dinero real. NFL/MLB no necesitan
# lista de equipos aparte -- ya se resuelven arriba vía el chequeo de
# slug contra CATEGORIAS (slug "nfl-.../mlb-..." matchea `\bNFL\b`/
# `\bMLB\b` directamente); ver comentario junto a `_VS_RE` sobre por qué
# se descartó la lista de nombres de equipo (3 rondas de /code-review).
_VS_RE = re.compile(r'\bvs\.?\b', re.I)
_NO_ES_DEPORTE_RE = re.compile(
    r'\blawsuit\b|\bcase\b|\bv\.\s|\bdebate\b|\belection\b|\bpresident\b|'
    r'\bsenate\b|\bcongress\b|\bpeace\b|\bwar\b|\bcombo\b|\bshutdown\b',
    re.I)
# 02-Sep, 3 rondas de /code-review: el primer intento de este fix incluía
# listas de nombres de equipo NFL/MLB para conservar el nombre humano
# ("NFL"/"MLB") en vez de "Liga-nfl"/"Liga-mlb" -- descartado por
# completo. Cada ronda encontró una colisión real entre ligas distintas
# con el mismo nombre de equipo (Giants NFL/MLB, Cardinals NFL/MLB,
# Rangers MLB/NHL/fútbol escocés, Panthers NFL/NHL) que un simple
# `if team in title` no puede distinguir -- superficie de bugs sin fondo,
# nunca demostrablemente completa. Con `event_slug` presente (caso común,
# verificado con datos reales del firehose) el chequeo de slug contra
# CATEGORIAS de arriba YA resuelve NFL/MLB sin ambigüedad (slug
# "nfl-ne-sea-..."/"mlb-det-cle-..." matchea `\bNFL\b`/`\bMLB\b`
# literalmente). Sin slug, el fallback genérico `Liga-<prefijo>` de abajo
# es la respuesta correcta -- no comprometerse con una liga concreta que
# no se puede verificar, mejor no clasificar que clasificar mal con
# dinero real de por medio (alimenta sports_wallet_mirror_sniper.py,
# DRY_RUN=False desde 31-Ago).


def clasificar(title, event_slug=""):
    for nombre, rx in CATEGORIAS:
        if rx.search(title):
            return nombre
    # 02-Sep, petición explícita Javi ("y además ganará Alcaraz el US
    # Open???/igual que ganará Vinicius el Balón de Oro???"): futuros de
    # un solo competidor ("Will Alcaraz win the 2026 US Open?") no tienen
    # "vs" en el título (el gate `_VS_RE` de abajo no los alcanza) y el
    # título tampoco lleva la sigla de liga -- pero el SLUG casi siempre
    # sí ("2026-mens-us-open-winner-tennis", "nba-2027-champion",
    # "mlb-2026-nl-mvp", "f1-italian-grand-prix-..."). Comprobar el slug
    # contra la MISMA lista CATEGORIAS ya vetada (nunca una lista nueva)
    # es seguro por construcción -- verificado contra 29 slugs políticos
    # reales del mismo día (*-senate-election-winner, *-presidential-
    # nominee-2028, *-parliamentary-election-winner...): NINGUNO contiene
    # ninguna palabra de CATEGORIAS, cero riesgo de colar política/legal
    # como deporte (a diferencia de un blacklist de política, que nunca
    # puede garantizarse completo).
    for nombre, rx in CATEGORIAS:
        if rx.search(event_slug or ""):
            return nombre
    # 10-Sep (petición explícita Javi, "ponle nombres claros ya para no
    # liarte más adelante" -- hallazgo real: "Soccer-epl"/"Liga-epl" NO
    # eran ligas distintas ni un bug de clasificación duplicada, eran el
    # MISMO partido separado por TIPO DE MERCADO -- verificado con datos
    # reales: epl-liv-ful-2026-09-12 generaba "Will Liverpool FC win..."
    # (moneyline) Y "Will...end in a draw?"/"O/U Total Corners" (resto)
    # bajo dos prefijos que parecían dos ligas. Renombrado para que el
    # nombre diga lo que es: "{liga}-ganador" (moneyline, "will X win")
    # vs "{liga}-otros" (empate/O-U/córners/spread, todo lo demás con
    # "vs" en el título). Migración de data/sports/*.json con nombres
    # viejos hecha el mismo día, ver migrar_nombres_categoria_sports_10sep.py.
    if _WILL_WIN_RE.search(title):
        m = _SLUG_PREFIX_RE.match(event_slug or "")
        liga = m.group(1) if m else "otra"
        return f"{liga}-ganador"
    if not _VS_RE.search(title) or _NO_ES_DEPORTE_RE.search(title):
        return None
    m = _SLUG_PREFIX_RE.match(event_slug or "")
    liga = m.group(1) if m else "otra"
    return f"{liga}-otros"


def _clave_tx(h: str):
    """24-Sep: dedupe por transaction_hash con 64 bits (int) en vez del string
    de 66 chars -- el set de ~4M hashes era ~600 MB. Colisión despreciable
    (~4M^2/2^65). Mismo comportamiento que antes para hashes vacíos/raros
    (se deduplican por su string literal, incluido "")."""
    if len(h) >= 18 and h[:2] == "0x":
        try:
            return int(h[2:18], 16)
        except ValueError:
            pass
    return h


def _acumular(agg: dict, wallet, cid, cat, outcome, price):
    """24-Sep (OOM-kill cada corrida desde 21-Sep, 5,7 GB): en vez de una
    lista de ~4M dicts (+ copia {**t} de otros 3,4M), se agrega en streaming
    por (wallet, categoria, condition_id, outcome) -> [n, suma_precio].
    Es todo lo que main() necesita (n/hit/precio_medio por wallet×categoria,
    conteos por categoria/especialista, set de condition_ids)."""
    k = (sys.intern(wallet), sys.intern(cat), sys.intern(cid), sys.intern(outcome))
    v = agg.get(k)
    if v is None:
        agg[k] = [1, price]
    else:
        v[0] += 1
        v[1] += price


def cargar_trades_whale(vistos: set, agg: dict) -> int:
    """Acumula en `agg` los trades whale-tier (ver _acumular); devuelve cuántos
    se clasificaron. Dedupe por transaction_hash; `vistos` compartido con
    cargar_trades_completo() para dedupe CRUZADO entre las dos fuentes (un
    trade whale puede aparecer en ambas, 18-Ago)."""
    files = sorted(glob.glob(f"{DATALOGS}/polymarket_activity_*.csv*"))
    n = 0
    for path in files:
        opener = gzip.open if path.endswith(".gz") else open
        with opener(path, "rt") as f:
            for r in csv.DictReader(f):
                if r.get("activo"):
                    continue
                h = _clave_tx(r.get("transaction_hash", ""))
                if h in vistos:
                    continue
                vistos.add(h)
                if (r.get("side") or "").strip().upper() != "BUY":
                    continue
                cat = clasificar(r.get("title", ""), r.get("event_slug", ""))
                if cat is None:
                    continue
                try:
                    price = float(r["price"])
                except (ValueError, KeyError):
                    continue
                if not (0 < price < 1):
                    continue
                _acumular(agg, r["wallet"].lower(), r["condition_id"], cat,
                          (r.get("outcome") or "").strip().lower(), price)
                n += 1
    return n


def cargar_trades_completo(vistos_hash: set, agg: dict) -> int:
    """18-Ago (tarde, petición explícita Javi tras el repaso a fondo del
    sniper): cargar_trades_whale() solo veía trades >=$1000 del firehose
    COMPARTIDO de cripto (filtro whale de fetch_polymarket_activity_ws.py)
    -- la inmensa mayoría de actividad sports/esports (trades pequeños)
    nunca llegaba ahí, sesgando el descubrimiento hacia generalistas de
    alto volumen. sports_activity_ws.py (conexión propia sin ese filtro) se
    fusiona aquí con el histórico whale, dedupe cruzado por
    transaction_hash. 24-Sep: acumula en `agg` (streaming), ver _acumular."""
    # 23-Sep: *.csv* (no solo *.csv) -- comprimir_data_historica.sh ahora
    # rota activity_ws_*.csv a .gz igual que el resto de directorios de
    # data/ (ver feedback_disco_activity_ws_sports_sin_rotar_23sep).
    files = sorted(glob.glob(str(DIR_SPORTS / "activity_ws_*.csv*")))
    n = 0
    for path in files:
        opener = gzip.open if path.endswith(".gz") else open
        with opener(path, "rt", newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                h = _clave_tx(r.get("transaction_hash", ""))
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
                except (ValueError, KeyError):
                    continue
                if not (0 < price < 1):
                    continue
                _acumular(agg, r["wallet"].lower(), r["condition_id"], cat,
                          (r.get("outcome") or "").strip().lower(), price)
                n += 1
    return n


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
    agg = {}
    n_whale = cargar_trades_whale(vistos, agg)
    print(f"trades whale-tier clasificados: {n_whale}")
    print("Cargando trades completos de sports_activity_ws.py (sin filtro whale)...")
    n_completo = cargar_trades_completo(vistos, agg)
    del vistos  # ya no hace falta (era el mayor consumidor tras la lista de trades)
    print(f"trades adicionales (no-whale) clasificados: {n_completo}")
    n_trades = n_whale + n_completo
    print(f"total combinado: {n_trades} ({len(agg)} claves agregadas wallet×cat×mercado×outcome)")
    por_cat = Counter()
    for (_w, cat, _c, _o), (n, _sp) in agg.items():
        por_cat[cat] += n
    print("por categoria:", dict(por_cat))

    print("\nResolviendo outcomes via gamma-api...")
    outcomes = resolver_outcomes({k[2] for k in agg})
    print(f"mercados resueltos: {len(outcomes)}")

    # (cat, wallet) -> [n, aciertos, suma_precio] solo sobre trades resueltos
    res_cat_wallet = defaultdict(lambda: [0, 0, 0.0])
    n_resueltos = 0
    for (w, cat, cid, outcome), (n, sp) in agg.items():
        oc = outcomes.get(cid)
        if oc is None:
            continue
        v = res_cat_wallet[(cat, w)]
        v[0] += n
        v[1] += n if outcome == oc else 0
        v[2] += sp
        n_resueltos += n
    print(f"trades con outcome resuelto: {n_resueltos}")
    if not n_resueltos:
        return

    # A) especialistas: >=80% de actividad (todas, no solo resueltas) en 1 categoria
    por_wallet_cat_n = defaultdict(Counter)
    for (w, cat, _c, _o), (n, _sp) in agg.items():
        por_wallet_cat_n[w][cat] += n
    del agg
    especialistas = {}
    for w, cats in por_wallet_cat_n.items():
        total = sum(cats.values())
        top_cat, top_n = cats.most_common(1)[0]
        if total >= 5 and top_n / total >= 0.8:
            especialistas[w] = (top_cat, top_n, total)
    del por_wallet_cat_n
    print(f"\nwallets especialistas (>=80% en 1 categoria, n>=5): {len(especialistas)}")

    # B) edge por (wallet, categoria), BH-FDR DENTRO de cada categoria
    print("\n=== EDGE VALIDADO POR WALLET x CATEGORIA (BH-FDR por categoria) ===")
    por_cat_wallet = defaultdict(dict)
    for (cat, w), v in res_cat_wallet.items():
        por_cat_wallet[cat][w] = v
    del res_cat_wallet

    todas_significativas = []
    for cat, por_wallet in sorted(por_cat_wallet.items()):
        candidatas = {w: v for w, v in por_wallet.items() if v[0] >= N_MIN}
        if not candidatas:
            continue
        filas_cat = []
        for w, (n, aciertos, suma_precio) in candidatas.items():
            hit = aciertos / n
            precio_medio = suma_precio / n
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
        "n_trades_whale_clasificados": n_trades,
        "n_trades_resueltos": n_resueltos,
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
