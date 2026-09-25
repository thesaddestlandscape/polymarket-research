#!/usr/bin/env python3
"""vigia_perps_pendientes.py -- resumen DIARIO de Perps por Telegram (cron 07:58 UTC; 25-Sep, Javi: "procede con
todo"). Estado de la recogida (wallets con backfill, velas de 1 min acumuladas, huecos) + salida compacta de
analisis_perps_markout_entradas_25sep.py y analisis_perps_consenso_categoria_25sep.py. Solo lectura."""
import glob, json, subprocess, sys
from pathlib import Path
REPO = Path(__file__).resolve().parent


def correr(script, n=14):
    r = subprocess.run([sys.executable, str(REPO / script)], capture_output=True, text=True, timeout=1500, cwd=str(REPO))
    L = [l for l in (r.stdout or r.stderr).splitlines() if l.strip()]
    return L[:2] + ["..."] + L[-(n - 3):] if len(L) > n else L


def main():
    st = json.loads((REPO / "data/shadow/perps_fills_full_state.json").read_text())
    hechos = sum(1 for v in st.values() if v.get("back_done")); hf = sum(1 for v in st.values() if v.get("alta_frecuencia"))
    velas = sum(max(sum(1 for _ in open(f)) - 1, 0) for f in glob.glob(str(REPO / "data/shadow/perps_precios_1m/*.csv")))
    p1 = json.loads((REPO / "data/shadow/perps_precios_1m_state.json").read_text()) if (REPO / "data/shadow/perps_precios_1m_state.json").exists() else {}
    huecos = sum(v.get("huecos", 0) for v in p1.values())
    msg = [f"🛢️ PERPS pendientes -- {len(st)} wallets en backfill ({hechos} completas, {hf} alta frec.; objetivo 200), "
           f"serie 1 min: {velas} velas en {len(p1)} instrumentos ({huecos} huecos)."]
    msg += ["-- markout de entradas --"] + correr("analisis_perps_markout_entradas_25sep.py", 12)
    msg += ["-- consenso expertas por categoría --"] + correr("analisis_perps_consenso_categoria_25sep.py", 12)
    txt = "\n".join(msg)[:3800]
    print(txt)
    try:
        sys.path.insert(0, str(REPO))
        from shadow_digest import enviar_telegram
        enviar_telegram(txt)
    except Exception as e:
        print(f"(Telegram falló: {e})")


if __name__ == "__main__":
    main()
