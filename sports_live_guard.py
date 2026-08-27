"""sports_live_guard.py — Guardián de switch manual + whitelist para LIVE
en sports. Mismo patrón que live_guard.py (cripto) y weather_live_guard.py
(weather, ya adaptado una vez), SIMPLIFICADO igual que weather: SIN
ventanas horarias — Wallet Mirror dispara cuando una wallet válida opera,
no en franjas de reloj fijas (eventos deportivos no tienen ventanas
horarias fijas como los mercados Up/Down de cripto).

Responde a la pregunta: ¿puede el bot operar en LIVE ahora mismo?

Reglas:
  1. El fichero data/sports/LIVE_MODE_ON debe existir (switch manual,
     PROPIO de sports — nunca el mismo fichero que cripto, aunque viven
     en el mismo repo. Un switch compartido apagaría/encendería los dos
     sistemas a la vez por error).
  2. La tupla (categoria#tipo#bucket) debe estar en pares_permitidos_live
     de config_live_sports.json (PROPIO, separado de config_live.json
     de cripto).

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


def tupla_permitida(categoria: str, tipo: str, config: dict | None = None) -> bool:
    """Whitelist por tupla exacta categoria#tipo (mismo patrón fail-closed
    que cripto/weather: lista vacía o ausente -> False, nunca por defecto
    permitido)."""
    if config is None:
        config = _cargar_config()
    pares_ok = config.get("pares_permitidos_live", [])
    return f"{categoria}#{tipo}" in pares_ok


def puede_operar_live(categoria: str = "", tipo: str = "") -> tuple[bool, str]:
    """Comprobación completa: switch + tupla permitida. (True, motivo) o
    (False, motivo)."""
    if not switch_activo():
        return False, "switch_OFF (toca: touch data/sports/LIVE_MODE_ON)"

    config = _cargar_config()
    if categoria and not tupla_permitida(categoria, tipo, config):
        return False, f"{categoria}#{tipo} no está en pares_permitidos_live (sports)"

    return True, "ok"


def estado_live() -> dict:
    config = _cargar_config()
    sw = switch_activo()
    return {
        "switch": sw,
        "pares_permitidos": config.get("pares_permitidos_live", []),
        "puede_operar": sw,
    }


if __name__ == "__main__":
    est = estado_live()
    print(f"Switch live sports: {'✅ ON' if est['switch'] else '❌ OFF'}")
    print(f"Pares permitidos:   {est['pares_permitidos'] or '(ninguno -- fail-closed, nada puede operar)'}")
