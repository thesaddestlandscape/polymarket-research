#!/usr/bin/env python3
"""
edge_quirurgico_rolling.py -- generador RODANTE de zonas de precio finas (0,01-0,05)
con validación FORWARD (21-Sep, aprobado por Javi: "si" a construirlo y dejarlo corriendo
en modo lectura, sin enganchar a evaluar()).

Por qué así (medido el 21-Sep con walk-forward 70/30 sobre WALLET_MIRROR + bot_wallets):
elegir ventanas finas con TODOS los datos y medirlas ahí mismo es sobreajuste -- solo 16 de
43 ventanas elegidas en train fueron positivas en test (37 %), pnl_test medio -0,108 en todos
los anchos, y el p-valor de la búsqueda NO discriminaba (deriva de régimen, no solo sesgo de
selección). Lo que sí funciona es exigir persistencia: una zona solo es OPERABLE si

  (a) se elige con datos ANTERIORES a `cutoff` (= ahora - FORWARD_DIAS) y pasa el rigor de
      analisis_edge_quirurgico_21sep._evaluar_tupla (n>=40, pnl>=0,10, robusta por días
      independientes, top1 wallet <=40 %, media sin la wallet top >0, max-estadístico),
  (b) y en los últimos FORWARD_DIAS (datos que NO participaron en la elección) tiene
      n>=N_FORWARD_MIN y pnl medio >= PISO_EUR.

Cada ejecución (cada ~3 h, vía vigia_edge_quirurgico.py en el carril "quirurgico" de
vigias_frecuentes_fase0.py) reescribe data/shadow/edge_quirurgico_zonas.json y AÑADE una línea
por zona a edge_quirurgico_historial.jsonl, para medir cuántas zonas sobreviven día a día.

MODO LECTURA: nada consume estos ficheros todavía. No toca gates, config ni ejecutores.
Enganchar a evaluar() requiere varios días de historial + /code-review + OK de Javi.
Guardia de frescura prevista para el consumo futuro: `generado_utc` fail-closed a las 4h (cadencia 3h +
duracion ~6 min +margen; el 2h15 de los gates horarios NO sirve aqui: caducaria ~25% del tiempo).

Uso:
  python3 edge_quirurgico_rolling.py            # genera zonas + historial
  python3 edge_quirurgico_rolling.py --resumen  # supervivencia diaria de zonas (historial)
"""
import collections
import json
import os
import pickle
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import analisis_edge_quirurgico_21sep as Q  # noqa: E402  (mismo motor de búsqueda/rigor)

FORWARD_DIAS = 7
N_FORWARD_MIN = 15
PISO_EUR = Q.PISO_EUR
OUT = REPO / "data" / "shadow" / "edge_quirurgico_zonas.json"
HISTORIAL = REPO / "data" / "shadow" / "edge_quirurgico_historial.jsonl"
RECHAZOS = REPO / "data" / "shadow" / "edge_quirurgico_rechazos.json"   # 24-Sep: descartes seguidos por caída de filas
# nombre `_cache_*.pkl` = ya cubierto por .gitignore
CACHE_TRAIN = REPO / "data" / "shadow" / "_cache_edge_quirurgico_train.pkl"
HISTORIAL_DIAS = 60         # rotacion: no crece sin limite
SNAPSHOT_MIN_HORAS = 12     # como mucho ~2 snapshots/dia en el historial
BOOT_ITERS = 1000
# cobertura (21-Sep, Javi: "extenderlo a todo el universo sniper/disperso"): minimo para que pueda existir
# una ventana de >=N_MIN_VENTANA filas distinta del total. Antes 160 dejaba fuera 60min/240min/weekly.
N_MIN_TRAIN = 2 * Q.N_MIN_VENTANA


class DatosTruncados(RuntimeError):
    pass


def _clave(fam, activo, marco, grande, decision=None):
    sufijo = f"#g{grande}" if grande is not None else (f"#{decision}" if decision else "")
    return f"{fam}#{activo}#{marco}{sufijo}"


def _ic90_bootstrap(pnls, seed_key):
    """(lo, hi) del IC90 bootstrap de la media forward. Con n=15-40 y pagos asimetricos es ancho:
    por eso se guarda APARTE del criterio simple (forward_ok) como forward_ok_estricto."""
    import zlib
    a = np.asarray(pnls, dtype=np.float64)
    rng = np.random.default_rng(zlib.crc32(seed_key.encode()))
    m = np.sort(a[rng.integers(0, len(a), size=(BOOT_ITERS, len(a)))].mean(axis=1))
    return float(m[int(0.05 * BOOT_ITERS)]), float(m[int(0.95 * BOOT_ITERS)])


def _escribir_atomico(path: Path, texto: str) -> None:
    tmp = path.with_name(f"{path.name}.{os.getpid()}.tmp")
    tmp.write_text(texto, encoding="utf-8")
    os.replace(tmp, path)


def _cargar_cache_train() -> dict:
    try:
        return pickle.loads(CACHE_TRAIN.read_bytes())
    except Exception:
        return {}


def _guardar_cache_train(cache: dict) -> None:
    try:
        tmp = CACHE_TRAIN.with_name(CACHE_TRAIN.stem + ".tmp.pkl")
        tmp.write_bytes(pickle.dumps(cache, protocol=4))
        os.replace(tmp, CACHE_TRAIN)
    except Exception:
        pass


def _snapshot_debido(prev_ts: str, ahora: datetime) -> bool:
    try:
        prev = datetime.fromisoformat(prev_ts)
        return (ahora - prev).total_seconds() >= SNAPSHOT_MIN_HORAS * 3600 or prev.date() != ahora.date()
    except Exception:
        return True


def _podar_historial(ahora: datetime) -> None:
    if not HISTORIAL.exists():
        return
    limite = (ahora - timedelta(days=HISTORIAL_DIAS)).strftime("%Y-%m-%d")
    mantener = [l for l in HISTORIAL.read_text(encoding="utf-8").splitlines() if l and json.loads(l).get("fecha", "") >= limite]
    _escribir_atomico(HISTORIAL, "\n".join(mantener) + ("\n" if mantener else ""))


WM_RECON = REPO / "data/shadow/wallet_mirror_executor_dryrun_reconstruido_08_22sep.csv"
WM_RECON_HASTA = "2026-09-22"   # el CSV principal cubre desde el 23-Sep (truncado por el OOM del 23-Sep 06:01)


def _filas_wm_unificadas() -> dict:
    """25-Sep (Javi "sí"): WALLET_MIRROR con el CSV principal MÁS el reconstruido 08-22 Sep. El
    principal perdió 15 días en el OOM del 23-Sep; sin esto los forward de 24-25 Sep salían con n=1
    (WM ETH#15min g1 [0,48-0,51) marcada "3 días operable" por datos parciales). Mismo loader
    (Q.W.cargar_filas) sobre ambos ficheros; del reconstruido solo entran filas <= WM_RECON_HASTA
    (evita duplicar el solape) y se deduplica por fila exacta."""
    base = Q.W.cargar_filas()
    if not WM_RECON.exists():
        return base
    orig = Q.W.EXECUTOR
    try:
        Q.W.EXECUTOR = WM_RECON
        rec = Q.W.cargar_filas()
    finally:
        Q.W.EXECUTOR = orig
    for k, v in rec.items():
        dst = base.setdefault(k, [])
        vistos = set(dst)
        for f in v:
            if str(f[0])[:10] <= WM_RECON_HASTA and f not in vistos:
                dst.append(f)
    return base


def generar() -> dict:
    ahora = datetime.now(timezone.utc)
    # cutoff a MEDIANOCHE UTC de hace FORWARD_DIAS dias: el conjunto de entrenamiento solo cambia una
    # vez al dia -> se cachea el resultado (caro) por tupla y las siguientes ejecuciones del dia solo
    # recalculan el lado forward (barato). Ventana forward efectiva: 7-8 dias.
    cutoff = (ahora - timedelta(days=FORWARD_DIAS)).strftime("%Y-%m-%dT00:00:00")
    cache_prev = _cargar_cache_train()
    cache_nuevo = {"cutoff": cutoff, "tuplas": {}}
    reusar = cache_prev.get("cutoff") == cutoff
    est = Q._estado_config()
    fuentes = [(arq, a, m, None, None, filas) for (arq, a, m), filas in Q.B.cargar_filas().items()]
    fuentes += [("WALLET_MIRROR", a, m, g, None, filas) for (_t, a, m, g), filas in _filas_wm_unificadas().items()]
    # 22-Sep (petición explícita Javi: extender a TODAS las estrategias que
    # han estado en live y candidatos_evaluacion_live, no solo P-GALLINA):
    # familia "clásica" vía results.csv, mismo loader TWAP-safe que gate_
    # bucket_propio.py. Sin identidad de wallet (ver Q._evaluar_tupla) --
    # el check de concentración se salta automáticamente para esta familia.
    fuentes += [(s, a, m, None, d, filas) for (s, a, m, d), filas in Q.cargar_filas_clasicas().items()]
    # Guardia de integridad: los resolvers de wallet_mirror/bot_wallets REESCRIBEN los CSV de origen
    # (no atomico) y una lectura a medias da un dataset truncado (visto 21-Sep 16:20: 52 tuplas vs 58
    # en la corrida anterior). Si el total de filas cae >10% frente a la corrida previa se descarta
    # este resultado (no se sobrescribe nada) y el vigia reintenta en 300 s.
    n_filas_total = sum(len(f) for *_r, f in fuentes)
    try:
        prev_total = json.loads(OUT.read_text(encoding="utf-8")).get("n_filas_total")
    except Exception:
        prev_total = None
    if prev_total and n_filas_total < 0.9 * prev_total:
        # 24-Sep: sin salida, esta guarda era un estado absorbente. El truncado REAL de
        # wallet_mirror_executor_dryrun.csv (OOM 23-Sep 06:01, 15 días perdidos para siempre)
        # dejó el total por debajo del 90 % de forma permanente -> 300+ corridas descartadas
        # seguidas y el JSON congelado. Una lectura a medias es puntual; una pérdida permanente
        # se repite con un recuento estable o creciente. Tras 3 descartes seguidos que no
        # bajan (±2 %) se acepta la nueva base (queda en el log).
        try:
            rech = json.loads(RECHAZOS.read_text(encoding="utf-8")).get("totales", [])
        except Exception:
            rech = []
        rech = (rech + [n_filas_total])[-3:]
        estable = len(rech) == 3 and all(b >= a * 0.98 for a, b in zip(rech, rech[1:]))
        if not estable:
            _escribir_atomico(RECHAZOS, json.dumps({"totales": rech, "prev_total": prev_total}))
            raise DatosTruncados(f"filas {n_filas_total} < 90% de la corrida previa ({prev_total}): lectura a medias")
        print(f"AVISO: caída de filas persistente ({prev_total} -> {n_filas_total}, 3 descartes estables {rech}): "
              f"se acepta como nueva base (pérdida permanente de datos de origen, no lectura a medias)")
    try:
        RECHAZOS.unlink()
    except FileNotFoundError:
        pass
    operables, observacion, descartadas = [], [], []
    n_tuplas = 0
    for fam, activo, marco, grande, decision, filas in fuentes:
        train = [f for f in filas if str(f[0])[:19] < cutoff]
        test = [f for f in filas if str(f[0])[:19] >= cutoff]
        if len(train) < N_MIN_TRAIN:
            descartadas.append((_clave(fam, activo, marco, grande, decision), len(train)))
            continue
        n_tuplas += 1
        ck = _clave(fam, activo, marco, grande, decision)
        previo = cache_prev.get("tuplas", {}).get(ck) if reusar else None
        if previo is not None and previo["n_train"] == len(train):
            ventanas = previo["ventanas"]            # mismo train -> mismo resultado (determinista)
        else:
            ventanas = Q._evaluar_tupla(train, f"{ck}#rolling")
        cache_nuevo["tuplas"][ck] = {"n_train": len(train), "ventanas": ventanas}
        for w in ventanas:
            pnls = [f[2] for f in test if w["lo"] <= f[1] < w["hi"]]
            n_te = len(pnls)
            pnl_te = float(np.mean(pnls)) if pnls else None
            z = {"tupla": ck, "familia": fam, "activo": activo,
                 "marco": marco, "grande": grande, "decision": decision,
                 "estado_config": est.get(f"{fam}#{activo}#{marco}", "dormida/sin config"),
                 "ancho": w["ancho"], "lo": w["lo"], "hi": w["hi"],
                 "n_train": w["n"], "pnl_train": w["pnl_medio"], "n_dias_train": w["n_dias"],
                 "pnl_sin_2_mejores_dias": w["pnl_sin_2_mejores_dias"], "wallets": w["wallets"],
                 "top1_wallet": w["top1_wallet"], "p_max_train": w["p_max"],
                 "n_forward": n_te, "pnl_forward": round(pnl_te, 4) if pnl_te is not None else None,
                 "hit_forward": round(float(np.mean([1 if x > 0 else 0 for x in pnls])), 3) if pnls else None}
            z["forward_ok"] = bool(n_te >= N_FORWARD_MIN and pnl_te is not None and pnl_te >= PISO_EUR)
            if n_te >= N_FORWARD_MIN:
                lo_b, hi_b = _ic90_bootstrap(pnls, f"{z['tupla']}#{w['ancho']}#{w['lo']}#fwd")
                z["forward_ic90"] = [round(lo_b, 4), round(hi_b, 4)]
                z["forward_ok_estricto"] = bool(z["forward_ok"] and lo_b > 0)
            else:
                z["forward_ic90"], z["forward_ok_estricto"] = None, False
            # 24-Sep (C5): la familia clásica (results.csv, única con `decision`) se mide al
            # precio_yes_mercado de la señal, que va desfasado: la auditoría con ask real
            # posterior (analisis_auditoria_twap_estrategias_24sep.py, 290.685 señales) da
            # €/tr ≈0 o negativo donde results.csv marca +0,3/+0,7. Sus zonas no son
            # ejecutables -> siempre a observación, marcadas, nunca "operables".
            if decision is not None:
                z["precio_medido"] = "senal_results_csv_desfasado"
                z["forward_ok_precio_senal"], z["forward_ok"] = z["forward_ok"], False
                z["forward_ok_estricto"] = False
            (operables if z["forward_ok"] else observacion).append(z)
    operables.sort(key=lambda z: -(z["pnl_forward"] or 0))
    observacion.sort(key=lambda z: -(z["pnl_forward"] if z["pnl_forward"] is not None else -9))
    res = {"generado_utc": ahora.isoformat(timespec="seconds"), "modo": "lectura (no consumido por evaluar())",
           "forward_dias": FORWARD_DIAS, "cutoff": cutoff, "n_forward_min": N_FORWARD_MIN,
           "piso_eur": PISO_EUR, "n_tuplas_evaluadas": n_tuplas, "n_filas_total": n_filas_total,
           "n_zonas_operables": len(operables), "n_zonas_en_observacion": len(observacion),
           "cobertura": {"total_tuplas_con_datos": len(fuentes), "evaluadas": n_tuplas,
                         "descartadas_n_train_insuficiente": sorted(descartadas, key=lambda t: -t[1])},
           "zonas_operables": operables, "zonas_en_observacion": observacion}
    res["n_zonas_operables_estrictas"] = sum(1 for z in operables if z.get("forward_ok_estricto"))
    prev_ts = ""
    try:
        prev_ts = json.loads(OUT.read_text(encoding="utf-8")).get("ultimo_snapshot_historial", "")
    except Exception:
        pass
    if _snapshot_debido(prev_ts, ahora):
        with open(HISTORIAL, "a", encoding="utf-8") as f:
            for z in operables + observacion:
                f.write(json.dumps({"ts": res["generado_utc"], "fecha": res["generado_utc"][:10], **z},
                                   ensure_ascii=False) + "\n")
        _podar_historial(ahora)
        res["ultimo_snapshot_historial"] = res["generado_utc"]
    else:
        res["ultimo_snapshot_historial"] = prev_ts
    _escribir_atomico(OUT, json.dumps(res, indent=1, ensure_ascii=False))
    _guardar_cache_train(cache_nuevo)
    return res


def resumen() -> None:
    """Supervivencia por día: ¿cuántas zonas distintas eran operables cada día, y cuántas
    repiten día tras día (persistencia)?"""
    if not HISTORIAL.exists():
        print("sin historial todavía"); return
    por_dia = collections.defaultdict(dict)   # fecha -> {clave_zona: forward_ok (último del día)}
    for linea in HISTORIAL.read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(linea)
        except Exception:
            continue
        por_dia[r["fecha"]][(r["tupla"], r["ancho"], r["lo"], r["hi"])] = r["forward_ok"]
    dias = sorted(por_dia)
    print(f"{'fecha':10} {'zonas':>5} {'operables':>9}")
    for d in dias:
        print(f"{d:10} {len(por_dia[d]):>5} {sum(1 for v in por_dia[d].values() if v):>9}")
    todas = {z for d in dias for z in por_dia[d]}
    print(f"\nzonas distintas vistas: {len(todas)} | días de historial: {len(dias)}")
    if len(dias) >= 2:
        print("persistencia (zonas operables en >=2 dias distintos):")
        for z in sorted(todas):
            n_ok = sum(1 for d in dias if por_dia[d].get(z))
            if n_ok >= 2:
                print(f"  {z[0]:34} w={z[1]} [{z[2]:.2f},{z[3]:.2f}) operable {n_ok}/{len(dias)} dias")


if __name__ == "__main__":
    if "--resumen" in sys.argv:
        resumen()
    else:
        try:
            r = generar()
        except DatosTruncados as e:
            print(f"DESCARTADO (no se sobrescribe nada): {e}")
            sys.exit(2)
        print(f"[{r['generado_utc']}] tuplas={r['n_tuplas_evaluadas']} zonas operables={r['n_zonas_operables']} "
              f"(estrictas IC90>0: {r['n_zonas_operables_estrictas']}) en observacion={r['n_zonas_en_observacion']} (forward {FORWARD_DIAS}d, cutoff {r['cutoff']})")
        for z in r["zonas_operables"]:
            print(f"  OPERABLE {z['estado_config']:10} {z['tupla']:32} w={z['ancho']} [{z['lo']:.2f},{z['hi']:.2f}) "
                  f"train n={z['n_train']} {z['pnl_train']:+.3f} -> fwd n={z['n_forward']} {z['pnl_forward']:+.3f}")
