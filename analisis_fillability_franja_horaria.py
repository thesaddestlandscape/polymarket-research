#!/usr/bin/env python3
"""analisis_fillability_franja_horaria.py — Fill-ability real (libro CLOB) de
las bandas milimétricas con edge que sobreviven BH-FDR (22-Jul, parte 2 de la
petición explícita de Javi: "Después instrumenta fill-ability de todas las
monedas por franja horaria, para las bandas milimétricas donde tienen carne").

Decisión ladder (CLAUDE.md) aplicada antes de escribir nada: NO hace falta
ningún capturador nuevo. `live_trade.py::_snapshots_por_lista()` ya consulta
el libro real cada ciclo para prácticamente todas las tuplas strategy#subtype
#direction activas (candidatos_evaluacion_live, expandido hoy a 225 combos =
cobertura total del histórico) y acumula en data/live/libro_snapshots.csv con
`ratio_vs_stake` -- exactamente el dato de fill-ability que hace falta. Este
script solo CRUZA lo que ya existe: cada fila de libro_snapshots.csv trae su
propio precio_plan (bucketable igual que ballenas_timing_history.csv) y su
propio timestamp (hora UTC) -- se le puede preguntar directamente "¿esta
observación de libro cae dentro de una banda con carne (activo,marco,hora)?"
sin capturar nada nuevo. Mismo principio de reutilización que analisis_fills.py
(el script ya existente que decide reapertura del live con esta misma fuente).

Umbral de fill-ability = ratio_vs_stake >= min_profundidad_ratio_libro (5.0),
el MISMO umbral que ya usa el veto de profundidad real en producción
(live_trade.py) -- no se inventa un criterio nuevo.

Solo lectura. No decide nada, no toca prob_yes ni ningún gate real.
"""
import csv
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent
SNAPSHOTS = REPO / "data" / "live" / "libro_snapshots.csv"
FRANJA_HORARIA = REPO / "data" / "shadow" / "franja_milimetrica_horaria.json"
OUT = REPO / "data" / "shadow" / "fillability_franja_horaria.json"
RATIO_MIN = 5.0  # == config_live.json riesgo.min_profundidad_ratio_libro

MARCO_MAP = {"5min": "5m", "15min": "15m", "60min": "60m", "240min": "240m", "weekly": "weekly"}
STEP = 0.05
N_MIN_INFORMATIVO = 15


def bucket(p):
    return round((p // STEP) * STEP, 3)


def cargar_carne():
    """clave 'ACTIVO#marco#hHH' -> set de (banda_lo) que sobrevivieron BH-FDR."""
    if not FRANJA_HORARIA.exists():
        raise SystemExit(f"Falta {FRANJA_HORARIA} -- correr antes analisis_franja_milimetrica_horaria.py")
    raw = json.loads(FRANJA_HORARIA.read_text(encoding="utf-8"))
    return {clave: {c["banda_lo"] for c in candidatas} for clave, candidatas in raw.items()}


def main():
    carne = cargar_carne()
    print(f"Combos (activo,marco,hora) con banda 'con carne' (post BH-FDR): {len(carne)}")

    # motivo -> observación real del libro; 'ejecutada' incluida (fill real).
    # No se dedup por señal (a diferencia de analisis_fills.py): aquí cada
    # fila es una observación de PRECIO+libro distinta y point-in-time -- el
    # objeto de medida es la banda de precio, no el resultado de una señal
    # única. _snapshot_senal_bloqueada ya deduplica en origen (1 fila por
    # market_id+direction+motivo-grupo), así que no hay doble conteo del
    # mismo instante.
    stats = defaultdict(lambda: {"n": 0, "n_fillable": 0, "suma_ratio": 0.0, "n_con_ratio": 0,
                                  "motivos": defaultdict(int)})

    n_filas = 0
    n_sin_banda_carne = 0
    with open(SNAPSHOTS, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            n_filas += 1
            subtype = row.get("subtype", "")
            if "#" not in subtype:
                continue
            activo, marco_raw = subtype.split("#", 1)
            marco = MARCO_MAP.get(marco_raw)
            if marco is None:
                continue
            try:
                precio = float(row["precio_plan"])
                hora = datetime.fromisoformat(row["timestamp_utc"]).hour
            except (TypeError, ValueError, KeyError):
                continue
            clave_hora = f"{activo}#{marco}#h{hora:02d}"
            bandas_carne = carne.get(clave_hora)
            if not bandas_carne:
                n_sin_banda_carne += 1
                continue
            b = bucket(precio)
            if b not in bandas_carne:
                n_sin_banda_carne += 1
                continue
            clave = f"{clave_hora}#[{b:.2f},{b+STEP:.2f})"
            s = stats[clave]
            s["n"] += 1
            s["motivos"][row.get("motivo", "")] += 1
            ratio_raw = row.get("ratio_vs_stake", "")
            if ratio_raw not in ("", None):
                try:
                    ratio = float(ratio_raw)
                    s["suma_ratio"] += ratio
                    s["n_con_ratio"] += 1
                    if ratio >= RATIO_MIN:
                        s["n_fillable"] += 1
                except ValueError:
                    pass

    print(f"Filas totales en libro_snapshots.csv: {n_filas}")
    print(f"Filas fuera de cualquier banda 'con carne' (activo/marco/hora/precio no coincide): {n_sin_banda_carne}")
    print(f"Filas DENTRO de una banda con carne (cruce real): {sum(s['n'] for s in stats.values())}")

    resultado = {}
    for clave, s in stats.items():
        n = s["n"]
        n_con_ratio = s["n_con_ratio"]
        entrada = {
            "n": n,
            "n_con_ratio_libro": n_con_ratio,
            "fill_rate": round(s["n_fillable"] / n_con_ratio, 4) if n_con_ratio else None,
            "ratio_medio": round(s["suma_ratio"] / n_con_ratio, 2) if n_con_ratio else None,
            "motivos": dict(s["motivos"]),
            "informativo_n15": n_con_ratio >= N_MIN_INFORMATIVO,
        }
        resultado[clave] = entrada

    con_dato = {k: v for k, v in resultado.items() if v["n_con_ratio_libro"] >= N_MIN_INFORMATIVO}
    print(f"\nCombos banda+hora con carne Y n>=15 de fill-ability real: {len(con_dato)}")
    print(f"(de {len(resultado)} combos banda+hora con carne que tienen AL MENOS 1 observación de libro)")

    filas = sorted(con_dato.items(), key=lambda kv: kv[1]["fill_rate"])
    print(f"\n{'combo#banda':38} {'n':>5} {'fill_rate':>10} {'ratio_medio':>12}  motivos")
    for k, v in filas:
        print(f"{k:38} {v['n_con_ratio_libro']:5} {v['fill_rate']*100:9.1f}% {v['ratio_medio']:12.2f}  {v['motivos']}")

    huecos = [k for k in carne if not any(kk.startswith(k + "#") for kk in resultado)]
    print(f"\nCombos con carne (BH-FDR) SIN NINGÚN dato de libro todavía (huecos de cobertura): {len(huecos)}")
    if huecos:
        print("  " + ", ".join(sorted(huecos)[:30]) + (" ..." if len(huecos) > 30 else ""))

    OUT.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
