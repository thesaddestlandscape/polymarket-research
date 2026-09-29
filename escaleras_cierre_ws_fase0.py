#!/usr/bin/env python3
"""escaleras_cierre_ws_fase0.py -- FASE 0 (solo observación), ronda2 #8 (precierre en escaleras
cripto 'above K' horarias/diarias) con el principio micro-latencia (29-Sep). Reusa el motor de
ya_decidido_ws_fase0 en modo "escaleras": strikes a <=4 % del spot cuyo endDate cae en los próximos
20 min; a T-90 s se piden sus tokens a libro_estado_ws (WS, histórico 100 ms) y a T+100 s se vuelca
la línea temporal del libro (best bid/ask, imbalance, profundidad) en T-60,-30,-20,-10,-5,-2,0,+1,+2,
+5,+10,+30,+60 s -> data/shadow/escaleras_cierre_ws_fase0.csv. El spot (bookTicker ms) y el
desenlace final se cruzan a posteriori: ¿a T-60/-10 s la dirección ya es conocida y el ask del lado
ganador aún deja margen? Se fusiona en observadores_fase0.py. NO coloca órdenes.
"""
import ya_decidido_ws_fase0 as Y


def _log(msg):
    Y._log(msg)


def main():
    Y.main("escaleras")


if __name__ == "__main__":
    main()
