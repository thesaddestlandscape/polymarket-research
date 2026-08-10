#!/usr/bin/env python3
"""vigia_gate_bucket_wallet_mirror.py — vigía diario del gate por
micro-bucket de precio real de Wallet Mirror (P24), mismo patrón exacto
que vigia_gate_bucket_propio.py aplicado a
data/shadow/wallet_mirror_gate_bucket.json.

Origen (10-Ago): tras rescatar SEGUIR#ETH#no_grande#15min#[0.50,0.55)
desagregando por micro-bucket de precio (ver
project_p24_wallet_mirror_refutado_ask_real_10ago), este vigía convierte
el hallazgo puntual en mecanismo recurrente -- re-corre el generador cada
día con el n fresco (wallet_mirror_executor_dryrun.csv/wallet_mirror_
sniper_dry_run.csv crecen solos), avisa por Telegram SOLO veredictos
NUEVOS (latch), y reporta cobertura (cuántos buckets siguen sin n
suficiente).

Puramente informativo -- WALLET_MIRROR no puede estar en
pares_permitidos_live (tupla sintética), nadie consume wallet_mirror_
gate_bucket.py::evaluar() todavía. Mismo criterio que vigia_log_growth.py:
el aviso es para que Javi lo sepa, no una puerta de aprobación.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/wallet_mirror_gate_bucket.json"
LATCH = REPO / "data/live/vigia_gate_bucket_wallet_mirror_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run([sys.executable, str(REPO / "analisis_wallet_mirror_gate_bucket_10ago.py")],
                        capture_output=True, text=True, timeout=300, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_wallet_mirror_gate_bucket_10ago.py: {r.stderr[-2000:]}")
        return 1

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    cobertura = []
    for clave_str, tabla in nuevo.items():
        veredictos_antes = previo.get(clave_str, {})
        n_sin_concluir = 0
        n_total_buckets = len(tabla)
        for b, info in tabla.items():
            v_nuevo = info.get("veredicto", "sin_concluir")
            v_antes = veredictos_antes.get(b, {}).get("veredicto", "sin_concluir")
            if v_nuevo != "sin_concluir":
                if v_antes != v_nuevo:
                    avisos.append(
                        f"{'🔴' if v_nuevo == 'malo_confirmado' else '🟢'} {clave_str} "
                        f"[{b},{float(b)+0.05:.2f}) -> {v_nuevo} "
                        f"(n={info['n']} pnl/tr={info['pnl_medio']:+.3f} p={info.get('shuffle_p')})"
                    )
            else:
                n_sin_concluir += 1
        if n_total_buckets:
            cobertura.append(f"{clave_str}: {n_total_buckets - n_sin_concluir}/{n_total_buckets} buckets con veredicto")

    print("\n".join(cobertura))

    if avisos:
        msg = "🪞 Wallet Mirror gate bucket — nuevos veredictos hoy:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin veredictos nuevos hoy.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
