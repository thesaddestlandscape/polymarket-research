# R5K (H43): limitaciones y camino (alpha-researcher, 19-Oct 2026 ~13:55Z, guardado por el chief)
Cifras del agente, NO re-verificadas por el chief. Definición: h43_auditoria_datos/grid.py (BTC, T∈(60,270], acumulado posicional, día = cierre UTC). Scripts en scripts/ (leen rutas del scratchpad: cambiar SP).

## Causa principal: RÉGIMEN, no datos ni multiplicidad
R5K diario = +0,057 + 1,61 × EV de la población de makers en banda BTC del mismo día (06-16 Oct, 11 días, corr 0,71; IC90 término fijo (−0,002,+0,139), pendiente (0,88,2,78)). ~2/3 del +0,20 in-sample era esa exposición apalancada.
Fuera de muestra (población en negativo): 05-Oct −0,142 (41), 17-Oct −0,190 (61), 18-Oct −0,298 (69); juntos 171 cierres EV −0,224 IC90 por cierre (−0,456,+0,014). Mismos makers (top-20 hace 40 % de rellenos fuera; nuevos 11 %), mismo T y precio: cambió el desenlace. No es fin de semana (10-11 Oct +0,22/+0,17).

## Limitaciones
L1 multiplicidad (24 celdas, ~5 independientes, máx azar ≈+0,10; no explica el colapso). L2 régimen (arriba; 16-Oct ya −0,013). L3 definición (C1-C4 ±0,01 agregado, ±0,1 un día; A6 contador en vivo sin construir). L4 tasa de relleno/cola desconocida (volumen tras cruce 5000: mediana 1.191, p10 134, p90 4.977; todo el volumen supera a K50 en 10/14 días: medir con H47). L5 selección adversa por maker (+0,60 a −0,30). L6 capacidad (5000 acc = p74 BTC; alts 32-456). L7 potencia (EV real +0,10 → ~3.000 unidades ≈33 días BTC; n≥40 no informa). L8 concentración (14-Oct +0,685; sin 2 mejores días +0,135).

## Walk-forward: sirve de protocolo, no de prueba (06-16 es un solo régimen)
Regla (a) máx EV: +0,291 adelante / +0,274 atrás / +0,299 un día fuera; (b) EV·√n: +0,235/+0,275/+0,197. Elige offset 5000 (todo el volumen tras el cruce, no puja única). Fuera del bloque esa celda: 05 −0,243, 17 +0,143, 18 −0,023 (171 cierres EV −0,009 IC90 (−0,38,+0,39)).
Regla de diseño: toda variante nueva en forward limpio desde 20-Oct 00:00Z y leída junto al exceso sobre la población del mismo día y moneda.

## Variantes (numeración del chief: H49 ya es "señal V4 como disparador de cancelación del maker", así que las del agente pasan a H50-H52)
- H46 R5K-NORM alts: se mantiene. Ojo: el percentil 95 en alts es el análogo de R8K, no de R5K; no cambiar el percentil. Umbrales ETH 824, SOL 341, XRP 128; días 11-18 OOS semi-limpio; gate ~21-Oct; lectura obligatoria de exceso sobre población y de volumen restante (XRP: si mediana <50 acc, reportar K=5). La mata: gate fallado por moneda tras ≥10 días o exceso ≤0.
- H50 R5K-REG (agente: H49): operar R5K solo si EV de la población BTC en los cierres de t−6h..t−60s > 0. Retro 05-18 una sola vez, descriptivo. La mata (≥10 días forward): EV(I>0)<+0,05, IC90 por cierre cruza 0, o EV(I>0)−EV(I≤0)≤0. Potencia ~550 unidades/10 días (EV ≥+0,23). Mismo interruptor serviría a H5M, H35, H46.
- H51 R5K-COTA15 (agente: H50): maker salta la unidad si lado implicado es ns y (1−bid15(ns)) − precio de puja < 0,02. Paso 0 sin desenlaces: si salta <10 % no se corre. La mata: EV con guarda − sin guarda ≤ +0,03 en ≥10 días. Relacionada con H49.
- H52 R8K-BTC (agente: H51): offset 8000, gate de R5K, solo cuenta forward desde 20-Oct (dentro 235 cierres +0,366; fuera 37 cierres +0,341 IC90 (−0,24,+0,95); ajuste: fijo +0,45, pendiente ≈0). Capacidad ≤7-21 k$/año no validada. La mata: gate fallado o EV<+0,05 tras 16 días.

## Orden recomendado
1) H46 con exceso (2-3 min, respuesta ~21-Oct). 2) H50 (puede rescatar R5K; ≥10 días ≈30-Oct). 3) H52 (coste ≈0, arrancar ya). H51 tras su paso 0. Contribución validada: 0. Ninguna mide captura real: H47 dirá la tasa de relleno.
H48 (solo anotada): ~600 unidades el 24-Oct; con EV real 0 saltaría ~14 %; publicar junto al exceso sobre población.
