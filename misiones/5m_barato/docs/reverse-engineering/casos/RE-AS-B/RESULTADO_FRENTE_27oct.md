# RESULTADO E-RE-AS-B-FRENTE y FRENTE-FAV (27-Oct-2026 ~13:35Z) — polymarket-quantum-alpha-miner (revisión DESPUÉS; no autocertifica)
Datos: m5_registro 24-26 Oct (vidas con el MISMO calendario que vpv: 1.197/1.197 claves (mercado,lado,t0) idénticas en la prueba de 3 M líneas), Binance x (recepción), desenlace caché (28+27 vidas sin gana fuera). Unidad = primer print por mercado-lado; EVw = Σpnl/Σcoste; IC90 bootstrap por CIERRE (2000, semilla 2711). Salidas: frente_salida.txt, frente_fav_salida.txt, frente_posthoc_salida.txt (sha en HASHES.txt). Datos por vida: experimentos/5m_barato/re_as_b_frente/{fr_D,fav/fr_D}.csv.gz.

## 1. FRENTE-TD (PREREG_FRENTE.md sha 1528f06b…): puja barata en el frente de un nivel nuevo (bb+0,01) + TD Binance — REFUTADA
- TODO: n=5.081 unidades, 864 cierres, coste 6.234 €, EVw −0,217 (IC90 −0,257..−0,174). DESC 24+25 −0,254 (−0,303..−0,207); OOS 26 −0,142 (−0,217..−0,065). Días −0,234 / −0,275 / −0,142 (3/3 <0).
- Mismas vidas, cola final (vpv) con TD: pes −0,286, opt −0,001. El frente gana a pes (+0,069, IC +0,045..+0,093) pero pierde contra opt (−0,216): no rescata nada.
- Moneda (TODO): BTC −0,077 (n=806, IC −0,152..−0,005; 26-Oct +0,006); ETH −0,150; SOL −0,226; XRP −0,224; DOGE −0,326; BNB −0,406. 0 de 27 celdas moneda×bucket con n≥40 y cota inferior del IC90 >0 (mejor: BTC b10 +0,24, n=62, IC −0,32..+0,92).

## 2. FRENTE-FAV-TD (PREREG_FRENTE_FAV.md sha ead88750…; idea nacida del post-hoc, DECLARADO): vender el barato = pujar el FAVORITO en el frente — REFUTADA
- TODO: n=3.922, 856 cierres, coste 14.581 €, EVw −0,056 (IC90 −0,075..−0,037); DESC −0,031 (−0,052..−0,010); OOS 26 −0,105 (−0,138..−0,071); días −0,033 / −0,030 / −0,105.
- BTC +0,006 (n=702, IC −0,027..+0,036); BTC b70 +0,020 (n=497, IC −0,020..+0,060); resto <0. 0/30 celdas con IC90 >0.
- Por ACCIÓN las dos caras pierden lo mismo: barato −0,217×~0,24 ≈ −5,2 c/acc; favorito −0,056×~0,80 ≈ −4,5 c/acc.

## 3. Mecanismo (lo que cambia la decisión)
- La AS de B NO es de cola ni de lado: el primer tomador que cruza una cotización mejorada en 5m está, en media, informado. En el frente barato el 94 % de los primeros prints son COMPRAS DEL FAVORITO por el espejo (tipo B, −0,264, n=5.297); las ventas directas del barato son pocas y menos malas (tipo A −0,110, n=365, IC cruza 0). Un primer print pequeño (<5 acc) es igual de tóxico (−0,252) → la premisa «el vendedor pequeño es no informado» es FALSA (post-hoc, descriptivo).
- Gradiente temporal: relleno con T restante 240-300 s −0,106 (IC −0,19..−0,02) frente a T<180 s −0,35: el flujo informado crece al avanzar la ventana (confirmación del favorito). Relleno <1 s tras colocar −0,085, pero ese tramo está contaminado por prints que llegan después y ocurrieron antes de nuestra orden (retardo feed p99 1,5 s; Lp 0→250 empeora el EV) → optimista.
- TD (Binance ≥2 bps/300 ms, Lc=100) discrimina en ambas caras (apartados −0,394 vs −0,220 barato; −0,172 vs −0,057 favorito) y mejora ~+0,02 sobre su placebo −60 s; es un orden de magnitud insuficiente.

## 4. Sensibilidad pes/opt (lo pedido)
- En el frente la regla de relleno casi no depende del modelo: A+B vs max(A,B) −0,2169/−0,2171 (fav −0,0556/−0,0558); Lp 0/85/250 −0,202/−0,217/−0,231 (fav −0,051/−0,056/−0,053); solo rellenos de 5 acc −0,242; sin disputadas −0,241. La refutación NO depende de pes/opt.
- Sí depende de lo no observable: la reacción de otros makers a nuestro nivel (penny-jumping → peor) y los vendedores que solo venderían a b' (signo desconocido); no es plausible que compensen −5 c/acc. La cola final sí depende (pes −0,286 vs opt −0,001 con TD); el B real (−0,072, n=202) queda dentro de ese intervalo.

## 5. Veredicto y siguiente
REFUTED (las dos políticas congeladas, según su criterio prerregistrado). Ninguna palanca medida (TD, cola, frente, lado, complementario) lleva la puja pasiva de 5m a EV>0; el mejor caso es BTC ≈0. Sin candidata no se deja forward ni cron.
Siguiente experimento con valor de decisión: REWARDS-5M (otro pagador): cuantificar el pool de recompensas de liquidez por mercado 5m (gamma: tasa diaria, tamaño mínimo 50, spread máx. 4,5c) y la cuota alcanzable frente a las cotizaciones rivales en libro5_ms, contra el coste de AS medido aquí (~4,5-5 c/acc rellenada, menos con TD) cotizando en el borde de la banda. Si pool×cuota < AS, cerrar la familia maker pasiva 5m para B.
