#!/usr/bin/env python3
"""vigia_5m_barato_h53_forward.py -- VIGIA FORWARD CONGELADO de H53 (V4b, umbral de margen 0,02) y comparacion emparejada H54
(maker H23 / tomador H53 / combinacion una-via, SIN sumar PnL). SOLO OBSERVACION/DRY-RUN.
H53: igual que V4 (BTC, 5m anidado, lado s por TWAP60, 1 entrada por cierre, +215 ms, nivel 1, limite = ask5(t), acciones = max(5, 2/ask))
pero con margen >= 0,02 (no 0,05). H54: maker H23 (join en el bid 5m-s, margen >= -0,05, cancelacion 60 ms, rebate 20 %, relleno solo
por operaciones tomadoras que atraviesan la cola) primero; el tomador H53 solo si el maker no se ha rellenado <= t_disparo + 60 ms.
OOS: cierres > 19-Oct 00:00Z. H53 GATE: n>=40, >=10 dias, EV pond >= +0,10, IC90 por cierre >0, sin 2 mejores dias >0 y diferencia
emparejada frente a V4 (misma maquinaria, margen 0,05, mismos cierres) con IC90 por cierre >0. H53 KILL: EV pond < -0,15 con n>=25, o
IC90 superior < 0 con n>=20. H54: comparacion emparejada de los tres brazos; el mejor por EV pond solo se promueve si cumple el gate de SU brazo.
Subcomandos: procesar --dia D [--forzar] | informe.  Salida: DL/vigia_5m_barato_h53/.
"""
import argparse, json, sys
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import m5b_anidado_dia as DIA      # noqa: E402
import m5b_anidado_stats as S      # noqa: E402

SAL = S.DL / "vigia_5m_barato_h53"
CONFIG = {"version": 1, "hipotesis": "H53+H54", "regla": "H53", "oos_dia": S.OOS_DIA, "latencia_ms": 215, "stake_eur": 2.0,
          "gate": {"n": 40, "dias": 10, "ev_pond": 0.10, "ic90_cierre_inf": 0, "sin_2_mejores_dias": 0, "dif_vs_v4_ic90_inf": 0},
          "kill": {"ev_pond_lt": -0.15, "n": 25, "ic90_sup_lt0_n": 20}, "congelado_utc": "2026-10-20T00:00:00+00:00"}
CODIGO = [Path(__file__).resolve()] + [AQUI / n for n in ("m5b_anidado_regla.py", "m5b_anidado_dia.py", "m5b_anidado_stats.py")]


def procesar(dia, forzar):
    S.manifiesto(SAL, "H53", CONFIG, CODIGO, dia)
    DIA.procesar_dia(dia, forzar)


def informe():
    hc = S.manifiesto(SAL, "H53", CONFIG, CODIGO)
    ok, par, dc, dp = S.cargar()
    des = S.desenlace_por_m5(ok + par) if (ok or par) else {}
    nd = S.dias_calendario(dc)
    o53, c53 = S.brazo_tomador(ok, "h53", des)
    o4, c4 = S.brazo_tomador(ok, "v4", des)
    om, cm = S.brazo_maker(ok, des)
    oc, cc = S.brazo_combinado(ok, des)
    r53, r4, rm, rc = (S.resumen(o53, "H53 tomador", nd), S.resumen(o4, "V4 replica nivel 1 (mismo motor)", nd),
                       S.resumen(om, "H23 maker (con rebate 20 %)", nd), S.resumen(oc, "H54 combinado una-via", nd))
    dif_v4 = S.dif_emparejada(o53, o4, "H53 - V4")
    v = S.veredicto_h53(r53, dif_v4)
    emp = [S.dif_emparejada(oc, om, "H54 combinado - maker"), S.dif_emparejada(oc, o53, "H54 combinado - tomador H53"),
           S.dif_emparejada(om, o53, "maker - tomador H53"), dif_v4]
    gate_brazo = {"H53": v["veredicto"], "H23_maker": "su gate es el de H23/H47 (no definido aqui)", "H54": "PENDIENTE: usa el mismo kill que H53"}
    out = {"hipotesis": "H53+H54", "generado_utc": datetime.now(timezone.utc).isoformat(), "hash_congelacion": hc, "config": CONFIG,
           "cobertura": {"dias_completos": dc, "dias_parciales_no_cuentan": dp, "cierres_con_fila": len(ok), "cierres_esperados": 96 * nd,
                         "desenlace_oficial_cobertura": (round(sum(1 for r in ok if r["m5"] in des) / len(ok), 4) if ok else None),
                         "contadores": {"h53": c53, "v4": c4, "maker": cm, "combinado_vias": cc}},
           "brazos": [r53, r4, rm, rc], "emparejadas_mismos_cierres": emp, "veredicto_h53": v, "veredicto_por_brazo": gate_brazo,
           "referencia_descubrimiento_NO_cuenta": {"H53": {"n": 24, "ev_pond": 0.507, "sin_2": 0.110}, "maker": {"n": 17, "ev_pond": 0.795},
                                                  "combinado": {"n": 25, "ev_pond": 0.457, "vias": "maker 5 / tomador 20"}}}
    SAL.mkdir(parents=True, exist_ok=True)
    (SAL / "informe.json").write_text(json.dumps(out, indent=1, default=str))
    L = [f"H53 (V4b 0,02) + H54 forward (EXPLORATORY) hash {hc} {out['generado_utc'][:19]}Z",
         f"dias completos OOS {dc} | parciales {dp} | cierres {len(ok)}/{96*nd} | desenlace oficial {out['cobertura']['desenlace_oficial_cobertura']}"]
    for r in (r53, r4, rm, rc):
        if r.get("n"):
            L.append(f"{r['brazo']}: n={r['n']} dias={r['dias_con_operacion']} coste={r['coste_eur']} PnL={r['pnl_eur']:+} EV pond={r['ev_pond_por_eur']:+} "
                     f"IC90 cierre {r['ic90_por_cierre']} dias {r['ic90_por_dias']} sin2 {r['ev_sin_2_mejores_dias']}")
        else:
            L.append(f"{r['brazo']}: n=0")
    L += ["Emparejadas (mismos cierres, union): " + " | ".join(f"{e['comparacion']} dif={e['dif']} IC90={e.get('ic90_por_cierre')} n={e['n_cierres']}" for e in emp),
          f"contadores {out['cobertura']['contadores']}", f"VEREDICTO H53: {v['veredicto']} | kill {v['kill_disparado']} | gate {v['condiciones_gate']}"]
    (SAL / "informe.txt").write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("procesar"); p.add_argument("--dia", required=True); p.add_argument("--forzar", action="store_true")
    sp.add_parser("informe")
    a = ap.parse_args()
    procesar(a.dia, a.forzar) if a.cmd == "procesar" else informe()
