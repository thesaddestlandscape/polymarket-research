# Mecanismos de W (pspspsps5 0xb0f85baa…) y MM (mo-money 0x32ed2e54…) — 26-Oct-2026 · EXPLORATORY · PARTIAL
Solo lectura (archivo on-chain `VOL/m5_onchain`, R_D de ganadoras_persistentes validado al céntimo contra la caché de mo-money del 10-Oct,
cachés de wallet_pspspsps5, polybolt twap60 source=chainlink). Desenlace oficial: cobertura 100 % en todo. EV = Σpnl/Σcoste, IC90 bootstrap por días.
Rebate = 20 % de 0,07·p(1−p) del tomador, ESTIMADO (no está on-chain). Rewards de liquidez: no observables en los fills.
Estado PARTIAL: H2-H4 del `PREREG.md` (sha256 89621a8f…, escrito antes de calcularlas) NO se han calculado: la extracción x1
(tx completas de ambas wallets, 05-25 Oct) sigue en segundo plano y `a1_ledger.py` está listo (ver §5). Tope de tokens alcanzado.

## 1. Tabla wallet × universo × periodo (unidad mercado-lado-rol; n5_salida.txt)
| wallet | periodo | coste $ | PnL $ (sin rebate) | EV | IC90 días | días+ | rebate est. |
|---|---|---|---|---|---|---|---|
| MM | SEL 06-14 | 692.428 | +10.264 | +0,015 | (+0,001,+0,027) | 7/9 | +2.400 |
| MM | **OOS 15-21** | 263.052 | **+1.634** | +0,006 | (−0,045,+0,041) | 3/7 | +1.040 |
| W | SEL 06-14 | 161.226 | +7.499 | +0,047 | (+0,014,+0,073) | 7/9 | +468 |
| W | **OOS 15-21** | 200.790 | **+5.438** | +0,027 | (+0,016,+0,039) | 6/7 | +544 |
MM: los 4 últimos días negativos (18-21 Oct: −1.073, −1.294, −978, −2.891 $). Su ventaja SE ESTÁ SECANDO; W persiste.
5m de las 6 monedas mezcladas en R_D (sin activo); W ≈ BTC/ETH/SOL, MM ≈ 60 % BTC (caché 05-14).

## 2. Atribución por componente (hechos)
- **MM**: la única pata con ventaja es MAKER comprando el FAVORITO 0,70-0,90 (SEL hit 0,838 vs p 0,799, +20,7 k$, IC>0, 8/9 d; OOS +0,036
  IC (+0,004,+0,058), +3,4 k$) y ≥0,90 (OOS +0,064, 7/7 d). Sus compras maker baratas por UNIDAD pierden (≤0,10 −0,49/−0,43; 0,10-0,30
  −0,15/−0,16) aunque por RELLENO salgan +0,29 (n2): promedia a la baja (mismo artefacto relleno≠unidad que W). Su toma (rol T) pierde
  (0,30-0,70: −0,094 SEL, IC<0) = la 2ª pata para «completar pares» → pares −12,2 k$ SEL / −3,8 k$ OOS, comisión −3,8 k$/−0,9 k$.
  Rebate estimado ≈ 23 % de su PnL SEL y > su PnL OOS: sin rebate MM es ≈0 en OOS.
- **W**: 100 % maker, 0 ventas. Unidades 0,10-0,30 +0,51 SEL / +0,13 OOS (IC cruza 0); carry ≥0,90 +0,017 / +0,034 (IC>0, 7/7 d);
  tickets <0,10 por unidad ≈0 (por relleno +0,3: escalera). Rebate +0,3 % del coste: irrelevante.
- **Rasgo común** (inferencia fuerte): ambas ganan como maker en el favorito tardío donde la POBLACIÓN maker está en ≈+0,003 (f3_carry) y
  una puja nuestra a final de cola pierde −0,035/−0,071 (f3_carry P2). Es decir, su ventaja es de RELLENO (no les llega el flujo informado),
  no de predicción: replica_ganadora (adenda 2, 24-Oct) vio sus órdenes rellenas más VIEJAS (~5 s vs 0,5 s) y 2-4 ticks bajo el mejor bid.

## 3. Hipótesis rivales probadas hoy (además de H-A..H-E y señales externas ya refutadas)
| H | test | resultado |
|---|---|---|
| NIDO-15m (info del 15m/bid15, lado s por TWAP oficial) | n1 W 05-23 vs población; n2 MM 05-14 | **REFUTADA**: cuota $ en s = 0,50-0,51 (W), 0,52/0,32/0,44 (MM); W infra-pondera los 5m anidados (21-25 % vs 33 %). |
| Velocidad/precio rancio como tomador | rol T de MM | **REFUTADA**: sus tomas pierden (−0,09 a −0,37 por €); W nunca toma. |
| Contraparte/barrido compartido W-MM | n3/n4 05-14 | «mercado compartido» +1,26 vs −0,39 era LOOK-AHEAD (MM entra después cuando el barato vuelve: +4,65). Ex ante (MM ≥3 s antes) W +0,36 vs «aún no» +0,34-0,39 → no explica W. Lead post hoc población BTC <0,10 con MM antes +0,117 (IC +0,014,+0,22) vs −0,122 → H3 prereg. |
| Rebate/tier | n5 | No es la fuente de W (0,3 %); en MM es ~todo su OOS. |
| Rewards de liquidez | — | No puede explicar el EV de los fills (medido sin rewards); W casi nunca tiene ambos lados (|Y−N|/(Y+N)=1). Inidentificable con datos públicos. |
| Selección horas/monedas | previo | Horas uniformes (W); no identifica. |
| H2 tipo de contraparte (CRUCE vs MINT), H3 MM-presente OOS, H4 MM-favorito OOS 22-25 | PREREG | **PENDIENTE** (x1 + a1). |

## 4. Veredictos
- **MM: IDENTIFICADO (componentes) — NO REPLICABLE / SECÁNDOSE.** Fuente = maker en el favorito 0,70-0,99 + rebate; pierde en pares y tomas.
  OOS +0,006 (IC cruza 0), últimos 4 días negativos. Copiar su estructura de pares es el cementerio (pares 5m maker −0,050). 0 €/año.
- **W: IDENTIFICADO_REQUISITO_NO_CUMPLIDO (parcial, inferido).** Fuente = calidad de relleno como maker (no selección adversa) en carry ≥0,90 y
  0,10-0,30, persistente OOS. Requisito para replicar: que nuestras pujas no sean el final de la cola que recibe el flujo informado; nuestra puja
  virtual a final de cola pierde −0,035/−0,071 y la cancelación mínima medida (60-65 ms) no ha mostrado discriminar (E1/BN_W300 REJECTED).
  Requisito cuantificable solo con micro-órdenes reales (edad de orden ≥5 s, 2-4 ticks bajo el mejor bid; OK Javi + /code-review). €/año hoy 0;
  techo honesto a escala W en carry (OOS +4,1 k$/7 d con 121 k$ de coste) exige ~17 k$ de capital rotando/día: fuera de la dedicada de 5 €.
- Lo que refutaría la lectura «relleno»: que H2 muestre la ventaja de W concentrada en una clase de contraparte (sería QUIÉN paga, no cómo se rellena).

## 5. Reproducción, hashes, warnings
Scripts en `scripts/`: x1_extraer.sh (en curso, log `/root/polymarket-research-datalogs/wallet_mecanismos_26oct/x1.log`, salida tx_D/k_*),
a1_ledger.py (tras x1), n1_nido.py, n2_nido_mm.py, n3_solape.py, n4_previo.py, n5_persistencia.py; salidas n1..n5_salida.txt; hashes en HASHES.txt.
Todo `nice -n 19 ionice -c3 python3 -W ignore`, `ulimit -v 3000000`. x1 espera load5<8 y MemAvailable>2,5 GB fuera de 06-09:30Z (autorización Javi 26-Oct).
Warnings: R_D sin comisión (estimada) ni activo; rebate estimado; n1/n2/n3/n4/n5 son post hoc (no preregistrados); n3/n4 «mercado compartido» y «MM nunca» usan futuro.
