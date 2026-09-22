#!/usr/bin/env python3
"""
sports_edge_quirurgico_rolling.py -- generador RODANTE de zonas de precio
finas para sports (22-Sep), mismo motor y mismo criterio de rigor que
edge_quirurgico_rolling.py (cripto, 21-Sep) -- ver ese fichero para el
razonamiento completo (walk-forward 70/30 demostró que elegir con TODOS
los datos y medir ahí mismo es sobreajuste). Reusa analisis_sports_edge_
quirurgico_22sep.py::cargar_filas()/_evaluar_tupla (importado de
analisis_edge_quirurgico_21sep.py) -- no reimplementar el motor.

Una zona sports es OPERABLE solo si:
  (a) se elige con datos ANTERIORES a `cutoff` (=ahora-FORWARD_DIAS) y
      pasa el rigor completo (multi-ancho, max-estadístico, robustez por
      días, concentración de wallet <=40%),
  (b) y en los últimos FORWARD_DIAS (fuera de la selección) tiene
      n>=N_FORWARD_MIN y pnl medio >= PISO_EUR.

MODO LECTURA: nada consume estos ficheros todavía. No toca gates, config
ni ejecutores -- enganchar a sports_wallet_mirror_gate_bucket.py::
evaluar() (si se decide) requiere varios días de historial + /code-review
+ OK de Javi, mismo protocolo que en cripto.

Uso:
  python3 sports_edge_quirurgico_rolling.py            # genera zonas + historial
  python3 sports_edge_quirurgico_rolling.py --resumen  # supervivencia diaria
"""
import collections
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import analisis_sports_edge_quirurgico_22sep as S  # noqa: E402
from analisis_edge_quirurgico_21sep import _evaluar_tupla, N_MIN_VENTANA  # noqa: E402

FORWARD_DIAS = 7
N_FORWARD_MIN = 15
PISO_EUR = S.PISO_EUR
OUT = REPO / "data" / "sports" / "edge_quirurgico_sports_zonas.json"
HISTORIAL = REPO / "data" / "sports" / "edge_quirurgico_sports_historial.jsonl"
HISTORIAL_DIAS = 60
SNAPSHOT_MIN_HORAS = 12
BOOT_ITERS = 1000
N_MIN_TRAIN = 2 * N_MIN_VENTANA


class DatosTruncados(RuntimeError):
    pass


def _clave(categoria, tipo):
    return f"{categoria}#{tipo}"


def _ic90_bootstrap(pnls, seed_key):
    import zlib
    a = np.asarray(pnls, dtype=np.float64)
    rng = np.random.default_rng(zlib.crc32(seed_key.encode()))
    m = np.sort(a[rng.integers(0, len(a), size=(BOOT_ITERS, len(a)))].mean(axis=1))
    return float(m[int(0.05 * BOOT_ITERS)]), float(m[int(0.95 * BOOT_ITERS)])


def _escribir_atomico(path: Path, texto: str) -> None:
    tmp = path.with_name(f"{path.name}.{os.getpid()}.tmp")
    tmp.write_text(texto, encoding="utf-8")
    os.replace(tmp, path)


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
    mantener = [l for l in HISTORIAL.read_text(encoding="utf-8").splitlines()
               if l and json.loads(l).get("fecha", "") >= limite]
    _escribir_atomico(HISTORIAL, "\n".join(mantener) + ("\n" if mantener else ""))


def generar() -> dict:
    ahora = datetime.now(timezone.utc)
    cutoff = (ahora - timedelta(days=FORWARD_DIAS)).strftime("%Y-%m-%dT00:00:00")
    est = S._estado_config()
    grupos = S.cargar_filas()
    n_filas_total = sum(len(f) for f in grupos.values())
    try:
        prev_total = json.loads(OUT.read_text(encoding="utf-8")).get("n_filas_total")
    except Exception:
        prev_total = None
    if prev_total and n_filas_total < 0.9 * prev_total:
        raise DatosTruncados(f"filas {n_filas_total} < 90% de la corrida previa ({prev_total}): lectura a medias")

    operables, observacion, descartadas = [], [], []
    n_tuplas = 0
    for (categoria, tipo), filas in grupos.items():
        train = [f for f in filas if str(f[0])[:19] < cutoff]
        test = [f for f in filas if str(f[0])[:19] >= cutoff]
        ck = _clave(categoria, tipo)
        if len(train) < N_MIN_TRAIN:
            descartadas.append((ck, len(train)))
            continue
        n_tuplas += 1
        ventanas = _evaluar_tupla(train, f"{ck}#rolling")
        for w in ventanas:
            pnls = [f[2] for f in test if w["lo"] <= f[1] < w["hi"]]
            n_te = len(pnls)
            pnl_te = float(np.mean(pnls)) if pnls else None
            z = {"tupla": ck, "categoria": categoria, "tipo": tipo,
                 "estado_config": est.get(ck, "candidata/dormida"),
                 "ancho": w["ancho"], "lo": w["lo"], "hi": w["hi"],
                 "n_train": w["n"], "pnl_train": w["pnl_medio"], "n_dias_train": w["n_dias"],
                 "pnl_sin_2_mejores_dias": w["pnl_sin_2_mejores_dias"], "wallets": w["wallets"],
                 "top1_wallet": w["top1_wallet"], "p_max_train": w["p_max"],
                 "n_forward": n_te, "pnl_forward": round(pnl_te, 4) if pnl_te is not None else None,
                 "hit_forward": round(float(np.mean([1 if x > 0 else 0 for x in pnls])), 3) if pnls else None}
            z["forward_ok"] = bool(n_te >= N_FORWARD_MIN and pnl_te is not None and pnl_te >= PISO_EUR)
            if n_te >= N_FORWARD_MIN:
                lo_b, hi_b = _ic90_bootstrap(pnls, f"{ck}#{w['ancho']}#{w['lo']}#fwd")
                z["forward_ic90"] = [round(lo_b, 4), round(hi_b, 4)]
                z["forward_ok_estricto"] = bool(z["forward_ok"] and lo_b > 0)
            else:
                z["forward_ic90"], z["forward_ok_estricto"] = None, False
            (operables if z["forward_ok"] else observacion).append(z)
    operables.sort(key=lambda z: -(z["pnl_forward"] or 0))
    observacion.sort(key=lambda z: -(z["pnl_forward"] if z["pnl_forward"] is not None else -9))
    res = {"generado_utc": ahora.isoformat(timespec="seconds"), "modo": "lectura (no consumido por evaluar())",
           "forward_dias": FORWARD_DIAS, "cutoff": cutoff, "n_forward_min": N_FORWARD_MIN,
           "piso_eur": PISO_EUR, "n_tuplas_evaluadas": n_tuplas, "n_filas_total": n_filas_total,
           "n_zonas_operables": len(operables), "n_zonas_en_observacion": len(observacion),
           "cobertura": {"total_combos_con_datos": len(grupos), "evaluadas": n_tuplas,
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
    return res


def resumen() -> None:
    if not HISTORIAL.exists():
        print("sin historial todavía"); return
    por_dia = collections.defaultdict(dict)
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
                print(f"  {z[0]:24} w={z[1]} [{z[2]:.2f},{z[3]:.2f}) operable {n_ok}/{len(dias)} dias")


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
              f"(estrictas IC90>0: {r['n_zonas_operables_estrictas']}) en observacion={r['n_zonas_en_observacion']} "
              f"(forward {FORWARD_DIAS}d, cutoff {r['cutoff']})")
        for z in r["zonas_operables"]:
            print(f"  OPERABLE {z['estado_config']:16} {z['tupla']:24} w={z['ancho']} [{z['lo']:.2f},{z['hi']:.2f}) "
                  f"train n={z['n_train']} {z['pnl_train']:+.3f} -> fwd n={z['n_forward']} {z['pnl_forward']:+.3f}")
