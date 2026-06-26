"""
live_control.py — Listener de comandos Telegram para controlar el bot live.

Corre en su propia screen session. Escucha mensajes del usuario y ejecuta:
  /on      → activa live trading
  /off     → desactiva live trading
  /status  → estado actual (switch, ventana, bankroll, PNL)
  /help    → muestra comandos disponibles

Solo responde a mensajes del TELEGRAM_CHAT_ID configurado (seguridad básica).
Arrancar con: screen -dmS control python3 live_control.py
"""

import os
import time
import json
import requests
from datetime import datetime, timezone, timedelta
from pathlib import Path

TELEGRAM_TOKEN   = os.environ.get("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")
SWITCH_PATH      = Path("data/live/LIVE_MODE_ON")
TIMEOUT          = 30
POLL_INTERVAL    = 2   # segundos entre polls

LOG_PATH = Path("logs/live_control.log")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)


def log(msg: str):
    ts   = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG_PATH, "a") as f:
        f.write(line + "\n")


def enviar(texto: str) -> bool:
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return False
    try:
        r = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={"chat_id": TELEGRAM_CHAT_ID, "text": texto,
                  "parse_mode": "Markdown"},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        return True
    except Exception as e:
        log(f"Error enviando Telegram: {e}")
        return False


def get_updates(offset: int) -> list:
    try:
        r = requests.get(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates",
            params={"offset": offset, "timeout": 20, "allowed_updates": ["message"]},
            timeout=25,
        )
        r.raise_for_status()
        return r.json().get("result", [])
    except Exception as e:
        log(f"Error getUpdates: {e}")
        return []


def estado_completo() -> str:
    from live_guard import estado_live
    from live_stake import bankroll_actual, pnl_live_hoy, verificar_circuit_breaker

    est    = estado_live()
    bkr    = bankroll_actual()
    pnl_h  = pnl_live_hoy()
    cb, _  = verificar_circuit_breaker()

    switch_txt  = "✅ ON"  if est["switch"]     else "❌ OFF"
    ventana_txt = f"✅ {est['motivo']}" if est["en_ventana"] else f"❌ {est['motivo']}"
    cb_txt      = "🛑 DISPARADO" if cb else "✅ OK"
    puede_txt   = "🟢 *SÍ puede operar*" if est["puede_operar"] and not cb else "🔴 *NO puede operar*"

    return (
        f"📊 *Estado del bot live*\n"
        f"Hora Madrid: {est['hora_madrid']} ({est['dia']})\n\n"
        f"Switch:         {switch_txt}\n"
        f"Ventana:        {ventana_txt}\n"
        f"Circuit break:  {cb_txt}\n\n"
        f"Bankroll:       {bkr:.2f}€\n"
        f"PNL hoy:        {pnl_h:+.2f}€\n\n"
        f"{puede_txt}"
    )


def procesar_comando(texto: str) -> str:
    cmd = texto.strip().lower().split()[0] if texto.strip() else ""

    if cmd in ("/on", "on", "/live_on", "activar", "start"):
        SWITCH_PATH.touch()
        log("Switch activado por comando Telegram")
        return (
            "✅ *Live trading ACTIVADO*\n"
            "El bot operará en las próximas ventanas horarias.\n"
            "Usa /off para parar en cualquier momento."
        )

    elif cmd in ("/off", "off", "/live_off", "parar", "stop", "para"):
        if SWITCH_PATH.exists():
            SWITCH_PATH.unlink()
        log("Switch desactivado por comando Telegram")
        return (
            "🛑 *Live trading DESACTIVADO*\n"
            "El bot está en shadow mode. Sin operaciones reales."
        )

    elif cmd in ("/status", "status", "estado", "/estado"):
        return estado_completo()

    elif cmd in ("/update", "update", "/resumen", "resumen"):
        try:
            from shadow_resumen import (
                cargar_csv, cargar_params, RESULTS_PATH,
                CAPITAL_OPERATIVO, LAST_TG_PATH,
                _ic_bayes, _esc, _telegram_periodico
            )
            from collections import defaultdict
            from datetime import datetime, timezone
            resultados = cargar_csv(RESULTS_PATH)
            params     = cargar_params()
            ahora      = datetime.now(timezone.utc)
            pnl_total  = sum(float(r.get("pnl_neto", 0)) for r in resultados)
            bankroll   = CAPITAL_OPERATIVO + pnl_total
            hoy        = ahora.strftime("%Y-%m-%d")
            pnl_hoy    = sum(float(r.get("pnl_neto", 0)) for r in resultados
                             if (r.get("resolution_timestamp","") or "")[:10] == hoy)
            n_total    = len(resultados)
            n_win      = sum(int(r.get("acierto", 0)) for r in resultados)
            por_strat  = defaultdict(lambda: {"n": 0, "win": 0, "pnl": 0.0})
            for r in resultados:
                key = r.get("strategy","?")
                sub = r.get("subtype","")
                if sub: key = f"{key}#{sub}"
                por_strat[key]["n"]   += 1
                por_strat[key]["win"] += int(r.get("acierto", 0))
                por_strat[key]["pnl"] += float(r.get("pnl_neto", 0))
            # Forzar envío borrando el timestamp guard
            if LAST_TG_PATH.exists():
                LAST_TG_PATH.unlink()
            _telegram_periodico(ahora, bankroll, pnl_total, pnl_hoy,
                                n_total, n_win, por_strat, params)
            return "✅ Resumen enviado."
        except Exception as e:
            return f"❌ Error generando resumen: {e}"

    elif cmd in ("/help", "help", "ayuda", "/ayuda"):
        return (
            "🤖 *Comandos disponibles*\n\n"
            "/on      → Activar live trading\n"
            "/off     → Desactivar live trading\n"
            "/status  → Ver estado actual\n"
            "/update  → Resumen compacto ahora\n"
            "/help    → Ver estos comandos"
        )

    else:
        return (
            f"❓ Comando no reconocido: `{texto[:30]}`\n"
            "Usa /help para ver los comandos disponibles."
        )


def main():
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        log("ERROR: TELEGRAM_TOKEN o TELEGRAM_CHAT_ID no configurados")
        return

    log("=== live_control arrancado — escuchando comandos Telegram ===")
    enviar(
        "🤖 *Control live arrancado*\n"
        "Comandos: /on · /off · /status · /help"
    )

    offset = 0
    while True:
        updates = get_updates(offset)
        for upd in updates:
            offset = upd["update_id"] + 1
            msg = upd.get("message", {})

            # Seguridad: solo aceptar del chat configurado
            chat_id = str(msg.get("chat", {}).get("id", ""))
            if chat_id != str(TELEGRAM_CHAT_ID):
                log(f"Mensaje ignorado de chat_id={chat_id}")
                continue

            texto = msg.get("text", "").strip()
            if not texto:
                continue

            log(f"Comando recibido: {texto!r}")
            respuesta = procesar_comando(texto)
            enviar(respuesta)

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
