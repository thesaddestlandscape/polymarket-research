"""gate_confirmacion_historial.py — 01-Sep, petición explícita Javi.

13-Oct: API NUEVA al final del módulo (veredicto_dia, cargar_estado_previo, mantener_no_confirmados,
mantener_dos_vias, reglas 1-7: días de calendario con marca por entrada y corridas no decisivas). La usan
gate_bucket_propio, bot_wallets y wallet_mirror. veredicto_con_tolerancia[_diario] y cargar_[fecha_]historial_previo
quedan SOLO para los generadores pendientes de migrar (fino, sports, candidata9/10): no usarlos en código nuevo.

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


# ---------------------------------------------------------------------------------------------------------------------
# 13-Oct (Javi "dale"; 10 pasadas de /code-review medium + revisión línea a línea): DÍAS DE CALENDARIO + corridas que NO
# confirman.
# Bug real: los generadores solo pasaban por la tolerancia "2 de 3 días" los buckets que sobrevivían al BH-FDR de ESA
# corrida; el resto hacía `continue` y quedaba sin_concluir aunque su historial fuera bueno/bueno/bueno (WALLET_MIRROR
# SEGUIR#BTC#15min#1 [0.35,0.40), gate horario, parpadeó cada hora con n y pnl idénticos: el BH-FDR del grupo depende de
# los p de los OTROS buckets). Y el historial no tenía fechas: un "bueno" de hace semanas contaba igual que uno de ayer
# (349 buckets del gate propio con un bueno rancio). Reglas, en UN solo sitio:
#   1. Calendario: cada entrada del historial lleva la MARCA de la corrida que la escribió (historial_fechas[_abs],
#      "AAAA-MM-DDTHH:MM" UTC; el día es [:10]). Ventana = HISTORIAL_DIAS_VENTANA días de calendario hasta hoy; lo
#      anterior se descarta. Un día sin entrada no es bueno. Dos buenos solo cuentan como 2 días si están separados
#      >= SEPARACION_MIN_H horas (dos corridas horarias a ambos lados de medianoche son la misma evidencia).
#   2. Sin migración: un historial sin historial_fechas (formato anterior) NO cuenta; nunca se inventan fechas.
#      Todo bucket vuelve a confirmar con 2 días buenos reales. Transición (OK Javi 13-Oct, "dale"): los buenos vigentes
#      quedan vetados ~1 día (WM horario) / ~2 días (gates diarios) hasta reconfirmar.
#   3. Un día = su última corrida DECISIVA (bueno, malo o sin_concluir). Una corrida "casi significativa" (p bruto
#      <= p_max, dirección y split-half a favor, suelo cumplido; solo le falta la corrección por multiplicidad) o una que
#      NO PUDO testear el bucket (sin p del test en esa vía) NUNCA pisa un día ya decidido; si el día aún no tiene
#      entrada, cuenta como sin_concluir.
#   4. malo_confirmado de una corrida que DECIDIÓ el bucket (su test, o las guardas sobre un bucket que esa corrida
#      decidió), en cualquiera de las dos vías: inmediato, reinicia el historial y se publica hasta medianoche. Se
#      aplica en UN solo punto, al final de cada corrida (aplicar_malos_de_hoy): toda entrada con un malo de HOY se
#      publica malo, salvo que el malo sea de ESTA corrida y el rescate absoluto lo haya levantado en ESTA corrida
#      (diseño 12-Sep). Una guarda NUNCA crea un malo en un bucket que la corrida no decidió. Límites aceptados: si el
#      fichero anterior es ilegible (escritura atómica en los 3 generadores: solo a mano) o cambia el METODO (decisión
#      nuestra), los malos de hoy se pierden con el resto del historial.
#   5. Un bucket que no confirma en esta corrida solo sigue bueno si la corrida ANTERIOR lo publicó bueno, su historial
#      de calendario tiene 2 días buenos (regla 1) y pasa HOY las guardas del generador, suelo de pnl incluido, y no es
#      hoy peor que el resto con split-half consistente. Nunca baja ni re-etiqueta lo que otra vía puso en la corrida.
#   6. La marca "ahora" se fija UNA vez por corrida. Si otra corrida decisiva del mismo día sustituye la entrada de
#      hoy con el MISMO veredicto, conserva la marca de la primera (una re-ejecución no retrasa los 20 h); si el
#      veredicto cambia, la marca es la de la corrida que lo produjo (un bueno de las 23:05 no hereda las 00:05).
#      Para los >= SEPARACION_MIN_H de la regla 1, si ESTA corrida da bueno hoy, el día de hoy cuenta hasta "ahora"
#      (la última corrida decisiva buena), no hasta su marca: sin esto un gate HORARIO (WM) bueno todas las horas
#      desde el día 1 a las 10:05 no confirmaba hasta el día 3 a las 00:05 (todas las horas del día 2 llevaban la
#      marca 00:05, 14 h). Con esto confirma el día 2 a las 06:05. Una corrida "casi significativa" que no pisa el
#      día (regla 3) NO usa "ahora": su bueno es de una corrida anterior.
#   7. Fichero anterior ilegible: se AVISA (stdout, que recogen los vigías) y se empieza de cero (fail-closed).
# ---------------------------------------------------------------------------------------------------------------------
from datetime import date, timedelta  # noqa: E402

BUENO, MALO, SIN = "bueno_confirmado", "malo_confirmado", "sin_concluir"
SEPARACION_MIN_H = 20


def ahora_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M")


def _dia(marca: str) -> str:
    return marca[:10]


def _parse_marca(m: str) -> datetime:
    """Único parser de marcas ("AAAA-MM-DD[THH:MM]", sin zona). Lanza TypeError/ValueError si no es válida."""
    d = datetime.fromisoformat(m if len(m) > 10 else m + "T23:59")
    if d.tzinfo is not None:
        raise ValueError(f"marca con zona horaria: {m}")
    return d


def _horas(a: str, b: str) -> float:
    return abs((_parse_marca(b) - _parse_marca(a)).total_seconds()) / 3600


def _en_ventana(hist: list, marcas: list, ahora: str) -> tuple[list, list]:
    desde = (date.fromisoformat(_dia(ahora)) - timedelta(days=HISTORIAL_DIAS_VENTANA - 1)).isoformat()
    pares = [(v, m) for v, m in zip(hist, marcas) if m and desde <= _dia(m) <= _dia(ahora)]
    return [v for v, _ in pares], [m for _, m in pares]


def _confirma(hist: list, marcas: list, hasta: str | None = None) -> str:
    """hasta: "ahora" si ESTA corrida dio bueno hoy (regla 6); el último bueno de hoy cuenta hasta esa hora."""
    buenas = [m for v, m in zip(hist, marcas) if v == BUENO]
    if buenas and hasta is not None and _dia(buenas[-1]) == _dia(hasta):
        buenas[-1] = hasta
    if len(buenas) >= HISTORIAL_DIAS_REQUERIDOS and _horas(buenas[0], buenas[-1]) >= SEPARACION_MIN_H:
        return BUENO
    return SIN


def veredicto_dia(veredicto_crudo: str, historial: list | None, marcas: list | None, ahora: str,
                  casi_significativo: bool = False) -> tuple[str, list, list]:
    """(veredicto, historial, marcas) para UNA corrida (reglas 1, 3 y 4). `historial`/`marcas` ya migrados."""
    hist, mar = _en_ventana(list(historial or []), list(marcas or []), ahora)
    if veredicto_crudo == MALO:
        return MALO, [MALO], [ahora]
    hoy_decidido = bool(mar) and _dia(mar[-1]) == _dia(ahora)
    if hoy_decidido and hist[-1] == MALO:
        return MALO, hist, mar                               # regla 4: el malo de hoy no lo pisa nadie hoy
    if hoy_decidido:
        if casi_significativo and veredicto_crudo == SIN:     # regla 3: no pisa el día ya decidido
            return _confirma(hist, mar), hist, mar
        mar = mar if hist[-1] == veredicto_crudo else mar[:-1] + [ahora]                      # regla 6
        hist = hist[:-1] + [veredicto_crudo]
        return _confirma(hist, mar, ahora if veredicto_crudo == BUENO else None), hist, mar
    hist, mar = hist + [veredicto_crudo], mar + [ahora]
    return _confirma(hist, mar), hist, mar


def veredicto_decidido(veredicto_crudo: str, historial: list | None, marcas: list | None,
                        ahora: str) -> tuple[str, list, list]:
    """veredicto_dia() para un bucket que ESTA corrida decidió (sobrevive al test). Si las guardas de hoy rebajaron el
    crudo (sin_concluir), no se mantiene un bueno por historial (regla 5 también aquí): se registra el día y se publica
    sin_concluir. Un malo del test sigue siendo malo."""
    ver, hist, marcas = veredicto_dia(veredicto_crudo, historial, marcas, ahora)
    if veredicto_crudo != BUENO and ver == BUENO:
        ver = SIN
    return ver, hist, marcas


def migrar_entrada(v: dict, sufijo: str = "") -> tuple[list, list]:
    """(historial, marcas) de una entrada del fichero ANTERIOR. Formato anterior (sin historial_fechas): nada (regla 2)."""
    hist = v.get("historial_crudo" + sufijo) or []
    if not isinstance(hist, list):
        return [], []
    marcas = v.get("historial_fechas" + sufijo)
    try:
        if (hist and isinstance(marcas, list) and len(marcas) == len(hist)
                and all(x in (BUENO, MALO, SIN) for x in hist)):
            for m in marcas:                                # marca parseable y SIN zona horaria (como ahora_utc())
                _parse_marca(m)
            return hist, list(marcas)
    except (TypeError, ValueError):
        pass
    return [], []                                         # forma inesperada = sin historial (fail-closed)


def cargar_estado_previo(out_path: Path) -> dict:
    """{"": (hists, marcas), "_abs": (hists, marcas), "veredicto": {clave: {bucket: veredicto publicado}}} del fichero
    ANTERIOR, migrado (regla 2), en UNA lectura. Ausente -> vacío; ilegible -> AVISO y vacío (regla 7)."""
    estado = estado_vacio()
    try:
        data = json.loads(Path(out_path).read_text(encoding="utf-8"))
        for clave, tabla in data.items():
            if not isinstance(tabla, dict):
                continue
            for b, v in tabla.items():
                if not isinstance(v, dict) or not isinstance(b, str):
                    continue
                estado["veredicto"].setdefault(clave, {})[b] = v.get("veredicto")
                estado["detalle"].setdefault(clave, {})[b] = {"n": v.get("n"), "pnl_medio": v.get("pnl_medio"),
                                                               "reales": v.get("n_pnl_heredados") is not False}
                for sufijo in ("", "_abs"):
                    h, m = migrar_entrada(v, sufijo)
                    if h:
                        estado[sufijo][0].setdefault(clave, {})[b] = h
                        estado[sufijo][1].setdefault(clave, {})[b] = m
    except FileNotFoundError:
        return estado_vacio()
    except Exception as e:
        print(f"🚨 gate_confirmacion_historial: {out_path} ILEGIBLE o con forma inesperada ({type(e).__name__}: {e}) -- "
              f"historial de tolerancia perdido, todo bucket tendrá que reconfirmar 2 días (fail-closed)")
        return estado_vacio()
    return estado


def estado_vacio() -> dict:
    return {"": ({}, {}), "_abs": ({}, {}), "veredicto": {}, "detalle": {}}


def malo_de_hoy(hist: list, marcas: list, ahora: str) -> bool:
    """Regla 4: el último día decidido es HOY y fue malo."""
    return bool(hist) and hist[-1] == MALO and bool(marcas) and _dia(marcas[-1]) == _dia(ahora)


def campos_historial(hist: list, marcas: list, sufijo: str = "") -> dict:
    """Campos a escribir en una entrada (fecha_historial = día de la última entrada, por compatibilidad)."""
    return {"historial_crudo" + sufijo: hist, "historial_fechas" + sufijo: marcas,
            "fecha_historial" + sufijo: _dia(marcas[-1]) if marcas else None}


def semilla(estado: dict, clave: str, b: str, ahora: str) -> dict:
    """Campos de historial (ambas vías) de un bucket al construir su entrada, ya recortados a la ventana."""
    out = {}
    for sufijo in ("", "_abs"):
        h = estado[sufijo][0].get(clave, {}).get(b, [])
        m = estado[sufijo][1].get(clave, {}).get(b, [])
        out.update(campos_historial(*_en_ventana(h, m, ahora), sufijo))
    return out


def entradas_sin_filas_hoy(tabla: dict, clave: str, estado: dict, ahora: str) -> None:
    """Buckets con historial vivo (dentro de la ventana, cualquier vía) que HOY no tienen filas: se conservan con su
    historial, marcados sin_filas_hoy; si hoy hubo un malo (de cualquier vía) se sigue publicando malo_confirmado (regla 4),
    si no, sin_concluir. Los que ya no tienen nada en la ventana desaparecen (poda)."""
    for b in (set(estado[""][0].get(clave, {})) | set(estado["_abs"][0].get(clave, {}))) - set(tabla):
        campos = semilla(estado, clave, b, ahora)
        if campos["historial_crudo"] or campos["historial_crudo_abs"]:
            # Un malo de HOY se sigue publicando (regla 4: si quedara sin_concluir, una fuente ADITIVA como el gate fino
            # podría promocionarlo a bueno). Lleva el n/pnl_medio de la corrida anterior (los vigías y el histórico CSV
            # los leen); si no los hay, 0 con n_pnl_heredados=False (los vigías no pueden recibir un malo sin n).
            malo = any(malo_de_hoy(campos["historial_crudo" + s], campos["historial_fechas" + s], ahora) for s in ("", "_abs"))
            previo = estado.get("detalle", {}).get(clave, {}).get(b) or {}
            if malo:
                n_p, pnl_p = previo.get("n"), previo.get("pnl_medio")
                ok = isinstance(n_p, (int, float)) and isinstance(pnl_p, (int, float)) and previo.get("reales", False)
                tabla[b] = {"veredicto": MALO, "sin_filas_hoy": True, "n": n_p if ok else 0,
                            "pnl_medio": pnl_p if ok else 0.0, "n_pnl_heredados": ok, **campos}
            else:
                tabla[b] = {"veredicto": SIN, "sin_filas_hoy": True, **campos}


def claves_sin_filas_hoy(resultado: dict, estado: dict, ahora: str) -> None:
    """Claves enteras con historial vivo que HOY no aparecen en los datos (CSV rotado, lectura parcial): se conservan
    como en entradas_sin_filas_hoy (sin esto desaparecían y una fuente aditiva podía promocionar un malo de hoy)."""
    for clave in (set(estado[""][0]) | set(estado["_abs"][0])) - set(resultado):
        tabla = {}
        entradas_sin_filas_hoy(tabla, clave, estado, ahora)
        if tabla:
            resultado[clave] = tabla


def aplicar_malos_de_hoy(resultado: dict, ahora: str) -> list:
    """Regla 4 en UN solo punto, al final de la corrida y después de TODAS las vías: toda entrada con un malo de HOY
    (vía relativa o absoluta) se publica malo_confirmado, salvo el rescate absoluto de ESTA corrida sobre un malo
    relativo de ESTA corrida (diseño 12-Sep). Devuelve la lista de (clave, bucket, veredicto que tenía) forzados a malo."""
    n = []
    for clave, tabla in resultado.items():
        for b, e in tabla.items():
            hr, mr = e.get("historial_crudo") or [], e.get("historial_fechas") or []
            ha, ma = e.get("historial_crudo_abs") or [], e.get("historial_fechas_abs") or []
            malo_rel, malo_abs = malo_de_hoy(hr, mr, ahora), malo_de_hoy(ha, ma, ahora)
            if not (malo_rel or malo_abs):
                continue
            # "de ESTA corrida": veredicto_crudo_hoy lo fija la propia corrida al decidir el bucket (no la marca, que solo
            # tiene resolución de minuto y dos corridas en el mismo minuto se confundirían).
            rescate_misma_corrida = (e.get("veredicto") == BUENO and e.get("via") == "absoluta"
                                     and "veredicto_crudo_hoy_abs" in e and not malo_abs
                                     and e.get("veredicto_crudo_hoy") == MALO)
            if rescate_misma_corrida or e.get("veredicto") == MALO:
                continue
            n.append((clave, b, e.get("veredicto")))
            e["veredicto"] = MALO
            e["via"] = "malo_de_hoy"
    return n


def mantener_no_confirmados(resultado: dict, ahora: str, n_min: int, estado: dict, casi_fn, guardas_fn,
                            sufijo: str = "") -> list[str]:
    """Regla 5 para los buckets que esta corrida NO decidió en esta vía (sin veredicto_crudo_hoy{sufijo}), con
    n>=n_min, publicados bueno en la corrida ANTERIOR y algún bueno en su historial. casi_fn(clave, b, e)->bool;
    guardas_fn(clave, b, e)->BUENO/SIN/MALO que darían HOY las guardas del generador (suelo y dirección incluidos) a un
    bueno. Un BUENO solo se publica si el vigente es sin_concluir. NO publica malos: los malos de hoy los publica
    aplicar_malos_de_hoy() al final de la corrida (regla 4). La vía absoluta salta lo que la relativa ya puso bueno en
    esta corrida (no erosiona su evidencia absoluta). Devuelve líneas de log NEUTRAS (no son veredictos nuevos)."""
    lineas = []
    for clave, tabla in resultado.items():
        for b, e in tabla.items():
            if "veredicto_crudo_hoy" + sufijo in e or e.get("sin_filas_hoy"):
                continue                                       # decidido en esta corrida, o marcador sin filas (sin n/pnl)
            if sufijo and e.get("veredicto") == BUENO and e.get("via") != "absoluta":
                continue                                       # la vía absoluta nunca pisa a la relativa
            hist, marcas = e.get("historial_crudo" + sufijo) or [], e.get("historial_fechas" + sufijo) or []
            if malo_de_hoy(hist, marcas, ahora):               # regla 4: lo publica aplicar_malos_de_hoy() al final
                continue
            if (e.get("n") or 0) < n_min or BUENO not in hist:
                continue
            guardas = guardas_fn(clave, b, e)
            testeado = e.get("p_valor_abs" if sufijo else "shuffle_p") is not None
            casi = guardas == BUENO and (bool(casi_fn(clave, b, e)) or not testeado)   # regla 3
            ver, hist, marcas = veredicto_dia(SIN, hist, marcas, ahora, casi_significativo=casi)
            e.update(campos_historial(hist, marcas, sufijo))
            publicado_antes = estado["veredicto"].get(clave, {}).get(b) == BUENO
            if guardas == BUENO and ver == BUENO and publicado_antes and e.get("veredicto") == SIN:
                e["veredicto"], e["via"] = BUENO, ("absoluta" if sufijo else "tolerancia")
                lineas.append(f"[tolerancia{sufijo}] {clave} [{b}) n={e.get('n')} historial {list(zip(hist, marcas))} "
                              f"({'casi significativo' if casi else 'día flojo'}) -> se mantiene bueno_confirmado")
    return lineas


def mantener_dos_vias(resultado: dict, ahora: str, n_min: int, estado: dict, pendientes: list, clave_key: str,
                      degradar_fn, p_max: float, umbral_abs: float | None, campo_split: str = "split_half") -> list[str]:
    """Las dos pasadas de mantener_no_confirmados (relativa y después absoluta) con los MISMOS criterios para todos los
    generadores (WM, bot wallets; gate propio con umbral_abs=None). degradar_fn(clave, b, e) -> veredicto que darían HOY
    las guardas del generador a un bueno (_degradar en WM/bot; piso CI90 en el gate propio).
    Relativa: suelo pnl_medio>=0 y no peor que el resto con split-half consistente; casi = diff>0 y p bruto<=p_max.
    Absoluta: suelo pnl_medio>=umbral_abs y las dos mitades del split-half absoluto > 0; casi = p_valor_abs<=p_max."""
    pend = {(p[clave_key], p["bucket"]): p for p in pendientes}

    def peor_que_resto(e):
        sh = e.get(campo_split)
        return sh is not None and sh[0] < 0 and sh[1] < 0

    def guardas_rel(c, b, e):
        return degradar_fn(c, b, e) if e["pnl_medio"] >= 0 and not peor_que_resto(e) else SIN

    def guardas_abs(c, b, e):
        sh = e.get("split_half_absoluto")
        ok = e["pnl_medio"] >= umbral_abs and sh is not None and sh[0] > 0 and sh[1] > 0
        return degradar_fn(c, b, e) if ok else SIN

    def casi_rel(c, b, e):
        p = pend.get((c, b))
        return p is not None and p["diff"] > 0 and p["p"] <= p_max

    def casi_abs(c, b, e):                           # el split-half absoluto ya lo exige guardas_abs
        pa = e.get("p_valor_abs")
        return pa is not None and pa <= p_max

    # Relativa primero: lo que mantiene queda etiquetado con su vía y la absoluta lo salta sin tocar su historial.
    lineas = mantener_no_confirmados(resultado, ahora, n_min, estado, casi_rel, guardas_rel)
    if umbral_abs is not None:                       # None = generador sin vía absoluta activa (gate propio)
        lineas += mantener_no_confirmados(resultado, ahora, n_min, estado, casi_abs, guardas_abs, sufijo="_abs")
    return lineas
