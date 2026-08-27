"""sports_live_guard.py — Guardián de switch manual + whitelist para LIVE
en sports. Mismo patrón que live_guard.py (cripto) y weather_live_guard.py
(weather, ya adaptado una vez), SIMPLIFICADO igual que weather: SIN
ventanas horarias — Wallet Mirror dispara cuando una wallet válida opera,
no en franjas de reloj fijas (eventos deportivos no tienen ventanas
horarias fijas como los mercados Up/Down de cripto).

Responde a la pregunta: ¿puede el bot operar en LIVE ahora mismo, con
este precio concreto?

Reglas:
  1. El fichero data/sports/LIVE_MODE_ON debe existir (switch manual,
     PROPIO de sports — nunca el mismo fichero que cripto, aunque viven
     en el mismo repo. Un switch compartido apagaría/encendería los dos
     sistemas a la vez por error).
  2. El precio de la señal debe caer DENTRO de un micro-bucket confirmado
     de pares_permitidos_live en config_live_sports.json (PROPIO,
     separado de config_live.json de cripto). Formato exacto de cada
     entrada: "CATEGORIA#TIPO#lo:hi" (ej. "CS#SEGUIR#0.24:0.29") — mismo
     criterio que gate_bucket_propio.py en cripto (CLAUDE.md pt.17):
     NUNCA gatear por categoria#tipo agregado, siempre por el
     micro-bucket de precio exacto que pasó el checklist de promoción —
     otros buckets del mismo categoria#tipo pueden estar sin confirmar o
     directamente ser malos, y deben seguir bloqueados aunque el par
     agregado ya tenga una ventana viva.

⚠️ Separación estricta dentro del mismo repo (CLAUDE.md, patrón ya
establecido por sports_wallet_mirror_sniper.py): lee/escribe SOLO
data/sports/ — nunca data/live/ ni data/shadow/ de cripto.
"""

import json
from pathlib import Path

DIR_SPORTS_LIVE = Path("data/sports")
CONFIG_PATH = DIR_SPORTS_LIVE / "config_live_sports.json"
SWITCH_PATH = DIR_SPORTS_LIVE / "LIVE_MODE_ON"


def _cargar_config() -> dict:
    if not CONFIG_PATH.exists():
        return {}
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def switch_activo() -> bool:
    return SWITCH_PATH.exists()


def _parsear_ventana(entrada: str) -> tuple[str, str, float, float] | None:
    """"CATEGORIA#TIPO#lo:hi" -> (categoria, tipo, lo, hi). None si el
    formato no es válido (fail-closed: una entrada mal escrita en el
    JSON no debe colar un "todo permitido" silencioso)."""
    partes = entrada.split("#")
    if len(partes) != 3:
        return None
    categoria, tipo, ventana = partes
    try:
        lo_str, hi_str = ventana.split(":")
        return categoria, tipo, float(lo_str), float(hi_str)
    except (ValueError, TypeError):
        return None


def tupla_permitida(categoria: str, tipo: str, precio: float, config: dict | None = None) -> bool:
    """Whitelist por MICRO-BUCKET exacto (categoria#tipo#lo:hi), nunca por
    categoria#tipo agregado — ver docstring del módulo. Fail-closed: lista
    vacía/ausente, entradas mal formadas, o precio fuera de toda ventana
    confirmada -> False."""
    if config is None:
        config = _cargar_config()
    pares_ok = config.get("pares_permitidos_live", [])
    for entrada in pares_ok:
        parsed = _parsear_ventana(entrada)
        if parsed is None:
            continue
        cat_ok, tipo_ok, lo, hi = parsed
        if cat_ok == categoria and tipo_ok == tipo and lo <= precio < hi:
            return True
    return False


def puede_operar_live(categoria: str = "", tipo: str = "", precio: float | None = None) -> tuple[bool, str]:
    """Comprobación completa: switch + micro-bucket permitido. (True, motivo)
    o (False, motivo). Si se pasa `categoria` sin `precio`, falla cerrado
    (no se puede evaluar la ventana de precio sin el precio real)."""
    if not switch_activo():
        return False, "switch_OFF (toca: touch data/sports/LIVE_MODE_ON)"

    config = _cargar_config()
    if categoria:
        if precio is None:
            return False, f"{categoria}#{tipo}: falta 'precio' para evaluar el micro-bucket (fail-closed)"
        if not tupla_permitida(categoria, tipo, precio, config):
            return False, f"{categoria}#{tipo} @ precio={precio:.3f} no cae en ningún micro-bucket de pares_permitidos_live (sports)"

    return True, "ok"


def estado_live() -> dict:
    """Estado informativo. `switch` es SOLO el switch manual — para saber
    si una señal concreta puede operar, usar siempre puede_operar_live()
    con categoria/tipo/precio, nunca este campo solo (switch ON con
    whitelist vacía no significa que nada pueda ejecutarse)."""
    config = _cargar_config()
    sw = switch_activo()
    pares = config.get("pares_permitidos_live", [])
    return {
        "switch": sw,
        "pares_permitidos": pares,
        "listo_para_operar_algo": sw and bool(pares),
    }


if __name__ == "__main__":
    est = estado_live()
    print(f"Switch live sports: {'✅ ON' if est['switch'] else '❌ OFF'}")
    print(f"Pares permitidos:   {est['pares_permitidos'] or '(ninguno -- fail-closed, nada puede operar)'}")
    print(f"¿Listo para operar ALGO (switch+whitelist no vacía)?: {'✅ sí' if est['listo_para_operar_algo'] else '❌ no'}")
