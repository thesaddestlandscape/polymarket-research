#!/usr/bin/env python3
"""maker_protegido_wallets.py -- estrategia 7 del programa cripto10 (30-Sep, Javi: "7 - ok, constrúyelo y ponme un
cron con los datos"). SOLO SIMULACIÓN, nunca envía órdenes.

Idea: el maker pasivo pierde por selección adversa (le llenan justo cuando el favorito va a perder). El 30-Sep se
midió que hay wallets cuyas compras ADELANTAN los saltos de Binance (138 elegidas con 25-27 Sep; fuera de muestra,
un 57 % más de saltos a favor en los 6 s siguientes que el resto), aunque copiarlas no gana dinero. Hipótesis: como
alarma sí valen -- si una de ellas opera CONTRA nuestro favorito mientras tenemos la puja puesta, cancelar.

Qué hace, por día D cerrado:
 1. Caché por día (datalogs/maker_protegido_cache/lead_D.json): por wallet, compras (>=2 USD) en up/down 5m/15m del
    firehose y cuántas fueron seguidas de un salto de Binance en su dirección en (1, 6] s (saltos del observador
    binance_jump_leadlag_fase0).
 2. Wallets "líderes" para D = n>=50 y z>3,1 frente a la tasa base con los 3 días ANTERIORES (point-in-time).
 3. Maker del simulador analisis_precierre_maker_ms (mismo relleno conservador y cancelación por caída del mid,
    300 ms de latencia de cancelación) sobre precierre_libro_ms del día D, en dos versiones:
      BASE      = tal cual;
      PROTEGIDO = además cancela 300 ms después de RECIBIR (hora de recepción del firehose, lo que veríamos en vivo)
                  la primera operación de una líder contra nuestro favorito en ese mercado.
 4. Acumula por (marco, instante, cancelación, banda del favorito): colocadas, rellenos, acierto y EV por € del
    relleno (maker: sin fee), con IC90 por mercado; y la diferencia PROTEGIDO - BASE.
Salida: data/shadow/maker_protegido_wallets.json (lo resume vigia_cripto10_diario.py). Con <10 días: exploratorio.
"""
import csv
import glob
import gzip
import json
import math
import os
import random
import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import analisis_precierre_maker_ms as M  # noqa: E402

DATALOGS = Path("/root/polymarket-research-datalogs")
CACHE = DATALOGS / "maker_protegido_cache"
OUT = REPO / "data" / "shadow" / "maker_protegido_wallets.json"
LEADLAG = DATALOGS / "binance_jump_leadlag_fase0.csv"
VENTANA_SEL, N_MIN, Z_MIN = 3, 50, 3.1          # fijados 30-Sep (mismos que el hallazgo E3)
DUR = {"5min": 300, "15min": 900}


def _firehose(d: str):
    for p in (DATALOGS / f"polymarket_activity_{d}.csv", DATALOGS / f"polymarket_activity_{d}.csv.gz"):
        if p.exists():
            return gzip.open(p, "rt", errors="replace") if str(p).endswith(".gz") else open(p, errors="replace")
    return None


def _saltos():
    J = defaultdict(list)
    with open(LEADLAG, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                J[r["activo"]].append((datetime.fromisoformat(r["ts_evento"]).timestamp(), r["direccion"]))
            except (ValueError, KeyError):
                continue
    return {a: sorted(set(v)) for a, v in J.items()}


def _cache_lideres(d: str, J) -> dict | None:
    """wallet -> [compras, seguidas_de_salto]. None si no hay firehose del día."""
    CACHE.mkdir(parents=True, exist_ok=True)
    dst = CACHE / f"lead_{d}.json"
    if dst.exists():
        return json.loads(dst.read_text())
    f = _firehose(d)
    if f is None:
        return None
    Jt = {a: [x[0] for x in v] for a, v in J.items()}
    st = defaultdict(lambda: [0, 0])
    with f:
        rd = csv.reader(f)
        h = next(rd)
        ix = {c: h.index(c) for c in h}
        isl, iw, io, isd, iu, iws, ia = (ix[c] for c in ("market_slug", "wallet", "outcome", "side", "usd_value", "ws_timestamp", "activo"))
        for r in rd:
            try:
                if r[isd] != "BUY" or ("-5m-" not in r[isl] and "-15m-" not in r[isl]) or float(r[iu] or 0) < 2:
                    continue
                a, ws, up = r[ia], int(r[iws]), r[io] == "Up"
                L = Jt.get(a, [])
                i, j = bisect_right(L, ws + 0.999), bisect_right(L, ws + 5.999)
                x = any((J[a][k][1] == "Up") == up for k in range(i, j))
                s = st[r[iw].lower()]
                s[0] += 1
                s[1] += x
            except (ValueError, IndexError):
                continue
    out = {w: v for w, v in st.items()}
    tmp = dst.with_name(dst.name + f".tmp{os.getpid()}")
    tmp.write_text(json.dumps(out))
    tmp.replace(dst)
    return out


def _lideres_para(d: str, J) -> set:
    d0 = date.fromisoformat(d)
    acc = defaultdict(lambda: [0, 0])
    for k in range(1, VENTANA_SEL + 1):
        c = _cache_lideres((d0 - timedelta(days=k)).isoformat(), J)
        for w, (n, x) in (c or {}).items():
            acc[w][0] += n
            acc[w][1] += x
    n_t, x_t = sum(v[0] for v in acc.values()), sum(v[1] for v in acc.values())
    if not n_t:
        return set()
    b = x_t / n_t
    lid = {w for w, (n, x) in acc.items() if n >= N_MIN and (x - n * b) / math.sqrt(n * b * (1 - b)) > Z_MIN}
    # CONTROL: mismo número de wallets igual de activas (n>=N_MIN) que NO son líderes, al azar con semilla por día.
    # Si el control mejora al maker igual que las líderes, la mejora es "cancelar pronto", no información.
    resto = sorted(w for w, (n, _) in acc.items() if n >= N_MIN and w not in lid)
    ctl = set(random.Random(d).sample(resto, min(len(lid), len(resto))))
    return lid, ctl


def _alarmas(d: str, lideres: set, slugs: dict) -> dict:
    """market_id -> [(rel_fin_ms_recepcion, bajista_para_YES)] de las líderes en los mercados del día."""
    out = defaultdict(list)
    f = _firehose(d)
    if f is None or not lideres:
        return out
    with f:
        rd = csv.reader(f)
        h = next(rd)
        ix = {c: h.index(c) for c in h}
        isl, iw, io, isd, its = (ix[c] for c in ("market_slug", "wallet", "outcome", "side", "timestamp_utc"))
        for r in rd:
            try:
                mid_end = slugs.get(r[isl])
                if not mid_end or r[iw].lower() not in lideres:
                    continue
                mid, end = mid_end
                rel = int((datetime.fromisoformat(r[its]).timestamp() - end) * 1000)
                if -120000 <= rel <= 5000:
                    alcista_yes = (r[io] == "Up") == (r[isd] == "BUY")
                    out[mid].append((rel, not alcista_yes))
            except (ValueError, IndexError):
                continue
    for v in out.values():
        v.sort()
    return out


def main() -> int:
    random.seed(17)
    J = _saltos()
    mk = M._cargar()
    dias = sorted({m["dia"] for m in mk.values()})
    hoy = datetime.now(timezone.utc).date().isoformat()
    gan = M._desenlaces(mk.keys())
    res = defaultdict(lambda: {"BASE": [], "PROTEGIDO": [], "CONTROL": []})
    info_dias = {}
    for d in [x for x in dias if x < hoy]:
        lideres, control = _lideres_para(d, J)
        slugs = {}
        for k, m in mk.items():
            if m["dia"] != d or m["marco"] not in DUR:
                continue
            m.setdefault("end", None)
        # end_ts por mercado: el CSV lo trae; se relee barato del propio fichero del día
        ends = {}
        with gzip.open(DATALOGS / f"precierre_libro_ms_{d}.csv.gz", "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                ends.setdefault(r["market_id"], (r["activo"], r["marco"], float(r["end_ts"])))
        for k, (a, marco, end) in ends.items():
            if marco in DUR:
                slugs[f"{a.lower()}-updown-{'5m' if marco == '5min' else '15m'}-{int(end) - DUR[marco]}"] = (k, end)
        al = _alarmas(d, lideres, slugs)
        al_ctl = _alarmas(d, control, slugs)
        info_dias[d] = {"lideres": len(lideres), "mercados": len(ends), "mercados_con_alarma": len(al),
                        "mercados_con_alarma_control": len(al_ctl)}
        for k, m in mk.items():
            if m["dia"] != d or k not in gan or m["marco"] not in DUR:
                continue
            for inicio in (60, 30):
                for c in (None, 2):
                    s = M._simular(m, inicio, c)
                    if not s:
                        continue
                    banda = "0.55-0.80" if s["mid0"] < 0.80 else "0.80-0.95" if s["mid0"] < 0.95 else "0.95-1"
                    clave = f"{m['marco']}|T-{inicio}|cancel {'-' if c is None else str(c) + 'c'}|fav {banda}"
                    ok = gan[k] == s["fav"]
                    res[clave]["BASE"].append((d, k, s["relleno"], ok, s["precio"]))
                    # PROTEGIDO/CONTROL: primera alarma contraria tras colocar -> la puja deja de existir +300 ms después
                    t0 = -inicio * 1000
                    for grupo, alarmas in (("PROTEGIDO", al), ("CONTROL", al_ctl)):
                        contra = [rel for rel, bajista in alarmas.get(k, ()) if rel > t0 and bajista == (s["fav"] == "YES")]
                        rell = s["relleno"]
                        if rell and contra:
                            m2 = dict(m)
                            m2["tr"] = [x for x in m["tr"] if x[0] <= contra[0] + M.LAT_MS]
                            rell = M._simular(m2, inicio, c)["relleno"]
                        res[clave][grupo].append((d, k, rell, ok, s["precio"]))

    def resumen(filas):
        col = len(filas)
        rel = [x for x in filas if x[2]]
        if not rel:
            return {"colocadas": col, "rellenos": 0}
        ev = [((1 - p) / p) if ok else -1.0 for _, _, _, ok, p in rel]
        pdia = defaultdict(list)
        for (d, *_), e in zip(rel, ev):
            pdia[d].append(e)
        bs = []
        for _ in range(800):
            v = random.choices(ev, k=len(ev))
            bs.append(sum(v) / len(v))
        bs.sort()
        return {"colocadas": col, "rellenos": len(rel), "pct_relleno": round(len(rel) / col, 3),
                "acierto_relleno": round(sum(x[3] for x in rel) / len(rel), 3),
                "acierto_no_relleno": round(sum(x[3] for x in filas if not x[2]) / max(1, col - len(rel)), 3),
                "ev_por_eur_relleno": round(sum(ev) / len(ev), 4), "ic90": [round(bs[40], 4), round(bs[759], 4)],
                "ev_por_colocada": round(sum(ev) / col, 4), "dias": len(pdia),
                "dias_positivos": sum(1 for v in pdia.values() if sum(v) > 0)}
    salida = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "dias": info_dias,
              "exploratorio": len(info_dias) < 10,
              "celdas": {k: {g: resumen(v[g]) for g in ("BASE", "PROTEGIDO", "CONTROL")} for k, v in sorted(res.items())}}
    tmp = OUT.with_name(OUT.name + f".tmp{os.getpid()}")
    tmp.write_text(json.dumps(salida, indent=1, ensure_ascii=False), encoding="utf-8")
    tmp.replace(OUT)
    print(f"días {info_dias}")
    for k, v in salida["celdas"].items():
        b, p, q = v["BASE"], v["PROTEGIDO"], v["CONTROL"]
        if b.get("rellenos", 0) >= 15:
            print(f"{k:42s} BASE {b['rellenos']:4d}/{b['colocadas']:4d} acierto {b['acierto_relleno']:.3f} EV {b['ev_por_eur_relleno']:+.3f}"
                  f" | PROT {p.get('rellenos', 0):4d} acierto {p.get('acierto_relleno', 0):.3f} EV {p.get('ev_por_eur_relleno', 0):+.3f}"
                  f" | CONTROL {q.get('rellenos', 0):4d} acierto {q.get('acierto_relleno', 0):.3f} EV {q.get('ev_por_eur_relleno', 0):+.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
