#!/usr/bin/env python3
"""
analisis_p33_persistencia_fee_libro_13ago.py -- P33 (idea_p33_arbitraje_umbrales_
precio_monotonia_12ago): verifica los 3 pendientes del hallazgo de ayer antes de
proponer nada ejecutable -- persistencia multi-día, fee real, profundidad de libro.
Solo lectura, no toca dinero ni ninguna decisión. Reusa el mismo parseo de
"(reach|dip to) $X" que el análisis original del 12-Ago.
"""
import re
import sys
import json
from collections import defaultdict

import pandas as pd
import requests

DIAS = ["2026-08-09", "2026-08-10", "2026-08-11", "2026-08-12", "2026-08-13"]
COLS = ["timestamp_utc", "market_id", "condition_id", "question", "slug",
        "end_date", "liquidity", "price_yes", "best_bid", "best_ask",
        "event_id", "event_title"]

PAT = re.compile(r"\b(reach|dip to)\s*\$([\d,]+\.?\d*)", re.IGNORECASE)


def parsear_umbral(pregunta):
    m = PAT.search(pregunta)
    if not m:
        return None, None
    direccion = m.group(1).lower()
    umbral = float(m.group(2).replace(",", ""))
    return direccion, umbral


def cargar_dia_filtrado(fecha):
    """Lee solo filas con 'reach $' o 'dip to $' en la pregunta, última
    snapshot del día por market_id."""
    path = f"data/markets/{fecha}.csv"
    chunks = []
    for chunk in pd.read_csv(path, usecols=COLS, chunksize=200_000,
                              on_bad_lines="skip"):
        mask = chunk["question"].str.contains(r"(reach|dip to)\s*\$", case=False,
                                                regex=True, na=False)
        if mask.any():
            chunks.append(chunk[mask])
    if not chunks:
        return pd.DataFrame(columns=COLS)
    df = pd.concat(chunks, ignore_index=True)
    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"])
    # última snapshot del día por market_id (precio más reciente y estable)
    df = df.sort_values("timestamp_utc").groupby("market_id", as_index=False).last()
    df["direccion"], df["umbral"] = zip(*df["question"].map(parsear_umbral))
    df = df.dropna(subset=["direccion", "umbral"])
    return df


def extraer_fecha_evento(pregunta):
    m = re.search(r"by\s+([A-Za-z]+\s+\d{1,2},?\s*\d{4}|\d{4}-\d{2}-\d{2})", pregunta)
    return m.group(1) if m else "sin_fecha"


def detectar_violaciones(df):
    df = df.copy()
    df["fecha_evento"] = df["question"].map(extraer_fecha_evento)
    violaciones = []
    for (event_id, direccion, fecha_evento), grupo in df.groupby(
            ["event_id", "direccion", "fecha_evento"]):
        grupo = grupo.sort_values("umbral")
        if len(grupo) < 2:
            continue
        filas = grupo.to_dict("records")
        for i in range(len(filas) - 1):
            a, b = filas[i], filas[i + 1]  # a.umbral < b.umbral
            if direccion == "reach":
                # P(reach umbral alto) debe ser <= P(reach umbral bajo)
                viola = b["price_yes"] > a["price_yes"]
                gap = b["price_yes"] - a["price_yes"]
            else:  # dip to
                # P(dip umbral alto, más cerca del spot) debe ser >= P(dip umbral bajo)
                viola = b["price_yes"] < a["price_yes"]
                gap = a["price_yes"] - b["price_yes"]
            if viola and gap > 0.001:
                violaciones.append({
                    "event_title": a["event_title"], "direccion": direccion,
                    "fecha_evento": fecha_evento,
                    "umbral_bajo": a["umbral"], "umbral_alto": b["umbral"],
                    "p_bajo": round(a["price_yes"], 4), "p_alto": round(b["price_yes"], 4),
                    "gap_pp": round(gap * 100, 2),
                    "liq_bajo": round(a["liquidity"], 1), "liq_alto": round(b["liquidity"], 1),
                    "bid_bajo": a["best_bid"], "ask_bajo": a["best_ask"],
                    "bid_alto": b["best_bid"], "ask_alto": b["best_ask"],
                    "condition_id_bajo": a["condition_id"], "condition_id_alto": b["condition_id"],
                    "slug_bajo": a["slug"], "slug_alto": b["slug"],
                })
    return pd.DataFrame(violaciones)


def main():
    print("=== Paso 1: cargar y detectar violaciones por día ===")
    resultados_por_dia = {}
    for fecha in DIAS:
        try:
            df = cargar_dia_filtrado(fecha)
        except FileNotFoundError:
            print(f"{fecha}: fichero no encontrado, salto")
            continue
        viol = detectar_violaciones(df)
        resultados_por_dia[fecha] = viol
        print(f"{fecha}: {len(df)} mercados 'reach/dip' encontrados, "
              f"{len(viol)} violaciones de monotonía")

    print("\n=== Paso 2: persistencia -- ¿las mismas parejas violan varios días? ===")
    conteo_pares = defaultdict(list)
    for fecha, viol in resultados_por_dia.items():
        if viol.empty:
            continue
        for _, row in viol.iterrows():
            clave = (row["event_title"], row["direccion"], row["umbral_bajo"], row["umbral_alto"])
            conteo_pares[clave].append((fecha, row["gap_pp"], row["liq_bajo"], row["liq_alto"],
                                         row["ask_bajo"], row["bid_alto"]))

    persistentes = {k: v for k, v in conteo_pares.items() if len(v) >= 3}
    print(f"Pares (evento,dirección,umbral_bajo,umbral_alto) que violan monotonía "
          f"en >=3/{len(resultados_por_dia)} días: {len(persistentes)} de {len(conteo_pares)} totales")

    for clave, apariciones in sorted(persistentes.items(), key=lambda kv: -len(kv[1]))[:15]:
        evento, direccion, u_bajo, u_alto = clave
        dias_str = ",".join(a[0][-2:] for a in apariciones)
        gaps = [a[1] for a in apariciones]
        liq_min = min(min(a[2], a[3]) for a in apariciones)
        print(f"  {evento[:50]:50s} {direccion} ${u_bajo:g}/${u_alto:g}  "
              f"días={dias_str}  gap_pp={gaps}  liq_min={liq_min:.0f}")

    print("\n=== Paso 3: fee real de estos mercados (gamma-api, mercado de HOY) ===")
    if not resultados_por_dia.get("2026-08-13", pd.DataFrame()).empty:
        cid_muestra = resultados_por_dia["2026-08-13"].iloc[0]["condition_id_bajo"]
    else:
        # coger cualquier condition_id de cualquier día disponible
        cid_muestra = None
        for viol in resultados_por_dia.values():
            if not viol.empty:
                cid_muestra = viol.iloc[0]["condition_id_bajo"]
                break
    if cid_muestra:
        try:
            r = requests.get("https://gamma-api.polymarket.com/markets",
                              params={"condition_ids": cid_muestra}, timeout=15)
            data = r.json()
            if data:
                m = data[0]
                print(f"  condition_id={cid_muestra}")
                print(f"  question={m.get('question')}")
                print(f"  feeSchedule/fee fields relevantes:")
                for k in ["fee", "feeRateBps", "makerBaseFee", "takerBaseFee",
                          "rewardsMinSize", "rewardsMaxSpread", "clobTokenIds"]:
                    if k in m:
                        print(f"    {k} = {m[k]}")
        except Exception as e:
            print(f"  ERROR consultando gamma-api: {e}")
    else:
        print("  sin condition_id de muestra disponible")

    print("\n=== Guardando resultado completo ===")
    out = {
        "generado_utc": pd.Timestamp.utcnow().isoformat(),
        "dias_analizados": list(resultados_por_dia.keys()),
        "n_violaciones_por_dia": {f: len(v) for f, v in resultados_por_dia.items()},
        "n_pares_persistentes_3mas_dias": len(persistentes),
        "pares_persistentes": [
            {
                "event_title": k[0], "direccion": k[1],
                "umbral_bajo": k[2], "umbral_alto": k[3],
                "apariciones": [{"fecha": a[0], "gap_pp": a[1],
                                  "liq_bajo": a[2], "liq_alto": a[3],
                                  "ask_bajo": a[4], "bid_alto": a[5]} for a in v],
            }
            for k, v in persistentes.items()
        ],
    }
    with open("data/shadow/p33_persistencia_fee_13ago.json", "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False, default=str)
    print("Guardado en data/shadow/p33_persistencia_fee_13ago.json")


if __name__ == "__main__":
    main()
