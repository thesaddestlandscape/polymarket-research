#!/usr/bin/env python3
"""csv_incremental.py -- lector INCREMENTAL de CSV que solo crecen (append).

Origen (24-Sep, load5 13-18 en 4 cores): varios procesos persistentes
releían ENTEROS CSV de ~500MB que crecen todo el día (data/markets/HOY.csv,
predictions_HOY.csv) cada vez que caducaba una caché por TTL/mtime. Este
lector recuerda el offset en bytes y solo parsea lo añadido.

Garantías (mismas que los arreglos ya revisados en fetch_libro_ambos_lados.
_universo_activo y gbm_confluencia._index_actualizado, /code-review 24-Sep):
  - Lectura por bloques (RAM acotada también en la lectura en frío).
  - Corte SOLO por b"\\n" (splitlines() cortaría por U+2028, \\x0b...; csv.writer
    no los entrecomilla). Requiere CSV sin saltos de línea dentro de campos.
  - Una línea final incompleta se deja para la siguiente llamada.
  - Reset completo si cambia la ruta, el inodo o el fichero encoge.
  - El offset solo avanza si TODO el tramo se procesó sin excepción: si el
    callback lanza, se reintenta entero (sin perder filas en silencio).
  - Thread-safe: un cerrojo por instancia (por_fila corre DENTRO del cerrojo).
  - por_fila DEBE ser idempotente (p.ej. mapa[k] = v): si falla a mitad de un
    tramo, las filas ya aplicadas se vuelven a aplicar en el reintento.

Uso:
    lector = LectorIncremental()
    def fila(cab_idx, vals): ...            # cab_idx = {columna: índice}
    lector.leer(path, fila, al_reset=lambda: estado.clear())
"""
import csv
import threading
from pathlib import Path

BLOQUE_BYTES = 8 * 1024 * 1024


class LectorIncremental:
    def __init__(self, bloque_bytes: int = BLOQUE_BYTES):
        self._lock = threading.Lock()
        self._bloque = bloque_bytes
        self._path = None
        self._ino = None
        self._offset = 0
        self._cab = None

    def leer(self, path, por_fila, al_reset=None) -> bool:
        """Procesa las líneas nuevas llamando por_fila(cab_idx, vals).
        Devuelve True si hubo reset (el llamador debe haber vaciado su estado
        en al_reset, que se invoca ANTES de procesar). Propaga OSError si el
        fichero no existe y cualquier excepción de por_fila."""
        path = Path(path)
        with self._lock:
            st = path.stat()
            reset = (self._path != path or self._ino != st.st_ino
                     or st.st_size < self._offset)
            if reset:
                self._path, self._ino, self._offset, self._cab = path, st.st_ino, 0, None
                if al_reset:
                    al_reset()
            if st.st_size == self._offset:
                return reset
            cab = self._cab
            consumido = 0
            resto = b""
            with open(path, "rb") as f:
                f.seek(self._offset)
                pendiente = st.st_size - self._offset
                while pendiente > 0:
                    trozo = f.read(min(self._bloque, pendiente))
                    if not trozo:
                        break
                    pendiente -= len(trozo)
                    partes = (resto + trozo).split(b"\n")
                    resto = partes.pop()
                    consumido += sum(len(x) + 1 for x in partes)
                    lineas = [x.rstrip(b"\r").decode("utf-8", errors="replace") for x in partes]
                    if cab is None and lineas:
                        cab = {c: i for i, c in enumerate(next(csv.reader([lineas[0]])))}
                        lineas = lineas[1:]
                    if cab is None:
                        continue
                    for vals in csv.reader(lineas):
                        por_fila(cab, vals)
            self._cab = cab
            self._offset += consumido
            return reset
