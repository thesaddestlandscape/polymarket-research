#!/usr/bin/env python3
"""Vigía diario: automatiza la clasificación que se hizo a mano el 05-Ago
(project_candidatas_estancadas_diagnostico_05ago) sobre `candidatos_evaluacion_live`
(config_live.json, 282 tuplas) e `hipotesis_pendientes.json` (79 hipótesis) --
distingue "genuinamente pendiente de más datos" de "estructuralmente
congelado", que antes se confundían bajo el mismo aspecto ("n bajo") y
tardaban semanas en notarse (petición explícita de Javi tras encontrar el
patrón: "esto es tu responsabilidad").

Dos clases de estancamiento que se detectan por separado:

1. CEMENTERIO (estado absorbente real, el bug de fondo de la Parte 3 del
   diagnóstico 05-Ago): estrategia con `activa: False` (o `activa_BUY_YES`/
   `activa_BUY_NO`) en strategy_params.json, que NUNCA ha estado en
   pares_permitidos_live y NO tiene la excepción
   ACUMULAR_SHADOW_AUNQUE_DESACTIVADA (shadow_predict.py) -- no puede generar
   ni una fila más para corregirse a sí misma. Se resalta aparte si además
   tiene n<15 (viola la regla dura del manual: "ninguna conclusión con
   n<15" -- fue silenciada antes de poder defenderse).

2. ESTANCADO / NUNCA_GENERO: tuplas de candidatos_evaluacion_live e
   hipótesis de hipotesis_pendientes.json cuyo `n` no ha crecido nada en los
   últimos 7 días de historial propio (persistido aquí día a día -- no hace
   falta arqueología de git). NUNCA_GENERO (n=0 en TODO el historial
   disponible) es más grave que ESTANCADO (n>0 pero plano) -- suele indicar
   un filtro/bug bloqueando la generación, no solo falta de tiempo.

Esto es clasificación automática, NO diagnóstico de causa -- decir "por qué"
(filtro causal degenerado, clave de feature inexistente, blacklist que se
solapa, etc.) sigue exigiendo trazar el caso a mano, igual que se hizo el
05-Ago. El vigía solo garantiza que ningún caso pase desapercibido "mucho
tiempo" sin que nadie lo note -- avisa por Telegram (latch, solo casos
NUEVOS) y persiste el estado completo para revisión de sesión.

Read-only sobre resultados/config, no toca dinero ni desactiva/reactiva nada
-- la decisión y el arreglo siguen siendo de Claude Code en sesión o de
Javi, igual que el resto de vigías del proyecto.
"""
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from resultados_dedup import cargar_results_dedup  # noqa: E402

CONFIG_LIVE = REPO / "data/live/config_live.json"
HIPOTESIS_PENDIENTES = REPO / "data/shadow/hipotesis_pendientes.json"
STRATEGY_PARAMS = REPO / "data/shadow/strategy_params.json"
HISTORIAL = REPO / "data/live/candidatas_estancadas_historial.json"
LATCH = REPO / "data/live/vigia_candidatas_estancadas_latch.json"
SALIDA = REPO / "data/shadow/candidatas_estancadas.json"

DIAS_HISTORIAL = 14      # cuánto se conserva
DIAS_VENTANA_ESTANCADO = 7  # ventana para juzgar "no ha crecido"


def _cargar_json(path, default):
    try:
        return json.loads(path.read_text())
    except Exception:
        return default


def _n_por_tupla_candidatos(rows, tuplas):
    """n por tupla 'STRATEGY#SUBTYPE#DIRECTION' de candidatos_evaluacion_live,
    contando filas de results.csv cuyo (strategy, subtype, decision) matchea
    exactamente el sufijo de la tupla (subtype puede tener sub-segmentos,
    ej. 'BTC#15min')."""
    contador = {t: 0 for t in tuplas}
    indice = {}
    for t in tuplas:
        partes = t.split("#")
        decision = partes[-1]
        strategy = partes[0]
        subtype = "#".join(partes[1:-1])
        indice.setdefault((strategy, subtype, decision), []).append(t)
    for r in rows:
        clave = (r.get("strategy", ""), r.get("subtype", ""), r.get("decision", ""))
        for t in indice.get(clave, []):
            contador[t] += 1
    return contador


def _es_exenta_cementerio(nombre_base, exentas):
    return nombre_base in exentas


def _vive_en_pares_permitidos(nombre_base, subtype_key, pares_permitidos):
    return any(p.startswith(nombre_base) for p in pares_permitidos) or \
        any(subtype_key and p.startswith(subtype_key) for p in pares_permitidos)


def _detectar_cementerio():
    """Parte 1: strategy_params.json con activa=False, sin excepción, nunca live."""
    try:
        import shadow_predict as sp
        exentas = sp.ACUMULAR_SHADOW_AUNQUE_DESACTIVADA
    except Exception as e:
        print(f"[vigia_candidatas_estancadas] no se pudo importar ACUMULAR_SHADOW_AUNQUE_DESACTIVADA: {e}")
        exentas = set()

    params = _cargar_json(STRATEGY_PARAMS, {})
    estrategias = params.get("estrategias", params)
    config_live = _cargar_json(CONFIG_LIVE, {})
    pares_permitidos = set(config_live.get("pares_permitidos_live", []))

    cementerio = []
    for clave, datos in estrategias.items():
        if not isinstance(datos, dict):
            continue
        nombre_base = clave.split("#")[0]
        desactivada_mixta = datos.get("activa") is False
        desactivada_direccional = (
            datos.get("activa_BUY_YES") is False or datos.get("activa_BUY_NO") is False
        )
        if not (desactivada_mixta or desactivada_direccional):
            continue
        if _es_exenta_cementerio(nombre_base, exentas):
            continue
        if _vive_en_pares_permitidos(nombre_base, clave, pares_permitidos):
            continue  # tupla live pausada por decisión explícita -- no es cementerio, es pausa deliberada
        n = datos.get("n", 0)
        cementerio.append({
            "clave": clave,
            "n": n,
            "ic_bayes": datos.get("ic_bayes"),
            "motivo": datos.get("motivo", ""),
            "viola_n_minimo": n < 15,
        })
    # strategy_params.json repite la MISMA estrategia desactivada a varios
    # niveles de granularidad ("GBM_LATE_5M", "GBM_LATE_5M#5min",
    # "GBM_LATE_5M#BTC", "GBM_LATE_5M#BTC#5min", todas activa=False juntas) --
    # sin esto el mismo hallazgo real aparecía 2-4 veces e inflaba el aviso.
    # Quedarse solo con la clave MÁS ESPECÍFICA (hoja) de cada grupo: si
    # existe otra clave del propio cementerio que empieza por "clave#", esta
    # es un agregado redundante, se descarta.
    claves = {c["clave"] for c in cementerio}
    hojas = [c for c in cementerio
             if not any(k != c["clave"] and k.startswith(c["clave"] + "#") for k in claves)]
    return sorted(hojas, key=lambda x: x["n"])


_CLAVES_N = ("n", "n_overlaps", "n_total", "n_celdas_trackeadas")


def _extraer_n(entry):
    """Suma todos los valores bajo claves tipo n/n_overlaps/n_total/etc.,
    buscando en anidados de 1 nivel (by_pair.BTC.n, after_win.n, etc.) --
    BUG REAL encontrado 06-Ago: 13/79 hipótesis builtin NUNCA tuvieron un
    campo 'n' plano (n_overlaps/by_subtype/aligned_btc/... en su lugar,
    ver H-WINDOW-MOMENTUM/H-CROSS-ASSET/H-60MIN-LIVE/H-BTC-LEADS-ETH/etc.)
    -- un primer borrador de este vigía usaba entry.get('n', 0), que las
    habría marcado 'nunca_genero' (falsa alarma) pese a estar sanas y
    acumulando miles de filas. Devuelve None (no trackeable) si no se
    encuentra ningún valor bajo esas claves en ningún nivel -- eso excluye
    correctamente a las bloqueadas por dataset/API (H-OBI, H-KALMAN, etc.)
    en vez de mentir con un 0."""
    total = 0
    encontrado = False

    def _walk(obj):
        nonlocal total, encontrado
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in _CLAVES_N and isinstance(v, (int, float)):
                    total += v
                    encontrado = True
                elif isinstance(v, dict):
                    _walk(v)
        # listas (ej. gate_ok, subtypes_listos) no son conteos, se ignoran

    if isinstance(entry.get("n"), (int, float)):
        return entry["n"]
    _walk(entry)
    return total if encontrado else None


def _cargar_historial():
    h = _cargar_json(HISTORIAL, {"candidatos": {}, "hipotesis": {}})
    h.setdefault("candidatos", {})
    h.setdefault("hipotesis", {})
    return h


def _actualizar_historial(historial, categoria, valores_hoy, hoy_iso):
    bucket = historial[categoria]
    for clave, n in valores_hoy.items():
        serie = bucket.setdefault(clave, {})
        serie[hoy_iso] = n
        # podar fechas viejas
        fechas = sorted(serie.keys())
        if len(fechas) > DIAS_HISTORIAL:
            for f in fechas[: len(fechas) - DIAS_HISTORIAL]:
                del serie[f]
    # también podar claves que ya no existen en valores_hoy Y llevan
    # DIAS_HISTORIAL sin aparecer (evita crecer sin límite con candidatos
    # retirados) -- conservador, solo poda si no se ha visto en toda la
    # ventana conservada.
    for clave in list(bucket.keys()):
        if clave not in valores_hoy and len(bucket[clave]) >= DIAS_HISTORIAL:
            del bucket[clave]


def _clasificar_estancados(bucket, hoy_iso):
    """Para cada clave con >= DIAS_VENTANA_ESTANCADO días de historial,
    compara n de hace esos días vs hoy. Devuelve (estancados, nunca_genero)."""
    estancados, nunca_genero = [], []
    hoy_dt = datetime.fromisoformat(hoy_iso)
    for clave, serie in bucket.items():
        fechas = sorted(serie.keys())
        if len(fechas) < 2:
            continue
        fecha_ref = None
        for f in fechas:
            if (hoy_dt - datetime.fromisoformat(f)).days >= DIAS_VENTANA_ESTANCADO:
                fecha_ref = f
        if fecha_ref is None:
            continue  # todavía no hay suficiente historial para juzgar
        n_ref = serie[fecha_ref]
        n_hoy = serie.get(hoy_iso, serie[fechas[-1]])
        if n_hoy == 0 and all(serie[f] == 0 for f in fechas):
            nunca_genero.append({"clave": clave, "dias_historial": len(fechas)})
        elif n_hoy <= n_ref:
            estancados.append({
                "clave": clave, "n_hace_dias": n_ref, "n_hoy": n_hoy,
                "dias": (hoy_dt - datetime.fromisoformat(fecha_ref)).days,
            })
    return estancados, nunca_genero


def main() -> int:
    from shadow_digest import enviar_telegram

    hoy_iso = datetime.now(timezone.utc).date().isoformat()

    # --- Parte 1: cementerio ---
    cementerio = _detectar_cementerio()

    # --- Parte 2: candidatos_evaluacion_live ---
    config_live = _cargar_json(CONFIG_LIVE, {})
    tuplas = [t for t in config_live.get("candidatos_evaluacion_live", []) if isinstance(t, str)]
    rows = cargar_results_dedup()
    n_candidatos_hoy = _n_por_tupla_candidatos(rows, tuplas)

    # --- Parte 3: hipotesis_pendientes.json (n ya calculado por hypothesis_tracker) ---
    hipotesis = _cargar_json(HIPOTESIS_PENDIENTES, {})
    n_hipotesis_hoy = {}
    for k, v in hipotesis.items():
        if not isinstance(v, dict):
            continue
        if v.get("bloqueante") or str(v.get("status", "")).startswith("BLOQUEADA"):
            continue  # bloqueada por dataset/API a propósito, no es estancamiento
        n = _extraer_n(v)
        if n is not None:
            n_hipotesis_hoy[k] = n

    historial = _cargar_historial()
    _actualizar_historial(historial, "candidatos", n_candidatos_hoy, hoy_iso)
    _actualizar_historial(historial, "hipotesis", n_hipotesis_hoy, hoy_iso)
    HISTORIAL.parent.mkdir(parents=True, exist_ok=True)
    HISTORIAL.write_text(json.dumps(historial, indent=2))

    cand_estancados, cand_nunca = _clasificar_estancados(historial["candidatos"], hoy_iso)
    hip_estancadas, hip_nunca = _clasificar_estancados(historial["hipotesis"], hoy_iso)

    resultado = {
        "generado": datetime.now(timezone.utc).isoformat(),
        "cementerio": cementerio,
        "candidatos_estancados": cand_estancados,
        "candidatos_nunca_genero": cand_nunca,
        "hipotesis_estancadas": hip_estancadas,
        "hipotesis_nunca_genero": hip_nunca,
    }
    SALIDA.write_text(json.dumps(resultado, indent=2, ensure_ascii=False))

    print(f"[vigia_candidatas_estancadas] cementerio={len(cementerio)} "
          f"cand_estancados={len(cand_estancados)} cand_nunca={len(cand_nunca)} "
          f"hip_estancadas={len(hip_estancadas)} hip_nunca={len(hip_nunca)}")

    # --- Aviso Telegram solo de casos NUEVOS (latch) ---
    latch = _cargar_json(LATCH, {})
    nuevos = []

    def _revisar(lista, prefijo, clave_id="clave"):
        for item in lista:
            cid = f"{prefijo}:{item[clave_id]}"
            if not latch.get(cid, {}).get("avisado"):
                nuevos.append((cid, prefijo, item))
                latch[cid] = {"avisado": True}

    _revisar(cementerio, "cementerio")
    _revisar(cand_nunca, "cand_nunca")
    _revisar(hip_nunca, "hip_nunca")
    # estancados (no nunca_genero) son más ruidosos/menos graves -- solo se
    # avisan si violan n<15 en cementerio; para candidatos/hipotesis
    # "estancado pero con n>0" se deja para revisión de sesión vía SALIDA,
    # no telegram (evita ruido -- ya se sabe que 111/282 estaban así el
    # 05-Ago, avisar de cada uno individualmente saturaría el canal).

    if nuevos:
        lineas = []
        for cid, prefijo, item in nuevos[:20]:
            if prefijo == "cementerio":
                extra = " ⚠️n<15" if item.get("viola_n_minimo") else ""
                lineas.append(f"  🪦 {item['clave']} (n={item['n']}, ic={item.get('ic_bayes')}){extra}")
            else:
                lineas.append(f"  🚫 {item['clave']} (0 filas en {item['dias_historial']}d de historial)")
        extra_n = f"\n  ... y {len(nuevos)-20} más" if len(nuevos) > 20 else ""
        msg = (
            f"🔍 vigia_candidatas_estancadas: {len(nuevos)} caso(s) NUEVO(s) "
            f"de estado absorbente / nunca-genera-datos\n" + "\n".join(lineas) + extra_n +
            f"\n\nDetalle completo en data/shadow/candidatas_estancadas.json"
        )
        ok = enviar_telegram(msg)
        print(f"[vigia_candidatas_estancadas] aviso enviado (telegram={ok}, {len(nuevos)} nuevos)")
        LATCH.write_text(json.dumps(latch, indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
