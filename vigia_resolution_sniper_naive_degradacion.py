#!/usr/bin/env python3
"""vigia_resolution_sniper_naive_degradacion.py — 22-Sep, petición
explícita Javi tras la promoción a live de RESOLUTION_SNIPER_NAIVE
5min+15min el mismo día ("esta tupla no se degrada no? ponle un observer
que me avise por telegram si empieza a degradarse").

Reusa cargar_naive()/RATIO_FILLABLE_MIN/pnl_trade de analisis_gate_
riguroso_resolution_sniper_naive_depth_19ago.py (import, no reimplementar
el join market_id -> outcome_real). Segmentado por (activo,marco)
-- CLAUDE.md pt.17, nunca agregado.

Método (ventana rodante, mismo espíritu que edge_quirurgico_rolling.py):
sobre el subconjunto FILLABLE (ratio_implicita_vs_stake>=5x, el mismo
filtro que usa el ejecutor real), compara los últimos FORWARD_DIAS
("recientes") con TODO lo anterior ("baseline"). Degradado = ventana
reciente con n>=N_MIN y CUALQUIERA de: (a) pnl_medio reciente<=PISO_EUR;
(b) wilson90lo reciente < ask_medio reciente (el hit-rate real ya no
cubre ni el breakeven implícito); (c) pnl_medio reciente cae por debajo
de la MITAD del pnl_medio del baseline con baseline n>=N_MIN (declive
relativo claro aunque siga nominalmente positivo y por encima de
breakeven -- lo que (a)/(b) solos no detectan). Latch por (activo,marco):
solo avisa por Telegram en la TRANSICIÓN ok->degradado o
degradado->recuperado, nunca repite el mismo estado (mismo patrón que
vigia_gate_bucket_propio.py/vigia_log_growth.py).

MODO LECTURA. No toca gate_bucket, whitelist ni ejecutor -- solo avisa.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_gate_riguroso_resolution_sniper_naive_depth_19ago import (  # noqa: E402
    cargar_naive, wilson_lower, RATIO_FILLABLE_MIN,
)

N_MIN = 15
FORWARD_DIAS = 7
PISO_EUR = 0.0
LATCH = REPO / "data/live/vigia_resolution_sniper_naive_degradacion_latch.json"
OUT = REPO / "data/shadow/resolution_sniper_naive_degradacion.json"


def _cargar_latch() -> dict:
    try:
        return json.loads(LATCH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _guardar_latch(d: dict) -> None:
    LATCH.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")


def main() -> int:
    from shadow_digest import enviar_telegram

    filas = [f for f in cargar_naive() if f["ratio"] is not None and f["ratio"] >= RATIO_FILLABLE_MIN]
    if not filas:
        print("Sin filas fillable todavía.")
        return 0

    fechas = sorted({f["ts"][:10] for f in filas if f["ts"]})
    if len(fechas) < 2:
        print("Historial de días insuficiente para ventana rodante todavía.")
        return 0
    cutoff = fechas[-1]
    dias_recientes = fechas[-FORWARD_DIAS:]
    cutoff_ini = dias_recientes[0]

    grupos = defaultdict(list)
    for f in filas:
        grupos[(f["activo"], f["marco"])].append(f)

    latch_previo = _cargar_latch()
    latch_nuevo = {}
    avisos = []
    resumen = {}

    for (activo, marco), fs in sorted(grupos.items()):
        clave = f"{activo}#{marco}"
        recientes = [f for f in fs if f["ts"][:10] >= cutoff_ini]
        anteriores = [f for f in fs if f["ts"][:10] < cutoff_ini]
        n_rec = len(recientes)
        if n_rec < N_MIN:
            resumen[clave] = {"estado": "n_insuficiente", "n_reciente": n_rec}
            latch_nuevo[clave] = latch_previo.get(clave, "ok")
            continue
        hits_rec = sum(1 for f in recientes if f["acierto"])
        pnl_rec = sum(f["pnl"] for f in recientes) / n_rec
        ask_medio_rec = sum(f["ask"] for f in recientes) / n_rec
        wl_rec = wilson_lower(hits_rec, n_rec)
        n_base = len(anteriores)
        pnl_base = (sum(f["pnl"] for f in anteriores) / n_base) if n_base >= N_MIN else None
        declive_relativo = (
            pnl_base is not None and pnl_base > 0 and pnl_rec < pnl_base * 0.5
        )
        degradado = pnl_rec <= PISO_EUR or wl_rec < ask_medio_rec or declive_relativo
        estado = "degradado" if degradado else "ok"
        resumen[clave] = {
            "estado": estado, "n_reciente": n_rec, "hit_reciente": round(hits_rec / n_rec, 3),
            "wilson90lo_reciente": round(wl_rec, 3), "ask_medio_reciente": round(ask_medio_rec, 3),
            "pnl_medio_reciente": round(pnl_rec, 4), "dias_ventana": f"{cutoff_ini}..{cutoff}",
            "n_baseline": n_base, "pnl_medio_baseline": round(pnl_base, 4) if pnl_base is not None else None,
            "declive_relativo": declive_relativo,
        }
        estado_previo = latch_previo.get(clave, "ok")
        if estado != estado_previo:
            if estado == "degradado":
                motivos = []
                if pnl_rec <= PISO_EUR:
                    motivos.append("pnl_medio<=0")
                if wl_rec < ask_medio_rec:
                    motivos.append("wilson90lo<breakeven")
                if declive_relativo:
                    motivos.append(f"pnl cae >50% vs baseline ({pnl_base:+.3f}€, n={n_base})")
                avisos.append(
                    f"🔻 {clave} DEGRADADO [{', '.join(motivos)}]: n={n_rec} hit={hits_rec/n_rec:.1%} "
                    f"wilson90lo={wl_rec:.3f} (breakeven implícito ~{ask_medio_rec:.3f}) "
                    f"pnl/tr={pnl_rec:+.3f}€ (ventana {cutoff_ini}..{cutoff})"
                )
            else:
                avisos.append(
                    f"🟢 {clave} recuperado: n={n_rec} hit={hits_rec/n_rec:.1%} "
                    f"wilson90lo={wl_rec:.3f} pnl/tr={pnl_rec:+.3f}€ (ventana {cutoff_ini}..{cutoff})"
                )
        latch_nuevo[clave] = estado

    OUT.write_text(json.dumps({"generado_hasta": cutoff, "ventana": f"{cutoff_ini}..{cutoff}",
                                "resumen": resumen}, ensure_ascii=False, indent=1), encoding="utf-8")

    n_deg = sum(1 for v in resumen.values() if v["estado"] == "degradado")
    print(f"[{cutoff}] {len(resumen)} combos evaluados, {n_deg} degradados, "
          f"{sum(1 for v in resumen.values() if v['estado']=='n_insuficiente')} con n insuficiente todavía")
    for clave, v in sorted(resumen.items()):
        print(f"  {clave:16} {v['estado']}")

    if avisos:
        msg = "🎯 RESOLUTION_SNIPER_NAIVE — cambios de estado (ventana %s):\n" % f"{cutoff_ini}..{cutoff}" \
              + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin cambios de estado.")

    _guardar_latch(latch_nuevo)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_resolution_sniper_naive_degradacion] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
