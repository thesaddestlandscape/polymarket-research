# ALPHA-B «ENTRADA + SALIDA» de B (5m barato) — alpha miner, 27-Oct-2026 ~16:00Z
Expediente: experimentos/5m_barato/alpha_miner_b_27oct/ (PREREG_ALPHA_B.md sha c491e2c6…; ADENDA1 sha 25b22432…, firmada ANTES
de calcular ningún EV: la regla de libro cruzado C daba el 94 % de los rellenos y es un artefacto de orden invisible; sim.py e9909023…,
eval.py 975842c0…, run_all.sh, HASHES.txt, sim.log, eval_salida.txt, units/u_D.csv.gz). Datos: m5_registro 05-26 Oct (22 días,
50.078 mercado-lados, desenlace oficial 99,85 %; 22-Oct 97 %), reloj de recepción, libro real nivel 1, tomador a +250 ms,
fee 0,07·p(1−p), maker sin rebate. IS 05-22 / OOS 23-26 (visto una vez). sim.py es ciego (no lee desenlaces). Selftest OK.

## Veredictos prerregistrados (EVw = Σpnl/Σcoste, 1 obs por mercado-lado)
| Regla | IS EVw (IC90 días), días>0 | OOS EVw (IC90 cierre), días>0 | Veredicto |
|---|---|---|---|
| R1 puja bb+0,01 recotizada en continuo (Q1) + TD Binance, mantener | +0,0004 (−0,025..+0,025), 8/18; sin 2 mejores −0,012; n=25.427 | −0,032 (−0,083..+0,018), 1/4; n=5.711 | INSUFFICIENT_EVIDENCE (≈0) |
| R2 = R1 + salida maker a avg+0,01 (mandato) | −0,224 (−0,233..−0,215), 0/18 | −0,225 (−0,240..−0,212), 0/4 | REJECTED |
| R3 tomador incondicional del barato al ask (frente 4) | −0,066 (−0,081..−0,053), 0/18; n=40.369 | −0,133 (−0,157..−0,108), 0/4 | REJECTED |

Secundarias, IS (0/18 días >0 salvo L1/L5): salida +0,02 −0,231; X1 y volcar a T=30 s −0,218; inversión, descarga a avg−0,01: −0,231;
volcar al bid enseguida −0,116; cubrir con el favorito enseguida −0,026 (sobre el capital total). Vida fija 1 s / 5 s manteniendo:
+0,011 / +0,005 (OOS −0,028 / −0,025). Con la regla C: −0,025 (OOS −0,067). Placebo, comprar a bb+0,01 sin condicionar: +0,061
(17/18 días; OOS +0,083, 4/4). Inversión de R3, comprar el favorito al ask: −0,048 (OOS −0,048).

## Mecanismo
1. Una salida a precio fijo VENDE LAS GANADORAS. Con X1, las vendidas aciertan el 32,2 % con entrada media 0,234 (n=18.716) y las no
   vendidas el 0,1 % (n=8.086). Una venta por encima de la entrada se rellena en las trayectorias ganadoras, que pasan por todos los
   precios hasta 1, y deja las perdedoras: es vender la opción por 1 c. Δ(X1−mantener) = −0,224 (IC90 −0,244..−0,204) y es igual en el
   placebo (−0,224): no es selección adversa, es convexidad. Ninguna salida convierte la pérdida en ganancia. Volcar como tomador paga
   diferencial + comisión (−0,116), y el par bloqueado cuesta más de 1 (−2,6 %).
2. Lo que mueve la AS es la ENTRADA. Recotizar en continuo (o con vida de 1-5 s) + TD lleva la puja de ≈−0,2 (FRENTE-TD, vida 60 s) a
   ≈0. AS ≈ placebo − R1 ≈ 6 c/€: la selección por relleno se come exactamente el valor del bid.
3. Ser tomador pierde en los dos lados: el diferencial más la comisión supera cualquier sesgo.

## Hallazgos adversariales
- La entrada supone cola en cabeza a bb+0,01 con 130 ms de retraso (optimista: otro maker podría ir delante).
- No se modela la reacción de otros makers. YES = Up.
- Recotizar en cada cambio de libro exige muchas cancelaciones por segundo; los límites de la API no están medidos.
- R1 los días 24/25/26: −0,145/−0,146/+0,164, frente a FRENTE-TD −0,233/−0,276/−0,143 (poblaciones distintas, sin emparejar).
- R1 por moneda sigue al placebo: BNB +0,064 (IC90 +0,01..+0,11, n=3.726), DOGE +0,038, BTC −0,056 (−0,08..−0,03); vol60 <3 bps
  −0,048. Son cortes post-hoc (17) sin corregir por multiplicidad.

## Cartera
- Contribución validada: 0 €. R1 ≈ 0 no acerca a los 200 k€.
- Como DEFENSA de B (sin validar): recotizar en continuo + TD podría quitar casi toda su pérdida real (−0,072, n=202).
- Bolsillo hipotético BNB+DOGE: ~350 rellenos/día de 5 acc ≈ 7 k€/año si el EV fuese +0,05 (exploratorio).

## Siguiente experimento (uno)
- Primero, un validador independiente (cheap5m-statistical-validator) reproduce R1/R2/R3 con código propio desde units/, más 50
  unidades contra filas crudas.
- Si R1 se sostiene: forward congelado de R1 solo BNB+DOGE desde el 27-Oct, ≥10 días (~06-Nov). Éxito = EVw > 0 con IC90 por días > 0
  y ≥7/10 días > 0. Fracaso = EVw ≤ 0. Coste ~2 min de CPU al día, 0 €.
- Después, cheap5m-red-team-auditor: cola, recotización y límites de API.
- Sin dinero real.
