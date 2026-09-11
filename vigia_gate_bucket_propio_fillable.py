#!/usr/bin/env python3
"""vigia_gate_bucket_propio_fillable.py — Vigía diario del veto por
fill-ability real (gate_bucket_propio.py::_veto_fillable(), conectado
28-Ago).

Origen: en una sola sesión (28-Ago) se cazaron a mano 3 buckets marcados
"bueno_confirmado" (por el gate propio o por gate_bucket_fino) cuyo
subconjunto REALMENTE fillable (profundidad-al-origen) tenía pnl negativo
o una tasa de fill por debajo del 30% -- selección adversa disfrazada de
señal. El script analisis_gate_bucket_propio_fillable_03ago.py ya existía
(construido 03-Ago) pero nunca se conectó a nada ni tuvo cron -- este
vigía es lo que le faltaba: lo re-ejecuta a diario, y avisa por Telegram
SOLO cuando el veto empieza/deja de aplicar a un bucket, mismo patrón que
vigia_gate_bucket_propio.py/vigia_gate_bucket_fino.py.

No enumera exhaustivamente cada (tupla, precio) posible -- evalúa el
veto en el precio REPRESENTATIVO (punto medio) de cada bucket/zona que
HOY podría devolver "bueno_confirmado": los buckets del gate principal
con ese veredicto, las ventanas de gate_bucket_fino, y las zonas de
zonas_validadas_externas. Es un muestreo, no una garantía exhaustiva --
mismo espíritu que el resto de vigías del proyecto (avisa de lo que
encuentra, no promete cobertura perfecta de todo el rango continuo).

Cron diario 06:59 UTC (después de vigia_gate_bucket_propio 06:55 y
vigia_gate_bucket_fino 06:58, para que ambos JSON ya estén frescos).
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import gate_bucket_propio as gbp  # noqa: E402

LATCH = REPO / "data/live/vigia_gate_bucket_propio_fillable_latch.json"


def _puntos_a_revisar() -> set[tuple[str, float]]:
    puntos = set()

    principal = gbp._cargar()
    for tupla, tabla in principal.items():
        for b, info in tabla.items():
            if isinstance(info, dict) and info.get("veredicto") == "bueno_confirmado":
                puntos.add((tupla, round(float(b) + gbp.STEP / 2, 4)))

    fino = gbp._zonas_finas()
    for tupla, info in fino.items():
        if info.get("veredicto") == "bueno_confirmado" and info.get("lo") is not None:
            lo, hi = info["lo"], info["hi"]
            puntos.add((tupla, round((lo + hi) / 2, 4)))

    externas = gbp._zonas_validadas_externamente()
    for tupla, zonas in externas.items():
        for lo, hi in zonas:
            puntos.add((tupla, round((lo + hi) / 2, 4)))

    return puntos


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run([sys.executable, str(REPO / "analisis_gate_bucket_propio_fillable_03ago.py")],
                        capture_output=True, text=True, timeout=180, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_gate_bucket_propio_fillable_03ago.py: {r.stderr[-2000:]}")
        return 1

    # Refrescar caches de gate_bucket_propio tras la regeneración (el
    # propio mtime-cache ya lo haría en la siguiente llamada, forzado aquí
    # por claridad).
    gbp._cache_fillable["mtime"] = None

    puntos = _puntos_a_revisar()
    estado_hoy = {}
    avisos = []
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    for tupla, py in sorted(puntos):
        resultado = gbp.evaluar(tupla, py)
        vetado = resultado.get("detalle", {}).get("origen") == "veto_fillable_28ago" if resultado.get("detalle") else False
        clave = f"{tupla}@{py:.4f}"
        estado_hoy[clave] = vetado
        vetado_antes = previo.get(clave, False)
        if vetado and not vetado_antes:
            motivo = resultado["detalle"]["motivo"]
            avisos.append(f"🚫 {tupla} (py≈{py:.3f}) -- VETADO por fill-ability real: {motivo}")
        elif vetado_antes and not vetado:
            avisos.append(f"✅ {tupla} (py≈{py:.3f}) -- ya no vetado por fill-ability (más n propio, o zona ya no confirmada)")

    print(f"Puntos revisados: {len(puntos)} | vetados hoy: {sum(estado_hoy.values())}")

    if avisos:
        msg = "🛡️ Veto por fill-ability real — cambios hoy:\n" + "\n".join(avisos)
        print(msg)
        if len(msg) > 3900:
            msg = msg[:3850] + f"\n… ({len(avisos)} avisos totales, truncado por límite de Telegram)"
        enviar_telegram(msg)
    else:
        print("Sin cambios en el veto de fill-ability hoy.")

    LATCH.write_text(json.dumps(estado_hoy, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
