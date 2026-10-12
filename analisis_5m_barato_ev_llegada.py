#!/usr/bin/env python3
"""analisis_5m_barato_ev_llegada.py -- misión «5m barato» (12-Oct), paso 5: EV a la LLEGADA de la orden. SOLO LECTURA.
Para cada evento B1_5m OOS del vigía v4 (todas las señales; desenlace oficial) reconstruye con el archivo ms del volumen
(registro_5m_barato, filas q por RECEPCIÓN) el estado en t0 y en t0+L (L = 215 ms, la del vigía, y 450 ms, la del pipeline
real medido el 12-Oct: decisión→casado ~420-450 ms):
  bid15(s) y ask5(s) en ambos instantes, Δbid15 = bid15(t0+L) - bid15(t0) y margen a la llegada
  bid15(t0+L) - ask5(t0+L) - fee. Pregunta: ¿la información que llega DURANTE la latencia separa las ejecuciones que
  ganan de las que pierden? (si sí, el deterioro es real y el filtro debe usar información ANTERIOR al envío: H3a).
Uso: python3 analisis_5m_barato_ev_llegada.py   (ulimit -v 3000000, fuera de 06-09Z)
"""
import collections
import sys
from datetime import date, datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import vigia_5m_barato_forward as V  # noqa: E402
from analisis_5m_barato_autopsia import _cargar  # noqa: E402
from analisis_5m_barato_maker_sim import _ultimo, cargar_dia  # noqa: E402

LATS = (215, 450)


def main():
    from analisis_maker_cancelacion_binance import desenlaces
    ev = _cargar(True)
    des = desenlaces({e["market_compra"] for e in ev})
    ev = [e for e in ev if e["market_compra"] in des]
    por_dia = collections.defaultdict(list)
    for e in ev:
        por_dia[datetime.fromtimestamp(int(e["t_deteccion"]) / 1000, timezone.utc).date().isoformat()].append(e)
    filas = []
    for dia, lst in sorted(por_dia.items()):
        _t, meta, idx, q, _tr = cargar_dia(dia)
        for e in lst:
            C, coin = int(e["cierre"]), e["moneda"]
            lado = "YES" if e["lado"] == "Up" else "NO"
            toks = idx.get((coin, C), {})
            t15, t5 = toks.get(("15min", lado)), toks.get(("5min", lado))
            if not (t15 and t5):
                continue
            t0 = int(e["t_deteccion"])
            gana = (des[e["market_compra"]] == "YES") == (e["lado"] == "Up")
            f = {"dia": dia, "moneda": coin, "cierre": C, "gana": gana, "clase215": e["L215_clase"][:1],
                 "ejec215": float(e["L215_acciones"] or 0) > 0}
            a0, b0 = _ultimo(q.get(t15), t0), _ultimo(q.get(t5), t0)
            if not (a0 and b0 and a0[1] is not None and b0[2] is not None):
                continue
            f["bid15_0"], f["ask5_0"] = a0[1], b0[2]
            for L in LATS:
                a, b = _ultimo(q.get(t15), t0 + L), _ultimo(q.get(t5), t0 + L)
                if a and b and a[1] is not None and b[2] is not None:
                    f[f"dbid15_{L}"] = round(a[1] - a0[1], 3)
                    f[f"margen_{L}"] = round(a[1] - b[2] - V.fee(b[2]), 3)
                    f[f"dask5_{L}"] = round(b[2] - b0[2], 3)
            filas.append(f)
        del meta, idx, q
        print(f"{dia}: {len(lst)} eventos", file=sys.stderr, flush=True)
    print(f"eventos reconstruidos: {len(filas)} de {len(ev)}\n")
    for L in LATS:
        print(f"== a t0+{L} ms ==")
        for nom, sub in (("ejecutadas a 215 (clase A/D)", [f for f in filas if f["ejec215"]]), ("todas", filas)):
            for g in (True, False):
                v = [f for f in sub if f["gana"] == g and f"dbid15_{L}" in f]
                if not v:
                    continue
                m = lambda k: sum(x[k] for x in v) / len(v)  # noqa: E731
                cae = sum(1 for x in v if x[f"dbid15_{L}"] < 0) / len(v)
                print(f"  {nom:30} {'ganan ' if g else 'pierden'} n={len(v):2d}  Δbid15 medio {m(f'dbid15_{L}'):+.3f} (cae en {cae:.0%})  "
                      f"Δask5 {m(f'dask5_{L}'):+.3f}  margen a la llegada {m(f'margen_{L}'):+.3f}")
        sub = [f for f in filas if f"margen_{L}" in f]
        for umbral in (0.05, 0.0):
            ok = [f for f in sub if f[f"margen_{L}"] >= umbral]
            if ok:
                print(f"  si se exigiera margen >= {umbral:.2f} A LA LLEGADA (no ejecutable sin cancelar en vuelo): n={len(ok)} acierto {sum(f['gana'] for f in ok) / len(ok):.0%}")
    print("\nLectura: si las perdedoras muestran Δbid15 < 0 durante la latencia, el deterioro llega mientras la orden viaja;"
          " un tomador FOK no puede reaccionar -> el filtro tiene que usar información ANTERIOR al envío (H3a, Binance).")


if __name__ == "__main__":
    main()
