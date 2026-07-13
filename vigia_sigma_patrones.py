#!/usr/bin/env python3
"""Vigía sigma_* (13-Jul, petición Javi): rastrea CUALQUIER filtro_causal o
patrón_ganador cuya feature empiece por "sigma_" (sigma_h, sigma_ewma_delta_pct,
o cualquier variante futura) en TODAS las claves de strategy_params.json —
no una lista fija de moneda/horizonte, sino cada key que el postmortem genere
(GBM_LATE_15M, _TARDIO, _ESPACIO_ATR, UPDOWN_GBM, PRICE_TARGET_GBM, por
activo y por agregado, lo que exista hoy o se añada mañana).

Contexto: sesión 13-Jul confirmó con rigor (permutación, split temporal,
cross-asset) que sigma_ewma_delta_pct es señal real en GBM_LATE_15M y se
promocionó a mano en ETH; sigma_h (nivel bruto, no el delta) se probó y
resultó NO estable entre regímenes (signo se invierte 06-08Jul vs 09-13Jul).
Este vigía no decide nada — solo evita que un patrón sigma_* nuevo con n
grande pase desapercibido en una clave que nadie está mirando activamente.

Fail-safe existente (_es_par_live_protegido, shadow_predict.py/live_trade.py)
ya impide que estos patrones salten o rehabiliten señales de pares live
(SOL/ETH#15min BUY_YES) sin promoción manual — este script es una capa de
visibilidad adicional (CAPA 2), no de control. Read-only: solo lee
strategy_params.json y config_live.json, nunca escribe en datos de dinero real.

Umbral de aviso por Telegram: n>=GATE_N_AVISO (mismo listón que la promoción
a live, min_n_para_live=40) para no generar ruido con hallazgos pequeños que
ya se ven en `strategy_params.json` directamente. Todo lo que cruce
N_BUCKET_MIN (15, el propio umbral del postmortem para generar el patrón)
se registra en el latch aunque no llegue a avisar, para que la primera
ejecución no dispare un aluvión de mensajes por el histórico ya acumulado.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

PARAMS = REPO / "data/shadow/strategy_params.json"
CONFIG_LIVE = REPO / "data/live/config_live.json"
LATCH = REPO / "data/live/vigia_sigma_patrones_latch.json"
GATE_N_AVISO = 40


def _firma(clave: str, tipo: str, f: dict) -> str:
    return f"{clave}|{tipo}|{f.get('feature')}|{f.get('condicion')}|{f.get('umbral')}|{f.get('direccion')}"


def _n_de(f: dict, tipo: str) -> int:
    return f.get("n_patron", 0) if tipo == "patron" else f.get("n_malo", 0)


def _ic_de(f: dict, tipo: str) -> float | None:
    return f.get("ic_patron") if tipo == "patron" else f.get("ic_malo")


def main() -> int:
    from shadow_digest import enviar_telegram

    if not PARAMS.exists():
        print("[vigia_sigma_patrones] sin strategy_params.json")
        return 0
    try:
        sp = json.loads(PARAMS.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[vigia_sigma_patrones] strategy_params.json ilegible: {e}")
        return 0
    estrategias = sp.get("estrategias", sp)

    try:
        pares_live = set(json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
                          .get("pares_permitidos_live", []))
    except Exception:
        pares_live = set()

    latch = {}
    if LATCH.exists():
        try:
            latch = json.loads(LATCH.read_text())
        except Exception:
            latch = {}
    es_primera_ejecucion = not latch
    vistos = set(latch.get("_vistos", []))

    nuevos_avisar = []
    total_sigma = 0
    for clave, entry in estrategias.items():
        if not isinstance(entry, dict):
            continue
        for tipo, campo in (("filtro", "filtros_causales"), ("patron", "patrones_ganadores")):
            for f in entry.get(campo, []) or []:
                feature = f.get("feature") or ""
                if not feature.startswith("sigma_"):
                    continue
                total_sigma += 1
                firma = _firma(clave, tipo, f)
                if firma in vistos:
                    continue
                vistos.add(firma)
                n = _n_de(f, tipo)
                if n < 15:
                    continue  # por debajo del propio umbral del postmortem, ruido
                tupla_live = f"{clave}#{f.get('direccion')}"
                es_live = tupla_live in pares_live
                nuevos_avisar.append((clave, tipo, f, n, es_live))

    print(f"[vigia_sigma_patrones] claves_totales={len(estrategias)} "
          f"entradas_sigma_vistas={total_sigma} nuevas={len(nuevos_avisar)} "
          f"primera_ejecucion={es_primera_ejecucion}")

    # Primera ejecución: sembrar el latch en silencio (evita aluvión con el
    # histórico ya acumulado), igual que vigia_filtro_gbmlate.py.
    if not es_primera_ejecucion:
        for clave, tipo, f, n, es_live in nuevos_avisar:
            if n < GATE_N_AVISO:
                continue
            ic = _ic_de(f, tipo)
            etiqueta = "🔴 PAR LIVE (bloqueado por fail-safe, no se aplica solo)" if es_live else "shadow"
            msg = (
                f"🔎 VIGÍA sigma_*: nuevo {tipo} en {clave}\n"
                f"feature={f.get('feature')} {f.get('condicion')} {f.get('umbral')} "
                f"dir={f.get('direccion')} ic={ic:+.4f} n={n}\n"
                f"{etiqueta}\n"
                f"Antes de promocionar: permutación + split temporal + coherencia "
                f"cross-asset (mismo rigor que sigma_ewma_delta_pct#ETH 13-Jul)."
            )
            ok = enviar_telegram(msg)
            print(f"[vigia_sigma_patrones] aviso enviado {clave}#{tipo} (telegram={ok})")

    latch["_vistos"] = sorted(vistos)
    LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_sigma_patrones] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
