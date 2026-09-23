"""zonas_forward_pgallina.py -- (23-Sep, aprobado por Javi: "Sí, me parece bien") fuente ADITIVA de
apertura para el ejecutor P-GALLINA (dispersed_bot_executor_dryrun.py), para cerrar el Stage 0.

Origen: buscador de edge perdido aplicado al universo P-GALLINA con precio EJECUTABLE (23-Sep). Zonas
que se sostuvieron de train (10-16 Sep) a forward (17-23 Sep), agrupando por el ASK (no por el precio
de la wallet: por precio de wallet el edge desaparece):
  - DISPERSO#BTC#5min#BUY_Up  ask [0,75,0,80): fwd n=144 +0,121/tr IC90 [+0,05,+0,19]
  - SNIPER#ETH#5min#BUY_Down  ask [0,70,0,75): fwd n=69 +0,099/tr IC90 [-0,01,+0,21] (la más justa)
El gate canónico (bot_wallets_gate_bucket) las tiene en sin_concluir por falta de días independientes
(solo 14 días con precio de decisión). Esta fuente las abre SOLO en ese rango de ask exacto y con
kill-switch propio sobre los trades REALES desde `desde`:
  - n_real >= n_min y media < pnl_media_min  -> se cierra (latch persistente, aviso Telegram)
  - pérdida acumulada real <= -perdida_max_eur -> se cierra
Fail-closed: JSON ilegible/ausente, zona inexistente, ask fuera de rango o kill -> NO abre.
Las zonas con modo "dry_run" nunca abren nada: solo las sigue el vigía diario.
"""
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
RUTA = REPO / "data" / "live" / "zonas_forward_pgallina.json"
LATCH = REPO / "data" / "live" / "zonas_forward_pgallina_kill.json"
TRADES = REPO / "data" / "live" / "trades.csv"

_cache = {"mtime": None, "zonas": {}}


def cargar() -> dict:
    """{tupla: zona} de zonas en modo 'live'. Fail-closed a {}."""
    try:
        m = RUTA.stat().st_mtime
        if _cache["mtime"] != m:
            d = json.loads(RUTA.read_text(encoding="utf-8"))
            _cache["zonas"] = {z["tupla"]: z for z in d.get("zonas", []) if z.get("modo") == "live"}
            _cache["mtime"] = m
        return _cache["zonas"]
    except Exception:
        return {}


def _tupla_a_trade(tupla: str):
    """'DISPERSO#BTC#5min#BUY_Up' -> ('DISPERSO', 'BTC#5min', 'BUY_YES') (convención de trades.csv)."""
    arq, activo, marco, dec = tupla.split("#")
    return arq, f"{activo}#{marco}", "BUY_YES" if dec == "BUY_Up" else "BUY_NO"


def _trades_zona(tupla: str, desde: str, lo: float, hi: float):
    """(pnls_cerrados, stakes_abiertos) de la tupla desde `desde` con signal_ask en [lo,hi).
    /code-review 23-Sep: un CLOSED sin pnl_neto_eur cuenta como stake PERDIDO (fail-closed, nunca 0)."""
    arq, sub, dire = _tupla_a_trade(tupla)
    cerrados, abiertos = [], []
    try:
        with open(TRADES, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if (r.get("strategy") != arq or r.get("subtype") != sub or r.get("direction") != dire
                        or (r.get("timestamp_utc") or "") < desde):
                    continue
                try:
                    ask = float(r.get("signal_ask") or "x")
                except ValueError:
                    continue
                if not (lo - 1e-9 <= ask < hi + 1e-9):
                    continue
                try:
                    stake = float(r.get("stake_eur") or 1.05)
                except ValueError:
                    stake = 1.05
                if r.get("status") == "OPEN":
                    abiertos.append(stake)
                elif r.get("status") == "CLOSED":
                    try:
                        cerrados.append(float(r["pnl_neto_eur"]))
                    except (KeyError, TypeError, ValueError):
                        cerrados.append(-stake)
    except OSError:
        return [], []
    return cerrados, abiertos


def trades_reales(tupla: str, desde: str, lo: float, hi: float) -> list:
    """PnL de los trades reales CLOSED de la zona (para el rastreador)."""
    return _trades_zona(tupla, desde, lo, hi)[0]


def solo_zona(tupla: str) -> bool:
    """/code-review 23-Sep: tuplas añadidas a la whitelist SOLO por su zona -- el ejecutor no debe
    abrirlas por la vía del gate canónico (que no distingue lado ni rango de ask)."""
    z = cargar().get(tupla)
    return bool(z and z.get("solo_zona", True))


def edge(tupla: str):
    """Edge medido de la zona (para stake y re-quote), o None."""
    z = cargar().get(tupla)
    try:
        return float(z["edge"]) if z and z.get("edge") is not None else None
    except (TypeError, ValueError):
        return None


def _latch() -> dict:
    try:
        return json.loads(LATCH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def evaluar_kill(tupla: str, zona: dict) -> tuple[bool, str]:
    """(matada, motivo). Persiste el kill en LATCH (no se reabre solo)."""
    lt = _latch()
    if lt.get(tupla, {}).get("matada"):
        return True, lt[tupla].get("motivo", "latch")
    k = zona.get("kill", {})
    pnls, abiertos = _trades_zona(tupla, zona["desde"], zona["lo"], zona["hi"])
    peor_caso = sum(pnls) - sum(abiertos)   # /code-review: las posiciones abiertas cuentan como perdidas
    motivo = ""
    if len(pnls) >= k.get("n_min", 20) and sum(pnls) / len(pnls) < k.get("pnl_media_min", 0.0):
        motivo = f"media {sum(pnls)/len(pnls):+.3f} en n={len(pnls)} reales"
    elif peor_caso <= -abs(k.get("perdida_max_eur", 3.0)):
        motivo = (f"pérdida acumulada peor caso {peor_caso:+.2f}€ (cerrados {sum(pnls):+.2f}€ n={len(pnls)}, "
                  f"abiertos {len(abiertos)} por {sum(abiertos):.2f}€)")
    if motivo:
        lt[tupla] = {"matada": True, "motivo": motivo, "ts": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        try:
            LATCH.write_text(json.dumps(lt, ensure_ascii=False, indent=1), encoding="utf-8")
            from shadow_digest import enviar_telegram
            enviar_telegram(f"🛑 Zona forward P-GALLINA CERRADA por kill-switch: {tupla} "
                            f"[{zona['lo']:.2f},{zona['hi']:.2f}) -- {motivo}")
        except Exception:
            pass
        return True, motivo
    return False, ""


def permitido(tupla: str, ask) -> tuple[bool, float | None]:
    """(abre, techo_precio). Abre SOLO si la tupla tiene zona live, ask en [lo,hi) y no está matada.
    techo_precio = hi (para que el re-quote aborte si el precio sale de la zona por arriba)."""
    z = cargar().get(tupla)
    if not z:
        return False, None
    try:
        a = float(ask)
    except (TypeError, ValueError):
        return False, None
    if not (z["lo"] <= a < z["hi"]):
        return False, None
    matada, _ = evaluar_kill(tupla, z)
    if matada:
        return False, None
    return True, float(z["hi"])
