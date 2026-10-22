#!/usr/bin/env python3
"""h23_huecos_ws.py -- LIBRO DE HUECOS del registro maker_ms (fuente del replay H23) a partir del log de observadores (22-Oct-2026). SOLO LECTURA de logs/observadores_fase0.log y de los
mtime de los ficheros maker_ms_*.csv.gz; escribe SOLO su propio ledger JSON atomico en /root/polymarket-research-datalogs/h23_cobertura/.

Por que: el registro maker_ms NO marca las caidas del WS (1013 slow consumer, ~45-75 por dia en BTC#5min) ni los reinicios del hijo lector (~7/dia, 1,5-4,5 min sin NADA), y al reconectar el
snapshot `book` no escribe fila q: el replay (h23_sim_v3.py) las ve como libro quieto/obsoleto. Medido 19-21 Oct: ~16 % de los cierres BTC tienen un hueco de caida dentro de la ventana de
cotizacion [C-305 s, C-10 s] y ademas ~5 % caen en un reinicio. Este modulo reconstruye esos huecos para marcar cada cierre (limpio / con hueco) y acotar el sesgo; NO repara datos.
Tipos de hueco: `caida` (log `sesion caida [G]` -> siguiente `conectado [G]`, relleno +-1 s por resolucion de 1 s del log) y `reinicio` (hijo lector nuevo: desde el mtime del ultimo
fichero del pid anterior hasta el primer `conectado [G]` del pid nuevo, +5 s hasta que llegue el primer q real).
Uso: python3 -I h23_huecos_ws.py --guardar            # reconstruye y guarda el ledger completo (idempotente: sustituye por clave)
     python3 -I h23_huecos_ws.py --clasifica COIN D   # tabla de cierres del dia D con su estado
"""
import argparse
import glob
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone

LOG = "/root/polymarket-research/logs/observadores_fase0.log"
DL = "/root/polymarket-research-datalogs"
SALIDA = DL + "/h23_cobertura"
RX = re.compile(r"^\[(\S+)\] \[libro_estado_ws\] (sesión caída|conectado) \[([A-Z]+#[0-9a-z]+|extra)\](.*)")
PAD_CAIDA_S, PAD_REINICIO_S = 1.0, 5.0
VENTANA = (305.0, 10.0)     # [C-305 s, C-10 s]


def _t(iso):
    return datetime.fromisoformat(iso).timestamp()


def parsear(log=LOG):
    ev = defaultdict(list)       # grupo -> [(t, tipo, pid)]
    with open(log, errors="replace") as f:
        for ln in f:
            m = RX.match(ln)
            if not m:
                continue
            pid = re.search(r"pid (\d+)", m.group(4))
            ev[m.group(3)].append((_t(m.group(1)), "caida" if m.group(2).startswith("sesi") else "con", pid.group(1) if pid else None))
    for g in ev:
        ev[g].sort()
    return ev


def mtimes_por_pid(dl=DL):
    out = {}
    for f in glob.glob(os.path.join(dl, "maker_ms_????-??-??_*.csv.gz")):
        m = re.search(r"maker_ms_\d{4}-\d{2}-\d{2}_(\d+)(?:_\w+)?\.csv\.gz$", f)
        if m:
            out[m.group(1)] = max(out.get(m.group(1), 0), os.stat(f).st_mtime)
    return out


def construir(log=LOG, dl=DL):
    """-> {grupo: [dict(a, b, tipo, ...)]} con a,b en epoch s (ya con relleno)."""
    ev = parsear(log)
    mt = mtimes_por_pid(dl)
    res = defaultdict(list)
    for g, L in ev.items():
        # caidas
        for i, (t, tp, pid) in enumerate(L):
            if tp == "caida":
                nxt = next((u for (u, tq, _) in L[i + 1:] if tq == "con"), None)
                if nxt is not None:
                    res[g].append(dict(a=t - PAD_CAIDA_S, b=nxt + PAD_CAIDA_S, tipo="caida"))
        # reinicios: primer `conectado` de cada pid nuevo
        vistos, prev = {}, None
        for (t, tp, pid) in L:
            if tp == "con" and pid and pid not in vistos:
                vistos[pid] = t
                if prev is not None and prev != pid:
                    fin_prev = mt.get(prev)
                    est = fin_prev is None
                    a = fin_prev if fin_prev is not None else t - 120.0
                    if a < t:
                        res[g].append(dict(a=a, b=t + PAD_REINICIO_S, tipo="reinicio", pid_prev=prev, pid=pid, fin_estimado=est))
                prev = pid
    return {g: sorted(v, key=lambda d: d["a"]) for g, v in res.items()}


def guardar(h, salida=SALIDA):
    os.makedirs(salida, exist_ok=True)
    f = os.path.join(salida, "huecos_registro_ledger.json")
    previo = {}
    if os.path.exists(f):
        try:
            previo = json.load(open(f))
        except ValueError:
            os.replace(f, f + ".invalido_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S"))
    # fusion idempotente por (grupo, tipo, a redondeado): el ledger conserva lo que el log ya rotó
    for g, v in h.items():
        d = {(x["tipo"], round(x["a"], 1)): x for x in previo.get(g, [])}
        for x in v:
            d[(x["tipo"], round(x["a"], 1))] = x
        previo[g] = sorted(d.values(), key=lambda x: x["a"])
    tmp = f + ".tmp"
    json.dump(previo, open(tmp, "w"), separators=(",", ":"))
    os.replace(tmp, f)
    return f, sum(len(v) for v in previo.values())


def cargar(salida=SALIDA):
    f = os.path.join(salida, "huecos_registro_ledger.json")
    return json.load(open(f)) if os.path.exists(f) else {}


def estado_cierre(ledger, coin, C):
    """-> (estado, detalle): 'limpio' | 'caida' | 'reinicio' | 'caida+reinicio' segun huecos de coin#5min o coin#15min que cortan [C-305, C-10]."""
    lo, hi = C - VENTANA[0], C - VENTANA[1]
    tipos = set()
    det = []
    for g in (f"{coin}#5min", f"{coin}#15min"):
        for h in ledger.get(g, []):
            if h["a"] < hi and h["b"] > lo:
                tipos.add(h["tipo"])
                det.append((g, h["tipo"], round(max(h["a"], lo)), round(min(h["b"], hi))))
    return ("limpio" if not tipos else "+".join(sorted(tipos))), det


def clasificar(coin, dia, ledger=None, salida=SALIDA):
    ledger = ledger if ledger is not None else cargar(salida)
    d0 = datetime.strptime(dia, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    out = {}
    for k in range(1, 97):
        C = int(d0.timestamp()) + 900 * k
        out[C] = estado_cierre(ledger, coin, C)[0]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--guardar", action="store_true")
    ap.add_argument("--clasifica", nargs=2, metavar=("COIN", "DIA"))
    a = ap.parse_args()
    if a.guardar:
        f, n = guardar(construir())
        print(f"ledger {f}: {n} huecos")
    if a.clasifica:
        cl = clasificar(a.clasifica[0], a.clasifica[1])
        from collections import Counter
        print(a.clasifica, dict(Counter(cl.values())), f"limpios {sum(v == 'limpio' for v in cl.values())}/{len(cl)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
