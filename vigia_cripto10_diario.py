#!/usr/bin/env python3
"""vigia_cripto10_diario.py -- seguimiento DIARIO de las estrategias 4-10 del programa cripto10 (30-Sep noche, Javi:
"4 ok, 5 ok + cron diario, 6 ok, 7 constrúyelo + cron, 8 y 9 amplía el observador, 10 cron diario"). Las 1-3 (valor
tras salto H1-H4) van en vigia_valor_tras_salto_forward.py. SOLO LECTURA, nunca opera.

Reglas CONGELADAS antes de ver su forward (no se retocan; contexto en datalogs analisis_persistente_30sep/cripto10_30sep/):
  #4  PRECIERRE banda alta, T-45 s, libro real con profundidad >=5x (precierre_multioffset_fase0):
        A) 15m z>=1,0 ask [0,80-0,95)     B) 5m z>=1,8 ask [0,80-0,95)          forward desde CORTE
  #5  PRECIERRE con veto de recotización (precierre_libro_ms, libro a 100 ms): a T-45 s el favorito (ask [0,55-0,95));
        se espera 0,5 s y se compra al ask de ese momento (a2). V1 = a2 >= ask inicial (no bajó) · V2 = bajó (lo vetado).
  #6  Maker con cancelación en ms: salida de analisis_precierre_maker_ms.py (celdas con rellenos >=15).
  #7  Maker protegido por wallets líderes: data/shadow/maker_protegido_wallets.json (maker_protegido_wallets.py, cron propio).
  #8  Salto de Binance -> libros de OTRAS monedas 5m/15m (binance_jump_cruzado): comprar el lado del salto al ask a +0,6 s.
  #9  Salto -> marcos 1 h / 4 h de la MISMA moneda, idem.   Para ambos: % de libros quietos entre +0 y +0,6 s.
  #11 Penny Clipper RÁPIDO (penny_clipper_ws_fase0, disparo por trades del WS del CLOB, ~0,1 s): comprar el token al ask del
        libro en memoria a +0 / 0,5 / 1 / 2 s desde la detección (curva de decaimiento); profundidad >=5x stake.
        Antes del corte, con el disparo por RTDS: lectura <500 ms +8,6 % (n=395), 500-1000 −4,7 %, >1 s −9,8 %.
  #10 Up/Down DIARIO (updown_diario_fase0): primer instante con <=10 min restantes y valor = prob_justa - ask >= 0,10.
Gate común para proponer algo con dinero: n>=40, >=5 días (10 en #4-#5), EV>=+0,10 por €, IC90 por días >0 -> y aun así
checklist de 6 categorías + /code-review + OK de Javi. Comisión cripto 7 % x (1 - p) por € (maker: 0).
Salida: data/shadow/vigia_cripto10_diario.json; Telegram con --telegram.
"""
import csv
import glob
import gzip
import json
import random
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
DATALOGS = Path("/root/polymarket-research-datalogs")
OUT = REPO / "data" / "shadow" / "vigia_cripto10_diario.json"
CORTE = "2026-09-30T19:30:00"
FEE = 0.07


def _pnl(win, a, fee=FEE):
    return (1 / a - 1 - fee * (1 - a)) if win else (-1 - fee * (1 - a))


def _res(por_dia: dict) -> dict:
    x = [v for d in por_dia.values() for v in d]
    if not x:
        return {"n": 0}
    ks = [k for k in por_dia if por_dia[k]]
    ic = None
    if len(ks) >= 3:
        rng, ms = random.Random(5), []
        for _ in range(2000):
            s = [v for k in (rng.choice(ks) for _ in ks) for v in por_dia[k]]
            ms.append(sum(s) / len(s))
        ms.sort()
        ic = [round(ms[100], 4), round(ms[1899], 4)]
    return {"n": len(x), "dias": len(ks), "ev": round(sum(x) / len(x), 4), "ic90": ic,
            "dias_positivos": sum(1 for k in ks if sum(por_dia[k]) > 0)}


def _txt(nombre, r):
    if not r.get("n"):
        return f"{nombre}: n=0"
    return f"{nombre}: n={r['n']} días={r['dias']} EV {r['ev']:+.3f}" + (f" IC90 {r['ic90']}" if r.get("ic90") else "")


def _resolver_ids(ids):
    import analisis_binance_jump_leadlag as J
    return J._resolver(sorted({str(i) for i in ids}))


def _resolver_slugs(slugs):
    import analisis_precierre_rejilla_ask_real as P
    return P.desenlaces(list(slugs))


def s4():
    filas = []
    with open(DATALOGS / "precierre_multioffset_fase0.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["ts_utc"][:19] < CORTE or r.get("error") or r["offset_s"] not in ("-45", "-45.0"):
                continue
            try:
                filas.append((r, float(r["z"]), float(r["ask"]), float(r["ratio_vs_stake"] or 0)))
            except ValueError:
                continue
    gan = _resolver_slugs({r["slug"] for r, *_ in filas})
    out = {}
    for nombre, marco, zmin in (("A 15m z>=1 ask 0,80-0,95", "15m", 1.0), ("B 5m z>=1,8 ask 0,80-0,95", "5m", 1.8)):
        pd = defaultdict(list)
        for r, z, a, ratio in filas:
            o = gan.get(r["slug"])
            if r["marco"] == marco and z >= zmin and 0.80 <= a < 0.95 and ratio >= 5 and o in ("Up", "Down"):
                pd[r["ts_utc"][:10]].append(_pnl(o == r["direccion"], a))
        out[nombre] = _res(pd)
    return out


def s5():
    B = defaultdict(list)
    for p in sorted(glob.glob(str(DATALOGS / "precierre_libro_ms_*.csv.gz"))):
        if p[-17:-7] < CORTE[:10]:
            continue
        with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                if r["tipo"] == "book" and r["token"] == "YES" and r["best_bid"] and r["best_ask"]:
                    B[r["market_id"]].append((int(r["rel_fin_ms"]), float(r["best_bid"]), float(r["best_ask"]), float(r["end_ts"])))
    unidades = []
    for mk, L in B.items():
        L.sort()
        c = [x for x in L if -46000 <= x[0] <= -44000]
        if not c or datetime.fromtimestamp(c[0][3] - 45, timezone.utc).isoformat()[:19] < CORTE:
            continue
        rel, bid, ask, end = c[0]
        lado = "YES" if 0.55 <= ask < 0.95 else ("NO" if 0.55 <= 1 - bid < 0.95 else None)
        if not lado:
            continue
        a1 = ask if lado == "YES" else round(1 - bid, 4)
        nx = [x for x in L if rel + 400 <= x[0] <= rel + 700]
        if not nx:
            continue
        a2 = nx[0][2] if lado == "YES" else round(1 - nx[0][1], 4)
        unidades.append((mk, lado, a1, a2, datetime.fromtimestamp(end, timezone.utc).isoformat()[:10]))
    gan = _resolver_ids({u[0] for u in unidades})
    pd = {"V1 no bajó (compra a +0,5 s)": defaultdict(list), "V2 bajó (vetado)": defaultdict(list)}
    for mk, lado, a1, a2, d in unidades:
        o = gan.get(str(mk))
        if o not in ("Up", "Down") or not 0.03 <= a2 < 0.99:
            continue
        win = (o == "Up") == (lado == "YES")
        pd["V1 no bajó (compra a +0,5 s)" if a2 >= a1 else "V2 bajó (vetado)"][d].append(_pnl(win, a2))
    return {k: _res(v) for k, v in pd.items()}


def s6():
    try:
        r = subprocess.run([sys.executable, str(REPO / "analisis_precierre_maker_ms.py")], capture_output=True, text=True, timeout=1500)
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}"}
    lineas = [l for l in r.stdout.splitlines() if l[:5] in ("5min ", "15min")]
    mejores = []
    for l in lineas:
        try:
            ev_col = float(l.split()[-2])
            mejores.append((ev_col, l))
        except (ValueError, IndexError):
            continue
    mejores.sort(reverse=True)
    return {"cabecera": (r.stdout.splitlines() or [""])[0], "celdas": len(lineas), "top3": [l for _, l in mejores[:3]]}


def s7():
    p = REPO / "data" / "shadow" / "maker_protegido_wallets.json"
    if not p.exists():
        return {"error": "sin JSON (corre maker_protegido_wallets.py)"}
    d = json.loads(p.read_text())
    out = {"dias": list(d.get("dias", {})), "exploratorio": d.get("exploratorio"), "celdas": {}}
    for k, v in d.get("celdas", {}).items():
        if v["BASE"].get("rellenos", 0) >= 15:
            out["celdas"][k] = {g: {x: v[g].get(x) for x in ("rellenos", "acierto_relleno", "ev_por_eur_relleno", "ic90")} for g in v}
    return out


def s8_9():
    filas = []
    for p in sorted(glob.glob(str(DATALOGS / "binance_jump_cruzado_*.csv.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
            filas += list(csv.DictReader(fh))
    ev = defaultdict(dict)
    for r in filas:
        ev[(r["ts_evento"], r["activo"], r["marco"], r["market"], r["activo_salto"])][r["offset_s"]] = r
    slugs = {k[3] for k in ev if k[2] != "1h"}
    ids = {k[3] for k in ev if k[2] == "1h"}
    gan = dict(_resolver_slugs(slugs)) if slugs else {}
    gan.update(_resolver_ids(ids) if ids else {})
    grupos = defaultdict(lambda: defaultdict(list))
    quieto = defaultdict(lambda: [0, 0])
    for (ts, a, marco, mkt, a_s), offs in ev.items():
        r0, r6 = offs.get("0.0"), offs.get("0.6")
        if not r0 or not r6 or not r6["ask"] or not r0["ask"]:
            continue
        a0, a6 = float(r0["ask"]), float(r6["ask"])
        propia = a == a_s
        clave = f"{'#9' if marco in ('1h', '4h') else '#8'} {marco} {'misma moneda' if propia else 'otra moneda'}"
        if marco in ("1h", "4h") or not propia:
            quieto[clave][0] += a6 == a0
            quieto[clave][1] += 1
        o = gan.get(mkt)
        if o not in ("Up", "Down") or not 0.03 <= a6 < 0.97 or float(r6["resto_s"]) < 5:
            continue
        if float(r6["ask_size"] or 0) * a6 < 5 * 1.05:
            continue
        grupos[clave][ts[:10]].append(_pnl(o == r6["direccion"], a6))
    out = {k: _res(v) for k, v in sorted(grupos.items())}
    for k, (q, n) in quieto.items():
        out.setdefault(k, {"n": 0})["libro_quieto_0_a_0,6s"] = round(q / n, 3) if n else None
    return out


def s10():
    filas = []
    p = REPO / "data" / "shadow" / "updown_diario_fase0.csv"
    if not p.exists():
        return {"error": "sin datos"}
    with open(p, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                if r.get("error") or float(r["min_restantes"]) > 10:
                    continue
                pu, au, ad = float(r["prob_justa_up"]), float(r["ask_up"] or 9), float(r["ask_down"] or 9)
            except ValueError:
                continue
            filas.append((r, pu, au, ad))
    visto, unidades = set(), []
    for r, pu, au, ad in sorted(filas, key=lambda x: x[0]["ts_utc"]):
        if r["market_id"] in visto:
            continue
        for lado, v, a in (("Up", pu - au, au), ("Down", (1 - pu) - ad, ad)):
            if v >= 0.10 and 0.03 <= a < 0.97:
                visto.add(r["market_id"])
                unidades.append((r["market_id"], lado, a, r["ts_utc"][:10]))
                break
    gan = _resolver_ids({u[0] for u in unidades}) if unidades else {}
    pd = defaultdict(list)
    for mk, lado, a, d in unidades:
        o = gan.get(str(mk))
        if o in ("Up", "Down"):
            pd[d].append(_pnl(o == lado, a))
    dias_obs = len({r["ts_utc"][:10] for r, *_ in filas})
    return {"valor>=0,10 a <=10 min": _res(pd), "dias_observados": dias_obs, "disparos": len(unidades)}


def s11():
    filas = []
    for p in sorted(glob.glob(str(DATALOGS / "penny_clipper_ws_*.csv.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
            filas += list(csv.DictReader(fh))
    gan = _resolver_ids({r["market_id"] for r in filas}) if filas else {}
    pd = {o: defaultdict(list) for o in ("0.0", "0.5", "1.0", "2.0")}
    lat = sorted(int(r["lat_deteccion_ms"]) for r in filas if r.get("lat_deteccion_ms"))
    for r in filas:
        o = gan.get(str(r["market_id"]))
        if o not in ("Up", "Down"):
            continue
        win = (r["decision"] == "BUY_YES") == (o == "Up")
        for off in pd:
            try:
                a, sz = float(r[f"ask_{off}"]), float(r[f"ask_size_{off}"] or 0)
            except (ValueError, KeyError):
                continue
            if 0.03 <= a < 0.97 and a * sz >= 5 * 1.05:
                pd[off][r["ts_deteccion_utc"][:10]].append(_pnl(win, a))
    out = {f"entrada +{o} s": _res(v) for o, v in pd.items()}
    out["latencia_deteccion_p50_ms"] = lat[len(lat) // 2] if lat else None
    out["disparos"] = len(filas)
    return out


def main() -> int:
    informe, lin = {}, ["🧪 Cripto10 — seguimiento diario (estrategias 4-10; las 1-3 en el vigía de valor tras salto)"]
    for nombre, fn in (("#4 PRECIERRE banda alta", s4), ("#5 PRECIERRE veto recotización +0,5 s", s5),
                       ("#6 maker con cancelación ms", s6), ("#7 maker protegido por líderes", s7),
                       ("#8/#9 salto -> otras monedas y 1h/4h", s8_9), ("#10 Up/Down diario", s10),
                       ("#11 Penny Clipper rápido (WS)", s11)):
        try:
            r = fn()
        except Exception as e:
            r = {"error": f"{type(e).__name__}: {e}"}
        informe[nombre] = r
        lin.append(f"\n{nombre}")
        if "error" in r:
            lin.append(f"  error: {r['error']}")
        elif nombre.startswith("#6"):
            lin.append(f"  {r.get('cabecera', '')[:140]}")
            lin += [f"  {l[:150]}" for l in r.get("top3", [])]
        elif nombre.startswith("#7"):
            lin.append(f"  días: {r['dias']} {'(exploratorio)' if r.get('exploratorio') else ''}")
            for k, v in list(r["celdas"].items())[:4]:
                b, p, c = v["BASE"], v["PROTEGIDO"], v.get("CONTROL", {})
                lin.append(f"  {k}: base {b['rellenos']} rell. EV {b['ev_por_eur_relleno']:+.3f} | protegido {p.get('rellenos')} EV {p.get('ev_por_eur_relleno')} | control {c.get('rellenos')} EV {c.get('ev_por_eur_relleno')}")
        else:
            for k, v in r.items():
                if isinstance(v, dict):
                    lin.append("  " + _txt(k, v) + (f" · libro quieto {v['libro_quieto_0_a_0,6s']:.0%}" if v.get("libro_quieto_0_a_0,6s") is not None else ""))
                else:
                    lin.append(f"  {k}: {v}")
    lin.append("\nGate: n≥40, ≥5 días (10 en #4-#5), EV≥+0,10, IC90 por días >0. Nada con dinero sin checklist + /code-review + OK de Javi.")
    OUT.write_text(json.dumps({"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "corte": CORTE,
                               "secciones": informe}, ensure_ascii=False, indent=1), encoding="utf-8")
    texto = "\n".join(lin)
    print(texto)
    if "--telegram" in sys.argv:
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram(texto[:3900])
        except Exception as e:
            print(f"(telegram falló: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
