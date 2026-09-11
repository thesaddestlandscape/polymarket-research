#!/usr/bin/env python3
"""vigia_resolution_sniper_precierre.py — Vigía del gate riguroso de
RESOLUTION_SNIPER_PRECIERRE (resolution_sniper_precierre_gate_riguroso.json,
usado por resolution_sniper_precierre_gate.py -> resolution_sniper_precierre_
executor.py). Hueco real encontrado 07-Sep (petición Javi: "ampliamos a
todas las monedas, no solo coge btc"): el ejecutor YA evalúa las 6 monedas
desde su construcción (04-Sep), pero el JSON del gate riguroso NO tenía
NINGÚN cron que lo regenerase -- solo se actualizaba si alguien corría
analisis_gate_riguroso_resolution_sniper_precierre_02sep.py a mano en una
sesión. Mismo patrón de bug ya cazado varias veces en este proyecto (CLAUDE.md
pt.15/16): infraestructura sin cron/screen = "se me olvidó conectarlo". Sin
esto, aunque SOL#[0.50,0.55) offset=-2s (n=16 hoy, ya p_bh_signif=True,
split_half_positivo_ambas=True, wilson90lo=0.855 >> breakeven=0.512 -- solo
le falta n, no rigor) cruce n>=40 mañana, el ejecutor seguiría leyendo el
veredicto "sin_concluir" de hace días hasta la próxima sesión manual.

Mismo patrón exacto que vigia_gate_bucket_propio.py: (1) re-corre el
generador (barato, ~9s), (2) diffea contra un latch, (3) avisa por Telegram
SOLO veredictos NUEVOS (sin_concluir -> bueno_confirmado), nunca repite
ruido. Puramente informativo/de reconexión -- no toca prob_yes/stake, el
propio resolution_sniper_precierre_gate.py ya relee el JSON por mtime en
cada instante crítico del ejecutor (fail-closed: sin JSON fresco o sin
veredicto confirmado, no dispara).
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/resolution_sniper_precierre_gate_riguroso.json"
LATCH = REPO / "data/live/vigia_resolution_sniper_precierre_latch.json"
GENERADOR = REPO / "analisis_gate_riguroso_resolution_sniper_precierre_02sep.py"


def _claves_confirmadas(data: dict) -> dict:
    """Aplana por_offset[*][grid|fino] a {clave_unica: info} para diffear."""
    out = {}
    for offset, bloque in data.get("por_offset", {}).items():
        for tipo in ("grid", "fino"):
            for k, v in bloque.get(tipo, {}).items():
                out[f"{offset}|{tipo}|{k}"] = v
    return out


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run([sys.executable, str(GENERADOR)], capture_output=True,
                        text=True, timeout=120, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando {GENERADOR.name}: {r.stderr[-2000:]}")
        return 1

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    claves_nuevo = _claves_confirmadas(nuevo)
    claves_previo = _claves_confirmadas(previo)

    # 07-Sep: grid y fino NO comparten esquema de claves -- grid usa
    # 'p_shuffle'/'split_half_positivo_ambas', fino usa 'p_valor'/
    # 'split_half_ok'; y hay un 3er veredicto ('n_insuficiente_para_ventana',
    # sin ninguna otra clave estadística) que grid no produce nunca. Todo
    # acceso vía .get() con default -- nunca asumir que un dict de
    # veredicto trae las mismas claves que otro.
    avisos = []
    n_sin_concluir = 0
    n_total = len(claves_nuevo)
    cerca_del_umbral = []  # sin_concluir pero ya con rigor propio pasado, solo falta n
    for clave, v in sorted(claves_nuevo.items()):
        v_nuevo = v.get("veredicto", "sin_concluir")
        v_antes = claves_previo.get(clave, {}).get("veredicto", "sin_concluir")
        p_valor = v.get("p_shuffle", v.get("p_valor"))
        split_half_ok = v.get("split_half_positivo_ambas", v.get("split_half_ok"))
        if v_nuevo == "bueno_confirmado":
            if v_antes != "bueno_confirmado":
                p_txt = f"{p_valor:.4f}" if p_valor is not None else "?"
                avisos.append(
                    f"🟢 {clave} -> bueno_confirmado (n={v.get('n')} hit={v.get('hit', 0):.3f} "
                    f"wilson90lo={v.get('wilson90lo', 0):.3f} pnl_medio={v.get('pnl_medio', 0):+.3f} "
                    f"p={p_txt})"
                )
        else:
            n_sin_concluir += 1
            if (v_nuevo != "n_insuficiente_para_ventana" and v.get("p_bh_signif") and split_half_ok
                    and not v.get("n_min_live_ok") and v.get("pnl_medio", 0) > 0):
                wl = v.get("wilson90lo")
                wl_txt = f"{wl:.3f}" if wl is not None else "?"
                cerca_del_umbral.append(f"{clave} (n={v.get('n')}/40, wilson90lo={wl_txt})")

    print(f"cobertura: {n_total - n_sin_concluir}/{n_total} claves con veredicto bueno_confirmado")
    if cerca_del_umbral:
        print("cerca del umbral (rigor OK, solo falta n>=40): " + "; ".join(cerca_del_umbral))

    if avisos:
        msg = "🎯 Resolution Sniper Precierre — nuevos veredictos hoy:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin veredictos nuevos.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
