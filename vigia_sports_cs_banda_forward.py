#!/usr/bin/env python3
"""vigia_sports_cs_banda_forward.py -- seguimiento FORWARD de las hipótesis de CS CONGELADAS el 30-Sep
(Javi 30-Sep: "ok a las dos" -> extensión 1b en observación y versión maker). Aviso diario por Telegram.

De dónde salen (no valen por lo visto antes del corte; solo cuenta lo posterior, reglas tal cual):
cribado de 504 celdas de sports con TRAIN<=17-Sep / VAL 18-24 / HOLDOUT 25-30 (20 positivas en TRAIN
con ~25 esperables por azar; 6 pasan VAL y las 6 son este mismo fenómeno). Antes del corte:
  A  CS#FADE [0,65-0,70)            n=389 EV +0,153 IC90 (+0,102,+0,200), holdout +0,103   (LIVE desde 30-Sep 15:26Z)
  B  CS [0,65-0,70) cualquier disparo n=482 EV +0,088, holdout -0,018 (NO se sostiene)
  C  CS partido [0,65-0,70)          n=195 EV +0,112, holdout +0,060 (n=32)
  D  CS partido [0,60-0,80)          n=665 EV +0,061, holdout +0,034
  M  maker: vender el longshot en CS cuando una wallet lo compra a [0,30-0,40) (nosotros compramos el
     favorito a 1-precio, sin comisión)  n=2.306 EV +0,029 IC90 (+0,009,+0,050); muere con +2c.
Unidad: primer disparo fillable (ask real, ratio>=5x) por mercado-lado (A: además por tipo) del dry-run
del sniper de sports. Fee real de sports: 5 % x (1-p) SOLO al ganar. Se excluyen 2 wallets con precio
artefacto en mercados completed-match.
Confirmada = n>=40, >=10 días, EV>=+0,10 (M: >=+0,03), IC90 por días >0, wallet top<=30 %.
Refutada = n>=40 e IC90 por días entero <0. Además informa de los trades REALES de CS#FADE desde la
reactivación frente al tope del kill. Solo lectura. Salida: data/sports/cs_banda_forward.json
"""
import csv
import json
import random
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
DRY = REPO / "data/sports/wallet_mirror_sniper_dry_run.csv"
TRADES = REPO / "data/sports/trades.csv"
APROB = REPO / "data/sports/wallet_mirror_aprobaciones_manuales.json"
OUT = REPO / "data/sports/cs_banda_forward.json"
CORTE = "2026-09-30T16:00"      # congelación de reglas; no tocar
FEE = 0.05
ARTEFACTO = {"0x9c5ef1b4", "0xf6705478"}


def _pnl(ask: float, gana: int) -> float:
    return ((1 - ask) / ask - FEE * (1 - ask)) if gana else -1.0


def _es_partido(slug: str) -> bool:
    return not re.search(r"completed-match|draw|handicap|spread|total|-(game|map|set)\d", slug)


def _ic90(por_dia: dict):
    ks = list(por_dia)
    if len(ks) < 4:
        return None
    rng = random.Random(7)
    ms = []
    for _ in range(1500):
        s = c = 0
        for k in (rng.choice(ks) for _ in ks):
            s += sum(por_dia[k])
            c += len(por_dia[k])
        ms.append(s / c)
    ms.sort()
    return [round(ms[75], 4), round(ms[1424], 4)]


def _resumen(filas: list, ev_min: float) -> dict:
    n = len(filas)
    if n == 0:
        return {"n": 0, "veredicto": "sin_datos"}
    pd = defaultdict(list)
    for d, p, _w, _a, _wal in filas:
        pd[d].append(p)
    ev = sum(p for _, p, *_ in filas) / n
    ic = _ic90(pd)
    top = Counter(w for *_, w in filas).most_common(1)[0][1] / n
    ver = "sin_concluir"
    if n >= 40 and ic and ic[1] < 0:
        ver = "refutada_forward"
    elif n >= 40 and len(pd) >= 10 and ev >= ev_min and ic and ic[0] > 0 and top <= 0.30:
        ver = "confirmada_forward"
    return {"n": n, "dias": len(pd), "acierto": round(sum(w for _, _, w, _, _ in filas) / n, 4),
            "precio_medio": round(sum(a for _, _, _, a, _ in filas) / n, 4), "ev": round(ev, 4), "ic90": ic,
            "dias_positivos": sum(1 for v in pd.values() if sum(v) > 0), "wallet_top_pct": round(top * 100),
            "veredicto": ver}


def main() -> int:
    prim, prim_tipo, maker = {}, {}, {}
    with open(DRY, encoding="utf-8", errors="replace", newline="") as f:
        for r in csv.DictReader(f):
            if r.get("categoria") != "CS" or (r.get("wallet") or "")[:10].lower() in ARTEFACTO:
                continue
            ts = r.get("timestamp_utc") or ""
            if ts < CORTE:
                continue
            try:
                pw = float(r["precio_wallet"])
            except (TypeError, ValueError):
                continue
            if 0.30 <= pw < 0.40 and r.get("outcome_real_index") not in ("", None):
                k = (r["condition_id"], r["outcome_index_wallet"])
                if k not in maker or ts < maker[k][0]:
                    gana = int(r["outcome_real_index"] != r["outcome_index_wallet"])
                    coste = 1 - pw
                    maker[k] = (ts, (ts[:10], ((1 - coste) / coste if gana else -1.0), gana, coste, r["wallet"]))
            if r.get("acierto") not in ("0", "1"):
                continue
            try:
                ratio, ask = float(r["ratio_vs_stake_mirror"]), float(r["mejor_ask_mirror"])
            except (TypeError, ValueError):
                continue
            if ratio < 5 or not 0.02 < ask < 0.98:
                continue
            fila = (ts, ask, int(r["acierto"]), r["tipo"], r["market_slug"], r["wallet"])
            k = (r["condition_id"], r["mirror_outcome_index"])
            if k not in prim or ts < prim[k][0]:
                prim[k] = fila
            kt = k + (r["tipo"],)
            if kt not in prim_tipo or ts < prim_tipo[kt][0]:
                prim_tipo[kt] = fila

    def fl(rows, cond):
        return [(t[:10], _pnl(a, w), w, a, wal) for t, a, w, tipo, slug, wal in rows if cond(a, tipo, slug)]

    hip = {
        "A CS#FADE [0,65-0,70) (LIVE)": _resumen(fl(prim_tipo.values(), lambda a, t, s: t == "FADE" and 0.65 <= a < 0.70), 0.10),
        "B CS [0,65-0,70) cualquier disparo": _resumen(fl(prim.values(), lambda a, t, s: 0.65 <= a < 0.70), 0.10),
        "C CS partido [0,65-0,70)": _resumen(fl(prim.values(), lambda a, t, s: 0.65 <= a < 0.70 and _es_partido(s)), 0.10),
        "D CS partido [0,60-0,80)": _resumen(fl(prim.values(), lambda a, t, s: 0.60 <= a < 0.80 and _es_partido(s)), 0.10),
        "M maker vende longshot [0,30-0,40)": _resumen([v[1] for v in maker.values()], 0.03),
    }
    # trades REALES de CS#FADE desde la reactivación, frente al tope del kill
    real = {"n": 0}
    try:
        ap = json.loads(APROB.read_text(encoding="utf-8"))["aprobaciones"]["CS#FADE#0.65"]
        desde, tope = ap["desde"], float(ap["kill"]["perdida_max_eur"])
        cer, ab = [], 0
        with open(TRADES, encoding="utf-8", errors="replace", newline="") as f:
            for r in csv.DictReader(f):
                if r.get("categoria") == "CS" and r.get("tipo") == "FADE" and (r.get("timestamp_utc") or "") >= desde:
                    try:
                        ep = float(r["entry_price"])
                    except (TypeError, ValueError):
                        continue
                    if not 0.65 <= ep < 0.70:
                        continue
                    if r.get("status") == "CLOSED":
                        cer.append(float(r["pnl_neto_eur"] or 0))
                    elif r.get("status") == "OPEN":
                        ab += 1
        real = {"desde": desde, "n": len(cer), "aciertos": sum(1 for x in cer if x > 0), "pnl_eur": round(sum(cer), 2),
                "abiertos": ab, "tope_kill_eur": -tope}
    except Exception as e:  # solo informe: nunca tumbar el vigía por esto
        real = {"error": str(e)}
    sal = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "corte": CORTE,
           "hipotesis": hip, "real_cs_fade": real}
    tmp = OUT.with_name(OUT.name + ".tmp")
    tmp.write_text(json.dumps(sal, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(OUT)
    lin = [f"🎯 CS banda 0,65-0,70 — forward desde {CORTE[:10]}"]
    for k, v in hip.items():
        lin.append(f"{k}: n={v['n']}" + ("" if not v["n"] else
                   f" acierto {v['acierto']:.1%} a {v['precio_medio']:.3f} EV {v['ev']:+.1%} IC90 {v['ic90']} → {v['veredicto']}"))
    if "error" not in real:
        lin.append(f"REAL CS#FADE: {real.get('aciertos', 0)}/{real.get('n', 0)} aciertos, {real.get('pnl_eur', 0):+.2f} € "
                   f"(tope {real.get('tope_kill_eur')} €), abiertos {real.get('abiertos', 0)}")
    print("\n".join(lin))
    if "--sin-telegram" not in sys.argv:
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram("\n".join(lin), bot="sports")
        except Exception as e:
            print(f"aviso: no se pudo enviar Telegram ({e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
