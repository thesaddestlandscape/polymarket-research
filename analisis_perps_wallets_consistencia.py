#!/usr/bin/env python3
"""
analisis_perps_wallets_consistencia.py -- 14-Sep, petición explícita Javi
tras preguntar si hay datos suficientes para plantear wallet-mirror/
wallet-consensus sobre Polymarket Perps (oro, plata, petróleo, y sobre
todo memecoins -- "hay muchos expertos en memecoins que se han hecho de
oro estos días").

Primer vistazo (14-Sep, 6 días de datos desde el 09-Sep): varias wallets
mostraban PnL agregado espectacular en metales/memecoins (ej.
0xfc1B24B1 +82.993€ en metales, 0xFAd25C30 +9.698€ en memecoins con solo
90 fills). Al desagregar por DÍA (mismo rigor que el resto del proyecto
-- split-half, nunca fiarse de un agregado sin desagregar por tiempo)
resultó ser casi siempre UN SOLO día gigante, con pérdidas el resto --
ni siquiera el trader #1 histórico del leaderboard (+823k€ de por vida)
se libra: está perdiendo dinero en la ventana de 6 días que llevamos
observando. Conclusión: 6 días es demasiado poco para separar suerte de
skill sostenido. Este script construye el mecanismo para que la
respuesta se vuelva automática con más días, sin recalcularlo a mano
cada vez -- mismo patrón que `bot_wallets_gate_bucket_historico.py`
(evolución diaria) aplicado aquí.

Categorías de instrumento (las que pidió Javi + resto para contexto):
  - metales_petroleo: GOLD/SILVER/BRENTOIL/WTIOIL
  - memecoins: FARTCOIN/CASHCAT/KPEPE/KSHIB/PUMP/USELESS (lista viva,
    ampliar si el universo de `polymarket_perps_market_*.csv` añade más)
  - otros: todo lo demás (BTC/ETH/acciones/índices/resto de altcoins)

Por wallet × categoría × día: pnl agregado (suma de la columna `pnl` de
cada fill con pnl!=0, es decir cierres/reducciones de posición) y n de
cierres. Apila en `data/shadow/perps_wallets_consistencia_historico.csv`
-- NUNCA reprocesa un día ya registrado (idempotente por fecha, mismo
criterio que el resto de históricos diarios del proyecto).

Solo lectura de los CSV de fetch_polymarket_perps_wallet_fills.py -- no
toca dinero real (Perps no tiene ninguna infraestructura de ejecución
todavía, esto es investigación pura). Pensado para cron diario, después
de que el fetcher cierre el CSV del día anterior (~23:45 UTC → correr
00:20 UTC).
"""
import csv
import glob
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
FILLS_GLOB = str(REPO / "data/shadow/polymarket_perps_wallet_fills_*.csv")
OUT = REPO / "data/shadow/perps_wallets_consistencia_historico.csv"
OUT_COLS = ["fecha", "address", "categoria", "pnl_dia", "n_cierres"]

METALES_PETROLEO = {"GOLD-USD", "SILVER-USD", "BRENTOIL-USD", "WTIOIL-USD"}
MEMECOINS = {"FARTCOIN-USD", "CASHCAT-USD", "KPEPE-USD", "KSHIB-USD", "PUMP-USD", "USELESS-USD"}


def categoria_de(symbol: str) -> str:
    if symbol in METALES_PETROLEO:
        return "metales_petroleo"
    if symbol in MEMECOINS:
        return "memecoins"
    return "otros"


def _fecha_de_fichero(fn: str) -> str | None:
    m = re.search(r"(\d{4}-\d{2}-\d{2})\.csv$", fn)
    return m.group(1) if m else None


def _fechas_ya_registradas() -> set[str]:
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {row["fecha"] for row in csv.DictReader(f)}


def procesar_fichero(fn: str) -> list[dict]:
    """[{fecha, address, categoria, pnl_dia, n_cierres}, ...] para un
    fichero (un día) de wallet_fills."""
    fecha = _fecha_de_fichero(fn)
    if fecha is None:
        return []
    agregados: dict[tuple, list] = defaultdict(lambda: [0.0, 0])
    with open(fn, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                pnl = float(row.get("pnl") or 0)
            except (TypeError, ValueError):
                continue
            if pnl == 0:
                continue  # fill sin cierre de posición, no aporta a PnL realizado
            cat = categoria_de(row.get("symbol", ""))
            clave = (row.get("address", ""), cat)
            agregados[clave][0] += pnl
            agregados[clave][1] += 1
    return [{"fecha": fecha, "address": addr, "categoria": cat,
              "pnl_dia": round(vals[0], 4), "n_cierres": vals[1]}
             for (addr, cat), vals in agregados.items()]


def main() -> int:
    ya_registradas = _fechas_ya_registradas()
    hoy = datetime.now(timezone.utc).date().isoformat()
    filas_nuevas = []
    for fn in sorted(glob.glob(FILLS_GLOB)):
        fecha = _fecha_de_fichero(fn)
        if fecha is None or fecha in ya_registradas or fecha == hoy:
            # El día de HOY todavía está a medio escribir (el fetcher sigue
            # corriendo) -- solo se registra un día una vez cerrado, igual
            # que el resto de históricos diarios del proyecto no procesan
            # el CSV del día en curso.
            continue
        filas_nuevas.extend(procesar_fichero(fn))

    if not filas_nuevas:
        print("[perps_wallets_consistencia] 0 días nuevos que registrar")
        return 0

    nuevo = not OUT.exists()
    with open(OUT, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS)
        if nuevo:
            w.writeheader()
        w.writerows(filas_nuevas)

    dias_nuevos = sorted({r["fecha"] for r in filas_nuevas})
    print(f"[perps_wallets_consistencia] {len(filas_nuevas)} fila(s) nuevas "
          f"({len(dias_nuevos)} día(s): {', '.join(dias_nuevos)}) -> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
