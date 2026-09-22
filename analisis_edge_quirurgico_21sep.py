#!/usr/bin/env python3
"""
analisis_edge_quirurgico_21sep.py -- 21-Sep, petición explícita de Javi:
"en todas las estrategias, mirar el punto exacto del edge [...] si el edge solo
vive en el 0,46 pues ejecutar ahí [...] entre el 0,46 y el 0,48 [...] mirar
constantemente dónde vive el edge de cada tupla de forma ultraquirúrgica", y
"esto puede pasar también en estrategias que están dormidas".

SOLO LECTURA. No toca gates, config ni ejecutores. Reusa los loaders de los gates
(misma población fillable/resuelta que los gates reales, verificado: mismo n) para
WALLET_MIRROR y bot_wallets (SNIPER/DISPERSO/WEEKLY_*), incluidas tuplas NO vivas.

Diferencias frente al fino actual (analisis_gate_bucket_fino.evaluar_tupla):
  * anchos 0.01 / 0.02 / 0.03 / 0.05 (el fino solo usa 0.05)
  * mejor ventana POSITIVA (el fino elige la de mayor |diff|, que puede ser una
    ventana perdedora y tapar a una ganadora robusta vecina -- caso real 21-Sep:
    WM SEGUIR#ETH#15min#1 elige [0.42,0.47) no robusta y no [0.46,0.51) robusta)
  * criterio de dias independientes (gate_dias_independientes) y concentración
    de wallet por ventana
  * permutación max-estadístico POR TUPLA Y ANCHO (corrige por haber buscado entre
    todas las ventanas de ese ancho); BH-FDR entre tuplas por activo.
Una ventana "califica" si: n>=40, pnl_medio>=0.10, robusto por dias (sin 2 mejores
dias >=0.10 y >=7 dias), top1 wallet<=40%, media sin la wallet top >0, p_max<0.05.
Salida: data/shadow/edge_quirurgico.json + tabla en stdout.
"""
import collections
import json
import sys
import zlib
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import gate_dias_independientes as G  # noqa: E402
import analisis_bot_wallets_gate_bucket_25ago as B  # noqa: E402
import analisis_wallet_mirror_gate_bucket_10ago as W  # noqa: E402
import analisis_gate_bucket_propio_28jul as C  # noqa: E402 -- familia "clasica" (results.csv)

ANCHOS = (0.01, 0.02, 0.03, 0.05)
PASO = 0.01
N_MIN_VENTANA = 40
N_MIN_TUPLA = 80
PISO_EUR = 0.10
CONC_MAX = 0.40
P_MAX = 0.05
ITERS = 500
TOP_K = 25
OUT = REPO / "data" / "shadow" / "edge_quirurgico.json"

_cargar_filas_clasicas_cache = {"tuplas": None, "filas": None}


def cargar_filas_clasicas() -> dict:
    """22-Sep (petición explícita Javi: extender el método quirúrgico a
    TODAS las estrategias que han estado en live y a candidatos_evaluacion_
    live, no solo la familia P-GALLINA): {(strategy, activo, marco,
    decision): [(ts, py, pnl, None), ...]} desde results.csv, vía el mismo
    loader TWAP-safe que usa gate_bucket_propio.py (cargar_tuplas_live +
    cargar_filas de analisis_gate_bucket_propio_28jul.py -- única fuente de
    verdad para esta familia, no reimplementar el filtrado aparte).

    `wallet` se deja a None a propósito: estas estrategias son modelo-
    dirigidas (GBM_LATE, FAVORITO_CONFIRMADO, BALLENAS_TARDIAS,
    RESOLUTION_SNIPER, CANDIDATA9/10, MOMENTUM_IBS...), no wallet-dirigidas
    -- el check de concentración de wallet de _evaluar_tupla() no aplica
    aquí arquitectónicamente (no hay una "wallet" cuya convicción replicar,
    a diferencia de WALLET_MIRROR/bot_wallets) y se salta automáticamente
    cuando todas las filas de la ventana tienen wallet=None (ver ahí)."""
    if _cargar_filas_clasicas_cache["filas"] is not None:
        return _cargar_filas_clasicas_cache["filas"]
    tuplas = C.cargar_tuplas_live()
    filas_por_tupla = C.cargar_filas(tuplas)
    grupos = {}
    for tupla_str, filas in filas_por_tupla.items():
        partes = tupla_str.split("#")
        if len(partes) != 4:
            continue
        strategy, activo, marco, decision = partes
        clave = (strategy, activo, marco, decision)
        grupos[clave] = [(ts, py, pnl, None) for ts, py, pnl in filas]
    _cargar_filas_clasicas_cache["filas"] = grupos
    return grupos


def _ventanas(py_sorted, n_total, ancho):
    pos, lo = [], 0.0
    while lo <= 1.0 - ancho + 1e-9:
        hi = lo + ancho
        i0 = int(np.searchsorted(py_sorted, lo, side="left"))
        i1 = int(np.searchsorted(py_sorted, hi, side="left"))
        if i1 - i0 >= N_MIN_VENTANA and i1 - i0 < n_total:
            pos.append((round(lo, 2), round(hi, 2), i0, i1))
        lo = round(lo + PASO, 2)
    return pos


def _evaluar_tupla(filas, seed_key):
    """filas: [(ts, ask, pnl, wallet)]. Devuelve lista de ventanas calificadas
    (una por ancho como máximo: la mejor positiva robusta)."""
    n = len(filas)
    if n < N_MIN_TUPLA:
        return []
    orden = sorted(range(n), key=lambda i: filas[i][1])
    ask = np.array([filas[i][1] for i in orden], dtype=np.float64)
    pnl = np.array([filas[i][2] for i in orden], dtype=np.float64)
    ts = [filas[i][0] for i in orden]
    wal = [filas[i][3] for i in orden]
    cs = np.concatenate([[0.0], np.cumsum(pnl)])
    total = float(pnl.sum())
    out = []
    for ancho in ANCHOS:
        pos = _ventanas(ask, n, ancho)
        if not pos:
            continue
        i0 = np.array([p[2] for p in pos]); i1 = np.array([p[3] for p in pos]); nv = i1 - i0
        sv = cs[i1] - cs[i0]
        diff = sv / nv - (total - sv) / (n - nv)          # media ventana - media resto
        # p max-estadístico (solo cola POSITIVA: buscamos zonas buenas)
        rng = np.random.default_rng(zlib.crc32(f"{seed_key}#{ancho}".encode()))
        mejores = np.empty(ITERS)
        for it in range(ITERS):
            c = np.concatenate([[0.0], np.cumsum(rng.permutation(pnl))])
            s = c[i1] - c[i0]
            mejores[it] = (s / nv - (total - s) / (n - nv)).max()
        p_max = float(np.mean(mejores >= diff.max()))
        for j in np.argsort(-diff)[:TOP_K]:
            lo, hi, a, b = pos[j]
            media = float(sv[j] / nv[j])
            if media < PISO_EUR:
                continue
            rob = G.robustez_dias([(ts[k], pnl[k]) for k in range(a, b)])
            if not rob["robusto"]:
                continue
            # 22-Sep: familias sin identidad de wallet (wallet=None en TODAS
            # las filas, ver cargar_filas_clasicas()) no tienen check de
            # concentración que hacer -- no hay wallet cuya convicción
            # replicar, a diferencia de WALLET_MIRROR/bot_wallets. Sin este
            # salto, Counter(wal[a:b]) daría {None: n} -> conc=1.0 y
            # bloquearía TODA ventana de estas familias por construcción.
            sin_wallet = all(w is None for w in wal[a:b])
            if sin_wallet:
                cnt, conc, media_sin_top = {}, None, None
            else:
                cnt = collections.Counter(wal[a:b])
                top_w, top_n = cnt.most_common(1)[0]
                conc = top_n / (b - a)
                resto = [pnl[k] for k in range(a, b) if wal[k] != top_w]
                media_sin_top = float(np.mean(resto)) if resto else float("nan")
                if conc > CONC_MAX or not (media_sin_top > 0):
                    continue
            out.append({"ancho": ancho, "lo": lo, "hi": hi, "n": int(b - a), "pnl_medio": round(media, 4),
                        "diff_vs_resto": round(float(diff[j]), 4), "p_max": round(p_max, 4),
                        "n_dias": rob["n_dias"], "dias_positivos": rob["dias_positivos"],
                        "pnl_sin_2_mejores_dias": rob["pnl_sin_mejores"],
                        "wallets": len(cnt), "top1_wallet": round(conc, 3) if conc is not None else None,
                        "pnl_sin_top_wallet": round(media_sin_top, 4) if media_sin_top is not None else None})
            break   # la mejor (por diff) que pasa todo, una por ancho
    return out


def _estado_config():
    """{clave 'FAMILIA#ACTIVO#MARCO': 'live'|'candidata'|'pausada/dormida'}"""
    try:
        c = json.load(open(REPO / "data/live/config_live.json"))
    except Exception:
        return {}
    est = {}
    for t in c.get("pares_permitidos_live", []):
        p = t.split("#"); est["#".join(p[:3])] = "LIVE"
    for t in c.get("candidatos_evaluacion_live", []):
        p = str(t).split("#"); est.setdefault("#".join(p[:3]), "candidata")
    return est


def main():
    est = _estado_config()
    resultados = []
    grupos_bot = B.cargar_filas()
    for (arq, activo, marco), filas in grupos_bot.items():
        for w in _evaluar_tupla(filas, f"{arq}#{activo}#{marco}"):
            resultados.append({"familia": arq, "activo": activo, "marco": marco, "grande": None,
                               "decision": None, **w})
    grupos_wm = W.cargar_filas()
    for (tipo, activo, marco, grande), filas in grupos_wm.items():
        for w in _evaluar_tupla(filas, f"WM#{tipo}#{activo}#{marco}#{grande}"):
            resultados.append({"familia": "WALLET_MIRROR", "activo": activo, "marco": marco, "grande": grande,
                               "decision": None, **w})
    grupos_clasicas = cargar_filas_clasicas()
    for (strategy, activo, marco, decision), filas in grupos_clasicas.items():
        for w in _evaluar_tupla(filas, f"{strategy}#{activo}#{marco}#{decision}"):
            resultados.append({"familia": strategy, "activo": activo, "marco": marco, "grande": None,
                               "decision": decision, **w})
    for r in resultados:
        r["estado"] = est.get(f"{r['familia']}#{r['activo']}#{r['marco']}", "dormida/sin config")
    # BH-FDR entre resultados por activo (mismo criterio del proyecto)
    por_activo = collections.defaultdict(list)
    for i, r in enumerate(resultados):
        por_activo[r["activo"]].append(i)
    for a, idx in por_activo.items():
        ps = [resultados[i]["p_max"] for i in idx]
        orden = sorted(range(len(ps)), key=lambda k: ps[k]); corte = -1
        for rank, k in enumerate(orden, 1):
            if ps[k] <= rank / len(ps) * P_MAX: corte = rank
        ok = set(orden[:corte]) if corte > 0 else set()
        for k, i in enumerate(idx):
            resultados[i]["bh_ok"] = k in ok
    resultados.sort(key=lambda r: (not r["bh_ok"], -r["pnl_sin_2_mejores_dias"]))
    OUT.write_text(json.dumps(resultados, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"tuplas con >=1 ventana calificada: {len({(r['familia'],r['activo'],r['marco'],r['grande'],r['decision']) for r in resultados})} | ventanas: {len(resultados)} | pasan BH-FDR: {sum(r['bh_ok'] for r in resultados)}")
    print(f"{'BH':2} {'estado':10} {'tupla':40} {'anch':5} {'ventana':12} {'n':>4} {'pnl':>6} {'dias':>4} {'sin2':>6} {'wal':>3} {'top1':>5} {'p':>6}")
    for r in resultados:
        sufijo = f"#g{r['grande']}" if r['grande'] is not None else (f"#{r['decision']}" if r['decision'] else "")
        tup = f"{r['familia']}#{r['activo']}#{r['marco']}{sufijo}"
        top1_str = f"{r['top1_wallet']:>5.2f}" if r['top1_wallet'] is not None else "  n/a"
        print(f"{'OK' if r['bh_ok'] else '--':2} {r['estado']:10} {tup:40} {r['ancho']:<5} [{r['lo']:.2f},{r['hi']:.2f}) {r['n']:>4} {r['pnl_medio']:+.3f} {r['n_dias']:>4} {r['pnl_sin_2_mejores_dias']:+.3f} {r['wallets']:>3} {top1_str} {r['p_max']:>6.3f}")


def forward():
    """Validacion OUT-OF-SAMPLE (walk-forward): por tupla, las ventanas se ELIGEN con el
    70% cronologico mas antiguo y se MIDEN en el 30% mas reciente. Es la unica prueba
    que separa un edge fino real de sobreajuste (con ancho 0.01 el sesgo de seleccion
    es maximo). Salida: data/shadow/edge_quirurgico_forward.json."""
    est = _estado_config()
    filas_out = []
    fuentes = []
    for (arq, activo, marco), filas in B.cargar_filas().items():
        fuentes.append((arq, activo, marco, None, None, filas))
    for (tipo, activo, marco, grande), filas in W.cargar_filas().items():
        fuentes.append(("WALLET_MIRROR", activo, marco, grande, None, filas))
    for (strategy, activo, marco, decision), filas in cargar_filas_clasicas().items():
        fuentes.append((strategy, activo, marco, None, decision, filas))
    for fam, activo, marco, grande, decision, filas in fuentes:
        if len(filas) < N_MIN_TUPLA * 2:
            continue
        tss = sorted(str(f[0]) for f in filas)
        corte = tss[int(len(tss) * 0.70)]
        train = [f for f in filas if str(f[0]) < corte]
        test = [f for f in filas if str(f[0]) >= corte]
        for w in _evaluar_tupla(train, f"{fam}#{activo}#{marco}#{grande}#{decision}#fwd"):
            sel = [f[2] for f in test if w["lo"] <= f[1] < w["hi"]]
            filas_out.append({"familia": fam, "activo": activo, "marco": marco, "grande": grande,
                              "decision": decision,
                              "estado": est.get(f"{fam}#{activo}#{marco}", "dormida/sin config"),
                              "ancho": w["ancho"], "lo": w["lo"], "hi": w["hi"], "corte": corte[:10],
                              "n_train": w["n"], "pnl_train": w["pnl_medio"], "p_max_train": w["p_max"],
                              "n_test": len(sel), "pnl_test": round(float(np.mean(sel)), 4) if sel else None,
                              "hit_test": round(float(np.mean([1 if x > 0 else 0 for x in sel])), 3) if sel else None})
    (REPO / "data" / "shadow" / "edge_quirurgico_forward.json").write_text(
        json.dumps(filas_out, indent=1, ensure_ascii=False), encoding="utf-8")
    con = [r for r in filas_out if r["n_test"] >= 10]
    print(f"ventanas elegidas en train: {len(filas_out)} | con n_test>=10: {len(con)} | "
          f"pnl_test>0: {sum(1 for r in con if r['pnl_test'] > 0)} | pnl_test>=0.10: {sum(1 for r in con if r['pnl_test'] >= 0.10)}")
    for a in ANCHOS:
        c = [r for r in con if r["ancho"] == a]
        if c:
            print(f"  ancho {a}: n={len(c)} pnl_test medio={np.mean([r['pnl_test'] for r in c]):+.3f} "
                  f"positivas={sum(1 for r in c if r['pnl_test'] > 0)}/{len(c)}")
    print(f"{'estado':10} {'tupla':40} {'anch':5} {'ventana':12} {'n_tr':>4} {'pnl_tr':>7} {'n_te':>4} {'pnl_te':>7} {'hit_te':>6}")
    for r in sorted(filas_out, key=lambda r: (-(r["pnl_test"] if r["pnl_test"] is not None else -9))):
        sufijo = f"#g{r['grande']}" if r['grande'] is not None else (f"#{r['decision']}" if r['decision'] else "")
        tup = f"{r['familia']}#{r['activo']}#{r['marco']}{sufijo}"
        pt = f"{r['pnl_test']:+.3f}" if r["pnl_test"] is not None else "  -  "
        print(f"{r['estado']:10} {tup:40} {r['ancho']:<5} [{r['lo']:.2f},{r['hi']:.2f}) {r['n_train']:>4} {r['pnl_train']:+.3f} {r['n_test']:>4} {pt:>7} {r['hit_test'] if r['hit_test'] is not None else '-':>6}")


if __name__ == "__main__":
    forward() if "--forward" in sys.argv else main()
