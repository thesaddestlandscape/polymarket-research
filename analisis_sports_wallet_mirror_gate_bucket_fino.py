#!/usr/bin/env python3
"""
analisis_sports_wallet_mirror_gate_bucket_fino.py — 26-Ago, ventana
deslizante (mismo mecanismo que analisis_gate_bucket_fino.py de cripto,
20-Ago, y su gemelo analisis_wallet_mirror_gate_bucket_fino_25ago.py)
aplicada a Sports Wallet Mirror.

Origen: petición explícita Javi ("sports tiene que tener todo lo que
tiene cripto y weather para que funcione") — el gate de grid fijo
(analisis_sports_wallet_mirror_gate_bucket_26ago.py, bucket 0.05 anclado
a múltiplos de 0.05) ya rescató 1 bucket (CS#SEGUIR[0.25,0.30) tras
corregir el fee) pero puede estar diluyendo edges más estrechos que no
caen justo en el grid, exactamente el mismo patrón que rescató
BALLENAS_TARDIAS#ETH#5min en cripto el 20-Ago.

Reusa el motor genérico de análisis_gate_bucket_fino.py sin reimplementar
nada (evaluar_tupla: max-statistic + LOO + bootstrap CI90%, bh_fdr_signif:
BH-FDR por familia). Única adaptación: en sports "familia" es la
categoría (CS/LoL/Tennis/...), no hay concepto de "activo" — se agrupa
BH-FDR por (categoria, tipo) en vez de (familia, activo) de cripto,
mismo tamaño de grupo típico (1 combo = su propia familia, sin mezclar
categorías entre sí, igual de estricto).

FEE=0.05 (verificado 26-Ago contra gamma-api, ver
analisis_sports_wallet_mirror_gate_bucket_26ago.py), no el 0.07 de
cripto.

Solo lectura -- sports no tiene infraestructura de dinero real, esto NO
conecta a ningún ejecutor. Salida: data/sports/wallet_mirror_gate_bucket_fino.json
"""
import csv
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

from analisis_gate_bucket_fino import evaluar_tupla, bh_fdr_signif, P_MAX

F_KELLY = 0.10  # 29-Ago: mismo default que analisis_log_growth.py/gate_bucket_propio.py (P28/CLAUDE.md pt.14)

csv.field_size_limit(sys.maxsize)

REPO = Path(__file__).resolve().parent
DRY_RUN = REPO / "data/sports/wallet_mirror_sniper_dry_run.csv"
OUT = REPO / "data/sports/wallet_mirror_gate_bucket_fino.json"

RATIO_MIN = 5.0
FEE = 0.05
STAKE = 1.0


def payout_win(ask: float) -> float:
    return STAKE * (1 - ask) / ask - STAKE * FEE * (1 - ask)


def cargar_filas() -> dict:
    grupos = defaultdict(list)
    with open(DRY_RUN, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") not in ("0", "1"):
                continue
            try:
                ratio = float(row["ratio_vs_stake_mirror"])
                ask = float(row["mejor_ask_mirror"])
            except (TypeError, ValueError, KeyError):
                continue
            if ratio < RATIO_MIN or not (0.01 < ask < 0.99):
                continue
            acierto = int(row["acierto"])
            pnl = payout_win(ask) if acierto == 1 else -STAKE
            ts = row.get("resolved_ts") or row.get("timestamp_utc", "")
            key = (row["categoria"], row["tipo"])
            grupos[key].append((ts, ask, pnl))
    return grupos


def main() -> int:
    grupos = cargar_filas()
    print(f"Combos (categoria,tipo): {len(grupos)}")

    pendientes = []
    for (categoria, tipo), filas in grupos.items():
        tupla_str = f"{categoria}#{tipo}"
        info = evaluar_tupla(filas)
        if not info:
            continue
        if info["split_half_ok"] and info["robusto_loo"] and info["robusto_bootstrap"]:
            pendientes.append({"tupla_str": tupla_str, "info": info,
                                "p": info["p_valor"], "diff": info["diff_vs_resto"]})

    print(f"Ventanas candidatas (n>=40 tupla, rigor individual OK): {len(pendientes)}")

    # BH-FDR por categoria (mismo nivel de agrupación que "familia" en cripto)
    por_categoria = defaultdict(list)
    for idx, p in enumerate(pendientes):
        cat = p["tupla_str"].split("#")[0]
        por_categoria[cat].append(idx)

    sobreviven = set()
    for cat, indices in por_categoria.items():
        p_valores = [pendientes[i]["p"] for i in indices]
        sobreviven_grupo = bh_fdr_signif(p_valores, q=P_MAX)
        sobreviven |= {indices[j] for j in sobreviven_grupo}

    print(f"Sobreviven BH-FDR: {len(sobreviven)}")

    salida = {}
    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            continue
        info = p["info"]
        if p["diff"] < 0:
            veredicto = "malo_confirmado"
        elif info["pnl_medio"] >= 0:
            veredicto = "bueno_confirmado"
        else:
            continue
        # 29-Ago (paridad con el mismo hueco cerrado en el grid fijo,
        # analisis_sports_wallet_mirror_gate_bucket_26ago.py, y en
        # WALLET_MIRROR cripto): veto de payout asimétrico (Kelly g(f)) --
        # calculado localmente sobre las filas propias que caen dentro de
        # la ventana [lo,hi) confirmada, sin tocar el motor genérico
        # compartido analisis_gate_bucket_fino.py (ese motor también
        # alimenta gate_bucket_fino.json de cripto, que SÍ vetea dinero
        # real hoy -- cambiar su firma exige su propio /code-review por
        # separado, fuera del alcance de esta paridad sports). Solo puede
        # degradar bueno_confirmado, nunca promover.
        categoria, tipo = p["tupla_str"].split("#")
        filas_tupla = grupos.get((categoria, tipo), [])
        pnls_ventana = [pnl for _, ask, pnl in filas_tupla if info["lo"] <= ask < info["hi"]]
        g_kelly = (sum(math.log(1 + F_KELLY * x) for x in pnls_ventana) / len(pnls_ventana)
                   if pnls_ventana else None)
        info["g_kelly_f10"] = round(g_kelly, 5) if g_kelly is not None else None
        if veredicto == "bueno_confirmado" and g_kelly is not None and g_kelly <= 0:
            veredicto = "malo_confirmado"
        info["veredicto"] = veredicto
        salida[p["tupla_str"]] = info
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        print(f"  {marca} {p['tupla_str']} [{info['lo']:.2f},{info['hi']:.2f}) "
              f"n={info['n']} pnl_medio={info['pnl_medio']:+.3f} p={info['p_valor']:.4f} {veredicto}")

    OUT.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Guardado en {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
