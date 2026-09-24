#!/usr/bin/env python3
"""vigia_sports_fade_extremas_forward.py -- validación FORWARD (fuera de muestra
real) de 3 hipótesis de FADE de wallets de sports con edge muy negativo,
CONGELADAS el 24-Sep (cutoff abajo, NO se reescriben solas). Petición Javi
24-Sep: "tenemos que sacarle pasta a eso".

Por qué forward y no el resultado de hoy: el barrido retrospectivo
(analisis_sports_fade_wallets_extremas_24sep.py) miró 4 tramos x ~7 zonas
de precio; la mejor celda (p=0,010) no sobrevive a Bonferroni (~0,28). Solo
cuenta lo que pase DESPUÉS de fijar las hipótesis.

Unidad = primer disparo FADE fillable (ask real, ratio>=5x) por
(mercado, lado) del dry-run del sniper (mismo cargar() del análisis).
Veredicto por hipótesis:
  confirmado_forward: n>=40, >=10 días, wallet top<=30 %, pnl/tr>=0,10 €,
                      CI90 bootstrap por DÍAS >0 y ambas mitades >0
  refutado_forward:   n>=40 y CI90 por días entero <0
  sin_concluir:       resto
Salida data/sports/fade_extremas_forward.json; Telegram (bot sports) solo
cuando cambia un veredicto (latch). Solo lectura, no toca nada operativo --
pasar a dinero real exige además el checklist de 6 categorías + OK de Javi.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import analisis_sports_fade_wallets_extremas_24sep as base  # noqa: E402

CUTOFF = "2026-09-24T08:00:00"
OUT = REPO / "data/sports/fade_extremas_forward.json"
LATCH = REPO / "data/live/vigia_sports_fade_extremas_forward_latch.json"

HIPOTESIS = {
    "H1_peores_todas": lambda u: u["tramo"] == "<=-40pp",
    "H2_malas_ask_020_030": lambda u: u["tramo"] == "(-20,-10]" and 0.20 <= u["ask"] < 0.30,
    "H3_peores_longshot_ask_lt_050": lambda u: u["tramo"] == "<=-40pp" and u["ask"] < 0.50,
}


def veredicto(d: dict) -> str:
    n = d.get("n_unidades", 0)
    ci = d.get("ci90_bootstrap_dia")
    if n < 40 or not ci:
        return "sin_concluir"
    if ci[1] < 0:
        return "refutado_forward"
    sh = d.get("split_half") or [0, 0]
    if (d["n_dias"] >= 10 and d["top_wallet_pct"] <= 0.30 and d["pnl_medio"] >= 0.10
            and ci[0] > 0 and min(sh) > 0):
        return "confirmado_forward"
    return "sin_concluir"


def main() -> int:
    us = [u for u in base.cargar() if u["ts"] >= CUTOFF]
    for u in us:
        u["pnl"] = base.payout_win(u["ask"]) if u["acierto"] else -base.STAKE
        u["tramo"] = base.tramo(u["edge"])
    us = [u for u in us if u["tramo"]]
    res = {}
    for i, (nombre, filtro) in enumerate(HIPOTESIS.items()):
        d = base.resumen(nombre, [u for u in us if filtro(u)], 500 + i)
        d["veredicto"] = veredicto(d)
        res[nombre] = d
    salida = {"actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "cutoff": CUTOFF, "n_unidades_fade_forward": len(us), "hipotesis": res}
    OUT.write_text(json.dumps(salida, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(salida, ensure_ascii=False))

    try:
        latch = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        latch = {}
    cambios = [f"{h}: {latch.get(h, '—')} → {d['veredicto']} (n={d.get('n_unidades', 0)}, "
               f"pnl/tr={d.get('pnl_medio', 0):+.3f}€, CI90d={d.get('ci90_bootstrap_dia')})"
               for h, d in res.items() if latch.get(h) != d["veredicto"] and h in latch
               or (h not in latch and d["veredicto"] != "sin_concluir")]
    if cambios:
        from shadow_digest import enviar_telegram
        enviar_telegram("🏟 FADE wallets extremas sports (forward desde 24-Sep):\n" + "\n".join(cambios),
                        bot="sports")
    LATCH.write_text(json.dumps({h: d["veredicto"] for h, d in res.items()}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
