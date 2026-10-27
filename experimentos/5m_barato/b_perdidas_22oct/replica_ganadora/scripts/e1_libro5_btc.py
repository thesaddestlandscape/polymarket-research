#!/usr/bin/env python3
"""e1: extrae de libro5 (VOL/libro5_ms) los niveles BID (<0,45) de los tokens 5m BTC del día D + operaciones T + huecos G.
Salida compacta: agentes_datos/replica_ganadora/l5_D.csv.gz con filas
  R,recep,tok            reset de bids del token (snapshot B del servidor)
  L,recep,tok,p,size     nivel bid (de snapshot o price_change; tamaño absoluto)
  T,recep,tok,p,side,size  last_trade_price
  G,recep,tok|*          hueco
recep = hora de RECEPCIÓN ms (orden de llegada); se ordena por (pid, seq) implícito = orden de fichero. Solo lectura."""
import sys, gzip, subprocess, glob, os
sys.path.insert(0, "/root/polymarket-research")
from analisis_5m_barato_quien_gana import mapas
OUT = "/mnt/HC_Volume_106538179/agentes_datos/replica_ganadora"
PMAX = 0.45
for d in sys.argv[1:]:
    out = f"{OUT}/l5_{d}.csv.gz"
    if os.path.exists(out): continue
    tok = {t: v for t, v in mapas(d)["5min"].items() if v[0] == "BTC"}
    tf = f"{OUT}/toks_{d}.txt"
    with open(tf, "w") as fh:
        fh.write("\n".join(tok) + "\nG,\n")
    fs = sorted(glob.glob(f"/mnt/HC_Volume_106538179/libro5_ms/libro5_ms_{d}_*.csv.gz"), key=os.path.getmtime)
    n = 0
    with gzip.open(out + ".tmp", "wt", compresslevel=3) as w:
        for f in fs:
            p = subprocess.Popen(f"zcat {f} 2>/dev/null | grep -F -f {tf}", shell=True, stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
            for ln in p.stdout:
                c = ln.rstrip("\n").split(",")
                if len(c) < 8: continue
                k = c[0]
                if k == "d":
                    if c[3] != "B": continue
                    try:
                        pr = float(c[4])
                    except ValueError:
                        continue
                    if pr < PMAX:
                        w.write(f"L,{c[6]},{c[2]},{c[4]},{c[5]}\n"); n += 1
                elif k == "B":
                    if c[2] not in tok: continue
                    w.write(f"R,{c[6]},{c[2]}\n")
                    for lv in c[3].split(";"):
                        if ":" not in lv: continue
                        a, b = lv.split(":")
                        try:
                            if float(a) < PMAX:
                                w.write(f"L,{c[6]},{c[2]},{a},{b}\n"); n += 1
                        except ValueError:
                            pass
                elif k == "T":
                    w.write(f"T,{c[6]},{c[2]},{c[3]},{c[4]},{c[5]}\n")
                elif k == "G":
                    w.write(f"G,{c[6]},{c[2]}\n")
            p.wait()
            print(d, os.path.basename(f), n, flush=True)
    os.rename(out + ".tmp", out)
