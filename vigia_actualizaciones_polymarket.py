#!/usr/bin/env python3
"""vigia_actualizaciones_polymarket.py -- vigía diaria de actualizaciones
de la PLATAFORMA Polymarket (no de nuestros datos/estrategias).

Origen (09-Ago, petición explícita Javi tras el hallazgo del cambio TWAP
de resolución del 07-Ago -- "solo así estaremos informados de forma fiel
de qué cambios se introducen en la plataforma que operamos"): el cambio
TWAP no lo detectó ningún vigía nuestro, lo trajo Javi de un tuit externo.
Verificado esa noche (ver memoria project_twap_chainlink_confirmado_09ago)
con dos fuentes propias -- ninguna sola basta:

1. Changelog oficial (docs.polymarket.com/changelog/predictions):
   mantenido por Polymarket, fechado, cubre fees/latencia/contratos/tick
   sizes -- pero NO tenía ninguna entrada de agosto cuando se comprobó,
   el cambio TWAP no se documentó ahí (al menos no a tiempo).
2. Diff estructural de nuestros propios mercados vía gamma-api (mismo
   método con el que se confirmó el TWAP esa noche): compara
   description/resolutionSource/feeSchedule/rewards de un mercado
   representativo por (activo, marco) contra el snapshot de ayer -- esto
   SÍ habría detectado el TWAP automáticamente (el texto de `description`
   cambió literalmente).

Avisa por Telegram SOLO si hay algo nuevo en cualquiera de las dos
fuentes (mismo criterio que el resto de vigías, evitar ruido) -- pero
persiste el estado completo siempre, revisable en cualquier sesión.
Primera ejecución nunca avisa (no hay baseline todavía), solo siembra.

Cron diario propuesto: 06:45 UTC (antes de los vigías de gate_bucket_
propio/calibración que ya usan datos del día).
"""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

TIMEOUT = 20
H = {"User-Agent": "Mozilla/5.0 (compatible; polymarket-research-monitor/1.0)"}
GAMMA = "https://gamma-api.polymarket.com"

CHANGELOG_URL = "https://docs.polymarket.com/changelog/predictions"
CHANGELOG_STATE = REPO / "data" / "shadow" / "polymarket_changelog_predictions_state.json"
ESTRUCTURA_STATE = REPO / "data" / "shadow" / "polymarket_estructura_mercados_state.json"
LOG = REPO / "logs" / "vigia_actualizaciones_polymarket.log"

# Representativos: (activo, patrón de slug, campo de duración legible).
# BTC+ETH cubren de sobra los mecanismos de resolución (ya verificado
# 09-Ago que BTC/SOL#60min comparten fuente Binance, no hace falta más
# de 1-2 activos por marco para detectar un cambio de MECANISMO).
COMBOS = [
    ("BTC", "5min", "btc-updown-5m"),
    ("BTC", "15min", "btc-updown-15m"),
    ("BTC", "60min", "bitcoin-up-or-down-"),   # slug distinto: nombre completo, no BTC
    ("BTC", "240min", "btc-updown-4h"),
    ("ETH", "5min", "eth-updown-5m"),
    ("ETH", "15min", "eth-updown-15m"),
    ("ETH", "60min", "ethereum-up-or-down-"),  # idem, nombre completo
    ("ETH", "240min", "eth-updown-4h"),
]

CAMPOS_VIGILADOS = ["description", "resolutionSource", "feeSchedule",
                    "rewardsMinSize", "rewardsMaxSpread", "negRisk", "enableOrderBook"]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def _limpiar_html(html: str) -> str:
    """HTML -> texto plano legible, con saltos de línea en tags de bloque
    para que un diff por líneas tenga sentido."""
    texto = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.S)
    texto = re.sub(r"<style[^>]*>.*?</style>", "", texto, flags=re.S)
    texto = re.sub(r"</(p|li|h[1-6]|div|tr)>", "\n", texto, flags=re.I)
    texto = re.sub(r"<[^>]+>", " ", texto)
    texto = re.sub(r"[ \t]+", " ", texto)
    lineas = [l.strip() for l in texto.splitlines()]
    return "\n".join(l for l in lineas if l)


def _extraer_cuerpo_changelog(texto: str) -> str:
    """El cuerpo real empieza tras el segundo 'Copy page' (el primero es
    un botón de navegación, antes del contenido)."""
    marca = "Copy page"
    i1 = texto.find(marca)
    i2 = texto.find(marca, i1 + 1) if i1 >= 0 else -1
    if i2 >= 0:
        return texto[i2 + len(marca):].strip()
    return texto


def revisar_changelog_oficial() -> dict | None:
    """Devuelve {'cambio': bool, 'nuevo_fragmento': str|None} o None si
    falla la petición (best-effort, no crítico -- la fuente B cubre el
    caso silencioso)."""
    try:
        r = requests.get(CHANGELOG_URL, headers=H, timeout=TIMEOUT)
        r.raise_for_status()
    except Exception as e:
        _log(f"WARN changelog oficial inaccesible: {type(e).__name__}: {e}")
        return None

    cuerpo = _extraer_cuerpo_changelog(_limpiar_html(r.text))
    if not cuerpo:
        _log("WARN changelog oficial: cuerpo vacío tras parseo, saltado")
        return None

    hash_actual = hashlib.sha256(cuerpo.encode("utf-8")).hexdigest()

    anterior = {}
    if CHANGELOG_STATE.exists():
        try:
            anterior = json.loads(CHANGELOG_STATE.read_text(encoding="utf-8"))
        except Exception:
            anterior = {}

    hash_anterior = anterior.get("hash")
    texto_anterior = anterior.get("texto", "")

    resultado = {"cambio": False, "nuevo_fragmento": None}
    if hash_anterior is not None and hash_anterior != hash_actual:
        # nuevo contenido: las entradas son fecha-primero (más reciente
        # arriba) -- el fragmento nuevo es lo que aparece ANTES del punto
        # donde el texto vuelve a coincidir con el snapshot anterior.
        import difflib
        sm = difflib.SequenceMatcher(None, texto_anterior, cuerpo)
        bloques_nuevos = []
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag in ("insert", "replace"):
                bloques_nuevos.append(cuerpo[j1:j2])
        fragmento = "\n".join(b.strip() for b in bloques_nuevos if b.strip())
        resultado["cambio"] = True
        resultado["nuevo_fragmento"] = fragmento[:2000]

    CHANGELOG_STATE.write_text(json.dumps({
        "hash": hash_actual, "texto": cuerpo,
        "actualizado": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "primera_vez": hash_anterior is None,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    if hash_anterior is None:
        _log("changelog oficial: primera ejecución, baseline sembrado (sin aviso)")
        resultado["cambio"] = False  # nunca avisar en la siembra inicial

    return resultado


def _listar_eventos_abiertos(max_paginas: int = 8) -> list:
    """gamma-api ignora/clampa limit>100 en la práctica (confirmado 09-Ago:
    limit=500 devolvía solo 100 eventos) -- pagina con offset hasta
    max_paginas*100 eventos o hasta que una página venga vacía. Los
    marcos menos frecuentes (60min/240min) quedan más abajo en la lista
    ordenada por startDate descendente que 5min/15min."""
    eventos = []
    for offset in range(0, max_paginas * 100, 100):
        try:
            r = requests.get(f"{GAMMA}/events", params={
                "closed": "false", "limit": 100, "offset": offset,
                "order": "startDate", "ascending": "false",
            }, headers=H, timeout=TIMEOUT)
            r.raise_for_status()
            batch = r.json()
        except Exception as e:
            _log(f"WARN página de eventos offset={offset} falló: {type(e).__name__}: {e}")
            break
        if not batch:
            break
        eventos.extend(batch)
    return eventos


def _buscar_market_id(activo: str, marco_slug_prefix: str, marco: str) -> str | None:
    """Busca el market_id de un mercado ABIERTO representativo con ese
    prefijo de slug de evento. Verificado 09-Ago: 5min/15min/240min usan
    prefijo por símbolo (btc-updown-5m/15m/4h), 60min usa el nombre
    completo del activo (bitcoin-up-or-down-/ethereum-up-or-down-) --
    slugs distintos, NO una duración calculable desde startDate/endDate
    del evento (startDate ahí es cuándo se LISTÓ el mercado, no la
    apertura de la ventana -- descartado como heurística tras probarlo)."""
    eventos = _listar_eventos_abiertos()
    if not eventos:
        _log(f"WARN sin eventos abiertos disponibles para {activo}#{marco}")
        return None

    for e in eventos:
        slug = e.get("slug", "")
        if slug.startswith(marco_slug_prefix):
            markets = e.get("markets") or []
            if markets:
                return markets[0].get("id") or markets[0].get("slug")
    return None


def _fetch_market(market_id: str) -> dict | None:
    try:
        r = requests.get(f"{GAMMA}/markets/{market_id}", headers=H, timeout=TIMEOUT)
        r.raise_for_status()
        d = r.json()
        if isinstance(d, list):
            d = d[0] if d else None
        return d
    except Exception:
        return None


def revisar_estructura_mercados() -> dict:
    """Diff de description/resolutionSource/feeSchedule/rewards por
    (activo, marco) contra el snapshot de ayer. Fuente que SÍ habría
    detectado el cambio TWAP del 07-Ago."""
    anterior_completo = {}
    if ESTRUCTURA_STATE.exists():
        try:
            anterior_completo = json.loads(ESTRUCTURA_STATE.read_text(encoding="utf-8"))
        except Exception:
            anterior_completo = {}
    # BUG real encontrado y arreglado en pruebas 09-Ago: `anterior_completo`
    # es {"mercados": {...}, "actualizado": ...} -- comparar contra
    # anterior_completo.get(clave) directamente (sin bajar a "mercados")
    # siempre daba None, así que NINGÚN cambio se detectaba nunca. Probado
    # con un cambio simulado antes de confiar en el script.
    anterior = anterior_completo.get("mercados", {})

    actual = {}
    cambios = []
    for activo, marco, slug_prefix in COMBOS:
        clave = f"{activo}#{marco}"
        mid = _buscar_market_id(activo, slug_prefix, marco)
        if mid is None:
            _log(f"WARN sin mercado abierto encontrado para {clave}, saltado")
            continue
        m = _fetch_market(mid)
        if m is None:
            _log(f"WARN fetch de mercado falló para {clave} (id={mid})")
            continue
        snapshot = {c: m.get(c) for c in CAMPOS_VIGILADOS}
        actual[clave] = snapshot

        prev = anterior.get(clave)
        if prev is not None and prev != snapshot:
            diffs = {c: (prev.get(c), snapshot.get(c)) for c in CAMPOS_VIGILADOS if prev.get(c) != snapshot.get(c)}
            cambios.append({"combo": clave, "diffs": diffs})

    primera_vez = not anterior
    ESTRUCTURA_STATE.write_text(json.dumps({
        "mercados": actual,
        "actualizado": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    if primera_vez:
        _log(f"estructura mercados: primera ejecución, baseline sembrado ({len(actual)} combos, sin aviso)")
        return {"cambio": False, "cambios": []}

    return {"cambio": bool(cambios), "cambios": cambios}


def main() -> int:
    from shadow_digest import enviar_telegram

    _log("=== inicio ===")
    r_changelog = revisar_changelog_oficial()
    r_estructura = revisar_estructura_mercados()

    partes = []
    if r_changelog and r_changelog.get("cambio"):
        partes.append("📰 *Changelog oficial de Polymarket actualizado*\n"
                       + (r_changelog["nuevo_fragmento"] or "(ver docs.polymarket.com/changelog/predictions)"))

    if r_estructura.get("cambio"):
        lineas = ["🔧 *Cambio estructural detectado en mercados que operamos*"]
        for c in r_estructura["cambios"]:
            lineas.append(f"\n*{c['combo']}*:")
            for campo, (antes, despues) in c["diffs"].items():
                lineas.append(f"  {campo}: `{str(antes)[:150]}` -> `{str(despues)[:150]}`")
        partes.append("\n".join(lineas))

    if partes:
        mensaje = "🚨 VIGÍA actualizaciones Polymarket -- cambios detectados hoy:\n\n" + "\n\n---\n\n".join(partes)
        mensaje = mensaje[:3900]  # límite Telegram
        ok = enviar_telegram(mensaje)
        _log(f"aviso enviado (telegram={ok})")
    else:
        _log("sin cambios nuevos hoy (changelog oficial + estructura de mercados)")

    _log("=== fin ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
