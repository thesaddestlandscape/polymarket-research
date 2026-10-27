"""Tests de ciclo_vida_W.py con filas sinteticas (sin disco, sin red). Uso: python3 test_ciclo_vida_W.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciclo_vida_W as C

TOK, GEM = "111", "222"
TX = "0x" + "ab" * 32
def fila(*a): return [str(x) for x in a]

# nivel bid 0.05 del token: B (100) -> alta +25 -> baja -25 sin T (cancelacion) -> alta +25 -> T + baja -25 (relleno)
rows = [
    fila("B", 1000, TOK, "0.05:100", "", "", 1010, 1),
    fila("d", 2000, TOK, "B", "0.05", 125, 2010, 2),
    fila("d", 3000, TOK, "B", "0.05", 100, 3010, 3),          # cancelacion (sin T)
    fila("d", 4000, TOK, "B", "0.05", 125, 4010, 4),          # alta == acc
    fila("T", 9000, TOK, "0.05", "SELL", 25, 9010, 5),        # el casado
    fila("X", 9000, TOK, TX, "", "", 9010, 6),
    fila("d", 9000, TOK, "B", "0.05", 100, 9011, 7),          # baja coincidente
    fila("T", 9100, GEM, "0.95", "BUY", 7, 9110, 8),          # T de otro casado, gemelo, precio 0.95 -> p=0.05
    fila("G", 9500, "*", "fin_sesion", "", "", 9500, 9),
]
serie, trades, huecos = C.reconstruir(rows, TOK, GEM, 0.05, 9400, 60, 5)
assert [x[2] for x in serie] == [100.0, 125.0, 100.0, 125.0, 100.0], serie
assert len(trades) == 2 and len(huecos) == 1
m, modo = C.elegir_T(trades, C.reconstruir.xs, TX, 0.05, TOK, 9400)
assert modo == "TX" and len(m) == 1 and m[0][2] == 9000, (m, modo)
m, modo = C.elegir_T(trades, C.reconstruir.xs, "0x" + "cd" * 32, 0.05, TOK, 9400 + 2400)   # otro tx: cae a ventana, 2 candidatos
assert modo == "VENTANA" and len(m) == 2, (m, modo)
# fuera de la ventana temporal no entra
serie2, tr2, _ = C.reconstruir(rows, TOK, GEM, 0.05, 900000, 60, 5)
assert serie2 == [] and tr2 == []
print("OK test_ciclo_vida_W")
