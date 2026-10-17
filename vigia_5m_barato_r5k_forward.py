#!/usr/bin/env python3
"""vigia_5m_barato_r5k_forward.py -- forward DESCRIPTIVO y de solo lectura de H43 R5K (misión 5m barato, regla
CONGELADA 17-Oct 14:30Z en misiones/5m_barato/docs/REGISTRO_HIPOTESIS.md; no se retoca).

Regla: BTC 5m, unidad mercado-lado s. cum_banda(s) = acciones casadas como MAKER en el bid de s dentro de la banda
(0,10; 0,30] con T en (60, 300] s (definición del análisis original: experimentos/5m_barato/vendedores_tardios_17oct/,
pass1.py + an/mkslim.py; incluye los casados contra compradores de no-s). Al cruzar 5000 acciones, se miden las K=50
acciones de maker SIGUIENTES (prorrata en el relleno que cruza) con T en (60, 270] s, al precio y desenlace reales.
Es la POBLACIÓN con prioridad de cola optimista (nos tocarían esas 50): no es un resultado propio.
Criterio congelado: tras >=40 unidades en >=10 días -> REFUTADA si EV/€ < +0,05, o IC90 por cierre cruza 0, o EV sin
las 20 mejores unidades <= 0; si no, SIGUE. Antes: EN CURSO. EV siempre PONDERADO por € (Σpnl/Σcoste).
Fuente: on-chain /mnt/HC_Volume_106538179/m5_onchain/m5_onchain_D.csv.gz (filas del exchange; maker/tomador explícitos),
mapa de tokens desde las filas k del m5_registro (D-1 y D), desenlace oficial (gamma + /v2/tokens) con cobertura.
Uso: python3 vigia_5m_barato_r5k_forward.py [--telegram]   (cron propuesto 09:30 UTC; ~1 día nuevo cada mañana)
"""
import csv
import gzip
import json
import os
import random
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
VOL = Path("/mnt/HC_Volume_106538179")
CACHE = Path("/root/polymarket-research-datalogs/vigia_5m_barato_r5k")
PASS1 = REPO / "experimentos/5m_barato/vendedores_tardios_17oct/pass1.py"
OUT = REPO / "data/shadow/vigia_5m_barato_r5k.json"
DESDE = "2026-10-17"
OFFSET, K, T_MIN, T_MAX = 5000.0, 50.0, 60.0, 270.0
N_MIN, DIAS_MIN, EV_MIN = 40, 10, 0.05


def _dias():
    d, hoy = datetime.fromisoformat(DESDE).date(), datetime.now(timezone.utc).date()
    while d < hoy:
        s = d.isoformat()
        if (VOL / "m5_onchain" / f"m5_onchain_{s}.csv.gz").exists() and (VOL / "m5_registro" / f"m5_registro_{s}.csv.gz").exists():
            yield s
        d += timedelta(days=1)


def _kall(dia, destino):
    """Mapa token -> (act, marco, mkt, fin_iso, lado) desde las filas k del registro de D-1 y D (formato de kall.csv)."""
    vistos = set()
    with open(destino, "w", newline="") as fo:
        w = csv.writer(fo)
        for d in ((datetime.fromisoformat(dia) - timedelta(days=1)).date().isoformat(), dia):
            f = VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
            if not f.exists():
                continue
            try:
                with gzip.open(f, "rt", errors="replace") as fh:
                    for ln in fh:
                        if not ln.startswith("k,"):
                            continue
                        c = ln.rstrip("\n").split(",")
                        if len(c) >= 8 and c[2] not in vistos:
                            vistos.add(c[2])
                            w.writerow([c[2], c[3], c[4], c[5], c[6], c[7]])
            except (EOFError, OSError):
                pass
    return len(vistos)


def _band(dia):
    """band_D.csv.gz del día (pass1.py, en un proceso aparte con ulimit). Idempotente: si ya existe, se reutiliza."""
    d = CACHE / dia
    band = d / "out" / f"band_{dia}.csv.gz"
    if band.exists():
        return band
    (d / "out").mkdir(parents=True, exist_ok=True)
    n = _kall(dia, d / "kall.csv")
    if n == 0:
        raise RuntimeError(f"{dia}: sin filas k en el registro")
    tmp = d / "out_tmp"
    tmp.mkdir(exist_ok=True)
    cmd = f"ulimit -v 1500000; nice -n 19 ionice -c3 {sys.executable} {PASS1} {dia} {tmp}"
    r = subprocess.run(["bash", "-c", cmd], cwd=str(d), capture_output=True, text=True)
    if r.returncode != 0 or not (tmp / f"band_{dia}.csv.gz").exists():
        raise RuntimeError(f"{dia}: pass1 falló rc={r.returncode}: {r.stderr[-300:]}")
    for f in tmp.iterdir():
        f.rename(d / "out" / f.name)                # band, finpos, wstat
    tmp.rmdir()
    return band


def _filas(band):
    """Rellenos maker de BTC en banda, ordenados por (mercado, lado, ts) como an/build2.py + an/mkslim.py."""
    rs = []
    with gzip.open(band, "rt") as fh:
        rd = csv.reader(fh)
        h = next(rd)
        ix = {k: i for i, k in enumerate(h)}
        for c in rd:
            if c[ix["act"]] != "BTC":
                continue
            rs.append((c[ix["mkt"]], c[ix["lado_c"]], float(c[ix["ts"]]), float(c[ix["acc"]]), float(c[ix["coste"]]),
                       float(c[ix["T"]])))
    rs.sort(key=lambda x: (x[0], x[1], x[2]))
    return rs


def _unidades(dia, rs, des):
    """Por mercado-lado: las K acciones siguientes al cruce de OFFSET (prorrata), con T en (T_MIN, T_MAX]."""
    out, cum, prev = {}, 0.0, None
    sin_des = set()
    for mkt, lado, ts, acc, coste, T in rs:
        if (mkt, lado) != prev:
            prev, cum = (mkt, lado), 0.0
        cum0, cum = cum, cum + acc
        if acc <= 0:
            continue
        lo, hi = max(cum0 - OFFSET, 0.0), max(cum0 + acc - OFFSET, 0.0)
        tk = max(min(K, hi) - min(K, lo), 0.0)
        if tk <= 0 or not (T_MIN < T <= T_MAX):
            continue
        g = des.get(str(mkt))
        if g is None:
            sin_des.add(mkt)
            continue
        f = tk / acc
        gana = 1.0 if g == lado else 0.0
        u = out.setdefault((mkt, lado), {"dia": dia, "fin": round((ts + T) / 300) * 300, "c": 0.0, "p": 0.0, "acc": 0.0})
        u["c"] += coste * f
        u["p"] += (acc * gana - coste) * f
        u["acc"] += acc * f
    return out, sin_des


def _ic90(grupos, rng=random.Random(11)):
    if len(grupos) < 3:
        return None
    g = list(grupos.values())
    bs = []
    for _ in range(2000):
        m = [rng.choice(g) for _ in g]
        c = sum(x[0] for x in m)
        bs.append(sum(x[1] for x in m) / c if c else 0.0)
    bs.sort()
    return [round(bs[100], 3), round(bs[1899], 3)]


def main() -> int:
    sys.path.insert(0, str(REPO))
    from analisis_maker_cancelacion_binance import desenlaces   # gamma + /v2/tokens, con caché y fail-closed
    unidades, cobertura, errores = {}, {}, []
    for dia in _dias():
        try:
            rs = _filas(_band(dia))
            mids = sorted({r[0] for r in rs})
            des = desenlaces(mids)
            u, sd = _unidades(dia, rs, des)
            unidades.update({(dia,) + k: v for k, v in u.items()})
            cobertura[dia] = {"mercados": len(mids), "con_desenlace": sum(1 for m in mids if str(m) in des),
                              "unidades": len(u), "unidades_sin_desenlace": len(sd)}
        except Exception as e:
            errores.append(f"{dia}: {type(e).__name__}: {e}")
    us = list(unidades.values())
    c = sum(u["c"] for u in us)
    p = sum(u["p"] for u in us)
    por_dia, por_cierre = {}, {}
    for u in us:
        a = por_dia.setdefault(u["dia"], [0.0, 0.0]); a[0] += u["c"]; a[1] += u["p"]
        b = por_cierre.setdefault(u["fin"], [0.0, 0.0]); b[0] += u["c"]; b[1] += u["p"]
    ev = round(p / c, 4) if c else None
    ev_unidad = round(sum(u["p"] / u["c"] for u in us if u["c"]) / len(us), 4) if us else None
    top = sorted(us, key=lambda u: u["p"], reverse=True)[20:]
    ev_sin20 = round(sum(u["p"] for u in top) / sum(u["c"] for u in top), 4) if top and sum(u["c"] for u in top) else None
    mejores = sorted(por_dia, key=lambda d: por_dia[d][1], reverse=True)[:2]
    resto = [v for d, v in por_dia.items() if d not in mejores]
    ev_sin2 = round(sum(v[1] for v in resto) / sum(v[0] for v in resto), 4) if resto and sum(v[0] for v in resto) else None
    ic_c, ic_d = _ic90(por_cierre), _ic90(por_dia)
    acc = sum(u["acc"] for u in us)
    pm = round(c / acc, 3) if acc else None
    n, nd = len(us), len(por_dia)
    if n >= N_MIN and nd >= DIAS_MIN:
        motivos = [m for m, mal in (("EV<+0,05", ev is None or ev < EV_MIN), ("IC90 cierre cruza 0", not ic_c or ic_c[0] <= 0),
                                    ("sin top-20 <= 0", ev_sin20 is None or ev_sin20 <= 0)) if mal]
        veredicto = "REFUTADA (" + ", ".join(motivos) + ")" if motivos else "SIGUE"
    else:
        veredicto = f"EN CURSO ({n}/{N_MIN} unidades, {nd}/{DIAS_MIN} días)"
    res = {"actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "regla": "H43 R5K congelada 17-Oct",
           "n_unidades": n, "dias": nd, "coste_usd": round(c, 2), "pnl_usd": round(p, 2), "ev_eur_ponderado": ev,
           "ev_por_unidad": ev_unidad, "ic90_cierre": ic_c, "ic90_dias": ic_d, "ev_sin_2_mejores_dias": ev_sin2,
           "ev_sin_top20_unidades": ev_sin20, "precio_medio": pm,
           "por_dia": {d: {"coste": round(v[0], 2), "ev": round(v[1] / v[0], 4) if v[0] else None} for d, v in sorted(por_dia.items())},
           "cobertura": cobertura, "errores": errores, "veredicto": veredicto}
    OUT.write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    dias_txt = " ".join(f"{d[5:]}:{v['ev']:+.2f}" for d, v in res["por_dia"].items() if v["ev"] is not None)
    msg = (f"🧊 Vigía H43 R5K (forward desde {DESDE}; población, cola optimista; EV ponderado por €)\n"
           f"unidades {n} en {nd} días | coste {c:.0f} $ | EV/€ {ev} (por unidad {ev_unidad}) | IC90 cierre {ic_c} días {ic_d}\n"
           f"sin 2 mejores días {ev_sin2} | sin top-20 unidades {ev_sin20} | precio medio {pm}\n"
           f"por día: {dias_txt or '-'}\n"
           + (f"⚠ errores: {'; '.join(errores)}\n" if errores else "")
           + f"VEREDICTO: {veredicto}. Nada pasa a dinero sin micro-órdenes reales + /code-review + OK Javi.")
    print(msg)
    if "--telegram" in sys.argv:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg)
        print("Mensaje enviado a Telegram (bot=cripto).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
