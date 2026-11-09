#!/usr/bin/env python3
"""T3 (FASE 1): bnreg en SOMBRA contra el registro vivo del hijo de `observadores` (red REAL, solo lectura de feed publico, salida en un scratch; NO escribe en datalogs).
Uso: nice -n 19 ionice -c3 .venv/bin/python experimentos/5m_barato/bnreg/tests/t3_sombra.py [segundos=150] [directorio_scratch]
Compara las filas x (T,sym,p,q,m) de bnreg con las del fichero maker_ms_<hoy>_<pid>.csv.gz vivo (el de mtime mas reciente; lectura, tolera final truncado) en la ventana comun.
Criterios del diseno: cobertura >=99,9 % de las x del hijo; mediana (recv_bnreg - recv_hijo) <=5 ms; ids contiguos (faltantes 0 en binance_integridad)."""
import collections
import csv
import glob
import gzip
import os
import signal
import statistics
import subprocess
import sys
import time
from pathlib import Path

BN = Path(__file__).resolve().parent.parent
REPO = BN.parent.parent.parent
DL = Path("/root/polymarket-research-datalogs")
dur = float(sys.argv[1]) if len(sys.argv) > 1 else 150.0
out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(f"/tmp/t3_sombra_{int(time.time())}")
out.mkdir(parents=True, exist_ok=True)
assert str(out.resolve()) != str(DL), "el scratch no puede ser datalogs"
(out / "BNREG_HABILITADO").touch()
env = dict(os.environ, LIBRO_WS_REGISTRO_DIR=str(out))
env.pop("BINANCE_WS_URL", None)
p = subprocess.Popen([sys.executable, "-u", str(BN / "binance_registro_ms.py")], env=env, stdout=open(out / "bnreg.stdout", "ab"), stderr=subprocess.STDOUT, cwd=str(REPO))
t0 = time.time()
time.sleep(dur)
rss_kb = next((int(l.split()[1]) for l in open(f"/proc/{p.pid}/status") if l.startswith("VmRSS")), -1)
p.send_signal(signal.SIGTERM)
p.wait(15)
print(f"bnreg: RSS al final = {rss_kb / 1024:.1f} MB")
time.sleep(8)                                    # el gz del hijo vuelca cada 5 s


def leer(f):
    xs = []
    try:
        with gzip.open(f, "rt", encoding="utf-8") as fh:
            for ln in fh:
                if ln.startswith("x,"):
                    c = ln.rstrip("\n").split(",")
                    if len(c) == 8:
                        xs.append((int(c[1]), c[2], c[3], c[4], c[5], int(c[7])))
    except (EOFError, OSError):
        pass
    return xs


bn = leer(glob.glob(str(out / "maker_ms_*.csv.gz"))[0])
hoy = time.strftime("%Y-%m-%d", time.gmtime())
vivos = sorted(glob.glob(str(DL / f"maker_ms_{hoy}_*.csv.gz")), key=os.path.getmtime)
live_f = vivos[-1]
lv = leer(live_f)
print(f"bnreg: {len(bn)} x ; hijo vivo {Path(live_f).name}: {len(lv)} x ; duracion {dur:.0f} s")
if not bn or not lv:
    print("RESULTADO: INCONCLUSO (sin filas en uno de los lados)")
    sys.exit(2)
r_lo = min(r[5] for r in bn) + 5000
r_hi = max(r[5] for r in bn) - 5000
# ventana comun por hora de recepcion en cada lado (los relojes de recepcion son el mismo reloj de la maquina)
bw = [r for r in bn if r_lo <= r[5] <= r_hi]
lw = [r for r in lv if r_lo <= r[5] <= r_hi]
kb = collections.Counter(r[:5] for r in bw)
kl = collections.Counter(r[:5] for r in lw)
# bordes: una x recibida por un lado a ~r_lo puede caer fuera del otro por unos ms -> comparar por clave sobre la ventana de T interior
T_lo = min(r[0] for r in bw) + 1000
T_hi = max(r[0] for r in bw) - 1000
kb = collections.Counter(r[:5] for r in bn if T_lo <= r[0] <= T_hi)
kl = collections.Counter(r[:5] for r in lv if T_lo <= r[0] <= T_hi)
com = sum((kb & kl).values())
cov_h = com / max(1, sum(kl.values()))      # del hijo, cuanto tiene bnreg
cov_b = com / max(1, sum(kb.values()))
print(f"ventana T [{T_lo}, {T_hi}] ({(T_hi - T_lo) / 1000:.0f} s): bnreg {sum(kb.values())} x, hijo {sum(kl.values())} x, comunes {com}")
print(f"cobertura de bnreg sobre lo del hijo: {cov_h * 100:.3f} %  |  del hijo sobre lo de bnreg: {cov_b * 100:.3f} %")
rb, rl = collections.defaultdict(collections.deque), {}
for r in lv:
    rl.setdefault(r[:5], collections.deque()).append(r[5])
dif = []
for r in bn:
    if T_lo <= r[0] <= T_hi and r[:5] in rl and rl[r[:5]]:
        dif.append(r[5] - rl[r[:5]].popleft())
if dif:
    dif.sort()
    q = lambda f: dif[int(f * (len(dif) - 1))]
    print(f"recv_bnreg - recv_hijo (ms, n={len(dif)}): p5={q(.05)} mediana={statistics.median(dif):.1f} p95={q(.95)}")
ig = list(csv.DictReader(open(glob.glob(str(out / "binance_integridad_*.csv"))[0])))
falt, dup, fo = (sum(int(r[k]) for r in ig) for k in ("faltantes", "dup", "fuera_orden"))
print(f"binance_integridad: filas={len(ig)} faltantes={falt} dup={dup} fuera_de_orden={fo}")
hu = open(glob.glob(str(out / "binance_huecos_*.csv"))[0]).read().strip().splitlines()
print("binance_huecos:", " | ".join(hu[1:]))
# criterio del diseno: bnreg NO mas tarde que el hijo en mas de 5 ms (mediana recv_bnreg - recv_hijo <= +5; negativo = bnreg recibe antes, que es lo deseable)
ok = cov_h >= 0.999 and bool(dif) and statistics.median(dif) <= 5 and falt == 0
print("RESULTADO:", "PASA" if ok else "NO PASA (ver cifras)", f"; scratch={out}")
sys.exit(0 if ok else 1)
