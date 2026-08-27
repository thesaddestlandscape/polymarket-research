"""
sports_wallet_mirror_clv.py -- CLV (Closing Line Value) para Sports Wallet
Mirror, mismo patrón que wallet_mirror_clv.py (cripto) pero leyendo
data/sports/trades.csv (categoria/tipo directos, sin parsear notas -- el
formato de sports ya los guarda como columnas propias).

27-Ago noche (petición explícita Javi: "construye lo que falte de sports
para tenerlo ya hecho"): solo lectura, no toca ninguna decisión. n=0
trades reales hoy (pares_permitidos_live=[] todavía) -- diseñado para
acumular solo, mismo criterio fail-open-por-n-insuficiente que el resto
del proyecto (un veto que nunca ha visto datos no debe bloquear nada).

CLV aquí: `direction` en trades.csv es el índice de outcome comprado
(mirror_idx, "0"/"1", ver sports_wallet_mirror_sniper.py), NO BUY_YES/
BUY_NO como en cripto -- normalizado: CLV = (outcome_real_index==direction
? 1 : 0) - entry_price, en la convención "1 si acertó el lado comprado".
"""
from pathlib import Path
import csv

TRADES_CSV = Path("data/sports/trades.csv")


def _clv_fila(entry_price: str, direction: str, outcome_real: str) -> float | None:
    try:
        p = float(entry_price)
        dir_idx = int(direction)
        outcome_idx = int(outcome_real)
    except (TypeError, ValueError):
        return None
    acierto = 1.0 if outcome_idx == dir_idx else 0.0
    return acierto - p


def clv_tupla_sports(categoria: str, tipo: str) -> tuple[float, int]:
    """CLV medio y n de <categoria>#<tipo> sobre TODOS los trades CLOSED
    en data/sports/trades.csv (sin ventana temporal, mismo criterio que
    el hermano de cripto -- n bajo no admite recortar más)."""
    vals = []
    try:
        with open(TRADES_CSV, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("status") != "CLOSED":
                    continue
                if row.get("categoria") != categoria or row.get("tipo") != tipo:
                    continue
                clv = _clv_fila(row.get("entry_price", ""), row.get("direction", ""), row.get("outcome_real", ""))
                if clv is not None:
                    vals.append(clv)
    except FileNotFoundError:
        return 0.0, 0
    if not vals:
        return 0.0, 0
    return sum(vals) / len(vals), len(vals)


if __name__ == "__main__":
    import json
    from sports_wallet_mirror_gate_bucket import DATA_PATH as GB_PATH
    tuplas = set()
    try:
        for k in json.loads(GB_PATH.read_text(encoding="utf-8")).keys():
            partes = k.split("#")
            if len(partes) == 2:
                tuplas.add((partes[0], partes[1]))
    except Exception:
        pass
    if not tuplas:
        tuplas = {("CS", "SEGUIR"), ("CS", "FADE")}
    for categoria, tipo in sorted(tuplas):
        clv, n = clv_tupla_sports(categoria, tipo)
        if n:
            print(f"{categoria}#{tipo}: clv_medio={clv:+.4f} n={n}")
        else:
            print(f"{categoria}#{tipo}: sin trades reales cerrados todavía")
