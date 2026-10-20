"""Equivalencia H59 vs V4 congelada sobre un DIA REAL (solo lectura; pesado: lanzar de noche, fuera de 06-09Z, MemAvailable > 2,5 GB).
  H59_SALIDA=<dir_scratch> nice -n 19 ionice -c3 python3 -I vigia_5m_barato_h59_forward.py procesar --dia D --forzar     # NO tocar la salida oficial
  python3 -I comparar_con_v4_dia.py D <dir_scratch>
Compara, para cada cierre BTC con 1.ª senal en DL/vigia_5m_barato/eventos_D.csv (V4): mismos cierres, t0, ask0, p_limite, margen y precio de llegada;
imprime las diferencias (esperadas solo en rellenos parciales: V4 admite parciales y niveles 2-3; H59 usa nivel 1 todo-o-nada)."""
import csv, gzip, sys
from pathlib import Path

dia, salida = sys.argv[1], Path(sys.argv[2])
DL = Path("/root/polymarket-research-datalogs")
v4 = {int(r["cierre"]): r for r in csv.DictReader(open(DL / "vigia_5m_barato" / f"eventos_{dia}.csv"))
      if r["regla"] == "B1_5m" and r["es_primero"] == "1" and r["moneda"] == "BTC"}
h = {int(r["cierre"]): r for r in csv.DictReader(gzip.open(salida / f"entradas_{dia}.csv.gz", "rt")) if r["t0"] != ""}
print(f"V4 BTC 1.a senal: {len(v4)} | H59: {len(h)} | solo V4: {sorted(set(v4) - set(h))} | solo H59: {sorted(set(h) - set(v4))}")
bad = 0
for c in sorted(set(v4) & set(h)):
    a, b = v4[c], h[c]
    d = [k for k, x, y in (("t0", a["t_deteccion"], b["t0"]), ("ask0", a["ask_compra_t0"], b["ask0"]), ("plim", a["p_limite"], b["plim"]),
                           ("margen", a["margen_neto"], b["margen"])) if float(x) != float(y)]
    v4_llena, h_llena = float(a["L215_acciones"] or 0) > 0, b["k0.00_clase"] == "llena"
    if v4_llena and h_llena and float(a["L215_precio"]) != float(b["k0.00_precio"]):
        d.append("precio_llegada")
    if v4_llena != h_llena and b["k0.00_clase"] != "corte_tamano":
        d.append(f"relleno_k0 V4={v4_llena} H59={b['k0.00_clase']}")
    bad += bool(d)
    print(c, "OK" if not d else d, "| k0.00:", b["k0.00_clase"], "| k0.02:", b["k0.02_clase"], "| V4 L215:", a["L215_clase"])
print("DIFERENCIAS:", bad)
