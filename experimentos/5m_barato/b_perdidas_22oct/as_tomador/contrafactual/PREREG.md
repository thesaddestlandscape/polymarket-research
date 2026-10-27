# PREREG CONTRAFACTUAL SHADOW "tomadores informados" sobre B (OLA 8b) - redactado 24-Oct-2026 ~09:40Z
Estado de honestidad: los scripts `scripts/cf_lib.py` y `scripts/build_set.py` estan ESCRITOS pero NO EJECUTADOS al firmar este documento; el set se construye despues y su hash se anade en `PREREG_ANEXO_SET.md` (sin cambiar nada de lo definido aqui). Origen: VERIFICACION.md (revisor), contraste post-hoc de B "informados por ROI BRUTO>=2 %": EXCESO_B +0,267 (IC90 por cierre +0,039..+0,515), 24 tomadores, 105 fills. NO es prueba: es una hipotesis a replicar en dias nuevos. 100 % PASIVO: no toca B, `experimento_maker_h47.py`, live, config ni crons; solo lee.

## 1. Hipotesis
H_CF: en los rellenos REALES de B (wallet dedicada 0x659a40ff...), las unidades cuyo tomador esta en un set de tomadores "informados" (ROI bruto previo >= +2 %), fijado con datos hasta el 23-Oct 23:59Z, rinden PEOR que el resto, de modo que saltarlas (no cotizar/cancelar contra ellos) mejoraria el EV de B. Nula: EXCESO <= 0.

## 2. Sets CONGELADOS (datos hasta 23-Oct 23:59Z; hash en el anexo; se calculan UNA vez y no se tocan)
Fuente: `/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_YYYY-MM-DD.csv.gz` (filas `F` con taker != contrato 0xe111...; 5m ETH/SOL/XRP, TODAS las bandas de precio), mapa token->mercado de las filas `k` de `m5_registro` (D-1,D,D+1), desenlaces oficiales de `maker_ms_desenlaces_cache.json` (solo mercados resueltos; sin desenlace = excluido, no 0). Perspectiva del TOMADOR por fill: coste = sh*(1-pc), pnl_bruto = -(sh*gana - sh*pc), con pc/lado segun `verificacion/vlib.py`. Se excluye la wallet propia como tomador. ROI_bruto = sum(pnl_bruto)/sum(coste) por tomador.
- **SET_I (PRIMARIO)**: ventana 09..23-Oct; n_fills >= 30, coste_tomador >= 50 $, ROI_bruto >= +0,02. (Definicion pedida por el chief; ventana incluye 20-23 Oct, dias de B: por eso el desempeno de SET_I sobre 20-23 es EN MUESTRA y no cuenta.)
- **SET_V (REPLICA del verificador)**: ventana 09..18-Oct; n_fills >= 100, coste >= 200 $, ROI_bruto >= +0,02 (= `v3_B.py::inf_gro`, 370 tomadores; es el set que produjo el +0,267). El primario y la replica difieren porque el encargo describia el umbral como n>=30/coste>=50 pero el +0,267 se obtuvo con n>=100/coste>=200; se congelan AMBOS y se evalua cada uno por separado. K = 2 sets (alfa de decision de los p: 0,025).
- **POOL_I** (universo del placebo): tomadores con n>=30 y coste>=50 en 09..23-Oct (sin criterio de ROI).
Sensibilidad descriptiva (no gate): version neta de fee del tomador (0,07*sh*pc*(1-pc)) de SET_I.

## 3. Regla, unidad y metrica
- Flujo evaluado: fills reales de B = `movimientos.csv` (tipo COMPRA, experimento H47-B) de `experimentos/5m_barato/contabilidad_wallet_dedicada/` (solo lectura) con `fecha_utc` >= **2026-10-24T00:00Z**. Tomador de cada fill = `taker` de la fila `F` on-chain con maker == wallet dedicada y el mismo `tx` (en la verificacion: 215/215 casadas, 0 tx con >1 tomador, size y coste coinciden con el ledger). Fill sin tomador hallado = `sin_taker` (se cuenta y se reporta; nunca 0 ni se imputa).
- Resultado de cada fill: desenlace oficial de la posicion en `posiciones.csv` (`liquidada_ganada`/`liquidada_perdida`; payout/size). pnl_fill = size*gana - coste. Fills de posiciones sin liquidar = `pendiente` (fuera del calculo hasta resolverse; reportados). **Fee: B es MAKER, fee 0** (ledger `comision_est` 0, columna `fee` on-chain de la fila maker 0); el rebate del 20 % no se suma (conservador). La comision 0,07*p*(1-p) solo se usa en el lado tomador (definicion del set y su sensibilidad neta).
- **Unidad = (mercado, lado)** (posicion). **Bandera = el tomador del PRIMER relleno de la unidad (orden por fecha_utc, log_index) esta en el set.** Lectura descriptiva adicional a nivel de fill (bandera por fill).
- **EXCESO = EV_ret - EV_total**, EV ponderado por EUR = sum(pnl)/sum(coste); EV_ret = unidades NO banderadas (lo que B habria retenido saltando las banderadas); EV_flag = unidades banderadas; EV_total = todas. EXCESO > 0 significa que saltarlas mejora a B (sin efecto de sustitucion: cota optimista). Tambien se reporta la media por unidad (no ponderada).
- Cierre = cluster = epoch final del mercado (el sufijo numerico del slug); varias monedas en el mismo cierre son una sola apuesta.

## 4. Gates (TODOS, por set, evaluados SOLO con dias >= 24-Oct; el set no se retoca)
- G1 n >= 40 cierres con al menos una unidad banderada (y n_unidades_flag reportado).
- G2 >= 10 dias UTC independientes con >=1 unidad banderada y >=1 no banderada.
- G3 IC90 de EXCESO por CIERRE (bootstrap de clusters, 3000 reps, semilla 777) con limite inferior > 0.
- G4 EXCESO > 0 sin los 2 mejores dias (los 2 dias con mayor EXCESO diario propio).
- G5 PLACEBO: p < 0,05 unilateral (5000 sorteos) frente a sets aleatorios de tomadores del mismo tamano k (k = nº de tomadores banderados distintos observados), extraidos de POOL_I ∩ tomadores observados en el flujo (permutacion a nivel TOMADOR, no de fill). Se reporta tambien el p con pool = todos los tomadores observados y el p por fill.
- G6 Desagregado ETH/SOL/XRP: EXCESO reportado por moneda (mismo EV ponderado; sin recortes); gate: signo > 0 en >= 2 de 3 monedas con la moneda >= 10 unidades banderadas; ninguna moneda se descarta.
- G7 Concentracion: tomador top <= 30 % del EUR banderado y ningun dia > 40 % del pnl banderado absoluto.
Veredicto: `PASS` solo si G1-G7 se cumplen a la vez en el mismo corte; `REFUTADO` si G1 y G2 se cumplen y G3 o G5 falla; si no, `EN_CURSO` (n insuficiente) o `BLOCKED_SIN_FLUJO` (B sin fills nuevos). **Prohibido parar al ver un resultado favorable** (test unico cuando se cumplan G1 y G2; los informes diarios son descriptivos). Un PASS no autoriza nada live: solo habilita proponer un prereg de politica (cancelar/no cotizar) con otro test.

## 5. Corrientes
- **B (primaria)**: la definida arriba. NOTA CRITICA: B no tiene fills desde el 23-Oct 08:56Z (wallet con ~3,41 pUSD, "B agotado"); sin relanzar B esta corriente no acumula n y el estado sera `BLOCKED_SIN_FLUJO`.
- **POB (secundaria, descriptiva)**: rellenos de OTROS makers (ETH/SOL/XRP 5m, pc en (0,10-0,30], T 60..300 s antes del cierre, primeras 5 acciones por maker-mercado-lado), mismos sets y mismas metricas, desde 24-Oct. Replica la poblacion de `tab.pkl`; puede refutar/matizar pero NO valida B (poblacion distinta).

## 6. Dry-run 22-23 Oct
Solo valida que el script corre y reproduce cifras del verificador; esos dias son EN MUESTRA para SET_I (ventana 09-23) y parcialmente para SET_V (20-23 sin solape con 09-18, pero ya vistos por el verificador: post-hoc). No cuentan para ningun gate.

## 7. Operacion
`scripts/cf_diario.py` (cron diario propuesto, NO instalado): lee ledger + `m5_onchain` D y D+1; reanuda con cache idempotente por `tx`; escribe `salidas/cf_resumen_YYYY-MM-DD.json` (acumulado desde 24-Oct), `salidas/cf_unidades.csv`, `run_manifest.json`, log con marca de tiempo; `nice -n 19 ionice -c3`, `ulimit -v`, fuera de 06-09Z, RAM < 300 MB.
