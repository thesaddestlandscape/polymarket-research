#!/usr/bin/env python3
"""Vigía FAVORITO_CONFIRMADO 60min: avisa por Telegram (una vez por tupla)
cuando cualquiera de las 6 tuplas #{BTC,ETH,SOL}#60min#{BUY_YES,BUY_NO}
cruza n>=40 en su dirección (mismo listón que las 15min graduadas 11-Jul).

Origen (11-Jul, "carril 60min"): tras refutar 6 ángulos de arreglo de la
fill-ability en 15min, la tesis estructural aprobada por Javi es RODEAR el
problema migrando el edge a mercados 60min (libros profundos: primer
snapshot ETH#60min ratio 409x vs medianas 0€ en 15min). FAVORITO_CONFIRMADO
#60min: agregado n=63 ic=0.254 en el momento de instrumentar.

El aviso incluye IC de la tupla + fill-ability acumulada de sus snapshots
candidato_evaluacion (libro_snapshots.csv), para que la decisión de
whitelist llegue con el cuadro completo. La decisión SIEMPRE es de Javi:
además del n>=40 se exige pasar analisis_gate_riguroso.py (Wilson+shuffle)
antes de proponer — este vigía solo informa. Read-only, no toca dinero.
"""
import csv
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

PARAMS = REPO / "data/shadow/strategy_params.json"
SNAPSHOTS = REPO / "data/live/libro_snapshots.csv"
LATCH = REPO / "data/live/vigia_favorito_60min_latch.json"
GATE_N = 40
PARES = ("BTC", "ETH", "SOL")
DIRECCIONES = ("BUY_YES", "BUY_NO")


def _fill_ability(subtype: str, direction: str) -> tuple[int, float]:
    """(n_snapshots, pct que pasaría el veto 5x) de los snapshots
    candidato_evaluacion de esa tupla."""
    if not SNAPSHOTS.exists():
        return 0, 0.0
    n = pasa = 0
    with open(SNAPSHOTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("motivo") != "candidato_evaluacion":
                continue
            if row.get("strategy") != "FAVORITO_CONFIRMADO":
                continue
            if row.get("subtype") != subtype or row.get("direction") != direction:
                continue
            n += 1
            try:
                if float(row.get("ratio_vs_stake") or 0) >= 5:
                    pasa += 1
            except ValueError:
                pass
    return n, (pasa / n if n else 0.0)


def main() -> int:
    from shadow_digest import enviar_telegram

    if not PARAMS.exists():
        print("[vigia_favorito_60min] sin strategy_params.json")
        return 0
    params = json.loads(PARAMS.read_text(encoding="utf-8")).get("estrategias", {})

    latch = {}
    if LATCH.exists():
        try:
            latch = json.loads(LATCH.read_text())
        except Exception:
            latch = {}

    cambiado = False
    for par in PARES:
        clave = f"FAVORITO_CONFIRMADO#{par}#60min"
        entry = params.get(clave, {})
        for dec in DIRECCIONES:
            tupla = f"{clave}#{dec}"
            n = entry.get(f"n_{dec}", 0) or 0
            ic = entry.get(f"ic_{dec}")
            print(f"[vigia_favorito_60min] {tupla} n={n}/{GATE_N} ic={ic}")
            if n < GATE_N or latch.get(tupla, {}).get("avisado"):
                continue

            n_snap, pct_fill = _fill_ability(f"{par}#60min", dec)
            msg = (
                f"🔔 VIGÍA carril 60min: {tupla} cruzó n≥{GATE_N}\n"
                f"n={n} ic={ic}\n"
                f"Fill-ability (snapshots candidato): n={n_snap}, "
                f"{pct_fill:.0%} pasaría el veto 5x\n"
                f"Siguiente paso ANTES de proponer whitelist: correr "
                f"analisis_gate_riguroso.py (Wilson+shuffle) sobre esta tupla "
                f"y revisar fill-ability vs el 5-56% del 15min. Decisión de "
                f"Javi — solo informativo, no toca dinero."
            )
            ok = enviar_telegram(msg)
            latch[tupla] = {"avisado": True, "n": n, "ic": ic,
                            "fill_n": n_snap, "fill_pct": round(pct_fill, 3),
                            "telegram_ok": ok}
            cambiado = True
            print(f"[vigia_favorito_60min] aviso enviado {tupla} (telegram={ok})")

    if cambiado:
        LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_favorito_60min] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
