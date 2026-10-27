"""Hijo de los tests de proceso: Exp47 en SECO con un mercado falso a mitad de puja. Imprime LEDGER=<ruta> y READY, y espera señales.
modo 'sleep': duerme (2 SIGTERM -> SystemExit -> atexit) | modo 'tick': vuelca mids cada 0,2 s hasta que lo matan (SIGKILL)."""
import sys, time, os
from pathlib import Path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import test_experimento_maker_h47 as T
import h47_robustez as R
R.INTERVALO_S = 0.2
modo = sys.argv[1]
ex = T.nuevo("hijo_" + modo, real=False)
c = T.ctx_de(ex, "eth", fin_en=100.0)
c.tok, c.hashes, c.fase, c.posteado = "tU", ["seco-1"], "asentando", True
t0 = time.time()
c.lib.mids["tU"] = [(t0 - 1, 0.20), (t0 + 0.2, 0.22)]
c.estado["tU"]["rellenos"] = [{"oid": "seco-1", "acc": 5.0, "precio": 0.18, "t_deteccion": t0 - 0.5, "mid0": 0.2}]
c.estado["tU"]["llenas"] = 5.0
ex._log47({"tipo": "puja_post", "oid": "seco-1", "slug": c.mk["slug"], "coin": "eth", "lado": "YES", "k": 2, "precio": 0.18, "size": 5, "real": False})
_cs0 = ex.cerrar_salida
def _cs():                                   # marca en el ledger CUANDO se invoca cerrar_salida (el test comprueba que va antes de puja_fin)
    ex._log47({"tipo": "cs_marca", "mids_antes": len(list(Path(os.environ["H47R_DIR"]).glob("h47_mids_*")))})
    _cs0()
ex.cerrar_salida = _cs
R.instalar(ex)
print("LEDGER=" + str(T.X.LEDGER), flush=True)
print("SLUG=" + c.mk["slug"], flush=True)
print("READY", flush=True)
if modo == "sleep":
    time.sleep(60)
else:
    while True:
        R.tick(ex, c)
        time.sleep(0.05)
