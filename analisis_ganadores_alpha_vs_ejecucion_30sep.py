#!/usr/bin/env python3
"""analisis_ganadores_alpha_vs_ejecucion_30sep.py -- ¿CÓMO ganan las wallets que ganan en up/down cripto?

Petición Javi 30-Sep: "hay miles de billeteras minando pasta en cripto con edge validado... tienes
que entender qué variables hacen que cada estrategia falle y cómo hacer que funcionen".

Misma descomposición que analisis_alpha_vs_execution_edge_30sep.py, aplicada a TODAS las wallets
del firehose (polymarket_activity_*.csv: cada transacción trae al tomador y a los makers) en los
mercados up/down de 5 y 15 min de las 6 monedas:

  PnL por wallet  = caja (ventas - compras) + posición final x pago (1 si gana su outcome)
  por trade       : ejecución = (mid - precio) x size en compras, (precio - mid) x size en ventas
                    alpha     = (pago - mid) x size en compras, (mid - pago) x size en ventas
  mid             = (bid+ask)/2 del outcome en libro_ambos_lados, último snapshot <= trade (<=20 s)
  rol             = en transacciones de >=3 filas, el tomador es la fila cuyo size iguala la suma
                    del resto; las demás son makers. En las de 2 filas no se puede saber ("?").
  fee estimado    = 0,07 x p x (1-p) x size solo para el tomador (los makers no pagan).

Solo lectura. Salida: data/shadow/ganadores_alpha_vs_ejecucion.json + tablas por pantalla.
Uso: python3 analisis_ganadores_alpha_vs_ejecucion_30sep.py 2026-09-27 2026-09-28 2026-09-29
"""
import bisect
import csv
import gzip
import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
OUT = REPO / "data" / "shadow" / "ganadores_alpha_vs_ejecucion.json"
MARCOS = ("5min", "15min")
EDAD_MAX_MID_S = 20
FEE = 0.07


def _abrir(base: Path):
    for p in (base, Path(str(base) + ".gz")):
        if p.exists():
            return gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")
    return None


def _ts(s: str) -> float:
    return datetime.fromisoformat(s).timestamp()


def cargar_desenlaces(dias):
    out = {}
    for d in dias:
        f = _abrir(REPO / "data" / "shadow" / f"resolution_sniper_obs_{d}.csv")
        if f is None:
            continue
        with f:
            for r in csv.DictReader(f):
                if r.get("outcome_real") in ("Up", "Down"):
                    out[r["slug"]] = r["outcome_real"]
    return out


def cargar_mids(dias):
    """condition_id -> ([ts], [mid_up])"""
    serie = defaultdict(list)
    for d in dias:
        f = _abrir(DATALOGS / f"libro_ambos_lados_{d}.csv")
        if f is None:
            continue
        with f:
            for r in csv.DictReader(f):
                if r.get("marco") not in MARCOS:
                    continue
                try:
                    b, a = float(r["bid_yes"]), float(r["ask_yes"])
                except (ValueError, TypeError):
                    continue
                if 0 < b <= a < 1:
                    serie[r["condition_id"]].append((_ts(r["timestamp_utc"]), (a + b) / 2))
    out = {}
    for c, v in serie.items():
        v.sort()
        out[c] = ([t for t, _ in v], [m for _, m in v])
    return out


def nuevo():
    return {"n": 0, "vol": 0.0, "caja": 0.0, "pos": defaultdict(float), "alpha": 0.0, "ejec": 0.0,
            "vol_mid": 0.0, "fee": 0.0, "n_tomador": 0, "n_maker": 0, "n_rol": 0, "vol_compra": 0.0,
            "mercados": set(), "ambos_lados": set(), "lados": defaultdict(set), "sum_precio_vol": 0.0,
            "dias": set(), "pnl_dia": defaultdict(float), "resto_s": []}


def main() -> int:
    dias = sys.argv[1:] or ["2026-09-27", "2026-09-28", "2026-09-29"]
    out = cargar_desenlaces(dias)
    mids = cargar_mids(dias)
    print(f"mercados con desenlace: {len(out)} | mercados con libro: {len(mids)}", flush=True)
    W = defaultdict(nuevo)
    rol_total = {"tomador": [0.0, 0.0, 0.0, 0.0], "maker": [0.0, 0.0, 0.0, 0.0], "?": [0.0, 0.0, 0.0, 0.0]}  # vol, alpha, ejec, fee

    def procesar_tx(filas):
        # rol por transacción
        roles = ["?"] * len(filas)
        if len(filas) >= 3:
            sizes = [f[5] for f in filas]
            i = max(range(len(filas)), key=lambda k: sizes[k])
            resto = sum(sizes) - sizes[i]
            if resto > 0 and abs(sizes[i] - resto) / resto < 0.02:
                roles = ["maker"] * len(filas)
                roles[i] = "tomador"
        for (w, slug, cid, outcome, side, size, price, t, dia), rol in zip(filas, roles):
            gan = out.get(slug)
            if gan is None:
                continue
            a = W[w]
            pago = 1.0 if outcome == gan else 0.0
            signo = 1 if side == "BUY" else -1
            a["n"] += 1
            a["vol"] += size * price
            a["sum_precio_vol"] += price * size * price
            a["caja"] -= signo * size * price
            a["pos"][(slug, outcome)] += signo * size
            a["mercados"].add(slug)
            a["lados"][slug].add(outcome)
            a["dias"].add(dia)
            pnl_trade = signo * size * (pago - price)      # aditivo: suma = caja + posición x pago
            a["pnl_dia"][dia] += pnl_trade
            if side == "BUY":
                a["vol_compra"] += size * price
            if rol != "?":
                a["n_rol"] += 1
                a["n_tomador" if rol == "tomador" else "n_maker"] += 1
            fee = FEE * price * (1 - price) * size if rol == "tomador" else 0.0
            a["fee"] += fee
            try:
                fin = int(slug.rsplit("-", 1)[1]) + (300 if "-5m-" in slug else 900)
                if len(a["resto_s"]) < 5000:
                    a["resto_s"].append(fin - t)
            except (ValueError, IndexError):
                pass
            m = mids.get(cid)
            if m:
                i = bisect.bisect_right(m[0], t) - 1
                if i >= 0 and t - m[0][i] <= EDAD_MAX_MID_S:
                    mid = m[1][i] if outcome == "Up" else 1 - m[1][i]
                    al, ej = signo * size * (pago - mid), signo * size * (mid - price)
                    a["alpha"] += al
                    a["ejec"] += ej
                    a["vol_mid"] += size * price
                    r = rol_total[rol]
                    r[0] += size * price
                    r[1] += al
                    r[2] += ej
                    r[3] += fee

    for d in dias:
        f = _abrir(DATALOGS / f"polymarket_activity_{d}.csv")
        if f is None:
            print(f"{d}: sin fichero de actividad")
            continue
        n = 0
        tx_act, filas = None, []
        with f:
            for r in csv.DictReader(f):
                if r.get("categoria_updown_tracked") != "1" or r.get("marco") not in MARCOS:
                    continue
                try:
                    size, price = float(r["size"]), float(r["price"])
                    t = _ts(r["timestamp_utc"])
                except (ValueError, TypeError):
                    continue
                if size <= 0 or not (0 < price < 1) or r["outcome"] not in ("Up", "Down"):
                    continue
                clave = (r["transaction_hash"], r["condition_id"])
                if clave != tx_act:
                    if filas:
                        procesar_tx(filas)
                    tx_act, filas = clave, []
                filas.append((r["wallet"].lower(), r["market_slug"], r["condition_id"], r["outcome"],
                              r["side"], size, price, t, d))
                n += 1
            if filas:
                procesar_tx(filas)
        print(f"{d}: {n} fills up/down 5-15 min", flush=True)

    res = []
    for w, a in W.items():
        pnl = sum(a["pnl_dia"].values())
        res.append({
            "wallet": w, "n": a["n"], "vol": round(a["vol"], 0), "pnl": round(pnl, 2),
            "pnl_pct_vol": round(pnl / a["vol"] * 100, 2) if a["vol"] else 0,
            "alpha": round(a["alpha"], 2), "ejec": round(a["ejec"], 2), "fee_est": round(a["fee"], 2),
            "cobertura_mid_pct": round(a["vol_mid"] / a["vol"] * 100) if a["vol"] else 0,
            "pct_maker": round(a["n_maker"] / a["n_rol"] * 100) if a["n_rol"] else None,
            "pct_compra": round(a["vol_compra"] / a["vol"] * 100) if a["vol"] else 0,
            "precio_medio": round(a["sum_precio_vol"] / a["vol"], 3) if a["vol"] else 0,
            "mercados": len(a["mercados"]),
            "pct_mercados_ambos_lados": round(sum(1 for s in a["lados"].values() if len(s) == 2) / len(a["mercados"]) * 100),
            "resto_s_mediana": sorted(a["resto_s"])[len(a["resto_s"]) // 2] if a["resto_s"] else None,
            "dias_positivos": f"{sum(1 for v in a['pnl_dia'].values() if v > 0)}/{len(a['pnl_dia'])}",
        })
    activos = [r for r in res if r["n"] >= 200]
    print(f"\nwallets: {len(res)} | con >=200 fills: {len(activos)} | de esas, con PnL>0: {sum(r['pnl'] > 0 for r in activos)}")
    print(f"PnL total de todas las wallets (suma cero antes de fees): {sum(r['pnl'] for r in res):.0f} $ | fee estimado pagado por tomadores: {sum(r['fee_est'] for r in res):.0f} $")
    print("\nPor ROL (solo fills con rol identificado y mid): volumen, alpha, ejecución, fee")
    for rol, (v, al, ej, fe) in rol_total.items():
        if v:
            print(f"  {rol:8s} vol {v:12.0f} $ | alpha {al:10.0f} ({al / v * 100:+.2f}%) | ejecución {ej:10.0f} ({ej / v * 100:+.2f}%) | fee {fe:8.0f} ({fe / v * 100:.2f}%) | neto {(al + ej - fe) / v * 100:+.2f}% del volumen")

    def tabla(titulo, filas):
        print(f"\n== {titulo} ==")
        print(f"{'wallet':12s} {'fills':>6s} {'vol$':>9s} {'PnL$':>8s} {'%vol':>6s} {'alpha$':>8s} {'ejec$':>8s} {'fee$':>6s} {'mid%':>4s} {'maker%':>6s} {'compra%':>7s} {'precio':>6s} {'merc':>5s} {'2lados%':>7s} {'resto_s':>7s} {'días+':>5s}")
        for r in filas:
            print(f"{r['wallet'][:12]:12s} {r['n']:6d} {r['vol']:9.0f} {r['pnl']:8.0f} {r['pnl_pct_vol']:6.2f} {r['alpha']:8.0f} {r['ejec']:8.0f} "
                  f"{r['fee_est']:6.0f} {r['cobertura_mid_pct']:4d} {str(r['pct_maker']):>6s} {r['pct_compra']:7d} {r['precio_medio']:6.3f} "
                  f"{r['mercados']:5d} {r['pct_mercados_ambos_lados']:7d} {str(int(r['resto_s_mediana'])) if r['resto_s_mediana'] is not None else '':>7s} {r['dias_positivos']:>5s}")

    top = sorted(activos, key=lambda r: -r["pnl"])
    tabla("TOP 25 por PnL (>=200 fills)", top[:25])
    tabla("PEORES 10 por PnL (>=200 fills)", top[-10:])
    gan = [r for r in activos if r["pnl"] > 0]
    per = [r for r in activos if r["pnl"] <= 0]
    for nombre, g in (("GANADORAS", gan), ("PERDEDORAS", per)):
        v = sum(r["vol"] for r in g)
        vm = sum(r["vol"] * r["cobertura_mid_pct"] / 100 for r in g)
        if v and vm:
            con_rol = [r for r in g if r["pct_maker"] is not None]
            print(f"\n{nombre} (>=200 fills): {len(g)} wallets | vol {v:.0f} $ | PnL {sum(r['pnl'] for r in g):.0f} $ ({sum(r['pnl'] for r in g) / v * 100:+.2f}% del vol) | "
                  f"alpha {sum(r['alpha'] for r in g) / vm * 100:+.2f}% | ejecución {sum(r['ejec'] for r in g) / vm * 100:+.2f}% | "
                  f"% maker mediano {sorted(r['pct_maker'] for r in con_rol)[len(con_rol) // 2] if con_rol else None} | "
                  f"mediana de '% mercados con ambos lados' {sorted(r['pct_mercados_ambos_lados'] for r in g)[len(g) // 2]}")
    OUT.write_text(json.dumps({"dias": dias, "rol_total": rol_total, "top": top[:100], "peores": top[-50:],
                               "n_wallets": len(res), "n_activas": len(activos)}, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
