# PREREG wallets_ballenas_b (25-Oct-2026 ~11:15Z) — congelado ANTES de calcular ningún EV/desenlace
Agente: cheap5m-wallet-intelligence-analyst. Solo lectura. Datos: m5_onchain (VOL) 06..21-Oct (5m, 6 monedas; filas F con maker/tomador explícitos),
tokens/desenlace oficial `DL/mapa_escala/{tokens,des}.json` (cobertura 06-21 = 100 % de mercados 5m). 22-24 Oct excluidos (sin mapa/desenlace).
NO se usan wallet_edge_score*/smart_money_consensus/ballenas_timing para seleccionar: se calculan con datos que incluyen el periodo de prueba (circular).

## Poblaciones
- M = fila con taker != exchange (fill MAKER; campo maker = wallet maker, campo taker = wallet tomadora). Venta convertida a compra del complementario (pc=1-p).
- T = fila con taker == exchange (orden TOMADORA propia; campo maker = wallet tomadora, fee = comisión pagada). Misma conversión.
- P (población de prueba) = fills M con pc en [0,05, 0,30] (banda de B), sec desde apertura en [0,300]. EV ponderado por € = Σpnl/Σcoste, pnl = acc·1{gana lado} − coste (maker fee 0). Rebate separado: 0,014·(1−pc)·coste (inferido; suelo 1 €/día/wallet ⇒ se reporta aparte, no suma al EV principal).
- Unidad de EV/IC = (mercado, lado, celda) agregando makers; IC90 bootstrap por DÍA (2000) y por CIERRE; "sin 2 mejores días".
- DESC = 06..11-Oct (6 d) solo para seleccionar; HOLD = 12..21-Oct (10 d) solo para medir.

## H1 (primaria, ángulo b: señal ex ante de wallets para CANCELAR) 
- Conjunto S (fijado en DESC): wallets tomadoras (filas T) con ≥30 unidades (wallet,mercado,lado), coste ≥200 $, EV neto de fee ≥ +0,03/€, y pnl>0 en ≥2/3 de sus días activos (≥3 días activos).
- Señal para un fill f (mercado m, maker compra lado s, bloque tf): F_S = Σ coste de compras (convertidas) de S en m del lado opuesto a s − Σ de S del lado s, con bloque en [tf−33, tf−3] s. Bandera = F_S > 0.
  Latencia: identidad+dirección disponible por RTDS ≈ casado+0,9 s ≈ bloque−1,5 s; nuestro relleno casa ≈ tf−2,4 s ⇒ margen ≥2 s para cancelar (65 ms). Ventana acaba en tf−3.
- Métrica primaria (HOLD): EXCESO = EV€(no bandera) − EV€(todo P); secundaria Δ = EV€(bandera) − EV€(no bandera).
- PASA si TODO: n unidades bandera ≥40 en ≥10 días; EXCESO>0 con IC90 por días >0 y por cierre >0; EXCESO>0 sin 2 mejores días; p placebo < 0,05/3 (placebo = 500 conjuntos aleatorios del mismo tamaño |S| extraídos de tomadoras con la misma actividad mínima pero SIN filtro de EV; estadístico Δ); top-1 wallet de S ≤30 % del coste bandera; mismo signo en BTC y en ALT.
- Controles (descriptivos, no deciden): bandera con TODAS las tomadoras (F_all>0); inversión (S con EV ≤ −0,03 = "malas").
- Secundario H1-WF: S re-seleccionado walk-forward (días < d, mismos umbrales), medido en 09..21.

## H2 (ángulo c: nichos donde los makers PASIVOS ganan)
- Celdas = moneda(6) × franja UTC (0-6,6-12,12-18,18-24) × banda (0,05-0,15, 0,15-0,30) = 48. En DESC: EV€ por celda, t por días; seleccionar EV>0 y BH-FDR q<0,10.
- HOLD: EV€ de la UNIÓN de celdas seleccionadas. PASA si n≥40 unidades, ≥10 días, IC90 por días >0, sin 2 mejores días >0, > p95 de 1000 uniones aleatorias del mismo nº de celdas (p<0,05/3), y la inversión (peores celdas DESC) no sale igual de positiva. Si 0 celdas seleccionadas ⇒ H2 = sin candidata (se reporta tal cual).
- "Pasivo" = toda la población maker; variante descriptiva: makers con ≤5 órdenes distintas por unidad.

## H3 (ángulo a, DESCRIPTIVO, K declarado, no decide)
- EV€ maker por moneda × lado (Up/Down) × banda (0,05-0,15/0,15-0,30) × T restante (0-60,60-120,120-240,240-300 s), DESC y HOLD; persistencia = Spearman ponderado DESC↔HOLD de las 96 celdas; BH-FDR sobre HOLD.
- Posición de cola: NO testable con fills públicos más allá de log_index (medido 13-Oct: nadie va por delante): `missing`.

## Multiplicidad
K confirmatorio = 3 (H1, H1-WF, H2) ⇒ α = 0,0167 para p de placebo. H3 descriptivo. Anti-huérfana (qué pata se completa): NO testada aquí (cementerio de pares); declarado.
