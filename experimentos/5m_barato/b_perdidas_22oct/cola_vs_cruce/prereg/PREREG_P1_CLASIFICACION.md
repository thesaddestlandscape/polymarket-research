# PREREG P1 — clasificación cola/cruce de rellenos maker (B real y población), 22-Oct-2026 ~16:00Z
Congelado ANTES de calcular EV por clase en población y la clase por bloque en B. Ya visto antes de congelar (declarado):
(a) r3_escalado: B real cola +0,190 (n=85) / cruce −0,091 (n=59), definición WS «print por debajo en 1 s» (reproducido igual aquí);
(b) B real a nivel de TX (p1_b_tx.py): TX_STOP n=161 EV −0,003, hit 19,9 %; TX_DEEP n=36 EV −0,114, hit 19,4 %.
Nada más (ni población ni bloques).

## Unidad y precio equivalente
Todo relleno maker = posición larga en un token c a precio pc: maker BUY de x → c=x, pc=precio; maker SELL de x a a → c = complemento, pc = 1−a.
«Más hondo» que una posición (c, pc): otro relleno maker (cualquier maker) que da largo en c a pc' < pc − 0,005.
Población: primeras 5 acc por (maker, mercado, c), pc del 1.er relleno en (0,10; 0,30], T = fin − ts_bloque en (60; 300] s, ETH/SOL/XRP 5m,
17–22 Oct (22 hasta el fichero disponible), excluida la wallet de B. B real: cada relleno on-chain (movimientos.csv, tanda_B) y su posición.

## Clases (de la 1.ª fila de la unidad)
- C1 TX_DEEP: la MISMA tx contiene un relleno más hondo (la orden tomadora atravesó nuestro nivel).
- C2 POST_DEEP: no C1, y hay un relleno más hondo en una tx POSTERIOR (mismo bloque con log_index mayor, o bloques b+1..b+H), H=1 primario.
- C3 COLA: ni C1 ni C2.  CRUCE = C1 ∪ C2.
Sensibilidad (no cambia el primario): H=0, H=2, H=5; umbral 0,005 → 0,015 (un tick entero más).
B: además la clase WS de r3 (V1_lt>0) para matriz de concordancia.

## Métricas
EV = Σpnl/Σcoste (pnl con desenlace oficial; missing se cuenta y excluye); IC90 bootstrap por DÍA y por CIERRE (2.000, semilla 20261022);
EV sin los 2 mejores días; hit vs precio medio; por moneda y por tramo de pc (0,10-0,15-0,20-0,25-0,30]. Diferencia COLA−CRUCE con IC90 por día.
## Control de supervivencia/selección (encargo b del chief)
La clase es posterior al relleno (es en parte un markout): se reporta así. Para separar «cola» de «puja que sobrevive»: (i) estratos
moneda × tramo pc × tramo T (60-120-180-240-300) con diferencia ponderada; (ii) dentro de B, a igual edad de la orden y nivel (k) con el ledger.
## Criterio para pasar a palancas (P2)
La diferencia COLA−CRUCE en población tiene IC90 por días > 0 en ≥2 de 3 monedas Y la clase es predecible antes del relleno por algún
rasgo de colocación (AUC > 0,55 en días 17-19 y > 0,55 en 20-22). Si no: el efecto es markout ex post y se declara no accionable.
