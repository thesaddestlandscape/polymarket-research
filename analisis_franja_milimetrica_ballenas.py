#!/usr/bin/env python3
"""Franja milimétrica ballenas — cruce a resolución fina (no la banda única
[0.70,0.90) que usa el resto del sistema) de TRES fuentes por (activo,marco):

  1. BALLENAS  — ballenas_timing_history.csv: TODAS las compras de TODAS las
     wallets en TODOS los mercados resueltos de nuestro nicho (no solo las
     "smart"), vía /trades real de Polymarket. Es el histórico completo de
     mercado, no filtrado por si nuestras estrategias dispararon o no ahí.
  2. SHADOW    — results.csv: qué habría pasado con cada predicción nuestra
     (todas las estrategias BUY_YES#15min activas), solo en los precios
     donde SÍ generamos señal.
  3. REAL      — trades.csv: lo que de verdad hemos operado con dinero desde
     que estamos en live, agregado por (activo,marco,BUY_YES) porque el n
     real es bajo.

Objetivo (petición explícita Javi, 21-Jul): detectar no solo el patrón
"dentro/fuera de banda" ya validado con gate riguroso, sino HUECOS DE
COBERTURA — franjas de precio donde las ballenas aciertan mucho y nosotros
apenas operamos (shadow_n bajo o cero), que es donde puede haber edge sin
explotar todavía, no solo refinamiento de lo que ya hacemos.

Solo lectura. No decide nada, no toca prob_yes ni ningún gate real. Pensado
para correr cada inicio de sesión (petición Javi 21-Jul) y ver cómo crece n
en cada bucket fino día a día antes de decidir cortar nada con más precisión
que la banda agregada actual.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
BALLENAS_HIST = REPO / "data" / "shadow" / "ballenas_timing_history.csv"
RESULTS = REPO / "data" / "shadow" / "results.csv"
TRADES = REPO / "data" / "live" / "trades.csv"
OUT = REPO / "data" / "shadow" / "franja_milimetrica_ballenas.json"

STEP = 0.05
ACTIVOS = ("BTC", "ETH", "SOL")
MARCO = "15min"          # nomenclatura resultado/trades ("...#15min")
MARCO_BALLENAS = "15m"   # nomenclatura ballenas_timing_history.csv
FAMILIAS_SHADOW = (
    "FAVORITO_CONFIRMADO", "UPDOWN_GBM", "GBM_LATE_15M",
    "GBM_LATE_15M_ESPACIO_ATR", "GBM_LATE_15M_TARDIO",
)
N_MIN_BUCKET_INFORMATIVO = 15   # regla del proyecto: nada se concluye por debajo
N_MIN_BUCKET_MADURO = 40        # umbral de gate riguroso


def bucket(p):
    return round((p // STEP) * STEP, 3)


def cargar_ballenas():
    """activo -> bucket -> [aciertos, n] sobre TODAS las wallets/mercados
    resueltos #15m, sin filtrar por si nuestras estrategias dispararon ahí."""
    out = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    with open(BALLENAS_HIST, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("marco") != MARCO_BALLENAS:
                continue
            if row.get("compro_yes") not in ("0", "1"):
                continue
            activo = row.get("activo")
            if activo not in ACTIVOS:
                continue
            try:
                p = float(row["precio"])
                acierto = int(row["acierto"])
            except (TypeError, ValueError):
                continue
            d = out[activo][bucket(p)]
            d[0] += acierto
            d[1] += 1
    return out


def cargar_shadow():
    """(strategy,subtype,decision) -> bucket -> [n, aciertos, pnl_total]."""
    out = defaultdict(lambda: defaultdict(lambda: [0, 0, 0.0]))
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            strat = row["strategy"]
            if strat not in FAMILIAS_SHADOW:
                continue
            if row["decision"] != "BUY_YES":
                continue
            sub = row["subtype"]
            if not sub.endswith(MARCO):
                continue
            activo = sub.split("#")[0]
            if activo not in ACTIVOS:
                continue
            try:
                p = float(row["precio_yes_mercado"])
                acierto = int(row["acierto"])
                pnl = float(row["pnl_neto"])
            except (TypeError, ValueError):
                continue
            d = out[(strat, sub, "BUY_YES")][bucket(p)]
            d[0] += 1
            d[1] += acierto
            d[2] += pnl
    return out


def cargar_real():
    """activo -> bucket -> [n, aciertos, pnl_total] -- dinero real, CLOSED,
    agregado por activo (cualquier estrategia BUY_YES #15min), porque el n
    real es demasiado bajo para desagregar más."""
    out = defaultdict(lambda: defaultdict(lambda: [0, 0, 0.0]))
    if not TRADES.exists():
        return out
    with open(TRADES, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED":
                continue
            if row.get("direction") != "BUY_YES":
                continue
            sub = row.get("subtype") or ""
            if not sub.endswith(MARCO):
                continue
            activo = sub.split("#")[0]
            if activo not in ACTIVOS:
                continue
            try:
                p = float(row["entry_price"])
                pnl = float(row["pnl_neto_eur"])
            except (TypeError, ValueError):
                continue
            acierto = 1 if pnl > 0 else 0
            d = out[activo][bucket(p)]
            d[0] += 1
            d[1] += acierto
            d[2] += pnl
    return out


def main():
    ballenas = cargar_ballenas()
    shadow = cargar_shadow()
    real = cargar_real()

    resultado = {}
    print(f"{'='*100}")
    print("FRANJA MILIMÉTRICA BALLENAS — cruce ballenas / shadow / real, step=%.3f" % STEP)
    print(f"{'='*100}\n")

    for activo in ACTIVOS:
        print(f"\n########## {activo}#{MARCO} ##########")
        buckets_vistos = set(ballenas.get(activo, {}).keys())
        for (strat, sub, dec), bd in shadow.items():
            if sub.split("#")[0] == activo:
                buckets_vistos |= set(bd.keys())
        buckets_vistos |= set(real.get(activo, {}).keys())

        filas_activo = []
        huecos = []
        for b in sorted(buckets_vistos):
            ab, nb = ballenas.get(activo, {}).get(b, [0, 0])
            hit_ballenas = ab / nb * 100 if nb else None

            # shadow: suma across familias en este bucket (misma franja de
            # precio, distintas estrategias) para tener una lectura agregada
            # además de por-familia
            n_sh = h_sh = 0
            pnl_sh = 0.0
            por_familia = {}
            for (strat, sub, dec), bd in shadow.items():
                if sub.split("#")[0] != activo:
                    continue
                if b not in bd:
                    continue
                n, h, pnl = bd[b]
                n_sh += n; h_sh += h; pnl_sh += pnl
                por_familia[strat] = {"n": n, "hit": round(h / n * 100, 1), "pnl_trade": round(pnl / n, 3)}

            nr, hr, pnlr = real.get(activo, {}).get(b, [0, 0, 0.0])

            fila = {
                "bucket": f"[{b:.2f},{b+STEP:.2f})",
                "ballenas_n": nb, "ballenas_hit": round(hit_ballenas, 1) if hit_ballenas is not None else None,
                "shadow_n": n_sh, "shadow_hit": round(h_sh / n_sh * 100, 1) if n_sh else None,
                "shadow_pnl_trade": round(pnl_sh / n_sh, 3) if n_sh else None,
                "shadow_por_familia": por_familia,
                "real_n": nr, "real_hit": round(hr / nr * 100, 1) if nr else None,
                "real_pnl_trade": round(pnlr / nr, 3) if nr else None,
            }
            filas_activo.append(fila)

            # hueco de cobertura: ballenas con dato sólido (n>=50) y hit alto
            # (>=70%), pero nosotros con poca o ninguna señal shadow ahí
            if nb >= 50 and hit_ballenas is not None and hit_ballenas >= 70 and n_sh < N_MIN_BUCKET_INFORMATIVO:
                huecos.append((b, hit_ballenas, nb, n_sh))

            marca_n = "🟢" if n_sh >= N_MIN_BUCKET_MADURO else ("🟡" if n_sh >= N_MIN_BUCKET_INFORMATIVO else "⚪")
            print(f"  [{b:.2f},{b+STEP:.2f})  ballenas: n={nb:5d} hit={hit_ballenas if hit_ballenas is not None else 0:5.1f}%"
                  f"   |  shadow{marca_n}: n={n_sh:4d} hit={(h_sh/n_sh*100) if n_sh else 0:5.1f}% pnl/trade={(pnl_sh/n_sh) if n_sh else 0:+.3f}"
                  f"   |  real: n={nr:3d} hit={(hr/nr*100) if nr else 0:5.1f}% pnl/trade={(pnlr/nr) if nr else 0:+.3f}")

        resultado[activo] = filas_activo

        if huecos:
            print(f"\n  🚨 HUECOS DE COBERTURA {activo}#{MARCO} (ballenas n>=50 hit>=70% pero shadow_n<{N_MIN_BUCKET_INFORMATIVO}):")
            for b, hit, nb, n_sh in huecos:
                print(f"     [{b:.2f},{b+STEP:.2f}) ballenas hit={hit:.1f}% (n={nb}) — shadow_n={n_sh} (casi sin cobertura propia aquí)")
        else:
            print(f"\n  (sin huecos de cobertura significativos en {activo}#{MARCO} con los umbrales actuales)")

    OUT.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
