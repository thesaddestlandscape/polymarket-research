# PREREG E-RE-AS-B-REWARDS5M (27-Oct-2026, escrito ANTES de calcular la cuota; solo lectura de datos publicos)
Fuente de la formula: https://docs.polymarket.com/programs/liquidity-rewards (leida 27-Oct 13:2xZ; seccion Methodology, ecuaciones 1-7). NO de memoria.
## Formulas (copiadas de la doc)
- S(v,s) = ((v-s)/v)^2 * b ; v = max_spread (centimos), s = distancia al punto medio ajustado por tamano, b=1 (sin multiplicador in-game).
- Q_one = sum S*BidSize(m) + sum S*AskSize(m')  ; Q_two = sum S*AskSize(m) + sum S*BidSize(m')   (m=token Up, m'=complemento).
- Q_min: medio en [0,10;0,90] -> max(min(Q_one,Q_two), max(Q_one,Q_two)/c), c=3,0 ; medio fuera -> min(Q_one,Q_two) (hay que cotizar los dos lados).
- Reparto: Q_normal = Q_min / sum_n Q_min_n por muestra; muestra = 1 libro por minuto (1.440/dia UTC); recompensa = pool_mercado * Q_final (Q_epoch normalizado). Minimo de pago 1 $.
## Supuestos NO verificables (se declaran, no se afirman)
A1. "punto medio ajustado por tamano" = punto medio simple (bb+ba)/2 del libro agregado (la doc no define el recorte exacto).
A2. min_size=50 es POR ORDEN; el libro L2 solo da tamano por nivel (puede agregar ordenes <50): se calculan dos variantes de masa rival: (a) todos los niveles (cota alta de masa rival), (b) solo niveles con tamano >=50 (cota baja).
A3. No se ve la composicion por participante: por participante Q_min_n esta en [(Q1+Q2)/6 , (Q1+Q2)/2] con medio en [0,1;0,9] (max/3 >= (Q1+Q2)/6 ; min<=media). Masa rival R in [Qtot/6, Qtot/2], Qtot=Q1+Q2 agregado del libro SIN nuestra orden.
A4. Pool diario por mercado 5m = cap de agosto /31 dias /288 mercados (BTC 300k$, ETH/SOL/XRP 50k$ cada una = 200k$/4 -> NOTA: la doc lista HYPE tambien, 'SOL,ETH,HYPE,XRP' 200k$/4). Programa 'ended' segun la doc; es SOLO escenario de referencia.
## Medidas
M1 (hecho, API publica): rewards.rates / rewards_config / rate_per_day de mercados 5m vivos BTC/ETH/SOL/XRP (clob /markets/{cid}, /rewards/markets/{cid}) con control positivo (mercado con rate_per_day>0).
M2 (libro5_ms 24-Oct tramo final y 26-Oct 22:21-24:00Z): para mercados 5min BTC/ETH/SOL/XRP, muestras en cierre-300+30+60k s (k=0..4): medio, Qtot rival (variantes a/b), con v=4,5.
M3: nuestra cotizacion hipotetica: bid de 50 acciones en la mejor puja (s=medio-bb) y en medio-1c, un solo lado (Q_our = S*50/c). cuota = Q_our/(Q_our+R) con R en [Qtot/6,Qtot/2] (rango bajo/alto de cuota).
M4: ingreso/mercado = pool_escenario * cuota * f (f=1 presente toda la vida; la fraccion real de puntuacion la da la muestra de 5 puntos).
M5: coste AS = 50 acc * 0,045 $ = 2,25 $ por relleno (medido RESULTADO_FRENTE_27oct: -4,5..-5,2 c/acc); p(relleno) NO medida para cotizar cerca del medio -> se reporta el p* de equilibrio = ingreso / 2,25.
Criterio: pool*cuota >= AS por mercado solo si p* >= p(relleno) plausible; con pool=0 medido la respuesta es NO sin mas calculo.
