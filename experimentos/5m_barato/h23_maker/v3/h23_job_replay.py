#!/usr/bin/env python3
"""h23_job_replay.py -- JOB LARGO del replay H23 v3 por (fuente, moneda, dia) con el contrato de jobs largos de la mision 5m barato (22-Oct-2026).
Cada unidad (moneda, dia) = un subproceso `h23_sim_v3_monedas.py` (nice 19, ionice 3, RLIMIT_AS 3 GB, uno a la vez). Contrato:
  1. run_manifest.json   job id, hashes de codigo (y de la regla), parametros, entradas (tamano+mtime y sha de las pequenas), fechas/monedas previstas, inicio/fin, estado, comando.
  2. checkpoint durable   = la salida atomica de cada unidad (os.replace) + su fila en `unidades` del manifiesto (atomico). Al reanudar se VALIDA cada salida existente (cabecera, claves unicas, cobertura
                          JSON coherente, errores==0); una salida invalida se aparta (.invalido_<ts>), nunca se borra, y se recalcula; una valida NO se recalcula (sin duplicar filas ni PnL).
  3. resultados idempotentes   clave unica (cierre, brazo, sizing, modo, rep, cola, lat_post, lat_cancel) por fichero; el job comprueba 0 duplicados.
  4. logs con hora   <dir>/job.log (stdout/stderr del job y de cada subproceso).
  5. cobertura   por moneda y dia: esperados (96 cierres), cierres con libro/lado, errores, sin_desenlace, huecos (ledger h23_huecos_ws) -> resumen_parcial.json tras CADA unidad.
  6. informe final   estado COMPLETE | PARTIAL | FAILED | BLOCKED con cobertura exacta, excepciones y comando de reproduccion (informe_final.txt).
Guardas (si no se cumplen, espera hasta --espera-min y luego BLOCKED/PARTIAL; nunca se salta): fuera de 06:00-09:15Z y 22:15-22:30Z, MemAvailable > 2,5 GB, load1 < 16.
Uso: nice -n 19 python3 -I h23_job_replay.py --job ID --fuente registro --monedas ETH,SOL,XRP,DOGE,BNB --dias 2026-10-06:2026-10-21 [--dir DIR]
"""
import argparse
import csv
import glob
import hashlib
import json
import os
import resource
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
COLS = ['coin', 'dia', 'cierre', 'lado', 'm5', 'brazo', 'sizing', 'modo', 'rep', 'cola', 'lat_post', 'lat_cancel', 'n_cotiz', 'need', 'lleno', 'coste', 'n_fill',
        't_rel', 'p_rel', 'gana', 'rebate']
OUT = {"registro": "/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3/", "pares": "/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3_pares/"}
JOBS = "/root/polymarket-research-datalogs/h23_jobs/"
PESADOS = ('extrae_btc.sh', 'extrae_alts.sh', 'extrae_dogebnb.sh', 'h61b_sim.py', 'ms_extract.py', 'run_v3.sh', 'h23_sim_v3.py', 'run_v2_dogebnb.sh', 'h23_sim_v2.py')   # los de vigia_h23_repuja + extractores de alts
CODIGO = ("h23_sim_v3_monedas.py", "h23_sim_v3.py", "h23_regla_v3.py", "h23_pares_lector.py", "h23_job_replay.py", "h23_huecos_ws.py")


def now():
    return time.strftime("%FT%TZ", time.gmtime())


def sha_arch(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()[:16]


def rangos(s):
    if ":" in s:
        a, b = s.split(":")
        d0, d1 = datetime.strptime(a, "%Y-%m-%d"), datetime.strptime(b, "%Y-%m-%d")
        return [(d0 + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((d1 - d0).days + 1)]
    return s.split(",")


def atomico(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=1)
    os.replace(tmp, path)


class Job:
    def __init__(self, a):
        self.a = a
        self.dir = os.path.join(JOBS, a.job) if not a.dir else a.dir
        os.makedirs(self.dir, exist_ok=True)
        self.out = OUT[a.fuente]
        self.logf = open(os.path.join(self.dir, "job.log"), "a", buffering=1)
        self.mf = os.path.join(self.dir, "run_manifest.json")
        self.m = json.load(open(self.mf)) if os.path.exists(self.mf) else {}
        self.coins, self.dias = a.monedas.split(","), rangos(a.dias)

    def log(self, *x):
        print(now(), *x, file=self.logf, flush=True)
        print(now(), *x, flush=True)

    # -- manifiesto -----------------------------------------------------------------------------------------------------
    def manifiesto(self, estado):
        m = self.m
        if "job_id" not in m:
            import h23_regla_v3 as R
            m.update(job_id=self.a.job, inicio=now(), fuente=self.a.fuente, monedas=self.coins, fechas_previstas=self.dias,
                     parametros=dict(reps_ms=[0, 50, 150, 300, 500, 1500], sizings=["2eur", "real"], modos=["acum", "primer"], celda_primaria="BTC/alt, cola base, alta 79, cancel 60, real, primer"),
                     codigo={n: sha_arch(os.path.join(HERE, n)) for n in CODIGO if os.path.exists(os.path.join(HERE, n))}, regla_hash_config=R.hash_config(),
                     comando=f"cd {HERE} && nice -n 19 python3 -I h23_job_replay.py --job {self.a.job} --fuente {self.a.fuente} --monedas {self.a.monedas} --dias {self.a.dias}",
                     entradas="extractos del registro (rows/k) + controles_D.csv del vigia v4 + maker_ms_desenlaces_cache.json", unidades={})
        m["estado"] = estado
        m["actualizado"] = now()
        if estado in ("COMPLETE", "PARTIAL", "FAILED", "BLOCKED"):
            m["fin"] = now()
        atomico(self.mf, m)

    # -- validacion de una salida ---------------------------------------------------------------------------------------------
    def validar(self, coin, D):
        f = os.path.join(self.out, f"v3_{coin}_{D}.csv")
        fc = os.path.join(self.out, f"v3_cobertura_{coin}_{D}.json")
        if not (os.path.exists(f) and os.path.exists(fc)):
            return False, "falta salida o cobertura"
        try:
            cob = json.load(open(fc))
            seen, n = set(), 0
            with open(f, newline="") as fh:
                rd = csv.DictReader(fh)
                if rd.fieldnames != COLS:
                    return False, "cabecera distinta"
                for r in rd:
                    if None in r or None in r.values():
                        return False, f"fila truncada o con columnas de mas (fila {n + 2})"
                    k = (r["cierre"], r["brazo"], r["sizing"], r["modo"], r["rep"], r["cola"], r["lat_post"], r["lat_cancel"])
                    if k in seen:
                        return False, f"clave duplicada {k}"
                    seen.add(k)
                    n += 1
            if cob.get("errores", 1) != 0:
                return False, f"errores={cob.get('errores')}"
            if cob.get("coin") != coin or cob.get("dia") != D:
                return False, "cobertura de otra unidad"
            return True, dict(filas=n, **{k: cob.get(k) for k in ("cierres_grupo", "con_lado", "con_libro", "errores", "sin_desenlace", "cotizados_A", "cotizados_B")})
        except (ValueError, OSError, KeyError) as e:
            return False, f"{type(e).__name__}: {e}"

    def apartar(self, coin, D, motivo):
        for pat in (f"v3_{coin}_{D}.csv", f"v3_cobertura_{coin}_{D}.json"):
            p = os.path.join(self.out, pat)
            if os.path.exists(p):
                os.replace(p, p + ".invalido_" + time.strftime("%Y%m%dT%H%M%S"))
        self.log("APARTADA salida invalida", coin, D, motivo)

    # -- guardas ------------------------------------------------------------------------------------------------------------------
    def guardas(self):
        t = time.gmtime()
        hm = t.tm_hour * 100 + t.tm_min
        if 600 <= hm < 915 or 2215 <= hm < 2230:
            return False, f"franja prohibida {hm:04d}Z"
        mem = [int(l.split()[1]) // 1024 for l in open("/proc/meminfo") if l.startswith("MemAvailable")][0]
        l1 = float(open("/proc/loadavg").read().split()[0])
        if mem < 2500:
            return False, f"MemAvailable {mem} MB < 2500"
        if l1 >= 16:
            return False, f"load1 {l1} >= 16"
        if self.a.respeta_otros:
            yo = os.getpid()
            for p in os.listdir("/proc"):
                if p.isdigit() and int(p) != yo:
                    try:
                        cmd = open(f"/proc/{p}/cmdline", "rb").read().replace(b"\0", b" ").decode(errors="replace")
                    except OSError:
                        continue
                    if any(x in cmd for x in PESADOS) and "h23_job_replay" not in cmd and "h23_sim_v3_monedas" not in cmd and "pgrep" not in cmd:
                        return False, f"otro job pesado en marcha (pid {p}: {cmd[:70]})"
        return True, ""

    def esperar(self, etiqueta):
        t0 = time.time()
        while True:
            ok, why = self.guardas()
            if ok:
                return True
            if time.time() - t0 > self.a.espera_min * 60:
                self.log("BLOCKED", etiqueta, why)
                return False
            time.sleep(30)

    # -- ejecucion ---------------------------------------------------------------------------------------------------------------
    def unidad(self, coin, D):
        ok, det = self.validar(coin, D)
        if ok:
            return "ya_valida", det
        if os.path.exists(os.path.join(self.out, f"v3_{coin}_{D}.csv")):
            self.apartar(coin, D, det)
        if not self.esperar(f"{coin} {D}"):
            return "bloqueada", "guardas"

        def lim():
            resource.setrlimit(resource.RLIMIT_AS, (3_000_000_000, 3_000_000_000))
            os.nice(19)
        cmd = ["ionice", "-c3", sys.executable, "-I", os.path.join(HERE, "h23_sim_v3_monedas.py"), self.a.fuente, coin, D]
        t0 = time.time()
        p = subprocess.run(cmd, preexec_fn=lim, stdout=self.logf, stderr=subprocess.STDOUT, timeout=self.a.timeout_min * 60)
        ok, det = self.validar(coin, D)
        if p.returncode != 0 or not ok:
            self.log("FALLA", coin, D, p.returncode, det)
            return "fallida", f"rc={p.returncode} {det}"
        return "calculada", dict(det, segundos=round(time.time() - t0, 1))

    def resumen_parcial(self):
        try:
            import h23_huecos_ws as H
            led = H.cargar()
        except Exception:
            led = {}
        res = {}
        for c in self.coins:
            for D in self.dias:
                u = self.m["unidades"].get(f"{c}|{D}")
                if not u:
                    continue
                d = dict(u)
                if led and isinstance(u.get("detalle"), dict):
                    cl = H.clasificar(c, D, led)
                    d["cierres_limpios_registro"] = sum(1 for v in cl.values() if v == "limpio")
                    d["cierres_con_hueco_registro"] = sum(1 for v in cl.values() if v != "limpio")
                res[f"{c}|{D}"] = d
        atomico(os.path.join(self.dir, "resumen_parcial.json"), res)

    def correr(self):
        self.log("JOB", self.a.job, "fuente", self.a.fuente, "monedas", self.coins, "dias", self.dias[0], "..", self.dias[-1])
        self.manifiesto("RUNNING")
        estado = "COMPLETE"
        for D in self.dias:
            for c in self.coins:
                try:
                    est, det = self.unidad(c, D)
                except subprocess.TimeoutExpired:
                    est, det = "fallida", "timeout"
                except Exception as e:
                    est, det = "fallida", f"{type(e).__name__}: {e}"
                self.m["unidades"][f"{c}|{D}"] = dict(estado=est, detalle=det, t=now())
                self.log(c, D, est, det)
                self.resumen_parcial()
                self.manifiesto("RUNNING")
                if est == "bloqueada":
                    estado = "BLOCKED"
                    break
                if est == "fallida":
                    estado = "PARTIAL"
            if estado == "BLOCKED":
                break
        us = self.m["unidades"]
        esperadas = len(self.coins) * len(self.dias)
        hechas = sum(1 for u in us.values() if u["estado"] in ("calculada", "ya_valida"))
        if estado == "COMPLETE" and hechas != esperadas:
            estado = "PARTIAL"
        self.manifiesto(estado)
        self.informe(estado, esperadas, hechas)
        return 0 if estado == "COMPLETE" else 2

    def informe(self, estado, esperadas, hechas):
        us = self.m["unidades"]
        L = [f"{estado}  job={self.a.job}  fuente={self.a.fuente}  {now()}", f"unidades esperadas {esperadas}, validas {hechas}, fallidas {sum(u['estado']=='fallida' for u in us.values())}, "
             f"bloqueadas {sum(u['estado']=='bloqueada' for u in us.values())}, pendientes {esperadas - len(us)}", f"reproducir: {self.m.get('comando')}"]
        dup = 0
        for k, u in sorted(us.items()):
            if u["estado"] in ("fallida", "bloqueada"):
                L.append(f"  EXCEPCION {k}: {u['estado']} {u['detalle']}")
        L.append(f"claves duplicadas: {dup} (validadas una a una en cada unidad)")
        open(os.path.join(self.dir, "informe_final.txt"), "w").write("\n".join(L) + "\n")
        self.log("\n".join(L))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--job", required=True)
    ap.add_argument("--fuente", choices=("registro", "pares"), default="registro")
    ap.add_argument("--monedas", default="ETH,SOL,XRP,DOGE,BNB")
    ap.add_argument("--dias", required=True, help="A:B (inclusive) o lista A,B,C")
    ap.add_argument("--dir", default=None)
    ap.add_argument("--espera-min", type=float, default=120.0)
    ap.add_argument("--timeout-min", type=float, default=40.0)
    ap.add_argument("--respeta-otros", action="store_true", help="no arrancar una unidad mientras corra otro job pesado conocido (PESADOS); en cron SIEMPRE")
    a = ap.parse_args()
    return Job(a).correr()


if __name__ == "__main__":
    sys.exit(main())
