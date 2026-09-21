#!/usr/bin/env python3
"""vigia_edge_quirurgico.py -- envoltorio de edge_quirurgico_rolling.py para el planificador
vigias_frecuentes_fase0.py (carril "quirurgico", cada 3h) + AVISOS POR TELEGRAM (21-Sep,
petición explícita Javi: "un vigía de telegram diario y que me avise cada vez que haya cambios
en micro-bucket quirúrgico").

Corre el generador en un SUBPROCESO (nice 10): es trabajo numpy y en el mismo proceso competiria
por el GIL con el resto de vigias. Devuelve 0/1 (convencion de las tareas de carril aparte: un
fallo se reintenta en 300 s, no a las 3 h).

Avisos (bot "cripto"):
  * CAMBIOS -- una zona ENTRA como operable, SUBE a estricta (IC90 forward > 0), BAJA de estricta o SALE.
    Firma = tupla|ancho|lo|hi + estado (NUNCA los numeros recalculados cada ciclo: mismo bug de
    latch que ya se corrigio en vigia_sigma_patrones / vigia_causal_vs_fillable). Histeresis: un
    cambio solo se avisa si se observa en 2 corridas seguidas (~6h), para que una zona pegada al
    umbral no genere ruido.
  * RESUMEN DIARIO -- a partir de las 07:00 UTC, una vez al dia, siempre (haya o no cambios).
La primera ejecucion (sin latch) inicializa el estado en silencio y solo envia el resumen."""
import json
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
ZONAS = REPO / "data" / "shadow" / "edge_quirurgico_zonas.json"
HISTORIAL = REPO / "data" / "shadow" / "edge_quirurgico_historial.jsonl"
LATCH = REPO / "data" / "shadow" / "edge_quirurgico_telegram_latch.json"
HORA_RESUMEN_UTC = 7
CORRIDAS_CONFIRMAR = 2


def _clave(z: dict) -> str:
    return f"{z['tupla']}|{z['ancho']}|{z['lo']}|{z['hi']}"


def _estados(zonas_json: dict) -> dict:
    """{clave: 'estricta'|'operable'} -- solo las zonas con forward_ok."""
    est = {}
    for z in zonas_json.get("zonas_operables", []):
        est[_clave(z)] = "estricta" if z.get("forward_ok_estricto") else "operable"
    return est


def _etiqueta(k: str, zonas_json: dict) -> str:
    t, ancho, lo, hi = k.split("|")
    z = next((z for z in zonas_json.get("zonas_operables", []) + zonas_json.get("zonas_en_observacion", [])
              if _clave(z) == k), None)
    extra = ""
    if z:
        extra = (f" [{z['estado_config']}] train n={z['n_train']} {z['pnl_train']:+.2f} -> "
                 f"fwd n={z['n_forward']} {z['pnl_forward'] if z['pnl_forward'] is not None else 0:+.2f}")
    return f"{t} w={ancho} [{float(lo):.2f},{float(hi):.2f}){extra}"


def _persistencia() -> dict:
    """{clave: dias distintos en que estuvo operable} desde el historial."""
    por_dia = defaultdict(set)
    if HISTORIAL.exists():
        for linea in HISTORIAL.read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(linea)
            except Exception:
                continue
            if r.get("forward_ok"):
                por_dia[f"{r['tupla']}|{r['ancho']}|{r['lo']}|{r['hi']}"].add(r["fecha"])
    return {k: len(v) for k, v in por_dia.items()}


def _cambios(actual: dict, latch: dict) -> tuple[list, dict]:
    """Aplica histeresis. Devuelve (avisos_confirmados, latch_nuevo)."""
    confirmado = dict(latch.get("confirmado", {}))
    pendiente = dict(latch.get("pendiente", {}))
    avisos = []
    for k in set(actual) | set(confirmado):
        nuevo, viejo = actual.get(k, "fuera"), confirmado.get(k, "fuera")
        if nuevo == viejo:
            pendiente.pop(k, None)
            continue
        p = pendiente.get(k)
        cnt = (p["cnt"] + 1) if (p and p["estado"] == nuevo) else 1
        if cnt >= CORRIDAS_CONFIRMAR:
            avisos.append((k, viejo, nuevo))
            if nuevo == "fuera":
                confirmado.pop(k, None)
            else:
                confirmado[k] = nuevo
            pendiente.pop(k, None)
        else:
            pendiente[k] = {"estado": nuevo, "cnt": cnt}
    return avisos, {**latch, "confirmado": confirmado, "pendiente": pendiente}


def _texto_cambios(avisos: list, zonas_json: dict) -> str:
    lin = ["🔬 Edge quirúrgico — cambios en micro-buckets (validación forward 7d):"]
    for k, viejo, nuevo in sorted(avisos, key=lambda a: a[0]):
        icono = {"fuera": "⚪", "operable": "🟢", "estricta": "🟢🟢"}
        if nuevo == "fuera":
            lin.append(f"🔴 SALE ({viejo}): {_etiqueta(k, zonas_json)}")
        elif viejo == "fuera":
            lin.append(f"{icono[nuevo]} ENTRA como {nuevo}: {_etiqueta(k, zonas_json)}")
        elif nuevo == "estricta":
            lin.append(f"🟢🟢 SUBE a estricta (IC90>0): {_etiqueta(k, zonas_json)}")
        else:
            lin.append(f"🟡 BAJA a operable (pierde IC90>0): {_etiqueta(k, zonas_json)}")
    return "\n".join(lin)


def _texto_resumen(zonas_json: dict, estados: dict) -> str:
    n_est = sum(1 for v in estados.values() if v == "estricta")
    pers = _persistencia()
    cob = zonas_json.get("cobertura", {})
    desc = cob.get("descartadas_n_train_insuficiente", [])
    lin = [f"🔬 Edge quirúrgico — resumen diario ({zonas_json.get('generado_utc', '?')[:16]} UTC)",
           f"cobertura: {cob.get('evaluadas', zonas_json.get('n_tuplas_evaluadas'))}/{cob.get('total_tuplas_con_datos', '?')} "
           f"tuplas SNIPER/DISPERSO/WEEKLY/WALLET_MIRROR con datos suficientes"
           + (f" ({len(desc)} sin n: " + ", ".join(f"{t}={n}" for t, n in desc[:4]) + ("…" if len(desc) > 4 else "") + ")" if desc else ""),
           f"zonas operables: {len(estados)} (estrictas IC90>0: {n_est}) | en observación: {zonas_json.get('n_zonas_en_observacion')}",
           "modo LECTURA: nada de esto opera todavía."]
    zs = zonas_json.get("zonas_operables", [])
    for z in sorted(zs, key=lambda z: (not z.get("forward_ok_estricto"), -(z.get("pnl_forward") or 0))):
        k = _clave(z)
        lin.append(f"{'🟢🟢' if z.get('forward_ok_estricto') else '🟢'} {_etiqueta(k, zonas_json)} "
                   f"| días operable: {pers.get(k, 1)}")
    persist = sorted([(d, k) for k, d in pers.items() if d >= 2], reverse=True)[:5]
    if persist:
        lin.append("Persistentes (≥2 días): " + "; ".join(f"{k.split('|')[0]} {k.split('|')[1]} ({d}d)" for d, k in persist))
    return "\n".join(lin)


def _enviar_partido(enviar, texto: str, limite: int = 3500) -> bool:
    """Telegram corta a 4096 chars: se parte por lineas. True solo si TODOS los trozos salieron."""
    trozos, actual = [], ""
    for linea in texto.split("\n"):
        if len(actual) + len(linea) + 1 > limite and actual:
            trozos.append(actual); actual = ""
        actual += linea + "\n"
    if actual:
        trozos.append(actual)
    return all([enviar(t.rstrip("\n")) for t in trozos])


def avisar(zonas_json: dict, enviar, ahora: datetime = None, latch_path: Path = LATCH) -> list:
    """Lógica de avisos, separada de main() para poder probarla con un `enviar` falso."""
    ahora = ahora or datetime.now(timezone.utc)
    try:
        latch = json.loads(latch_path.read_text(encoding="utf-8")) if latch_path.exists() else None
    except Exception:
        latch = None
    actual = _estados(zonas_json)
    enviados = []
    primera = latch is None
    if primera:
        latch = {"confirmado": dict(actual), "pendiente": {}, "ultimo_resumen": ""}   # init silencioso
    else:
        avisos, latch = _cambios(actual, latch)
        if avisos:
            txt = _texto_cambios(avisos, zonas_json)
            if _enviar_partido(enviar, txt):
                enviados.append(txt)
            else:
                # no se pudo enviar: NO consolidar el cambio (se reintenta en la proxima corrida)
                latch = json.loads(latch_path.read_text(encoding="utf-8"))
    hoy = ahora.strftime("%Y-%m-%d")
    if ahora.hour >= HORA_RESUMEN_UTC and latch.get("ultimo_resumen") != hoy:
        txt = _texto_resumen(zonas_json, actual)
        if _enviar_partido(enviar, txt):
            latch["ultimo_resumen"] = hoy
            enviados.append(txt)
    tmp = latch_path.with_name(latch_path.name + ".tmp")
    tmp.write_text(json.dumps(latch, ensure_ascii=False), encoding="utf-8")
    tmp.replace(latch_path)
    return enviados


def main() -> int:
    r = subprocess.run(["nice", "-n", "10", sys.executable, str(REPO / "edge_quirurgico_rolling.py")],
                       capture_output=True, text=True, timeout=2400, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando edge_quirurgico_rolling.py (rc={r.returncode}): {r.stdout[-300:]} {r.stderr[-1200:]}")
        return 1
    print(r.stdout[-1500:])
    try:
        from shadow_digest import enviar_telegram
        zonas = json.loads(ZONAS.read_text(encoding="utf-8"))
        enviados = avisar(zonas, lambda t: enviar_telegram(t, bot="cripto"))
        print(f"telegram: {len(enviados)} mensaje(s) enviado(s)")
    except Exception as e:   # un fallo de aviso no debe marcar como roto el generador
        print(f"aviso: no se pudo procesar/enviar Telegram: {type(e).__name__}: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
