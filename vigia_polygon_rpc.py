#!/usr/bin/env python3
"""vigia_polygon_rpc.py -- cada hora prueba TODOS los RPCs de polygon_rpc_lista.json con las tres llamadas que usa el sistema
(12-Oct, Javi: "tienes que asegurarte de que no nos rechacen peticiones nunca más"). Prueba la UNIÓN de los grupos
de polygon_rpc_lista.json:
  cabeza   eth_blockNumber (y que no vaya >50 bloques por detrás del mejor)          -> fetchers on-chain
  archivo  eth_getLogs de hace ~3,5 días en el exchange de Polymarket               -> recuperar huecos on-chain
  latest   eth_getBalance del exchange en "latest"                                   -> saldos (live_balance, rebates)
Avisa por Telegram cuando un RPC CAMBIA de estado en alguna prueba (cae o se recupera) y en 🚨 si quedan <2 RPCs
sanos para una prueba (ahí ya no hay a dónde saltar). Un fallo que sigue se recuerda cada 24 h, no cada hora.
Estado: data/live/polygon_rpc_salud.json. Cron 23 * * * *.
"""
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from polygon_rpc import error_lista, llamar, rpcs, todos  # noqa: E402

EXCHANGE = "0xe111180000d2663c0091e4f400237545b87b996b"
ESTADO = REPO / "data/live/polygon_rpc_salud.json"
BLOQUES_ARCHIVO = 150_000      # ~3,5 días (el hueco del 09-12 Oct)
MAX_RETRASO_CABEZA = 50
RECORDAR_S = 24 * 3600
MIN_SANOS = 2


def _probar(url):
    r = {}
    try:
        cab = int(llamar("eth_blockNumber", [], intentos=2, timeout=15, lista=[url], log=None), 16)
        r["cabeza"] = (True, cab)
    except Exception as e:
        r["cabeza"] = (False, f"{type(e).__name__}: {str(e)[:160]}")
        cab = None
    try:
        ref = (cab or 0) - BLOQUES_ARCHIVO
        if cab is None:
            raise RuntimeError("sin cabeza")
        logs = llamar("eth_getLogs", [{"fromBlock": hex(ref), "toBlock": hex(ref + 2), "address": EXCHANGE}],
                      intentos=2, timeout=30, lista=[url], log=None)
        r["archivo"] = (True, len(logs))
    except Exception as e:
        r["archivo"] = (False, f"{type(e).__name__}: {str(e)[:160]}")
    try:
        llamar("eth_getBalance", [EXCHANGE, "latest"], intentos=2, timeout=15, lista=[url], log=None)
        r["latest"] = (True, "ok")
    except Exception as e:
        r["latest"] = (False, f"{type(e).__name__}: {str(e)[:160]}")
    return r


def main() -> int:
    res = {u: _probar(u) for u in todos()}
    cabezas = [v["cabeza"][1] for v in res.values() if v["cabeza"][0]]
    mejor = max(cabezas) if cabezas else None
    for u, v in res.items():   # una cabeza muy retrasada cuenta como fallo de "cabeza"
        if v["cabeza"][0] and mejor is not None and mejor - v["cabeza"][1] > MAX_RETRASO_CABEZA:
            v["cabeza"] = (False, f"retrasado {mejor - v['cabeza'][1]} bloques")
    try:
        prev = json.loads(ESTADO.read_text(encoding="utf-8"))
    except Exception:
        prev = {}
    ahora, avisos, nuevo = time.time(), [], {}
    for u, v in res.items():
        nuevo[u] = {}
        for prueba, (ok, det) in v.items():
            p = (prev.get(u) or {}).get(prueba) or {}
            e = {"ok": ok, "detalle": det if not ok else "", "desde": p.get("desde", ahora) if p.get("ok") == ok else ahora,
                 "ultimo_aviso": p.get("ultimo_aviso", 0)}
            cambio = p and p.get("ok") != ok
            recordar = not ok and ahora - e["ultimo_aviso"] > RECORDAR_S
            if cambio or (not p and not ok) or recordar:
                avisos.append(f"{'✅' if ok else '❌'} {u.split('//')[1]} [{prueba}] "
                              f"{'recuperado' if ok else det}")
                e["ultimo_aviso"] = ahora
            nuevo[u][prueba] = e
    criticos = []
    err = error_lista()
    if err:
        criticos.append(f"🚨 polygon_rpc_lista.json ilegible o incompleto ({err[:120]}): TODO el sistema usa la lista por defecto")
    # /code-review 12-Oct: los sanos se cuentan DENTRO del grupo que usa cada prueba (cabeza la pide el fetch on-chain
    # con el grupo archivo; latest, los saldos)
    grupo_de = {"cabeza": set(rpcs("archivo")), "archivo": set(rpcs("archivo")), "latest": set(rpcs("latest"))}
    for prueba in ("cabeza", "archivo", "latest"):
        sanos = [u for u in res if res[u][prueba][0] and u in grupo_de[prueba]]
        if len(sanos) < MIN_SANOS:
            criticos.append(f"🚨 solo {len(sanos)} RPC(s) sanos para [{prueba}]: {', '.join(s.split('//')[1] for s in sanos) or 'NINGUNO'}")
    clave_crit = "|".join(criticos)
    if criticos and (clave_crit != prev.get("_criticos") or ahora - prev.get("_criticos_ts", 0) > RECORDAR_S):
        avisos = criticos + avisos
        nuevo["_criticos_ts"] = ahora
    else:
        nuevo["_criticos_ts"] = prev.get("_criticos_ts", 0)
    nuevo["_criticos"] = clave_crit
    nuevo["_actualizado_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    tmp = ESTADO.with_name(ESTADO.name + ".tmp")
    tmp.write_text(json.dumps(nuevo, indent=1, ensure_ascii=False), encoding="utf-8")
    tmp.replace(ESTADO)
    resumen = " | ".join(f"{u.split('//')[1].split('/')[0]}: " + "".join("✓" if res[u][k][0] else "✗" for k in ("cabeza", "archivo", "latest"))
                         for u in res)
    print(f"[{nuevo['_actualizado_utc']}] cabeza/archivo/latest -> {resumen}")
    if avisos:
        msg = "🛰️ RPCs de Polygon (cabeza/archivo/latest)\n" + "\n".join(avisos) + \
              "\nLista: polygon_rpc_lista.json (editar NO reinicia nada). Estado: data/live/polygon_rpc_salud.json"
        print(msg)
        if "--telegram" in sys.argv:
            from shadow_digest import enviar_telegram
            enviar_telegram(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
