#!/usr/bin/env python3
"""vigia_edge_quirurgico.py -- envoltorio de edge_quirurgico_rolling.py para el planificador
vigias_frecuentes_fase0.py (carril "quirurgico", cada 3h).

Corre el generador en un SUBPROCESO (nice 10): es trabajo numpy pesado (~5-8 min) y en el mismo
proceso competiria por el GIL con el resto de vigias. Devuelve 0/1 (convencion de las tareas de
carril aparte: un fallo se reintenta en 300 s, no a las 3 h). Sin Telegram a proposito: en modo
lectura el resultado se consulta con `edge_quirurgico_rolling.py --resumen`."""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent


def main() -> int:
    r = subprocess.run(["nice", "-n", "10", sys.executable, str(REPO / "edge_quirurgico_rolling.py")],
                       capture_output=True, text=True, timeout=2400, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando edge_quirurgico_rolling.py (rc={r.returncode}): {r.stderr[-1500:]}")
        return 1
    print(r.stdout[-2500:])
    return 0


if __name__ == "__main__":
    sys.exit(main())
