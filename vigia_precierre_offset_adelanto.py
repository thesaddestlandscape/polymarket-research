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
    n15 = res["15m#-47"]["n"]
    lineas.append(f"Estado: {'✅ 15m con n≥40 a T-47 -> LISTO para decidir con Javi' if n15 >= N_DECIDIR else f'EN CURSO (15m T-47 n={n15}/{N_DECIDIR})'}. "
                  "Nada cambia en real sin /code-review medium + OK de Javi.")
    msg = "\n".join(lineas)
    OUT.write_text(json.dumps({"actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                               "fok_reales": fok, "offsets": res}, indent=1, ensure_ascii=False), encoding="utf-8")
    print(msg)
    if "--telegram" in sys.argv:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg)
        print("Mensaje enviado a Telegram (bot=cripto).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
