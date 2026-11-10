#!/usr/bin/env python3
"""l2_extraer_dia.py DIA [--orig DIR] [--dest DIR] [--pmax 0.40] : extracto diario del plano de B de libro5_ms con lectura
TOLERANTE de gzip truncado (l2_gzcat). Mismo filtro que extraer_libro5_bajos.sh (T y G integras, d de bids <= pmax, B con
bids <= pmax y asks vaciados; 8 columnas). Idempotente (.tmp + os.replace; si el destino existe no hace nada). Solo LEE libro5_ms.
Escribe DEST/libro5_b40_DIA.csv.gz y DEST/libro5_b40_DIA.stats.json (por fichero: lineas leidas, truncado, linea parcial
descartada, filas perdidas ESTIMADAS; y filas de salida). Nunca aborta por un gz truncado; sin ficheros origen = MISSING (exit 3)."""
import argparse, glob, json, os, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l2_gzcat

AWK = r'''
NR==1 {next}
$1=="T" || $1=="G" {print; n++; next}
$1=="d" { if ($4=="B" && $5+0 <= pmax) {print; n++}; next }
$1=="B" { m=split($4,a,";"); s=""; for(i=1;i<=m;i++){ split(a[i],kv,":"); if (kv[1]+0<=pmax) s=(s==""?a[i]:s";"a[i]) }
          print $1,$2,$3,s,"","",$7,$8; n++; next }
END { print n+0 > cnt }
'''


def extraer(dia, orig, dest, pmax="0.40"):
    ficheros = sorted(glob.glob(os.path.join(orig, f"libro5_ms_{dia}_*.csv.gz")))
    if not ficheros:
        return 3, {"dia": dia, "error": "sin ficheros origen (MISSING, no es 0)"}
    os.makedirs(dest, exist_ok=True)
    out = os.path.join(dest, f"libro5_b40_{dia}.csv.gz")
    if os.path.exists(out) and os.path.getsize(out) > 0:
        return 0, {"dia": dia, "ya_existe": out}
    tmp = f"{out}.tmp.{os.getpid()}"
    res = {"dia": dia, "pmax": pmax, "ficheros": []}
    with open(tmp, "wb") as fo:
        gz = subprocess.Popen(["gzip", "-6"], stdin=subprocess.PIPE, stdout=fo)
        for f in ficheros:
            with tempfile.NamedTemporaryFile("r", suffix=".cnt") as cn:
                aw = subprocess.Popen(["awk", "-F,", "-v", f"pmax={pmax}", "-v", "OFS=,", "-v", f"cnt={cn.name}", AWK],
                                      stdin=subprocess.PIPE, stdout=gz.stdin)
                try:
                    st = l2_gzcat.leer_tolerante(f, aw.stdin)
                except BrokenPipeError:
                    st = {"fichero": os.path.basename(f), "error": "tuberia rota"}
                try:
                    aw.stdin.close()
                except BrokenPipeError:
                    pass
                aw.wait()
                st["filas_salida"] = int((cn.read().strip() or 0))
                st["awk_rc"] = aw.returncode
            res["ficheros"].append(st)
        gz.stdin.close()
        rc = gz.wait()
    if rc != 0:
        os.unlink(tmp)
        res["error"] = f"gzip rc={rc}"
        return 4, res
    os.replace(tmp, out)
    res["salida"] = out
    res["salida_bytes"] = os.path.getsize(out)
    for k in ("lineas_ok", "filas_salida", "filas_perdidas_est", "linea_parcial_descartada_bytes"):
        res["total_" + k] = sum((x.get(k) or 0) for x in res["ficheros"])
    res["ficheros_truncados"] = sum(1 for x in res["ficheros"] if x.get("truncado") or x.get("corrupto"))
    sj = os.path.join(dest, f"libro5_b40_{dia}.stats.json")
    with open(sj + ".tmp", "w") as fh:
        json.dump(res, fh, indent=1)
    os.replace(sj + ".tmp", sj)
    return 0, res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dia")
    ap.add_argument("--orig", default="/mnt/HC_Volume_106538179/libro5_ms")
    ap.add_argument("--dest", default="/mnt/HC_Volume_106538179/libro5_b40")
    ap.add_argument("--pmax", default=os.environ.get("PMAX", "0.40"))
    a = ap.parse_args()
    rc, res = extraer(a.dia, a.orig, a.dest, a.pmax)
    print(json.dumps(res))
    return rc


if __name__ == "__main__":
    sys.exit(main())
