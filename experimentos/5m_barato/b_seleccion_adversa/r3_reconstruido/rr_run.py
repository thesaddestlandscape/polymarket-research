#!/usr/bin/env python3
"""rr_run.py -- reconstruye UN dia del brazo R3 (informativo). Idempotente: si existe la salida del dia con manifest COMPLETE y el mismo hash de codigo, no recalcula (--force para rehacer).
Escritura atomica (tmp + os.replace). Salida SOLO bajo /root/polymarket-research-datalogs/r3_reconstruido/ (nunca r3_shadow).
Uso:  nice -n 19 ionice -c3 .venv/bin/python -I rr_run.py --dia 2026-10-27 [--sub puerta] [--solo-cobertura] [--force]
Reproduccion de la puerta: --dia 2026-10-26 --sub puerta ; luego  rr_puerta.py"""
import argparse
import gzip
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rr_core as C  # noqa: E402

JOB = "r3_reconstruido_v1"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:16]


def codigo_hash():
    base = Path("/root/polymarket-research/experimentos/5m_barato/b_seleccion_adversa/r3_shadow")
    return {f: sha(p) for f, p in (("rr_core.py", HERE / "rr_core.py"), ("rr_run.py", HERE / "rr_run.py"), ("r3_regla.py", base / "r3_regla.py"), ("r3_shadow.py", base / "r3_shadow.py"))}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--dia", required=True)
    ap.add_argument("--sub", default="")
    ap.add_argument("--solo-cobertura", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--reusar-cobertura", action="store_true", help="usa cobertura_D.json ya calculada para las mismas entradas (acelera repeticiones)")
    ap.add_argument("--max-mercados", type=int, default=None, help="SOLO humo")
    a = ap.parse_args(argv)
    d = a.dia
    out = C.OUT / a.sub if a.sub else C.OUT
    out.mkdir(parents=True, exist_ok=True)
    fsal, fman, flog = out / f"r3_reconstruido_{d}.jsonl.gz", out / f"run_manifest_{d}.json", out / f"run_{d}.log"
    logf = open(flog, "a")

    def log(m):
        ln = f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} {m}"
        print(ln, flush=True)
        logf.write(ln + "\n")
        logf.flush()
    ch = codigo_hash()
    if fman.exists() and fsal.exists() and not a.force and not a.solo_cobertura and not a.max_mercados:
        man = json.loads(fman.read_text())
        if man.get("status") == "COMPLETE" and man.get("codigo") == ch:
            log(f"{d}: ya COMPLETE con el mismo codigo; no se recalcula (idempotente)")
            return 0
    t0 = time.time()
    man = {"job": JOB, "dia": d, "codigo": ch, "parametros": {"DELTA_CREA_S": C.DELTA_CREA_S, "TICK_MS": C.TICK_MS, "PRE_S": C.R.PRE_S, "VERSION_NUCLEO": C.R.VERSION},
           "entradas": {p.name: {"bytes": p.stat().st_size, "mtime": int(p.stat().st_mtime)} for p in C.ficheros_l5(d)}, "inicio": datetime.now(timezone.utc).isoformat(),
           "status": "RUNNING", "fuente": "reconstruido", "informativo": True}
    log(f"{d}: inicio {JOB} sub='{a.sub}' ficheros_libro5={list(man['entradas'])}")
    mapa, conf = C.mapa_tokens(d)
    mercs, faltan = C.mercados_dia(d, mapa)
    log(f"mapa tokens: conflictos={conf} mercados={len(mercs)} sin_mapa={len(faltan)}")
    fcob = out / f"cobertura_{d}.json"
    if a.reusar_cobertura and fcob.exists():
        cob = json.loads(fcob.read_text())
        stc = {}
        for v in cob.values():
            stc[v] = stc.get(v, 0) + 1
        log("cobertura reutilizada de " + str(fcob))
    else:
        cob, stc = C.cobertura(d, mercs, log)
    cob.update({s: "sin_mapa_tokens" for s in faltan})
    man["cobertura"] = {"esperados": 864, "con_mapa": len(mercs), "sin_mapa": len(faltan), "por_motivo": {k: v for k, v in stc.items() if k != "sin_mapa_tokens"}, "ok": stc.get("ok", 0), "frac_ok": round(stc.get("ok", 0) / 864.0, 4)}
    (out / f"cobertura_{d}.json").write_text(json.dumps(cob, separators=(",", ":")))
    if a.solo_cobertura:
        man["status"] = "COBERTURA_SOLO"
        fman.write_text(json.dumps(man, indent=1))
        log(f"{d}: solo cobertura: {man['cobertura']}")
        return 0
    filas = []

    def salida(row):
        row["fuente"] = "reconstruido"
        filas.append(json.dumps(row, separators=(",", ":"), allow_nan=False, default=str))
    try:
        st = C.replay(d, mercs, cob, salida, log, a.max_mercados)
    except Exception as e:
        man.update(status="FAILED", error=f"{type(e).__name__}: {e}", fin=datetime.now(timezone.utc).isoformat())
        fman.write_text(json.dumps(man, indent=1))
        log(f"{d}: FALLO {type(e).__name__}: {e}")
        raise
    tipos = {}
    for ln in filas:
        k = json.loads(ln)["tipo"]
        tipos[k] = tipos.get(k, 0) + 1
    # unicidad de claves k
    ks = [json.loads(ln)["k"] for ln in filas]
    dup = len(ks) - len(set(ks))
    tmp = fsal.with_suffix(".tmp")
    with gzip.open(tmp, "wt") as f:
        f.write("\n".join(filas) + "\n")
    os.replace(tmp, fsal)
    man.update(status="COMPLETE" if not a.max_mercados else "SMOKE", fin=datetime.now(timezone.utc).isoformat(), segundos=round(time.time() - t0, 1), filas=tipos, duplicados_k=dup,
               replay=st, salida=str(fsal), sha_salida=sha(fsal))
    fman.write_text(json.dumps(man, indent=1))
    log(f"{d}: {man['status']} filas={tipos} dup={dup} replay={st} en {man['segundos']} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
