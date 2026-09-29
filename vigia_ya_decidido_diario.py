#!/usr/bin/env python3
"""vigia_ya_decidido_diario.py -- informe DIARIO por Telegram (29-Sep, Javi:
"un vigía diario por Telegram") de ya_decidido_universal_fase0.py (ronda3 #5):
mercados con fin pasado y sin asentar cuyo lado ganador aparente aún cotiza
<0,99. SIEMPRE envía. Cron 09:00 UTC. Solo observación."""
import csv
import statistics as st
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
CSV_IN = REPO / "data/shadow/ya_decidido_universal_fase0.csv"


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _limpio(t):
    return ''.join(ch for ch in (t or '') if ch not in '*_`[]')


def main():
    if not CSV_IN.exists():
        msg = "⏳ *Ya decidido, aún abierto (ronda3 #5)*: todavía sin datos."
    else:
        R = list(csv.DictReader(open(CSV_IN, encoding="utf-8")))
        desde = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()
        vis = [r for r in R if r["evento"] in ("visto", "cambio")]
        res = [r for r in R if r["evento"] == "resuelto"]
        nuevos24 = {r["condition_id"] for r in vis if r["timestamp_utc"] >= desde}
        comprables = {}
        for r in vis:
            c = _f(r["coste_real"])
            if c is not None and c < 0.99:
                comprables[r["condition_id"]] = r          # último estado visto
        L = ["⏳ *Ya decidido, aún abierto (ronda3 #5, FASE 0)* — informe diario",
             f"Total acumulado: {len({r['condition_id'] for r in vis})} candidatos vistos (lado >=0,90), "
             f"{len(comprables)} con coste real <0,99; nuevos 24h: {len(nuevos24)}; resueltos: {len(res)}."]
        ev = [(_f(r["retorno_bruto"]), _f(r["profundidad_usd"]) or 0, r) for r in comprables.values()
              if _f(r["retorno_bruto"])]
        if ev:
            cap = sum(p for _, p, _ in ev)
            L.append(f"Comprables ahora (último estado): retorno bruto mediano {st.median(e for e, _, _ in ev):.1%}, "
                     f"capacidad total {cap:.0f} USD a coste+1c.")
            for e, p, r in sorted(ev, key=lambda x: -x[1])[:5]:
                L.append(f"· [{r['categoria_txt']}] {_limpio(r['question'])[:55]} → {r['lado_ganador']} coste {r['coste_real']} "
                         f"({e:.1%}), prof {p:.0f} USD, {r['horas_desde_fin']} h tras fin, uma {r['uma_status'] or '-'}")
        ac = [r for r in res if r["acierto_lado"] in ("0", "1")]
        if ac:
            aciertos = sum(r["acierto_lado"] == "1" for r in ac)
            hs = [_f(r["horas_hasta_resolver"]) for r in res if _f(r["horas_hasta_resolver"]) is not None]
            L.append(f"*Acierto real del lado ganador aparente*: {aciertos}/{len(ac)} ({aciertos/len(ac):.1%}) "
                     f"— hace falta >=99 % para que coste 0,95 sea rentable (un fallo = -100 %). "
                     f"Horas hasta asentar (desde que lo vemos): mediana {st.median(hs):.1f}" if hs else
                     f"*Acierto real*: {aciertos}/{len(ac)}")
            for r in ac:
                if r["acierto_lado"] == "0":
                    L.append(f"🚨 FALLÓ: {_limpio(r['question'])[:70]} (lado {r['lado_ganador']} → final {r['lado_final']})")
        else:
            L.append("Aún sin resoluciones con desenlace conocido (mide el acierto real del lado ganador).")
        L.append("Gate para pensar en ejecutor: n>=40 resueltos, acierto >=99 %, capacidad y tiempo de asentado útiles; hoy solo observación.")
        msg = "\n".join(L)
    print(msg)
    try:
        sys.path.insert(0, str(REPO))
        from shadow_digest import enviar_telegram
        enviar_telegram(msg, bot="cripto")
    except Exception as e:
        print(f"[vigia_ya_decidido_diario] error Telegram: {e}")


if __name__ == "__main__":
    main()
