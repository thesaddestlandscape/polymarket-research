#!/usr/bin/env python3
"""vigia_buscador_edge_perdido.py -- envoltorio de buscador_edge_perdido.py
para el planificador vigias_frecuentes_fase0.py (carril propio, subproceso).

Corre el buscador (trabajo numpy, subproceso nice 10 para no competir por el
GIL) y avisa por Telegram (bot "cripto") SOLO hallazgos NUEVOS -- mismo
patrón de latch por firma estable que vigia_edge_quirurgico.py (nunca
incluir en la firma un valor recalculado cada ciclo, ver CLAUDE.md pt.5).

Avisa también, una vez por tupla (latch aparte), cuando una tupla degradada
cae en la familia P-GALLINA sin loader todavía (FASE 1B) -- para que no
pase desapercibido que el buscador no la está mirando de verdad."""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
OUT = REPO / "data" / "shadow" / "buscador_edge_perdido.json"
LATCH = REPO / "data" / "shadow" / "vigia_buscador_edge_perdido_latch.json"


def _firma(tupla: str, dimension: str, bucket) -> str:
    return f"{tupla}|{dimension}|{bucket}"


def _texto_hallazgos(nuevos: list) -> str:
    lin = ["🔎 Buscador de edge perdido -- hallazgos nuevos (forward 7d confirmado):"]
    for tupla, dimension, c in nuevos:
        lin.append(f"🟢 {tupla} | {dimension}={c['bucket']}: train n={c['n_train']} "
                   f"{c['pnl_train']:+.2f}€ -> fwd n={c['n_test']} {c['pnl_test']:+.2f}€")
    return "\n".join(lin)


def _texto_sin_loader(tuplas: list) -> str:
    lin = ["🔎 Buscador de edge perdido -- degradadas sin cubrir todavía (familia "
           "P-GALLINA, loader FASE 1B pendiente, ver buscador_edge_perdido.py):"]
    for t in tuplas:
        lin.append(f"⚪ {t}")
    return "\n".join(lin)


def avisar(datos: dict, enviar, latch_path: Path = LATCH) -> list:
    try:
        latch = json.loads(latch_path.read_text(encoding="utf-8")) if latch_path.exists() else {}
    except Exception:
        latch = {}
    vistos = set(latch.get("vistos", []))
    vistos_sin_loader = set(latch.get("vistos_sin_loader", []))
    primera = not latch

    nuevos = []
    for tupla, info in datos.get("tuplas", {}).items():
        for dimension, cands in info.get("dimensiones", {}).items():
            for c in cands:
                if not c.get("forward_ok"):
                    continue
                f = _firma(tupla, dimension, c["bucket"])
                if f not in vistos:
                    nuevos.append((tupla, dimension, c))
                vistos.add(f)

    sin_loader_nuevas = [t for t, info in datos.get("tuplas", {}).items()
                         if info.get("sin_loader") and t not in vistos_sin_loader]
    vistos_sin_loader |= set(sin_loader_nuevas)

    enviados = []
    if not primera:
        if nuevos:
            txt = _texto_hallazgos(nuevos)
            if enviar(txt):
                enviados.append(txt)
        if sin_loader_nuevas:
            txt2 = _texto_sin_loader(sin_loader_nuevas)
            if enviar(txt2):
                enviados.append(txt2)

    latch_path.write_text(json.dumps({"vistos": sorted(vistos),
                                      "vistos_sin_loader": sorted(vistos_sin_loader)},
                                     ensure_ascii=False), encoding="utf-8")
    return enviados


def main() -> int:
    r = subprocess.run(["nice", "-n", "10", sys.executable, str(REPO / "buscador_edge_perdido.py")],
                       capture_output=True, text=True, timeout=1800, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando buscador_edge_perdido.py (rc={r.returncode}): "
              f"{r.stdout[-300:]} {r.stderr[-1200:]}")
        return 1
    print(r.stdout[-1500:])
    try:
        from shadow_digest import enviar_telegram
        datos = json.loads(OUT.read_text(encoding="utf-8"))
        enviados = avisar(datos, lambda t: enviar_telegram(t, bot="cripto"))
        print(f"telegram: {len(enviados)} mensaje(s) enviado(s)")
    except Exception as e:
        print(f"aviso: no se pudo procesar/enviar Telegram: {type(e).__name__}: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
