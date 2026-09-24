#!/usr/bin/env python3
"""vigia_precierre_naive_twap.py -- seguimiento DIARIO del PRECIERRE y del NAIVE en
modo TWAP (24-Sep, petición Javi: "vigila diariamente esto").

Para cada estrategia (RESOLUTION_SNIPER_PRECIERRE, RESOLUTION_SNIPER_NAIVE) y
marco (5min/15min), sobre los trades REALES desde el arranque de su modo TWAP
(data/live/precierre_twap_desde.txt / naive_twap_desde.txt):
  - n cerrados, acierto (esperado ~95 % precierre 5min; 15min con evidencia más
    floja: n=84, +0,32 EUR/EUR, 7/10 días), PnL total y por trade, abiertos.
  - estado del kill-switch (latch).
  - embudo de decisiones de las últimas 24 h (gate_motivo del CSV del ejecutor).
  - alerta si el acierto real cae >10 pp por debajo del esperado con n>=20.
Cuando PolyBolt acumule >=7 días (data/prices/polybolt_*.csv), recuerda la
revalidación del offset (T-30/-45/-60) y de la banda por moneda con el TWAP
OFICIAL (analisis_precierre_twap_ventana_24sep.py).
Telegram SIEMPRE (resumen diario). Salida data/live/vigia_precierre_naive_twap.json.
"""
import csv
import glob
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
LIVE = REPO / "data" / "live"
TRADES = LIVE / "trades.csv"
DECISIONES = REPO / "data" / "shadow" / "resolution_sniper_precierre_executor_v2.csv"
OUT = LIVE / "vigia_precierre_naive_twap.json"
MODOS = {
    "RESOLUTION_SNIPER_PRECIERRE": (LIVE / "precierre_twap_desde.txt", LIVE / "precierre_twap_kill.json",
                                    {"5min": 0.95, "15min": 0.95}),
    "RESOLUTION_SNIPER_NAIVE": (LIVE / "naive_twap_desde.txt", LIVE / "naive_twap_kill.json",
                                {"5min": 0.85}),
}


def _leer(p: Path, defecto=None):
    try:
        return p.read_text(encoding="utf-8").strip()
    except Exception:
        return defecto


def main() -> int:
    ahora = datetime.now(timezone.utc)
    informe, lineas, alertas = {}, [], []
    filas = list(csv.DictReader(open(TRADES, encoding="utf-8")))
    for est, (p_desde, p_kill, esperado) in MODOS.items():
        desde = _leer(p_desde)
        kill = _leer(p_kill)
        info = {"desde": desde, "kill": json.loads(kill) if kill else {"matado": False}, "marcos": {}}
        for marco in ("5min", "15min"):
            ts = [r for r in filas if r.get("strategy") == est and desde and (r.get("timestamp_utc") or "") >= desde
                  and (r.get("subtype") or "").endswith(marco)]
            cerr = [r for r in ts if r.get("status") == "CLOSED"]
            pnls = []
            for r in cerr:
                try:
                    pnls.append(float(r["pnl_neto_eur"]))
                except (KeyError, ValueError):
                    pass
            n = len(pnls)
            hit = sum(p > 0 for p in pnls) / n if n else None
            d = {"n_cerrados": n, "acierto": round(hit, 3) if hit is not None else None,
                 "pnl_total": round(sum(pnls), 2), "pnl_trade": round(sum(pnls) / n, 3) if n else None,
                 "abiertos": sum(1 for r in ts if r.get("status") in ("OPEN", "ERROR")),
                 "esperado": esperado.get(marco)}
            info["marcos"][marco] = d
            if esperado.get(marco) and n >= 20 and hit is not None and hit < esperado[marco] - 0.10:
                alertas.append(f"⚠️ {est} {marco}: acierto real {hit:.0%} (n={n}) vs esperado {esperado[marco]:.0%}")
            if n or d["abiertos"]:
                lineas.append(f"{est.replace('RESOLUTION_SNIPER_', '')} {marco}: n={n} acierto="
                              f"{'-' if hit is None else f'{hit:.0%}'} pnl={sum(pnls):+.2f}€ "
                              f"({'-' if not n else f'{sum(pnls)/n:+.3f}'}/tr) abiertos={d['abiertos']}")
        if info["kill"].get("matado"):
            alertas.append(f"🛑 {est} kill-switch ACTIVO: {info['kill'].get('motivo')}")
        informe[est] = info
    # embudo de decisiones 24 h
    lim = (ahora - timedelta(hours=24)).isoformat()
    embudo = defaultdict(Counter)
    try:
        for r in csv.DictReader(open(DECISIONES, encoding="utf-8")):
            if (r.get("timestamp_utc") or "") >= lim:
                mot = (r.get("gate_motivo") or "").split("=")[0].split(":")[0]
                embudo[f"{r.get('estrategia')}|{r.get('marco')}"][mot] += 1
    except OSError:
        pass
    informe["embudo_24h"] = {k: dict(v.most_common(8)) for k, v in embudo.items()}
    dias_pb = len(glob.glob(str(REPO / "data/prices/polybolt_*.csv*")))
    informe["dias_polybolt"] = dias_pb
    if dias_pb >= 7:
        alertas.append(f"📅 PolyBolt ya tiene {dias_pb} días: toca revalidar offset (T-30/-45/-60) y banda por moneda "
                       f"con el TWAP oficial (analisis_precierre_twap_ventana_24sep.py)")
    informe["actualizado_utc"] = ahora.isoformat(timespec="seconds")
    OUT.write_text(json.dumps(informe, indent=1, ensure_ascii=False), encoding="utf-8")
    msg = ["📊 PRECIERRE/NAIVE modo TWAP -- resumen diario"] + (lineas or ["sin trades reales todavía"])
    for k, v in informe["embudo_24h"].items():
        msg.append(f"· 24h {k}: " + ", ".join(f"{m}={c}" for m, c in list(v.items())[:5]))
    msg += alertas
    print("\n".join(msg))
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram("\n".join(msg))
    except Exception as e:
        print(f"(Telegram falló: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
