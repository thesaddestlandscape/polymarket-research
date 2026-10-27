# F8 ESTRUCTURA — prereg (escrito 24-Oct 12:55Z, ANTES de calcular ningún EV de política; solo se ha visto un smoke test de 1.056 vidas del 23-Oct, sin agregar pnl)
Pregunta: ¿existe una política de INCLUSIÓN de pujas B (qué pujas colocar) basada solo en información ex ante (marca de recepción) cuya contribución por € comprometido supere a colocar todas, fuera de muestra y por días?
## Unidad y etiqueta
- Unidad = puja VIRTUAL viva (copia ampliada de `detector_ex_ante/scripts/vida_puja_virtual_5m.py`: 5 acc al mejor bid b∈[0,10;0,30], T∈[60;300] s, una cada 10 s por token 5m, vida 60 s, cola delante Q0=bs; relleno PESIMISTA = prints SELL del token ≤b + BUY del complementario ≥1−b ≥ Q0+5).
- Etiqueta L2: y = pnl de 5 acc (desenlace oficial, fee maker 0, sin rebate) si relleno_pes, 0 si no. Contribución por € = Σy/Σ(5·b). Se reporta también P(relleno) y EV|relleno por € (Σpnl/Σcoste).
- Universo principal: ETH, SOL, XRP (universo de B). BTC/DOGE/BNB solo descriptivo (réplica, no decide).
## Rasgos (todos anteriores a t0 por recepción)
- P0 ESTRUCTURA: b, T, hora UTC, moneda, lado, fin de semana.
- P1 = P0 + libro/Binance: ba, as_, spread, Q0, log Q0, bn_r300ms, bn_r5s, bn_r60s (con signo del lado), bn_rng60, bn_edad.
- P2 = P1 + flujo: edad del último print del mercado, n/usd de prints 120 s, n/usd/edad de prints CONTRA la puja (SELL del token o BUY del complementario), y composición on-chain del flujo tomador en [t0−130, t0−10) s del mercado (usd total, usd de tomadores ≥200 y ≥2000 órdenes en 96 h, shares; clase ex ante como F6 e2).
## Modelo y política (congelada por día ANTES de evaluar el día)
- HGB regresión (prof. 3, 200 it., lr 0,05, hoja ≥300, l2 1,0, semilla fija) sobre y/(5b) ponderado por 5b; walk-forward expansivo: entrena días < d (mín. 3 días), evalúa d.
- Política: retener las pujas con score ≥ cuantil del TRAIN que retiene el 30 % del € (fijado a priori; 10 % y 50 % solo descriptivos).
- K declarado = 3 (P0, P1, P2) × 1 nivel = 3 → Bonferroni unilateral α 0,10/3 (z≈2,13 sobre t por días).
## Métricas y gate (por modelo, días de evaluación ≥16-Oct)
- exceso € = Σy(retenidas) − f_€·Σy(todas) del día (= frente a placebo esperado que retiene el mismo € al azar); placebo por permutación dentro de día×moneda×hora (500); inversión (30 % inferior).
- PASA si: exceso total >0, IC90 bootstrap por DÍAS >0, t por días ≥2,13, sin el mejor día >0 y sin 2 mejores >0, ≥60 % días >0, IC90 por cierre >0, placebo p<0,05, inversión <0, y se mantiene en días laborables solos y con placebo estratificado moneda×hora. EV|relleno por € de lo retenido ≥ EV|relleno total (ataca la AS, no solo P(relleno)).
- P2 solo «añade» si su exceso supera al de P1 con IC90 por días de la diferencia >0.
- Comparación (no reentrena): detector congelado M1F aplicado a las vidas RELLENAS (rasgos ausentes en vidas virtuales = NaN, «M1F degradado»), top por su corte_ev congelado; M2 DATA_BLOCKED.
## Falsador
Si ningún modelo pasa → no hay política de inclusión desplegable con estos rasgos; se reporta el techo (mejor exceso e IC) y no se registra forward.
