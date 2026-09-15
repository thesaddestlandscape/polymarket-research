#!/usr/bin/env python3
"""analisis_kelly_precio_wallet_familias_15sep.py — 15-Sep, petición
explícita Javi ("masterizar" SNIPER/DISPERSO/WALLET_MIRROR/CANDIDATA9,
punto 1, "dale al 1"): corrección de Kelly por precio de entrada para
las familias que NO pasan por results.csv (mismo problema de fondo que
analisis_kelly_precio_gate_29jul.py ya solucionó para GBM_LATE/FAVORITO/
BALLENAS/UPDOWN_GBM, pero ese script no puede ver esta familia -- lee
results.csv, y DISPERSED_BOT/WALLET_MIRROR nunca escriben ahí).

Por qué aquí la corrección NO necesita el mismo rigor estadístico
(Wilson+shuffle+split-half+BH-FDR) que el script original: para las
familias de results.csv, `ic_bayes` es un SCORE de modelo cuya relación
exacta con (p_hat-precio) no se conoce de antemano -- por eso hace falta
validar empíricamente si el ratio_correccion observado es real o ruido.
Para DISPERSED_BOT (SNIPER+DISPERSO) y WALLET_MIRROR, el "ic" que
`calcular_stake()` recibe YA ES una medición directa del edge real
(`bot_wallets_gate_bucket.py::edge_estimado()` = hit_rate-ask_medio
literal, o `edge_pp_validado/100` para Wallet Mirror) -- no un score de
modelo. La fórmula de Kelly exacto es determinista una vez se acepta
que "ic" representa (p_hat-precio) sin normalizar:

  f_actual = |ic| * 0.5
  f_exacto = max(0, ic / (1 - precio)) * 0.5
  ratio_correccion = f_exacto / f_actual = 1 / (1 - precio)   (si ic>0)

Es geometría, no estadística -- el ÚNICO rigor que hace falta aquí es
confirmar que el propio "ic" (edge medido) tiene evidencia suficiente
(n>=15), lo cual YA exige bot_wallets_edge_medido_real.json (SNIPER/
DISPERSO) y el propio veredicto bueno_confirmado con n>=40 (WALLET_
MIRROR, que ya exige N_MIN=40 desde el 01-Sep). No se reimplementa
ningún cálculo de edge aquí, solo se consulta lo que ya existe.

CANDIDATA9_BOT_CONSENSO deliberadamente EXCLUIDA: su stake usa
ic_conviccion=0.05 fijo a propósito ("empezando con stake mínimo",
petición explícita Javi) y siempre se flooriza a min_stake_eur después
-- una corrección de Kelly aquí no cambiaría nada en la práctica.

Salida: fusiona (nunca sobrescribe) las claves "DISPERSED_BOT" y
"WALLET_MIRROR" dentro de data/shadow/kelly_precio_gate.json (MISMA
estructura que analisis_kelly_precio_gate_29jul.py genera, consumida sin
cambios por kelly_precio_gate.py::evaluar() -- family="DISPERSED_BOT"
subtype="activo#marco", family="WALLET_MIRROR" subtype="activo#marco").

Cron diario (ver crontab, franja de vigías 06:00-08:33 UTC).
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

STEP = 0.10
N_MIN_WALLET_MIRROR = 40  # mismo N_MIN que wallet_mirror_gate_bucket_10ago.py exige desde 01-Sep

KELLY_GATE_PATH = REPO / "data" / "shadow" / "kelly_precio_gate.json"
BOT_WALLETS_EDGE = REPO / "data" / "shadow" / "bot_wallets_edge_medido_real.json"
WALLET_MIRROR_GATE = REPO / "data" / "shadow" / "wallet_mirror_gate_bucket.json"


def _bucket10(precio: float) -> float:
    import math
    return round(math.floor(precio / STEP + 1e-9) * STEP, 4)


def _dispersed_bot_familia() -> dict:
    """clave 'activo#marco' -> {bucket_str: {ratio_correccion, n, veredicto}}
    UNION de evidencia SNIPER+DISPERSO (calcular_stake() no distingue
    arquetipo en el subtype -- ver docstring del módulo) para ese
    activo/marco. Un bucket de precio 0.10 puede agrupar varios buckets
    de 0.05 de bot_wallets_edge_medido_real.json -- si hay más de uno,
    nos quedamos con el de mayor n (más evidencia)."""
    if not BOT_WALLETS_EDGE.exists():
        return {}
    edge_data = json.loads(BOT_WALLETS_EDGE.read_text(encoding="utf-8"))
    # También necesitamos "n" real por bucket -- lo sacamos de bot_wallets_gate_bucket.json
    gate_data = {}
    gate_path = REPO / "data" / "shadow" / "bot_wallets_gate_bucket.json"
    if gate_path.exists():
        gate_data = json.loads(gate_path.read_text(encoding="utf-8"))

    por_activo_marco = {}
    for clave, edge in edge_data.items():
        arquetipo, activo, marco, b_str = clave.split("#")
        b10 = _bucket10(float(b_str))
        gate_key = f"{arquetipo}#{activo}#{marco}"
        gate_bucket = gate_data.get(gate_key, {}).get(b_str, {})
        n = gate_bucket.get("n", 0)
        act_marco = f"{activo}#{marco}"
        actual = por_activo_marco.setdefault(act_marco, {})
        prev = actual.get(f"{b10:.2f}")
        if prev is None or n > prev["n"]:
            # /code-review 15-Sep, 2 hallazgos reales corregidos:
            # (1) ratio=1/(1-precio) SOLO es la fórmula correcta si el
            # edge medido es POSITIVO (docstring del módulo, "si ic>0")
            # -- con edge<=0 el f_exacto real es 0 (veto), nunca un
            # boost. bot_wallets_edge_medido_real.json se remide a diario
            # y puede pasar a negativo si el régimen degrada (mismo
            # riesgo que CLAUDE.md pt.9/17/22 vigila en todo el proyecto)
            # -- sin este check, un bucket con edge ya negativo seguiría
            # recibiendo un multiplicador >1x sobre dinero real.
            # (2) exigir también que el veredicto ACTUAL del gate sea
            # bueno_confirmado (mismo criterio que _wallet_mirror_
            # familia() ya aplicaba, faltaba aquí) -- un bucket puede
            # seguir en BUCKETS_APROBADOS_REAL (whitelist estática) pero
            # haber girado a malo_confirmado en el gate vivo.
            edge_positivo = edge is not None and float(edge) > 0
            gate_confirma = gate_bucket.get("veredicto") == "bueno_confirmado"
            ratio = round(1.0 / (1.0 - b10), 4) if (b10 < 0.95 and edge_positivo and gate_confirma) else None
            actual[f"{b10:.2f}"] = {
                "n": n, "ratio_correccion": ratio,
                "veredicto": "confirmado" if (n >= 15 and ratio is not None) else "sin_concluir",
                "fuente": f"{arquetipo}#{b_str}",
            }
    return por_activo_marco


def _wallet_mirror_familia() -> dict:
    """clave 'activo#marco' -> {bucket_str: {...}}. wallet_mirror_gate_
    bucket.json está indexado por 'SEGUIR#activo#marco#grande' (0/1) --
    unimos ambos tamaños de jugada para el mismo activo/marco (mismo
    motivo que DISPERSED_BOT: calcular_stake() no distingue jugada
    grande en el subtype)."""
    if not WALLET_MIRROR_GATE.exists():
        return {}
    gate_data = json.loads(WALLET_MIRROR_GATE.read_text(encoding="utf-8"))
    por_activo_marco = {}
    for clave, tabla in gate_data.items():
        partes = clave.split("#")
        if len(partes) != 4 or partes[0] != "SEGUIR":
            continue
        _, activo, marco, _grande = partes
        act_marco = f"{activo}#{marco}"
        for b_str, info in tabla.items():
            if not isinstance(info, dict):
                continue
            n = info.get("n", 0)
            # Solo buckets que el ejecutor REALMENTE opera hoy -- generar
            # una corrección para un bucket malo_confirmado es inofensivo
            # (permitido_real() ya lo bloquea antes de llegar aquí) pero
            # sucio: no genera ruido de "confirmado" sobre zonas muertas.
            if n < N_MIN_WALLET_MIRROR or info.get("veredicto") != "bueno_confirmado":
                continue
            try:
                b10 = _bucket10(float(b_str))
            except ValueError:
                continue
            actual = por_activo_marco.setdefault(act_marco, {})
            prev = actual.get(f"{b10:.2f}")
            if prev is None or n > prev["n"]:
                ratio = round(1.0 / (1.0 - b10), 4) if b10 < 0.95 else None
                actual[f"{b10:.2f}"] = {
                    "n": n, "ratio_correccion": ratio,
                    "veredicto": "confirmado" if ratio is not None else "sin_concluir",
                    "fuente": f"SEGUIR#{b_str}",
                }
    return por_activo_marco


def main() -> int:
    kelly_gate = {}
    if KELLY_GATE_PATH.exists():
        try:
            kelly_gate = json.loads(KELLY_GATE_PATH.read_text(encoding="utf-8"))
        except Exception:
            kelly_gate = {}
    kelly_gate.setdefault("familias", {})

    dispersed = _dispersed_bot_familia()
    wallet_mirror = _wallet_mirror_familia()
    kelly_gate["familias"]["DISPERSED_BOT"] = dispersed
    kelly_gate["familias"]["WALLET_MIRROR"] = wallet_mirror

    tmp = KELLY_GATE_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(kelly_gate, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    tmp.replace(KELLY_GATE_PATH)

    print("[analisis_kelly_precio_wallet_familias_15sep] DISPERSED_BOT:")
    for act_marco, buckets in dispersed.items():
        for b, info in buckets.items():
            print(f"  {act_marco}[{b}] n={info['n']} ratio={info['ratio_correccion']} veredicto={info['veredicto']} (fuente {info['fuente']})")
    print("[analisis_kelly_precio_wallet_familias_15sep] WALLET_MIRROR:")
    for act_marco, buckets in wallet_mirror.items():
        for b, info in buckets.items():
            print(f"  {act_marco}[{b}] n={info['n']} ratio={info['ratio_correccion']} veredicto={info['veredicto']} (fuente {info['fuente']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
