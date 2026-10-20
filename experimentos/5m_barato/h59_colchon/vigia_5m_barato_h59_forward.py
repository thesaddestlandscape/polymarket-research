#!/usr/bin/env python3
"""vigia_5m_barato_h59_forward.py -- VIGIA FORWARD CONGELADO de H59 (V4 como TOMADOR con colchon de 2c). SOLO OBSERVACION / DRY-RUN:
no firma, no envia, no importa ejecutores; lee el registro ms crudo y escribe en DL/vigia_5m_barato_h59/. Preregistro: PREREGISTRO.md/json.

REGLA CONGELADA (h59_regla.py; cambiar cualquier cosa = CONFIG['version'] nueva y OOS nuevo; el hash cubre ESTE fichero entero + h59_regla
+ h59_stats + h59_lectura + el hash de V4):
  BTC. Disparo = el de V4 (vigia_5m_barato_forward.py, importado, no replicado). Primera senal de cada cierre. FOK enviada a t0+215 ms con limite
  p_limite(bid15(t0)) + 0,02, acciones = max(5, ceil(2/limite*100)/100), valida contra el TAMANO del nivel 1 vigente a t0+215 (todo o nada).
  Desenlace OFICIAL (gamma closed). EV ponderado por EUR. OOS = disparos con t0 >= CONFIG['congelado_utc'].
  Se registran tambien los colchones 0 / 0,01 / 0,03 / 0,05 como DESCRIPTIVOS (no cuentan para el gate).

Subcomandos: procesar --dia D [--forzar] | informe [--telegram]   (Telegram SOLO con la bandera; no hay cron instalado).
Idempotente: entradas_D.csv.gz se reemplaza completo y de forma atomica (clave unica = cierre); nada se anexa.
Salidas: entradas_D.csv.gz, entradas_D.meta.json, calidad_D.csv, manifiesto.json, runs/run_<ts>.json, informe.json, informe.txt.
"""
import argparse
import bisect  # noqa: F401
import collections
import csv
import glob
import gzip
import hashlib
import json
import os
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import h59_lectura as LEC   # noqa: E402
import h59_regla as R       # noqa: E402
import h59_stats as S       # noqa: E402

V4 = R.V4
DL = LEC.DL
SAL = Path(os.environ.get("H59_SALIDA", str(DL / "vigia_5m_barato_h59")))
CONFIG = {
    "version": 1, "hipotesis": "H59", "moneda": "BTC", "k_principal": R.K_PRINCIPAL, "k_descriptivos": [k for k in R.K_COLCHONES if k != R.K_PRINCIPAL],
    "latencia_ms": R.LAT_TOMADOR_MS, "stake_eur": R.STAKE_EUR, "min_acciones": R.MIN_ACCIONES, "nivel_libro": "nivel1_todo_o_nada",
    "congelado_utc": "2026-10-20T19:05:00+00:00", "v4_hash_config_esperado": "77a75859ae5cf22e",
    "gate": S.GATE, "kill": S.KILL,
    "multiplicidad": "5 colchones probados en descubrimiento (0; 0,01; 0,02; 0,03; 0,05); k=0,02 elegido a posteriori; forward = UNA hipotesis (k=0,02)",
}
CODIGO = [Path(__file__).resolve(), AQUI / "h59_regla.py", AQUI / "h59_stats.py", AQUI / "h59_lectura.py"]
CAMPOS = ["dia", "cierre", "lado", "m5", "n_inst", "ref15", "ref5", "gap_bps", "t0", "resto_s", "ask0", "asz0", "bid15", "margen", "plim",
          "ask_llegada", "asz_llegada", "edad_llegada_ms"]
for _k in R.K_COLCHONES:
    CAMPOS += [f"k{_k:.2f}_{c}" for c in ("lim", "acc_obj", "clase", "acc", "precio")]


def log(*a):
    print(datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ"), *a, flush=True)


def cong_ms():
    return int(datetime.fromisoformat(CONFIG["congelado_utc"]).timestamp() * 1000)


def hash_codigo():
    h = hashlib.sha256(json.dumps(CONFIG, sort_keys=True).encode())
    for a in sorted(CODIGO, key=lambda p: p.name):
        h.update(a.name.encode() + a.read_bytes())
    h.update(V4.hash_config().encode())
    return h.hexdigest()[:16]


def manifiesto(dia=None):
    """Congelacion: si cambia codigo/config/V4 -> SystemExit. Escritura atomica."""
    if V4.hash_config() != CONFIG["v4_hash_config_esperado"]:
        raise SystemExit(f"STOP: V4 cambio ({V4.hash_config()} != {CONFIG['v4_hash_config_esperado']}); la senal de H59 ya no es la congelada")
    SAL.mkdir(parents=True, exist_ok=True)
    hc = hash_codigo()
    fm = SAL / "manifiesto.json"
    m = json.loads(fm.read_text()) if fm.exists() else {"versiones": {}}
    v = m["versiones"].setdefault(str(CONFIG["version"]), {
        "hash": hc, "inicio_utc": datetime.now(timezone.utc).isoformat(), "config": CONFIG,
        "archivos": {a.name: hashlib.sha256(a.read_bytes()).hexdigest()[:16] for a in CODIGO}, "dias": []})
    if v["hash"] != hc:
        raise SystemExit(f"STOP: codigo/config de H59 v{CONFIG['version']} cambio ({v['hash']} -> {hc}). Regla congelada: nueva version y nuevo OOS.")
    if dia and dia not in v["dias"]:
        v["dias"].append(dia)
    tmp = Path(str(fm) + ".tmp")
    tmp.write_text(json.dumps(m, indent=1))
    os.replace(tmp, fm)
    return hc


def evaluar_cierre(C, lado, tok, qs, cal):
    """-> fila (CAMPOS) o None. Estado = ultima fila q con recepcion <= t (sin look-ahead). Primera senal V4 del cierre."""
    sl = "YES" if lado == "Up" else "NO"
    k5, k15 = tok.get(("5min", sl)), tok.get(("15min", sl))
    if not (k5 and k15) or k5 not in qs or k15 not in qs:
        cal["cierre_sin_libro"] += 1
        return None
    r5, b5, a5, bs5, as5 = qs[k5].np()
    r15, b15, a15, _, _ = qs[k15].np()
    t_ini, t_fin = (C - 300) * 1000 + R.REF_CONOCIBLE_MS, (C - R.FIN_MARGEN_S) * 1000
    inst = np.unique(np.concatenate([r5, r15]))
    inst = inst[(inst >= t_ini) & (inst < t_fin)]
    if not len(inst):
        cal["cierre_sin_instantes"] += 1
        return None
    i5, i15 = LEC.i_en(r5, inst), LEC.i_en(r15, inst)
    ok = (i5 >= 0) & (i15 >= 0)
    inst, i5, i15 = inst[ok], i5[ok], i15[ok]
    if not len(inst):
        cal["cierre_sin_instantes"] += 1
        return None
    ask5, bid5, asz5 = a5[i5], b5[i5], as5[i5]
    bid15, ask15 = b15[i15], a15[i15]
    s = R.senal_v4(ask5, bid15, bid5, ask15)
    row = {"n_inst": len(inst)}
    if not s.any():
        return row                                    # cierre sin senal: fila vacia (cuenta como cierre procesado)
    k = int(np.argmax(s))
    t0, a0, bb = int(inst[k]), float(ask5[k]), float(bid15[k])
    te = t0 + R.LAT_TOMADOR_MS
    j = int(LEC.i_en(r5, te))                         # ultima fila con rx <= t0+215 (puede ser la misma del disparo)
    al = float(a5[j]) if j >= 0 else float("nan")
    az = float(as5[j]) if j >= 0 else float("nan")
    edad = (te - int(r5[j])) if j >= 0 else None
    row.update({"t0": t0, "resto_s": round(C - t0 / 1000, 2), "ask0": a0, "asz0": float(asz5[k]), "bid15": bb,
                "margen": V4.margen(bb, a0), "plim": V4.p_limite(bb), "ask_llegada": al, "asz_llegada": az, "edad_llegada_ms": edad})
    for kk, e in R.evaluar_evento(a0, bb, al, az, edad).items():
        row.update({f"k{kk:.2f}_lim": e["lim"], f"k{kk:.2f}_acc_obj": e["acc_obj"], f"k{kk:.2f}_clase": e["clase"],
                    f"k{kk:.2f}_acc": round(e["acc"], 4), f"k{kk:.2f}_precio": e["precio"]})
    return row


def procesar(dia, forzar=False, ahora=None):
    t_ini_run = datetime.now(timezone.utc)
    hc = manifiesto(dia)
    SAL.mkdir(parents=True, exist_ok=True)
    d = date.fromisoformat(dia)
    t_lo = int(datetime(d.year, d.month, d.day, tzinfo=timezone.utc).timestamp())
    t_hi = t_lo + 86400
    ahora = time.time() if ahora is None else ahora
    completo = ahora >= t_hi + 600
    fo, fm = SAL / f"entradas_{dia}.csv.gz", SAL / f"entradas_{dia}.meta.json"
    if fo.exists() and fm.exists() and not forzar:
        m0 = json.loads(fm.read_text())
        if m0.get("completo") and m0.get("hash_codigo") == hc:
            log(f"{dia}: ya procesado COMPLETO (hash {hc}); nada que hacer")
            return m0
    fich = sorted((f for f in glob.glob(str(DL / "maker_ms_*.csv.gz"))
                   if Path(f).name[9:19] in (dia, (d + timedelta(days=1)).isoformat())), key=lambda f: Path(f).stat().st_mtime)
    cal = collections.Counter()
    estado = "COMPLETE" if completo else "PARTIAL"
    if not fich:
        estado = "BLOCKED"
        cal["sin_registro_ms"] += 1
    t0 = time.time()
    meta, idx, qs, _ts = LEC.leer(dia, fich, t_lo, t_hi, cal)
    tw = LEC.twap_refs([(d - timedelta(days=1)).isoformat(), dia])
    filas, esperados = [], 0
    for C in sorted(idx):
        if C % 900:
            continue
        esperados += 1
        tok = idx[C]
        if not all(x in tok for x in (("5min", "YES"), ("5min", "NO"), ("15min", "YES"), ("15min", "NO"))):
            cal["par_incompleto"] += 1
            continue
        r15, r5 = tw.get("BTC", {}).get(C - 900), tw.get("BTC", {}).get(C - 300)
        if r15 is None or r5 is None:
            cal["par_sin_ref"] += 1
            continue
        gap = (r5 / r15 - 1) * 1e4
        if abs(gap) < R.GAP_MIN_BPS:
            cal["par_gap<min"] += 1
            continue
        lado = "Up" if r15 > r5 else "Down"
        row = evaluar_cierre(C, lado, tok, qs, cal)
        if row is None:
            continue
        row.update({"dia": dia, "cierre": C, "lado": lado, "m5": meta[tok[("5min", "YES")]][1], "ref15": r15, "ref5": r5, "gap_bps": round(gap, 3)})
        filas.append(row)
    cierres = [r["cierre"] for r in filas]
    duplicados = len(cierres) - len(set(cierres))
    assert duplicados == 0, "clave cierre duplicada"
    tmp = Path(str(fo) + ".tmp")
    with gzip.open(tmp, "wt", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CAMPOS, restval="")
        w.writeheader()
        w.writerows(filas)
    os.replace(tmp, fo)
    con_senal = sum(1 for r in filas if r.get("t0") not in (None, ""))
    meta_out = {"dia": dia, "completo": bool(completo), "estado": estado, "generado_utc": datetime.now(timezone.utc).isoformat(), "hash_codigo": hc,
                "ficheros_ms": [{"n": Path(f).name, "bytes": Path(f).stat().st_size, "mtime_ns": Path(f).stat().st_mtime_ns} for f in fich],
                "cierres_esperados": 96, "cierres_en_registro": esperados, "cierres_procesados": len(filas), "cierres_con_senal": con_senal,
                "saltados_o_invalidos": dict(cal), "duplicados": duplicados, "segundos": round(time.time() - t0, 1)}
    ftmp = Path(str(fm) + ".tmp")
    ftmp.write_text(json.dumps(meta_out, indent=1))
    os.replace(ftmp, fm)
    with open(SAL / f"calidad_{dia}.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["dia", "incidencia", "n"])
        for k, v in sorted(cal.items()):
            w.writerow([dia, k, v])
    (SAL / "runs").mkdir(exist_ok=True)
    run = {"job_id": f"h59_procesar_{dia}_{t_ini_run:%Y%m%dT%H%M%S}", "codigo_hash": hc, "parametros": {"dia": dia, "forzar": forzar},
           "config": CONFIG, "fechas_previstas": [dia], "inicio_utc": t_ini_run.isoformat(), "fin_utc": datetime.now(timezone.utc).isoformat(),
           "estado": estado, "cobertura": meta_out, "reproducir": f"cd {AQUI} && nice -n 19 ionice -c3 python3 -I vigia_5m_barato_h59_forward.py procesar --dia {dia}"}
    (SAL / "runs" / f"run_{run['job_id']}.json").write_text(json.dumps(run, indent=1, default=str))
    log(f"{dia}: {estado} cierres {len(filas)}/{esperados} (esperados 96) con senal {con_senal} calidad {dict(cal)}")
    return meta_out


# ------------------------------------------------------------------------------------------------ informe
def cargar():
    """-> (filas OOS, dias completos, dias parciales, dias bloqueados). OOS = disparos con t0 >= congelacion."""
    filas, dc, dp, db = [], [], [], []
    for fm in sorted(SAL.glob("entradas_*.meta.json")):
        m = json.loads(fm.read_text())
        fo = SAL / f"entradas_{m['dia']}.csv.gz"
        if not fo.exists():
            continue
        (db if m.get("estado") == "BLOCKED" else dc if m["completo"] else dp).append(m["dia"])
        with gzip.open(fo, "rt") as fh:
            filas += [r for r in csv.DictReader(fh)]
    c = cong_ms()
    oos = [r for r in filas if r.get("t0") not in ("", None) and int(r["t0"]) >= c]
    return oos, dc, dp, db


def desenlaces(m5ids):
    f = os.environ.get("M5B_DES")
    if f:
        return json.load(open(f))
    sys.path.insert(0, str(R.REPO))
    from analisis_maker_cancelacion_binance import desenlaces as d
    return d(sorted(m5ids))


def operaciones(filas, k, des):
    """Operaciones llenas del colchon k con desenlace oficial. -> (ops, contadores). Pendiente != 0."""
    ops, c = [], collections.Counter()
    for r in filas:
        cl = r.get(f"k{k:.2f}_clase")
        c[cl] += 1
        if cl != "llena":
            continue
        o = des.get(r["m5"])
        if o is None:
            c["pendiente_desenlace"] += 1
            continue
        gana = o == ("YES" if r["lado"] == "Up" else "NO")
        acc, pr = float(r[f"k{k:.2f}_acc"]), float(r[f"k{k:.2f}_precio"])
        p, co = R.pnl(acc, pr, gana)
        ops.append({"dia": r["dia"], "cierre": int(r["cierre"]), "pnl": p, "coste": co, "precio": pr, "gana": bool(gana)})
    return ops, dict(c)


def informe(telegram=False):
    manifiesto()
    oos, dc, dp, db = cargar()
    des = desenlaces({r["m5"] for r in oos}) if oos else {}
    kp = R.K_PRINCIPAL
    opp, cp = operaciones(oos, kp, des)
    op0, c0 = operaciones(oos, 0.0, des)
    cierres0 = {o["cierre"] for o in op0}
    incr = [o for o in opp if o["cierre"] not in cierres0]
    rp, r0, ri = S.resumen(opp, f"H59 k={kp:.2f}"), S.resumen(op0, "V4 nivel1 todo-o-nada (k=0)"), S.resumen(incr, "incremental (llena con k=0,02 y no con k=0)")
    v = S.veredicto(rp, ri)
    desc = {f"k{k:.2f}": S.resumen(operaciones(oos, k, des)[0], f"k={k:.2f} DESCRIPTIVO") for k in R.K_COLCHONES if k != kp}
    dias_cal = len(dc)
    sin_desenlace = [r["m5"] for r in oos if r.get(f"k{kp:.2f}_clase") == "llena" and r["m5"] not in des]
    rep = {"hipotesis": "H59", "generado_utc": datetime.now(timezone.utc).isoformat(), "hash_congelacion": hash_codigo(), "config": CONFIG,
           "cobertura": {"dias_completos": dc, "dias_parciales": dp, "dias_bloqueados": db, "disparos_oos": len(oos),
                         "cierres_esperados_dias_completos": 96 * dias_cal, "pendientes_desenlace": len(sin_desenlace),
                         "contadores_k0.02": cp, "contadores_k0": c0},
           "principal": rp, "v4_nivel1_k0": r0, "incremental": ri, "emparejada_k002_menos_k0": S.dif_emparejada(opp, op0, "H59 - V4 nivel1"),
           "descriptivos": desc, "veredicto": v}
    SAL.mkdir(parents=True, exist_ok=True)
    (SAL / "informe.json").write_text(json.dumps(rep, indent=1, default=str))
    L = [f"H59 (V4 tomador, colchon +2c, EXPLORATORY, DRY-RUN) hash {rep['hash_congelacion']} OOS desde {CONFIG['congelado_utc'][:16]}Z",
         f"dias completos {len(dc)} | parciales {len(dp)} | bloqueados {len(db)} | disparos OOS {len(oos)} | pendientes desenlace {len(sin_desenlace)}"]
    for r in (rp, r0, ri):
        L.append(f"{r['brazo']}: n={r['n']}" + ("" if not r["n"] else
                 f" dias={r['dias_con_operacion']} coste={r['coste_eur']} PnL={r['pnl_eur']:+} EVpond={r['ev_pond_por_eur']:+} IC90dias={r['ic90_por_dias']} "
                 f"IC90cierre={r['ic90_por_cierre']} sin2dias={r['ev_sin_2_mejores_dias']} sinTop5%={r['ev_sin_top5pct']}"))
    L.append(f"contadores k=0,02: {cp}")
    L.append(f"VEREDICTO: {v['veredicto']} | kill {v['kill_disparado']} | gate {v['condiciones_gate']}")
    L.append("Nada pasa a dinero sin gate + validador + red-team + /code-review + OK de Javi.")
    txt = "\n".join(L)
    (SAL / "informe.txt").write_text(txt + "\n")
    print(txt)
    if telegram:
        try:
            sys.path.insert(0, str(R.REPO))
            from shadow_digest import enviar_telegram
            enviar_telegram(txt[:3900])
        except Exception as e:
            print(f"(Telegram fallo: {e})")
    return rep


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("procesar")
    p.add_argument("--dia", default=(datetime.now(timezone.utc).date() - timedelta(days=1)).isoformat())
    p.add_argument("--forzar", action="store_true")
    q = sp.add_parser("informe")
    q.add_argument("--telegram", action="store_true")
    a = ap.parse_args()
    procesar(a.dia, a.forzar) if a.cmd == "procesar" else informe(a.telegram)
