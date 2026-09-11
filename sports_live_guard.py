"""sports_live_guard.py — Guardián de switch manual + whitelist para LIVE
en sports. Mismo patrón que live_guard.py (cripto) y weather_live_guard.py
(weather, ya adaptado una vez), SIMPLIFICADO igual que weather: SIN
ventanas horarias — Wallet Mirror dispara cuando una wallet válida opera,
no en franjas de reloj fijas (eventos deportivos no tienen ventanas
horarias fijas como los mercados Up/Down de cripto).

Responde a la pregunta: ¿puede el bot operar en LIVE ahora mismo con esta
categoria#tipo?

Reglas:
  1. El fichero data/sports/LIVE_MODE_ON debe existir (switch manual,
     PROPIO de sports — nunca el mismo fichero que cripto, aunque viven
     en el mismo repo. Un switch compartido apagaría/encendería los dos
     sistemas a la vez por error).
  2. categoria#tipo debe estar en pares_permitidos_live de
     config_live_sports.json (PROPIO, separado de config_live.json de
     cripto). Formato: "CATEGORIA#TIPO" (ej. "CS#SEGUIR") — decisión de
     negocio (Javi aprueba qué combos operan con dinero real), SIN banda
     de precio.

  08-Sep (rediseño, hallazgo real: sports llevaba 5 días sin trades):
  hasta hoy el formato era "CATEGORIA#TIPO#lo:hi" y esta whitelist
  ERA la banda de precio -- comprobada aquí, ANTES de que el gate
  dinámico (sports_wallet_mirror_gate_bucket.py::evaluar(), autoaprendiz,
  regenerado a diario) llegara a mirar nada. Dos problemas reales: (a) la
  banda estática quedaba obsoleta en cuanto el mercado se movía —
  LoL#SEGUIR#0.45:0.50 y LoL#FADE#0.70:0.75 llevaban tiempo sin ningún
  soporte en datos frescos (grid `sin_concluir`, fino sin cobertura o
  directamente `malo_confirmado` en otro precio) y seguían bloqueando
  cualquier match fuera de esa banda exacta; (b) casi ningún match de
  wallet-mirror caía dentro de bandas de 0.05 de ancho, así que la
  mayoría de oportunidades morían aquí sin llegar nunca al gate real.
  Mismo antipatrón que CLAUDE.md prohíbe para cripto ("NO crear tablas
  de zonas hardcodeadas por ejecutor... gate_bucket_propio.py es la
  ÚNICA fuente de verdad, autoaprendiente") — corregido para que sports
  siga el mismo patrón: esta whitelist decide SOLO qué categoria#tipo
  tiene aprobación de negocio para dinero real (igual que
  pares_permitidos_live en cripto lista STRATEGY#SUBTYPE#DIRECTION sin
  precio); el micro-bucket de precio exacto lo decide en exclusiva y en
  caliente sports_wallet_mirror_gate_bucket.py::evaluar() (fail-closed,
  exige "bueno_confirmado"), ya invocado después de este guard en
  sports_wallet_mirror_sniper.py — nunca se dejó de comprobar, solo
  estaba duplicado/vuelto obsoleto por el filtro estático de aquí.
  LoL#SEGUIR y LoL#FADE retirados de la whitelist el mismo día por no
  tener ningún soporte fresco (decisión explícita Javi); se re-añaden en
  cuanto el gate confirme un bucket para ellos — ya no hace falta ni
  banda ni fecha manual, el propio gate lo hará solo.

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


def categorias_tipos_live(config: dict | None = None) -> set[tuple[str, str]]:
    """Todas las (categoria,tipo) en pares_permitidos_live -- 08-Sep,
    extraído aquí (único punto de verdad, mismo motivo que bucket() en
    sports_wallet_mirror_gate_bucket.py) tras encontrarse duplicado en
    vigia_sports_log_growth.py y vigia_sports_slippage_kill_switch.py."""
    if config is None:
        config = _cargar_config()
    out = set()
    for entrada in config.get("pares_permitidos_live", []):
        partes = entrada.split("#")
        if len(partes) != 2:
            continue
        out.add((partes[0], partes[1]))
    return out


def tupla_permitida(categoria: str, tipo: str, config: dict | None = None) -> bool:
    """Whitelist por categoria#tipo exacto (sin precio -- ver docstring
    del módulo, 08-Sep). Fail-closed: lista vacía/ausente, o cualquier
    entrada que no sea EXACTAMENTE "categoria#tipo" -> False.

    /code-review 08-Sep: la v1 aceptaba también el formato viejo
    "CATEGORIA#TIPO#lo:hi" por prefijo, pero como esta función ya no
    recibe precio, cualquier entrada legacy sin migrar habría quedado
    aprobada para TODO precio (justo lo que el string decía impedir) --
    fail-open silencioso, no fail-closed como afirma el docstring.
    config_live_sports.json ya está migrado por completo (verificado
    08-Sep) -- match exacto, sin shim de compatibilidad."""
    if config is None:
        config = _cargar_config()
    objetivo = f"{categoria}#{tipo}"
    return objetivo in config.get("pares_permitidos_live", [])


def puede_operar_live(categoria: str = "", tipo: str = "") -> tuple[bool, str]:
    """Comprobación de negocio: switch + categoria#tipo aprobada. (True,
    motivo) o (False, motivo). NO decide precio -- eso lo hace el gate
    dinámico (sports_wallet_mirror_gate_bucket.py::evaluar()), llamado
    SIEMPRE después de esto por el caller (fail-closed en dos capas
    independientes, ver docstring del módulo)."""
    if not switch_activo():
        return False, "switch_OFF (toca: touch data/sports/LIVE_MODE_ON)"

    config = _cargar_config()
    if categoria:
        if not tupla_permitida(categoria, tipo, config):
            return False, f"{categoria}#{tipo} no está en pares_permitidos_live (sports)"

    return True, "ok"


def estado_live() -> dict:
    """Estado informativo. `switch` es SOLO el switch manual — para saber
    si una señal concreta puede operar, usar siempre puede_operar_live()
    con categoria/tipo (el precio lo decide aparte el gate dinámico,
    sports_wallet_mirror_gate_bucket.py::evaluar()), nunca este campo
    solo (switch ON con whitelist vacía no significa que nada pueda
    ejecutarse)."""
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
