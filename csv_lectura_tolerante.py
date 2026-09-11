"""csv_lectura_tolerante.py — lectura tolerante de CSVs que otro proceso
puede estar escribiendo a la vez.

18-Ago: desde que run_fast_mantenimiento.sh desacopló resolve/postmortem/
resumen de predict/live_trade (antes secuenciales en el mismo ciclo, ahora
procesos independientes), shadow_resolve.py/shadow_postmortem.py/
shadow_resumen.py pueden leer predictions_HOY.csv justo mientras
shadow_predict.py lo está escribiendo -- una fila cortada a mitad de
escritura puede hacer que el parser CSV lance una excepción.

/code-review (mismo día): la primera versión de este fix capturaba
`except Exception` y siempre lo etiquetaba "probable escritura
concurrente", sin distinguir una carrera transitoria real (que se cura
sola en el siguiente ciclo, ~45s) de una corrupción PERMANENTE (disco
lleno, bug real en el escritor, ficheros con encoding roto) -- silenciar
esto último para siempre bajo la etiqueta de "concurrencia" viola Fail
Loud (CLAUDE.md: "surfacear incertidumbre siempre"). Este módulo reintenta
UNA vez tras una pausa breve (una carrera genuina, de una sola fila, se
resuelve en milisegundos -- el escritor ya habrá terminado esa fila); si
el segundo intento también falla, se reporta como error real y visible.

2ª ronda /code-review (mismo día): aun con el mensaje "🔴 ... revisar a
mano", nada lo vigilaba de verdad -- un fichero permanentemente corrupto
se saltaría en silencio para siempre, cada ~45-90s, sin que nadie lo
viera salvo grepeando logs a mano. Con estado persistido en
FALLOS_STATE_PATH: si el MISMO fichero lleva fallando de forma continuada
más de ESCALADA_S, se avisa por Telegram UNA vez (hasta que se recupere)
-- deja de ser "ruido esperado" y pasa a ser una alerta real."""
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, TypeVar

T = TypeVar("T")

FALLOS_STATE_PATH = Path(__file__).resolve().parent / "data/shadow/csv_lectura_tolerante_fallos.json"
ESCALADA_S = 600  # 10min fallando sin interrupción -> corrupción real, avisar


def _cargar_estado() -> dict:
    try:
        return json.loads(FALLOS_STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _guardar_estado(estado: dict) -> None:
    try:
        FALLOS_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
        FALLOS_STATE_PATH.write_text(json.dumps(estado, indent=1), encoding="utf-8")
    except Exception:
        pass  # el propio tracking de fallos nunca debe tumbar al caller


def _registrar_fallo_y_quizas_avisar(path: Path, log_fn: Callable[[str], None]) -> None:
    clave = str(path)
    ahora = datetime.now(timezone.utc)
    estado = _cargar_estado()
    entrada = estado.get(clave)
    if entrada is None:
        estado[clave] = {"primera_vez": ahora.isoformat(), "avisado": False}
        _guardar_estado(estado)
        return
    try:
        primera = datetime.fromisoformat(entrada["primera_vez"])
    except Exception:
        estado[clave] = {"primera_vez": ahora.isoformat(), "avisado": False}
        _guardar_estado(estado)
        return
    edad_s = (ahora - primera).total_seconds()
    if edad_s >= ESCALADA_S and not entrada.get("avisado"):
        log_fn(f"🚨 {path}: fallando de forma CONTINUADA desde hace {edad_s/60:.1f}min "
               f"(>{ESCALADA_S/60:.0f}min) -- ya no es una carrera transitoria, es "
               f"corrupción real. Avisando por Telegram.")
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram(
                f"🚨 *csv_lectura_tolerante*: `{path.name}` lleva fallando "
                f"{edad_s/60:.1f}min sin interrupción -- probable corrupción real "
                f"(no una carrera de escritura concurrente, esas se curan en "
                f"segundos). Revisar a mano."
            )
        except Exception as e:
            log_fn(f"  (no se pudo avisar por Telegram: {e})")
        entrada["avisado"] = True
    estado[clave] = entrada
    _guardar_estado(estado)


def _limpiar_si_exito(path: Path) -> None:
    clave = str(path)
    estado = _cargar_estado()
    if clave in estado:
        del estado[clave]
        _guardar_estado(estado)


def leer_csv_tolerante(path: Path, parse_fn: Callable[[Path], T],
                        log_fn: Callable[[str], None] = print) -> T | None:
    """parse_fn(path) hace la lectura/parseo real y devuelve el resultado
    (o lanza excepción). Reintenta una vez tras 0.5s; si el segundo
    intento también falla, lo reporta como fallo persistente (no una
    carrera) y devuelve None -- el caller decide el valor por defecto
    (lista/dict vacíos, normalmente). Si el MISMO fichero lleva fallando
    sin interrupción más de ESCALADA_S (llamadas sucesivas desde procesos
    distintos, cada ~45-90s), avisa por Telegram una sola vez."""
    try:
        resultado = parse_fn(path)
        _limpiar_si_exito(path)
        return resultado
    except Exception:
        time.sleep(0.5)
        try:
            resultado = parse_fn(path)
            _limpiar_si_exito(path)
            return resultado
        except Exception as e2:
            log_fn(f"🔴 {path}: fallo persistente tras reintento (0.5s) -- "
                   f"probable CORRUPCIÓN REAL, no una carrera transitoria de "
                   f"escritura concurrente -- {type(e2).__name__}: {e2}. "
                   f"Fichero saltado, revisar a mano.")
            _registrar_fallo_y_quizas_avisar(path, log_fn)
            return None
