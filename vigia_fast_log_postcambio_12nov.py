#!/usr/bin/env python3
"""vigia_fast_log_postcambio_12nov.py -- monitor temporal (cron */10, 48 h) tras el cambio de
live_trade.py (commit d0388b87f32, CLOB API 14-Dic). Lee SOLO lo nuevo de logs/fast.log
(offset en data/live/vigia_fast_log_postcambio_state.json) y avisa por Telegram si aparece
Traceback / error de tipo de código / línea del camino maker tocado. Al cumplirse el plazo
envía un resumen 'sin errores' (o con el total) y se desactiva solo. Solo lectura."""
import json, re, sys, time
from pathlib import Path
REPO = Path(__file__).resolve().parent
LOG = REPO / "logs" / "fast.log"
ST = REPO / "data" / "live" / "vigia_fast_log_postcambio_state.json"
FIN = 1794641400  # 2026-11-14T07:30Z (48 h tras el despliegue)
PAT = re.compile(r"Traceback \(most recent|NameError|TypeError|AttributeError|SyntaxError|KeyError|"
                 r"cid_maker|maker: |get_open_orders|condition_id|🚨.*live_trade", re.I)
RUIDO = re.compile(r"huérfana .* sin condition_id|Gamma falló")  # esperados: se cuentan, avisan aparte


def main() -> int:
    try:
        st = json.loads(ST.read_text())
    except Exception:
        st = {"offset": LOG.stat().st_size, "avisos": 0, "esperados": 0, "inicio": time.time()}
    if st.get("fin"):
        return 0
    try:
        size = LOG.stat().st_size
        off = st["offset"] if size >= st["offset"] else 0   # rotación
        with open(LOG, "rb") as f:
            f.seek(off); datos = f.read(size - off); st["offset"] = size
    except Exception as e:
        datos = b""; print(f"no se pudo leer fast.log: {e}")
    lineas = datos.decode("utf-8", "replace").splitlines()
    malas = [l for l in lineas if PAT.search(l) and not RUIDO.search(l)]
    st["esperados"] += sum(1 for l in lineas if RUIDO.search(l))
    msgs = []
    if malas:
        st["avisos"] += len(malas)
        msgs.append("🔎 live_trade post-cambio 12-Nov: %d línea(s) a revisar en logs/fast.log:\n%s"
                    % (len(malas), "\n".join(l[:200] for l in malas[:6])))
    if time.time() >= FIN:
        st["fin"] = True
        msgs.append("✅ Monitor live_trade 48 h terminado: %d línea(s) a revisar en total, %d esperadas "
                    "(huérfana sin condition_id). Cron a retirar." % (st["avisos"], st["esperados"]))
    ST.write_text(json.dumps(st))
    if msgs:
        try:
            sys.path.insert(0, str(REPO))
            from shadow_digest import enviar_telegram
            for m in msgs:
                enviar_telegram(m)
        except Exception as e:
            print(f"telegram falló: {e}\n" + "\n".join(msgs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
