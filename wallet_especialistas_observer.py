#!/usr/bin/env python3
"""
wallet_especialistas_observer.py -- observer diario (petición explícita
Javi, 23-Jul: "anota que esto tienes que hacerlo diariamente... cada día
irán apareciendo más... sería conveniente hacer un observer solo de
esto") de wallets ESPECIALISTAS: aquellas con >=80% de su actividad
concentrada en UNA sola moneda (de las 5 que operamos: BTC/ETH/SOL/XRP/
DOGE) en un marco temporal concreto, con edge validado (shuffle test +
BH-FDR, wallet_edge_tracker.py) -- no wallets "smart" genéricas, wallets
que saben algo de UNA moneda específica que un análisis agregado por
marco (mezclando las 5) diluiría.

Cubre TODOS los marcos temporales que operamos: 5m, 15m, 60m, 240m,
weekly (no solo 5min como el primer barrido de la sesión).

Persiste estado en wallet_especialistas_state.json (clave
wallet#activo#marco) para que "cada día aparezcan más" sea visible: cada
corrida marca cuáles son NUEVAS desde la última vez, sin perder el
histórico de cuándo se vio cada una por primera vez.

Cruza cada especialista contra NUESTROS propios datos (results.csv,
agregado por activo/marco) -- ¿tenemos ya cobertura ahí? ¿nuestro propio
IC agregado es comparable, mejor o peor que el edge de esa wallet? Un
hueco de cobertura (wallet con edge fuerte, nosotros con n bajo o nulo
en ese activo/marco) es la señal más valiosa: sitios donde una wallet
concreta sabe algo que no estamos ni midiendo.

Solo lectura/reporte. No decide ni conecta nada a ejecutores.
Cron sugerido: diario, después de wallet_edge_tracker.py (:25 horaria).
"""
import csv
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from shadow_postmortem import _ic_bayes  # noqa: E402 -- fuente única, no reimplementar

DIR = Path(__file__).resolve().parent
DIR_SHADOW = DIR / "data" / "shadow"
WALLET_EDGE_ACTIVO_MARCO = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
RESULTS = DIR_SHADOW / "results.csv"
STATE = DIR_SHADOW / "wallet_especialistas_state.json"

ACTIVOS = ("BTC", "ETH", "SOL", "XRP", "DOGE")
MARCOS_BALLENAS = ("5m", "15m", "60m", "240m", "weekly")
MARCO_BALLENAS_A_RESULTS = {"5m": "5min", "15m": "15min", "60m": "60min", "240m": "240min", "weekly": None}
CONCENTRACION_MIN = 0.80
N_TOTAL_MIN = 15


def detectar_especialistas():
    db = json.loads(WALLET_EDGE_ACTIVO_MARCO.read_text())
    por_wallet_marco = defaultdict(dict)
    for v in db.values():
        por_wallet_marco[(v["wallet"], v["marco"])][v["activo"]] = v

    especialistas = []
    for (wallet, marco), por_activo in por_wallet_marco.items():
        if marco not in MARCOS_BALLENAS:
            continue
        n_total = sum(f["n"] for f in por_activo.values())
        if n_total < N_TOTAL_MIN:
            continue
        activo_dom, fila_dom = max(por_activo.items(), key=lambda kv: kv[1]["n"])
        concentracion = fila_dom["n"] / n_total
        if concentracion >= CONCENTRACION_MIN and fila_dom["sig_bhfdr"]:
            especialistas.append({
                "wallet": wallet, "marco": marco, "activo": activo_dom,
                "concentracion": round(concentracion, 4), "n": fila_dom["n"],
                "n_total_5monedas": n_total, "edge_pp": fila_dom["edge_pp"],
                "hit": fila_dom["hit"], "precio_medio": fila_dom["precio_medio"],
                "pnl_proxy": fila_dom.get("pnl_proxy"),
            })
    return especialistas


def cargar_cobertura_propia():
    """(activo, marco_results) -> {n, ic_bayes, pnl} agregado de TODAS
    nuestras estrategias BUY_YES en results.csv -- mismo espíritu que
    cargar_shadow_filas() de analisis_franja_milimetrica_ballenas.py pero
    sin filtrar por volumen mínimo de estrategia (aquí solo se usa como
    referencia de "cuánto sabemos ya", no como candidata)."""
    acumulado = defaultdict(lambda: {"n": 0, "aciertos": 0, "pnl": 0.0})
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") not in ("0", "1"):
                continue
            sub = row.get("subtype") or ""
            strat = row.get("strategy") or ""
            if strat == "WEEKLY_PRICE" and sub in ACTIVOS:
                clave = (sub, "weekly")
            elif "#" in sub:
                activo, marco_r = sub.split("#", 1)
                if activo not in ACTIVOS:
                    continue
                clave = (activo, marco_r)
            else:
                continue
            d = acumulado[clave]
            d["n"] += 1
            d["aciertos"] += int(row["acierto"])
            try:
                d["pnl"] += float(row.get("pnl_neto") or 0)
            except ValueError:
                pass
    salida = {}
    for clave, d in acumulado.items():
        salida[clave] = {"n": d["n"], "ic_bayes": round(_ic_bayes(d["aciertos"], d["n"]), 4),
                          "pnl": round(d["pnl"], 2)}
    return salida


def main():
    ahora = datetime.now(timezone.utc)
    print(f"[wallet_especialistas_observer] {ahora.isoformat(timespec='seconds')}")

    especialistas = detectar_especialistas()
    print(f"especialistas detectados hoy (n_total>=15, concentracion>={CONCENTRACION_MIN}, sig_bhfdr): {len(especialistas)}")

    cobertura = cargar_cobertura_propia()

    estado_previo = {}
    if STATE.exists():
        try:
            estado_previo = json.loads(STATE.read_text()).get("wallets", {})
        except Exception:
            estado_previo = {}

    estado_nuevo = {}
    nuevos_hoy = []
    for e in especialistas:
        clave = f"{e['wallet']}#{e['activo']}#{e['marco']}"
        marco_r = MARCO_BALLENAS_A_RESULTS.get(e["marco"])
        clave_cobertura = (e["activo"], "weekly" if marco_r is None else marco_r)
        cob = cobertura.get(clave_cobertura, {"n": 0, "ic_bayes": None, "pnl": None})

        previo = estado_previo.get(clave)
        primera_vez = previo["primera_vez_visto"] if previo else ahora.isoformat(timespec="seconds")
        if previo is None:
            nuevos_hoy.append({**e, "cobertura_propia": cob})

        estado_nuevo[clave] = {
            "wallet": e["wallet"], "activo": e["activo"], "marco": e["marco"],
            "n": e["n"], "concentracion": e["concentracion"], "hit": e["hit"],
            "edge_pp": e["edge_pp"], "precio_medio": e["precio_medio"],
            "cobertura_propia_n": cob["n"], "cobertura_propia_ic_bayes": cob["ic_bayes"],
            "primera_vez_visto": primera_vez,
            "ultima_vez_visto": ahora.isoformat(timespec="seconds"),
        }

    print(f"\nNUEVAS desde la última corrida: {len(nuevos_hoy)}")
    for e in sorted(nuevos_hoy, key=lambda x: -x["n"])[:20]:
        cob = e["cobertura_propia"]
        hueco = " ⚠️ HUECO DE COBERTURA (n propio<15)" if cob["n"] < 15 else ""
        print(f"  {e['wallet'][:12]}... {e['activo']}#{e['marco']} n={e['n']} hit={e['hit']:.3f} "
              f"edge_pp={e['edge_pp']:+.2f} | nuestro n={cob['n']} ic_bayes={cob['ic_bayes']}{hueco}")

    huecos_totales = [v for v in estado_nuevo.values() if v["cobertura_propia_n"] < 15]
    print(f"\nHUECOS DE COBERTURA totales (especialista con edge validado, nuestro n<15 en ese activo/marco): {len(huecos_totales)}")
    for h in sorted(huecos_totales, key=lambda x: -x["n"])[:15]:
        print(f"  {h['wallet'][:12]}... {h['activo']}#{h['marco']} n={h['n']} edge_pp={h['edge_pp']:+.2f} -- nuestro n={h['cobertura_propia_n']}")

    desaparecidos = set(estado_previo) - set(estado_nuevo)
    if desaparecidos:
        print(f"\nya NO cumplen el criterio hoy (dejaron de ser especialistas o cayó su n): {len(desaparecidos)}")

    STATE.write_text(json.dumps({"actualizado": ahora.isoformat(timespec="seconds"),
                                   "wallets": estado_nuevo}, indent=2, ensure_ascii=False),
                      encoding="utf-8")
    print(f"\nescrito {STATE} ({len(estado_nuevo)} especialistas activos)")


if __name__ == "__main__":
    main()
