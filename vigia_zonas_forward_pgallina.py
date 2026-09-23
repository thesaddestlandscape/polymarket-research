#!/usr/bin/env python3
"""vigia_zonas_forward_pgallina.py -- (23-Sep, petición Javi: "pon un rastreador de esta acción para que
vaya avisando diariamente de cómo evoluciona"). Cron diario; SIEMPRE envía Telegram (no solo cambios).

Por cada zona de data/live/zonas_forward_pgallina.json (live y dry_run), desde su `desde`:
  - REAL: trades CLOSED en trades.csv de la tupla con signal_ask en la zona -> n, total, media, hit, IC90
  - DRY-RUN forward: bot_wallets_gate_bucket_fase0.csv (fillable en decisión, ratio>=5, ask de detección
    en la zona, resuelto) -> n, media, IC90  (mismo PnL que el análisis: fee 7%, 1€)
  - estado del kill-switch (zonas_forward_pgallina_kill.json)
Y el progreso del GATE DE STAGE 0 (n>=150-200 trades reales con IC90 bootstrap > 0) sobre los trades
reales de las zonas live. Guarda serie en data/shadow/zonas_forward_pgallina_historial.jsonl.
Solo lectura (no abre ni cierra nada: eso lo hace zonas_forward_pgallina.py en el ejecutor).
"""
import csv
import json
import random
import statistics as st
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import zonas_forward_pgallina as Z  # noqa: E402

BW = REPO / "data" / "shadow" / "bot_wallets_gate_bucket_fase0.csv"
HIST = REPO / "data" / "shadow" / "zonas_forward_pgallina_historial.jsonl"
FEE = 0.07
_rng = random.Random(11)


def _ic90(v):
    if len(v) < 5:
        return None
    b = sorted(st.mean(_rng.choices(v, k=len(v))) for _ in range(1000))
    return round(b[50], 3), round(b[950], 3)


def _pnl(ask, win):
    return (1 - ask) / ask * (1 - FEE) if win else -1.0


def _dryrun(zonas):
    """{(tupla,lo): [pnl,...]} desde bot_wallets fase0."""
    out = {(z["tupla"], z["lo"]): [] for z in zonas}
    idx = {}
    for z in zonas:
        arq, act, mar, dec = z["tupla"].split("#")
        idx.setdefault((arq, act, mar, dec[len("BUY_"):]), []).append(z)
    try:
        with open(BW, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                zs = idx.get((r.get("arquetipo"), r.get("activo"), r.get("marco"), r.get("lado_wallet")))
                if not zs or not r.get("outcome_real") or r.get("acierto") not in ("0", "1"):
                    continue
                if r.get("sigue_fillable_decision") != "1":
                    continue
                try:
                    a_det = float(r.get("mejor_ask_deteccion") or "x")
                    a_dec = float(r.get("mejor_ask_decision") or "x")
                    ratio = float(r.get("ratio_vs_stake_decision") or 0)
                except ValueError:
                    continue
                if ratio < 5 or not (0 < a_dec < 0.80):
                    continue
                # /code-review: tramo nuevo = DETECTADO después de `desde` (no resuelto después)
                ts = r.get("timestamp_utc") or r.get("trade_timestamp", "")
                for z in zs:
                    if ts >= z["desde"] and z["lo"] <= a_det < z["hi"]:
                        out[(z["tupla"], z["lo"])].append(_pnl(a_dec, r["acierto"] == "1"))
    except OSError:
        pass
    return out


def main() -> int:
    d = json.loads(Z.RUTA.read_text(encoding="utf-8"))
    zonas = d.get("zonas", [])
    kill = Z._latch()
    dr = _dryrun(zonas)
    ahora = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lineas = ["📊 *Zonas forward P-GALLINA (Stage 0)* -- " + ahora[:16] + " UTC"]
    todos_real, hist = [], {"ts": ahora, "zonas": []}
    for z in zonas:
        real = Z.trades_reales(z["tupla"], z["desde"], z["lo"], z["hi"])
        dry = dr.get((z["tupla"], z["lo"]), [])
        k = kill.get(z["tupla"], {})
        if z.get("modo") == "live":
            todos_real += real
        est = "🛑 CERRADA (" + k.get("motivo", "") + ")" if k.get("matada") else ("🟢 LIVE" if z.get("modo") == "live" else "🧪 dry-run")
        r_txt = (f"real n={len(real)} total={sum(real):+.2f}€ media={st.mean(real):+.3f} "
                 f"hit={sum(1 for p in real if p > 0)/len(real):.0%} IC90={_ic90(real)}") if real else "real n=0"
        d_txt = f"dry n={len(dry)} media={st.mean(dry):+.3f} IC90={_ic90(dry)}" if dry else "dry n=0"
        lineas.append(f"{est} {z['tupla']} [{z['lo']:.2f},{z['hi']:.2f}) | {r_txt} | {d_txt}")
        hist["zonas"].append({"tupla": z["tupla"], "lo": z["lo"], "modo": z.get("modo"), "matada": bool(k.get("matada")),
                              "real_n": len(real), "real_total": round(sum(real), 3), "dry_n": len(dry),
                              "dry_media": round(st.mean(dry), 4) if dry else None})
    ic = _ic90(todos_real)
    gate = "✅ PASA" if (len(todos_real) >= 150 and ic and ic[0] > 0) else "⏳ no todavía"
    lineas.append(f"*Gate Stage 0* (zonas live): n={len(todos_real)}/150-200 total={sum(todos_real):+.2f}€ "
                  f"IC90={ic} -> {gate}")
    hist["stage0"] = {"n": len(todos_real), "total": round(sum(todos_real), 3), "ic90": ic}
    with open(HIST, "a", encoding="utf-8") as f:
        f.write(json.dumps(hist, ensure_ascii=False) + "\n")
    msg = "\n".join(lineas)
    print(msg)
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg)
    except Exception as e:
        print(f"telegram falló: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
