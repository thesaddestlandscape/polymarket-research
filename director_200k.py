#!/usr/bin/env python3
"""director_200k.py -- "Parte B: dirige y masteriza" (28-Sep, petición explícita
Javi: "una estrategia... que se dedique a buscar ineficiencias de nuestras
estrategias e hipótesis y las dirija y masterice a ganar pasta pase lo que
pase, con la única visión de alcanzar los objetivos y misiones de este
proyecto"). MODO LECTURA -- no toca dinero, no conecta nada solo.

No reinventa detección: agrega en UN informe priorizado por impacto €
estimado lo que YA detectan mecanismos existentes, cada uno con su propio
rigor ya construido:
  - shadow_pnl_fiel.py (pnl_fiel_por_estrategia.json): tuplas del shadow con
    edge fiel positivo (fill-ability real, Kelly real, circuit breakers
    reales) que TODAVÍA no están en pares_permitidos_live.
  - vigia_log_growth.py (vigia_log_growth_latch.json): tuplas YA en
    pares_permitidos_live con crecimiento logarítmico negativo (payout
    inverso) sin que nadie haya decidido pausar/mantener.
  - buscador_edge_perdido.py (buscador_edge_perdido.json): tuplas
    degradadas cuyo edge se movió a una franja concreta (hora/día), ya
    forward-validada.

Cada fila lleva SIEMPRE los caveats de la fuente que la generó -- nunca se
presenta un número como concluyente por sí solo (mismo criterio que
CLAUDE.md pt.23: "el número por tupla individual es orientativo con n bajo,
no concluyente, hasta gate riguroso propio"). Ninguna acción se ejecuta
aquí -- cada fila es una PROPUESTA para decidir con Javi, no una promoción.

Salida: data/shadow/director_200k.json + informe por stdout (Telegram vía
vigía propio, pendiente de decidir si se añade a cron).
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
CONFIG_LIVE = REPO / "data/live/config_live.json"
PNL_FIEL = REPO / "data/shadow/pnl_fiel_por_estrategia.json"
LOG_GROWTH_LATCH = REPO / "data/live/vigia_log_growth_latch.json"
BUSCADOR = REPO / "data/shadow/buscador_edge_perdido.json"
OUT = REPO / "data/shadow/director_200k.json"

N_MIN_PNL_FIEL = 15
TOP_N = 10

# 28-Sep: estrategias con un hueco de integridad ya documentado en CLAUDE.md
# (protocolo pt.2, "claves de features fantasma") -- pnl_fiel positivo en
# estas NO es evidencia limpia hasta re-verificar que sus features existen
# de verdad en shadow_predict.py. Lista corta, a mano -- extender aquí
# cuando el barrido de salud encuentre otra.
SOSPECHOSAS_INTEGRIDAD = {"GBM_LATE_15M_MULTIHORIZONTE"}


def _cargar(p):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def seccion_pnl_fiel_sin_conectar(vivos: set) -> list[dict]:
    d = _cargar(PNL_FIEL)
    if not d:
        return []
    ests = d.get("estrategias", {})
    out = []
    for tupla_str, v in ests.items():
        pnl = v.get("pnl_fiel_eur_sin_suelo")
        n = v.get("n_ejecutado", 0)
        if pnl is None or n < N_MIN_PNL_FIEL or pnl <= 0:
            continue
        if tupla_str in vivos:
            continue
        strategy = v.get("strategy", tupla_str.split("#")[0])
        out.append({
            "tupla": tupla_str,
            "pnl_fiel_eur_sin_suelo": round(pnl, 2),
            "n_ejecutado": n,
            "fill_rate": v.get("fill_rate"),
            "sospechosa_integridad": strategy in SOSPECHOSAS_INTEGRIDAD,
            "accion": "candidata a checklist de 6 categorías + gate riguroso propio antes de promocionar"
                       + (" -- ANTES verificar features reales (protocolo pt.2)" if strategy in SOSPECHOSAS_INTEGRIDAD else ""),
        })
    out.sort(key=lambda x: -x["pnl_fiel_eur_sin_suelo"])
    return out[:TOP_N]


def seccion_payout_inverso_sin_decidir(vivos: set) -> list[dict]:
    d = _cargar(LOG_GROWTH_LATCH)
    if not d:
        return []
    out = []
    for tupla_str, v in d.items():
        if not v.get("avisado") or tupla_str not in vivos:
            continue
        growth = v.get("growth")
        if growth is None or growth >= 0:
            continue
        out.append({
            "tupla": tupla_str,
            "n": v.get("n"),
            "growth_g_f10pct": round(growth, 6),
            "ev_por_dolar": v.get("ev_por_dolar"),
            "accion": "SIGUE EN pares_permitidos_live con payout inverso avisado -- decisión de Javi pendiente (pausar o mantener con más n)",
        })
    out.sort(key=lambda x: x["growth_g_f10pct"])
    return out


def seccion_buscador_edge_perdido() -> list[dict]:
    d = _cargar(BUSCADOR)
    if not d:
        return []
    out = []
    for tupla_str, info in d.get("tuplas", {}).items():
        for dim, cands in info.get("dimensiones", {}).items():
            for c in cands:
                if not c.get("forward_ok"):
                    continue
                out.append({
                    "tupla": tupla_str, "dimension": dim, "bucket": c["bucket"],
                    "pnl_train": c.get("pnl_train"), "pnl_test": c.get("pnl_test"),
                    "n_test": c.get("n_test"),
                    "accion": f"edge movido a {dim}={c['bucket']} (forward-validado) -- proponer filtro/reenfoque",
                })
    return out


def main() -> int:
    ahora = datetime.now(timezone.utc)
    try:
        cfg = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
        vivos = set(cfg.get("pares_permitidos_live", []))
    except Exception:
        vivos = set()

    pnl_fiel_secc = seccion_pnl_fiel_sin_conectar(vivos)
    payout_secc = seccion_payout_inverso_sin_decidir(vivos)
    buscador_secc = seccion_buscador_edge_perdido()

    salida = {
        "generado_utc": ahora.isoformat(timespec="seconds"),
        "n_tuplas_live_hoy": len(vivos),
        "pnl_fiel_sin_conectar_top": pnl_fiel_secc,
        "pnl_fiel_sin_conectar_suma_top": round(sum(x["pnl_fiel_eur_sin_suelo"] for x in pnl_fiel_secc), 2),
        "payout_inverso_sin_decidir": payout_secc,
        "buscador_edge_perdido_forward_ok": buscador_secc,
        "caveats": [
            "pnl_fiel: no modela CLV/discrepancia entre tuplas/streak_cooldown/abort_requote/fok_kill (ver cabecera shadow_pnl_fiel.py) -- orientativo con n bajo",
            "ninguna fila de este informe es una promoción -- checklist de 6 categorías + /code-review + OK Javi sigue siendo obligatorio",
        ],
    }
    OUT.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"[director_200k] {len(vivos)} tuplas live hoy")
    print(f"\n== PARTE B: edge propio sin conectar (pnl_fiel real, top {TOP_N}) ==")
    for x in pnl_fiel_secc:
        flag = " ⚠️ SOSPECHOSA (ver protocolo pt.2)" if x["sospechosa_integridad"] else ""
        print(f"  {x['tupla']}: +{x['pnl_fiel_eur_sin_suelo']}€ (n={x['n_ejecutado']}, "
              f"fill={x['fill_rate']}){flag}")
    print(f"  suma top {TOP_N}: {salida['pnl_fiel_sin_conectar_suma_top']}€ (techo orientativo, no sumable sin más rigor)")

    print(f"\n== PARTE B: payout inverso live sin decidir ({len(payout_secc)}) ==")
    for x in payout_secc:
        print(f"  {x['tupla']}: g={x['growth_g_f10pct']} n={x['n']} -- {x['accion']}")

    print(f"\n== PARTE B: edge perdido con hallazgo forward-validado ({len(buscador_secc)}) ==")
    for x in buscador_secc:
        print(f"  {x['tupla']} | {x['accion']}")

    print(f"\nGuardado en {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
