# PREREG CF1 — CARRY-FAV-5M fase 1: ¿ganan fuera de muestra los rellenos maker PROFUNDOS en el favorito (≥0,70), y por qué? (5m, 6 monedas)
Congelado 26-Oct-2026 (polymarket-quantum-alpha-miner, programa BANDA-0-0,30 ampliado). Escrito ANTES de calcular ninguna clase de profundidad en el lado favorito y antes de ningún día de medida decisiva (≥27-Oct). Lo ya visto está en §7. Cambios posteriores = CF1b con días frescos nuevos; aclaraciones solo en ADENDA con sha.
En términos de la banda 0-0,30: pujar el favorito a q ≡ PEDIR (vender) el token barato a 1−q. CF1 es el lado CORTO de la banda, el que ocupan las dos ganadoras reales.

## 1. Decisión que se evalúa
Mantener pujas maker en el token FAVORITO (precio de compra equivalente pc ∈ [0,70; 0,99)) k ≥ 2 ticks por debajo del mejor bid, en reposo (sin cancelación rápida), de modo que solo se rellenen cuando una orden tomadora barre ≥3 niveles. La fase 1 mide en la POBLACIÓN on-chain el EV de los rellenos con esa firma; NO mide nuestra captura (fase 2 con la etiqueta virtual calibrada [pes, opt]; fase 3 micro-real con OK de Javi).

## 2. Mecanismo, pagador y predicción diferencial
Pagador: el flujo agresivo que barre hacia el longshot (tomadores que compran el barato atravesando niveles: compradores de lotería; las perdedoras persistentes pierden −0,196 €/€, 0/9 días +) o que vuelca el favorito (stop-loss, cierre de inventario). La puja profunda del favorito es la liquidez que ese flujo consume. Persiste: sesgo de lotería estable día a día; niveles profundos finos; el capital por acción del favorito (0,70-0,99) disuade a los makers pequeños. Hipótesis de asimetría: el barrido HACIA el longshot es desinformado y el barrido HACIA el favorito es informado (explicaría a la vez que B pierda pujando hondo en el barato y que W/MM ganen pujando hondo en el favorito).
Predicciones frente a H0 (profundo = top = población ≈ 0, como el agregado 5m ≥0,90 +0,003 de f3_carry):
(a) EV(DEEP) > 0 y > EV(TOP) en días frescos; (b) la ventaja de DEEP se concentra en contraparte MINT (el tomador COMPRA el barato complementario) frente a CRUCE (el tomador VENDE el favorito); (c) control asimétrico: en el lado barato 0,05-0,30 los rellenos DEEP no ganan más que TOP, y EV(DEEP favorito) − EV(DEEP barato) > 0.
No es rebautizo: f3_carry midió la población entera y pujas virtuales AL TOP al final de la cola (5 acc, vida 60 s), nunca la clase de profundidad en el barrido; «maker de un solo lado» y H26 mezclan clases; la R1 de `replica_ganadora` (ADENDA 2) es el lado barato (<0,40, BTC) con edad y alta por libro5; carry de 15m (FAV-15M-ETH) es otra misión.

## 3. Datos y definiciones
- Rellenos: `/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_D.csv.gz`; relleno maker = fila F con `taker` ≠ exchange 0xe111… (convención de `mapa_escala`), dedup tx+log_index; mapa token → (moneda, mercado, lado, cierre) = tokmap ∪ filas k (nunca `mapa_escala/tokens.json`). Compra equivalente (venta a q = compra del contrario a 1−q). Banda favorita pc ∈ [0,70; 0,99); T = cierre − ts_est ∈ (5; 300] s. Fuera pc ≥0,99 y T ≤5 s (congelación / «ya decidido»). Se excluyen los rellenos de la wallet dedicada 0x659a…297F.
- Profundidad en el barrido: dentro de la misma orden tomadora (misma tx y mismo grupo de casación; si la tx tiene varias filas M, se separa por la secuencia de log_index entre filas M, igual que `cola_vs_cruce/scripts/p1_pop.py`; cualquier desviación va al diff), L = nº de niveles de precio (ticks distintos) de rellenos maker del mismo lado económico estrictamente MEJORES (más caros para un comprador) que el de este relleno. TOP: L = 0; MID: L = 1; DEEP: L ≥ 2.
- Contraparte: de la fila M de la orden tomadora: MINT = el tomador compra el token complementario (barato); CRUCE = el tomador vende el mismo token (favorito). Indeterminable ⇒ missing (se reporta la tasa).
- Desenlace OFICIAL (`maker_ms_desenlaces_cache.json` ∪ gamma `closed=true`), cobertura ≥99 % del € por moneda × día o se excluye y se declara. EV = Σpnl/Σcoste (ponderado por €) y también por unidad mercado-lado-clase; pnl/acc = 1{gana} − pc; maker sin comisión; rebate aparte (0,014·pc·(1−pc)/acc; no entra en el gate).
- Control lado barato: misma definición con pc ∈ [0,05; 0,30).

## 4. Periodos
VISTO (§7). DESC 05..25-Oct: descriptivo, se publica ANTES de la primera mirada fresca y no decide. FRESCO = días UTC completos ≥27-Oct con el m5_onchain del día y del siguiente: DECIDE. Miradas a 10, 20 y 30 días frescos (≈06-Nov, 16-Nov, 26-Nov); entre miradas solo n y cobertura.

## 5. Gate (FRESCO, en cada mirada)
Celdas decisivas (K=2): A = ALL [0,70; 0,99) DEEP; B = BTC [0,90; 0,99) DEEP.
PASA si TODO: ≥10 días frescos; en A y en B: EV(DEEP) ≥ +0,02 con IC90 bootstrap por DÍA (2.000, semilla 20261026) inferior > 0, IC90 por CIERRE (1.000) inferior > 0 y test de signo por días (permutación de signo del EV diario ponderado, 10.000) p < 0,01; en A: EV(DEEP) − EV(TOP) con IC90 por días inferior > 0; EV(DEEP) sin los 2 mejores días > 0 en A y en B; EV(DEEP) > 0 (punto) en ≥4 de las monedas con ≥200 unidades DEEP; cuota de DEEP en el € maker de la celda ≥2 % (si no: PASA_SIN_CAPACIDAD).
REFUTADA si en A y en B el IC90 por días superior de EV(DEEP) < +0,01 (en cualquier mirada ≥10 días). INSUFICIENTE en otro caso (qué falla y fecha de la siguiente mirada; nada se reajusta).
Lecturas de mecanismo (descriptivas, BH-FDR entre ellas, no deciden): EV(DEEP∩MINT) − EV(DEEP∩CRUCE); EV(DEEP favorito) − EV(DEEP barato); sub-bandas 0,70-0,80 / 0,80-0,90 / 0,90-0,95 / 0,95-0,99; T (5,60] / (60,150] / (150,300]; por moneda; tamaño del relleno; cuota del € DEEP cuyo tomador es perdedora persistente (lista D−7..D−1 de `ganadoras_persistentes/scripts/a3_perdedoras.py`); clase ON/MEDIO/OFF de BR1; con y sin W (0xb0f85baa…) y MM (0x32ed2e54…) en la población.

## 6. Salvaguardas y colas
Pagos asimétricos (gana 1−pc, pierde pc): se reportan la pérdida por cierre (distribución, peor cierre, peor día en €), el EV sin el 1 % mejor de unidades y con el peor cierre duplicado (estrés), y el racimo (cierres con ≥2 monedas falladas). IC por día y por cierre; EV ponderado por €; cobertura y missing declarados; sin reloj WS en la definición (solo on-chain); un resultado espectacular es primero un bug. Ningún resultado de CF1 autoriza dinero ni cambia B.

## 7. Ya visto (declarado)
`mapa_escala` 06-21 Oct (5m ALL 0,70-0,90 −0,006; 0,90-0,99 +0,007; BTC 0,90-0,99 +0,007); `f3_carry` 06-24 Oct (5m ALL ≥0,90 +0,003; pujas virtuales fin de cola pes −0,035/−0,071, opt +0,005/+0,009); `wallet_mecanismos_26oct` (MM 0,70-0,90 OOS +0,036, ≥0,90 +0,064; W ≥0,90 +0,034, 7/7 días); R7a (maker frente a perdedoras +0,034); `replica_ganadora` ADENDA 2 (24-Oct: órdenes rellenas de W ~5 s de edad, 2-4 ticks bajo el mejor bid). Nunca se ha calculado la profundidad en el barrido ni MINT/CRUCE en el lado favorito. Ningún dato ≥27-Oct.

## 8. Recursos, entregable y fases siguientes (no prerregistradas aquí)
Un trabajo pesado a la vez; `nice -n 19 ionice -c3`, `ulimit -v 3000000`; nunca 06:00-09:30Z; load5<8 (autorización de Javi 26-Oct) y MemAvailable>2,5 GB; checkpoint por día. Código en `experimentos/5m_barato/banda_0_30/cf1/` (diff y sha). Entregable `alpha_miner/banda_0_30/RESULTADO_CF1.md`.
CF2 (tras CF1 ≠ REFUTADA y la calibración de `calibracion_etiqueta` con veredicto): pujas virtuales k = 2-4 ticks bajo el mejor bid, vivas ≥5 s, 5 acc, sobre libro5_ms en días frescos, intervalo [pes, opt] calibrado. CF3: micro-real en la dedicada (una orden de 5 acc a ~0,90 ≈ 4,5 € de exposición), con /code-review y OK de Javi.
