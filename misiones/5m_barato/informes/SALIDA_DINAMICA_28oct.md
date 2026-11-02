# SALIDA DINÁMICA CONDICIONADA de B (ejecutado 27-Oct 17:40Z). Veredicto: REJECTED (no hay salida condicionada con EV>0); micro-canal «valor residual» EXPLORATORY, despreciable y no ejecutable. Beneficio validado: 0 €.
Código/prereg/salidas: experimentos/5m_barato/salida_dinamica_28oct/{PREREG_SALIDA_DIN.md, eval_sal.py, extras_sal.py, eval_sal_salida.txt, extras_sal_salida.txt, HASHES.txt}. Solo lectura sobre units/ del alpha miner (alpha_miner_b_27oct, sim.py ADENDA1, reloj de RECEPCIÓN), 22 días 05-26 Oct, 31.138 posiciones P rellenadas (IS 05-22 n=25.427; OOS 23-26 n=5.711), desenlace oficial 99,8 % (76 sin desenlace de 50.154).

## Qué se probó (prereg con sha antes de calcular; A30 era la única regla con derecho a veredicto)
Salida = venta tomadora al bid (llegada +250 ms, comisión 0,07·p(1−p)); Δ = q·(bb − fee − g). Las unidades solo guardan DOS sondas post-relleno: tx+250 ms (I1) y T−30 s (A30). Etiqueta pesimista = Δ pareado + HOLD pesimista del validador (cola estricta IS −0,015 / OOS −0,046).

## Resultados (EV ponderado por €, Σpnl/Σcoste; IC90 bootstrap por días)
- HOLD (reproduce R1): IS +0,0004 (IC90d −0,025/+0,025; 8/18 días+), OOS −0,0318. Real on-chain −0,072 (n=202).
- I1 «vender ya» a tx+250 ms: IS −0,1164 (IC90d −0,121/−0,112; 0/18 días+; sin 2 mejores −0,118), OOS −0,1263 (0/4). 38 celdas de estado (moneda, causa A/B, parciales, Te, spread, v60, hora, espera, nivel de bid, Δbid): 0 con IC90d>0, max-statistic p=0,996. Calibración: el acierto supera al bid en 0,7-1,7 c en todos los tramos (bid 0,160→0,175; 0,255→0,272) ⇒ salir paga semiespread+comisión (−0,018/−0,031 por acción).
- A30 «sin rebote → vender al bid a T−30 s, si no mantener»: EV total IS +0,0028 (IC90d −0,023/+0,028; 9/18; sin 2 mejores −0,010), OOS −0,0291 (IC90d −0,143/+0,093). Δ vs HOLD pareado: IS +0,0024 (IC90d +0,001/+0,004; 14/18 días+; sin 2 mejores +0,0019), OOS +0,0027 (IC90d 0,000/+0,004; 3/4).
- EV total PESIMISTA A30: IS −0,0126 (IC90d −0,014/−0,011), OOS −0,0433; sobre el −0,072 on-chain: −0,070. No cumple EV>0 en ningún caso.
- De dónde sale el Δ: cola con bid ≤0,02 (n=4.023 de 31.138; 7 ganadoras = 0,17 % frente a bid 0,9 %; 16.215 acciones; ΣΔ +106,7 $ = +0,0033 €/€). NS con bid >0,02 (n=235): −25,9 $. Total +80,7 $ en 22 días = +3,7 $/día a escala sim (todas las unidades elegibles; a escala B real, céntimos/día). Positivo en BTC/ETH/SOL/XRP/DOGE (+0,0016..+0,0051), BNB −0,0001.
- Cota oráculo del canal (vender TODO perdedor, 77,2 %, a 0,01 en T−30 s sin vender ganadoras): +0,0317 €/€; A30 capta el 7,8 %.
- Placebo/inversión NO discriminables con las sondas guardadas (NS∪PS es 95 % NS: placebo +0,0188 vs NS +0,0196, 22 % de los placebos ≥ NS; inversión PS n=161 +0,0046 IC −0,029/+0,035; OOS n=57 degenerado). El Δ procede del nivel de bid (suelo de 1 c), no del «rebote».
- Fill-ability de salida: I1 bs≥restante 95,7 % (q/restante 0,979, n=30.430); A30 91,5 % (0,957, n=4.258); 6.537 de 31.138 (21 %) con libro rancio >30 s a T−30 s (sin bid conocido). 5 acc × 0,01 = 0,05 $, bajo el mínimo de 1 $ del CLOB documentado en CLAUDE.md (no reverificado aquí) ⇒ canal inejecutable al tamaño de B.

## Razón estructural
Δ(salida tomadora) = q·(bb − fee − g) solo es >0 si el bid supera la probabilidad condicional de ganar en más que la comisión; el mercado está calibrado al mid (acierto ≈ mid > bid), así que salir cuesta 2,4-3,1 c/acc (−0,117 €/€, 22/22 días). La salida maker cobra a informados (convexidad, X1 −0,22, alpha miner). Con precio ≈ martingala, parar no cambia el EV bruto (optional stopping) y los costes son >0. La única anomalía (suelo de 1 c en fichas muertas, comisión ≈0) tiene techo +0,032 €/€ < hueco a EV>0.

## No probado (declarado)
Instantes intermedios y retorno Binance post-relleno (fase B: re-ejecutar sim.py con sondas por T_rem y Binance, ≈37 min CPU, 5 llamadas; valor de información bajo, no recomendada); fills reales (n=202/364: sin potencia); etiqueta de entrada optimista (cabeza de cola; el Δ pareado no depende de ella); libro rancio 21 % (subestima la cola, no cambia el techo); decisión con bid de EJECUCIÓN (≤250 ms de ventaja) en las celdas EX; salidas maker condicionadas.

## Reabrir solo si
Alguna clase de estado con bid − fee − acierto ≥ +0,02/acc medida con el libro de DECISIÓN, n≥750 posiciones, ≥10 días e IC90 por días>0, o B real ≥750 rellenos nuevos (PREREG_TRANSFERENCIA) con contribución de salida >0. La palanca de B sigue siendo la entrada (sin selección adversa y EV>0), no la salida.
Reproducir: cd experimentos/5m_barato/salida_dinamica_28oct; nice -n 19 ionice -c3 python3 eval_sal.py > eval_sal_salida.txt; python3 extras_sal.py > extras_sal_salida.txt (≈1 min, <3 GB).
