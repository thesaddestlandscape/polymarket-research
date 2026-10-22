#!/usr/bin/env python3
"""r3_vigia.py [--telegram] [--dir DIR] [--ledger RUTA] -- VIGIA DIARIO del brazo shadow R2/R3 (solo lectura; no toca B ni ejecutores ni screens).
Aplica el gate de r3_shadow_preregistro.json (CONGELADO; los umbrales se LEEN de su seccion `parametros_gate` y el vigia FALLA CERRADO si el sha256 del fichero no coincide con
HASH_PREREG.txt): dias validos >= 10 (>= 80 % de los 864 mercados esperados con mkt_fin completo),
EV ponderado por EUR, DIF = EV(BASE con flag true al pujar) - EV(BASE con flag false), IC por remuestreo de DIAS, sin los 2 mejores dias, en cons_x Y cons_r.
Informa ademas: cobertura por dia/moneda (esperado/recibido/completo/huecos/sin desenlace), EV por moneda, retencion de EUR, motivos de no cotizar, cota optimista opt_x y,
como INFORMACION (no entra en el veredicto), el emparejamiento con B real (ledger experimento_h47_B_ledger.jsonl) segun el flag de la regla en su puja_post.
Telegram solo si cambia el veredicto de alguna regla (latch por veredicto, NO por cifras; el latch se escribe DESPUES de que Telegram confirme el envio: si falla, se reintenta
en la siguiente corrida y el vigia sale con codigo 1). Estado: DIR/estado_r3_shadow.json."""
import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import r3_shadow as S  # noqa: E402

PREREG = HERE / "r3_shadow_preregistro.json"
HASH_PREREG = HERE / "HASH_PREREG.txt"
REGLAS = ("R2", "R3")
CLAVES_PARAMS = ("esperados_dia", "cobertura_dia_min", "dias_min", "dias_no_conf", "n_true_min", "n_false_min", "bootstrap_n", "seed_ev", "seed_dif", "mejores_dias_excluidos",
                 "ic_confirmada", "ic_refutada", "escenarios_primarios")
# lo unico que el CODIGO implementa y el JSON solo puede confirmar (si el JSON dijera otra cosa, el vigia no lo respetaria en silencio: falla cerrado)
IMPLEMENTADO = {"ic_confirmada": "ic95", "ic_refutada": "ic90", "escenarios_primarios": ["cons_x", "cons_r"]}


class PreregInvalido(RuntimeError):
    pass


def cargar_prereg(prereg=None, hash_file=None):
    """Parametros del gate desde el preregistro CONGELADO. Fail-closed (PreregInvalido) si falta HASH_PREREG.txt, el sha256 del fichero entero no coincide, falta/sobra
    alguna clave de `parametros_gate` o el JSON pide algo que este codigo no implementa. Devuelve (params, sha256 completo)."""
    prereg, hash_file = Path(prereg or PREREG), Path(hash_file or HASH_PREREG)
    try:
        esperado = hash_file.read_text().split()[0].strip().lower()
    except (OSError, IndexError) as e:
        raise PreregInvalido(f"sin HASH_PREREG.txt legible ({hash_file}): {e}")
    try:
        crudo = prereg.read_bytes()
    except OSError as e:
        raise PreregInvalido(f"preregistro ilegible: {e}")
    real = hashlib.sha256(crudo).hexdigest()
    if real != esperado:
        raise PreregInvalido(f"sha256 del preregistro {real[:16]}... != HASH_PREREG.txt {esperado[:16]}...: preregistro modificado tras congelarlo; el gate no se evalua")
    try:
        p = json.loads(crudo)["parametros_gate"]
    except (ValueError, KeyError, TypeError) as e:
        raise PreregInvalido(f"preregistro sin `parametros_gate` legible: {e}")
    if set(p) - {"nota"} != set(CLAVES_PARAMS):
        raise PreregInvalido(f"parametros_gate: claves {sorted((set(p) - {"nota"}) ^ set(CLAVES_PARAMS))} de mas o de menos")
    for k, v in IMPLEMENTADO.items():
        if p[k] != v:
            raise PreregInvalido(f"parametros_gate.{k}={p[k]!r}: este vigia solo implementa {v!r}")
    return p, real


_PARAMS = []


def params():
    """Parametros del preregistro vigente (cache de proceso); PreregInvalido si no verifica."""
    if not _PARAMS:
        _PARAMS.append(cargar_prereg()[0])
    return _PARAMS[0]


LEDGER_B = "/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl"


# ------------------------------------------------------------------ estadistica (por EUR, remuestreo de DIAS)
def _g(df, mask=None):
    """Sumas diarias (pnl, coste) de las filas de df (lista de dicts) opcionalmente filtradas."""
    p, c = defaultdict(float), defaultdict(float)
    for r in df:
        if mask is None or mask(r):
            p[r["dia"]] += r["pnl"]
            c[r["dia"]] += r["coste"]
    return p, c


def ev_dias(rows, n=4000, seed=1, k_sin=2):
    """EV agregado + IC90/IC95 por dias + EV sin los 2 mejores dias (por pnl)."""
    p, c = _g(rows)
    dias = sorted(c)
    out = {"n": len(rows), "dias": len(dias), "eur": round(sum(c.values()), 2), "ev": None, "ic90": [None, None], "ic95": [None, None], "ev_sin2": None, "dias_pos": None}
    if not dias or sum(c.values()) <= 0:
        return out
    a = np.array([p[d] for d in dias])
    b = np.array([c[d] for d in dias])
    out["ev"] = float(a.sum() / b.sum())
    out["dias_pos"] = int((a > 0).sum())
    if len(dias) >= 2:
        r = np.random.default_rng(seed)
        i = r.integers(0, len(dias), (n, len(dias)))
        e = a[i].sum(1) / np.maximum(b[i].sum(1), 1e-9)
        out["ic90"] = [float(np.quantile(e, .05)), float(np.quantile(e, .95))]
        out["ic95"] = [float(np.quantile(e, .025)), float(np.quantile(e, .975))]
        o = np.argsort(-a)[k_sin:]
        out["ev_sin2"] = float(a[o].sum() / b[o].sum()) if len(o) and b[o].sum() > 0 else None
    return out


def dif_dias(rows, flag, n=4000, seed=3, k_sin=2):
    """DIF = EV(flag true) - EV(flag false), remuestreando dias; IC90/IC95; sin los 2 mejores dias de la diferencia."""
    pt, ct = _g(rows, lambda r: r[flag])
    pf, cf = _g(rows, lambda r: not r[flag])
    dias = sorted(set(ct) & set(cf))
    usados = set(dias)
    # n_true/n_false SOLO de los dias de la interseccion (los que entran en DIF): un dia con fills de un solo flag no aporta a la diferencia y no debe inflar el n del gate
    nt = sum(1 for r in rows if r[flag] and r["dia"] in usados)
    nf = sum(1 for r in rows if not r[flag] and r["dia"] in usados)
    out = {"n_true": nt, "n_false": nf, "n_true_total": sum(1 for r in rows if r[flag]), "n_false_total": sum(1 for r in rows if not r[flag]), "dias": len(dias), "ev_true": None, "ev_false": None, "dif": None, "ic90": [None, None], "ic95": [None, None], "dif_sin2": None}
    if not dias:
        return out
    a1, b1 = np.array([pt[d] for d in dias]), np.array([ct[d] for d in dias])
    a0, b0 = np.array([pf[d] for d in dias]), np.array([cf[d] for d in dias])
    if b1.sum() <= 0 or b0.sum() <= 0:
        return out
    out["ev_true"], out["ev_false"] = float(a1.sum() / b1.sum()), float(a0.sum() / b0.sum())
    out["dif"] = out["ev_true"] - out["ev_false"]
    if len(dias) >= 2:
        r = np.random.default_rng(seed)
        i = r.integers(0, len(dias), (n, len(dias)))
        e = a1[i].sum(1) / np.maximum(b1[i].sum(1), 1e-9) - a0[i].sum(1) / np.maximum(b0[i].sum(1), 1e-9)
        out["ic90"] = [float(np.quantile(e, .05)), float(np.quantile(e, .95))]
        out["ic95"] = [float(np.quantile(e, .025)), float(np.quantile(e, .975))]
        dd = a1 / np.maximum(b1, 1e-9) - a0 / np.maximum(b0, 1e-9)
        keep = np.argsort(-dd)[k_sin:]
        if len(keep) and b1[keep].sum() > 0 and b0[keep].sum() > 0:
            out["dif_sin2"] = float(a1[keep].sum() / b1[keep].sum() - a0[keep].sum() / b0[keep].sum())
    return out


def veredicto_regla(dias_validos, por_esc, P=None):
    """por_esc = {esc: {'dif': dif_dias(...), 'ev': ev_dias(R_i policy)}} para cons_x y cons_r. -> (veredicto, motivos). Fail-closed: cualquier dato None => no CONFIRMADA."""
    P = P or params()

    def pasa(e):
        d, v = e["dif"], e["ev"]
        if None in (d["dif"], d["ic95"][0], d["dif_sin2"], v["ev"], v["ic95"][0], v["ev_sin2"]):
            return False, "datos_insuficientes"
        if d["n_true"] < P["n_true_min"] or d["n_false"] < P["n_false_min"]:
            return False, f"n_fills true={d['n_true']} false={d['n_false']}"
        if not (d["ic95"][0] > 0 and d["dif_sin2"] > 0):
            return False, "DIF no >0 (IC95 o sin 2 mejores dias)"
        if not (v["ic95"][0] > 0 and v["ev_sin2"] > 0):
            return False, "REDUCE_PERDIDA"
        return True, ""
    ok = {esc: pasa(por_esc[esc]) for esc in P["escenarios_primarios"] if esc in por_esc}
    DIAS_MIN, DIAS_NO_CONF = P["dias_min"], P["dias_no_conf"]
    if dias_validos >= DIAS_MIN and len(ok) == len(P["escenarios_primarios"]) and all(v[0] for v in ok.values()):
        return "CONFIRMADA", []
    dx = por_esc.get("cons_x", {}).get("dif", {})
    if dias_validos >= DIAS_MIN and dx.get("ic90", [None, None])[1] is not None and dx["ic90"][1] <= 0:
        return "REFUTADA", ["IC90(DIF).sup<=0 en cons_x"]
    if dias_validos >= DIAS_MIN and ok.get("cons_x", (0, ""))[1] == "REDUCE_PERDIDA" and ok.get("cons_r", (0, ""))[1] == "REDUCE_PERDIDA":
        return "REDUCE_PERDIDA", ["DIF>0 pero EV de la politica no >0"]
    if dias_validos >= DIAS_NO_CONF:
        return "NO_CONFIRMADA", [v[1] for v in ok.values()]
    return "ACUMULANDO", [f"dias_validos={dias_validos}/{DIAS_MIN}"] + [v[1] for v in ok.values() if v[1]]


# ------------------------------------------------------------------ carga
def dias_en(dirn, prefijo):
    return sorted(p.name[len(prefijo) + 1:-len(".jsonl.gz")] for p in Path(dirn).glob(f"{prefijo}_*.jsonl.gz"))


def cargar(dirn, desde, con_prueba=False):
    mkts, fin, fills, des, smp, decs, fint = {}, {}, [], {}, [], [], []
    for d in dias_en(dirn, "r3_shadow"):
        if d < desde:
            continue
        for r in S.leer_gz_tolerante(Path(dirn) / f"r3_shadow_{d}.jsonl.gz"):
            t = r.get("tipo")
            if r.get("prueba") and not con_prueba:
                continue
            if t == "mkt":
                mkts[r["slug"]] = r
            elif t == "mkt_fin":
                fin[r["slug"]] = r
            elif t == "fill":
                fills.append(r)
            elif t == "smp":
                smp.append(r)
            elif t == "dec":
                decs.append(r)
            elif t == "fin_t":
                fint.append(r)
    for d in dias_en(dirn, "r3_desenlaces"):
        if d < desde:
            continue
        for r in S.leer_gz_tolerante(Path(dirn) / f"r3_desenlaces_{d}.jsonl.gz"):
            if r.get("tipo") == "des":
                des[r["slug"]] = r
    return mkts, fin, fills, des, smp, decs, fint


def dia_de(cierre):
    """Dia UTC de APERTURA del mercado 5m (cierre-300): asi cada dia tiene exactamente 288 mercados por moneda."""
    return datetime.fromtimestamp(cierre - 300, timezone.utc).strftime("%Y-%m-%d")


def cobertura(mkts, fin, des, fills, P=None):
    P = P or params()
    ESPERADOS_DIA, COBERTURA_DIA_MIN = P["esperados_dia"], P["cobertura_dia_min"]
    por_dia = defaultdict(lambda: Counter())
    for s, r in fin.items():
        d = dia_de(r["cierre"])
        c = por_dia[d]
        c["mkt_fin"] += 1
        c["completo"] += bool(r.get("completo"))
        c["huecos"] += bool(r.get("huecos"))
        c["tarde"] += bool(r.get("arranque_tarde"))
        c["con_des"] += s in des and des[s].get("ganador") is not None
        c["sin_cierre_log"] += 0
        c["coin_" + r["coin"]] += 1
    for s, r in mkts.items():
        if s not in fin:
            por_dia[dia_de(r["fin"])]["sin_mkt_fin"] += 1
    sin_des_fill = Counter()
    for f in fills:
        if f["slug"] not in des or des[f["slug"]].get("ganador") is None:
            sin_des_fill[dia_de(int(f["slug"].rsplit("-", 1)[1]) + 300)] += 1
    out = {}
    for d, c in sorted(por_dia.items()):
        out[d] = {"esperados": ESPERADOS_DIA, "recibidos": c["mkt_fin"], "completos": c["completo"], "huecos": c["huecos"], "arranque_tarde": c["tarde"],
                  "con_desenlace": c["con_des"], "sin_mkt_fin": c["sin_mkt_fin"], "fills_sin_desenlace": sin_des_fill.get(d, 0),
                  "cobertura": round(c["completo"] / ESPERADOS_DIA, 3), "valido": c["completo"] / ESPERADOS_DIA >= COBERTURA_DIA_MIN,
                  "por_moneda": {k[5:]: v for k, v in c.items() if k.startswith("coin_")}}
    return out


def tabla_fills(fills, fin, des, validos):
    """Una fila por fill con pnl/coste y flags al pujar. Excluye mercados incompletos, dias no validos y fills sin desenlace (contados aparte)."""
    out, excl = [], Counter()
    for f in fills:
        s = f["slug"]
        mf = fin.get(s)
        if mf is None or not mf.get("completo"):
            excl["mercado_incompleto"] += 1
            continue
        d = dia_de(mf["cierre"])
        if d not in validos:
            excl["dia_no_valido"] += 1
            continue
        g = (des.get(s) or {}).get("ganador")
        if g is None:
            excl["sin_desenlace"] += 1
            continue
        coste = f["acc"] * f["precio"]
        pnl = f["acc"] * (1.0 if f["lado"] == g else 0.0) - coste
        fp = f.get("feat_post") or {}
        out.append({"slug": s, "dia": d, "coin": f["coin"], "pol": f["pol"], "esc": f["esc"], "lado": f["lado"], "acc": f["acc"], "precio": f["precio"], "coste": coste, "pnl": pnl,
                    "R2": bool(fp.get("r2")), "R3": bool(fp.get("r3")), "T1": f.get("T1")})
    return out, excl


def b_real(ledger, smp, decs, des, fin=None, fills=None, fint=None):
    """INFORMATIVO: rellenos de B real segun el flag de R2/R3 en su puja_post (emparejado por slug+lado, fila del brazo shadow mas cercana <= 10 s)."""
    p = Path(ledger)
    if not p.exists():
        return {"disponible": False}
    idx = defaultdict(list)
    for r in smp + decs:
        if r.get("lado") and r.get("r2") is not None and (r["tipo"] == "smp" or (r.get("pol") == "BASE" and r.get("esc") == "cons_x")):
            idx[(r["slug"], r["lado"])].append((r["r"] / 1000.0, r["r2"], r["r3"]))
    first, finb = {}, {}
    for ln in p.open():
        try:
            r = json.loads(ln)
        except ValueError:
            continue
        if not r.get("real") or r.get("escalon") != "B":
            continue
        if r.get("tipo") == "puja_post":
            first.setdefault((r["slug"], r["lado"]), r)
        elif r.get("tipo") == "puja_fin":
            finb[(r["slug"], r["lado"])] = r
    g = defaultdict(lambda: {"pujas": 0, "rellenos": 0, "coste": 0.0, "pnl": 0.0, "sin_desenlace": 0})
    for (slug, lado), f in finb.items():
        t0 = (first.get((slug, lado)) or {}).get("t_dec")
        cand = idx.get((slug, lado), [])
        m = min(cand, key=lambda x: abs(x[0] - t0)) if (cand and t0) else None
        etiqueta = "sin_match_shadow" if (m is None or abs(m[0] - t0) > 10) else ("R3=true" if m[2] else ("R2=true,R3=false" if m[1] else "R2=false"))
        c = g[etiqueta]
        c["pujas"] += 1
        rl = f.get("rellenos") or []
        if not rl:
            continue
        w = (des.get(slug) or {}).get("ganador")
        if w is None:
            c["sin_desenlace"] += 1
            continue
        acc = sum(x["acc"] for x in rl)
        coste = sum(x["acc"] * x["precio"] for x in rl)
        c["rellenos"] += 1
        c["coste"] += coste
        c["pnl"] += acc * (1.0 if lado == w else 0.0) - coste
    # fidelidad del gemelo: ¿el BASE simulado rellena donde B real relleno? (solo mercados completos del shadow; matriz real x simulado)
    acuerdo = {}
    if fin is not None and fills is not None and fint is not None:
        llen = {(f["slug"], f["lado"], f["esc"]) for f in fills if f["pol"] == "BASE"}
        pujo = {(r["slug"], r["lado"]) for r in fint if r["pol"] == "BASE" and r["esc"] == "cons_x" and r["n_post"] > 0}
        for esc in ("cons_x", "cons_r", "opt_x"):
            m = Counter()
            for (slug, lado), f in finb.items():
                if not (fin.get(slug) or {}).get("completo") or (slug, lado) not in pujo:
                    m["sin_comparable"] += 1
                    continue
                m[f"real_{'si' if (f.get('rellenos') or []) else 'no'}__sim_{'si' if (slug, lado, esc) in llen else 'no'}"] += 1
            acuerdo[esc] = dict(m)
    return {"disponible": True, "nota": "informativo, n pequeno, no entra en el veredicto", "acuerdo_relleno_real_vs_simulado": acuerdo,
            "por_flag": {k: {**v, "ev": (v["pnl"] / v["coste"] if v["coste"] > 0 else None)} for k, v in g.items()}}


# ------------------------------------------------------------------ informe
def informe(dirn, desde="2026-10-22", ledger=LEDGER_B, con_prueba=False, prereg=None, hash_file=None):
    P, sha = cargar_prereg(prereg, hash_file)              # PreregInvalido si el preregistro no es el congelado: no se calcula nada
    mkts, fin, fills, des, smp, decs, fint = cargar(dirn, desde, con_prueba)
    cob = cobertura(mkts, fin, des, fills, P)
    validos = {d for d, c in cob.items() if c["valido"]}
    filas, excl = tabla_fills(fills, fin, des, validos)
    res = {"generado": datetime.now(timezone.utc).isoformat(timespec="seconds"), "desde": desde, "dias_validos": len(validos), "dias_con_datos": len(cob), "cobertura": cob,
           "fills_excluidos": dict(excl), "prereg_sha256": sha[:16], "prereg_verificado": True, "reglas": {}}
    base = [r for r in filas if r["pol"] == "BASE"]
    for regla in REGLAS:
        por_esc = {}
        for esc in ("cons_x", "cons_r", "opt_x"):
            b = [r for r in base if r["esc"] == esc]
            pol = [r for r in filas if r["pol"] == regla and r["esc"] == esc]
            kw = {"n": P["bootstrap_n"], "k_sin": P["mejores_dias_excluidos"]}
            por_esc[esc] = {"dif": dif_dias(b, regla, seed=P["seed_dif"], **kw), "ev": ev_dias(pol, seed=P["seed_ev"], **kw), "ev_base": ev_dias(b, seed=P["seed_ev"], **kw)}
        v, motivos = veredicto_regla(len(validos), por_esc, P)
        # retencion de volumen y por moneda (cons_x)
        eur_b = sum(r["coste"] for r in base if r["esc"] == "cons_x")
        eur_r = sum(r["coste"] for r in filas if r["pol"] == regla and r["esc"] == "cons_x")
        por_moneda = {}
        for coin in sorted({r["coin"] for r in filas}):
            por_moneda[coin] = {"ev_politica": ev_dias([r for r in filas if r["pol"] == regla and r["esc"] == "cons_x" and r["coin"] == coin], P["bootstrap_n"], P["seed_ev"], P["mejores_dias_excluidos"]),
                                "dif": dif_dias([r for r in base if r["esc"] == "cons_x" and r["coin"] == coin], regla, P["bootstrap_n"], P["seed_dif"], P["mejores_dias_excluidos"])}
        res["reglas"][regla] = {"veredicto": v, "motivos": motivos, "escenarios": por_esc, "retencion_eur": (eur_r / eur_b if eur_b > 0 else None), "por_moneda": por_moneda}
    # cobertura de decision: share de muestras con flags true y motivos
    n_s = len(smp)
    res["muestreo"] = {"n_smp": n_s, "r2_true": (sum(1 for s in smp if s.get("r2")) / n_s if n_s else None), "r3_true": (sum(1 for s in smp if s.get("r3")) / n_s if n_s else None),
                       "motivos_r3_no": dict(Counter(s.get("m3") for s in smp if not s.get("r3")).most_common(6))}
    res["contra_B_real"] = b_real(ledger, smp, decs, des, fin, fills, fint)
    return res


def texto(res):
    L = [f"R3 shadow | dias validos {res['dias_validos']}/{res['dias_con_datos']} con datos | fills excluidos {res['fills_excluidos']} | prereg {res['prereg_sha256']}"]
    for d, c in res["cobertura"].items():
        L.append(f"  {d}: recibidos {c['recibidos']}/{c['esperados']} completos {c['completos']} (cob {c['cobertura']:.2f}{'' if c['valido'] else ' NO VALIDO'}) huecos {c['huecos']} "
                 f"con_desenlace {c['con_desenlace']} fills_sin_desenlace {c['fills_sin_desenlace']} {c['por_moneda']}")
    for r, x in res["reglas"].items():
        L.append(f"{r}: {x['veredicto']} {x['motivos']} retencion EUR {x['retencion_eur']}")
        for esc, e in x["escenarios"].items():
            d, v, b = e["dif"], e["ev"], e["ev_base"]
            f = lambda z: "NA" if z is None else f"{z:+.3f}"
            L.append(f"   {esc}: DIF {f(d['dif'])} IC90 ({f(d['ic90'][0])},{f(d['ic90'][1])}) IC95 ({f(d['ic95'][0])},{f(d['ic95'][1])}) sin2 {f(d['dif_sin2'])} n_true {d['n_true']} n_false {d['n_false']} (totales {d['n_true_total']}/{d['n_false_total']}) | "
                     f"EV politica {f(v['ev'])} IC95 ({f(v['ic95'][0])},{f(v['ic95'][1])}) sin2 {f(v['ev_sin2'])} n {v['n']} EUR {v['eur']} dias+ {v['dias_pos']}/{v['dias']} | EV BASE {f(b['ev'])} n {b['n']}")
    L.append(f"muestreo {res['muestreo']}")
    L.append(f"contra B real {json.dumps(res['contra_B_real'], default=float)}")
    return "\n".join(L)


def main(argv=None, enviar=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=S.SALIDA_DEFECTO)
    ap.add_argument("--desde", default="2026-10-22")
    ap.add_argument("--ledger", default=LEDGER_B)
    ap.add_argument("--telegram", action="store_true")
    ap.add_argument("--incluir-prueba", action="store_true", help="SOLO humo: cuenta filas marcadas prueba (salida de --minutos)")
    a = ap.parse_args(argv)
    try:
        res = informe(a.dir, a.desde, a.ledger, a.incluir_prueba)
    except PreregInvalido as e:
        print(f"PREREGISTRO INVALIDO (fail-closed, no se evalua el gate): {e}", file=sys.stderr, flush=True)
        return 2
    print(texto(res))
    est_f = Path(a.dir) / "estado_r3_shadow.json"
    prev = json.loads(est_f.read_text()) if est_f.exists() else {}
    prev_firma = prev.get("firma", {})
    firma = {k: v["veredicto"] for k, v in res["reglas"].items()}
    avisar = firma != prev_firma and not (not prev_firma and all(v == "ACUMULANDO" for v in firma.values()))
    firma_guardar, rc = firma, 0
    if avisar:
        firma_guardar = prev_firma                       # el latch solo avanza cuando el aviso SALIO (o no hay nada que avisar)
        if a.telegram:
            msg = "R3 shadow (B selección adversa): veredicto nuevo " + json.dumps(firma) + f" | días válidos {res['dias_validos']} | " + " | ".join(
                f"{k}: DIF {v['escenarios']['cons_x']['dif']['dif']} EV {v['escenarios']['cons_x']['ev']['ev']}" for k, v in res["reglas"].items())
            if enviar is None:
                sys.path.insert(0, "/root/polymarket-research")
                from shadow_digest import enviar_telegram as enviar
            try:
                enviado = bool(enviar(msg))
            except Exception as e:
                print(f"Telegram lanzo {type(e).__name__}: {e}", file=sys.stderr, flush=True)
                enviado = False
            if enviado:
                firma_guardar = firma
            else:
                print("Telegram NO confirmo el envio: el latch no avanza, se reintenta en la proxima corrida", file=sys.stderr, flush=True)
                rc = 1
    tmp = est_f.with_suffix(".tmp")
    tmp.write_text(json.dumps({"firma": firma_guardar, "ultimo": res}, indent=1, default=float))
    tmp.replace(est_f)
    return rc


if __name__ == "__main__":
    sys.exit(main())
