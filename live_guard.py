"""
live_guard.py — Guardián de ventanas temporales y switch manual.

Responde a la pregunta: ¿puede el bot operar en LIVE ahora mismo?

Reglas:
  1. El fichero data/live/LIVE_MODE_ON debe existir (switch manual).
  2. Si es L-V: la hora de Madrid debe estar dentro de alguna ventana del config.
     Si es S-D:
       - fines_de_semana = "ventanas"    → usa ventanas_fin_de_semana
       - fines_de_semana = "solo_manual" → opera sin restricción horaria
       - fines_de_semana = "off"         → no opera en finde
  3. Si la estrategia/subtype no está en la lista de permitidos → no opera.
"""

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

DIR_LIVE   = Path("data/live")
CONFIG_PATH = DIR_LIVE / "config_live.json"
SWITCH_PATH = DIR_LIVE / "LIVE_MODE_ON"


def _cargar_config() -> dict:
    if not CONFIG_PATH.exists():
        return {}
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def ahora_madrid(config: dict) -> datetime:
    offset_h = config.get("utc_offset_verano", 2)
    return datetime.now(timezone.utc) + timedelta(hours=offset_h)


def switch_activo() -> bool:
    return SWITCH_PATH.exists()


def en_ventana_horaria(config: dict | None = None) -> tuple[bool, str]:
    """
    Devuelve (True, nombre_ventana) si ahora está dentro de una ventana permitida.
    Devuelve (False, motivo) si no.
    """
    if config is None:
        config = _cargar_config()
    if not config:
        return False, "config_live.json no encontrado"

    ahora = ahora_madrid(config)
    dia_semana = ahora.weekday()  # 0=lunes … 6=domingo

    if dia_semana >= 5:  # fin de semana
        modo_fds = config.get("fines_de_semana", "solo_manual")
        if modo_fds == "off":
            return False, "fin_de_semana_desactivado"
        if modo_fds == "solo_manual":
            return True, "fin_de_semana_manual"
        # modo "ventanas": usar ventanas_fin_de_semana igual que L-V
        ventanas_fds = config.get("ventanas_fin_de_semana", [])
        if not ventanas_fds:
            return False, "fin_de_semana_sin_ventanas_configuradas"
        hora_actual = ahora.time()
        for v in ventanas_fds:
            try:
                h_ini = datetime.strptime(v["inicio"], "%H:%M").time()
                h_fin = datetime.strptime(v["fin"],    "%H:%M").time()
                if h_ini <= hora_actual <= h_fin:
                    return True, v.get("nombre", "fds_ventana")
            except Exception:
                continue
        proxima = _proxima_ventana(ventanas_fds, hora_actual, dia_semana)
        return False, f"fds_fuera_de_ventana (proxima: {proxima})"

    ventanas = config.get("ventanas_lunes_viernes", [])
    hora_actual = ahora.time()

    for v in ventanas:
        try:
            h_ini = datetime.strptime(v["inicio"], "%H:%M").time()
            h_fin = datetime.strptime(v["fin"],    "%H:%M").time()
            if h_ini <= hora_actual <= h_fin:
                return True, v.get("nombre", "ventana")
        except Exception:
            continue

    proxima = _proxima_ventana(ventanas, hora_actual, dia_semana)
    return False, f"fuera_de_ventana (proxima: {proxima})"


def _proxima_ventana(ventanas: list, hora_actual, dia_semana: int) -> str:
    from datetime import time as dtime
    candidatas = []
    for v in ventanas:
        try:
            h_ini = datetime.strptime(v["inicio"], "%H:%M").time()
            if h_ini > hora_actual:
                candidatas.append(v["inicio"])
        except Exception:
            pass
    if candidatas:
        return f"hoy {min(candidatas)}"
    dias = ["lun","mar","mié","jue","vie","sáb","dom"]
    prox = dias[(dia_semana + 1) % 7]
    return f"{prox} {ventanas[0]['inicio']}" if ventanas else "indefinida"


def estrategia_permitida(strategy: str, subtype: str, config: dict | None = None) -> bool:
    if config is None:
        config = _cargar_config()
    estrategias_ok = config.get("estrategias_permitidas_live", [])
    subtypes_ok    = config.get("subtypes_permitidos_live", [])
    if strategy not in estrategias_ok:
        return False
    if subtypes_ok and subtype not in subtypes_ok:
        return False
    return True


def puede_operar_live(strategy: str = "", subtype: str = "") -> tuple[bool, str]:
    """
    Comprobación completa: switch + ventana + estrategia permitida.
    Devuelve (True, motivo) o (False, motivo).
    """
    if not switch_activo():
        return False, "switch_OFF (toca: touch data/live/LIVE_MODE_ON)"

    config = _cargar_config()
    en_v, motivo_v = en_ventana_horaria(config)
    if not en_v:
        return False, motivo_v

    if strategy and not estrategia_permitida(strategy, subtype, config):
        return False, f"{strategy}#{subtype} no está en lista de permitidos"

    return True, motivo_v


def estado_live() -> dict:
    """Resumen legible del estado actual del guardián."""
    config  = _cargar_config()
    sw      = switch_activo()
    en_v, mv = en_ventana_horaria(config)
    ahora   = ahora_madrid(config)
    return {
        "switch":        sw,
        "en_ventana":    en_v,
        "motivo":        mv,
        "hora_madrid":   ahora.strftime("%H:%M"),
        "dia":           ["lun","mar","mié","jue","vie","sáb","dom"][ahora.weekday()],
        "puede_operar":  sw and en_v,
    }


if __name__ == "__main__":
    est = estado_live()
    print(f"Switch live:   {'✅ ON' if est['switch'] else '❌ OFF'}")
    print(f"Hora Madrid:   {est['hora_madrid']} ({est['dia']})")
    print(f"En ventana:    {'✅ SÍ' if est['en_ventana'] else '❌ NO'} — {est['motivo']}")
    print(f"Puede operar:  {'✅ SÍ' if est['puede_operar'] else '❌ NO'}")
