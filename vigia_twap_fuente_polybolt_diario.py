#!/usr/bin/env python3
"""vigia_twap_fuente_polybolt_diario.py -- ¿puede el ejecutor de precierre/naive vivir SIN RTDS?

Contexto (30-Sep): la resolución real es TWAP60 Chainlink de cierre vs de apertura. Hoy el
ejecutor (resolution_sniper_precierre_executor.py) reconstruye ambos con los ticks Chainlink
de RTDS (chainlink_*.csv). RTDS `crypto_prices_chainlink` se retirará sin fecha, y PolyBolt
solo da Chainlink en el canal twap60 (oficial); su spot es PYTH (sesgo +0,1/+0,4 bps).

Este vigía reproduce offline, con los CSV ya capturados, la decisión de dirección en los dos
instantes del ejecutor (T-45 s precierre y T+0 naive) con dos métodos y la compara contra el
desenlace real (resolution_sniper_obs_*.csv):

  hoy      : ticks Chainlink RTDS para la proyección + referencia reconstruida con esos ticks
  polybolt : spot Pyth CORREGIDO (se le resta su sesgo, medido en tiempo real como
             media_pyth[t-62,t-2] - twap60_oficial(t-2)) + referencia = twap60 oficial(ts_start)

Hallazgos del 29-Sep que motivan medirlo a diario antes de tocar dinero real:
  - twap60 oficial en el segundo exacto reproduce el desenlace en 1664/1664 (5min) y 561/561
    (15min); la reconstrucción con ticks RTDS, 99,0 % / 99,4 %.
  - PERO a T-45 s cambiar solo la referencia por la oficial NO mejora el acierto (mezclar
    fuentes reintroduce el desfase reconstruido-vs-oficial): lo que cuenta es que proyección
    y referencia salgan de la MISMA fuente. El método `polybolt` completo iguala al de hoy.

Solo lectura, sin dinero. Días cerrados se cachean en el JSON de salida. Cron diario; con
--telegram envía el resumen. Criterio para proponer el cambio de fuente en el ejecutor (decisión
de Javi + /code-review): >=10 días y acierto de `polybolt` no inferior al de `hoy` en los
mercados con margen >=2 bps (IC90 por días de la diferencia que no quede por debajo de -0,5 pp).
"""
import bisect
import csv
import glob
import gzip
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DIR_PRICES = REPO / "data" / "prices"
DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "vigia_twap_fuente_polybolt.json"
MARCOS = {"5min": 300, "15min": 900}
INSTANTES = {"precierre_T-45": 45, "naive_T+0": 0}
MARGENES_BPS = (0, 1, 2, 4)
N_MIN_REF = 50        # ticks/segundos mínimos en la ventana de 60 s de la referencia
N_MIN_PROY = 10       # ídem en el tramo ya transcurrido de la ventana de cierre
RETRASO_OFICIAL_S = 2
VENTANA_DESDE_S, VENTANA_HASTA_S = 62, 3   # twap60 oficial de e = media RTDS [e-62, e-3] (02-Oct)
METODOS_PB = ("polybolt", "polybolt_t60a", "polybolt_s30")  # el twap60 oficial del segundo t llega ~1,3 s después (p99 2,0 s)


def _abrir(p):
    return gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")


def _ruta(prefijo: str, dia: str, directorio: Path):
    for cand in (directorio / f"{prefijo}_{dia}.csv", directorio / f"{prefijo}_{dia}.csv.gz"):
        if cand.exists():
            return cand
    return None


def _cargar_dia(dia: str):
    """(twap oficial, spot pyth, ticks chainlink, desenlaces) del día, o None si falta algo."""
    p_pb, p_cl = _ruta("polybolt", dia, DIR_PRICES), _ruta("chainlink", dia, DIR_PRICES)
    p_obs = _ruta("resolution_sniper_obs", dia, DIR_SHADOW)
    if not (p_pb and p_cl and p_obs):
        return None
    tw, py, s30 = {}, {}, {}
    with _abrir(p_pb) as f:
        for r in csv.DictReader(f):
            if r.get("snapshot") != "0":
                continue
            try:
                k = (r["asset"], int(r["event_ts_ms"]) // 1000)
                v = float(r["value"])
            except (ValueError, TypeError, KeyError):
                continue
            if r.get("canal") == "twap60":
                tw.setdefault(k, v)
            elif (r.get("source") or "pyth") == "pyth":
                # 02-Oct: desde las 02:53Z PolyBolt sirve el spot como `chainlink`, una serie
                # suavizada (~media móvil 35 s, ~17 s de retraso) que el método solo-PolyBolt
                # no puede usar. Solo filas pyth (las de antes del 30-Sep no traen `source`).
                py.setdefault(k, v)
            elif r.get("source") == "chainlink":
                s30.setdefault(k, v)      # media EXACTA de los ticks Chainlink de [t-32, t-3] s
    ts, px = {}, {}
    with _abrir(p_cl) as f:
        for r in csv.DictReader(f):
            if r.get("source") != "chainlink":      # fuera coingecko y polybolt_fallback (Pyth)
                continue
            try:
                ts.setdefault(r["asset"], []).append((int(r["ws_timestamp_ms"]) / 1000, float(r["price_usd"])))
            except (ValueError, TypeError, KeyError):
                continue
    for a in list(ts):
        ts[a].sort()
        px[a] = [p for _, p in ts[a]]
        ts[a] = [t for t, _ in ts[a]]
    out = {}
    with _abrir(p_obs) as f:
        for r in csv.DictReader(f):
            if r.get("outcome_real") in ("Up", "Down") and r.get("marco") in MARCOS:
                try:
                    out[(r["activo"], r["marco"], int(r["ts_end"]))] = r["outcome_real"]
                except (ValueError, KeyError):
                    continue
    return tw, py, s30, ts, px, out


def _evaluar_dia(dia: str):
    datos = _cargar_dia(dia)
    if datos is None:
        return None
    tw, py, s30, ts, px, out = datos

    def media_cl(a, t0, t1):
        v = ts.get(a)
        if not v:
            return None, 0, None
        i, j = bisect.bisect_left(v, t0), bisect.bisect_right(v, t1)
        return (sum(px[a][i:j]) / (j - i), j - i, px[a][j - 1]) if j > i else (None, 0, None)

    def media_py(a, t0, t1):
        v = [py[(a, s)] for s in range(int(t0), int(t1) + 1) if (a, s) in py]
        return (sum(v) / len(v), len(v), v[-1]) if v else (None, 0, None)

    # 02-Oct: ventana oficial del twap60 de e = [e-62, e-3] (ver VENTANA_*); el ejecutor y
    # shadow_predict se alinearon el mismo día. Se alinean la proyección y la referencia de
    # TODOS los métodos; la ventana del SESGO no: `polybolt` la sigue midiendo en [t-60, t] y
    # `polybolt_t60a` en [t-62, t-3] (esa es justo la diferencia entre ambos). Días cacheados
    # antes del cambio: recalcular con --recalcular para no mezclar definiciones en el gate.
    def proy(media, a, e, off):
        hasta = min(e - VENTANA_HASTA_S, e - off)
        m, n, sp = media(a, e - VENTANA_DESDE_S, hasta)
        if n < N_MIN_PROY:
            return None
        resto = (e - VENTANA_HASTA_S) - hasta
        return (m * n + sp * resto) / (n + resto)

    def hoy(a, e, dur, off):
        ref, n, _ = media_cl(a, e - dur - VENTANA_DESDE_S, e - dur - VENTANA_HASTA_S)
        if n < N_MIN_REF:
            return None
        p = proy(media_cl, a, e, off)
        return None if p is None else (p, ref)

    def polybolt(a, e, dur, off):
        ref = tw.get((a, e - dur))
        t = e - off - RETRASO_OFICIAL_S
        oficial = tw.get((a, t))
        mp, n, _ = media_py(a, t - 60, t)
        if ref is None or oficial is None or n < N_MIN_REF:
            return None
        p = proy(media_py, a, e, off)
        return None if p is None else (p - (mp - oficial), ref)

    # 02-Oct, dos variantes fijadas ANTES de ver datos (mismo gate que `polybolt`):
    #  polybolt_t60a: igual que `polybolt` pero con la media Pyth en la MISMA ventana que el
    #    twap60 oficial (media de [t-62, t-3], medido 02-Oct); `polybolt` usa [t-60, t].
    #  polybolt_s30: sesgo = media de 10 comparaciones exactas de 30 s (Pyth [t-32, t-3] contra
    #    el spot `chainlink` de PolyBolt, que es la media de esos mismos ticks Chainlink),
    #    t = tc, tc-10, ..., tc-90 (~2 min de sesgo).
    def polybolt_t60a(a, e, dur, off):
        ref = tw.get((a, e - dur))
        t = e - off - RETRASO_OFICIAL_S
        oficial = tw.get((a, t))
        mp, n, _ = media_py(a, t - 62, t - 3)
        if ref is None or oficial is None or n < N_MIN_REF:
            return None
        p = proy(media_py, a, e, off)
        return None if p is None else (p - (mp - oficial), ref)

    def polybolt_s30(a, e, dur, off):
        ref = tw.get((a, e - dur))
        tc = e - off - RETRASO_OFICIAL_S
        sesgos = []
        for t in range(tc - 90, tc + 1, 10):
            cl30 = s30.get((a, t))
            mp, n, _ = media_py(a, t - 32, t - 3)
            if cl30 is not None and n >= 25:
                sesgos.append(mp - cl30)
        if ref is None or len(sesgos) < 6:
            return None
        p = proy(media_py, a, e, off)
        return None if p is None else (p - sum(sesgos) / len(sesgos), ref)

    metodos = {"hoy": hoy, "polybolt": polybolt, "polybolt_t60a": polybolt_t60a, "polybolt_s30": polybolt_s30}
    res = {}
    for (a, marco, e), o in out.items():
        dur = MARCOS[marco]
        for inst, off in INSTANTES.items():
            pares = {}
            for nombre, fn in metodos.items():
                r = fn(a, e, dur, off)
                if r is None:
                    continue
                p, ref = r
                mg = abs(p - ref) / ref * 1e4
                ok = int(("Up" if p >= ref else "Down") == o)
                pares[nombre] = (mg, ok)
                for u in MARGENES_BPS:
                    if mg >= u:
                        for clave in (f"{inst}|{marco}|TODOS|{nombre}|{u}", f"{inst}|{marco}|{a}|{nombre}|{u}"):
                            c = res.setdefault(clave, [0, 0])
                            c[0] += 1
                            c[1] += ok
            for nombre in METODOS_PB:
                if "hoy" in pares and nombre in pares and pares["hoy"][0] >= 2 and pares[nombre][0] >= 2:
                    suf = "" if nombre == "polybolt" else f"|{nombre}"
                    c = res.setdefault(f"{inst}|{marco}|TODOS|pareado>=2bps{suf}", [0, 0, 0])   # n, solo_hoy_ok, solo_pb_ok
                    c[0] += 1
                    c[1] += int(pares["hoy"][1] and not pares[nombre][1])
                    c[2] += int(pares[nombre][1] and not pares["hoy"][1])
    return {"n_mercados": len(out), "celdas": res}


def _dias_disponibles():
    dias = set()
    for p in glob.glob(str(DIR_PRICES / "polybolt_*.csv*")):
        dias.add(Path(p).name.split("_")[1][:10])
    return sorted(dias)


def _agregar(por_dia: dict) -> dict:
    tot = {}
    for d in por_dia.values():
        for k, c in d["celdas"].items():
            t = tot.setdefault(k, [0] * len(c))
            for i, v in enumerate(c):
                t[i] += v
    return tot


def _ic90_dif_por_dias(por_dia: dict, inst: str, marco: str, u: int = 2, metodo: str = "polybolt"):
    """Bootstrap por DÍAS de (acierto `metodo` - acierto hoy) en pp, margen >= u bps."""
    dias = [d["celdas"] for d in por_dia.values()
            if f"{inst}|{marco}|TODOS|hoy|{u}" in d["celdas"] and f"{inst}|{marco}|TODOS|{metodo}|{u}" in d["celdas"]]
    if len(dias) < 3:
        return None
    rng = random.Random(42)
    difs = []
    for _ in range(2000):
        m = [rng.choice(dias) for _ in dias]
        nh = sum(c[f"{inst}|{marco}|TODOS|hoy|{u}"][0] for c in m)
        kh = sum(c[f"{inst}|{marco}|TODOS|hoy|{u}"][1] for c in m)
        npb = sum(c[f"{inst}|{marco}|TODOS|{metodo}|{u}"][0] for c in m)
        kpb = sum(c[f"{inst}|{marco}|TODOS|{metodo}|{u}"][1] for c in m)
        difs.append((kpb / npb - kh / nh) * 100)
    difs.sort()
    return round(difs[int(0.05 * len(difs))], 2), round(difs[int(0.95 * len(difs))], 2)


def main() -> int:
    hoy_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    try:
        previo = json.loads(OUT.read_text(encoding="utf-8")).get("por_dia", {})
    except Exception:
        previo = {}
    por_dia = {}
    for dia in _dias_disponibles():
        if dia == hoy_utc:
            continue                      # día en curso: incompleto, no se evalúa
        if dia in previo and "--recalcular" not in sys.argv:
            por_dia[dia] = previo[dia]    # día cerrado ya calculado
            continue
        r = _evaluar_dia(dia)
        if r is not None:
            por_dia[dia] = r
            print(f"{dia}: {r['n_mercados']} mercados con desenlace", flush=True)
    tot = _agregar(por_dia)
    resumen, lineas = {}, [f"🛰️ TWAP sin RTDS (PolyBolt) vs método de hoy — {len(por_dia)} días"]
    for inst in INSTANTES:
        for marco in MARCOS:
            fila = {}
            for nombre in ("hoy",) + METODOS_PB:
                for u in MARGENES_BPS:
                    c = tot.get(f"{inst}|{marco}|TODOS|{nombre}|{u}")
                    if c and c[0]:
                        fila[f"{nombre}_>={u}bps"] = {"n": c[0], "acierto_pct": round(c[1] / c[0] * 100, 2)}
            for nombre in METODOS_PB:
                suf = "" if nombre == "polybolt" else f"|{nombre}"
                par = tot.get(f"{inst}|{marco}|TODOS|pareado>=2bps{suf}")
                if par:
                    fila[f"pareado_>=2bps{suf}"] = {"n": par[0], "solo_hoy_acierta": par[1], f"solo_{nombre}_acierta": par[2]}
            ic = _ic90_dif_por_dias(por_dia, inst, marco)
            if ic:
                fila["ic90_dif_pp_polybolt_menos_hoy_>=2bps"] = ic
            resumen[f"{inst}|{marco}"] = fila
            h, p = fila.get("hoy_>=2bps"), fila.get("polybolt_>=2bps")
            if h and p:
                lineas.append(f"{inst} {marco} (margen≥2bps): hoy {h['acierto_pct']}% n={h['n']} | "
                              f"polybolt {p['acierto_pct']}% n={p['n']}" + (f" | IC90 dif {ic[0]}..{ic[1]} pp" if ic else ""))
            for nombre in METODOS_PB[1:]:      # variantes 02-Oct: solo días con su serie
                pv = fila.get(f"{nombre}_>=2bps")
                if not pv:
                    continue
                icv = _ic90_dif_por_dias(por_dia, inst, marco, metodo=nombre)
                if icv:
                    fila[f"ic90_dif_pp_{nombre}_menos_hoy_>=2bps"] = icv
                par = fila.get(f"pareado_>=2bps|{nombre}", {})
                lineas.append(f"   └ {nombre}: {pv['acierto_pct']}% n={pv['n']}"
                              + (f" | pareado: solo hoy {par.get('solo_hoy_acierta')} / solo {nombre} {par.get(f'solo_{nombre}_acierta')}" if par else "")
                              + (f" | IC90 dif {icv[0]}..{icv[1]} pp" if icv else " | <3 días"))
    por_activo = {}
    for k, c in tot.items():
        inst, marco, activo, nombre, u = (k.split("|") + [""])[:5]
        if activo != "TODOS" and u == "2" and c[0]:
            por_activo[f"{inst}|{marco}|{activo}|{nombre}"] = {"n": c[0], "acierto_pct": round(c[1] / c[0] * 100, 2)}
    listo = len(por_dia) >= 10
    lineas.append("Gate para proponer el cambio de fuente: ≥10 días e IC90 de la diferencia ≥ −0,5 pp. "
                  + ("YA hay ≥10 días: revisar." if listo else f"Faltan {10 - len(por_dia)} días."))
    OUT.write_text(json.dumps({
        "generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "dias": sorted(por_dia), "resumen": resumen, "por_activo_margen>=2bps": por_activo,
        "por_dia": por_dia,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
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
