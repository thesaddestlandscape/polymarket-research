# PREREGISTRO E1b -- confirmacion FORWARD de S1_x2_w2000 (regla NO elegida en E1; observada post-hoc) -- 22-Oct-2026 ~15:45Z
Fijado ANTES de existir los datos que lo juzgan (dias >= 2026-10-23). Solo lectura; no toca B, procesos, crons ni config.
Origen: E1 (PREREG_E1_CANCELAR_MS.md sha 31d09a9f...) eligio S3 en DESC y fue REJECTED en TEST. S1_x2_w2000 fue positiva en DESC y TEST
(6/6 dias), pero es una de 7 reglas vistas en ambos periodos: hipotesis post-hoc, por eso necesita datos virgenes.
## Regla congelada
Retirar la puja tipo B (ETH/SOL/XRP 5m) cuando el retorno del aggTrade Binance de la misma moneda en los 2.000 ms previos (por recepcion),
firmado a favor de nuestro lado, sea <= -2 bps; retirada efectiva a +100 ms; vuelve a los 2.068 ms del ULTIMO disparo. Simulador y
evaluacion: scripts/e1_sim.py (sha256 en HASHES_E1.txt) sin cambios de parametros; variante 'S1_x2_w2000|D100'.
## Datos
Dias >= 2026-10-23 extraidos con ../salida/scripts/extraer.py (registro ms; ROTA a ~4-5 dias: extraer cada dia o se pierden) +
../salida/scripts/desenlaces.py; dia valido = >= 80 % de los mercados 5m ETH/SOL/XRP esperados con desenlace oficial.
## Gate (todo en dias forward, sin reelegir nada)
CONFIRMADA si >= 5 dias validos y: (1) dPnL/EUR > 0 con IC90 por DIA > 0 y por CIERRE > 0; (2) >= 60 % de dias con dPnL > 0;
(3) dPnL/EUR > INV y > maximo de los 8 desplazamientos; (4) D250 > 0; (5) en el subconjunto R2-falso (bid15 mismo lado - obj > 0,03 en
r-100 ms) dPnL > 0. REFUTADA si >= 5 dias y IC90 por dia sup <= 0, o si a 10 dias la estimacion puntual <= 0. Si no: ACUMULANDO.
Expectativa declarada (de E1, no gate): dentro de R2-verdadero el incremento ~0 (E1: +0,002/EUR); si en forward fuese < 0, S1 NO se
apila sobre R3. Descriptivo: rellenos reales de B con/sin senal (E1: con senal n=20 EV -0,44; sin senal n=124 +0,15) al llegar a 300 posiciones.
Primera lectura: 28-Oct (dias 23-27). Ningun cambio a B antes de N=500 + /code-review + OK de Javi.
