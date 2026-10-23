# PREREG W1 tendencia/régimen para B (23-Oct-2026). Congelado ANTES de calcular ningún EV por tendencia.
Solo lectura. Entradas: `../cola_posicion/datos/pop_units_*.csv.gz` (población ETH/SOL/XRP 5m, 0,10-0,30, T 60-300, 5 acc por maker-mercado-lado, sin B; 17-22 Oct),
`../salida/datos/unidades_b.csv` (B real, 175 posiciones), `../salida/datos/ms_D.npz` (Binance con RECEPCIÓN, libro 5m/15m, prints), `../../pares_huecos/datos/fills_alts.csv.gz` (fills on-chain de wallets).
## Parte 1. Indicadores (todos causales; t0 = hora on-chain del relleno − 5 s en población; B: t_det − 4 s, o primer_fill_chain − 5 s si falta t_det [marcado]).
Todos orientados al lado COMPRADO (sgn=+1 si compra YES/Up, −1 si NO/Down). CON = indicador a favor del lado comprado (>0), CONTRA (<0), 0/NaN = missing (no se cuenta como CONTRA).
- I1 (PRIMARIO) r300: retorno Binance del subyacente en [t0−300 s, t0], en bps, × sgn.
- Secundarios: I1b r60, I1c r900, I1d rop (desde apertura de la ventana 5m: fin−300 s), I1e rpre (900 s ANTERIORES a la apertura de la ventana = régimen previo puro).
- I2 b15: mid del token del MISMO lado en el 15m que contiene la ventana (último top con recepción ≤ t0) − 0,5. Secundario I2b: Δmid15 en 300 s.
- I3 f60: flujo tomador neto de los prints del mercado 5m (ambos tokens, equivalente-Up: BUY YES +, BUY NO −, SELL al revés, por acciones) en [t0−60, t0] × sgn.
## Contrastes (población; B descriptivo)
Estratos de placebo: dia × act × lado × cubo de precio pc (0,05). Estadístico: Δ = EV(CON) − EV(CONTRA), EV = Σpnl/Σcoste (ponderado por €).
- Descubrimiento 17-19, TEST 20-22. «Separa EV» solo si, para el indicador: signo de Δ en TEST igual al de DESC, IC90 por CIERRE (fin) del TEST excluye 0, p placebo-estratos (una cola, en el sentido del DESC) <0,05, p max-estadístico entre los 8 indicadores <0,10, y ≥4/6 días con el mismo signo. IC90 por día se reporta pero con 3-6 clusters NO decide.
- Refutado si Δ en TEST tiene signo opuesto o IC90 por cierre incluye 0.
- Regla de uso (skip): quitar la clase CONTRA (o CON, la de peor EV en DESC) → Δ PnL total en €, EV retenido, % de coste quitado, placebo de quitar la misma fracción al azar dentro de estratos; el EV mejora sin que el PnL total suba NO es mejora.
- B real: mismas clases, n por clase; bootstrap por cierre; con n<40 por clase NO se concluye (solo descriptivo).
## Parte 2. Wallets (maker, rol M, lado_ef = token largo efectivo, px_ef = px si BUY, 1−px si SELL), 17-22 Oct:
0xf074dc84, 0x0ab01745 (ETH). Elegidas por Javi, no por resultado de este análisis. BTC 0x21f4c1a1 solo si hay tiempo (otro npz).
- (a) Cuota de fills CON tendencia (por indicador) de la wallet frente a la esperada con la cuota de los OTROS makers de alts en el mismo estrato (dia, act, T en cubos de 60 s, px_ef 0,05): diferencia e IC90 por cierre.
- (b) Tamaño medio de fill y nº de fills por (mercado,lado) según CON/CONTRA. (c) EV por € de sus fills CON vs CONTRA (ponderado, IC por cierre) frente a los de otros makers en mismos estratos.
- Cancelación/recotización no se observan (solo fills): inidentificable. Se declara.
Fecha/commit: 23-Oct-2026, antes de cualquier cálculo por tendencia.
