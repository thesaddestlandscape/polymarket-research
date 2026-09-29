#!/usr/bin/env python3
"""vigia_stink_bids_diario.py -- informe DIARIO por Telegram (29-Sep, Javi) de
stink_bids_fase0.py (ronda3 #1): ¿la reversión tras ventas bajo la mediana es
COBRABLE con libro real y tamaño ejecutado? SIEMPRE envía. Cron 08:55 UTC."""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))


def main():
    from analisis_stink_bids_fase0 import evaluar
    r = evaluar()
    if not r.get("n_eventos"):
        msg = "🪙 *Stink bids (ronda3 #1, FASE 0)*: todavía sin eventos registrados."
    else:
        L = [f"🪙 *Stink bids: reversión con libro real (FASE 0)* — informe diario",
             f"{r['n_eventos']} eventos en {r['dias']} días, {r['mercados']} mercados (ventas >=5c bajo la mediana, "
             f"no updown). USD ejecutados mediana {r['usd_evento_mediana']}, caída mediana {r['desviacion_mediana']}, "
             f"bid restante cerca del precio (mediana) {r['depth_bid_cerca_mediana']} USD."]
        for d, x in r["por_delta"].items():
            if x.get("n", 0) < 3:
                L.append(f"· +{d}s: n={x.get('n', 0)} (<3)")
                continue
            L.append(f"· salida al bid a +{d}s: n={x['n']} mediana {x['mediana_c']}c media {x['media_c']}c "
                     f"{x['frac_pos']:.0%} positivos IC90 mercados [{x['ic90_clusters_c'][0]}, {x['ic90_clusters_c'][1]}]c "
                     f"→ {x['eur_por_evento']:+.3f} EUR/evento (stake max 2 EUR), total {x['eur_total']:+.2f} EUR")
        ok = r["n_eventos"] >= 40 and r["dias"] >= 10
        L.append("Gate: n>=40 eventos y >=10 días para decidir." + ("" if ok else " Aún exploratorio; sin ejecutor."))
        msg = "\n".join(L)
    print(msg)
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg, bot="cripto")
    except Exception as e:
        print(f"[vigia_stink_bids_diario] error Telegram: {e}")


if __name__ == "__main__":
    main()
