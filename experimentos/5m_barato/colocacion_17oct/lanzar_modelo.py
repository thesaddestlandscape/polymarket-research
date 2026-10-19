#!/usr/bin/env python3
"""Lanzador IDEMPOTENTE del modelo de colocación H43 (coloc_modelo.py). Solo lectura sobre los dp_D.npz; no envía órdenes ni toca procesos.

Espera un hueco (hora >= 09:15Z y < 22:15Z, MemAvailable > 2500 MB, load5 < 16) y lanza, UNA a UNA, estas etapas pesadas:
  1) humo   : 2 días DESC + 1 OOS, A_hgb, nrep 3 -> informe_humo.txt (valida la cadena con datos reales y mide RAM)
  2) modelo : DESC 05-10 Oct, OOS 14-16 Oct, 4 configuraciones, nrep 300 -> informe_modelo.txt/.json
Con `ulimit -v` 2 GB, `nice -n 19 ionice -c3`; si sale MemoryError reintenta UNA vez con 4,5 GB (solo si MemAvailable > 5,5 GB).
Si no hay hueco en AVISO_UTC lo anota y sigue esperando hasta LIMITE_UTC (no fuerza): estado final BLOCKED.

Contrato de trabajo largo: run_manifest_modelo.json (job, hash del código, parámetros, hash de las entradas, fechas previstas, etapas, estado),
checkpoint = estado por etapa en el manifest + informe_*.json (la etapa se SALTA si su informe existe, es JSON válido y el manifest guarda el
mismo hash de código+entradas), log con hora (modelo_<job>.log), cobertura por día (decisiones, cobertura de desenlaces, de los meta_D.json).
Estado final: COMPLETE | PARTIAL | FAILED | BLOCKED. Uso:
  nohup python3 lanzar_modelo.py --limite-utc 2026-10-19T14:00 --aviso-utc 2026-10-19T12:15 > /dev/null 2>&1 &
"""
import argparse
import hashlib
import json
import os
import resource
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import coloc_dataset as C  # noqa: E402

OUT = C.OUT
MODELO = AQUI / "coloc_modelo.py"
DESC = [f"2026-10-{d:02d}" for d in range(5, 11)]
OOS = ["2026-10-14", "2026-10-15", "2026-10-16"]
MEM_MIN, LOAD_MAX = 2500.0, 16.0
HM_INI, HM_FIN = 9 * 60 + 15, 22 * 60 + 15
ULIMIT_BASE, ULIMIT_ALTO = 2_000_000_000, 4_500_000_000
SONDEO_S = 300

ETAPAS = [
    {"nombre": "humo", "informe": "informe_humo.txt", "args": ["--desc", "2026-10-09,2026-10-10", "--oos", "2026-10-14", "--configs", "A_hgb", "--nrep", "3"]},
    {"nombre": "modelo", "informe": "informe_modelo.txt", "args": ["--nrep", "300"]},
]


def ahora():
    return datetime.now(timezone.utc)


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def mem_mb():
    for ln in open("/proc/meminfo"):
        if ln.startswith("MemAvailable"):
            return int(ln.split()[1]) / 1024.0
    return 0.0


def load5():
    return float(open("/proc/loadavg").read().split()[1])


def escribe_atomico(ruta, txt):
    tmp = ruta.with_name(ruta.name + f".tmp{os.getpid()}")
    with open(tmp, "w") as fh:
        fh.write(txt)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, ruta)


def hash_trabajo(dias):
    """Código (modelo + dataset + simulador) y entradas (sha del npz de cada día)."""
    ent = {}
    for d in dias:
        m = C.cache_valida(OUT, d)
        ent[d] = None if m is None else {"sha_npz": m["sha_npz"], "decisiones": m["decisiones"], "cobertura_des": m["cobertura_des"]}
    cod = sha(MODELO) + C.sha_codigo()
    return hashlib.sha256((cod + json.dumps(ent, sort_keys=True)).encode()).hexdigest()[:16], ent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--limite-utc", required=True, help="ISO UTC: pasada esta hora sin hueco -> BLOCKED")
    ap.add_argument("--aviso-utc", default="", help="ISO UTC: si aún no se ha lanzado se anota en el log")
    ap.add_argument("--solo-etapa", default="")
    a = ap.parse_args()
    out = Path(a.out)
    limite = datetime.fromisoformat(a.limite_utc).replace(tzinfo=timezone.utc)
    aviso = datetime.fromisoformat(a.aviso_utc).replace(tzinfo=timezone.utc) if a.aviso_utc else None
    job = f"modelo_{ahora():%Y%m%dT%H%M%SZ}"
    logf = out / f"{job}.log"
    mf = out / "run_manifest_modelo.json"

    def log(m):
        ln = f"{ahora():%Y-%m-%d %H:%M:%S}Z {m}"
        print(ln, flush=True)
        with open(logf, "a") as fh:
            fh.write(ln + "\n")

    dias = DESC + OOS
    hsh, ent = hash_trabajo(dias)
    previo = json.loads(mf.read_text()) if mf.exists() else {}
    man = {"job_id": job, "script": str(MODELO), "script_sha256": sha(MODELO), "lanzador_sha256": sha(Path(__file__)), "hash_trabajo": hsh,
           "params": {"desc": DESC, "oos": OOS, "etapas": ETAPAS, "mem_min_mb": MEM_MIN, "load5_max": LOAD_MAX, "ventana_utc_min": [HM_INI, HM_FIN],
                      "ulimit": [ULIMIT_BASE, ULIMIT_ALTO]},
           "entradas": ent, "dias_previstos": dias, "cobertura": {"esperados": len(dias), "validos": sum(1 for v in ent.values() if v),
                                                                    "faltan": [d for d, v in ent.items() if not v]},
           "inicio": ahora().isoformat(), "limite_utc": a.limite_utc, "estado": "EN_CURSO", "etapas_estado": {},
           "reproduccion": f"cd /root/polymarket-research && python3 experimentos/5m_barato/colocacion_17oct/lanzar_modelo.py --limite-utc {a.limite_utc}",
           "pid_lanzador": os.getpid(), "previo": {k: previo.get(k) for k in ("job_id", "estado", "hash_trabajo")}}

    def guarda():
        txt = json.dumps(man, indent=1, default=str)
        escribe_atomico(mf, txt)
        escribe_atomico(out / f"run_manifest_{job}.json", txt)

    guarda()
    log(f"inicio {job} pid {os.getpid()} hash_trabajo {hsh} | entradas válidas {man['cobertura']['validos']}/{len(dias)}")
    if man["cobertura"]["faltan"]:
        man["estado"] = "BLOCKED"
        man["motivo"] = f"faltan cachés válidas: {man['cobertura']['faltan']}"
        man["fin"] = ahora().isoformat()
        guarda()
        log("ESTADO FINAL: BLOCKED " + man["motivo"])
        return 1

    hecho_aviso = False
    errores = 0
    for et in ETAPAS:
        nom = et["nombre"]
        if a.solo_etapa and nom != a.solo_etapa:
            continue
        inf_json = out / et["informe"].replace(".txt", ".json")
        prev = (previo.get("etapas_estado") or {}).get(nom, {})
        if inf_json.exists() and prev.get("estado") == "COMPLETE" and prev.get("hash_trabajo") == hsh:
            try:
                json.loads(inf_json.read_text())
                man["etapas_estado"][nom] = {**prev, "estado": "COMPLETE", "nota": "saltada: informe existente con el mismo hash"}
                log(f"{nom}: informe válido con el mismo hash: se salta")
                guarda()
                continue
            except ValueError:
                log(f"{nom}: informe previo corrupto: se rehace")
        ulim = ULIMIT_BASE
        intento = 0
        while True:
            # ---- espera de hueco
            while True:
                t = ahora()
                hm = t.hour * 60 + t.minute
                ml, ld = mem_mb(), load5()
                ok = HM_INI <= hm < HM_FIN and ml > (MEM_MIN if ulim == ULIMIT_BASE else 5500.0) and ld < LOAD_MAX
                if ok:
                    break
                if t >= limite:
                    man["etapas_estado"][nom] = {"estado": "BLOCKED", "motivo": f"sin hueco antes de {a.limite_utc}", "hash_trabajo": hsh}
                    man["estado"] = "BLOCKED" if not any(v.get("estado") == "COMPLETE" for v in man["etapas_estado"].values()) else "PARTIAL"
                    man["fin"] = ahora().isoformat()
                    guarda()
                    log(f"{nom}: SIN HUECO hasta el límite {a.limite_utc} (MemAvailable {ml:.0f} MB, load5 {ld:.1f}, hm {hm}): BLOCKED, no se fuerza")
                    log(f"ESTADO FINAL: {man['estado']}")
                    return 1
                if aviso and t >= aviso and not hecho_aviso:
                    hecho_aviso = True
                    log(f"AVISO: pasado {a.aviso_utc} sin hueco (MemAvailable {ml:.0f} MB, load5 {ld:.1f}); sigo esperando hasta {a.limite_utc}")
                    man["aviso_sin_hueco"] = ahora().isoformat()
                    guarda()
                time.sleep(SONDEO_S)
            # ---- lanzamiento
            cmd = ["nice", "-n", "19", "ionice", "-c3", sys.executable, str(MODELO), "--out", str(out), "--informe", et["informe"]] + et["args"]
            log(f"{nom}: LANZA ulimit {ulim / 1e9:.1f} GB (MemAvailable {ml:.0f} MB, load5 {ld:.1f}) cmd: {' '.join(cmd)}")
            man["etapas_estado"][nom] = {"estado": "EN_CURSO", "inicio": ahora().isoformat(), "ulimit": ulim, "hash_trabajo": hsh}
            guarda()
            env = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
            cola = []
            t0 = time.time()
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env,
                                 preexec_fn=lambda: resource.setrlimit(resource.RLIMIT_AS, (ulim, ulim)))
            man["etapas_estado"][nom]["pid_hijo"] = p.pid
            guarda()
            for ln in p.stdout:
                ln = ln.rstrip("\n")
                cola.append(ln)
                del cola[:-60]
                log(f"[{nom}] {ln}")
            rc = p.wait()
            seg = round(time.time() - t0, 1)
            if rc == 0 and inf_json.exists():
                man["etapas_estado"][nom] = {"estado": "COMPLETE", "rc": 0, "segundos": seg, "informe": str(out / et["informe"]), "hash_trabajo": hsh,
                                             "ulimit": ulim, "sha_informe_json": sha(inf_json)}
                guarda()
                log(f"{nom}: COMPLETE en {seg} s -> {out / et['informe']}")
                break
            mem_err = any("MemoryError" in x for x in cola)
            log(f"{nom}: rc={rc} en {seg} s (MemoryError={mem_err})")
            if mem_err and ulim == ULIMIT_BASE and intento == 0:
                ulim, intento = ULIMIT_ALTO, 1
                log(f"{nom}: MemoryError con 2 GB: reintento UNA vez con 4,5 GB cuando MemAvailable > 5500 MB")
                continue
            errores += 1
            man["etapas_estado"][nom] = {"estado": "FAILED", "rc": rc, "segundos": seg, "mem_error": mem_err, "cola": cola[-15:], "hash_trabajo": hsh}
            guarda()
            break
        if man["etapas_estado"][nom]["estado"] == "FAILED":
            break          # si el humo o el modelo fallan no se encadena el siguiente
    est = man["etapas_estado"]
    todas = all(est.get(e["nombre"], {}).get("estado") == "COMPLETE" for e in ETAPAS if not a.solo_etapa or e["nombre"] == a.solo_etapa)
    man["estado"] = "COMPLETE" if todas else ("FAILED" if errores and not any(v.get("estado") == "COMPLETE" for v in est.values()) else "PARTIAL" if errores else "BLOCKED")
    man["fin"] = ahora().isoformat()
    guarda()
    log(f"ESTADO FINAL: {man['estado']} | etapas {json.dumps({k: v.get('estado') for k, v in est.items()})}")
    return 0 if man["estado"] == "COMPLETE" else 1


if __name__ == "__main__":
    sys.exit(main())
