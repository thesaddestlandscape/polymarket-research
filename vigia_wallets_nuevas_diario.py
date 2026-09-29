#!/usr/bin/env python3
"""vigia_wallets_nuevas_diario.py -- informe DIARIO Telegram (Javi 29-Sep) de wallets_nuevas_fase0 (ronda2 #2):
BUY de wallets nuevas, EV al ask COPIABLE por latencia. SIEMPRE envía. Cron 09:10 UTC."""
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))


def main():
    from analisis_wallets_nuevas_fase0 import evaluar
    r = evaluar()
    if not r.get("n_eventos"):
        msg = "🕵️ *Wallets nuevas con apuesta grande (ronda2 #2, FASE 0)*: todavía sin eventos."
    else:
        L = ["🕵️ *Wallets nuevas con apuesta grande (FASE 0)* — informe diario",
             f"{r['n_eventos']} BUY de wallets nuevas capturados ({r['wallets']} wallets), {r['resueltos']} resueltos. "
             "Retrospectivo (precio de la wallet): +0,034 €/€ nuevas vs −0,39 antiguas."]
        for k, v in r["filas"].items():
            ic = "n/d" if v["ic90"][0] is None else f"[{v['ic90'][0]:+.2f}, {v['ic90'][1]:+.2f}]"
            L.append(f"· {k}: n={v['n']} cond={v['cond']} días={v['dias']} EV {v['ev']:+.3f} IC90 {ic}")
        L.append("Gate: n>=40 resueltos, >=10 días, IC90>0 al ask copiable a +1-3 s; hoy solo observación.")
        msg = "\n".join(L)
    print(msg)
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg, bot="cripto")
    except Exception as e:
        print(f"[vigia_wallets_nuevas_diario] error Telegram: {e}")


if __name__ == "__main__":
    main()
