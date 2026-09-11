#!/usr/bin/env python3
"""Vigía (21-Jul, petición Javi): revisa cuándo UPDOWN_GBM#{BTC,ETH}#15min#
BUY_YES con filtro ibs_15>umbral alcanzan n>=40 en el canal REALMENTE
fillable (no shadow puro) -- ver idea_ibs_updowngbm_hallazgo_21jul.md para
el análisis completo. Hoy (21-Jul) BTC tenía n=19/43 y ETH n=3/8 en ese
canal -- lejos del n>=40 que exige el proyecto antes de promocionar.

Reusa _resultado_idx()/fillable_rows()/ic_bayes() de analisis_ic_fillable.py
tal cual (mismo proxy candidato_evaluacion+ratio_vs_stake>=5x que ya usa el
resto del sistema) -- solo añade el filtro ibs_15 y el aviso Telegram
cuando cruza el umbral, con latch para no repetir aviso cada ciclo.

Solo lectura -- no promociona nada, no toca pares_permitidos_live ni
ninguna decisión. Cron sugerido: cada 30-60min (el dato crece despacio).
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from analisis_ic_fillable import _resultado_idx, fillable_rows, ic_bayes  # noqa: E402

LATCH_PATH = REPO / "data" / "shadow" / "vigia_ibs_updowngbm_latch.json"
N_MIN_PROMOCION = 40

TUPLAS = [
    ("UPDOWN_GBM", "BTC#15min", "BUY_YES", 0.7019),
    ("UPDOWN_GBM", "ETH#15min", "BUY_YES", 0.7738),
]


def _fillable_ibs(strategy: str, subtype: str, decision: str, th: float) -> dict:
    idx = _resultado_idx(strategy, subtype, decision)
    fr = fillable_rows(strategy, subtype, decision, idx)
    con_ibs = []
    for r in fr:
        if not r.get("features"):
            continue
        try:
            feat = json.loads(r["features"])
        except Exception:
            continue
        if "ibs_15" in feat:
            con_ibs.append((r, feat["ibs_15"]))
    hi = [(r, v) for r, v in con_ibs if v > th]
    n_hi = len(hi)
    aciertos = sum(int(r["acierto"]) for r, _ in hi)
    ic, conf, ic_ef = ic_bayes(aciertos, n_hi) if n_hi else (None, None, None)
    return {"n_fillable_total": len(fr), "n_ibs_alto": n_hi,
            "hit_pct": round(100 * aciertos / n_hi, 1) if n_hi else None,
            "ic_efectivo": ic_ef}


def main() -> int:
    latch = json.loads(LATCH_PATH.read_text()) if LATCH_PATH.exists() else {}
    avisos = []
    for strategy, subtype, decision, th in TUPLAS:
        clave = f"{strategy}#{subtype}#{decision}#ibs>{th}"
        r = _fillable_ibs(strategy, subtype, decision, th)
        print(f"[vigia_ibs_updowngbm] {clave}: n_ibs_alto={r['n_ibs_alto']} "
              f"(de {r['n_fillable_total']} fillable total) hit={r['hit_pct']} ic_ef={r['ic_efectivo']}")
        if r["n_ibs_alto"] >= N_MIN_PROMOCION and not latch.get(clave):
            avisos.append(
                f"🎯 {clave} alcanzó n={r['n_ibs_alto']} en canal fillable real "
                f"(hit={r['hit_pct']}% ic_efectivo={r['ic_efectivo']:+.3f}) -- "
                f"listo para re-evaluar promoción a live (ver idea_ibs_updowngbm_hallazgo_21jul.md)."
            )
            latch[clave] = True

    if avisos:
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram("\n".join(avisos))
        except Exception as e:
            print(f"[vigia_ibs_updowngbm] no se pudo notificar Telegram: {e}")
        LATCH_PATH.write_text(json.dumps(latch, indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
