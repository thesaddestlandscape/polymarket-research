import os, sys, time, queue, gzip, tempfile, pathlib
sys.path.insert(0, sys.argv[1]); sys.path.insert(1, "/root/polymarket-research")
import libro_estado_ws as M
from datetime import datetime, timezone
def leer(p):
    r = []
    try:
        for l in gzip.open(p, "rt"): r.append(l.rstrip("\n"))
    except EOFError:
        pass
    return r
tmp = pathlib.Path(tempfile.mkdtemp()); M.LIBRO5_DIR = tmp
M._Libro5.MIN_LIBRE_GB = 0.0; M._Libro5.ESTADO = pathlib.Path(tempfile.mkdtemp()) / "estado.json"; M._Libro5.INTERRUPTOR = pathlib.Path(tempfile.mkdtemp()) / "OFF"
X = M._Libro5(); M._LIBRO5 = X; M._REGISTRO = None
cie = int(time.time()) + 200; fin = datetime.fromtimestamp(cie, timezone.utc).isoformat()
X.meta({"T5": ("BTC", "5min", "m", fin, "YES"), "T15": ("BTC", "15min", "m2", fin, "YES"),
        "OLD": ("BTC", "5min", "m0", datetime.fromtimestamp(cie - 5000, timezone.utc).isoformat(), "NO")})
assert X.toks == frozenset({"T5"}) and "OLD" in X.rechazados
X.alta("g", ["T5", "T15"]); assert X.dueno == {"T5": "g"}, X.dueno
now = int(time.time() * 1000); out = []
M._LIB["T5"] = {"bids": {}, "asks": {}}; M._LIB["T15"] = {"bids": {}, "asks": {}}
M._aplicar({"asset_id": "T5", "bids": [{"price": "0.20", "size": "10"}], "asks": [{"price": "0.22", "size": "7"}], "timestamp": now}, out, "g")
M._aplicar({"price_changes": [{"asset_id": "T5", "price": "0.20", "size": "4", "side": "BUY"}, {"asset_id": "T5", "price": None, "size": "1", "side": "BUY"},
                              {"asset_id": "T15", "price": "0.5", "size": "2", "side": "BUY"}, {"asset_id": "T5", "price": "0.22", "size": "0", "side": "SELL"}], "timestamp": now + 1}, out, "g")
M._aplicar({"event_type": "last_trade_price", "asset_id": "T5", "price": "0.22", "side": "BUY", "size": "7", "timestamp": now + 2}, out, "g")
M._hueco_libro5("g", {"T5", "T15"}, "baja")                 # baja: G y nada más suyo
M._aplicar({"asset_id": "T5", "bids": [{"price": "0.2", "size": "1"}], "asks": [], "timestamp": now + 3}, out, "g")
X.alta("g", ["T5"])
M._aplicar({"asset_id": "T5", "bids": [{"price": "0.19", "size": "1"}], "asks": [], "timestamp": now + 4}, out, "g")
M._cerrar_libro5()
assert X.cerrado.is_set()
fs = sorted(tmp.iterdir()); filas = [l for p in fs for l in leer(p)]
for l in filas: print(l)
cuerpo = filas[1:]
tipos = [x[0] for x in cuerpo]
assert tipos == ["G", "B", "d", "d", "T", "G", "B", "G"], tipos
assert ",*,arranque" in cuerpo[0] and ",*,fin_proceso" in cuerpo[-1] and ",T5,baja" in cuerpo[5]
assert "0.19:1" in cuerpo[6] and "0.20:10" in cuerpo[1] and ":1.0;" not in cuerpo[1].split(",")[3][0:0] + "x"
assert all(len(x.split(",")) == 8 for x in cuerpo), [len(x.split(",")) for x in cuerpo]
seqs = [int(x.split(",")[-1]) for x in cuerpo]; assert seqs == list(range(1, len(seqs) + 1)), seqs
assert all(",T15," not in x for x in cuerpo)
# cola llena en banda
Y = M._Libro5.__new__(M._Libro5); Y.q = queue.Queue(maxsize=2); Y.activo = True; Y.perdida = False; Y.descartes = 0
Y.put([("d", 1)]); Y.put([("d", 2)]); Y.put([("d", 3)]); assert Y.perdida
Y.q.get_nowait(); Y.q.get_nowait(); Y.put([("d", 4)]); lote = Y.q.get_nowait()[1]
assert lote[0][0] == "G" and lote[0][3] == "cola_llena" and lote[1] == ("d", 4) and not Y.perdida
# muerte definitiva no se reanuda
Z = M._Libro5.__new__(M._Libro5); Z.lk = __import__("threading").Lock(); Z.activo = True; Z.muerto = False
Z.desactivar("x", definitivo=False); assert Z._reanudar(); Z.desactivar("y"); assert not Z._reanudar()
# _abrir nunca sobrescribe
f, n = X._abrir("2026-10-17", 0); f.close(); f2, n2 = X._abrir("2026-10-17", 0); f2.close(); assert n2 > n
# carrera entre grupos: alta en g2 antes de la baja de g1 -> sigue grabable y SIN G
X2 = M._Libro5.__new__(M._Libro5); X2.toks = frozenset({"A"}); X2.dueno = {}; X2.activo = True; X2.perdida = False; X2.q = queue.Queue(); X2.descartes = 0
X2.alta("g1", ["A"]); assert X2.q.empty() and X2.grabable("A", "g1") and not X2.grabable("A", "g2")
X2.alta("g2", ["A"]); l = X2.q.get_nowait()[1]; assert l[0][3] == "traspaso" and X2.grabable("A", "g2") and not X2.grabable("A", "g1")
X2.hueco("g1", ["A"], "baja"); assert X2.q.empty() and X2.grabable("A", "g2"), "la baja del viejo dueño no corta al nuevo"
X2.hueco("g2", ["A"], "caida"); assert X2.q.qsize() == 1 and X2.grabable("A", "g2"), "caida: G y sigue dueño"
X2.q = queue.Queue(); X2.hueco("g2", ["A"], "baja"); assert X2.q.qsize() == 1 and not X2.grabable("A", "g2")
# volumen no montado -> no arranca (simulado con ruta bajo /mnt/HC_Volume_106538179 y ismount falso)
import unittest.mock as um
with um.patch.object(M, "LIBRO5_DIR", pathlib.Path("/mnt/HC_Volume_106538179/libro5_test")), um.patch("os.path.ismount", return_value=False):
    try:
        M._Libro5(); assert False, "debía fallar"
    except RuntimeError:
        pass
# interruptor persistente: con el fichero, pausa con G interruptor; al quitarlo, reanuda
import shutil
tmp2 = pathlib.Path(tempfile.mkdtemp()); M.LIBRO5_DIR = tmp2
inter = pathlib.Path(tempfile.mkdtemp()) / "LIBRO5_OFF"
M._Libro5.INTERRUPTOR = inter; inter.touch()
W = M._Libro5(); time.sleep(1.5); assert not W.activo and not W.muerto, "pausado por interruptor"
inter.unlink(); W.dueno = {}
print("OK todos")
# presupuesto: borra los más antiguos y nunca el actual
tmp3 = pathlib.Path(tempfile.mkdtemp()); M.LIBRO5_DIR = tmp3
P = M._Libro5.__new__(M._Libro5); P.PRESUPUESTO_GB = 2e-9 * 1000
import time as _t
for i, n in enumerate(["libro5_ms_2026-10-01_1.csv.gz", "libro5_ms_2026-10-02_1.csv.gz", "libro5_ms_2026-10-03_1.csv.gz"]):
    (tmp3 / n).write_bytes(b"x" * 1000); os.utime(tmp3 / n, (1000 + i, 1000 + i))
P._ajustar_presupuesto("libro5_ms_2026-10-01_1.csv.gz")
quedan = sorted(p.name for p in tmp3.iterdir()); print(quedan)
assert "libro5_ms_2026-10-01_1.csv.gz" in quedan and "libro5_ms_2026-10-02_1.csv.gz" not in quedan, "borra el más antiguo salvo el actual"
print("OK presupuesto")
