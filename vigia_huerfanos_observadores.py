#!/usr/bin/env python3
"""vigia_huerfanos_observadores.py -- cron cada 5 min (instalar: ver pie). Avisa por Telegram si hay procesos
`observadores_fase0.py` o `libro_estado_ws.py --hijo` con ppid 1 durante >10 min seguidos (27-Nov).

Origen: el 27-Nov se encontraron 41 `observadores_fase0.py` huerfanos (11-12 dias, ~30 MB de swap cada uno). Causa medida:
el stub `observadores_fase0.py` de tests/test_e2e_real.py (calma_v3/cobertura_5m_13nov/v3) se lanza con start_new_session y su
`_matar_sandbox` busca el sandbox en la cmdline, que no lo contiene (ruta relativa): cada ensayo e2e dejaba un stub vivo. El
reinicio de produccion (screen quit -> SIGHUP) NO filtra: el hijo real muere <=0,2 s tras matar al padre (medidas_muerte_hijo.txt).
Solo lectura de /proc; sin red salvo el Telegram. Latch SIN valores recalculados en la firma: un aviso por episodio
(avisado=True hasta que desaparezcan todos) + un aviso de recuperacion.
"""
import json
import os
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent
LATCH = REPO / "data/live/vigia_huerfanos_observadores_latch.json"
UMBRAL_S = 600  # 10 min


def _args(pid_dir: Path):
    try:
        raw = (pid_dir / "cmdline").read_bytes()
    except OSError:
        return None
    return [a.decode(errors="replace") for a in raw.split(b"\0") if a]


def _ppid(pid_dir: Path):
    try:
        for ln in (pid_dir / "status").read_text().splitlines():
            if ln.startswith("PPid:"):
                return int(ln.split()[1])
    except (OSError, ValueError):
        pass
    return None


def es_objetivo(args) -> bool:
    """python ... observadores_fase0.py  |  python ... libro_estado_ws.py --hijo. Excluye SCREEN y el `bash -c` envoltorio."""
    if not args or not os.path.basename(args[0]).startswith("python"):
        return False
    resto = args[1:]
    if any(os.path.basename(a) == "observadores_fase0.py" for a in resto):
        return True
    return any(os.path.basename(a) == "libro_estado_ws.py" for a in resto) and "--hijo" in resto


def listar_huerfanos(proc_root="/proc"):
    """[(pid, args)] de los procesos objetivo con ppid 1."""
    out = []
    for d in Path(proc_root).iterdir():
        if not d.name.isdigit():
            continue
        a = _args(d)
        if a is None or not es_objetivo(a) or _ppid(d) != 1:
            continue
        out.append((int(d.name), " ".join(a)[:160]))
    return sorted(out)


def decidir(prev: dict, pids, ahora: float, umbral_s: int = UMBRAL_S):
    """Devuelve (nuevo_estado, accion) con accion en {None,'avisar','recuperado'}. Sin huerfanos: se resetea todo.
    desde = primer instante del episodio actual (continuo); avisado solo pasa a True una vez por episodio."""
    if not pids:
        accion = "recuperado" if prev.get("avisado") else None
        return {"desde": None, "avisado": False}, accion
    desde = prev.get("desde") or ahora
    avisado = bool(prev.get("avisado"))
    accion = None
    if not avisado and ahora - desde > umbral_s:
        accion, avisado = "avisar", True
    return {"desde": desde, "avisado": avisado}, accion


def main() -> int:
    ahora = time.time()
    try:
        prev = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        prev = {}
    h = listar_huerfanos()
    estado, accion = decidir(prev, [p for p, _ in h], ahora)
    print(f"[vigia_huerfanos_observadores] huerfanos={len(h)} pids={[p for p, _ in h][:10]} accion={accion}", flush=True)
    if accion:
        from shadow_digest import enviar_telegram
        if accion == "avisar":
            msg = (f"🧟 VIGÍA huérfanos observadores: {len(h)} proceso(s) observadores_fase0.py/libro_estado_ws --hijo "
                   f"con ppid 1 desde hace >{UMBRAL_S // 60} min (ej. pids {[p for p, _ in h][:5]}). "
                   f"Cada uno ~30 MB de swap. Matar por PID tras comprobar cwd (/proc/<pid>/cwd) y que no es el vivo.")
        else:
            msg = "✅ VIGÍA huérfanos observadores: ya no quedan procesos huérfanos"
        ok = enviar_telegram(msg)
        print(f"[vigia_huerfanos_observadores] aviso enviado (telegram={ok})", flush=True)
        if accion == "avisar" and not ok:
            estado["avisado"] = False  # reintenta en el siguiente ciclo si el envio fallo
    LATCH.parent.mkdir(parents=True, exist_ok=True)
    tmp = LATCH.with_suffix(".tmp")
    tmp.write_text(json.dumps(estado))
    os.replace(tmp, LATCH)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_huerfanos_observadores] ERROR {type(e).__name__}: {e}", flush=True)
        sys.exit(0)

# Cron propuesto (lo instala la sesion principal; NO instalado):
# */5 * * * * cd /root/polymarket-research && nice -n 10 .venv/bin/python vigia_huerfanos_observadores.py >> logs/vigia_huerfanos_observadores.log 2>&1 || true
