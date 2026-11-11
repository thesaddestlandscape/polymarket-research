# PREREG_CXB60_FORWARD — BORRADOR (NO CONGELADO) — 11-Nov-2026
**Estado: BORRADOR del execution-engineer para que el validador estadístico lo revise, lo corrija y lo congele (sha256). Nada de esto es resultado ni alfa. Este documento no autoriza ningún envío de órdenes (ni reales ni de prueba); el dry-run solo simula.**
Fuente de la hipótesis: PASS_T_V3_RESULTADOS_11nov.md §5 (TRAIN 26-Oct..09-Nov, motor v3) y L_REAL_Y_DRYRUN_CXB60_11nov.md (curva EV(l), l real, brecha de nivel). Código: `dryrun/cxb60_core.py`, `dryrun/cxb60_dryrun_fase0.py`, `dryrun/cxb60_resolve.py` (hashes sha256[:16] en `run_manifest.json`).

## 1. Hipótesis (una sola, primaria)
**H-CXB60-FWD**: en mercados 5m de ETH/SOL/XRP (cada token YES/NO es una unidad de mercado, como en el motor), una orden virtual maker BUY GTC post-only de 5 acciones en L∈{0,10; 0,13; 0,16; 0,19} colocada con la regla B-CXB60 v1 (entrada: gate G0 [b15 finito, vol30≥26, hora UTC≥4, b15−L≤0,03] Y ask_rx>L Y bid_rx(t−300 ms)≥L+0,01; salida: bid_otros_rx<L con l=60 ms, o gate falso (+60 ms), o T≤61 s; re-armado con la regla de entrada) tiene EV ponderado por euro (Σpnl/Σcoste, rebate maker 0,2·0,07·L(1−L) incluido) **> 0** en el forward, y **mayor que el de su control GEO1** (misma colocación, sin cancelar).
- Fuera de hipótesis (descriptivo, no puertas): CXB35/100/150 (curva de l), G0, por moneda, por L.

## 2. Qué se mide (definiciones)
- Unidad de análisis: **cierre de 5 min** (`fin`; todos los tokens/monedas que cierran en el mismo `fin` = un clúster) y **día UTC**. El n de rellenos NO es n independiente.
- Relleno virtual: regla v3 del motor (`engine_v3.fill_segment_v3`, dedupe, cola BASE) con la cinta de prints WS (sello `ex−19−1`, supuesto declarado: sin firma exacta on-chain en vivo). PnL = q·(gana−L) + q·0,2·0,07·L(1−L); coste = q·L. Desenlace: OFICIAL (gmap sa_r1), cobertura ≥ 99 % de los rellenos; un relleno sin desenlace se excluye y se cuenta (missing ≠ 0).
- Relojes (CONTRATO_RELOJES): decisiones con RX; relleno/cancelación con EX; `t_arr = t_dec + 68 ms`; cancelación efectiva = rx del disparo + l.
- Variantes en paralelo (misma corrida, mismos datos): G0, GEO1 (control de igual colocación), CXB35/60/100/150 (l), placebo PLC60_s (20 semillas: mismo disparo que CXB60 pero cancelación en instante uniforme del segmento: igual cobertura, sin información del libro).

## 3. Puertas (todas deben cumplirse; ninguna se relaja tras ver datos)
G1 n ≥ 40 rellenos de CXB60 resueltos y ≥ 10 días UTC independientes con datos completos (cobertura diaria de mercados esperados/procesados ≥ 95 %, `coverage_<D>.json`).
G2 EV(CXB60) ponderado por € > 0 con IC90 bootstrap **por días** con extremo inferior > 0, y IC90 **por cierre** con extremo inferior > 0.
G3 Incremental vs GEO1 (Δpnl diario, misma colocación) > 0 con IC90 por días > 0.
G4 EV sin los 2 mejores días > 0.
G5 Placebo: p = (1+#{EV_placebo ≥ EV_CXB60})/(1+S) ≤ 0,05 con S ≥ 20 semillas (y el EV del placebo no puede ser ≥ 0 de forma sistemática: si PLC60 ≈ CXB60 la señal de cancelación no aporta).
G6 Concentración: ninguna moneda > 60 % del coste y ningún día > 25 % del PnL positivo.
G7 Sensibilidad a la cinta: re-simular los mismos ficheros ms offline con sello de cinta pesimista (`--once --files ... --c-print 59 --out OTRO_DIR`; defecto 19); el signo del EV no puede cambiar.
G8 Sensibilidad a l: EV(CXB100) no puede ser peor que −0,05 si CXB60 pasa (si solo pasa a l ≤ 45 ms, el resultado es «condicionado a l», no apto para ejecución sin medir d_proc).
Multiplicidad: contraste primario único (CXB60 agregado). Por moneda (3) con Bonferroni; curva de l y L descriptivas.
Resultado: PASS (todas), FAIL (G2 o G3 con IC90 superior < 0, o G5 refutado con n≥40), INSUFFICIENT (resto). **PASS no es «rentable»: solo habilita proponer a Javi un micro-ensayo real con tope de pruebas**, tras auditoría independiente.

## 4. Congelación y HOLD
- Congelar (sha256 de este fichero + hashes de código del manifiesto) ANTES de leer ningún dato forward. El forward cuenta solo desde el primer día UTC completo posterior a la congelación Y al despliegue.
- Los días ≥ 10-Nov son HOLD del programa TRAIN/HOLD de PASS_T_V3: no se usaron para ajustar nada; el forward es independiente de ellos. Lo que el dry-run observe en días previos a la congelación es exploratorio y no cuenta para las puertas.
- Sin ventanas de tuning: parámetros (L, size, TMIN, LAT_POST, l, SETTLE, c_print, gate) fijos = los del manifiesto.

## 5. Exclusiones y fallos declarados
Mercados `incompleto_arranque` (el lector arrancó menos de 32 s antes de la rejilla), `sin_comp`, `sin_token_15m`, `buffer_ausente`: excluidos y contados por día (no se rellenan con ceros). Reinicio del proceso: los mercados abiertos se reprocesan desde el principio del fichero ms; los ya escritos se saltan (idempotente, probado).

## 6. Debilidades conocidas que el validador debe sopesar (no verificado)
1. **l real**: delay efectivo de cancelación medido con n pequeño (4 anclas directas del canal de usuario; 39 en la carrera cancelación-vs-print de B real: δ≈40 ms, IC90 32–136); **d_proc** (disparo → envío del DELETE) no está medido en bucle; el dry-run no lo mide.
2. **Nivel de EV**: el motor sobre-estima la pérdida (−0,222 sim vs −0,061 real en verif_v3) y lo explica sobre todo por 12 falsos positivos de relleno (cancelación que gana la carrera): el EV del dry-run es un índice, no una previsión de euros.
3. **Cinta**: en TRAIN el 61 % del sello es de firma exacta y el 38 % es fallback; en el forward la cinta es WS con sello `ex−c_print−1` (sin libro5_tx) — no validada contra órdenes reales.
4. **«Bid sin nosotros»**: en un ejecutor real con la orden dentro del libro, `bid<L` nunca se ve (23 filas de 85.464); la regla `bid_otros = szb − r` acierta 87,0 % (454/522) como estado al cancelar sobre B real y necesita el canal de usuario para r exacto con parciales. En el dry-run no hay orden propia: el libro es limpio.
5. Fills por «toque» (precio llega a L sin traspasar) y cola: supuestos BASE de la cola; sin orden real no se valida.
6. Rebate maker 0,2 (verificado 07-Oct en gamma): no confirmado como cobrado en cada relleno de órdenes reales de B.
