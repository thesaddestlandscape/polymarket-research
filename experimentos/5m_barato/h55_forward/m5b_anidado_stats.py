"""m5b_anidado_stats.py -- lectura de entradas diarias, desenlace oficial, EV ponderado por EUR, IC90 por cierre y por dias,
sin 2 mejores dias, diferencias emparejadas y veredictos gate/kill. Sin E/S de red salvo `desenlaces` (gamma closed=true, cache)."""
import csv, glob, gzip, json, math, os, sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
import numpy as np

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import m5b_anidado_regla as R  # noqa: E402

DL = Path(os.environ.get("M5B_DL", "/root/polymarket-research-datalogs"))
ENTRADAS = Path(os.environ.get("M5B_SALIDA", str(DL / "vigia_5m_barato_anidado")))
OOS_DIA = "2026-10-19"          # OOS = cierres > 19-Oct 00:00Z (el cierre de las 00:00:00 ya estaba en el descubrimiento)
NBOOT, SEED = 4000, 20261020


def cargar(oos_dia=OOS_DIA):
    """-> (filas OOS de dias COMPLETOS, filas de dias parciales, dias_completos, dias_parciales)."""
    ok, par, dc, dp = [], [], [], []
    for fm in sorted(ENTRADAS.glob("entradas_*.meta.json")):
        m = json.loads(fm.read_text())
        if m["dia"] < oos_dia:
            continue
        fo = ENTRADAS / f"entradas_{m['dia']}.csv.gz"
        if not fo.exists():
            continue
        with gzip.open(fo, "rt") as fh:
            filas = list(csv.DictReader(fh))
        (ok if m["completo"] else par).extend(filas)
        (dc if m["completo"] else dp).append(m["dia"])
    return ok, par, dc, dp


def desenlace_por_m5(filas):
    f = os.environ.get("M5B_DES")
    if f:
        return json.load(open(f))
    sys.path.insert(0, "/root/polymarket-research")
    from analisis_maker_cancelacion_binance import desenlaces
    return desenlaces(sorted({r["m5"] for r in filas}))


def gana_de(r, des):
    o = des.get(r["m5"])
    return None if o is None else (o == ("YES" if r["lado"] == "Up" else "NO"))


def f(x):
    return None if x in ("", None) else float(x)


def brazo_tomador(filas, regla, des):
    """Una entrada por cierre. -> (lista de operaciones ejecutadas con desenlace, contadores)."""
    ops, c = [], dict(disparos=0, no_llena=0, pendiente_desenlace=0)
    for r in filas:
        if f(r.get(f"{regla}_t")) is None:
            continue
        c["disparos"] += 1
        acc, pr = float(r[f"{regla}_acc"] or 0), f(r[f"{regla}_precio"])
        if acc <= 0 or pr is None:
            c["no_llena"] += 1
            continue
        g = gana_de(r, des)
        if g is None:
            c["pendiente_desenlace"] += 1
            continue
        pnl, coste = R.pnl_tomador(acc, pr, g)
        ops.append(dict(dia=r["dia"], cierre=int(r["cierre"]), pnl=pnl, coste=coste, precio=pr, gana=bool(g), acc=acc))
    return ops, c


def brazo_maker(filas, des):
    ops, c = [], dict(disparos=0, no_llena=0, pendiente_desenlace=0)
    for r in filas:
        if float(r["mk_n_cotiz"] or 0) <= 0:
            continue
        c["disparos"] += 1
        ll = float(r["mk_lleno"] or 0)
        if ll <= 0:
            c["no_llena"] += 1
            continue
        g = gana_de(r, des)
        if g is None:
            c["pendiente_desenlace"] += 1
            continue
        pnl, coste = R.pnl_maker(ll, float(r["mk_coste"]), g)
        ops.append(dict(dia=r["dia"], cierre=int(r["cierre"]), pnl=pnl, coste=coste, precio=float(r["mk_coste"]) / ll, gana=bool(g), acc=ll))
    return ops, c


def brazo_combinado(filas, des):
    ops, c = [], dict(maker=0, tomador=0, nada=0)
    for r in filas:
        th, ej = f(r.get("h53_t")), float(r.get("h53_acc") or 0) > 0
        mk_ll, mk_t = float(r["mk_lleno"] or 0), f(r["mk_t_rel"])
        via = R.combinado_una_via(mk_ll, mk_t, th, ej)
        c[via] += 1
        g = gana_de(r, des)
        if via == "nada" or g is None:
            continue
        if via == "maker":
            pnl, coste = R.pnl_maker(mk_ll, float(r["mk_coste"]), g)
        else:
            pnl, coste = R.pnl_tomador(float(r["h53_acc"]), f(r["h53_precio"]), g)
        ops.append(dict(dia=r["dia"], cierre=int(r["cierre"]), pnl=pnl, coste=coste, via=via, gana=bool(g)))
    return ops, c


def _ratio(g):
    return g[:, 0].sum() / g[:, 1].sum() if g[:, 1].sum() > 0 else float("nan")


def boot_ratio(grupos, q=5, nboot=NBOOT, seed=SEED):
    """IC (q, 100-q) % de Sum pnl / Sum coste remuestreando GRUPOS (cierres o dias). None si <3 grupos."""
    g = np.array(grupos, dtype=float)
    if len(g) < 3:
        return None
    rng = np.random.default_rng(seed)
    ix = rng.integers(0, len(g), (nboot, len(g)))
    r = g[ix, 0].sum(1) / np.maximum(g[ix, 1].sum(1), 1e-12)
    return tuple(float(x) for x in np.percentile(r, [q, 100 - q]).round(4))


def por_dia(ops):
    d = {}
    for o in ops:
        a = d.setdefault(o["dia"], [0.0, 0.0]); a[0] += o["pnl"]; a[1] += o["coste"]
    return d


def resumen(ops, nombre, dias_calendario=None):
    out = {"brazo": nombre, "n": len(ops)}
    if not ops:
        return out
    pn, co = sum(o["pnl"] for o in ops), sum(o["coste"] for o in ops)
    pd_ = por_dia(ops)
    top2 = sorted(pd_, key=lambda k: -pd_[k][0])[:2]
    resto = [v for k, v in pd_.items() if k not in top2]
    r_i = np.array([o["pnl"] / o["coste"] for o in ops])
    out.update({
        "dias_con_operacion": len(pd_), "coste_eur": round(co, 2), "pnl_eur": round(pn, 2), "ev_pond_por_eur": round(pn / co, 4),
        "ev_medio_por_unidad": round(float(r_i.mean()), 4),
        "ic90_por_cierre": boot_ratio([(o["pnl"], o["coste"]) for o in ops]),
        "ic90_por_dias": boot_ratio(list(pd_.values())),
        "ev_sin_2_mejores_dias": (round(sum(v[0] for v in resto) / sum(v[1] for v in resto), 4) if len(pd_) >= 3 and sum(v[1] for v in resto) > 0 else None),
        "dias_positivos": sum(1 for v in pd_.values() if v[0] > 0), "acierto": round(float(np.mean([o["gana"] for o in ops])), 3),
        "g_log_f10": round(float(np.mean(np.log1p(0.10 * r_i))), 5),     # crecimiento compuesto por operacion a f=10 % (proxy de analisis_log_growth)
        "perdidas_con_precio_ge_090": [(o["dia"], o["cierre"]) for o in ops if (not o["gana"]) and o.get("precio", 0) >= 0.90],
    })
    if dias_calendario:
        out["pnl_por_dia_calendario_eur"] = round(pn / dias_calendario, 3)
        out["entradas_por_dia"] = round(len(ops) / dias_calendario, 3)
        out["coste_por_dia_eur"] = round(co / dias_calendario, 2)
    return out


def dif_emparejada(A, B, nombre):
    """EV_pond(A) - EV_pond(B) sobre la UNION de cierres, IC90 remuestreando cierres (cada cierre aporta (pnlA,costeA,pnlB,costeB))."""
    da, db = {o["cierre"]: o for o in A}, {o["cierre"]: o for o in B}
    cs = sorted(set(da) | set(db))
    if len(cs) < 3:
        return {"comparacion": nombre, "n_cierres": len(cs), "dif": None}
    M = np.array([[da[c]["pnl"] if c in da else 0, da[c]["coste"] if c in da else 0, db[c]["pnl"] if c in db else 0,
                   db[c]["coste"] if c in db else 0] for c in cs], dtype=float)
    est = lambda m: m[:, 0].sum() / max(m[:, 1].sum(), 1e-12) - m[:, 2].sum() / max(m[:, 3].sum(), 1e-12)
    rng = np.random.default_rng(SEED + 1)
    ix = rng.integers(0, len(cs), (NBOOT, len(cs)))
    b = [est(M[i]) for i in ix]
    return {"comparacion": nombre, "n_cierres": len(cs), "dif": round(float(est(M)), 4),
            "ic90_por_cierre": tuple(float(x) for x in np.percentile(b, [5, 95]).round(4)), "pnl_dif_eur": round(float(M[:, 0].sum() - M[:, 2].sum()), 2)}


def ventana_perdidas_ask90(res, ventana_dias=10, k=2):
    """True si alguna ventana de `ventana_dias` dias naturales contiene >= k perdidas totales con precio >= 0,90."""
    ds = sorted(datetime.fromisoformat(d).date() for d, _ in res.get("perdidas_con_precio_ge_090", []))
    return any(ds[i + k - 1] - ds[i] < timedelta(days=ventana_dias) for i in range(len(ds) - k + 1)) if len(ds) >= k else False


def veredicto_h55(r):
    n = r.get("n", 0)
    kill = (n >= 25 and r["ev_pond_por_eur"] < -0.10) or ventana_perdidas_ask90(r) if n else False
    cond = {"n>=40": n >= 40, "dias>=10": r.get("dias_con_operacion", 0) >= 10,
            "ev_pond>=+0,08": bool(n) and r["ev_pond_por_eur"] >= 0.08,
            "ic90_cierre_inf>0": bool(n) and r["ic90_por_cierre"] is not None and r["ic90_por_cierre"][0] > 0,
            "sin_2_mejores_dias>0": bool(n) and r["ev_sin_2_mejores_dias"] is not None and r["ev_sin_2_mejores_dias"] > 0}
    v = "KILLED_REJECTED" if kill else ("GATE_SUPERADO_pasa_a_revision" if all(cond.values()) else "PENDIENTE")
    return {"veredicto": v, "kill_disparado": bool(kill), "condiciones_gate": cond}


def veredicto_h53(r, dif_v4):
    n = r.get("n", 0)
    kill = bool(n) and ((n >= 25 and r["ev_pond_por_eur"] < -0.15) or (n >= 20 and r["ic90_por_cierre"] is not None and r["ic90_por_cierre"][1] < 0))
    cond = {"n>=40": n >= 40, "dias>=10": r.get("dias_con_operacion", 0) >= 10,
            "ev_pond>=+0,10": bool(n) and r["ev_pond_por_eur"] >= 0.10,
            "ic90_cierre_inf>0": bool(n) and r["ic90_por_cierre"] is not None and r["ic90_por_cierre"][0] > 0,
            "sin_2_mejores_dias>0": bool(n) and r["ev_sin_2_mejores_dias"] is not None and r["ev_sin_2_mejores_dias"] > 0,
            "dif_emparejada_vs_V4_ic90_inf>0": bool(dif_v4.get("dif") is not None and dif_v4["ic90_por_cierre"][0] > 0)}
    return {"veredicto": "KILLED_REJECTED" if kill else ("GATE_SUPERADO_pasa_a_revision" if all(cond.values()) else "PENDIENTE"),
            "kill_disparado": kill, "condiciones_gate": cond}


def manifiesto(dir_, nombre, cfg, archivos_codigo, dia=None):
    """Congelacion: hash(config + codigo). Si cambia -> SystemExit (hay que subir version y abrir OOS nuevo)."""
    import hashlib
    dir_.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256(json.dumps(cfg, sort_keys=True).encode())
    for a in sorted(archivos_codigo, key=lambda p: p.name):
        h.update(a.name.encode() + Path(a).read_bytes())
    hc = h.hexdigest()[:16]
    fm = dir_ / "manifiesto.json"
    m = json.loads(fm.read_text()) if fm.exists() else {"versiones": {}}
    v = m["versiones"].setdefault(str(cfg["version"]), {"hash": hc, "inicio_utc": datetime.now(timezone.utc).isoformat(), "config": cfg,
                                                       "archivos": {a.name: hashlib.sha256(Path(a).read_bytes()).hexdigest()[:16] for a in archivos_codigo}, "dias": []})
    if v["hash"] != hc:
        raise SystemExit(f"STOP: codigo/config de {nombre} v{cfg['version']} cambio ({v['hash']} -> {hc}). Regla congelada: nueva version y nuevo OOS.")
    if dia and dia not in v["dias"]:
        v["dias"].append(dia)
    fm.write_text(json.dumps(m, indent=1))
    return hc


def dias_calendario(dc):
    return len(dc)
