#!/usr/bin/env python3
"""h61b_manifest.py -- run_manifest.json del forward H61b (job id, hashes de codigo/entradas, parametros, fechas previstas/hechas, estado, cobertura por moneda y dia, duplicados).
Uso: h61b_manifest.py inicio|paso|fin|BLOCKED|FAILED [detalle]. Escritura atomica. Estado final COMPLETE solo si no faltan dias previstos y no hay errores/duplicados; si no, PARTIAL."""
import datetime, glob, hashlib, json, os, sys, time
Z = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, Z)
import h61b_regla as RG, h61b_sim as SM, h61b_stats as S
DL = S.DL
COINS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]
f = DL + "run_manifest.json"; os.makedirs(DL, exist_ok=True)
m = json.load(open(f)) if os.path.exists(f) else {}
ev = sys.argv[1]
hoy = datetime.datetime.utcnow().date()
if "job_id" not in m:
    m.update(job_id="h61b_forward_22oct", inicio=time.strftime("%FT%TZ", time.gmtime()), moneda_primaria="BTC", comando="bash %s/run_h61b_diario.sh [D ...]" % Z)
m["congelada_sha"] = RG.verificar_congelada()
m["codigo"] = {n: sha(os.path.join(Z, n)) for n in sorted(os.listdir(Z)) if n.endswith((".py", ".sh"))}
m["parametros"] = dict(W_ms=RG.W_MS, X_bps=RG.X_BPS, repuja_ms=RG.REPUJA_MS, datos_validos_desde=RG.DATOS_VALIDOS_DESDE, gate=RG.GATE, celda_central="cola base, alta 79, cancel 60, tamano real, un relleno cierra")
d0 = datetime.date.fromisoformat(RG.DATOS_VALIDOS_DESDE)
m["fechas_previstas_forward"] = [(d0 + datetime.timedelta(i)).isoformat() for i in range((hoy - d0).days)]   # hasta ayer inclusive
cob, dup = {}, {}
for c in COINS:
    for fc in sorted(glob.glob(DL + f"cobertura_{c}_20*.json")):
        j = json.load(open(fc)); cob.setdefault(c, {})[j["dia"]] = {k: j.get(k) for k in ("cierres_grupo", "con_lado", "con_libro", "cotizados", "sin_desenlace", "errores", "v3_vs_superset_dif", "feeds", "filas", "t_s")}
        dup.setdefault(c, {})[j["dia"]] = 0 if SM.validar_salida(DL + f"rows_{c}_{j['dia']}.csv.gz") else "INVALIDO"
m["cobertura"], m["duplicados_o_invalidos"] = cob, dup
hechos = sorted(cob.get("BTC", {}))
m["btc_dias_hechos"] = hechos
m["btc_dias_forward_pendientes"] = [d for d in m["fechas_previstas_forward"] if d not in hechos]
err = sum(v.get("errores", 0) for c in cob.values() for v in c.values()) + sum(1 for c in dup.values() for v in c.values() if v != 0)
if "pasos" not in m or ev == "inicio": m["pasos"] = m.get("pasos", [])
if len(sys.argv) > 2: m["pasos"].append({"t": time.strftime("%FT%TZ", time.gmtime()), "ev": ev, "detalle": sys.argv[2]}); m["pasos"] = m["pasos"][-60:]
if ev in ("BLOCKED", "FAILED"): m["estado"] = ev
elif ev == "fin": m["estado"] = "COMPLETE" if (not m["btc_dias_forward_pendientes"] and not err) else "PARTIAL"
else: m["estado"] = "RUNNING"
if ev in ("fin", "FAILED", "BLOCKED"): m["fin"] = time.strftime("%FT%TZ", time.gmtime())
m["actualizado"] = time.strftime("%FT%TZ", time.gmtime())
json.dump(m, open(f + ".tmp", "w"), indent=1, default=str); os.replace(f + ".tmp", f)
print("manifest", m["estado"], len(hechos), "dias BTC hechos;", len(m["btc_dias_forward_pendientes"]), "pendientes;", err, "errores/invalidos")
