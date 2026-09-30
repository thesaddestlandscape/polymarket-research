#!/usr/bin/env python3
"""analisis_macro_release_fast.py -- lee una captura de macro_release_fast_fase0.py y responde: ¿a qué ms
tuvimos el dato, a qué ms se repreció cada tramo y qué quedaba comprable cuando nuestra orden habría llegado?
Uso: analisis_macro_release_fast.py <nombre_normalizado> [--llegada_ms 450] [--valor clave=numero ...]
  <nombre_normalizado> = prefijo de los ficheros en /root/polymarket-research-datalogs/macro_fast/
  --llegada_ms: dato recibido -> orden en el libro (parseo + camino de orden ~250 ms + taker delay 150 ms)
  --valor: fuerza el valor (p. ej. core_mom=0.2) si la regex no lo sacó
Las claves de los valores se casan con los tramos por la palabra de la pregunta (core_mom -> "MoM", core_yoy ->
"YoY", paro -> "unemployment"). Solo lectura.
"""
import csv
import json
import re
import sys
from pathlib import Path

DIR = Path("/root/polymarket-research-datalogs/macro_fast")
PALABRA = {"core_mom": "MoM", "core_yoy": "YoY", "paro": "unemployment", "mom": "MoM", "yoy": "YoY"}


def _num(txt):
    if txt is None:
        return None
    if re.search(r"unchanged", str(txt), re.I):
        return 0.0
    m = re.search(r"(-?\d+(?:\.\d+)?)", str(txt))
    if not m:
        return None
    v = float(m.group(1))
    return -v if re.search(r"decreas|fell|declin", str(txt), re.I) else v


def _gana(pregunta: str, v: float):
    m = re.search(r"be (-?\d+(?:\.\d+)?)%( or less| or more)?", pregunta)
    if not m:
        return None
    k, cola = float(m.group(1)), (m.group(2) or "").strip()
    v = round(v, 1)
    return v <= k + 1e-9 if cola == "or less" else v >= k - 1e-9 if cola == "or more" else abs(v - k) < 1e-9


def main() -> int:
    a = sys.argv[1:]
    nombre = a[0]
    llegada = int(a[a.index("--llegada_ms") + 1]) if "--llegada_ms" in a else 450
    forz = dict(x.split("=") for x in a[a.index("--valor") + 1:]) if "--valor" in a else {}
    fuente = [json.loads(l) for l in open(DIR / f"{nombre}_fuente.jsonl", encoding="utf-8")]
    libro = list(csv.DictReader(open(DIR / f"{nombre}_libro.csv", encoding="utf-8")))
    t0_ms = int(libro[0]["t_ms"]) - int(float(libro[0]["rel_s"]) * 1000)
    print("== FUENTE (primer 200 con dato por modo/URL; rel = segundos desde la hora oficial)")
    primeros, valores = {}, {}
    for f in fuente:
        vals = {k: v for k, v in (f.get("valores") or {}).items() if v is not None}
        clave = f"{f.get('modo', '?')} {f['url'][-48:]}"
        if f["estado"] == 200 and (vals or "pdf" in f["url"]) and clave not in primeros:
            primeros[clave] = f
            for k, v in vals.items():
                valores.setdefault(k, v)
    for clave, f in sorted(primeros.items(), key=lambda kv: kv[1]["t_recibido_ms"]):
        print(f"  {f['rel_s']:+8.3f} s (enviada {f.get('rel_envio_s', float('nan')):+.3f}; petición nº {f.get('n_peticiones')})  {clave}  "
              f"{f.get('valores')}  last-modified={((f.get('cab') or {}).get('last-modified'))}")
    cambios = [(f["rel_s"], f.get("modo"), f["estado"]) for f in fuente if f["estado"] != 200][-6:]
    print("  últimos estados no-200:", cambios)
    con_dato = [f for f in primeros.values() if any(v is not None for v in (f.get("valores") or {}).values())]
    if not con_dato and not forz:
        print("sin dato en la ventana: nada que cruzar")
        return 1
    t_dato = min(f["t_recibido_ms"] for f in con_dato) if con_dato else None
    nums = {k: _num(v) for k, v in valores.items()}
    nums.update({k: float(v) for k, v in forz.items()})
    print(f"\n== DATO: {nums}; primer dato en mano a {((t_dato - t0_ms) / 1000 if t_dato else float('nan')):+.3f} s; "
          f"orden en el libro a +{llegada} ms de eso")
    por = {}
    for r in libro:
        por.setdefault(r["pregunta"], []).append(r)
    print(f"\n{'tramo':48s} gana  antes(bid/ask)   1er movimiento  al llegar(bid/ask x tamaño)   +10 s(bid/ask)   margen/acción al llegar")
    total = 0.0
    for q, filas in sorted(por.items()):
        clave = next((k for k in nums if PALABRA.get(k, k).lower() in q.lower()), None)
        g = _gana(q, nums[clave]) if clave and nums[clave] is not None else None

        def _f(x):
            try:
                return float(x)
            except ValueError:
                return None
        antes = [r for r in filas if float(r["rel_s"]) <= -1.0]
        b0, a0 = (_f(antes[-1]["bid"]), _f(antes[-1]["ask"])) if antes else (None, None)
        mov = next((float(r["rel_s"]) for r in filas if float(r["rel_s"]) > -1.0 and (
            (a0 is not None and _f(r["ask"]) is not None and abs(_f(r["ask"]) - a0) >= 0.02) or
            (b0 is not None and _f(r["bid"]) is not None and abs(_f(r["bid"]) - b0) >= 0.02) or
            ((a0 is None) != (_f(r["ask"]) is None)) or ((b0 is None) != (_f(r["bid"]) is None)))), None)
        def _en(t_ms):
            return next((r for r in filas if int(r["t_ms"]) >= t_ms), None)
        ll = _en(t_dato + llegada) if t_dato else None
        d10 = _en(t0_ms + 10000)
        margen = ""
        if ll and g is not None:
            bl, al = _f(ll["bid"]), _f(ll["ask"])
            if g and al is not None and al < 0.97:
                m = 1 - al
                total += m * (_f(ll["ask_size"]) or 0)
                margen = f"compra YES a {al:.3f}: +{m:.3f} x {_f(ll['ask_size']) or 0:.0f} acc"
            elif g is False and bl is not None and bl > 0.03:
                total += bl * (_f(ll["bid_size"]) or 0)
                margen = f"compra NO a {1 - bl:.3f}: +{bl:.3f} x {_f(ll['bid_size']) or 0:.0f} acc"
        fmt = lambda r: f"{r['bid'] or '-':>5s}/{r['ask'] or '-':<5s}" if r else "  -  "
        print(f"{q[:48]:48s} {'SÍ' if g else 'no' if g is False else '? ':4s}  {str(b0 or '-'):>5s}/{str(a0 or '-'):<5s}    "
              f"{(f'{mov:+.2f} s' if mov is not None else 'sin mov.'):>10s}     {fmt(ll)} x{(ll['ask_size'] if ll else ''):>6s}          {fmt(d10)}    {margen}")
    print(f"\nmargen bruto total en el MEJOR nivel de cada tramo al llegar (antes de fee, una sola orden por tramo): {total:.2f} USD")
    return 0


if __name__ == "__main__":
    sys.exit(main())
