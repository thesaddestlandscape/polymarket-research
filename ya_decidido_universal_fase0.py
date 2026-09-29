#!/usr/bin/env python3
"""ya_decidido_universal_fase0.py -- FASE 0 (solo lectura, NUNCA orden real),
ronda3 #5 (29-Sep, Javi: "dale"): escáner universal "ya decidido, aún
abierto". Generaliza sports_sniper_cierre_fase0.py (solo deportes) a TODO lo
demás: mercados con endDate YA pasado y closed=false (resultado ya
conocido en el mundo real, pero UMA no ha asentado), donde el lado casi
seguro sigue cotizando a 0,90-0,99 durante horas/días. Excluidos: deportes
(los cubre el otro), up/down cripto (minutos) y weather (repo aparte, no
mezclar).

Foto 29-Sep 10:00 UTC (analisis manual): 731 mercados 'otros' con fin pasado
y sin cerrar; solo 25 con precio de compra real <1 para el lado ganador y
casi todos polvo (Exact Score con volumen 0-300 USD); las excepciones
interesantes son publicaciones de datos (JOLTS bins equivocados a 0,92-0,94
1,7 h tras el dato, vol ~4k USD) y earnings. Retorno 2-10 % en horas/días
-> anualizado enorme, capacidad diminuta, RIESGO = un solo lado equivocado
(-100 %). Por eso este observador mide lo que decide todo: el ACIERTO REAL
del lado ganador aparente (necesita >=99 %) y el tiempo real hasta asentar.

Por candidato (lado top por outcomePrices >=0,90, coste real de compra =
mejor ask del token ganador en CLOB, profundidad USD hasta coste+1c):
 - fila al verlo la primera vez y al cambiar coste/estado UMA (no cada ciclo)
 - al desaparecer de closed=false: fila de resolución con el desenlace final
   (gamma por condition_id), horas reales hasta asentar y si el lado ganador
   aparente acertó.
CSV: data/shadow/ya_decidido_universal_fase0.csv. Cron cada 10 min.
"""
import csv
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from sports_wallet_edge_tracker import clasificar  # noqa: E402

GAMMA = "https://gamma-api.polymarket.com"
DATA_API = "https://data-api.polymarket.com"
CLOB_BOOK = "https://clob.polymarket.com/book"
VENTANA_PASADO_H = 120
PRECIO_MIN = 0.90
OUT = REPO / "data" / "shadow" / "ya_decidido_universal_fase0.csv"
VISTOS = REPO / "data" / "shadow" / "ya_decidido_universal_fase0_vistos.json"
CAMPOS = ["timestamp_utc", "evento", "condition_id", "question", "end_date", "horas_desde_fin", "lado_ganador",
          "precio_outcome", "coste_real", "retorno_bruto", "profundidad_usd", "uma_status", "resolutions_status",
          "was_disputed", "expected_settlement_time", "settlement_time_basis", "volumen_usd", "categoria_txt",
          "primera_vez_visto_utc", "horas_hasta_resolver", "lado_final", "acierto_lado"]
_S = requests.Session()


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _es_excluido(m) -> bool:
    q = (m.get("question") or "") + " " + (m.get("slug") or "")
    if re.search(r"up or down|updown|-5m-|-15m-", q, re.I):
        return True
    if re.search(r"temperature|highest temp", q, re.I):
        return True
    return clasificar(m.get("question", ""), m.get("groupItemTitle") or m.get("slug", "")) is not None


def _categoria(m) -> str:
    q = (m.get("question") or "").lower()
    for k, pat in (("datos", r"jolts|cpi|nfp|payroll|gdp|unemployment|inflation|fed |fomc|etf flows|earnings|beat"),
                   ("elecciones", r"election|seats|mayor|president|vote"),
                   ("cripto", r"bitcoin|ethereum|solana|xrp|crypto|microstrategy"),
                   ("geopolitica", r"ukraine|russia|israel|iran|hormuz|strait|missile|war|target"),
                   ("cine", r"box office|opening weekend|movie"),
                   ("clima_sismos", r"earthquake|wind gust|hurricane")):
        if re.search(pat, q):
            return k
    return "otros"


def _listar():
    ahora = datetime.now(timezone.utc)
    corte = ahora - timedelta(hours=VENTANA_PASADO_H)
    out, off = [], 0
    while off < 2100:
        j = None
        for i in range(3):
            try:
                r = _S.get(f"{GAMMA}/markets", params={"closed": "false", "limit": 100, "offset": off,
                                                        "order": "endDate", "ascending": "false",
                                                        "end_date_max": ahora.strftime("%Y-%m-%dT%H:%M:%SZ")}, timeout=20)
                j = r.json()
                break
            except Exception:
                time.sleep(2 * (i + 1))
        if not isinstance(j, list) or not j:
            break
        stop = False
        for m in j:
            try:
                ed = datetime.fromisoformat(m["endDate"].replace("Z", "+00:00"))
            except Exception:
                continue
            if ed < corte:
                stop = True
                break
            out.append((m, ed))
        off += 100
        time.sleep(0.2)
        if stop:
            break
    return out


def _ask(token):
    try:
        r = _S.get(CLOB_BOOK, params={"token_id": token}, timeout=8)
        r.raise_for_status()
        asks = sorted((float(a["price"]), float(a["size"])) for a in (r.json().get("asks") or []))
        if not asks:
            return None, 0.0
        c = asks[0][0]
        return c, round(sum(p * s for p, s in asks if p <= c + 0.01), 2)
    except Exception:
        return None, 0.0


def _resolutions(cid):
    try:
        r = _S.get(f"{DATA_API}/v2/resolutions", params={"condition": cid}, timeout=8)
        rows = r.json().get("data") or []
        return rows[0] if rows else {}
    except Exception:
        return {}


def _final(cid):
    try:
        j = _S.get(f"{GAMMA}/markets", params={"condition_ids": cid}, timeout=15).json()
        if j:
            return j[0]
    except Exception:
        pass
    return None


def _escribir(filas):
    if not filas:
        return
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if nuevo:
            w.writeheader()
        for r in filas:
            w.writerow({c: r.get(c, "") for c in CAMPOS})


def main():
    _log("ya_decidido_universal_fase0 arrancado (solo lectura)")
    try:
        vistos = json.loads(VISTOS.read_text(encoding="utf-8"))
    except Exception:
        vistos = {}
    ahora = datetime.now(timezone.utc)
    lista = _listar()
    actuales, filas = set(), []
    for m, ed in lista:
        if _es_excluido(m):
            continue
        cid = m.get("conditionId")
        if not cid:
            continue
        actuales.add(cid)
        try:
            pr = [float(x) for x in json.loads(m.get("outcomePrices") or "[]")]
            outs = json.loads(m.get("outcomes") or "[]")
            toks = json.loads(m.get("clobTokenIds") or "[]")
        except Exception:
            continue
        if not pr or max(pr) < PRECIO_MIN:
            continue
        top = max(range(len(pr)), key=lambda i: pr[i])
        coste, prof = _ask(toks[top]) if top < len(toks) else (None, 0.0)
        res = _resolutions(cid)
        estado = (round(coste, 3) if coste is not None else None, m.get("umaResolutionStatus"), res.get("status"))
        prev = vistos.get(cid)
        if prev and prev.get("estado") == list(estado):
            continue
        primera = prev["primera"] if prev else ahora.isoformat(timespec="seconds")
        vistos[cid] = {"estado": list(estado), "primera": primera, "lado": outs[top] if top < len(outs) else "",
                       "top": top, "coste": coste, "end": ed.isoformat()}
        filas.append({"timestamp_utc": ahora.isoformat(timespec="seconds"), "evento": "visto" if not prev else "cambio",
                      "condition_id": cid, "question": (m.get("question") or "")[:140], "end_date": ed.isoformat(),
                      "horas_desde_fin": round((ahora - ed).total_seconds() / 3600, 2),
                      "lado_ganador": outs[top] if top < len(outs) else "", "precio_outcome": pr[top],
                      "coste_real": "" if coste is None else coste,
                      "retorno_bruto": "" if not coste or coste >= 1 else round((1 - coste) / coste, 4),
                      "profundidad_usd": prof, "uma_status": m.get("umaResolutionStatus") or "",
                      "resolutions_status": res.get("status", ""), "was_disputed": res.get("was_disputed", ""),
                      "expected_settlement_time": res.get("expected_settlement_time", ""),
                      "settlement_time_basis": res.get("settlement_time_basis", ""),
                      "volumen_usd": m.get("volumeNum", ""), "categoria_txt": _categoria(m),
                      "primera_vez_visto_utc": primera})
        time.sleep(0.15)
    # desaparecidos = asentados (o cerrados) desde la última corrida
    for cid in [c for c in vistos if c not in actuales]:
        v = vistos[cid]
        fm = _final(cid)
        if fm is not None and not fm.get("closed"):
            # salió de la ventana de listado (endDate > VENTANA_PASADO_H) pero sigue sin asentar: no es una resolución
            continue
        vistos.pop(cid)
        lado_final, acierto = "", ""
        if fm:
            try:
                pf = [float(x) for x in json.loads(fm.get("outcomePrices") or "[]")]
                outs = json.loads(fm.get("outcomes") or "[]")
                if pf and max(pf) > 0.99:
                    lado_final = outs[max(range(len(pf)), key=lambda i: pf[i])]
                    acierto = int(lado_final == v.get("lado"))
            except Exception:
                pass
        try:
            h = round((ahora - datetime.fromisoformat(v["primera"])).total_seconds() / 3600, 2)
        except Exception:
            h = ""
        filas.append({"timestamp_utc": ahora.isoformat(timespec="seconds"), "evento": "resuelto", "condition_id": cid,
                      "lado_ganador": v.get("lado", ""), "coste_real": v.get("coste") or "", "end_date": v.get("end", ""),
                      "primera_vez_visto_utc": v["primera"], "horas_hasta_resolver": h, "lado_final": lado_final,
                      "acierto_lado": acierto, "question": (fm or {}).get("question", "")[:140] if fm else ""})
    _escribir(filas)
    VISTOS.write_text(json.dumps(vistos), encoding="utf-8")
    _log(f"{len(lista)} mercados fin-pasado, {len(actuales)} no excluidos, {len(filas)} filas escritas, "
         f"{len(vistos)} en seguimiento")


if __name__ == "__main__":
    main()
