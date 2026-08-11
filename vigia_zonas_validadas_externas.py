#!/usr/bin/env python3
"""vigia_zonas_validadas_externas.py — vigía diario de las zonas de precio
validadas externamente vía ballenas_timing_history.csv post-TWAP (10-Ago),
mismo patrón que vigia_gate_bucket_propio.py.

Re-corre analisis_zonas_validadas_externas_post_twap_10ago.py cada día
(ballenas_timing_history.csv crece solo) y avisa por Telegram solo cuando
una zona ENTRA o SALE del conjunto confirmado -- para que Javi vea si el
margen se sostiene o se erosiona con más n, sin repetir el mismo aviso
cada día.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/zonas_validadas_externas.json"
LATCH = REPO / "data/live/vigia_zonas_validadas_externas_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    # 11-Ago: el análisis ahora cubre ~300 tuplas agrupadas (antes 15
    # estáticas) -- una corrida completa tarda ~5.5min (verificado), el
    # timeout de 120s de antes lo mataría con TimeoutExpired sin capturar
    # (cron silenciosamente roto, sin avisar ni loguear nada útil).
    r = subprocess.run([sys.executable, str(REPO / "analisis_zonas_validadas_externas_post_twap_10ago.py")],
                        capture_output=True, text=True, timeout=600, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_zonas_validadas_externas_post_twap_10ago.py: {r.stderr[-2000:]}")
        return 1

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    # 11-Ago (/code-review, hallazgo real): antes se avisaba por TUPLA
    # individual -- con el refactor a grupos (activo,marco,dirección)
    # compartidos por hasta 15 tuplas, la misma zona generaba 1 línea por
    # cada tupla del grupo (87 líneas / 5025 chars en una prueba real,
    # por encima del límite de 4096 de Telegram -- requests.post fallaba
    # con 400, la excepción se tragaba en enviar_telegram(), y NINGÚN
    # aviso llegaba esa corrida, incluidos cambios reales en tuplas con
    # dinero real). Se avisa una vez por GRUPO (usando el campo nuevo
    # "tuplas_grupo"), no por tupla -- el cambio (activo,marco,dirección)
    # es el mismo para todas, listarlas todas 15 veces no añade info.
    vistos = set()
    avisos = []
    for tupla_str, info in nuevo.items():
        tuplas_grupo = tuple(sorted(set(info.get("tuplas_grupo", [tupla_str]))))
        if tuplas_grupo in vistos:
            continue
        vistos.add(tuplas_grupo)
        # clave de comparación contra el latch anterior: cualquier tupla
        # del grupo vale, todas comparten "zonas_bueno_confirmado" idéntico.
        zonas_nuevas = {tuple(z) for z in info.get("zonas_bueno_confirmado", [])}
        zonas_antes = {tuple(z) for z in previo.get(tupla_str, {}).get("zonas_bueno_confirmado", [])}
        entraron = zonas_nuevas - zonas_antes
        salieron = zonas_antes - zonas_nuevas
        etiqueta = tuplas_grupo[0] if len(tuplas_grupo) == 1 else f"{tuplas_grupo[0]} (+{len(tuplas_grupo)-1} más)"
        for lo, hi in sorted(entraron):
            det = info["detalle_por_bucket"].get(f"{lo:.2f}", {})
            avisos.append(f"🟢 {etiqueta} [{lo:.2f},{hi:.2f}) ENTRA confirmada "
                          f"(n={det.get('n')} margen={det.get('margen_pp'):+.1f}pp)")
        for lo, hi in sorted(salieron):
            avisos.append(f"🔴 {etiqueta} [{lo:.2f},{hi:.2f}) SALE de confirmada (revisar por qué)")

    if avisos:
        # fail-safe adicional: aunque agrupar ya reduce el volumen drásticamente
        # (44 grupos máximo, no 300 tuplas), trocear por si algún día vuelve a
        # crecer -- mejor 2 mensajes que 0 por un 400 de Telegram.
        LIMITE = 3500
        cabecera = "🐋 Zonas validadas externas (post-TWAP) — cambios hoy:\n"
        bloque = cabecera
        for linea in avisos:
            if len(bloque) + len(linea) + 1 > LIMITE:
                print(bloque)
                enviar_telegram(bloque)
                bloque = cabecera
            bloque += linea + "\n"
        print(bloque)
        enviar_telegram(bloque)
    else:
        print("Sin cambios hoy en las zonas confirmadas.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
