#!/usr/bin/env python3
"""Muestreo de CPU por script (07-Oct, consolidación de procesos, decisión de Javi). Cada PASO s lee /proc/<pid>/stat
(utime+stime) de todos los procesos y atribuye el delta de CPU al script .py/.sh de su línea de comandos (o al binario).
Procesos que nacen y mueren entre muestras: se cuenta lo que se ve. Salida: CSV por minuto y resumen final ordenado.
Uso: python3 muestreo_cpu_por_script.py <segundos> <salida.csv>"""
import os, re, sys, time, collections
DUR, OUT, PASO = int(sys.argv[1]), sys.argv[2], 5.0
HZ = os.sysconf("SC_CLK_TCK")
def nombre(pid):
    try:
        a = open(f"/proc/{pid}/cmdline", "rb").read().split(b"\0")
        a = [x.decode(errors="replace") for x in a if x]
        for x in a:
            if x.endswith(".py") or x.endswith(".sh"):
                return os.path.basename(x)
        return os.path.basename(a[0]) if a else "?"
    except Exception:
        return None
def cpu(pid):
    try:
        f = open(f"/proc/{pid}/stat").read().rsplit(")", 1)[1].split()
        return (int(f[11]) + int(f[12])) / HZ
    except Exception:
        return None
prev, tot, porm = {}, collections.Counter(), collections.defaultdict(collections.Counter)
fin = time.time() + DUR
while time.time() < fin:
    m = time.strftime("%H:%M", time.gmtime())
    for p in os.listdir("/proc"):
        if not p.isdigit():
            continue
        c = cpu(p)
        if c is None:
            continue
        n = nombre(p)
        if n is None:
            continue
        d = c - prev.get(p, (c if p in prev else 0.0, n))[0] if p in prev else (c if os.path.getmtime(f"/proc/{p}") > time.time() - PASO * 2 else 0.0)
        prev[p] = (c, n)
        if d > 0:
            tot[n] += d
            porm[m][n] += d
    time.sleep(PASO)
with open(OUT, "w") as f:
    f.write("minuto,script,cpu_s\n")
    for m in sorted(porm):
        for n, v in porm[m].most_common():
            f.write(f"{m},{n},{v:.2f}\n")
total = sum(tot.values())
print(f"CPU total {total:.0f} s en {DUR} s ({total / DUR:.2f} núcleos de media)")
for n, v in tot.most_common(40):
    print(f"{n:55} {v:8.1f} s  {v / DUR:5.2f} núcleos  {100 * v / total:5.1f} %")
