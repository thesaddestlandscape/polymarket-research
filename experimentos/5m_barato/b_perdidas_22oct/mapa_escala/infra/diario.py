#!/usr/bin/env python3
"""diario.py - orquestador diario MAPA-ESCALA infra (cron 12:15Z): extraccion on-chain D-1..D-3 (5m,15m guardian + 60m,4h,24h) -> TP1 dia -> resolvedor -> eval/informe.
Contrato: run_manifest.json (job, codigo, parametros, fuentes, dias, estado), checkpoints = ficheros atomicos por dia (extract_D.json, tp1_D.json, celdas_D),
claves de unicidad = (nicho, mid, lc, maker) por dia; reanudacion = recomputar solo lo que no esta COMPLETE. Estados: COMPLETE | PARTIAL | FAILED | BLOCKED."""
import sys, os, json, argparse, datetime as dt
import infra_lib as L, extrae_onchain_ext as E, tp1 as P, n4 as N4
def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--hoy', default=None); ap.add_argument('--sin-espera', action='store_true'); ap.add_argument('--solo-tp1', action='store_true'); a = ap.parse_args()
    hoy = a.hoy or dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d'); L.INFRA.mkdir(parents=True, exist_ok=True)
    man = dict(job=f'mapa_infra_{L.now()}', inicio=L.now(), hoy=hoy, estado='RUNNING', parametros=dict(fwd=[L.FWD0, L.FWD1], maxload=7.0, ventana_prohibida='06:00-09:15Z, 22:15-22:30Z'),
               codigo=L.sha_code([__file__, E.__file__, P.__file__, L.__file__, os.path.join(os.path.dirname(__file__), 'tokmap.py'), N4.__file__]), dias_extraccion={}, dias_tp1={})
    if L.en_ventana_prohibida() and not a.sin_espera:
        man.update(estado='BLOCKED', motivo='ventana horaria prohibida'); L.atomic_json(L.INFRA / 'run_manifest.json', man); L.log('ventana prohibida: no se lanza'); return 0
    if not a.sin_espera and not L.esperar_carga(7.0, 45):
        st = L.read_json(L.INFRA / 'skip_streak.json', {'n': 0}); st['n'] += 1; L.atomic_json(L.INFRA / 'skip_streak.json', st)
        man.update(estado='BLOCKED', motivo=f'load5>7 durante 45 min (racha {st["n"]})'); L.atomic_json(L.INFRA / 'run_manifest.json', man); L.log(man['motivo'])
        if st['n'] >= 2: L.telegram(f"MAPA-ESCALA infra: {st['n']} dias seguidos sin ejecutar por carga (load5>7). El on-chain rota a ~5 d: riesgo de perder dias. Ver {L.INFRA}/run_manifest.json")
        return 0
    L.atomic_json(L.INFRA / 'skip_streak.json', {'n': 0}); rc = 0; alertas = []
    if not a.solo_tp1:
        for k in (3, 2, 1):
            d = (dt.date.fromisoformat(hoy) - dt.timedelta(days=k)).isoformat()
            if not (L.ROOT / f'onchain_fills_{d}.csv.gz').exists(): man['dias_extraccion'][d] = 'BLOCKED(sin onchain_fills)'; continue
            try: m = E.extrae_dia(d, E.MARCOS)
            except Exception as e: m = dict(estado='FAILED', motivo=f'{type(e).__name__}: {e}', marcos={})
            man['dias_extraccion'][d] = m['estado']; L.log(f"extraccion {d}: {m['estado']} " + ' '.join(f"{x}={v['estado']}" for x, v in m.get('marcos', {}).items()))
            if m['estado'] in ('FAILED', 'PARTIAL', 'BLOCKED') and k == 1: alertas.append(f"extraccion {d} {m['estado']}: " + '; '.join(f"{x}:{v.get('motivo', v['estado'])}" for x, v in m.get('marcos', {}).items() if not v['estado'].startswith('COMPLETE')))
            if m['estado'] == 'FAILED': rc = 1
    for d in L.dias(L.FWD0, min(L.FWD1, (dt.date.fromisoformat(hoy) - dt.timedelta(days=1)).isoformat())):
        mf = L.read_json(P.dirs() / f'tp1_{d}.json'); edad = (dt.date.fromisoformat(hoy) - dt.date.fromisoformat(d)).days
        if mf and mf.get('estado') == 'COMPLETE': man['dias_tp1'][d] = 'COMPLETE(previo)'; continue
        if mf and mf.get('estado') in ('PARTIAL', 'BLOCKED') and edad > 4: man['dias_tp1'][d] = mf['estado'] + '(no se reintenta, >4 d)'; continue
        try: m = P.dia(d, forzar=True)
        except Exception as e: m = dict(estado='FAILED', motivo=f'{type(e).__name__}: {e}'); L.log(f'tp1 {d} FAILED {m["motivo"]}'); rc = 1
        man['dias_tp1'][d] = m['estado']
        if m['estado'] != 'COMPLETE' and edad == 1: alertas.append(f"TP1 {d} {m['estado']}: {m.get('motivos') or m.get('motivo')}")
    try: P.resolver([d for d in L.dias(L.FWD0, L.FWD1) if (P.dirs() / f"celdas_{d}.csv.gz").exists()])
    except Exception as e: L.log(f'resolver FAILED {type(e).__name__}: {e}'); rc = 1
    try: ev = P.cmd_eval(telegram=True); man['veredictos'] = {k: v['veredicto'] for k, v in ev.items()}
    except Exception as e: L.log(f'eval FAILED {type(e).__name__}: {e}'); rc = 1
    try: N4.cmd_eval(telegram=True)
    except Exception as e: L.log(f'n4 eval FAILED {type(e).__name__}: {e}'); rc = 1
    if alertas:
        latch = L.read_json(L.INFRA / 'alert_latch.json', {}); clave = '|'.join(alertas)[:300]
        if latch.get('ultima') != clave: L.telegram('MAPA-ESCALA infra: ' + ' || '.join(alertas) + f' (ver {L.INFRA}/run_manifest.json)'); L.atomic_json(L.INFRA / 'alert_latch.json', {'ultima': clave})
    man.update(fin=L.now(), estado='FAILED' if rc else ('PARTIAL' if alertas else 'COMPLETE'), alertas=alertas)
    L.atomic_json(L.INFRA / 'run_manifest.json', man); L.atomic_json(L.INFRA / f'run_manifest_{hoy}.json', man); return rc
if __name__ == '__main__': sys.exit(main())
