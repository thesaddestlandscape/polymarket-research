#!/usr/bin/env python3
"""seleccion_tomadores_persistentes.py -- universo DIARIO de tomadores que ganan de forma
persistente en up/down cripto 5/15 min, y medición de lo que vale copiarlos (Javi 30-Sep:
"tenemos que controlar todo el universo y solo fiarnos de las mejores").

Por qué existe: el universo de bots (bot_wallets_universo_25ago.json) está fijo desde el 24-Ago
y el de Wallet Mirror se elige por acierto frente al 50 %, no por PnL neto. Medido el 30-Sep:
de las 90 tomadoras agresivas con neto>0 y >=5/6 días positivos (21-26 Sep), solo 7 estaban en
el universo de bots y 6 en las operativas de Wallet Mirror; fuera de muestra (27-29 Sep)
siguieron ganando (+0,74 % de su volumen, 58 % repite).

Qué hace (cron diario, solo lectura de datos de mercado):
 1. Perfil por DÍA cerrado de todas las wallets del firehose (caché por día: cada día se
    procesa una sola vez): fills, volumen, PnL a resolución, volumen agresivo (precio por encima
    del mid del último snapshot <=20 s) y fee estimado de tomador.
 2. Selección con los últimos VENTANA_DIAS días cerrados: >=N_MIN fills, >=MERC_MIN mercados,
    >=70 % agresiva, neto de fee >0 y >=DIAS_POS_MIN días positivos.
    -> data/shadow/tomadores_persistentes_universo.json (lo lee tomadores_persistentes_fase0.py).
 3. Validación FORWARD honesta: para cada día D ya cerrado, las seleccionadas con los días
    ANTERIORES a D, medidas en D (su propio PnL y % que repite). Nunca se mide en los días
    con los que se eligió.
 4. Si existe la captura del observador con latencia real (tomadores_persistentes_fase0_*.csv),
    EV de copiarlas al ask real por marco x bucket de precio x moneda, con IC90 por días.
 5. Resumen por Telegram con --telegram. Comprime/caduca los CSV diarios del observador.

Gate para proponer algo con dinero (decisión de Javi + checklist + /code-review): celda con
n>=40, >=10 días, EV>=+0,10 por € al ask real, IC90 por días >0 y wallet top <=30 %.
"""
import bisect
import csv
import gzip
import json
import random
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
DATALOGS = Path("/root/polymarket-research-datalogs")
CACHE_DIR = DATALOGS / "tomadores_cache"
UNIVERSO = DIR_SHADOW / "tomadores_persistentes_universo.json"
INFORME = DIR_SHADOW / "tomadores_persistentes_informe.json"
MARCOS = ("5min", "15min")
VENTANA_DIAS = 6
N_MIN, MERC_MIN, DIAS_POS_MIN, AGR_MIN, COB_MIN = 500, 200, 5, 70.0, 0.15
FILLS_MIN_CACHE = 30          # por día: wallets con menos fills no se guardan en el caché
FEE = 0.07
RETENCION_OBS_DIAS = 21


def _abrir(p: Path):
    return gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")


def _ruta(directorio: Path, prefijo: str, dia: str):
    for c in (directorio / f"{prefijo}_{dia}.csv", directorio / f"{prefijo}_{dia}.csv.gz"):
        if c.exists():
            return c
    return None


def _ts(s: str) -> float:
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


def _desenlaces(dia: str) -> dict:
    out = {}
    p = _ruta(DIR_SHADOW, "resolution_sniper_obs", dia)
    if p:
        with _abrir(p) as f:
            for r in csv.DictReader(f):
                if r.get("outcome_real") in ("Up", "Down"):
                    out[r["slug"]] = r["outcome_real"]
    return out


def perfil_dia(dia: str):
    """{wallet: [n, vol, pnl, fee_est, vol_agresivo, vol_clasificado, n_mercados, precio*vol]} o None."""
    cache = CACHE_DIR / f"perfil_{dia}.json"
    if cache.exists():
        try:
            return json.loads(cache.read_text())
        except Exception:
            pass
    p_act, p_lib = _ruta(DATALOGS, "polymarket_activity", dia), _ruta(DATALOGS, "libro_ambos_lados", dia)
    out = _desenlaces(dia)
    if not (p_act and p_lib and out):
        return None
    mids = defaultdict(list)
    with _abrir(p_lib) as f:
        for r in csv.DictReader(f):
            if r.get("marco") not in MARCOS:
                continue
            try:
                b, a = float(r["bid_yes"]), float(r["ask_yes"])
            except (ValueError, TypeError):
                continue
            if 0 < b <= a < 1:
                mids[r["condition_id"]].append((_ts(r["timestamp_utc"]), (a + b) / 2))
    mt = {}
    for c, v in mids.items():
        v.sort()
        mt[c] = ([t for t, _ in v], [m for _, m in v])
    del mids
    W = defaultdict(lambda: [0, 0.0, 0.0, 0.0, 0.0, 0.0, set(), 0.0, 0.0])
    with _abrir(p_act) as f:
        for r in csv.DictReader(f):
            if r.get("categoria_updown_tracked") != "1" or r.get("marco") not in MARCOS:
                continue
            g = out.get(r["market_slug"])
            if g is None or r["outcome"] not in ("Up", "Down"):
                continue
            try:
                s, p, t = float(r["size"]), float(r["price"]), _ts(r["timestamp_utc"])
            except (ValueError, TypeError):
                continue
            if s <= 0 or not 0 < p < 1:
                continue
            a = W[r["wallet"].lower()]
            sg = 1 if r["side"] == "BUY" else -1
            v = s * p
            a[0] += 1
            a[1] += v
            a[2] += sg * s * ((1.0 if r["outcome"] == g else 0.0) - p)
            a[6].add(r["market_slug"])
            a[7] += p * v
            m = mt.get(r["condition_id"])
            if m:
                i = bisect.bisect_right(m[0], t) - 1
                if i >= 0 and t - m[0][i] <= 20:
                    mid = m[1][i] if r["outcome"] == "Up" else 1 - m[1][i]
                    a[5] += v
                    a[8] += v
                    if sg * (p - mid) > 0.004:
                        a[4] += v
                        a[3] += FEE * p * (1 - p) * s
    res = {w: [a[0], round(a[1], 2), round(a[2], 2), round(a[3], 3), round(a[4], 2), round(a[5], 2), len(a[6]), round(a[7], 2)]
           for w, a in W.items() if a[0] >= FILLS_MIN_CACHE}
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(res))
    return res


def combinar(perfiles: dict) -> dict:
    """perfiles {dia: perfil} -> {wallet: stats de la ventana}"""
    acc = {}
    for dia, per in perfiles.items():
        for w, (n, vol, pnl, fee, agr, cl, merc, pv) in per.items():
            a = acc.setdefault(w, dict(n=0, vol=0.0, pnl=0.0, fee=0.0, agr=0.0, cl=0.0, merc=0, pv=0.0, dpos=0, nd=0))
            a["n"] += n
            a["vol"] += vol
            a["pnl"] += pnl
            a["agr"] += agr
            a["cl"] += cl
            a["merc"] += merc
            a["pv"] += pv
            # el fee se midió solo sobre el volumen con mid: se escala al volumen total del día
            a["fee"] += fee / cl * vol if cl > 0 else 0.0
            a["nd"] += 1
            a["dpos"] += 1 if pnl > 0 else 0
    return acc


def seleccionar(acc: dict) -> dict:
    sel = {}
    for w, a in acc.items():
        if a["n"] < N_MIN or a["merc"] < MERC_MIN or a["cl"] < COB_MIN * a["vol"] or a["cl"] <= 0:
            continue
        agr = a["agr"] / a["cl"] * 100
        neto = a["pnl"] - a["fee"]
        if agr >= AGR_MIN and neto > 0 and a["dpos"] >= DIAS_POS_MIN:
            sel[w] = dict(n=a["n"], vol=round(a["vol"]), neto=round(neto, 2), neto_pct_vol=round(neto / a["vol"] * 100, 2),
                          agresiva_pct=round(agr), mercados=a["merc"], precio_medio=round(a["pv"] / a["vol"], 3),
                          dias_positivos=f"{a['dpos']}/{a['nd']}")
    return sel


def dias_cerrados(n: int) -> list:
    hoy = datetime.now(timezone.utc).date()
    return [(hoy - timedelta(days=k)).strftime("%Y-%m-%d") for k in range(n, 0, -1)]


def _ic90_por_dias(por_dia: dict):
    ks = [k for k in por_dia if por_dia[k]]
    if len(ks) < 3:
        return None
    rng = random.Random(5)
    ms = []
    for _ in range(1000):
        s = [x for k in (rng.choice(ks) for _ in ks) for x in por_dia[k]]
        ms.append(sum(s) / len(s))
    ms.sort()
    return [round(ms[50], 4), round(ms[950], 4)]


def copia_con_latencia_real() -> dict:
    """EV de copiar, con la captura del observador (ask real en el instante de detección)."""
    celdas, total = defaultdict(lambda: defaultdict(list)), defaultdict(list)
    wallets_celda, lags, dias = defaultdict(lambda: defaultdict(int)), [], set()
    for p in sorted(DATALOGS.glob("tomadores_persistentes_fase0_*.csv*")):
        dia = p.name.split("_")[-1][:10]
        out = _desenlaces(dia)
        if not out:
            continue
        with _abrir(p) as f:
            for r in csv.DictReader(f):
                g = out.get(r.get("market_slug", ""))
                try:
                    a, ratio = float(r["mejor_ask"]), float(r["ratio_vs_stake"] or 0)
                except (ValueError, TypeError, KeyError):
                    continue
                if g is None or not 0.05 <= a < 0.95 or ratio < 5:
                    continue
                ac = 1 if r["lado"] == g else 0
                pnl = ac / a - 1 - FEE * (1 - a)
                b = int(a * 10) / 10
                for clave in (f"{r['marco']}|TODOS|[{b:.1f},{b + 0.1:.1f})", f"{r['marco']}|{r['activo']}|[{b:.1f},{b + 0.1:.1f})"):
                    celdas[clave][dia].append(pnl)
                    wallets_celda[clave][r["wallet"]] += 1
                total[dia].append(pnl)
                dias.add(dia)
                try:
                    lags.append(float(r["lag_ms"]))
                except (ValueError, TypeError, KeyError):
                    pass
    res = {}
    for clave, pd in celdas.items():
        x = [v for d in pd.values() for v in d]
        if len(x) < 40:
            continue
        top = max(wallets_celda[clave].values()) / len(x)
        res[clave] = dict(n=len(x), dias=len(pd), ev=round(sum(x) / len(x), 4), ic90=_ic90_por_dias(pd), wallet_top_pct=round(top * 100))
    x = [v for d in total.values() for v in d]
    lags.sort()
    return dict(dias=sorted(dias), n=len(x), ev=round(sum(x) / len(x), 4) if x else None, ic90=_ic90_por_dias(total),
                lag_ms_mediana=lags[len(lags) // 2] if lags else None, celdas=res)


def mantenimiento_observador() -> None:
    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    limite = (datetime.now(timezone.utc) - timedelta(days=RETENCION_OBS_DIAS)).strftime("%Y-%m-%d")
    for p in DATALOGS.glob("tomadores_persistentes_fase0_*.csv"):
        dia = p.name.split("_")[-1][:10]
        if dia < hoy:
            with open(p, "rb") as fi, gzip.open(str(p) + ".gz", "wb") as fo:
                fo.write(fi.read())
            p.unlink()
    for p in DATALOGS.glob("tomadores_persistentes_fase0_*.csv.gz"):
        if p.name.split("_")[-1][:10] < limite:
            p.unlink()


def main() -> int:
    dias = dias_cerrados(VENTANA_DIAS + 6)
    perfiles = {}
    for d in dias:
        per = perfil_dia(d)
        if per is not None:
            perfiles[d] = per
            print(f"{d}: {len(per)} wallets con >={FILLS_MIN_CACHE} fills", flush=True)
    if len(perfiles) < VENTANA_DIAS:
        print(f"solo {len(perfiles)} días con datos completos; hacen falta {VENTANA_DIAS}")
        return 1
    orden = sorted(perfiles)
    ventana = orden[-VENTANA_DIAS:]
    sel = seleccionar(combinar({d: perfiles[d] for d in ventana}))
    try:
        previo = set(json.loads(UNIVERSO.read_text()).get("wallets", {}))
    except Exception:
        previo = set()
    entran, salen = sorted(set(sel) - previo), sorted(previo - set(sel))
    UNIVERSO.write_text(json.dumps({
        "generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "ventana": ventana,
        "criterio": f">={N_MIN} fills, >={MERC_MIN} mercados, >={AGR_MIN:.0f}% agresiva, neto de fee >0, >={DIAS_POS_MIN}/{VENTANA_DIAS} días positivos",
        "wallets": sel}, indent=1), encoding="utf-8")
    # validación forward: seleccionar con los VENTANA_DIAS anteriores a D, medir en D
    fwd = []
    for i in range(VENTANA_DIAS, len(orden)):
        d = orden[i]
        s = seleccionar(combinar({x: perfiles[x] for x in orden[i - VENTANA_DIAS:i]}))
        v = bruto = fee = 0.0
        act = rep = 0
        for w in s:
            r = perfiles[d].get(w)
            if not r or r[0] < 30:
                continue
            f_est = r[3] / r[5] * r[1] if r[5] > 0 else 0.0
            v += r[1]
            bruto += r[2]
            fee += f_est
            act += 1
            rep += 1 if r[2] - f_est > 0 else 0
        if v > 0:
            fwd.append(dict(dia=d, seleccionadas=len(s), activas=act, neto_pct_vol=round((bruto - fee) / v * 100, 2),
                            neto_usd=round(bruto - fee), repiten_pct=round(rep / act * 100) if act else 0))
    copia = copia_con_latencia_real()
    mantenimiento_observador()
    INFORME.write_text(json.dumps({"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                   "universo_n": len(sel), "entran": entran, "salen": salen,
                                   "forward_propio": fwd, "copia_latencia_real": copia}, indent=1), encoding="utf-8")
    lineas = [f"🎯 Tomadores persistentes — universo {len(sel)} wallets (ventana {ventana[0]}..{ventana[-1]}); entran {len(entran)}, salen {len(salen)}"]
    if fwd:
        pos = sum(1 for x in fwd if x["neto_pct_vol"] > 0)
        lineas.append(f"Forward propio (elegidas con los 6 días previos, medidas al día siguiente): {pos}/{len(fwd)} días netos + | último {fwd[-1]['dia']}: "
                      f"{fwd[-1]['neto_pct_vol']:+.2f}% del volumen, repiten {fwd[-1]['repiten_pct']}%")
    if copia["n"]:
        lineas.append(f"Copia al ask real (observador, {len(copia['dias'])} días, n={copia['n']}, latencia mediana {copia['lag_ms_mediana']:.0f} ms): "
                      f"EV {copia['ev']:+.4f} por €" + (f", IC90 {copia['ic90']}" if copia["ic90"] else ""))
        buenas = [(k, c) for k, c in copia["celdas"].items() if c["ev"] >= 0.10 and c["ic90"] and c["ic90"][0] > 0 and c["dias"] >= 10 and c["wallet_top_pct"] <= 30]
        lineas.append(f"Celdas que pasan el gate (n≥40, ≥10 días, EV≥+0,10, IC90>0, wallet top≤30 %): {len(buenas)}" + "".join(f"\n  {k}: EV {c['ev']:+.3f} n={c['n']}" for k, c in buenas[:6]))
    else:
        lineas.append("Copia al ask real: el observador aún no tiene días cerrados con desenlace.")
    print("\n".join(lineas))
    if "--telegram" in sys.argv:
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram("\n".join(lineas))
        except Exception as e:
            print(f"(no se pudo avisar por Telegram: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
