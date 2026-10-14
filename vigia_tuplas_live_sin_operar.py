#!/usr/bin/env python3
"""vigia_tuplas_live_sin_operar.py — 14-Oct (Javi): ¿qué tupla de pares_permitidos_live lleva días SIN operar y QUÉ
protección la está bloqueando?

Origen: Wallet Mirror estuvo un mes casi parado (filtro wallet+bucket del 04-Sep + tope 0,80 del 23-Sep + gate del
07-Oct, razonables una a una) y ningún vigía lo dijo. Este vigía no decide nada: mide y avisa.

Unidad = ESTRATEGIA#ACTIVO#MARCO (las tuplas live van por pares de dirección; los logs de WM no dicen la dirección).
Por unidad:
  - último trade REAL (data/live/trades.csv, cualquier dirección) y días sin operar;
  - señales y motivos de NO ejecución en las últimas VENTANA_H horas, normalizados (sin números ni direcciones), de:
      · logs/wallet_mirror_executor.log  (línea "🎯 DRY_RUN ACT#MARCO" + la decisión que la sigue)
      · logs/ejecutores_live_consolidado.log ("[SNIPER]/[DISPERSO] ACT#MARCO[b) ... veredicto=X fillable=Y -> NO_dispara"
        y "⛔ Re-chequeo gate post-requote (TUPLA)")
      · data/live/libro_snapshots.csv (motivo distinto de "ejecutada")
    PRECIERRE tiene vigías propios (vigia_precierre_naive_twap): aquí solo días sin operar.
Estado: OPERA (trade en < DIAS_ALERTA), BLOQUEADA (sin trade y con señales: top motivos), SIN_SEÑALES.
Salida: data/shadow/vigia_tuplas_live_sin_operar.json + Telegram diario con las BLOQUEADAS / SIN_SEÑALES (resumen de
una línea por unidad). Sin latch: el resumen diario ES el aviso (lo que faltó en septiembre era verlo cada día).
Uso: python3 vigia_tuplas_live_sin_operar.py [--telegram]
"""
import argparse
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

CONFIG = REPO / "data" / "live" / "config_live.json"
TRADES = REPO / "data" / "live" / "trades.csv"
SNAP = REPO / "data" / "live" / "libro_snapshots.csv"
LOG_WM = REPO / "logs" / "wallet_mirror_executor.log"
LOG_EJ = REPO / "logs" / "ejecutores_live_consolidado.log"
OUT = REPO / "data" / "shadow" / "vigia_tuplas_live_sin_operar.json"
VENTANA_H = 24
DIAS_ALERTA = 3
TS = re.compile(r"^\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})[^\]]*\]")


def unidad(tupla: str) -> str:
    p = tupla.split("#")
    return "#".join(p[:3]) if len(p) >= 3 else tupla


def normalizar(m: str) -> str:
    m = re.sub(r"0x[0-9a-fA-F.]+", "W", m)
    m = re.sub(r"\([A-Z_]+#[A-Z]+#\w+#BUY_\w+\)", "", m)
    m = re.sub(r"\d+(\.\d+)?", "N", m)
    m = m.split(" -- ")[0].strip(" ⛔🎯")
    return re.sub(r"\s+", " ", m)[:110]


def lineas_recientes(path: Path, desde: str):
    if not path.exists():
        return
    with open(path, encoding="utf-8", errors="replace") as fh:
        for ln in fh:
            m = TS.match(ln)
            if m and m.group(1) >= desde:
                yield ln.rstrip("\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--telegram", action="store_true")
    a = ap.parse_args()
    ahora = datetime.now(timezone.utc)
    desde = (ahora - timedelta(hours=VENTANA_H)).strftime("%Y-%m-%dT%H:%M:%S")
    tuplas = json.loads(CONFIG.read_text())["pares_permitidos_live"]
    unidades = sorted({unidad(t) for t in tuplas})
    alias = {"SNIPER": "SNIPER", "DISPERSO": "DISPERSO"}

    ultimo = {}
    with open(TRADES, encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            u = f"{r['strategy']}#{r['subtype']}"
            if u in unidades and r.get("status") in ("OPEN", "CLOSED"):
                ultimo[u] = max(ultimo.get(u, ""), r["timestamp_utc"][:19])

    senales = Counter()
    motivos = defaultdict(Counter)
    # Wallet Mirror: la decisión es la primera línea relevante tras "🎯 DRY_RUN ACT#MARCO"
    actual = None
    for ln in lineas_recientes(LOG_WM, desde):
        m = re.search(r"🎯 DRY_RUN (\w+#\w+) ", ln)
        if m:
            actual = f"WALLET_MIRROR#{m.group(1)}"
            senales[actual] += 1
            continue
        if actual is None:
            continue
        cuerpo = TS.sub("", ln).strip()
        if cuerpo.startswith("resumen:") or cuerpo.startswith("Conex") or cuerpo.startswith("Conectado"):
            continue
        if "ORDEN REAL" in cuerpo or "Orden ejecutada" in cuerpo:
            motivos[actual]["ejecutada"] += 1
        elif "⛔" in cuerpo or "no se ejecuta" in cuerpo:
            motivos[actual][normalizar(cuerpo)] += 1
        else:
            continue
        actual = None
    # SNIPER / DISPERSO (ejecutores live consolidados)
    for ln in lineas_recientes(LOG_EJ, desde):
        m = re.search(r"\[(SNIPER|DISPERSO)\] (\w+#\w+)\[[^)]*\) .*?veredicto=(\w+) fillable=(\d)\S* .*-> (\w+)", ln)
        if m:
            u = f"{alias[m.group(1)]}#{m.group(2)}"
            senales[u] += 1
            if m.group(5) != "dispara":
                motivos[u][f"gate={m.group(3)} fillable={m.group(4)}"] += 1
            continue
        m = re.search(r"Re-chequeo gate post-requote \(([A-Z_]+#\w+#\w+)#BUY_\w+\).*?veredicto=(\w+)", ln)
        if m:
            motivos[m.group(1)][f"recheck post-requote gate={m.group(2)}"] += 1
    # libro_snapshots: motivos de la fase de ejecución
    if SNAP.exists():
        with open(SNAP, encoding="utf-8", errors="replace") as fh:
            for r in csv.DictReader(fh):
                if r.get("timestamp_utc", "") < desde:
                    continue
                u = f"{r.get('strategy')}#{r.get('subtype')}"
                if u in unidades and r.get("motivo") not in ("ejecutada", "", None):
                    motivos[u][f"libro: {r['motivo']}"] += 1

    filas = []
    for u in unidades:
        ult = ultimo.get(u)
        dias = (ahora - datetime.fromisoformat(ult).replace(tzinfo=timezone.utc)).total_seconds() / 86400 if ult else None
        n_mot = sum(motivos[u].values())
        if dias is not None and dias < DIAS_ALERTA:
            estado = "OPERA"
        elif senales[u] or n_mot:
            estado = "BLOQUEADA"
        else:
            estado = "SIN_SEÑALES"
        filas.append({"unidad": u, "estado": estado, "ultimo_trade": ult, "dias_sin_operar": round(dias, 1) if dias is not None else None,
                      "senales_24h": senales[u], "motivos_24h": motivos[u].most_common(5)})
    tmp = OUT.with_name(OUT.name + ".tmp")
    tmp.write_text(json.dumps({"generado": ahora.isoformat(timespec="seconds"), "ventana_h": VENTANA_H,
                               "dias_alerta": DIAS_ALERTA, "unidades": filas}, ensure_ascii=False, indent=1))
    os.replace(tmp, OUT)
    orden = {"BLOQUEADA": 0, "SIN_SEÑALES": 1, "OPERA": 2}
    lin = [f"🧭 Tuplas live sin operar (≥{DIAS_ALERTA} d) — {ahora:%d-%b %H:%MZ}"]
    for f in sorted(filas, key=lambda x: (orden[x["estado"]], -(x["dias_sin_operar"] or 999))):
        d = "nunca" if f["dias_sin_operar"] is None else f"{f['dias_sin_operar']:.0f} d"
        if f["estado"] == "OPERA":
            continue
        top = "; ".join(f"{m} ×{n}" for m, n in f["motivos_24h"][:2]) or "—"
        lin.append(f"• {f['unidad']} [{f['estado']}] sin operar {d} | señales 24 h {f['senales_24h']} | {top}")
    n_op = sum(1 for f in filas if f["estado"] == "OPERA")
    lin.append(f"OPERAN (<{DIAS_ALERTA} d): {n_op}/{len(filas)}")
    txt = "\n".join(lin)
    print(txt)
    if a.telegram and len(lin) > 2:
        from shadow_digest import enviar_telegram
        enviar_telegram(txt[:3900], bot="cripto")


if __name__ == "__main__":
    main()
