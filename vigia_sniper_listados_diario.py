#!/usr/bin/env python3
"""vigia_sniper_listados_diario.py -- informe DIARIO por Telegram (29-Sep,
Javi: "ponme un aviso diario") de sniper_listados_fase0.py (ronda3 #7):
mercados recién listados, ¿cuánto tardan en tener cotización a dos lados y
hay edge al comprar al ask inicial frente al precio justo? SIEMPRE envía.
Cron 09:05 UTC. Solo observación."""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))


def main():
    from analisis_sniper_listados_fase0 import evaluar
    r = evaluar()
    if not r.get("n_mercados"):
        msg = "🆕 *Sniper de mercados recién listados (ronda3 #7, FASE 0)*: todavía sin datos."
    else:
        L = ["🆕 *Sniper de mercados recién listados (FASE 0)* — informe diario",
             f"{r['n_mercados']} mercados nuevos registrados: " + ", ".join(f"{k} {v}" for k, v in r["por_categoria"].items())]
        for off, d in r["disp"].items():
            sp = "n/d" if d["spread_mediano"] is None else f"{d['spread_mediano']:.2f}"
            L.append(f"· +{off // 60} min tras el listado: n={d['n']}, cotización a dos lados {d['frac_dos_lados']:.0%}, spread mediano {sp}")
        ev = r.get("ev") or {}
        if ev:
            L.append("Escaleras cripto, EV por € vs precio justo (vol realizada, margen 5c, desenlace final):")
            for k, v in ev.items():
                ic = "n/d" if v["ic90"][0] is None else f"[{v['ic90'][0]:+.2f}, {v['ic90'][1]:+.2f}]"
                L.append(f"  {k}: n={v['n']} días={v['dias']} EV {v['ev_eur']:+.3f} IC90 {ic}")
        else:
            L.append("Aún sin escaleras resueltas para calcular EV frente al precio justo.")
        L.append("Gate: n>=40 y >=10 días por celda; hoy solo observación.")
        msg = "\n".join(L)
    print(msg)
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg, bot="cripto")
    except Exception as e:
        print(f"[vigia_sniper_listados_diario] error Telegram: {e}")


if __name__ == "__main__":
    main()
