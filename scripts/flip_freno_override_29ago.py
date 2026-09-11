import json
from pathlib import Path

REPO = Path("/root/polymarket-research")
CFG = REPO / "data" / "live" / "config_live.json"

data = json.loads(CFG.read_text(encoding="utf-8"))
cb = data["riesgo"]["circuit_breaker"]
cb["freno_diario_pct_override"] = {
    "fecha": "2026-08-29",
    "pct": 0.35,
    "_nota": (
        "2026-08-28 (at job programado a las 22:00 UTC / medianoche Madrid, "
        "petición explícita Javi el mismo día: extender el override día a día "
        "mientras el bankroll siga bajo -- mismo patrón ya usado para el "
        "freno_ventana_pct_override 16->17-Jul). Bankroll bkr_ini_dia=3.493€ "
        "(28-Ago), con freno_diario_pct default 0.30 el margen proyectado da "
        "1.0479€, por debajo del suelo del CLOB (1.05€) por 0.0021€ -- mismo "
        "deadlock que bloqueó 34 intentos reales el 28-Ago. Con 0.35 el margen "
        "sube a ~1.22€, colchón ~0.17€ sobre el suelo. Autoexpira solo (código "
        "ya ignora overrides de fecha pasada) -- el 30-Ago vuelve a 0.30 salvo "
        "que se renueve otra vez con bankroll fresco (revisar cada sesión, no "
        "asumir que ya no hace falta)."
    ),
    "_valor_anterior": "0.35 del 2026-08-28 (ya expirado)",
}
CFG.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

import subprocess
subprocess.run(["git", "-C", str(REPO), "add", "data/live/config_live.json"], check=True)
subprocess.run(["git", "-C", str(REPO), "commit", "-m",
    "chore: extiende freno_diario_pct_override a 2026-08-29 (0.35)\n\n"
    "Aprobado por Javi 2026-08-28 (\"extender día a día mientras el bankroll "
    "siga bajo\"). Aplicado vía at job a medianoche Madrid para no tocar el "
    "override de HOY mientras siguiera vigente. bkr_ini_dia=3.493€, con "
    "freno_diario_pct default 0.30 el margen (1.0479€) queda por debajo del "
    "suelo del CLOB (1.05€) -- mismo deadlock del 28-Ago. Revisar en próxima "
    "sesión si sigue haciendo falta renovarlo para 30-Ago.\n\n"
    "Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>\n"
    "Claude-Session: https://claude.ai/code/session_01Y549WPb9XGkLiP2hZ5qDx8"],
    check=True)
print("OK: override extendido a 2026-08-29 y commiteado.")
