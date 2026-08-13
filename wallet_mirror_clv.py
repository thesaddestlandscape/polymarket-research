"""
wallet_mirror_clv.py -- CLV (Closing Line Value) para WALLET_MIRROR, mismo
patrón que lt._clv_tupla() pero leyendo data/live/trades.csv en vez de
data/shadow/results.csv.

13-Ago: corrige una premisa equivocada de la sesión anterior (ver memoria
project_walletmirror_clv_pendiente_disenar_13ago) -- se asumió que faltaba
instrumentación nueva (snapshot de precio post-entrada) para medir CLV en
Wallet Mirror. Falso: `shadow_resolve.py::_clv()` NO usa precio post-entrada,
solo `outcome_real - precio_entrada` (BUY_YES) / `precio_entrada -
outcome_real` (BUY_NO) -- exactamente los datos que `trades.csv` ya
registra por cada trade CLOSED de WALLET_MIRROR desde el 11-Ago. No hacía
falta construir nada, solo leerlo.

Solo lectura, no toca ninguna decisión todavía -- n=6 trades reales CLOSED
a 13-Ago, muy por debajo de cualquier umbral de rigor (n>=15 mínimo,
CLAUDE.md). Diseñado para acumular solo: `clv_tupla_wallet_mirror()` se
puede llamar desde wallet_mirror_executor_dryrun.py el día que n sea
suficiente, mismo criterio fail-open-por-n-insuficiente que
lt._clv_tupla() (un veto que nunca ha visto datos no debe bloquear nada).
"""
from pathlib import Path
import csv

TRADES_CSV = Path("data/live/trades.csv")


def _clv_fila(entry_price: float, direction: str, outcome_real: str) -> float | None:
    try:
        p = float(entry_price)
    except (TypeError, ValueError):
        return None
    outcome_yes = 1.0 if outcome_real == "YES" else 0.0
    if direction == "BUY_YES" or direction == "BUY_Up":
        return outcome_yes - p
    if direction == "BUY_NO" or direction == "BUY_Down":
        return p - outcome_yes
    return None


def clv_tupla_wallet_mirror(subtype: str, direction: str) -> tuple[float, int]:
    """CLV medio y n de WALLET_MIRROR#<subtype>#<direction> sobre TODOS los
    trades CLOSED en trades.csv (sin ventana temporal -- n=6 a 13-Ago no
    admite recortar más). direction acepta tanto BUY_Up/BUY_Down (vocabulario
    de pares_permitidos_live) como BUY_YES/BUY_NO (vocabulario real de
    trades.csv) -- se normaliza aquí, mismo bug ya documentado en
    project_walletmirror_clv_pendiente_disenar_13ago (punto "Bug encontrado
    de paso")."""
    direction_norm = {"BUY_Up": "BUY_YES", "BUY_Down": "BUY_NO"}.get(direction, direction)
    vals = []
    try:
        with open(TRADES_CSV, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("strategy") != "WALLET_MIRROR":
                    continue
                if row.get("status") != "CLOSED":
                    continue
                if row.get("subtype") != subtype:
                    continue
                if row.get("direction") != direction_norm:
                    continue
                clv = _clv_fila(row.get("entry_price"), direction_norm, row.get("outcome_real", ""))
                if clv is not None:
                    vals.append(clv)
    except FileNotFoundError:
        return 0.0, 0
    if not vals:
        return 0.0, 0
    return sum(vals) / len(vals), len(vals)


if __name__ == "__main__":
    import json
    from wallet_mirror_gate_bucket import DATA_PATH as GB_PATH
    tuplas = set()
    try:
        for k in json.loads(GB_PATH.read_text(encoding="utf-8")).keys():
            # clave GB: tipo#activo#marco#grande -- mapear a subtype activo#marco
            partes = k.split("#")
            if len(partes) >= 3:
                tuplas.add(f"{partes[1]}#{partes[2]}")
    except Exception:
        pass
    if not tuplas:
        tuplas = {"BTC#5min", "BTC#15min"}
    for subtype in sorted(tuplas):
        for direction in ("BUY_YES", "BUY_NO"):
            clv, n = clv_tupla_wallet_mirror(subtype, direction)
            if n:
                print(f"WALLET_MIRROR#{subtype}#{direction}: clv_medio={clv:+.4f} n={n}")
