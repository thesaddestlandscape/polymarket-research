#!/usr/bin/env python3
"""sports_seleccion_wallets_persistentes.py -- universo DIARIO de wallets que ganan de forma persistente en SPORTS,
elegido por PnL NETO de comisión y validado FORWARD (Javi 30-Sep: "soluciona esto igual que hemos hecho en cripto").
Gemelo de seleccion_tomadores_persistentes.py.

Por qué existe: el pool de sports (sports_wallet_edge_tracker.py, cada 6 h) valida cada wallet x categoría DENTRO de
la misma ventana de 21 días, al precio que pagó la wallet, sin comisión y sin forward. Medido el 30-Sep al ask real:
las señales de ese pool dan -2,5 % por € (5/36 días positivos) y seguir o contradecir da lo mismo.

Qué hace (cron diario, solo lectura de datos de mercado; NO cambia qué wallets opera nadie):
 1. Caché por DÍA cerrado del firehose (data/sports/activity_ws_*.csv[.gz]): posición neta por
    (wallet, mercado, lado, categoría): compras y ventas en acciones y en USD. Cada día se procesa una sola vez.
 2. Desenlace OFICIAL de todos los mercados (gamma-api con closed=true, caché persistente) y fecha de cierre.
    Se reporta la cobertura; un mercado sin desenlace oficial no entra (no se infiere de los últimos trades).
 3. PnL a resolución de cada posición, NETO: comisión de sports 5 % x (1 - precio) sobre lo comprado, SOLO si gana
    (se cobra a toda compra ganadora: el firehose no distingue maker de tomador, así que es conservador).
 4. Selección para el día D con los VENTANA días anteriores, usando solo posiciones cuyo mercado CERRÓ antes de D:
    wallet x categoría con >=POS_MIN posiciones, >=DIAS_MIN días activos, >=VOL_MIN USD, neto >0 y >=FRAC_POS de
    sus días activos en positivo.  Criterios FIJADOS el 30-Sep antes de mirar ningún resultado; no se retocan.
 5. Validación FORWARD: las elegidas para D, medidas en las posiciones que ABREN en D (su propio PnL neto por USD,
    % que repite en positivo), frente al resto de wallets x categoría con la misma actividad mínima ese día.
 6. Universo de hoy -> data/sports/wallets_persistentes_universo.json, con su solape con el pool actual.

Lo que NO mide todavía: el EV de copiarlas a NUESTRO ask con NUESTRA latencia. El dry-run de sports solo registra
las wallets del pool actual; añadir estas como candidatas de observación toca sports_wallet_mirror_sniper.py
(ejecutor con envío real) -> /code-review + OK de Javi.  Gate para proponer algo con dinero: celda con n>=40,
>=10 días, EV>=+0,10 por € al ask real, IC90 por días >0 y wallet top <=30 %.

Mercados `completed-match` excluidos: ahí el precio queda registrado en el lado equivocado (trampa 30-Sep).
Disco: caché en /root/polymarket-research-datalogs/sports_tomadores_cache (gz, retención RETENCION_DIAS, fuera de git).
"""
import csv
import glob
import gzip
import json
import os
import random
import sys
import time
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO = Path("/root/polymarket-research")
sys.path.insert(0, str(REPO))
DIR_SPORTS = REPO / "data" / "sports"
CACHE_DIR = Path("/root/polymarket-research-datalogs/sports_tomadores_cache")
DESENLACES = CACHE_DIR / "desenlaces.json"
DIR_OUT = Path(os.environ.get("SPORTS_PERSISTENTES_OUT", str(DIR_SPORTS)))
UNIVERSO = DIR_OUT / "wallets_persistentes_universo.json"
INFORME = DIR_OUT / "wallets_persistentes_informe.json"
POOL_ACTUAL = DIR_SPORTS / "wallet_edge_score_por_categoria.json"
FEE = 0.05                                                   # sports, solo en ganadoras
VENTANA, POS_MIN, DIAS_MIN, VOL_MIN, FRAC_POS = 14, 30, 5, 200.0, 0.60     # FIJADOS 30-Sep, no tocar
ACT_MIN_DIA = 3                                              # posiciones ese día para entrar en la medición forward
RETENCION_DIAS = 45
GATE_DIAS = 10
MAX_PETICIONES = 6000                                        # tope de peticiones a gamma por ejecución


def _abrir(ruta: str):
    return gzip.open(ruta, "rt", errors="replace", newline="") if ruta.endswith(".gz") else open(ruta, errors="replace", newline="")


def _cache_dia(dia: str, ruta: str) -> Path:
    """Agrega un día del firehose a posiciones netas. Devuelve la ruta del caché (lo crea si no existe)."""
    dst = CACHE_DIR / f"pos_{dia}.csv.gz"
    if dst.exists():
        return dst
    pos = {}
    with _abrir(ruta) as f:
        rd = csv.reader(f)
        h = next(rd)
        ix = {c: h.index(c) for c in h}
        ic, icat, isd, ioi, iw, isz, iusd, isl = (ix[c] for c in ("condition_id", "categoria", "side", "outcome_index", "wallet", "size", "usd_value", "market_slug"))
        for r in rd:
            try:
                if r[ioi] not in ("0", "1") or "completed-match" in r[isl]:
                    continue
                sz, usd = float(r[isz]), float(r[iusd])
                if sz <= 0 or usd <= 0:
                    continue
                k = (r[iw].lower(), r[ic], r[ioi], r[icat])
                p = pos.get(k)
                if p is None:
                    p = pos[k] = [0.0, 0.0, 0.0, 0.0, 0]
                if r[isd] == "BUY":
                    p[0] += sz
                    p[1] += usd
                elif r[isd] == "SELL":
                    p[2] += sz
                    p[3] += usd
                p[4] += 1
            except (ValueError, IndexError):
                continue
    tmp = dst.with_name(dst.name + f".tmp{os.getpid()}")
    with gzip.open(tmp, "wt", newline="") as f:
        w = csv.writer(f)
        w.writerow(["wallet", "condition_id", "outcome_index", "categoria", "buy_sh", "buy_usd", "sell_sh", "sell_usd", "fills"])
        for (wa, c, oi, cat), p in pos.items():
            w.writerow([wa, c, oi, cat, round(p[0], 4), round(p[1], 4), round(p[2], 4), round(p[3], 4), p[4]])
    tmp.replace(dst)
    return dst


def _leer_cache(ruta: Path):
    with gzip.open(ruta, "rt", newline="") as f:
        rd = csv.reader(f)
        next(rd)
        for r in rd:
            yield r[0], r[1], r[2], r[3], float(r[4]), float(r[5]), float(r[6]), float(r[7])


def _actualizar_desenlaces(des: dict, cids: set, hoy: str) -> int:
    """Pide a gamma (closed=true) los mercados sin desenlace. des[cid] = [ganador '0'/'1'/'X', dia_cierre].
    Los que aún no han cerrado se reintentan como mucho una vez al día (des['_intento'][cid] = día)."""
    import requests
    intento = des.setdefault("_intento", {})
    faltan = [c for c in cids if c not in des and intento.get(c) != hoy]
    s, pet = requests.Session(), 0
    for i in range(0, len(faltan), 20):
        if pet >= MAX_PETICIONES:
            break
        lote = faltan[i:i + 20]
        for _ in range(3):
            try:
                r = s.get("https://gamma-api.polymarket.com/markets",
                          params=[("condition_ids", c) for c in lote] + [("closed", "true"), ("limit", "50")], timeout=15)
                pet += 1
                if r.status_code == 200:
                    for m in r.json():
                        pr = m.get("outcomePrices")
                        pr = json.loads(pr) if isinstance(pr, str) else pr
                        if not pr or len(pr) != 2:
                            continue
                        a, b = float(pr[0]), float(pr[1])
                        g = "0" if a >= 0.99 and b <= 0.01 else "1" if b >= 0.99 and a <= 0.01 else "X"
                        cierre = (m.get("closedTime") or m.get("endDate") or "")[:10]
                        des[m["conditionId"]] = [g, cierre]
                    break
                time.sleep(1.5)
            except Exception:
                time.sleep(1.5)
        for c in lote:
            if c not in des:
                intento[c] = hoy
        time.sleep(0.1)
        if pet % 500 == 0:
            _guardar(DESENLACES, des)
            print(f"  desenlaces: {pet} peticiones, {len(des) - 1} mercados resueltos", flush=True)
    return pet


def _guardar(ruta: Path, obj) -> None:
    tmp = ruta.with_name(ruta.name + f".tmp{os.getpid()}")
    tmp.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")
    tmp.replace(ruta)


def _ic90(por_dia: dict):
    """IC90 por días del cociente suma(pnl)/suma(usd). por_dia[d] = (pnl, usd)."""
    ks = [k for k, v in por_dia.items() if v[1] > 0]
    if len(ks) < 4:
        return None
    rng, ms = random.Random(7), []
    for _ in range(2000):
        sel = [rng.choice(ks) for _ in ks]
        ms.append(sum(por_dia[k][0] for k in sel) / sum(por_dia[k][1] for k in sel))
    ms.sort()
    return [round(ms[100], 4), round(ms[1899], 4)]


def _res(por_dia: dict) -> dict:
    pnl, usd = sum(v[0] for v in por_dia.values()), sum(v[1] for v in por_dia.values())
    if usd <= 0:
        return {"dias": 0}
    ds = sorted(por_dia, key=lambda d: -por_dia[d][0])
    r_pnl, r_usd = sum(por_dia[d][0] for d in ds[2:]), sum(por_dia[d][1] for d in ds[2:])
    return {"dias": len(por_dia), "usd": round(usd), "pnl_neto": round(pnl), "roi_neto": round(pnl / usd, 4), "ic90_dias": _ic90(por_dia),
            "dias_positivos": sum(1 for v in por_dia.values() if v[0] > 0),
            "roi_sin_2_mejores_dias": round(r_pnl / r_usd, 4) if r_usd > 0 else None}


def main() -> int:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    hoy = datetime.now(timezone.utc).date().isoformat()
    ficheros = {}
    for p in sorted(glob.glob(str(DIR_SPORTS / "activity_ws_*.csv*"))):
        d = Path(p).name[len("activity_ws_"):len("activity_ws_") + 10]
        if d < hoy:
            ficheros[d] = p
    caches = {p.name[4:14]: p for p in CACHE_DIR.glob("pos_*.csv.gz")}
    for d, p in ficheros.items():
        if d not in caches:
            caches[d] = _cache_dia(d, p)
            print(f"caché {d} creado", flush=True)
    limite = (date.fromisoformat(hoy) - timedelta(days=RETENCION_DIAS)).isoformat()
    for d in [d for d in caches if d < limite]:
        caches.pop(d).unlink()
    dias = sorted(caches)

    des = json.loads(DESENLACES.read_text()) if DESENLACES.exists() else {}
    cids = set()
    for d in dias:
        for _, c, *_ in _leer_cache(caches[d]):
            cids.add(c)
    pet = _actualizar_desenlaces(des, cids, hoy)
    _guardar(DESENLACES, des)

    # agregado (wallet, categoría, día de apertura, día de cierre) -> [pnl neto, usd comprados, posiciones]
    agg = defaultdict(lambda: [0.0, 0.0, 0])
    cob = {}
    for d in dias:
        tot = con = 0
        for w, c, oi, cat, bsh, busd, ssh, susd in _leer_cache(caches[d]):
            tot += 1
            x = des.get(c)
            if not x:
                continue
            con += 1
            g = x[0]
            if g == "X":
                continue
            gana = g == oi
            pnl = (bsh if gana else 0.0) - busd + susd - (ssh if gana else 0.0)
            if gana and bsh > 0:
                pnl -= FEE * (1 - min(busd / bsh, 1.0)) * busd
            a = agg[(w, cat, d, max(x[1] or d, d))]
            a[0] += pnl
            a[1] += busd
            a[2] += 1
        cob[d] = round(con / tot, 3) if tot else None

    por_apertura = defaultdict(list)             # día de apertura -> [(wallet, cat, día cierre, pnl, usd, npos)]
    for (w, cat, d, dc), (pnl, usd, n) in agg.items():
        por_apertura[d].append((w, cat, dc, pnl, usd, n))

    def seleccionar(dia_d: str) -> dict:
        d0 = date.fromisoformat(dia_d)
        prev = [(d0 - timedelta(days=k)).isoformat() for k in range(1, VENTANA + 1)]
        acc = defaultdict(lambda: defaultdict(lambda: [0.0, 0.0, 0]))
        for p in prev:
            for w, cat, dc, pnl, usd, n in por_apertura.get(p, ()):
                if dc < dia_d:                   # el mercado ya había cerrado antes de D: sin fuga
                    a = acc[(w, cat)][p]
                    a[0] += pnl
                    a[1] += usd
                    a[2] += n
        sel = {}
        for k, pd in acc.items():
            pnl, usd, n = (sum(v[i] for v in pd.values()) for i in range(3))
            if n >= POS_MIN and len(pd) >= DIAS_MIN and usd >= VOL_MIN and pnl > 0 and \
                    sum(1 for v in pd.values() if v[0] > 0) >= FRAC_POS * len(pd):
                sel[k] = {"pnl_neto": round(pnl, 2), "usd": round(usd, 2), "roi_neto": round(pnl / usd, 4), "posiciones": n,
                          "dias_activos": len(pd), "dias_positivos": sum(1 for v in pd.values() if v[0] > 0)}
        return sel

    fwd = {"elegidas": {}, "resto": {}}
    repite, detalle = [], []
    for d in dias:
        if d < (date.fromisoformat(dias[0]) + timedelta(days=DIAS_MIN)).isoformat():
            continue
        sel = seleccionar(d)
        if not sel:
            continue
        hoy_d = defaultdict(lambda: [0.0, 0.0, 0])
        for w, cat, dc, pnl, usd, n in por_apertura.get(d, ()):
            a = hoy_d[(w, cat)]
            a[0] += pnl
            a[1] += usd
            a[2] += n
        e = [v for k, v in hoy_d.items() if k in sel and v[2] >= ACT_MIN_DIA and v[1] > 0]
        r = [v for k, v in hoy_d.items() if k not in sel and v[2] >= ACT_MIN_DIA and v[1] > 0]
        if e:
            fwd["elegidas"][d] = (sum(v[0] for v in e), sum(v[1] for v in e))
            repite.append(sum(1 for v in e if v[0] > 0) / len(e))
        if r:
            fwd["resto"][d] = (sum(v[0] for v in r), sum(v[1] for v in r))
        detalle.append({"dia": d, "elegidas": len(sel), "activas": len(e), "cobertura_desenlace": cob.get(d),
                        "roi_elegidas": round(fwd["elegidas"][d][0] / fwd["elegidas"][d][1], 4) if e else None,
                        "roi_resto": round(fwd["resto"][d][0] / fwd["resto"][d][1], 4) if r else None})

    universo = seleccionar(hoy)
    pool = set()
    if POOL_ACTUAL.exists():
        try:
            pool = {(x["wallet"].lower(), x["categoria"]) for x in json.loads(POOL_ACTUAL.read_text()).get("wallets_validadas", [])}
        except (ValueError, KeyError):
            pass
    por_cat = defaultdict(int)
    for (_, cat) in universo:
        por_cat[cat] += 1
    res_e, res_r = _res(fwd["elegidas"]), _res(fwd["resto"])
    # las últimas jornadas tienen mercados aún sin cerrar: se dicen, no se esconden
    veredicto = ("PERSISTEN fuera de muestra" if res_e.get("dias", 0) >= GATE_DIAS and res_e.get("ic90_dias") and res_e["ic90_dias"][0] > 0
                 else "positivo sin IC suficiente" if res_e.get("roi_neto", 0) > 0 else "no persisten")
    _guardar(UNIVERSO, {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                        "criterio": f"ventana {VENTANA} d, >={POS_MIN} posiciones, >={DIAS_MIN} días activos, >={VOL_MIN:.0f} USD, neto de comisión >0, >={FRAC_POS:.0%} días + (fijado 30-Sep)",
                        "wallets": [{"wallet": w, "categoria": cat, "en_pool_actual": (w, cat) in pool, **v}
                                    for (w, cat), v in sorted(universo.items(), key=lambda kv: -kv[1]["pnl_neto"])]})
    informe = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "dias_cache": len(dias),
               "mercados": len(cids), "con_desenlace_oficial": sum(1 for c in cids if c in des), "peticiones_gamma": pet,
               "universo_hoy": len(universo), "universo_en_pool_actual": sum(1 for k in universo if k in pool), "pool_actual": len(pool),
               "universo_por_categoria": dict(sorted(por_cat.items(), key=lambda kv: -kv[1])[:15]),
               "forward_elegidas": res_e, "forward_resto": res_r,
               "pct_medio_que_repite_en_positivo": round(sum(repite) / len(repite), 3) if repite else None,
               "veredicto": veredicto, "por_dia": detalle}
    _guardar(INFORME, informe)

    def _l(n, r):
        return (f"{n}: {r['dias']} días, {r['usd']:,} USD, ROI neto {r['roi_neto']:+.2%} IC90 {r['ic90_dias']} "
                f"({r['dias_positivos']}/{r['dias']} días +; sin los 2 mejores {r['roi_sin_2_mejores_dias']})" if r.get("dias") else f"{n}: sin datos")
    lineas = [f"🎯 SPORTS wallets persistentes (neto de comisión, forward) — {len(dias)} días de firehose",
              f"Desenlace oficial: {informe['con_desenlace_oficial']:,}/{len(cids):,} mercados ({informe['con_desenlace_oficial'] / max(len(cids), 1):.0%})",
              f"Universo de hoy: {len(universo)} wallet x categoría; solo {informe['universo_en_pool_actual']} están en el pool actual ({len(pool)} entradas)",
              "Top categorías: " + ", ".join(f"{c} {n}" for c, n in list(informe["universo_por_categoria"].items())[:8]),
              _l("FORWARD elegidas (su propio PnL el día siguiente)", res_e),
              _l("FORWARD resto con la misma actividad", res_r),
              f"Repiten en positivo: {informe['pct_medio_que_repite_en_positivo']}",
              f"Veredicto: {veredicto}. Solo observación. Falta medir copiarlas a NUESTRO ask (exige tocar el sniper: /code-review + OK)."]
    print("\n".join(lineas))
    if "--telegram" in sys.argv:
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram("\n".join(lineas), bot="sports")
        except Exception as e:
            print(f"(telegram falló: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
