#!/usr/bin/env python3
"""vigia_quirurgico_arquetipo_b.py -- (22-Sep, petición explícita Javi tras
la sesión de filtrar los 243 hallazgos del edge quirúrgico universal por
Arquetipo B): aviso diario de cómo evolucionan las zonas Arquetipo B
(coin-específico / correlado con ballenas -- ver project_dos_patrones_
edge_bandera_21jul, fill-ability típica 33-69% frente al 6-36% del
Arquetipo A) para decidir con datos si tras 3 días consecutivos operables
se repite el intento de saltar a live.

FAMILIAS_B: clasificación manual, no automática -- ver el docstring de
cada familia en shadow_predict.py/CLAUDE.md antes de añadir una nueva:
  - FAVORITO_CONFIRMADO(*): compra el favorito ya confirmado por el mercado.
  - BALLENAS_TARDIAS / BALLENAS_CONFIRMADAS_15M: decide directamente de
    posicionamiento de ballenas en tiempo real.
  - WALLET_MIRROR / SNIPER / DISPERSO / WEEKLY_TEMPRANO / WEEKLY_TARDIO:
    replican wallets con edge probado (P-GALLINA), Arquetipo B por
    construcción.
  - MOMENTUM_IBS_*_BALLENA: gateada por actividad de ballena real (ver
    shadow_predict.py:3765, "variantes gateadas por actividad de ballena
    real"), no modelo puro.
  - LIQUIDACIONES_5M/15M/60M: evento de mercado real (cascada de
    liquidaciones), no predicción de modelo.
NO están en FAMILIAS_B (Arquetipo A, modelo propio, excluidas a propósito):
GBM_LATE* (todas variantes), UPDOWN_GBM*, ORDER_FLOW_5M, LEADLAG_BTC_XRP_15M,
RESOLUTION_SNIPER, CANDIDATA9/10 (bot_consenso, mixta -- no clasificada
todavía, se deja fuera hasta revisar).

Fuente: data/shadow/edge_quirurgico_historial.jsonl (ya poblado por
edge_quirurgico_rolling.py cada ~12h, sin cambios aquí). Reporta, para cada
zona Arquetipo B vista en el historial: días operable, si acaba de cruzar
3 días consecutivos (aviso especial), y snapshot del día actual.

Corre 1 vez al día (cron, ver docstring de despliegue). No toca gates,
config ni ejecutores -- MODO LECTURA, mismo criterio que el resto de
edge_quirurgico_rolling.py."""
import collections
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

HISTORIAL = REPO / "data" / "shadow" / "edge_quirurgico_historial.jsonl"
ZONAS = REPO / "data" / "shadow" / "edge_quirurgico_zonas.json"
LATCH = REPO / "data" / "shadow" / "vigia_quirurgico_arquetipo_b_latch.json"

FAMILIAS_B = {
    "FAVORITO_CONFIRMADO", "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION",
    "FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION", "FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA",
    "FAVORITO_CONFIRMADO_DEPTH_FASE0",
    "BALLENAS_TARDIAS", "BALLENAS_CONFIRMADAS_15M",
    "WALLET_MIRROR", "SNIPER", "DISPERSO", "WEEKLY_TEMPRANO", "WEEKLY_TARDIO",
    "MOMENTUM_IBS_5M_BALLENA", "MOMENTUM_IBS_15M_BALLENA",
    "LIQUIDACIONES_5M", "LIQUIDACIONES_15M", "LIQUIDACIONES_60M",
}
N_DIAS_OBJETIVO = 3


def _clave_zona(r: dict) -> tuple:
    return (r["tupla"], r["ancho"], r["lo"], r["hi"])


def _etiqueta(k: tuple) -> str:
    tupla, ancho, lo, hi = k
    return f"{tupla} w={ancho} [{lo:.2f},{hi:.2f})"


def _persistencia_por_dia() -> dict:
    """clave_zona -> {fecha: forward_ok bool}, solo familias B."""
    por_zona = collections.defaultdict(dict)
    if not HISTORIAL.exists():
        return por_zona
    for linea in HISTORIAL.read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(linea)
        except Exception:
            continue
        if r.get("familia") not in FAMILIAS_B:
            continue
        por_zona[_clave_zona(r)][r["fecha"]] = bool(r.get("forward_ok"))
    return por_zona


def _texto_diario(por_zona: dict, latch: dict) -> tuple:
    """Devuelve (texto, nuevos_3_dias: set de claves que cruzan HOY)."""
    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    confirmadas_antes = set(tuple(k) for k in latch.get("cruzaron_3_dias", []))
    activas, nuevos_3d = [], set()
    for k, dias in por_zona.items():
        n_ok = sum(1 for v in dias.values() if v)
        if n_ok == 0:
            continue
        activas.append((k, n_ok, sorted(dias)))
        if n_ok >= N_DIAS_OBJETIVO and k not in confirmadas_antes:
            nuevos_3d.add(k)
    activas.sort(key=lambda x: -x[1])

    lin = [f"🔬🐋 Quirúrgico Arquetipo B -- evolución diaria ({hoy} UTC)",
           f"zonas vistas con >=1 día operable: {len(activas)} | objetivo: {N_DIAS_OBJETIVO} días consecutivos"]
    if nuevos_3d:
        lin.append(f"\n🎯 {len(nuevos_3d)} zona(s) CRUZAN {N_DIAS_OBJETIVO} días operable HOY -- candidatas a replantear el salto a live:")
        for k in sorted(nuevos_3d):
            lin.append(f"  🟢🟢🟢 {_etiqueta(k)} ({por_zona[k]})")
    lin.append(f"\nTop zonas por días operable:")
    for k, n_ok, fechas in activas[:20]:
        marca = "🎯" if n_ok >= N_DIAS_OBJETIVO else ("🟡" if n_ok == 2 else "🟢")
        lin.append(f"  {marca} {_etiqueta(k)} -- {n_ok} día(s) operable ({fechas[-1]})")
    if len(activas) > 20:
        lin.append(f"  … +{len(activas) - 20} zona(s) más")
    return "\n".join(lin), nuevos_3d


def _enviar_partido(enviar, texto: str, limite: int = 3500) -> bool:
    trozos, actual = [], ""
    for linea in texto.split("\n"):
        if len(actual) + len(linea) + 1 > limite and actual:
            trozos.append(actual); actual = ""
        actual += linea + "\n"
    if actual:
        trozos.append(actual)
    return all([enviar(t.rstrip("\n")) for t in trozos])


def main() -> int:
    por_zona = _persistencia_por_dia()
    try:
        latch = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        latch = {}

    if not por_zona:
        print("[vigia_quirurgico_arquetipo_b] sin historial Arquetipo B todavía")
        return 0

    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if latch.get("ultimo_envio") == hoy:
        print("[vigia_quirurgico_arquetipo_b] ya enviado hoy")
        return 0

    texto, nuevos_3d = _texto_diario(por_zona, latch)
    try:
        from shadow_digest import enviar_telegram
        ok = _enviar_partido(lambda t: enviar_telegram(t, bot="cripto"), texto)
    except Exception as e:
        print(f"[vigia_quirurgico_arquetipo_b] no se pudo enviar Telegram: {type(e).__name__}: {e}")
        ok = False

    if ok:
        cruzaron = set(tuple(k) for k in latch.get("cruzaron_3_dias", [])) | nuevos_3d
        latch["cruzaron_3_dias"] = [list(k) for k in cruzaron]
        latch["ultimo_envio"] = hoy
        LATCH.write_text(json.dumps(latch, ensure_ascii=False), encoding="utf-8")
    print(f"[vigia_quirurgico_arquetipo_b] enviado={ok} zonas_activas={len(por_zona)} nuevos_3dias={len(nuevos_3d)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
