"""Driver de prueba (dev): ejecuta SOLO la corrutina `_binance_registro` del libro_estado_ws PARCHEADO (dev_main/) con un registro falso que vuelca a un fichero.
Entorno: LIBRO_WS_REGISTRO_DIR (scratch), BINANCE_WS_URL (servidor falso). Salida: SALIDA_HIJO (lineas x/b que habria escrito), y logs a stdout."""
import asyncio
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dev_main"))
import libro_estado_ws as m  # noqa: E402


class Falso:
    def __init__(self, ruta):
        self.f = open(ruta, "a", buffering=1, encoding="utf-8")

    def put(self, linea):
        self.f.write(linea)


m._REGISTRO = Falso(os.environ["SALIDA_HIJO"])
asyncio.run(m._binance_registro())
