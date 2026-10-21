#!/usr/bin/env python3
"""vigia_5m_barato_h59_robusto.py -- ENVOLTORIO DE INTEGRIDAD del vigia H59 congelado (code-review 19:20Z, hallazgos 6-10). SOLO LECTURA / DRY-RUN.

NO sustituye ni edita `vigia_5m_barato_h59_forward.py` (hash de congelacion ea3789bafdc70764 intacto: ese fichero, h59_regla, h59_stats y
h59_lectura siguen byte a byte como en el preregistro). Importa de el la REGLA (evaluar_cierre, CAMPOS, CONFIG, manifiesto, operaciones, hash_codigo) y
solo cambia lo que NO es regla: cuando un dia es COMPLETE, que datos entran al gate y como se protege el estado.

  (6) estado COMPLETE solo si: dia terminado + 96/96 cierres con mercado en el registro + los datos llegan al final del dia (ultima fila q a
      <= 60 s de 24:00Z). Ficheros truncados (kill del proceso al reiniciar `observadores`) y ficheros aun abiertos (mtime < 300 s) se REGISTRAN en
      el meta; un fichero abierto/truncado sin datos hasta el final del dia deja el dia PARTIAL. "Ya procesado" solo si el estado fue COMPLETE, el
      hash coincide y los ficheros ms DEL DIA D conservan (tamano, mtime_ns) y no ha aparecido ninguno nuevo (los de D+1 crecen: no cuentan).
  (7) si faltan mercados (cierres < 96) se relee con los ficheros del dia anterior (donde pudo quedar la linea `k,`); se registra `usado_dia_previo`.
  (8) el gate usa SOLO dias COMPLETE verificados por este envoltorio; un dia procesado por el vigia congelado a pelo (sin `wrapper_sha256`) no entra.
      Con desenlaces oficiales pendientes en las llenas del OOS el veredicto es PENDIENTE_DESENLACES (nunca se evalua el gate con ellas fuera).
  (9) M5B_DL / M5B_PRICES / H59_SALIDA / M5B_DES distintos del estandar quedan escritos en meta, run, informe.json e informe.txt (con sha256 del fichero
      de desenlaces) y el veredicto pasa a NO_VALIDO_ENTORNO_SUSTITUIDO.
  (10) flock exclusivo en SAL/h59.lock alrededor de procesar e informe (manifiesto.json ya se escribe atomico; el flock evita la carrera leer-modificar-escribir).

Uso (el cron debe llamar a ESTE fichero, no al congelado):  procesar --dia D [--forzar] | informe [--telegram]
"""
import argparse
import collections
import csv
import fcntl
import glob
import gzip
import hashlib
import json
import os
import sys
import time
from contextlib import contextmanager
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import h59_lectura as LEC  # noqa: E402
import h59_regla as R  # noqa: E402
import h59_stats as S  # noqa: E402
import vigia_5m_barato_h59_forward as F  # noqa: E402  (CONGELADO: solo se importa)

SAL, DL, CONFIG = F.SAL, F.DL, F.CONFIG
CIERRES_ESPERADOS = 96
ABIERTO_S = 300                       # mtime mas reciente que esto = fichero aun en escritura
COBERTURA_FIN_MS = 60_000             # la ultima fila q debe estar a <= 60 s del fin del dia
DL_STD, PRICES_STD = "/root/polymarket-research-datalogs", "/root/polymarket-research/data/prices"
SAL_STD = str(Path(DL_STD) / "vigia_5m_barato_h59")


def log(*a):
    print(datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ"), *a, flush=True)


def sha_wrapper():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:16]


def entorno_no_estandar():
    """Sustituciones de rutas/datos por variable de entorno (9). {} si todo es estandar."""
    out = {}
    for var, std in (("M5B_DL", DL_STD), ("M5B_PRICES", PRICES_STD), ("H59_SALIDA", SAL_STD)):
        v = os.environ.get(var)
        if v and os.path.abspath(v) != std:
            out[var] = v
    d = os.environ.get("M5B_DES")
    if d:
        try:
            out["M5B_DES"] = {"ruta": d, "sha256": hashlib.sha256(Path(d).read_bytes()).hexdigest()[:16]}
        except OSError:
            out["M5B_DES"] = {"ruta": d, "sha256": None}
    return out


@contextmanager
def bloqueo():
    """(10) flock exclusivo: procesar e informe no se pisan el manifiesto ni las salidas."""
    SAL.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(SAL / "h59.lock"), os.O_RDWR | os.O_CREAT, 0o644)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX)
        yield
    finally:
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)


def _ficheros(dia, con_previo=False):
    d = date.fromisoformat(dia)
    dias = {dia, (d + timedelta(days=1)).isoformat()} | ({(d - timedelta(days=1)).isoformat()} if con_previo else set())
    return sorted((f for f in glob.glob(str(DL / "maker_ms_*.csv.gz")) if Path(f).name[9:19] in dias), key=lambda f: Path(f).stat().st_mtime)


def _calcular(dia, fich, t_lo, t_hi):
    """Cuerpo de `procesar` del vigia congelado (misma logica, mismas funciones de regla) -> filas, cierres con mercado, cal, ultima fila q."""
    d = date.fromisoformat(dia)
    cal = collections.Counter()
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
        row = F.evaluar_cierre(C, lado, tok, qs, cal)
        if row is None:
            continue
        row.update({"dia": dia, "cierre": C, "lado": lado, "m5": meta[tok[("5min", "YES")]][1], "ref15": r15, "ref5": r5, "gap_bps": round(gap, 3)})
        filas.append(row)
    max_rx = max((int(max(c.rx)) for c in qs.values() if len(c.rx)), default=None)
    return filas, esperados, cal, max_rx


def _info_ficheros(fich, cal, ahora):
    out = []
    for f in fich:
        st = Path(f).stat()
        n = Path(f).name
        out.append({"n": n, "bytes": st.st_size, "mtime_ns": st.st_mtime_ns, "truncado": f"fichero_truncado:{n}" in cal,
                    "abierto": (ahora - st.st_mtime) < ABIERTO_S})
    return out


def _ya_valido(m0, hc, dia, fich):
    """(6) 'ya procesado' solo si COMPLETE verificado, mismo codigo y los ficheros del dia D no han cambiado ni ha aparecido otro."""
    if not (m0.get("estado") == "COMPLETE" and m0.get("completo") and m0.get("hash_codigo") == hc and m0.get("wrapper_sha256")):
        return False
    previos = {x["n"]: x for x in m0.get("ficheros_ms", [])}
    actuales = {Path(f).name: Path(f).stat() for f in fich}
    for n, x in previos.items():
        if n[9:19] != dia:
            continue                                   # los de D+1 siguen creciendo despues de t_hi: irrelevantes
        st = actuales.get(n)
        if st is None or st.st_size != x["bytes"] or st.st_mtime_ns != x["mtime_ns"]:
            return False
    return all(n in previos for n in actuales if n[9:19] == dia)


def procesar(dia, forzar=False, ahora=None, cierres_esperados=CIERRES_ESPERADOS):
    t_ini_run = datetime.now(timezone.utc)
    ahora = time.time() if ahora is None else ahora
    d = date.fromisoformat(dia)
    t_lo = int(datetime(d.year, d.month, d.day, tzinfo=timezone.utc).timestamp())
    t_hi = t_lo + 86400
    with bloqueo():
        hc = F.manifiesto(dia)                                               # SystemExit si cambia codigo/config/V4
        fo, fm = SAL / f"entradas_{dia}.csv.gz", SAL / f"entradas_{dia}.meta.json"
        fich = _ficheros(dia)
        if fo.exists() and fm.exists() and not forzar:
            m0 = json.loads(fm.read_text())
            if _ya_valido(m0, hc, dia, fich):
                log(f"{dia}: ya procesado COMPLETE y ficheros sin cambios (hash {hc}); nada que hacer")
                return m0
        t0 = time.time()
        usado_previo = False
        cal = collections.Counter()
        filas, esperados, max_rx = [], 0, None
        if fich:
            filas, esperados, cal, max_rx = _calcular(dia, fich, t_lo, t_hi)
            previo = [f for f in _ficheros(dia, con_previo=True) if f not in fich]
            if esperados < cierres_esperados and previo:                    # (7) la linea `k,` pudo quedar en el fichero del dia anterior
                fich = _ficheros(dia, con_previo=True)
                filas, esperados, cal, max_rx = _calcular(dia, fich, t_lo, t_hi)
                usado_previo = True
        info = _info_ficheros(fich, cal, ahora)
        motivos = []
        if not fich:
            estado = "BLOCKED"
            cal["sin_registro_ms"] += 1
            motivos.append("sin_registro_ms")
        else:
            if ahora < t_hi + 600:
                motivos.append("dia_no_terminado")
            if esperados < cierres_esperados:
                motivos.append(f"cierres_con_mercado_{esperados}_de_{cierres_esperados}")
            if max_rx is None or max_rx < t_hi * 1000 - COBERTURA_FIN_MS:
                motivos.append("datos_no_llegan_al_fin_del_dia")
            estado = "PARTIAL" if motivos else "COMPLETE"
        cierres = [r["cierre"] for r in filas]
        duplicados = len(cierres) - len(set(cierres))
        assert duplicados == 0, "clave cierre duplicada"
        tmp = Path(str(fo) + ".tmp")
        with gzip.open(tmp, "wt", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=F.CAMPOS, restval="")
            w.writeheader()
            w.writerows(filas)
        os.replace(tmp, fo)
        env = entorno_no_estandar()
        meta_out = {"dia": dia, "completo": estado == "COMPLETE", "estado": estado, "motivos": motivos, "generado_utc": datetime.now(timezone.utc).isoformat(),
                    "hash_codigo": hc, "wrapper_sha256": sha_wrapper(), "entorno_no_estandar": env, "usado_dia_previo": usado_previo,
                    "ficheros_ms": info, "ficheros_truncados": [x["n"] for x in info if x["truncado"]], "ficheros_abiertos": [x["n"] for x in info if x["abierto"]],
                    "ultima_fila_q_ms": max_rx, "cierres_esperados": cierres_esperados, "cierres_en_registro": esperados, "cierres_procesados": len(filas),
                    "cierres_con_senal": sum(1 for r in filas if r.get("t0") not in (None, "")), "saltados_o_invalidos": dict(cal),
                    "duplicados": duplicados, "segundos": round(time.time() - t0, 1)}
        ftmp = Path(str(fm) + ".tmp")
        ftmp.write_text(json.dumps(meta_out, indent=1))
        os.replace(ftmp, fm)
        with open(SAL / f"calidad_{dia}.csv", "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["dia", "incidencia", "n"])
            for k, v in sorted(cal.items()):
                w.writerow([dia, k, v])
        (SAL / "runs").mkdir(exist_ok=True)
        run = {"job_id": f"h59_procesar_{dia}_{t_ini_run:%Y%m%dT%H%M%S}", "codigo_hash": hc, "wrapper_sha256": sha_wrapper(), "parametros": {"dia": dia, "forzar": forzar},
               "config": CONFIG, "entorno_no_estandar": env, "fechas_previstas": [dia], "inicio_utc": t_ini_run.isoformat(),
               "fin_utc": datetime.now(timezone.utc).isoformat(), "estado": estado, "cobertura": meta_out,
               "reproducir": f"cd {AQUI} && nice -n 19 ionice -c3 python3 -I vigia_5m_barato_h59_robusto.py procesar --dia {dia}"}
        (SAL / "runs" / f"run_{run['job_id']}.json").write_text(json.dumps(run, indent=1, default=str))
        log(f"{dia}: {estado} {motivos} cierres {len(filas)}/{esperados} con senal {meta_out['cierres_con_senal']} truncados {len(meta_out['ficheros_truncados'])} calidad {dict(cal)}")
        return meta_out


# ------------------------------------------------------------------------------------------------ informe
def cargar():
    """-> (filas OOS de dias COMPLETE verificados, dc, dp, db, sin_verificar, motivos parciales, n disparos OOS en dias no completos)."""
    filas, dc, dp, db, sinv, motivos, filas_np = [], [], [], [], [], {}, []
    for fm in sorted(SAL.glob("entradas_*.meta.json")):
        m = json.loads(fm.read_text())
        fo = SAL / f"entradas_{m['dia']}.csv.gz"
        if not fo.exists():
            continue
        with gzip.open(fo, "rt") as fh:
            rows = list(csv.DictReader(fh))
        if not m.get("wrapper_sha256"):
            sinv.append(m["dia"])                                # procesado por el vigia congelado a pelo: sin las comprobaciones (6)
            filas_np += rows
        elif m.get("estado") == "BLOCKED":
            db.append(m["dia"])
        elif m.get("estado") != "COMPLETE":
            dp.append(m["dia"])
            motivos[m["dia"]] = m.get("motivos")
            filas_np += rows
        else:
            dc.append(m["dia"])
            filas += rows
    c = F.cong_ms()
    oos = lambda rs: [r for r in rs if r.get("t0") not in ("", None) and int(r["t0"]) >= c]
    return oos(filas), dc, dp, db, sinv, motivos, len(oos(filas_np))


def informe(telegram=False, des=None):
    with bloqueo():
        F.manifiesto()
        oos, dc, dp, db, sinv, motivos, n_np = cargar()
        env = entorno_no_estandar()
        if des is None:
            des = F.desenlaces({r["m5"] for r in oos}) if oos else {}
        kp = R.K_PRINCIPAL
        opp, cp = F.operaciones(oos, kp, des)
        op0, c0 = F.operaciones(oos, 0.0, des)
        cierres0 = {o["cierre"] for o in op0}
        incr = [o for o in opp if o["cierre"] not in cierres0]
        rp, r0, ri = S.resumen(opp, f"H59 k={kp:.2f}"), S.resumen(op0, "V4 nivel1 todo-o-nada (k=0)"), S.resumen(incr, "incremental (llena con k=0,02 y no con k=0)")
        v = S.veredicto(rp, ri)
        desc = {f"k{k:.2f}": S.resumen(F.operaciones(oos, k, des)[0], f"k={k:.2f} DESCRIPTIVO") for k in R.K_COLCHONES if k != kp}
        pend = [r["m5"] for r in oos if r.get(f"k{kp:.2f}_clase") == "llena" and r["m5"] not in des]
        pend0 = [r["m5"] for r in oos if r.get("k0.00_clase") == "llena" and r["m5"] not in des]
        if pend or pend0:                                          # (8) con llenas sin desenlace oficial el gate NO se evalua
            v = {**v, "veredicto": "KILL_PROVISIONAL_con_pendientes" if v["kill_disparado"] else "PENDIENTE_DESENLACES", "gate_bloqueado_por_pendientes": True}
        if env:                                                    # (9) datos/rutas sustituidos: el resultado no es el oficial
            v = {**v, "veredicto": "NO_VALIDO_ENTORNO_SUSTITUIDO:" + v["veredicto"]}
        rep = {"hipotesis": "H59", "generado_utc": datetime.now(timezone.utc).isoformat(), "hash_congelacion": F.hash_codigo(), "wrapper_sha256": sha_wrapper(),
               "config": CONFIG, "entorno_no_estandar": env,
               "fuente_desenlaces": ("M5B_DES (sustituido)" if "M5B_DES" in env else "gamma oficial (analisis_maker_cancelacion_binance.desenlaces)"),
               "cobertura": {"dias_completos": dc, "dias_parciales": dp, "motivos_parciales": motivos, "dias_bloqueados": db, "dias_sin_verificar_wrapper": sinv,
                             "disparos_oos_en_dias_no_completos_excluidos_del_gate": n_np, "disparos_oos": len(oos),
                             "cierres_esperados_dias_completos": CIERRES_ESPERADOS * len(dc), "pendientes_desenlace": len(pend), "pendientes_desenlace_k0": len(pend0),
                             "contadores_k0.02": cp, "contadores_k0": c0},
               "principal": rp, "v4_nivel1_k0": r0, "incremental": ri, "emparejada_k002_menos_k0": S.dif_emparejada(opp, op0, "H59 - V4 nivel1"),
               "descriptivos": desc, "veredicto": v}
        SAL.mkdir(parents=True, exist_ok=True)
        (SAL / "informe.json").write_text(json.dumps(rep, indent=1, default=str))
        L = [f"H59 (V4 tomador, colchon +2c, EXPLORATORY, DRY-RUN) hash {rep['hash_congelacion']} OOS desde {CONFIG['congelado_utc'][:16]}Z",
             f"dias COMPLETE {len(dc)} (gate) | parciales {len(dp)} | bloqueados {len(db)} | sin verificar {len(sinv)} | disparos OOS gate {len(oos)} | "
             f"en dias no completos (fuera del gate) {n_np} | pendientes desenlace {len(pend)}"]
        if env:
            L.append(f"AVISO ENTORNO SUSTITUIDO (resultado NO oficial): {json.dumps(env)}")
        for dia, mo in sorted(motivos.items()):
            L.append(f"  parcial {dia}: {mo}")
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
        except Exception as e:                                     # noqa: BLE001
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
