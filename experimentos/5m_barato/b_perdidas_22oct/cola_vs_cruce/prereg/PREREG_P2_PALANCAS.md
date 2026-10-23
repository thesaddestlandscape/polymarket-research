# PREREG P2 — palancas de colocación contra el relleno «que sigue cruzando» (simulador con COLA), 22-Oct-2026 ~16:05Z
Congelado ANTES de construir resultados del simulador. Visto antes (declarado): P1 completo (AVANCE.md); E1/E1b/r3/V9-V3/salida;
dato E1b in-sample (C2 = seguir el bid con asentado 250 ms: +0,076 €/€, retención 0,82). El gate P1 FALLÓ: esto es exploración
de palancas medidas directamente sobre EV, no sobre la etiqueta cola/cruce.

## Instrumento E1Q (nuevo; motivo: E1 solo modela rellenos por cruce y el 54-59 % de los rellenos de B son en cola)
Libro L2 completo `libro5_ms` (B/d/T, hora de RECEPCIÓN, orden seq) por mercado ETH/SOL/XRP 5m. Política tipo B importada de
`seleccion_adversa_plan/scripts/e1_sim.py` (obj_raw, banda (0,11; 0,30], k ETH 2 / SOL,XRP 1, T 298→65 s, rejilla 100 ms, asentado
SETTLE del top). Lado = el primero cuyo top bid entra en banda (como B/E1). Orden viva a +85 ms del envío (calib_colas); cancelación
efectiva a +65 ms; tras cancelar, nueva orden en la siguiente decisión ≥150 ms. Cola FIFO: delante = tamaño del nivel al quedar viva;
bajadas del nivel explicadas por operaciones a ese precio en [−300, +150] ms consumen delante; no explicadas = cancelaciones repartidas
«prop» (central; sensibilidad lo/hi). Relleno: operación normalizada (SELL propio a q o BUY del contrario a 1−q) con q < puja → llena
el resto (CRUCE por atravesar); q = puja → consume delante y luego a nosotros (relleno al precio). Un relleno (aunque parcial) cierra la
puja (regla de B). Desenlace oficial (cache + desenlaces_extra; missing contado). Clase del relleno simulado: X1 = por atravesar;
X2 = al precio y en ≤2 s se opera por debajo; X3 = cola (resto).
Fidelidad (no gate, se reporta): tasa de relleno por puja y mezcla X1/X2/X3 frente a B real 20-22 Oct (on-chain C1/C2/C3).

## Palancas (familia cerrada, 8 variantes; nada más se mira)
BASE (k de B, SETTLE 1.500, 5 acc) · S250 (SETTLE 250 ms = C2 de E1b) · K0 (puja AL top) · KMAS (k+1) · NOTOP (si el top baja hasta
nuestro precio, cancelar y volver a top−k: no quedarse solo en el top ante un barrido) · COLA50 (pujar solo si hay ≥50 acc delante en
el nivel) · COLA0 (pujar solo si hay <50 acc delante) · K10 (10 acc).
## Métricas y controles
EV = Σpnl/Σcoste de los rellenos (5 acc o el tamaño de la variante); € PnL; retención de € frente a BASE; cuota X3.
Control de igual volumen: por día, quitar al azar rellenos de BASE hasta el € de la variante (2.000 réplicas) → p = P(EV placebo ≥ EV var).
Diferencia EV_var − EV_BASE con IC90 bootstrap por DÍA y por CIERRE (pareada por mercado). Sin 2 mejores días.
## Split por días
ELEGIR: 17-19 Oct (caché colas_20oct; 17 desde ~10:33Z). Se elige UNA palanca: la de mayor EV_var − EV_BASE con retención ≥ 0,70 y
p placebo < 0,10. MEDIR: 20-22 Oct (extracción nueva de libro5) solo la elegida + BASE (las demás se reportan como descriptivo).
Gate (para proponer una variante de B a review, no para operar): en MEDIR, diferencia > 0 con IC90 por cierre > 0, ≥2/3 días > 0,
p placebo < 0,10 y retención ≥ 0,70. Si falla: REJECTED para esta versión.
