"""gate_confirmacion_historial.py — 01-Sep, petición explícita Javi.

Hasta hoy, los 6 generadores de gates por micro-bucket/ventana
(`analisis_gate_bucket_propio_28jul.py`, `analisis_gate_bucket_fino.py`,
`analisis_wallet_mirror_gate_bucket_10ago.py`,
`analisis_wallet_mirror_gate_bucket_fino_25ago.py`,
`analisis_sports_wallet_mirror_gate_bucket_26ago.py`,
`analisis_sports_wallet_mirror_gate_bucket_fino.py`) implementaban, cada
uno por su cuenta (duplicado, señalado por /code-review el mismo día:
"missing one causes silent divergence"), el mismo guard de estabilidad:
"bueno_confirmado" solo se promueve si la corrida INMEDIATAMENTE ANTERIOR
también dio "bueno_confirmado" para esa misma clave -- un solo día de
mala racha (ruido, no falta de edge real) reiniciaba el progreso a cero,
exigiendo 2 días buenos consecutivos de nuevo desde ahí.

Fix (petición explícita Javi, "un día de mala racha no puede entorpecer
esto... en toda la whitelist y las candidatas evaluacion live"): en vez
de comparar solo contra el día inmediatamente anterior, mantener un
HISTORIAL rodante de los últimos HISTORIAL_DIAS_VENTANA veredictos crudos
(incluyendo hoy) y exigir que al menos HISTORIAL_DIAS_REQUERIDOS de ellos
sean "bueno_confirmado". Con la config por defecto (2 de 3), tolera
EXACTAMENTE un día flojo intercalado entre dos buenos sin perder el
progreso, pero sigue exigiendo consistencia real (no promueve con un solo
día bueno aislado).

Asimetría deliberada, sin cambios: "malo_confirmado" sigue siendo
INMEDIATO (un solo día malo basta) -- reaccionar rápido a la mala noticia,
exigir consistencia para la buena, mismo criterio de riesgo que ya tenía
el diseño original del 31-Ago.

Uso (mismo patrón en los 6 consumidores):
    historial_previos = cargar_historial_previo(OUT_PATH, clave_bucket=True)  # o False si es {tupla_str: veredicto}
    ...
    veredicto, nuevo_historial = veredicto_con_tolerancia(veredicto_crudo_hoy, historial_previos.get(clave, []))
    info["historial_crudo"] = nuevo_historial
    info["veredicto_crudo_hoy"] = veredicto_crudo_hoy
    info["veredicto"] = veredicto
"""
import json
from datetime import datetime, timezone
from pathlib import Path

HISTORIAL_DIAS_VENTANA = 3      # cuántos días recientes se recuerdan (incluye hoy)
HISTORIAL_DIAS_REQUERIDOS = 2   # cuántos de esos días deben ser bueno_confirmado


def historial_actualizado(historial_previo: list | None, veredicto_hoy: str) -> list:
    """Añade el veredicto de hoy al historial, recortado a los últimos
    HISTORIAL_DIAS_VENTANA (FIFO, el más viejo se descarta)."""
    base = list(historial_previo or [])[-(HISTORIAL_DIAS_VENTANA - 1):]
    base.append(veredicto_hoy)
    return base


def veredicto_con_tolerancia(veredicto_crudo_hoy: str, historial_previo: list | None) -> tuple[str, list]:
    """(veredicto_final, nuevo_historial). malo_confirmado es inmediato
    (asimetría deliberada) Y RESETEA el historial a solo ese día -- /code-
    review 01-Sep encontró que sin este reset, un día malo justo después de
    2 días buenos podía re-confirmar "bueno" al día siguiente con un solo
    día bueno más, arrastrando evidencia de ANTES del aviso (WALLET_MIRROR
    #BTC, dinero real, DRY_RUN=False). Con el reset, reconfirmar tras un
    malo exige HISTORIAL_DIAS_REQUERIDOS días buenos GENUINAMENTE
    posteriores al veto, no antes.

    bueno_confirmado exige HISTORIAL_DIAS_REQUERIDOS de los últimos
    HISTORIAL_DIAS_VENTANA días, incluido hoy."""
    if veredicto_crudo_hoy == "malo_confirmado":
        return "malo_confirmado", [veredicto_crudo_hoy]
    nuevo_historial = historial_actualizado(historial_previo, veredicto_crudo_hoy)
    n_buenos = sum(1 for v in nuevo_historial if v == "bueno_confirmado")
    if n_buenos >= HISTORIAL_DIAS_REQUERIDOS:
        return "bueno_confirmado", nuevo_historial
    return "sin_concluir", nuevo_historial


def veredicto_con_tolerancia_diario(veredicto_crudo_hoy: str, historial_previo: list | None,
                                     fecha_previa: str | None, fecha_hoy: str | None = None
                                     ) -> tuple[str, list, str]:
    """10-Sep, petición explícita Javi (WALLET_MIRROR#BTC#15min sin_concluir->
    bueno_confirmado->sin_concluir en horas, trade real perdedor de por medio
    -- ver idea_walletmirror_gate_bucket_ventana_horaria_diluye_tolerancia_10sep).

    Wrapper de veredicto_con_tolerancia() para generadores con cadencia
    INTRADÍA (p.ej. horaria, wallet_mirror_gate_bucket*.py vía
    vigias_frecuentes_fase0.py cada 3600s) que escriben sobre el MISMO
    fichero de salida varias veces al día. Sin este wrapper, cada corrida
    intradía cuenta como un "día" propio dentro de HISTORIAL_DIAS_VENTANA,
    diluyendo la ventana de tolerancia -- diseñada y documentada como "2 de
    los últimos 3 DÍAS" (ver cabecera del módulo) -- a "2 de las últimas 3
    CORRIDAS" (p.ej. horas si el generador es horario): 24x más débil de lo
    previsto, exactamente lo que pasó (bucket confirmado ~17:42 el 9-Sep,
    revertido antes de las 06:03 del 10-Sep, con un trade real de por medio).

    Colapsa todas las corridas del mismo día UTC en una sola entrada de
    historial (la más reciente del día manda, igual que ya hace cada
    generador con n/pnl_medio/shuffle_p en cada corrida) -- solo empuja una
    entrada NUEVA a la ventana al cruzar medianoche UTC respecto a la
    corrida anterior. Los generadores DIARIOS existentes (gate_bucket_
    propio, sports_wallet_mirror_gate_bucket, weather) no necesitan este
    wrapper -- cada corrida suya YA es un día distinto, fecha_previa!=
    fecha_hoy siempre, coincide con veredicto_con_tolerancia() sin cambio
    de comportamiento; no se han tocado.

    Devuelve (veredicto, nuevo_historial, fecha_hoy) -- el caller debe
    persistir fecha_hoy junto a historial_crudo (mismo campo que ya se
    escribe) para que la próxima corrida sepa si sigue siendo "hoy"."""
    if fecha_hoy is None:
        fecha_hoy = datetime.now(timezone.utc).date().isoformat()
    historial_efectivo = historial_previo
    if fecha_previa == fecha_hoy and historial_previo:
        # Misma fecha UTC que la última corrida registrada -- esta corrida
        # sustituye la entrada de HOY en vez de apilar una corrida más en
        # la ventana (que solo debe crecer al cruzar un día real).
        historial_efectivo = list(historial_previo)[:-1]
    veredicto, nuevo_historial = veredicto_con_tolerancia(veredicto_crudo_hoy, historial_efectivo)
    return veredicto, nuevo_historial, fecha_hoy


def _semilla_desde_formato_antiguo(info: dict) -> list:
    """Migración: entradas escritas ANTES de este fix solo tienen
    veredicto_crudo_hoy (un único día), sin historial_crudo -- se usa como
    semilla de 1 día en vez de perder esa evidencia. SKIP/sin_concluir no
    se registran (no aportan información de si fue "bueno" o "malo")."""
    if info.get("historial_crudo"):
        return list(info["historial_crudo"])
    v = info.get("veredicto_crudo_hoy") or info.get("veredicto")
    return [v] if v in ("bueno_confirmado", "malo_confirmado") else []


def sembrar_no_confirmados(historial_previo: dict, salida: dict) -> None:
    """/code-review 01-Sep, ronda 2: los 3 generadores "_fino" (gate_bucket_
    fino, wallet_mirror_gate_bucket_fino_25ago, sports_wallet_mirror_gate_
    bucket_fino) reimplementaban cada uno su propia versión de este barrido
    -- señalado como duplicación de riesgo (un fix futuro al formato del
    placeholder solo se aplicaría en 1 de los 3 copy-pastes). Centralizado
    aquí: para cualquier clave con historial_crudo previo que NO haya
    quedado ya en `salida` tras el resto del pipeline (BH-FDR, piso
    absoluto, o simplemente sin datos suficientes hoy), escribe un
    placeholder {"veredicto": "sin_concluir", "historial_crudo": hist} --
    NUNCA sobreescribe una entrada ya presente. Muta `salida` in-place."""
    for clave, hist in historial_previo.items():
        if hist and clave not in salida:
            salida[clave] = {"veredicto": "sin_concluir", "historial_crudo": hist}


def cargar_historial_previo(out_path: Path, anidado_por_bucket: bool) -> dict:
    """Lee el fichero de salida de la corrida ANTERIOR (antes de que esta
    corrida lo sobreescriba) y devuelve {clave: historial} (o
    {tupla_str: {bucket: historial}} si anidado_por_bucket=True, mismo
    esquema que gate_bucket_propio.json). Fail-closed: fichero ausente/
    corrupto -> {} (ninguna promoción "bueno_confirmado" pasará el guard
    hoy, exige empezar a acumular desde cero, nunca al revés)."""
    try:
        with open(out_path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return {}
    if not anidado_por_bucket:
        return {clave: _semilla_desde_formato_antiguo(info)
                for clave, info in data.items() if isinstance(info, dict)}
    out = {}
    for tupla_str, tabla in data.items():
        if not isinstance(tabla, dict):
            continue
        out[tupla_str] = {b: _semilla_desde_formato_antiguo(v)
                           for b, v in tabla.items() if isinstance(v, dict)}
    return out


def cargar_fecha_historial_previo(out_path: Path, anidado_por_bucket: bool) -> dict:
    """10-Sep: acompaña a cargar_historial_previo() para los consumidores
    que necesiten veredicto_con_tolerancia_diario() (generadores intradía).
    Devuelve {clave: fecha_historial|None} (o {tupla_str: {bucket:
    fecha_historial|None}} si anidado_por_bucket=True) leyendo el mismo
    fichero de salida de la corrida anterior. Fail-closed igual que
    cargar_historial_previo(): fichero ausente/corrupto -> {} (fecha_previa
    ausente para toda clave -> veredicto_con_tolerancia_diario() la trata
    como "día nuevo" y no colapsa nada, nunca menos estricto que antes)."""
    try:
        with open(out_path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return {}
    if not anidado_por_bucket:
        return {clave: info.get("fecha_historial")
                for clave, info in data.items() if isinstance(info, dict)}
    out = {}
    for tupla_str, tabla in data.items():
        if not isinstance(tabla, dict):
            continue
        out[tupla_str] = {b: v.get("fecha_historial")
                           for b, v in tabla.items() if isinstance(v, dict)}
    return out
