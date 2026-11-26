# CONTRATO DE MEDICIÓN L1b-v2 — retirada de liquidez del nivel antes del print (eje SALIR/CANCELAR de B)
measurement_id: M-L1B-V2-26nov · versión 1 · 2026-11-26 · estado previo: NOT_ASSESSED (L1b-B «REFUTADA» = NO VALIDADO/INSUFFICIENT) · veredicto del contrato: AMBER hasta firma; GREEN solo tras auditoría post-proceso.
Los campos marcados (VERIFICAR) no se han comprobado en disco en esta redacción: el engineer los confirma y registra antes de medir; si no existen, el campo pasa a `missing/not_identifiable`.

## 1. Pregunta, decisión, estimando
Pregunta: ¿cancelar la orden de B cuando el nivel en que reposa pierde liquidez antes del print reduce la selección adversa (rellenos perdedores) sin perder más rellenos buenos de los que evita?
Decisión que cambia: si la fila «SALIR/CANCELAR-L1b» entra en la matriz (CONTRATO_MATRIZ_B_25nov) como candidata o como NO VALIDADO. Sin efecto en la firma del 27-Nov ni en P1b.
Estimando (INCONDICIONAL, regla Javi 30-Oct): ΔEV por orden colocada de B = EV(política con cancelación) − EV(política sin cancelación), sobre TODAS las órdenes colocadas por la política real (rellenen o no; no rellenadas = 0 pnl, contrafactual declarado). Descomposición obligatoria: P(relleno) × EV|relleno para ambas ramas, y comparación condicional vs incondicional. Prohibido reportar solo EV|relleno.

## 2. Unidad, universo, política
- Unidad: primer relleno mercado-lado de la política REAL de B (DEEP_PEG top−k con repegado), no relleno hipotético por print (eso era G0).
- Política: IMPORTAR las funciones del simulador/ejecutor B-K (rama dev-bk/b-k-ejecutor y sim passT_v4 de `b_real_sim/`; ruta exacta VERIFICAR); prohibido copiarlas. Guardas del ejecutor incluidas (trampa «política sin guardas»).
- Universo: mercados 5m cripto (6 monedas, desagregado por moneda × clase de suelo), todas las órdenes colocadas, no solo con prints.
- Días utilizables: libro5 + libro5_tx con cobertura del join con_tx/units ≥0,90 POR DÍA; día <0,90 = INCOMPLETE terminal (excluido, listado). Solo COMPLETE (filtro de `evaluar_retirada.py`). EXCLUIDOS los días precintados ≥25-Nov hasta la mirada (si se tocan: EV precintado igual que SIM-L, es decir calculado y sellado sin lectura hasta la mirada). Retención ~3 d: extraer YA lo que caduque; octubre irrecuperable salvo copias keep (VERIFICAR `/root/archivo_libro5_raw`, keep_onchain_re_as_b y datalogs keep_*: si existen con libro5+libro5_tx+onchain del mismo día y cobertura ≥0,90, cuentan como días COMPLETE); libro5 en PAUSA 19-23 Nov por disco (INCOMPLETE). Declarado: con días precintados excluidos, la medición inicial será casi seguro INSUFFICIENT; el forward 6c acumula días con EV sellado hasta la mirada.

## 3. Anclas temporales y fuentes
- Ancla del relleno: casado on-chain por hash de tx (`onchain_fills_D.csv.gz`, takerFillAmount; excluir txs propias) / passT_v4. NO el print de `libro5_tx` (≈casado+20 ms, p95 76) ni la recepción del mensaje T del WS. NO hora de bloque (~2,4 s tras el casado: mira el futuro).
- Ancla de decisión de cancelar: RECEPCIÓN local del `price_change`/book del WS (el `timestamp` del WS no es hora de evento). Cancelación efectiva = recepción + reacción B-K 3 ms (VERIFICAR fuente) + latencia de cancelación vigente (§4). Un relleno ocurre si su casado on-chain precede a la cancelación efectiva; si no, la orden se anula.
- Clase de suelo (lo/hi, v3.4b): por SUELO MEDIDO por ventana, nunca por fecha. Resultados por clase por separado y luego combinados; reloj explícito en cada tabla. Una conclusión que solo vale en una clase = «condicional a esa clase».
- Lote/evento WS NO identifica el resto del tomador: el resto/límite del tomador solo del calldata (`tk_rem·tk_sz` = (makerAmount − takerFillAmount)/límite); es modelo del simulador, nunca rasgo de decisión. Rasgo NaN-si-no-hay-datos = fuga: solo datos ≤ t, probar que el NaN no predice desenlace.
- Libro cruzado/bloqueado: descartar el evento.

## 4. Latencia (SOLO datos vigentes)
Cancelación: `datalogs/paquete_l/ensayo_real_B2,B3,B5` (13-Nov, n=313; VERIFICAR) por clase de suelo + los 17 acks/cancel de P1b del 26-Nov (d_red_cancel p50 59,5 / p90 125 ms) como dato vigente adicional, reconciliado, no mezclado. Barrido de sensibilidad p50/p90 de cada fuente. Prohibido Sonda 30-Oct..05-Nov. Una cancelación que llega DENTRO del taker-delay de una orden ya enviada no la anula (cementerio); aquí solo se cancela NUESTRA orden maker en reposo.

## 5. Regla a evaluar y placebo (congeladas antes de ver resultados)
- Regla R: cancelar la orden de B en reposo cuando, tras su colocación/repegado, la liquidez del NIVEL propio (cola por delante, tamaño del nivel) cae por debajo de umbral u antes del print. Umbral u ∈ {predeclarado: 50 % y 80 % de caída en ≤W ms; W ∈ {100, 300} ms}: 4 celdas, multiplicidad con max-statistic/BH-FDR sobre esas 4. No se añaden celdas.
- Placebos obligatorios: (P1) cancelar en un instante aleatorio equivalente (misma tasa de cancelación); (P2) misma regla con el nivel ±1 tick (nivel equivocado); (P3) inversión (cancelar cuando el nivel NO se vacía). Si placebo/inversión salen igual de positivos, la regla no ordena nada.
- Misma política sin cancelación = base. Re-peg tras cancelar: según política real de B (declarar).

## 6. Métricas
Por celda, moneda × clase de suelo y total: n órdenes, n mercados, n días; P(relleno) base vs R; markout|relleno (a casado+{1,5,30} s y a desenlace oficial TWAP60 con la regla correcta); rellenos evitados que eran perdedores vs rellenos buenos perdidos (matriz 2×2, con € de cada celda); ΔEV incondicional por orden y por €. TODO ponderado por € (Σpnl/Σcoste) además de por unidad; fee/rebate real del mercado (cripto 0,07, rebate maker 0,2; versión del mercado v1/v2 leída por mercado). EV sin los 2 mejores días y por cierre/día (fallos en racimo). Desenlace oficial con cobertura ≈100 % (reportada); mercados sin libro NO se descartan (censura).
IC90 por DÍAS (bootstrap por días), nunca por filas/fills.

## 7. Criterio (fijado antes de medir)
- PASA (solo EXPLORATORY/PROMISING, nunca validado por sí solo): ≥10 días COMPLETE, ≥300 órdenes colocadas por clase de suelo, ΔEV incondicional ponderado por € >0 con IC90 por días >0 en AMBAS clases, también sin los 2 mejores días, placebo P1/P2/P3 con ΔEV ≤ 0 o IC cruzando 0, y ΔEV corregido por multiplicidad.
- FALLA: IC90 por días <0 en ambas clases con n cumplido, o placebo igual/mejor.
- INSUFFICIENT (por defecto): n o días por debajo del mínimo, o una clase sin datos. NO se declara «refutada/cerrada» (regla no cerrar puertas); se deja forward pasivo con fecha de gate.
- Stop rule: cobertura del join <0,90 en >50 % de los días disponibles, sim con paridad vivo≠batch, o RAM >límite → STOP y reporte PARTIAL/FAILED.

## 8. Coste y ejecución
Re-extracción de libro5/libro5_tx de los días COMPLETE disponibles (~3 d de retención; estimar filas/GB al abrir, copiar a keep con cp+cmp antes de que rote); un único job pesado, `scripts/cron_pesado.sh` (cgroup pesados.slice, MemAvailable ≥3 GB), `ulimit -v` ≤3 GB, nice 19/ionice -c3, fuera de 06:00-09:15Z y 22:15-02:45Z (y no en la KS 27-Nov 13:30-15:00Z); lectura en columnas array (no tuplas, no list(DictReader)). Sin llamadas API (todo local); sin gasto. Salidas en `experimentos/5m_barato/` con manifest, checkpoint idempotente, hash de código y datos; verificar JSON recién escrito con su sello, no el rc. Forward nuevo posterior: engineer (6c) con puerta de cobertura por día.

## 9. Auditoría y límites
Tras procesar: Measurement Audit (tabla derivada, denominadores, paridad con este contrato). Limitaciones conocidas: ventana de datos ≤~3 días COMPLETE (probable INSUFFICIENT inicial; la evidencia vendrá del forward); no valida sin validador estadístico + red-team independientes; no toca B, ejecutores ni módulos compartidos.

Firma (OK Javi): OK de Javi en sesión (condicionado a revisión del chief; correcciones del chief aplicadas: franjas pesadas 22:15-02:45Z y KS; copias keep y pausa 19-23 Nov declaradas)  Fecha: 2026-11-26T15:00Z
Sello sha256 del contrato: (lo añade el chief al commitear)
