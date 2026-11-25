"""`observadores_fase0.py` DE PRUEBAS (se copia a sb/repo/): arranca el libro_estado_ws REAL del sandbox (padre + hijo lector real por WS publico del CLOB, solo lectura)
con un universo FIJO (UNIVERSO_JSON) y las rutas de registro/libro5/txlog del sandbox (env). Imprime el estado en su log como el real. No es produccion."""
import json, os, sys, time
from pathlib import Path
sys.path.insert(0, os.getcwd())
import libro_estado_ws as L
U = json.load(open(os.environ["UNIVERSO_JSON"]))
toks, claves, meta = U["toks"], U["claves"], {k: tuple(v) for k, v in U["meta"].items()}


def universo_fijo(*a, **k):
    L._UNIVERSO.clear()
    L._UNIVERSO.update({"toks": toks, "claves": claves, "meta": meta})
    return toks


L._tokens_universo = universo_fijo
if hasattr(L, "TOK_CACHE_PATH"):
    L.TOK_CACHE_PATH = Path(os.environ["TOK_CACHE"])
for v in list(vars(L).values()):      # el sandbox usa /tmp (pocos GB libres): libro5 no debe pausarse por el umbral de disco
    if hasattr(v, "MIN_LIBRE_GB"):
        v.MIN_LIBRE_GB = 0.1
L.iniciar(("5min",))
print("[observadores-prueba] hilos arrancados", flush=True)
while True:
    time.sleep(10)
    print(str(L.estado())[:200], flush=True)
