#!/usr/bin/env python3
"""vigia_wallet_mirror_entrada_baja.py -- seguimiento DIARIO de WALLET_MIRROR con entrada < 0,20
(24-Sep, petición Javi: "sigue mirando día a día wallet mirror con entrada <0,20").

Fuente: wallet_mirror_executor_dryrun.csv (decisión REAL: sigue_fillable_en_decision=1,
ask_decision), desde 07-Ago (post-TWAP). Aparte y solo informativo, el reconstruido 09-23 Sep
(reconstruido=1, ver reconstruir_wallet_mirror_executor_08_22sep.py).
Celda = activo × marco × (jugada grande sí/no), desglose CLAUDE.md pt.17. PnL a 1 EUR al
ask_decision, fee cripto 7 % sobre la ganancia.
Candidata = n>=40, >=10 días, PnL>=+0,10 EUR/tr, IC90 bootstrap por DÍAS > 0 y ambas mitades
> 0 (mismo listón que el resto de vigías). Línea base 24-Sep: n=10.146, hit 10,7 % vs ask 0,106,
-0,109 EUR/tr (calibrado, sin edge agregado).
Telegram SIEMPRE (resumen) + JSON data/shadow/vigia_wallet_mirror_entrada_baja.json.
"""
import csv
import json
import random
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
REAL = REPO / "data/shadow/wallet_mirror_executor_dryrun.csv"
RECON = REPO / "data/shadow/wallet_mirror_executor_dryrun_reconstruido_08_22sep.csv"
OUT = REPO / "data/shadow/vigia_wallet_mirror_entrada_baja.json"
DESDE, ASK_MAX, FEE = "2026-08-07", 0.20, 0.07
csv.field_size_limit(10_000_000)


def pnl(a, ac):
    return (1 - a) / a * (1 - FEE) if ac else -1.0


def cargar(p):
    g = defaultdict(list)
    if not p.exists():
        return g
    with open(p, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if (r.get("sigue_fillable_en_decision") != "1" or r.get("acierto") not in ("0", "1")
                    or (r.get("timestamp_utc") or "") < DESDE):
                continue
            try:
                a = float(r["ask_decision"])
            except (KeyError, ValueError):
                continue
            if not 0.01 < a < ASK_MAX:
                continue
            ac = int(r["acierto"])
            x = (r["timestamp_utc"], r["timestamp_utc"][:10], ac, pnl(a, ac), a)
            g[f"{r['activo']}#{r['marco']}#{'grande' if r.get('es_jugada_grande') == '1' else 'normal'}"].append(x)
            g["TOTAL"].append(x)
    return g


def resumen(xs):
    n = len(xs)
    dias = defaultdict(list)
    for x in xs:
        dias[x[1]].append(x[3])
    out = {"n": n, "dias": len(dias), "hit": round(sum(x[2] for x in xs) / n, 3),
           "ask_medio": round(sum(x[4] for x in xs) / n, 3), "pnl_tr": round(sum(x[3] for x in xs) / n, 3)}
    if n >= 20:
        o = sorted(xs)
        h = n // 2
        out["mitades"] = [round(sum(x[3] for x in o[:h]) / h, 3), round(sum(x[3] for x in o[h:]) / (n - h), 3)]
        ds = list(dias.values())
        rng = random.Random(11)
        medias = []
        for _ in range(1000):
            m = [v for _ in ds for v in rng.choice(ds)]
            medias.append(sum(m) / len(m))
        medias.sort()
        out["ic90_dias"] = [round(medias[50], 3), round(medias[949], 3)]
    out["candidata"] = bool(n >= 40 and out["dias"] >= 10 and out["pnl_tr"] >= 0.10 and out.get("ic90_dias", [0])[0] > 0
                            and min(out.get("mitades", [0])) > 0)
    return out


def main() -> int:
    real = {k: resumen(v) for k, v in cargar(REAL).items() if len(v) >= 5}
    recon = {k: resumen(v) for k, v in cargar(RECON).items() if len(v) >= 5}
    salida = {"actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "ask_max": ASK_MAX, "real": real, "reconstruido_09_23sep": recon}
    OUT.write_text(json.dumps(salida, indent=1, ensure_ascii=False), encoding="utf-8")
    t = real.get("TOTAL")
    msg = [f"🪙 WALLET_MIRROR entrada <{ASK_MAX:.2f} (decisión real, fillable)"]
    if t:
        msg.append(f"Total: n={t['n']} ({t['dias']} días) acierto {t['hit']:.1%} vs ask {t['ask_medio']:.3f} "
                   f"-> {t['pnl_tr']:+.3f} €/tr")
    top = sorted(((k, v) for k, v in real.items() if k != "TOTAL" and v["n"] >= 15), key=lambda kv: -kv[1]["pnl_tr"])[:4]
    for k, v in top:
        msg.append(f"· {k}: n={v['n']} {v['dias']}d hit {v['hit']:.0%} {v['pnl_tr']:+.3f} €/tr "
                   f"IC90 {v.get('ic90_dias', '-')}{' ✅ CANDIDATA' if v['candidata'] else ''}")
    cands = [k for k, v in real.items() if v["candidata"] and k != "TOTAL"]
    msg.append(f"Candidatas (n>=40, >=10 días, >=+0,10, IC90 días>0, mitades>0): {', '.join(cands) or 'ninguna'}")
    print("\n".join(msg))
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram("\n".join(msg))
    except Exception as e:
        print(f"(Telegram falló: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
