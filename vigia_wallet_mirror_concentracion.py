#!/usr/bin/env python3
"""vigia_wallet_mirror_concentracion.py — 26-Ago, mismo patrón que
vigia_wallet_especialistas_huecos.py / vigia_hrp_exposicion.py de esta
sesión: `analisis_wallet_mirror_concentracion.py` corre a diario (cron
`46 6 * * *`) y ya calcula `alerta_wallet`/`alerta_mercado` por tupla
WALLET_MIRROR live, pero solo lo imprime -- nunca avisa. WALLET_MIRROR
mueve dinero real desde el 10/11/12-Ago; una concentración alta que
apareciera de un día para otro (una sola wallet dejó de operar, o un
evento puntual domina el edge medido) merece verse el mismo día, no
solo si alguien relee el log.

Avisa por Telegram con latch por FECHA (igual que vigia_hrp_exposicion
-- si la concentración sigue alta al día siguiente, vuelve a avisar,
no es un evento puntual que se resuelve solo).
"""
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/wallet_mirror_concentracion.json"
LATCH = REPO / "data/live/vigia_wallet_mirror_concentracion_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run(
        [sys.executable, str(REPO / "analisis_wallet_mirror_concentracion.py")],
        capture_output=True, text=True, timeout=120, cwd=str(REPO),
    )
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_wallet_mirror_concentracion.py: {r.stderr[-2000:]}")
        return 1

    if not DATA_PATH.exists():
        print("wallet_mirror_concentracion.json no se generó -- nada que hacer.")
        return 0
    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    hoy = datetime.now(timezone.utc).date().isoformat()

    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    claves_con_alerta_hoy = set()
    for clave, v in nuevo.get("tuplas", {}).items():
        if not (v.get("alerta_wallet") or v.get("alerta_mercado")):
            continue
        claves_con_alerta_hoy.add(clave)
        if previo.get(clave) == hoy:
            continue
        partes = []
        if v.get("alerta_wallet"):
            partes.append(f"wallet top1={v['top1_wallet_pct']}%")
        if v.get("alerta_mercado"):
            partes.append(f"mercado top1={v['top1_mercado_pct']}%")
        avisos.append(f"🪞 WALLET_MIRROR#{clave} concentración alta: {', '.join(partes)} (n={v['n_senales']})")
        previo[clave] = hoy

    previo = {k: v for k, v in previo.items() if k in claves_con_alerta_hoy}

    if avisos:
        msg = "🪞 Wallet Mirror — concentración alta:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print(f"Sin avisos nuevos hoy ({len(claves_con_alerta_hoy)} tuplas con alerta ya avisadas hoy).")

    LATCH.write_text(json.dumps(previo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
