#!/usr/bin/env python3
"""vigia_radar_estabilidad_temporal.py -- radar diario de celdas con EDGE
SOSTENIDO EN EL TIEMPO en sports wallet mirror (24-Sep, OK Javi).

Criterio (el único que mantuvo el signo en todos los walk-forward del 24-Sep,
ver analisis_promocion_forward_walkforward_24sep.py y la memoria
project_punto_medio_riesgo_y_edge_sostenido_24sep): celda (categoria, tipo,
bucket 0,05 de ask) con
  - n >= N_MIN unidades (primer disparo fillable por mercado-lado),
  - media > 0 en cada uno de 3 tramos temporales consecutivos,
  - >= FRAC_DIAS de días con PnL positivo,
  - wallet top <= TOP_MAX de las unidades.
Ejemplo que lo motivó: CS#FADE [0.65,0.70) -- 284 mercados, 31 días (71 %
positivos), 84 wallets, ~+0,16 EUR/tr en los 3 tramos (aprobada a live 24-Sep).

SOLO AVISA: no abre nada. Una celda del radar pasa a real únicamente con
aprobación manual de Javi (data/sports/wallet_mirror_aprobaciones_manuales.json,
con kill-switch). Telegram (bot sports) solo por celdas NUEVAS en el radar.
Salida: data/sports/radar_estabilidad_temporal.json.
"""
import json
import math
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from analisis_sports_wallet_mirror_gate_bucket_26ago import (  # noqa: E402
    cargar_unidades_independientes, payout_win)

N_MIN, FRAC_DIAS, TOP_MAX = 60, 0.60, 0.30
OUT = REPO / "data/sports/radar_estabilidad_temporal.json"
APROBACIONES = REPO / "data/sports/wallet_mirror_aprobaciones_manuales.json"


def main() -> int:
    por = defaultdict(list)
    for r in cargar_unidades_independientes():
        ask = float(r["mejor_ask_mirror"])
        b = round(math.floor(ask / 0.05 + 1e-9) * 0.05, 2)
        por[(r["categoria"], r["tipo"], b)].append(
            (r["timestamp_utc"], r["wallet"], payout_win(ask) if r["acierto"] == "1" else -1.0))
    radar = {}
    for (cat, tipo, b), xs in por.items():
        if len(xs) < N_MIN:
            continue
        xs.sort()
        k = len(xs) // 3
        tramos = [xs[:k], xs[k:2 * k], xs[2 * k:]]
        medias = [sum(p for *_, p in t) / len(t) for t in tramos]
        if min(medias) <= 0:
            continue
        dias = defaultdict(float)
        for ts, _w, p in xs:
            dias[ts[:10]] += p
        frac = sum(v > 0 for v in dias.values()) / len(dias)
        top = Counter(w for _, w, _ in xs).most_common(1)[0][1] / len(xs)
        if frac < FRAC_DIAS or top > TOP_MAX:
            continue
        radar[f"{cat}#{tipo}#{b:.2f}"] = {
            "n": len(xs), "dias": len(dias), "frac_dias_pos": round(frac, 3), "top_wallet": round(top, 3),
            "n_wallets": len({w for _, w, _ in xs}), "pnl_medio": round(sum(p for *_, p in xs) / len(xs), 4),
            "medias_tramos": [round(m, 4) for m in medias]}
    try:
        aprobadas = set(json.loads(APROBACIONES.read_text(encoding="utf-8")).get("aprobaciones", {}))
    except Exception:
        aprobadas = set()
    previo = {}
    try:
        previo = json.loads(OUT.read_text(encoding="utf-8")).get("radar", {})
    except Exception:
        pass
    nuevas = [c for c in radar if c not in previo]
    OUT.write_text(json.dumps({"actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                               "criterio": {"N_MIN": N_MIN, "FRAC_DIAS": FRAC_DIAS, "TOP_MAX": TOP_MAX},
                               "radar": radar}, indent=1, ensure_ascii=False), encoding="utf-8")
    for c, v in sorted(radar.items(), key=lambda x: -x[1]["pnl_medio"]):
        marca = " [APROBADA]" if c in aprobadas else (" [NUEVA]" if c in nuevas else "")
        print(f"{c}: n={v['n']} días={v['dias']} ({v['frac_dias_pos']:.0%}+) wallets={v['n_wallets']} "
              f"top={v['top_wallet']:.0%} €/tr={v['pnl_medio']:+.3f} tramos={v['medias_tramos']}{marca}")
    if nuevas and previo:  # no avisar en la primera corrida (siembra)
        from shadow_digest import enviar_telegram
        lineas = [f"{c}: n={radar[c]['n']} días={radar[c]['dias']} ({radar[c]['frac_dias_pos']:.0%}+) "
                  f"€/tr={radar[c]['pnl_medio']:+.3f} wallets={radar[c]['n_wallets']}" for c in nuevas]
        enviar_telegram("📡 Radar estabilidad temporal sports -- celdas NUEVAS con edge sostenido "
                        "(solo aviso, abrir requiere aprobación):\n" + "\n".join(lineas), bot="sports")
    return 0


if __name__ == "__main__":
    sys.exit(main())
