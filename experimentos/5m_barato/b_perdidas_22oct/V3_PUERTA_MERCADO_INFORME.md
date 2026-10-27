# V3 «puerta de MERCADO» para B (H47-B maker) -- cierre del cabo suelto -- 22-Oct-2026 ~15:35Z
**Veredicto: REFUTADA** (H-V, vetar mercados cuya 1.a cotizacion tiene spread > 0,02) y **REFUTADA** la version «al reves»
(H-F, pujar solo/preferentemente donde el spread de la 1.a cotizacion es 0,01). Etiqueta: `REJECTED` para esta version.
Segun el preregistro, **no se construye** el forward `shadow_v3m/` ni el MD de uso en B / R2 / R3.
No se ha tocado B (`experimento_maker_h47.py` sha c82f5dc5f304b8a6, verificado), supervisor, procesos, crons, config ni ordenes.

## 1. Preregistro (antes de calcular)
`prereg_v2/PREREG_V3_PUERTA_v2.md`, sha256 `6e317f97b35baeb2c3352f068591cfbf6e34126994f013dc9567cf9997add385`, solo lectura,
congelado 15:02Z; el script de analisis verifica el hash antes de calcular. Fija: definicion exacta de la puerta (la de sim_v2: 1.a
cotizacion valida de la politica B-like, spread = round(ask-bid, 2) del token del lado s; veto si > 0,025), umbral unico (0,02; y 0,01
para H-F), poblacion valida, dias primarios 09-16 Oct (no usados en el descubrimiento 17-21), gate R0 de reproduccion, IC90 por dia y
por cierre, placebo estricto (etiquetas de MERCADO barajadas dentro de dia-moneda-bloque de 6 h, mismo n vetado por estrato),
multiplicidad m=4 (Bonferroni, alfa 0,0125) y exigencia de pasar en los DOS instrumentos.
Desviacion declarada (higiene, post-congelacion, no cambia nada): un mercado que cierra a las 00:05 aparece en dos ficheros de dia
(tambien en el simv2 original: 5846643 en 18 y 19-Oct); se conserva la fila del dia de su ventana (2 filas en 09-16).

## 2. Por que la poblacion «no podia» replicarla y como se ha resuelto
- No faltaba ningun dato: `ms_units.pkl` mide el spread en t_obs = ts-4 s del token de CADA relleno (por eso I4b era otra variable).
  La puerta es una propiedad del MERCADO medible con el libro en T 295..65 s.
- El archivo `VOL/m5_registro/m5_registro_D.csv.gz` (05-21 Oct) guarda las filas q crudas de todos los tokens 5m. `v3m/book_grid.py`
  reconstruye el top en la rejilla de sim_v2 y `v3m/sim_v3m.py` copia la logica de sim_v2 (p, bb, ba, minpc, lado, desenlace).
- **R0 superado**: sobre 17-21 reproduce los `simv2_D.npz` originales: 100 % de celdas p y minpc identicas, 100 % mismo paso y mismo
  spread de la 1.a cotizacion, 99,88 % de mercados comunes (1 menos por dia: el duplicado de medianoche). Delta de la puerta en 17-21
  = +0,128 (original +0,129) (`v3m/r0_check.json`).
- Con eso hay dos instrumentos fuera de muestra: **I5** = el mismo simulador en 8 dias nuevos (09-16 Oct, 6.873 mercados cotizados,
  5.359 rellenos, cobertura 98,96-99,77 % de 864/dia) e **I6** = poblacion de OTROS makers (505 makers, 54.006 unidades del lado de
  la puerta y casadas despues de la decision) con la etiqueta de mercado.
- B real fuera de muestra (pujas tras 14:45Z): ~39 pujas / ~6 posiciones nuevas: n inutil, no se usa.

## 3. Resultados (EV ponderado por EUR; Delta = EV(no vetados) - EV(vetados); neto = -pnl de lo vetado)
| Instrumento | n / vetados | EV base / ret. / vet. | **Delta** | IC90 dia | IC90 cierre | dias Delta>0 | placebo p (Delta / neto) | neto EUR (- placebo) |
|---|---|---|---|---|---|---|---|---|
| I3 descubrimiento 17-21 (original, re-evaluado con el placebo v2) | 3.269 / 695 | -0,146 / -0,119 / -0,248 | +0,129 | (-0,006,+0,250) | (+0,008,+0,244) | 4/5 | 0,014 / 0,024 | +184,8 (+74,3) |
| **I5 simulador 09-16 (OOS)** | 5.359 / 622 | -0,108 / -0,122 / -0,001 | **-0,120** | (-0,240,+0,026) | (-0,258,+0,010) | 2/8 | 0,967 / 0,967 | +0,8 (-82,3) |
| **I6 poblacion 09-16 (OOS)** | 54.006 / 4.521 (773 mercados) | +0,064 / +0,050 / +0,223 | **-0,174** | (-0,350,+0,007) | (-0,360,-0,001) | 3/8 | 0,976 / 0,977 | -937,7 (-712,3) |
| I6 poblacion 17-21 (secundario, solapado) | 25.726 / 3.663 | -0,067 / -0,055 / -0,147 | +0,092 | (-0,028,+0,232) | (-0,067,+0,249) | 4/5 | 0,042 / 0,042 | +466,8 |
| I5+I3 13 dias (09-21, secundario) | 8.624 / 1.316 | -0,122 / -0,121 / -0,129 | +0,008 | (-0,112,+0,117) | (-0,076,+0,096) | 6/13 | 0,525 / 0,579 | +184,8 (-10,4) |
- Gate (§4): I5 y I6 fallan G1-G4 (I5 tambien G7: el cambio de PnL +0,8 EUR es menor que el de vetar al azar, +83,1); pasan solo
  G5 (no degenerada) y G6 (n). Criterio de REFUTADA cumplido: Delta <= 0 en ambos instrumentos y neto <= placebo en I5.
- Por moneda (I5, sensibilidad): ETH Delta -0,412 (69 vetados), SOL -0,077 (179), XRP -0,167 (374). Ninguna invierte el signo.
- Sensibilidades I6 (no deciden): sin restriccion de hora -0,137; ambos lados -0,083. Mismo signo.
- **H-F (al reves)**: I5 EV de los rellenos con puerta 0,01 = -0,129 (n=3.746, IC90 dia (-0,180,-0,079), cierre (-0,182,-0,073));
  DeltaF -0,069 (p 0,95); I6 DeltaF -0,055 (IC90 dia (-0,186,+0,079)). Los mercados de libro estrecho no favorecen la puja: REFUTADA.
- Fill/acierto (I5, pujas cotizadas): puerta <=0,02 rellena 79,4 % y acierta 19,8 % de lo rellenado; >0,02 rellena 68,7 % y acierta
  22,0 %. El patron de B real (13,5 % vs 25,4 %) y de 17-21 no aparece en 09-16.

## 4. Volumen frente a seleccion (hallazgo del red team aplicado)
El placebo v2 ya iguala el numero de mercados retirados por estrato. Ademas, como el EV del simulador (-0,11/-0,15) no es el de B
(+0,008), descompongo el neto en volumen (-coste_vetado x EV_base) y seleccion (coste_vetado x (EV_base - EV_vetado)) y lo reescalo a
la base de B: I3 17-21 neto +184,8 = volumen +108,6 + seleccion +76,2 (con la base de B: +70); **I5 09-16 = volumen +74,0 + seleccion
-73,2 (con la base de B: -78,7 EUR)**; I6 09-16 seleccion -668 (-0,159 por EUR vetado); 13 dias juntos: seleccion +10 (+0,007/EUR),
con la base de B -1,4 EUR. Mas de la mitad del «ahorro» del descubrimiento era apostar menos; la parte de seleccion cambia de signo
fuera de muestra.

## 5. Lectura
- El +0,129 era un efecto de periodo (17-21 Oct), no un mecanismo: aparece en las dos fuentes en 17-21 (simulador e I6 +0,092) y se
  invierte en las dos en 09-16. Coherente con la trampa de la casa: in-sample ≠ forward; con IC por dia de 5 dias no se distingue un
  regimen de un rasgo.
- Ni siquiera el descubrimiento pasaba la vara v2: con el placebo de mercado estratificado p = 0,014/0,024 > alfa 0,0125, e IC90 por
  dia (-0,006,+0,250).
- Multiplicidad: familia de 4 hipotesis (V3 por paso, puerta de mercado, puerta favorable, lectura de spread de B real/b_postmortem);
  ninguna p de esta ronda baja de 0,86, asi que la correccion no cambia nada.
- Para el chief: la linea «reglas de veto de B por spread» queda cerrada (por paso v1, en el relleno I4b, puerta de mercado v2 y su
  inversa). Lo vivo sigue siendo R2/R3 (bid 15m) de `b_seleccion_adversa`. Reabrir V3 exigiria un mecanismo distinto, no otro umbral.

## 6. Limites
- I5 es simulacion (relleno 'cons' sobre la cinta, 5 acc, sin cola real) y su nivel absoluto no es B; por eso decide Delta, con
  placebo y la descomposicion del §4, no el neto bruto. I6 son otros makers (hora = bloque - 2,4 s +-1,5 s). Solo ETH/SOL/XRP; BTC no.
- Sin comision (maker) ni rebate (+0,011/EUR, no cambia signos). 21-Oct parcial en I6 (2.490 unidades).
- Los 8 dias OOS son anteriores (09-16) al descubrimiento: refutan la regularidad, no prueban que el 20-22 de B real fuera azar.

## 7. Archivos y reproduccion
- `prereg_v2/PREREG_V3_PUERTA_v2.md` + `.sha256`.
- `v3m/book_grid.py` (libro desde m5_registro), `v3m/sim_v3m.py` (sim_v2 sin rasgos Binance), `v3m/r0_check.py` -> `r0_check.json`,
  `v3m/analisis_v3m.py` -> `resultados_v3m.json`, `salida_v3m.txt`, `run_manifest_v3m.json` (sha de inputs, semilla 20261023,
  2.000 remuestreos/permutaciones), `run_build.sh`. Datos pesados: `/root/polymarket-research-datalogs/v3m_puerta/` (14 MB:
  grid_D.npz, simv3m_D.npz, build.log).
- Reproducir: `cd .../b_perdidas_22oct/v3m && ./run_build.sh` (~20 min, <600 MB RSS, nice 19) y luego
  `(ulimit -v 2000000; ARROW_DEFAULT_MEMORY_POOL=system nice -n 19 ionice -c3 python3 analisis_v3m.py)` (~40 s).
