#!/usr/bin/env python3
"""vigia_saltos_ask_real.py -- A3 "ganarles al entrar": informe DIARIO del EV al ASK REAL de los
saltos de precio justo (24-Sep, Javi: "haz que cuente el ask real, si no no es objetivo...
ve informándome día a día por Telegram y en cada inicio de sesión").

Fuente: data/shadow/saltos_chainlink_fase0.csv (saltos_chainlink_fase0.py: en cada salto >=0,08
del precio justo lee el libro REAL del lado del salto). Solo filas con fuente=polybolt (la
fuente rápida, ~1,2 s antes que RTDS); las de RTDS (fichero _rtds_v1) se ignoran.
Resultado del mercado: regla real = TWAP60 al cierre > TWAP60 en la apertura, con el canal
twap60 OFICIAL de PolyBolt (data/prices/polybolt_*.csv, valor del segundo exacto); si falta,
media Chainlink [t-60, t] (99,0-99,8 % de acierto verificado 24-Sep). Sin ninguno: sin resolver.
EV a 1 EUR, fee cripto 7 % sobre la ganancia, con DOS precios:
  - ask: mejor ask leído (fillable = ratio_vs_stake >= 5, como el resto de ejecutores)
  - vwap: VWAP de relleno para 1,05 EUR (más realista si el primer nivel es fino)
Desglose moneda × marco (CLAUDE.md pt.17) + buckets de ventaja (p_justo del lado - ask).
Candidata = n>=40 fillables, >=5 días, EV>=+0,10 al vwap, IC90 bootstrap por DÍAS > 0 y ambas
mitades > 0 (con n>=20). Telegram SIEMPRE; JSON data/shadow/vigia_saltos_ask_real.json.
"""
import csv
import glob
import gzip
import json
import random
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
SALTOS = REPO / "data/shadow/saltos_chainlink_fase0.csv"
OUT = REPO / "data/shadow/vigia_saltos_ask_real.json"
FEE, RATIO_MIN = 0.07, 5.0
csv.field_size_limit(10_000_000)


def _abrir(p):
    return gzip.open(p, "rt") if str(p).endswith(".gz") else open(p, encoding="utf-8")


def _dia(epoch):
    return datetime.fromtimestamp(epoch, timezone.utc).strftime("%Y-%m-%d")


def cargar_twap(dias):
    """{(activo, epoch_s): twap60 oficial PolyBolt}"""
    tw = {}
    for d in dias:
        for p in glob.glob(str(REPO / f"data/prices/polybolt_{d}.csv*")):
            with _abrir(p) as f:
                for r in csv.DictReader(f):
                    if r.get("canal") == "twap60":
                        try:
                            tw[(r["asset"], int(r["event_ts_ms"]) // 1000)] = float(r["value"])
                        except (ValueError, KeyError, TypeError):
                            continue
    return tw


def cargar_chainlink(dias):
    s = defaultdict(list)
    for d in dias:
        for p in glob.glob(str(REPO / f"data/prices/chainlink_{d}.csv*")):
            with _abrir(p) as f:
                for r in csv.DictReader(f):
                    try:
                        s[r["asset"]].append((int(r["ws_timestamp_ms"]) / 1000, float(r["price_usd"])))
                    except (ValueError, KeyError, TypeError):
                        continue
    for a in s:
        s[a].sort()
    return s


def _media_cl(serie, t0, t1):
    v = [p for t, p in serie if t0 <= t <= t1]
    return sum(v) / len(v) if len(v) >= 10 else None


def resolver(activo, ini, fin, tw, cl):
    a, b = tw.get((activo, ini)), tw.get((activo, fin))
    if a is not None and b is not None and a != b:
        return ("Up" if b > a else "Down"), "twap_polybolt"
    s = cl.get(activo, [])
    a, b = _media_cl(s, ini - 60, ini), _media_cl(s, fin - 60, fin)
    if a is not None and b is not None and a != b:
        return ("Up" if b > a else "Down"), "chainlink"
    return None, None


def pnl(precio, gana):
    return (1 - precio) / precio * (1 - FEE) if gana else -1.0


def resumen(xs, clave):
    n = len(xs)
    if not n:
        return None
    dias = defaultdict(list)
    for x in xs:
        dias[x["dia"]].append(x[clave])
    out = {"n": n, "dias": len(dias), "acierto": round(sum(x["gana"] for x in xs) / n, 3),
           "precio_medio": round(sum(x["px_" + clave] for x in xs) / n, 3),
           "ev": round(sum(x[clave] for x in xs) / n, 3)}
    if n >= 20:
        o = sorted(xs, key=lambda x: x["t"])
        h = n // 2
        out["mitades"] = [round(sum(x[clave] for x in o[:h]) / h, 3), round(sum(x[clave] for x in o[h:]) / (n - h), 3)]
        ds, rng, med = list(dias.values()), random.Random(5), []
        for _ in range(1000):
            m = [v for _ in ds for v in rng.choice(ds)]
            med.append(sum(m) / len(m))
        med.sort()
        out["ic90_dias"] = [round(med[50], 3), round(med[949], 3)]
    return out


def main() -> int:
    filas = []
    if SALTOS.exists():
        with open(SALTOS, encoding="utf-8", newline="") as f:
            filas = [r for r in csv.DictReader(f) if r.get("fuente") == "polybolt"]
    dias = sorted({_dia(int(r["fin"])) for r in filas if r.get("fin")} | {_dia(int(r["ini"])) for r in filas if r.get("ini")})
    tw, cl = cargar_twap(dias), cargar_chainlink(dias)
    ahora = datetime.now(timezone.utc).timestamp()
    xs, pendientes, sin_libro, fuente_res = [], 0, 0, defaultdict(int)
    for r in filas:
        try:
            ini, fin = int(r["ini"]), int(r["fin"])
        except (ValueError, KeyError):
            continue
        if fin > ahora - 90:
            pendientes += 1
            continue
        try:
            ask = float(r["ask"])
            ratio = float(r["ratio_vs_stake"] or 0)
        except (ValueError, KeyError):
            sin_libro += 1
            continue
        try:
            vw = float(r["vwap_fill"]) if r.get("vwap_fill") not in ("", None) else ask
        except ValueError:
            vw = ask
        ganador, fres = resolver(r["activo"], ini, fin, tw, cl)
        if ganador is None:
            pendientes += 1
            continue
        fuente_res[fres] += 1
        gana = ganador == r["direccion"]
        p = float(r["p_justo"])
        p_lado = p if r["direccion"] == "Up" else 1 - p
        xs.append({"activo": r["activo"], "marco": r["marco"], "dia": _dia(fin), "t": r["ts_utc"], "gana": gana,
                   "fillable": ratio >= RATIO_MIN and 0.01 < ask < 0.99, "ventaja": p_lado - ask,
                   "px_ask": ask, "px_vwap": vw, "ask": pnl(ask, gana), "vwap": pnl(vw, gana)})
    fill = [x for x in xs if x["fillable"]]
    grupos = defaultdict(list)
    for x in fill:
        grupos["TOTAL"].append(x)
        grupos[f"{x['activo']}#{x['marco']}"].append(x)
        b = "ventaja<0" if x["ventaja"] < 0 else "0-0.05" if x["ventaja"] < 0.05 else "0.05-0.10" if x["ventaja"] < 0.10 else ">=0.10"
        grupos[f"ventaja {b}"].append(x)
    res = {}
    for g, v in grupos.items():
        ra, rv = resumen(v, "ask"), resumen(v, "vwap")
        cand = bool(g != "TOTAL" and not g.startswith("ventaja") and rv and rv["n"] >= 40 and rv["dias"] >= 5
                    and rv["ev"] >= 0.10 and rv.get("ic90_dias", [0])[0] > 0 and min(rv.get("mitades", [0])) > 0)
        res[g] = {"al_ask": ra, "al_vwap": rv, "candidata": cand}
    salida = {"actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "saltos_polybolt": len(filas), "resueltos": len(xs), "fillables": len(fill),
              "pendientes": pendientes, "sin_libro": sin_libro, "resolucion": dict(fuente_res), "grupos": res}
    OUT.write_text(json.dumps(salida, indent=1, ensure_ascii=False), encoding="utf-8")

    msg = ["⚡ A3 ganarles al entrar -- EV al ASK REAL (fuente PolyBolt)",
           f"saltos {len(filas)} | resueltos {len(xs)} | fillables {len(fill)} | pendientes {pendientes}"]
    t = res.get("TOTAL")
    if t and t["al_vwap"]:
        a, v = t["al_ask"], t["al_vwap"]
        msg.append(f"TOTAL: acierto {v['acierto']:.0%} | al ask {a['ev']:+.3f} €/tr | al vwap {v['ev']:+.3f} "
                   f"(n={v['n']}, {v['dias']}d, IC90 {v.get('ic90_dias', '-')})")
    for g in sorted(k for k in res if "#" in k):
        v, a = res[g]["al_vwap"], res[g]["al_ask"]
        msg.append(f"· {g}: n={v['n']} {v['acierto']:.0%} ask {a['ev']:+.3f} vwap {v['ev']:+.3f}"
                   f"{' ✅ CANDIDATA' if res[g]['candidata'] else ''}")
    for g in ("ventaja<0", "0-0.05", "0.05-0.10", ">=0.10"):
        r = res.get(f"ventaja {g}")
        if r and r["al_vwap"]:
            msg.append(f"  ventaja {g}: n={r['al_vwap']['n']} vwap {r['al_vwap']['ev']:+.3f}")
    msg.append("Candidata = n>=40 fillables, >=5 días, EV>=+0,10 al vwap, IC90 por días>0, mitades>0.")
    print("\n".join(msg))
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram("\n".join(msg))
    except Exception as e:
        print(f"(Telegram falló: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
