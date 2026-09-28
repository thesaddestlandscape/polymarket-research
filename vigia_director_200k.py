#!/usr/bin/env python3
"""vigia_director_200k.py -- cron diario ÚNICO con Parte A + Parte B (28-Sep,
petición explícita Javi: "mandame un mensaje de telegram diario con los
resultados de la parte A y la parte B"). Un solo mensaje, SIEMPRE (no solo
hallazgos nuevos) -- mismo criterio que vigia_dispersed_bot_progreso_diario.
py: es un informe de estado, no una alerta puntual, así que un día sin
cambios sigue siendo información útil.

  Parte A ("buscar ineficiencias del mercado/ballenas/wallets"):
    lee data/shadow/buscador_edge_perdido.json TAL CUAL está (regenerado
    cada 6h por vigias_frecuentes_fase0.py, carril "buscador" --
    NO se relanza aquí para no duplicar el coste real de esa corrida).
  Parte B ("dirigir y masterizar nuestras propias estrategias"):
    corre director_200k.py fresco (barato, solo lee JSONs ya generados
    por otros mecanismos) y usa su salida.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
DIRECTOR_JSON = REPO / "data" / "shadow" / "director_200k.json"
BUSCADOR_JSON = REPO / "data" / "shadow" / "buscador_edge_perdido.json"
TOP_TELEGRAM = 5


def _texto_parte_a(b: dict | None) -> list[str]:
    lin = ["🔎 PARTE A -- ineficiencias de mercado/ballenas/wallets (buscador_edge_perdido)"]
    if not b:
        lin.append("  (sin datos todavía -- vigias_frecuentes_fase0.py carril 'buscador' aún no ha corrido)")
        return lin
    n_deg = b.get("n_tuplas_degradadas", 0)
    lin.append(f"  {n_deg} tupla(s) live degradada(s) bajo la lupa (generado {b.get('generado_utc', '?')})")
    if n_deg == 0:
        lin.append("  (nada degradado hoy -- el buscador no tiene nada que investigar, es buena señal)")
        return lin
    for tupla, info in b.get("tuplas", {}).items():
        dims = info.get("dimensiones", {})
        if not dims:
            lin.append(f"  · {tupla}: sin dimensiones evaluadas ({info.get('n_filas', 0)} filas)")
            continue
        resumen_dims = []
        for nombre, cands in dims.items():
            ok = [c for c in cands if c.get("forward_ok")]
            if ok:
                resumen_dims.append(f"{nombre}={len(ok)} forward_ok")
        if resumen_dims:
            lin.append(f"  · {tupla}: {', '.join(resumen_dims)}")
        else:
            lin.append(f"  · {tupla}: sin candidato forward-validado todavía (dimensiones evaluadas: "
                       f"{', '.join(dims.keys())})")
    return lin


def _texto_parte_b(d: dict) -> list[str]:
    lin = ["\n🧭 PARTE B -- dirigir y masterizar nuestras propias estrategias (director_200k)"]
    lin.append(f"  {d.get('n_tuplas_live_hoy', '?')} tuplas live hoy")

    pf = d.get("pnl_fiel_sin_conectar_top", [])
    lin.append(f"\n  💰 Edge propio sin conectar ({len(pf)} candidatas, n≥15, top {TOP_TELEGRAM}):")
    if not pf:
        lin.append("    (ninguna)")
    for x in pf[:TOP_TELEGRAM]:
        flag = " ⚠️sospechosa" if x.get("sospechosa_integridad") else ""
        lin.append(f"    {x['tupla']}: +{x['pnl_fiel_eur_sin_suelo']}€ (n={x['n_ejecutado']}, "
                   f"fill={x['fill_rate']}){flag}")

    pi = d.get("payout_inverso_sin_decidir", [])
    lin.append(f"\n  ⚠️ Payout inverso live sin decidir: {len(pi)}")
    for x in pi[:TOP_TELEGRAM]:
        lin.append(f"    {x['tupla']}: g={x['growth_g_f10pct']} n={x['n']}")

    return lin


def main() -> int:
    r = subprocess.run([sys.executable, str(REPO / "director_200k.py")],
                       capture_output=True, text=True, timeout=600, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando director_200k.py (rc={r.returncode}): "
              f"{r.stdout[-300:]} {r.stderr[-1200:]}")
        return 1
    print(r.stdout[-2000:])
    try:
        datos_b = json.loads(DIRECTOR_JSON.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"ERROR leyendo {DIRECTOR_JSON}: {type(e).__name__}: {e}")
        return 1
    try:
        datos_a = json.loads(BUSCADOR_JSON.read_text(encoding="utf-8")) if BUSCADOR_JSON.exists() else None
    except Exception as e:
        print(f"aviso: no se pudo leer {BUSCADOR_JSON}: {type(e).__name__}: {e}")
        datos_a = None

    lineas = _texto_parte_a(datos_a) + _texto_parte_b(datos_b)
    lineas.append("\nNinguna fila es promoción automática -- checklist 6 categorías + /code-review + OK Javi siempre.")
    texto = "\n".join(lineas)
    print(texto)
    try:
        from shadow_digest import enviar_telegram
        ok = enviar_telegram(texto, bot="cripto")
        print(f"telegram: {'ok' if ok else 'fallo'}")
    except Exception as e:
        print(f"aviso: no se pudo enviar Telegram: {type(e).__name__}: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
