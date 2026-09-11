"""P13 (11-Ago, sesión, pendiente de idea_manipulacion... / project_twap_chainlink):
¿el ruido Binance/Kraken (o_inner/o_outer del scanner) invierte el orden real
de las aperturas (Chainlink) y eso explica las roturas de garantía del arb
anidado? Solo lectura, no toca dinero ni decide nada -- responde la pregunta
dejada pendiente en project_twap_chainlink_confirmado_09ago (punto 6).
"""
import csv
import bisect
from datetime import datetime, timedelta, timezone
from pathlib import Path

DIR_PRICES = Path("data/prices")
SIM_CSV = Path("data/shadow/nested_arb_sim.csv")

DUR = {"5min15m": (5, 15), "15min60m": (15, 60)}


def parse_iso(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def cargar_chainlink(fechas):
    series = {}  # asset -> (list_ts_epoch, list_price)
    for fecha in fechas:
        p = DIR_PRICES / f"chainlink_{fecha}.csv"
        if not p.exists():
            continue
        with open(p) as f:
            r = csv.DictReader(f)
            for row in r:
                try:
                    ts = parse_iso(row["timestamp_utc"]).timestamp()
                    px = float(row["price_usd"])
                except Exception:
                    continue
                a = row["asset"]
                series.setdefault(a, [[], []])
                series[a][0].append(ts)
                series[a][1].append(px)
    for a in series:
        # ya vienen ~ordenados por archivo/fecha, pero aseguramos
        combo = sorted(zip(series[a][0], series[a][1]))
        series[a][0] = [c[0] for c in combo]
        series[a][1] = [c[1] for c in combo]
    return series


def precio_en(series, asset, dt, tol_s=15):
    if asset not in series:
        return None
    ts_list, px_list = series[asset]
    target = dt.timestamp()
    i = bisect.bisect_left(ts_list, target)
    candidatos = []
    if i < len(ts_list):
        candidatos.append(i)
    if i > 0:
        candidatos.append(i - 1)
    mejor = None
    mejor_d = None
    for c in candidatos:
        d = abs(ts_list[c] - target)
        if mejor_d is None or d < mejor_d:
            mejor_d = d
            mejor = c
    if mejor is None or mejor_d > tol_s:
        return None
    return px_list[mejor]


def main():
    filas = []
    with open(SIM_CSV) as f:
        r = csv.DictReader(f)
        for row in r:
            if row.get("status") != "CLOSED":
                continue
            end_utc = row.get("end_utc")
            if not end_utc or end_utc < "2026-08-06":
                continue
            filas.append(row)

    fechas = sorted({row["end_utc"][:10] for row in filas})
    # margen: necesitamos también el día anterior por si inner_ini/outer_ini cae antes de medianoche
    fechas_ext = sorted(set(fechas) | {
        (datetime.fromisoformat(f).date() - timedelta(days=1)).isoformat() for f in fechas
    })
    series = cargar_chainlink(fechas_ext)
    print(f"Chainlink cargado: {[(a, len(v[0])) for a, v in series.items()]}")
    print(f"Filas CLOSED desde 06-Ago: {len(filas)}")

    n_total = 0
    n_rotura = 0
    n_mismatch = 0
    n_mismatch_rotura = 0
    n_sin_dato = 0
    detalle = []

    for row in filas:
        nesting = row.get("nesting")
        dur = DUR.get(nesting)
        if not dur:
            continue
        end_dt = parse_iso(row["end_utc"])
        inner_ini = end_dt - timedelta(minutes=dur[0])
        outer_ini = end_dt - timedelta(minutes=dur[1])
        act = row["activo"]

        px_in_cl = precio_en(series, act, inner_ini)
        px_out_cl = precio_en(series, act, outer_ini)
        if px_in_cl is None or px_out_cl is None:
            n_sin_dato += 1
            continue

        try:
            gap_kl_pct = float(row["gap_opens_pct"]) if row.get("gap_opens_pct") not in (None, "") else None
        except Exception:
            gap_kl_pct = None
        if gap_kl_pct is None:
            n_sin_dato += 1
            continue

        gap_cl_pct = (px_in_cl / px_out_cl - 1) * 100
        signo_kl = gap_kl_pct >= 0
        signo_cl = gap_cl_pct >= 0
        mismatch = signo_kl != signo_cl
        rotura = row.get("garantia_ok") in ("False", "0", "false")

        n_total += 1
        if rotura:
            n_rotura += 1
        if mismatch:
            n_mismatch += 1
            if rotura:
                n_mismatch_rotura += 1

        detalle.append({
            "activo": act, "end_utc": row["end_utc"], "combo": row["combo"],
            "px_in_cl": round(px_in_cl, 2), "px_out_cl": round(px_out_cl, 2),
            "gap_kl_pct": round(gap_kl_pct, 4),
            "gap_cl_pct": round(gap_cl_pct, 4),
            "mismatch": mismatch, "rotura": rotura,
            "pnl_usd": row.get("pnl_usd"),
        })

    print(f"\nSin dato chainlink suficiente: {n_sin_dato}")
    print(f"Total evaluado: {n_total}  roturas: {n_rotura} ({n_rotura/n_total*100:.1f}%)" if n_total else "sin datos")
    print(f"Mismatch orden (klines vs chainlink): {n_mismatch}/{n_total} ({n_mismatch/n_total*100:.1f}%)" if n_total else "")
    if n_mismatch:
        print(f"  De esos mismatch, roturas: {n_mismatch_rotura}/{n_mismatch} ({n_mismatch_rotura/n_mismatch*100:.1f}%)")
    n_no_mismatch = n_total - n_mismatch
    n_rotura_no_mismatch = n_rotura - n_mismatch_rotura
    if n_no_mismatch:
        print(f"  Sin mismatch, roturas: {n_rotura_no_mismatch}/{n_no_mismatch} ({n_rotura_no_mismatch/n_no_mismatch*100:.1f}%)")

    print("\n--- Detalle de roturas ---")
    for d in detalle:
        if d["rotura"]:
            print(d)

    print("\n--- Detalle de mismatch (sea rotura o no) ---")
    for d in detalle:
        if d["mismatch"]:
            print(d)


if __name__ == "__main__":
    main()
