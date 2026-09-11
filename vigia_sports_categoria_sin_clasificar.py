#!/usr/bin/env python3
"""vigia_sports_categoria_sin_clasificar.py — 26-Ago, vigía canario de
cobertura de sports (petición explícita Javi: "cobertura TOTAL, no puede
haber algo sin cubrir"). Auditoría en vivo (996k filas / 3 días, 0-Ago)
confirmó que hoy `clasificar()` (sports_wallet_edge_tracker.py) etiqueta
el 100% de lo que pasa por activity_ws.py — el riesgo real no es un hueco
de hoy, es que Polymarket lance un deporte/liga nueva mañana cuyo título
no matchee ningún regex de CATEGORIAS y caiga en el fallback silencioso
(devuelve "" si ni la lista explícita ni el patrón "will X win on Y" de
fútbol matchean). Sin este vigía, ese hueco solo se detecta en la próxima
auditoría manual — con este, avisa el mismo día.

Escanea las filas con categoria='' de activity_ws_HOY.csv +
activity_ws_AYER.csv (por si el cron corre justo tras medianoche UTC),
agrupa por patrón de título (primeras 6 palabras, evita 1 aviso por cada
partido individual del mismo deporte no reconocido) y avisa por Telegram
solo patrones NUEVOS (latch, mismo patrón que el resto de vigías).

Puramente de vigilancia -- no toca ninguna decisión ni fichero de otro
script.

Cron (07:06 UTC, mismo bloque que el resto de vigías diarios sports):
  6 7 * * * flock -n /tmp/vigia_sports_categoria_sin_clasificar.lock \
    /root/polymarket-research/.venv/bin/python \
    /root/polymarket-research/vigia_sports_categoria_sin_clasificar.py \
    >> /root/polymarket-research/logs/vigia_sports_categoria_sin_clasificar.log 2>&1
"""
import csv
import json
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DIR_SPORTS = REPO / "data" / "sports"
LATCH = REPO / "data" / "live" / "vigia_sports_categoria_sin_clasificar_latch.json"


def _archivo(fecha: str) -> Path:
    return DIR_SPORTS / f"activity_ws_{fecha}.csv"


def _patron_titulo(title: str) -> str:
    return " ".join((title or "").split()[:6]).strip().lower()


def _escanear() -> tuple[Counter, dict]:
    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    ayer = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    patrones: Counter = Counter()
    ejemplo_titulo: dict = {}
    for fecha in (ayer, hoy):
        fp = _archivo(fecha)
        if not fp.exists():
            continue
        with open(fp, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                cat = (row.get("categoria") or "").strip()
                if cat:
                    continue
                titulo = row.get("title", "")
                patron = _patron_titulo(titulo)
                if not patron:
                    continue
                patrones[patron] += 1
                ejemplo_titulo.setdefault(patron, titulo)
    return patrones, ejemplo_titulo


def main() -> int:
    from shadow_digest import enviar_telegram

    patrones, ejemplos = _escanear()
    n_total = sum(patrones.values())
    print(f"filas sin clasificar (hoy+ayer): {n_total}, patrones distintos: {len(patrones)}")

    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    nuevos = {p: n for p, n in patrones.items() if p not in previo}
    if nuevos:
        lineas = [
            f"⚠️ {ejemplos[p]!r} (patrón: \"{p}\", n={n})"
            for p, n in sorted(nuevos.items(), key=lambda x: -x[1])[:15]
        ]
        msg = (
            "🕳️ Sports — categoría SIN CLASIFICAR nueva detectada "
            f"({len(nuevos)} patrón(es) nuevo(s), {n_total} filas totales sin clasificar):\n"
            + "\n".join(lineas)
            + "\n\nRevisar CATEGORIAS en sports_wallet_edge_tracker.py -- puede ser un "
            "deporte/liga nueva en Polymarket que ningún regex reconoce todavía."
        )
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin patrones nuevos sin clasificar -- cobertura íntegra confirmada hoy." if not patrones
              else "Todos los patrones sin clasificar ya estaban vistos (sin novedad).")

    actual = {p: patrones[p] for p in patrones}
    for p, n in previo.items():
        actual.setdefault(p, n)
    LATCH.write_text(json.dumps(actual, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
