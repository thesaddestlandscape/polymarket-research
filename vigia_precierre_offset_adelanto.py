#!/usr/bin/env python3
"""vigia_precierre_offset_adelanto.py -- informe DIARIO por Telegram (12-Oct, Javi: "ponme diariamente una
notificación por telegram para saber cómo va esto"): ¿conviene adelantar PRECIERRE de T-45 a T-46/T-47?

Contexto (memoria project_precierre_fok_muertas_12oct): del 10 al 12-Oct murieron 5 de 9 FOK reales y 4 habrían
ganado. Hay competidores que casan en T-44,8 s (y en 15m en T-45,8 s). Desde el 12-Oct 13:39Z el observador
precierre_multioffset_fase0 mide también T-47 y T-46. Este vigía reporta:
  1) FOK reales de PRECIERRE desde el 10-Oct: enviadas, muertas y cuántas muertas habrían ganado (desenlace oficial).
  2) Por marco y offset (-47/-46/-45), con la regla del ejecutor (z>=Z_MIN, banda de ask del marco, profundidad>=5x):
     señales, acierto, EV/€ al ask real (comisión real) e IC90 por cierre; y emparejado en los MISMOS mercados:
     qué % de las señales de T-45 también pasa a T-47 y la diferencia de EV.
Decisión (no automática): 15m con n>=40 a T-47 -> comparar y, si compensa, offset POR MARCO + kill propio +
/code-review medium + OK de Javi. Solo lectura; JSON en data/shadow/vigia_precierre_offset_adelanto.json.
Cron 09:40 UTC (fuera del racimo 06-09Z; no coincide con vigia_precierre_naive_twap, que comparte la caché).
"""
import csv
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import vigia_precierre_naive_twap as V  # noqa: E402  (MULTIOFFSET y _resolver_outcomes: una sola caché)
from comision_cripto import pnl_por_euro  # noqa: E402

DESDE_OFFSETS = "2026-10-12T13:39"      # primer minuto con filas a -47/-46
DESDE_FOK = "2026-10-10"
OFFSETS = (-47, -46, -45)
BANDA = {"5m": (0.25, 0.65), "15m": (0.25, 0.85)}   # = ASK_TWAP_MIN / ASK_TWAP_MAX_POR_MARCO del ejecutor
Z_MIN, RATIO_MIN, N_DECIDIR = 1.8, 5.0, 40
EJECUTOR_CSV = REPO / "data/shadow/resolution_sniper_precierre_executor_v2.csv"
OUT = REPO / "data/shadow/vigia_precierre_offset_adelanto.json"
_FOK_KILL = "FOK orders are fully filled or killed"
# 17-Oct (OK Javi): seguimiento de la RAMPA de stake pre-registrada (memoria project_rampa_stake_precierre_17oct):
# 2 € -> 5 € solo con, POR MARCO y desde el arreglo del límite FOK: >=40 órdenes reales y >=10 días, EV/€ >= +0,05 con
# IC90 por días > 0, > 0 sin los 2 mejores días, FOK muertas <= 20 %; bajar un escalón si las 20 últimas dan EV < 0.
DESDE_RAMPA = "2026-10-17T08:16"
TRADES = REPO / "data/live/trades.csv"
RAMPA = {"n_min": 40, "dias_min": 10, "ev_min": 0.05, "fok_muertas_max": 0.20, "ultimas": 20}


def _fok_reales() -> dict:
    env, muertas = [], []
    with open(EJECUTOR_CSV, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r.get("timestamp_utc", "") < DESDE_FOK or r.get("disparado") != "True" or r.get("dry_run") == "True":
                continue
            env.append(r)
            if _FOK_KILL in (r.get("order_error") or ""):
                muertas.append(r)
    gan = V._resolver_outcomes(sorted({r["market_id"] for r in muertas if r.get("market_id")}))
    ganarian = sum(1 for r in muertas if gan.get(r["market_id"]) == r.get("direccion_implicita"))
    resueltas = sum(1 for r in muertas if r.get("market_id") in gan)
    return {"enviadas": len(env), "muertas": len(muertas), "muertas_resueltas": resueltas,
            "muertas_que_ganarian": ganarian}


def _señales() -> dict:
    """{(marco, offset): {market_id: {ask, dir, cierre}}} con la regla del ejecutor."""
    out = {}
    with open(V.MULTIOFFSET, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r["ts_utc"] < DESDE_OFFSETS or r.get("error"):
                continue
            try:
                off = int(float(r["offset_s"]))
                if off not in OFFSETS or r["marco"] not in BANDA:
                    continue
                ask, ratio = float(r["ask"]), float(r["ratio_vs_stake"])
                z = float(r["z_v2"]) if r.get("z_v2") else float(r["z"])
            except (TypeError, ValueError):
                continue
            d = r.get("direccion_v2") or r.get("direccion")
            lo, hi = BANDA[r["marco"]]
            if z < Z_MIN or ratio < RATIO_MIN or not (lo <= ask < hi) or d not in ("Up", "Down"):
                continue
            out.setdefault((r["marco"], off), {}).setdefault(
                r["market_id"], {"ask": ask, "dir": d, "cierre": r["slug"].rsplit("-", 1)[-1], "dia": r["ts_utc"][:10]})
    return out


def _ic90(por_cierre: dict):
    g = list(por_cierre.values())
    if len(g) < 10:
        return None
    rng, med = random.Random(1), []
    for _ in range(2000):
        s = [v for _ in g for v in rng.choice(g)]
        med.append(sum(s) / len(s))
    med.sort()
    return [round(med[100], 3), round(med[1899], 3)]


def _ic90_dias(por_dia: dict, rng=random.Random(7)):
    dias = list(por_dia)
    if len(dias) < 3:
        return None
    bs = []
    for _ in range(2000):
        m = [rng.choice(dias) for _ in dias]
        pnl = sum(por_dia[d][0] for d in m); st = sum(por_dia[d][1] for d in m)
        bs.append(pnl / st if st else 0.0)
    bs.sort()
    return [round(bs[100], 3), round(bs[1899], 3)]


def _rampa() -> dict:
    """Órdenes reales cerradas de PRECIERRE desde DESDE_RAMPA, por marco, frente a los criterios de la rampa."""
    filas = [r for r in csv.DictReader(open(TRADES, encoding="utf-8", newline=""))
             if r.get("strategy") == "RESOLUTION_SNIPER_PRECIERRE" and r.get("status") == "CLOSED"
             and r.get("timestamp_utc", "") >= DESDE_RAMPA]
    env = {"5m": 0, "15m": 0}; muertas = {"5m": 0, "15m": 0}
    with open(EJECUTOR_CSV, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r.get("timestamp_utc", "") < DESDE_RAMPA or r.get("disparado") != "True" or r.get("dry_run") == "True":
                continue
            if r.get("estrategia") not in ("", None, "RESOLUTION_SNIPER_PRECIERRE"):
                continue
            mk = "5m" if r.get("marco") == "5min" else ("15m" if r.get("marco") == "15min" else None)
            if mk:
                env[mk] += 1
                muertas[mk] += _FOK_KILL in (r.get("order_error") or "")
    out = {}
    for mk, sub in (("5m", "5min"), ("15m", "15min")):
        g = [r for r in filas if (r.get("subtype") or "").split("#")[-1] == sub]   # OJO: "15min".endswith("5min")
        por_dia = {}
        for r in g:
            d = r["timestamp_utc"][:10]
            a = por_dia.setdefault(d, [0.0, 0.0])
            a[0] += float(r["pnl_neto_eur"] or 0); a[1] += float(r["stake_eur"] or 0)
        pnl = sum(v[0] for v in por_dia.values()); st = sum(v[1] for v in por_dia.values())
        ev = round(pnl / st, 3) if st else None
        mejores = sorted(por_dia, key=lambda d: por_dia[d][0], reverse=True)[:2]
        resto = [v for d, v in por_dia.items() if d not in mejores]
        ev_sin2 = round(sum(v[0] for v in resto) / sum(v[1] for v in resto), 3) if resto and sum(v[1] for v in resto) else None
        ult = sorted(g, key=lambda r: r["timestamp_utc"])[-RAMPA["ultimas"]:]
        st_u = sum(float(r["stake_eur"] or 0) for r in ult)
        ev_ult = round(sum(float(r["pnl_neto_eur"] or 0) for r in ult) / st_u, 3) if st_u else None
        ic = _ic90_dias(por_dia)
        fm = round(muertas[mk] / env[mk], 3) if env[mk] else None
        gates = {"n>=40": len(g) >= RAMPA["n_min"], "dias>=10": len(por_dia) >= RAMPA["dias_min"],
                 "EV>=+0,05": ev is not None and ev >= RAMPA["ev_min"], "IC90_dias>0": bool(ic and ic[0] > 0),
                 "sin_2_mejores>0": ev_sin2 is not None and ev_sin2 > 0,
                 "FOK_muertas<=20%": fm is not None and fm <= RAMPA["fok_muertas_max"]}
        out[mk] = {"n": len(g), "dias": len(por_dia), "pnl_eur": round(pnl, 2), "ev_eur": ev, "ic90_dias": ic,
                   "ev_sin_2_mejores": ev_sin2, "ev_ultimas_20": ev_ult, "enviadas": env[mk], "fok_muertas": muertas[mk],
                   "fok_muertas_pct": fm, "gates": gates, "listo_para_subir": all(gates.values()),
                   "bajar_escalon": len(ult) >= RAMPA["ultimas"] and ev_ult is not None and ev_ult < 0}
    return out


def main() -> int:
    fok = _fok_reales()
    sen = _señales()
    gan = V._resolver_outcomes(sorted({mid for d in sen.values() for mid in d}))
    res, lineas = {}, []
    for marco in ("5m", "15m"):
        for off in OFFSETS:
            d = {mid: v for mid, v in sen.get((marco, off), {}).items() if mid in gan}
            porc = {}
            for mid, v in d.items():
                porc.setdefault(v["cierre"], []).append(pnl_por_euro(v["ask"], gan[mid] == v["dir"]))
            xs = [x for l in porc.values() for x in l]
            res[f"{marco}#{off}"] = {
                "n": len(d), "pendientes": len(sen.get((marco, off), {})) - len(d),
                "dias": len({v["dia"] for v in d.values()}),
                "acierto": round(sum(gan[m] == v["dir"] for m, v in d.items()) / len(d), 3) if d else None,
                "ask_medio": round(sum(v["ask"] for v in d.values()) / len(d), 3) if d else None,
                "ev_eur": round(sum(xs) / len(xs), 3) if xs else None, "ic90_cierre": _ic90(porc)}
        b, a = sen.get((marco, -45), {}), sen.get((marco, -47), {})
        comunes = [m for m in b if m in a and m in gan]
        dif = [pnl_por_euro(a[m]["ask"], gan[m] == a[m]["dir"]) - pnl_por_euro(b[m]["ask"], gan[m] == b[m]["dir"])
               for m in comunes]
        res[f"{marco}#emparejado"] = {
            "senales_T45": len(b), "tambien_a_T47": sum(1 for m in b if m in a),
            "solo_a_T47": sum(1 for m in a if m not in b), "comunes_resueltos": len(comunes),
            "dif_ev_T47_menos_T45": round(sum(dif) / len(dif), 3) if dif else None}

    lineas.append("⏱️ PRECIERRE: ¿adelantar de T-45 a T-46/T-47? (competidores casan en T-44,8 s)")
    lineas.append(f"FOK reales desde {DESDE_FOK}: {fok['enviadas']} enviadas, {fok['muertas']} muertas "
                  f"({fok['muertas_que_ganarian']}/{fok['muertas_resueltas']} de las muertas habrían ganado)")
    for marco in ("15m", "5m"):
        lineas.append(f"{marco} (z≥{Z_MIN}, banda {BANDA[marco]}, ≥5x; observador desde {DESDE_OFFSETS}Z):")
        for off in OFFSETS:
            x = res[f"{marco}#{off}"]
            ev = "-" if x["ev_eur"] is None else f"{x['ev_eur']:+.3f}"
            ac = "-" if x["acierto"] is None else f"{x['acierto']:.0%}"
            lineas.append(f"  T{off}: n={x['n']} ({x['dias']}d, {x['pendientes']} pend.) acierto {ac} ask {x['ask_medio']} "
                          f"EV/€ {ev} IC90 {x['ic90_cierre'] or 'n<10 cierres'}")
        e = res[f"{marco}#emparejado"]
        lineas.append(f"  mismos mercados: de {e['senales_T45']} señales a T-45, {e['tambien_a_T47']} también a T-47 "
                      f"(+{e['solo_a_T47']} solo a T-47); ΔEV T-47−T-45 = {e['dif_ev_T47_menos_T45']} (n={e['comunes_resueltos']})")
    try:
        rampa = _rampa()
    except Exception as e:                                   # el informe de offsets no depende de esto
        rampa = {"error": f"{type(e).__name__}: {e}"}
    lineas.append(f"📈 RAMPA de stake (desde {DESDE_RAMPA}Z, límite FOK nuevo; 2→5 € con n≥40, ≥10 días, EV≥+0,05, "
                  "IC90 días>0, >0 sin 2 mejores días, FOK muertas ≤20 %):")
    if "error" in rampa:
        lineas.append(f"  ⚠ no se pudo calcular: {rampa['error']}")
    for mk in ("15m", "5m"):
        x = rampa.get(mk)
        if not x:
            continue
        falta = [k for k, v in x["gates"].items() if not v]
        lineas.append(f"  {mk}: {x['n']} órdenes en {x['dias']} días | PnL {x['pnl_eur']:+.2f} € | EV/€ {x['ev_eur']} "
                      f"IC90 días {x['ic90_dias'] or 'n<3 días'} | sin 2 mejores {x['ev_sin_2_mejores']} | "
                      f"FOK muertas {x['fok_muertas']}/{x['enviadas']} | "
                      + ("✅ LISTO para proponer subir a Javi" if x["listo_para_subir"] else f"falta: {', '.join(falta)}")
                      + (" | 🔻 últimas 20 con EV<0: BAJAR escalón" if x["bajar_escalon"] else ""))
    n15 = res["15m#-47"]["n"]
    lineas.append(f"Estado: {'✅ 15m con n≥40 a T-47 -> LISTO para decidir con Javi' if n15 >= N_DECIDIR else f'EN CURSO (15m T-47 n={n15}/{N_DECIDIR})'}. "
                  "Nada cambia en real sin /code-review medium + OK de Javi.")
    msg = "\n".join(lineas)
    OUT.write_text(json.dumps({"actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                               "fok_reales": fok, "offsets": res, "rampa": rampa}, indent=1, ensure_ascii=False),
                   encoding="utf-8")
    print(msg)
    if "--telegram" in sys.argv:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg)
        print("Mensaje enviado a Telegram (bot=cripto).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
