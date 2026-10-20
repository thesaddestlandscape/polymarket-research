#!/usr/bin/env python3
"""vigia_5m_barato_h55_forward.py -- VIGIA FORWARD CONGELADO de H55 (favorito del 5m anidado). SOLO OBSERVACION/DRY-RUN.
Regla (REGISTRO_HIPOTESIS H55, variante F3, congelada 20-Oct): BTC, 5m anidado, lado s por TWAP60 oficiales (|gap|>=1 bp), 1 entrada
por cierre: primer instante t (RECEPCION; C-300+1,5 s <= t < C-10 s; sin libro cruzado) con 0,50 <= ask5(s) <= 0,95 y
margen = bid15(s) - ask5(s) - 0,07*p*(1-p) >= -0,05; compra virtual al ask real nivel 1 a t+215 ms, limite = ask5(t),
acciones = max(5, 2/ask). La decision vive en m5b_anidado_regla.py (la importa tambien el brazo H55 de F2).
OOS: cierres > 19-Oct 00:00Z. GATE: n>=40 ejecutables, >=10 dias, EV pond >= +0,08, IC90 por cierre >0, sin 2 mejores dias >0.
KILL: EV pond < -0,10 con n>=25, o 2 perdidas totales con ask>=0,90 en una ventana de 10 dias.
El hash del manifiesto cubre ESTE fichero + m5b_anidado_{regla,dia,stats}.py + la config: editar cualquiera rompe la congelacion.
Subcomandos: procesar --dia D [--forzar] | informe.  Salida: DL/vigia_5m_barato_h55/ (informe.json/.txt, manifiesto.json);
entradas diarias gz en DL/vigia_5m_barato_anidado/ (compartidas con el vigia H53/H54). Todo fuera de git.
"""
import argparse, json, sys
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import m5b_anidado_dia as DIA      # noqa: E402
import m5b_anidado_stats as S      # noqa: E402

SAL = S.DL / "vigia_5m_barato_h55"
CONFIG = {"version": 1, "hipotesis": "H55", "regla": "H55", "oos_dia": S.OOS_DIA, "latencia_ms": 215, "stake_eur": 2.0,
          "gate": {"n": 40, "dias": 10, "ev_pond": 0.08, "ic90_cierre_inf": 0, "sin_2_mejores_dias": 0},
          "kill": {"ev_pond_lt": -0.10, "n": 25, "perdidas_ask_ge": 0.90, "perdidas": 2, "ventana_dias": 10},
          "congelado_utc": "2026-10-20T00:00:00+00:00"}
CODIGO = [Path(__file__).resolve()] + [AQUI / n for n in ("m5b_anidado_regla.py", "m5b_anidado_dia.py", "m5b_anidado_stats.py")]


def procesar(dia, forzar):
    S.manifiesto(SAL, "H55", CONFIG, CODIGO, dia)
    DIA.procesar_dia(dia, forzar)


def informe():
    hc = S.manifiesto(SAL, "H55", CONFIG, CODIGO)
    ok, par, dc, dp = S.cargar()
    des = S.desenlace_por_m5(ok + par) if (ok or par) else {}
    ops, cont = S.brazo_tomador(ok, "h55", des)
    res = S.resumen(ops, "H55 tomador +215 ms (dias completos OOS)", S.dias_calendario(dc))
    v = S.veredicto_h55(res)
    cobertura = {"dias_completos": dc, "dias_parciales_no_cuentan": dp, "cierres_con_fila": len(ok),
                 "cierres_esperados": 96 * len(dc), "desenlace_oficial_cobertura": (round(sum(1 for r in ok if r["m5"] in des) / len(ok), 4) if ok else None),
                 "disparos": cont["disparos"], "no_llena": cont["no_llena"], "pendiente_desenlace": cont["pendiente_desenlace"]}
    ref = {"descubrimiento_06_18oct_NO_cuenta_para_el_gate": {"n": 36, "ev_pond": 0.179, "ic90_cierre": (0.005, 0.34), "sin_2_mejores_dias": 0.040,
                                                              "nota": "retencion historica de estimaciones exploratorias al forward: 11 %/28 %/~0 %"}}
    out = {"hipotesis": "H55", "generado_utc": datetime.now(timezone.utc).isoformat(), "hash_congelacion": hc, "config": CONFIG,
           "cobertura": cobertura, "resultado_oos": res, "veredicto": v, "referencia": ref}
    SAL.mkdir(parents=True, exist_ok=True)
    (SAL / "informe.json").write_text(json.dumps(out, indent=1, default=str))
    L = [f"H55 FAV-ANIDADO forward (EXPLORATORY) hash {hc} generado {out['generado_utc'][:19]}Z",
         f"dias completos OOS {dc} | parciales (no cuentan) {dp} | cierres {len(ok)}/{96*len(dc)} | desenlace oficial {cobertura['desenlace_oficial_cobertura']}",
         f"disparos {cont['disparos']}, no llena {cont['no_llena']}, pendientes de desenlace {cont['pendiente_desenlace']}"]
    if res.get("n"):
        L += [f"n={res['n']} dias con op={res['dias_con_operacion']} coste={res['coste_eur']} EUR PnL={res['pnl_eur']:+} EV pond={res['ev_pond_por_eur']:+} "
              f"(media/unidad {res['ev_medio_por_unidad']:+}) acierto {res['acierto']}",
              f"IC90 por cierre {res['ic90_por_cierre']} | IC90 por dias {res['ic90_por_dias']} | sin 2 mejores dias {res['ev_sin_2_mejores_dias']} | dias+ {res['dias_positivos']}/{res['dias_con_operacion']}",
              f"g log f=10 % por operacion {res['g_log_f10']:+} (payout inverso si <0) | perdidas con ask>=0,90: {res['perdidas_con_precio_ge_090']}",
              f"entradas/dia {res.get('entradas_por_dia')} PnL/dia {res.get('pnl_por_dia_calendario_eur')} EUR a 2 EUR de stake"]
    L += [f"VEREDICTO: {v['veredicto']} | kill {v['kill_disparado']} | gate {v['condiciones_gate']}"]
    (SAL / "informe.txt").write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("procesar"); p.add_argument("--dia", required=True); p.add_argument("--forzar", action="store_true")
    sp.add_parser("informe")
    a = ap.parse_args()
    procesar(a.dia, a.forzar) if a.cmd == "procesar" else informe()
