#!/usr/bin/env python3
"""colas_escaleras_ws_fase0.py -- FASE 0 (solo observación), ronda2 #6 (vender colas de mercados de rango) con
micro-latencia: para escaleras cripto horarias, strikes a 1-6 % del spot; desde T-31 min sigue el libro del YES por WS y
vuelca bid/ask + TAMAÑOS en T-30/-15/-5/-1 min, T y +60 s (data en datalogs gz, retención 14 d). Retrospectivo 29-Sep
(720 mercados, 21 h): YES a 0,02-0,05 acierta 0-0,5 % (n=216) => comprar NO a ~0,976 rinde +1,8-2,3 %/€ con g>0, PERO con
precio MEDIO de la historia; lo que decide es el BID real (y su tamaño) para vender el YES/comprar el NO y el riesgo de
cola (un solo evento arrastra todos los strikes de esa hora). NO coloca órdenes. Hilo de observadores_fase0."""
import ya_decidido_ws_fase0 as Y


def _log(msg):
    Y._log(msg)


def main():
    Y.main("colas")


if __name__ == "__main__":
    main()
