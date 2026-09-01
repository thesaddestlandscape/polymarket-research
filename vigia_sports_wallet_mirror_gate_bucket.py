#!/usr/bin/env python3
"""vigia_sports_wallet_mirror_gate_bucket.py — 26-Ago, vigía diario del
gate por micro-bucket de sports (analisis_sports_wallet_mirror_gate_
bucket_26ago.py), mismo patrón que el resto de vigías de la sesión.
Avisa por Telegram solo veredictos NUEVOS (bueno_confirmado/
malo_confirmado). Primera vez que sports tiene este mecanismo -- hoy
0 confirmados, LoL diluido al desagregar (CLAUDE.md pt.17).
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/sports/wallet_mirror_gate_bucket.json"
LATCH = REPO / "data/live/vigia_sports_wallet_mirror_gate_bucket_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run(
        [sys.executable, str(REPO / "analisis_sports_wallet_mirror_gate_bucket_26ago.py")],
        capture_output=True, text=True, timeout=180, cwd=str(REPO),
    )
    if r.returncode != 0:
        print(f"ERROR: {r.stderr[-2000:]}")
        return 1
    print(r.stdout[-2000:])

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    for tupla_str, buckets in nuevo.items():
        for b, info in buckets.items():
            v_nuevo = info.get("veredicto", "sin_concluir")
            v_antes = previo.get(tupla_str, {}).get(b, {}).get("veredicto", "sin_concluir")
            if v_nuevo in ("bueno_confirmado", "malo_confirmado") and v_nuevo != v_antes:
                avisos.append(
                    f"{'🟢' if v_nuevo == 'bueno_confirmado' else '🔴'} {tupla_str} "
                    f"[{b},{float(b)+0.05:.2f}) -> {v_nuevo} "
                    f"(n={info.get('n')} pnl/tr={info.get('pnl_medio')} p_bh={info.get('p_bh')})"
                )
            # 01-Sep (/code-review, hallazgo real -- misma noche del fix
            # N_MIN 15->40): solo se avisaba al ENTRAR en bueno/malo_
            # confirmado, nunca al SALIR (ej. bueno_confirmado -> n_
            # insuficiente al subir el umbral, o sin_concluir). Un bucket
            # live real (CS#SEGUIR[0.25,0.30)) perdió su confirmación
            # exactamente así, sin aviso -- mismo punto ciego que CLAUDE.md
            # ya documenta para vigia_log_growth.
            elif v_antes in ("bueno_confirmado", "malo_confirmado") and v_nuevo != v_antes:
                avisos.append(
                    f"⚠️ {tupla_str} [{b},{float(b)+0.05:.2f}) pierde confirmación "
                    f"({v_antes} -> {v_nuevo}, n={info.get('n')})"
                )

    # /code-review 01-Sep (hallazgo real, segunda ronda): el bucle de
    # arriba solo recorre las claves presentes HOY en `nuevo` -- un bucket
    # que ayer tenía filas (confirmado) y hoy tiene CERO (0 filas nuevas en
    # ese categoria#tipo#bucket exacto) ni siquiera aparece en `nuevo`
    # (analisis_sports_wallet_mirror_gate_bucket_26ago.py solo crea claves
    # para combos con al menos 1 fila), así que la pérdida de confirmación
    # pasaba igual de silenciosa que el caso que el fix de arriba
    # pretendía cerrar. Recorrer también lo que había en `previo` y ya no
    # está en `nuevo`.
    for tupla_str, buckets in previo.items():
        for b, info in buckets.items():
            v_antes = info.get("veredicto", "sin_concluir")
            if v_antes not in ("bueno_confirmado", "malo_confirmado"):
                continue
            if b not in nuevo.get(tupla_str, {}):
                avisos.append(
                    f"⚠️ {tupla_str} [{b},{float(b)+0.05:.2f}) pierde confirmación "
                    f"({v_antes} -> sin datos hoy)"
                )

    if avisos:
        # /code-review 01-Sep (hallazgo real): la cabecera siempre decía
        # "🏆 nuevos veredictos" incluso cuando avisos solo contenía
        # pérdidas de confirmación (⚠️) -- un operador mirando por encima
        # podía leer el trofeo y no darse cuenta de que un bucket con
        # dinero real acababa de dejar de operar.
        solo_perdidas = all(a.startswith("⚠️") for a in avisos)
        cabecera = "⚠️ Sports Wallet Mirror gate bucket — pérdidas de confirmación:" \
            if solo_perdidas else "🏆 Sports Wallet Mirror gate bucket — cambios hoy:"
        msg = cabecera + "\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin veredictos nuevos hoy.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
