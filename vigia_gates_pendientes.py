#!/usr/bin/env python3
"""Vigía genérico de "gates pendientes": bloqueos/decisiones con condición de
reapertura explícita (p.ej. "mantener bloqueado hasta n>=150") registrados en
data/shadow/gates_pendientes.json. Avisa por Telegram (una vez, latch en el
propio JSON) cuando un gate cruza su n_objetivo — read-only sobre results.csv,
no toca dinero ni config.

Nace 11-Jul: BNB en ORDER_FLOW_PAIR_BLACKLIST llevaba desde el 26-jun con nota
"revisar en n>=150", cruzó el umbral (n=191) y nadie lo notó hasta un análisis
manual. Este vigía existe para que ese tipo de bloqueo no vuelva a pasar
desapercibido — decisión final de reabrir/rebloquear SIEMPRE de Javi.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

REGISTRO = REPO / "data/shadow/gates_pendientes.json"
RESULTS = REPO / "data/shadow/results.csv"


def _cargar_resultados():
    import csv
    rows = []
    with open(RESULTS, newline="") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows


def _cumple(row, gate):
    if row.get("strategy") != gate.get("strategy"):
        return False
    sub = row.get("subtype", "")
    if "par" in gate and gate["par"] not in sub:
        return False
    if "par_in" in gate and not any(p in sub for p in gate["par_in"]):
        return False
    if "decision" in gate and row.get("decision") != gate["decision"]:
        return False
    if gate.get("fecha_desde"):
        ts = row.get("resolution_timestamp", "")
        if not ts or ts[:10] < gate["fecha_desde"]:
            return False
    if gate.get("hora_utc") is not None:
        ts = row.get("resolution_timestamp", "")
        try:
            hora = int(ts[11:13]) if len(ts) >= 13 else None
        except Exception:
            hora = None
        if hora != gate["hora_utc"]:
            return False
    return True


def _stats(subset):
    n = len(subset)
    if n == 0:
        return {"n": 0, "hit": 0.0, "ic_bayes": 0.0, "pnl": 0.0}
    aciertos = sum(int(r.get("acierto", 0) or 0) for r in subset)
    pnl = sum(float(r.get("pnl_neto", 0) or 0) for r in subset)
    return {
        "n": n,
        "hit": aciertos / n,
        "ic_bayes": (aciertos + 1) / (n + 2) - 0.5,
        "pnl": pnl,
    }


def main() -> int:
    if not REGISTRO.exists():
        print("[vigia_gates] sin registro, nada que hacer")
        return 0

    registro = json.loads(REGISTRO.read_text())
    gates = registro.get("gates", [])
    if not gates:
        print("[vigia_gates] registro vacío")
        return 0

    rows = _cargar_resultados()
    avisos = []
    cambios = False

    for gate in gates:
        if gate.get("avisado"):
            continue
        subset = [r for r in rows if _cumple(r, gate)]
        st = _stats(subset)
        n_obj = gate.get("n_objetivo", 0)
        print(f"[vigia_gates] {gate['id']}: n={st['n']}/{n_obj} "
              f"ic_bayes={st['ic_bayes']:+.4f} pnl={st['pnl']:+.2f}")
        if st["n"] < n_obj:
            continue

        gate["avisado"] = True
        gate["avisado_en"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        gate["resultado_al_avisar"] = st
        cambios = True
        avisos.append(
            f"🔔 GATE PENDIENTE cruzado: {gate['id']}\n"
            f"{gate.get('descripcion', '')}\n"
            f"n={st['n']} (objetivo {n_obj}) ic_bayes={st['ic_bayes']:+.4f} "
            f"hit={st['hit']:.1%} pnl_shadow={st['pnl']:+.2f}€\n"
            f"Acción sugerida: {gate.get('accion', '(sin definir)')}"
        )

    if cambios:
        REGISTRO.write_text(json.dumps(registro, ensure_ascii=False, indent=2))

    if avisos:
        from shadow_digest import enviar_telegram
        msg = "\n\n".join(avisos)
        ok = enviar_telegram(msg)
        print(f"[vigia_gates] {len(avisos)} aviso(s) enviado(s) (telegram={ok})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
