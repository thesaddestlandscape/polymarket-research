# PLAN DEL CICLO 26-Oct — agentes, orden y puertas de revisión (polymarket-quantum-alpha-miner → chief)
Reglas: ≤3 agentes con tokens a la vez; un solo trabajo pesado en la máquina; nada pesado 06:00-09:30Z ni con load5>4 (09:38Z: load5 5,2-6,4); sin dinero real, sin crons, sin tocar B/F2/vigías congelados/módulos compartidos; respuesta final de cada agente ≤5 líneas y detalle en su INFORME.md. Ningún resultado lo certifico yo: lo valida otro agente desde datos crudos.

## 1. Prerregistros congelados (hechos en esta sesión, antes de mirar datos)
| Prereg | sha256 | mtime (UTC) |
|---|---|---|
| `alpha_miner/PREREG_M2_COLCHON_PARIDAD.md` | 86291260965998e2f62a19162a20a6d42dfbfe23446615acca76714d608a3112 | 2026-10-26 09:46:18 |
| `alpha_miner/PREREG_M1_CONTRA_PERDEDORA.md` | da120f36e70e930ca3cf421e64a2f9b107a1c777dfd17160b77c812421bb13af | 2026-10-26 09:46:45 |
Verificar: `cd misiones/5m_barato/docs/reverse-engineering/alpha_miner && sha256sum -c PREREG_M2_COLCHON_PARIDAD.sha256 PREREG_M1_CONTRA_PERDEDORA.sha256`.

## 2. Olas (en orden; la siguiente arranca al entregar la anterior)
| Ola | Agente (modelo) | Tarea | Pesado | Cuándo |
|---|---|---|---|---|
| 1a | `cheap5m-execution-engineer` (sonnet) | Calibración [pes,opt] vs rellenos on-chain de B (ya en cola #1 de PLAN_AGENTES_26OCT; NO duplicar si ya está lanzado) | medio | tras 13:00Z, load5<4 |
| 1b | `cheap5m-market-data-engineer` (sonnet) | Contrato de datos para M2/M1/V4: cobertura token-map + desenlace oficial 22-Oct→hoy en `m5_onchain`, y existencia de los ficheros que necesitan f24/f25 y a3/a4 para días nuevos | ligero | ya (solo lectura ligera) |
| 2a | `cheap5m-statistical-validator` (sonnet) | Ejecutar E-AM-M2 fase 1 (solo cobertura hasta ≥10 días; lectura decisoria ~03-Nov) y E-AM-M1 (lectura ~01-Nov) exactamente según prereg | medio | tras 1b; uno detrás de otro, nunca en paralelo |
| 2b | `cheap5m-red-team-auditor` (opus) | V4: verificación on-chain de los 40 ejecutables (fila 1 del intake) | ligero | tras 1b, en paralelo con 2a (ligero) |
| 3 | `cheap5m-red-team-auditor` (opus) | Red-team del resultado de M2/M1 (cuando haya lectura decisoria) | ligero | ≥01/03-Nov |
| 3b | `cheap5m-wallet-intelligence-analyst` (sonnet) | Diseño + prereg de M4 (completado de cosechadores) sobre el ledger `r4` ya extraído | ligero | solo si M1 o M2 no salen REFUTADA, o si hay hueco de cuota |
| — | `cheap5m-objetivo-200k` | Actualizar LIBRO con las filas M1-M5 como POTENCIAL etiquetado (no ingreso) | ligero | tras ola 2 |
Re-mediciones R0/R1 sobre población on-chain (intake filas 12-13): encargo al `cheap5m-statistical-validator` en la ola 2 SOLO si 2a no lo ocupa; si no, ola 3.

## 3. Prompts listos (copiar tal cual)

### 1b — market-data-engineer
«Misión 5m barato. Solo lectura, nice 19, sin cómputo pesado, ≤60 k tokens. Lee `misiones/5m_barato/docs/reverse-engineering/alpha_miner/{PREREG_M2_COLCHON_PARIDAD,PREREG_M1_CONTRA_PERDEDORA}.md` (comprueba sus sha256 con `sha256sum -c`). Para cada día de cierre 2026-10-22..hoy di: (1) existe `/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_D.csv.gz` y si está completo (primer/último bloque vs 00:00/24:00 UTC); (2) qué fichero da el mapa token→(mercado 5m, lado Up/Down, moneda, cierre) para esos días (`mapa_escala` llegaba solo al 22-Oct: ¿hay otro? ¿gamma closed=true?) y su cobertura por moneda; (3) cobertura en € del desenlace OFICIAL por moneda×día con la mejor fuente disponible (`maker_ms_desenlaces_cache.json`, gamma closed=true); (4) qué entradas necesitan `wallet_pspspsps5/senales_externas/scripts/f24_otro_lado.py` y `f25_gap_robustez.py` y `ganadoras_persistentes/scripts/a3_perdedoras.py`/`a4_contraparte.py` para correr sobre días nuevos SIN cambiar su lógica (solo la lista de días), y si alguna depende de ficheros ya rotados; (5) para V4: si `onchain_fills_D.csv.gz`/`m5_onchain` tienen `log_index` y bloque suficientes para saber si un nivel de ask fue consumido antes de t0+215 ms. No calcules ningún EV. Entrega `alpha_miner/DATOS_M1_M2_V4.md` con tabla día×moneda×cobertura y la lista exacta de comandos; respuesta ≤5 líneas.»

### 2a — statistical-validator
«Misión 5m barato. Ejecuta EXACTAMENTE los prereg `alpha_miner/PREREG_M2_COLCHON_PARIDAD.md` (sha 86291260…3112) y luego `PREREG_M1_CONTRA_PERDEDORA.md` (sha da120f36…13af); verifica los sha antes de empezar y no cambies umbrales, bandas, monedas ni ventanas. Usa la tabla de datos de `alpha_miner/DATOS_M1_M2_V4.md`. Copia los scripts de descubrimiento a `misiones/5m_barato/docs/reverse-engineering/alpha_miner/scripts/` cambiando SOLO la lista de días (registra el diff y los sha). Desenlace oficial con cobertura ≥99 % por moneda×día o excluye el día. EV ponderado por €, unidad mercado-lado (M2) / mercado (M1), IC90 bootstrap por día, semilla 20261026, sin 2 mejores días, placebo como dice el prereg. Si hay <10 días completos, reporta SOLO n y cobertura por día (estado INSUFICIENTE, sin EV). Recursos: un trabajo a la vez, `nice -n 19 ionice -c3`, `ulimit -v 3000000`, nunca 06:00-09:30Z ni con load5>4 (comprueba `uptime` antes de cada día procesado; si sube, para y deja checkpoint). Entrega `alpha_miner/RESULTADO_M2.md` y `RESULTADO_M1.md` con veredicto PASA/REFUTADA/INSUFICIENTE según el prereg, comandos y hashes; respuesta ≤5 líneas.»

### 2b — red-team-auditor (V4 on-chain)
«Misión 5m barato. Solo lectura, ligero. V4 forward congelado (`logs/vigia_5m_barato_forward.log`, bloque [OOS_forward] de hoy: 40 ejecutables a +215 ms, EV +0,261, IC90 diario −0,16..+0,77). NO toques el vigía (hash 77a75859ae5cf22e) ni sus ficheros. Objetivo: refutar que esos 40 «ejecutables» fueran comprables de verdad. Para cada uno, con `m5_onchain`/`onchain_fills` (tabla de `alpha_miner/DATOS_M1_M2_V4.md`): ¿hubo casación tomadora en ese token a precio ≤ ask_vigía entre t0 y t0+215 ms (hora de bloque − ~2,4 s, usa log_index para el orden) que hubiera consumido el nivel antes que nosotros? ¿El precio de nuestro supuesto relleno aparece en algún fill on-chain en el bloque correspondiente? Clasifica: CONFIRMADO / CONSUMIDO_ANTES / NO_VERIFICABLE. Recalcula EV ponderado por € solo con CONFIRMADOS, IC90 por CIERRE (no por señal: agrupa monedas del mismo cierre), sin el mejor día y sin BTC. Recuerda: el timestamp del WS de mercado es sello de lote (puede ir 192-468 ms antes del evento). Entrega `alpha_miner/V4_ONCHAIN.md`; respuesta ≤5 líneas.»

### 3 — red-team-auditor (M2/M1)
«Misión 5m barato. Refuta `alpha_miner/RESULTADO_M2.md` y `RESULTADO_M1.md` desde datos CRUDOS (no desde sus intermedios): reproduce n y EV de 2 días al azar; busca look-ahead en «último opuesto» (bloque anterior estricto) y en la identidad de perdedoras (solo D−7..D−1); supervivencia (rellenos sin desenlace, mercados sin opuesto); concentración (día, mercado, vendedor/tomador top); racimos por cierre; si M2 viene de la cola de pagos (hit/p ≈1), cuánto queda sin el 1 % mejor de unidades; si M1 es dirección (compara con control emparejado por movimiento de Binance 60 s previo, descriptivo). Veredicto CONFIRMADO/CORREGIDO/REFUTADO por línea; `alpha_miner/RT_M1_M2.md`; ≤5 líneas.»

### 3b — wallet-intelligence-analyst (M4)
«Misión 5m barato. Diseña (no ejecutes aún más que descriptivos baratos) M4 COMPLETADO DE COSECHADORES de `alpha_miner/MECANICAS_NUEVAS.md`. Con el ledger ya extraído de `b_perdidas_22oct/rebate_ganadores` (r4, 1,40 M fills BTC 5m 06-21 Oct): (1) define cosechador por CONDUCTA en días previos (cobertura ambos lados ≥90 % de mercados, ≥X mercados/día) — no por PnL; (2) descriptivo DESC (06-13): EV y markout +5/+30 s de los rellenos maker cuya contraparte tomadora es un cosechador vs población misma celda; P(compra tomadora del lado faltante en 60 s | desequilibrio visible ≥X acc a bloque+3 s). Con eso escribe `alpha_miner/PREREG_M4.md` (OOS 14-21 Oct y 22-Oct+, gates n≥400 mercados, ≥10 días, Δ IC90 días >0, placebo) y calcula su sha256. No mires el OOS antes de congelar. ≤5 líneas.»

## 4. Lo que reviso YO antes de aceptar cada regla (puerta ANTES)
1. La decisión está definida con hora observable (bloque + ~3 s para identidades on-chain; recepción para WS; [e−62, e−3] para TWAP).
2. Pagador identificado y por qué persiste; predicción diferencial frente a M0 escrita.
3. Prereg con sha y mtime ANTERIOR a la primera lectura de los días de medida; días de medida no vistos por ningún análisis previo.
4. Unidad = mercado-lado/mercado, IC por día y por cierre, EV ponderado por €; K declarado.
5. No es rebautizo del cementerio (lista en MECANICAS_NUEVAS §2 «descartadas»).
6. Si la regla usa rellenos virtuales: intervalo [pes, opt] con la calibración de la ola 1a, nunca un solo número.

## 5. Lo que reviso YO después de cada experimento (puerta DESPUÉS)
1. sha del prereg y del script coinciden; el diff de scripts solo toca la lista de días.
2. Cobertura de desenlace ≥99 % por moneda×día y n excluidos declarados (supervivencia).
3. Sin 2 mejores días, sin el 1 % mejor de unidades, por moneda, por mitad del periodo.
4. Identidades: ninguna cifra se presenta como premio si es (M_f − M_all)/(1−P) o residuo contable.
5. Contrastar con un segundo origen (p. ej., M2 con `libro5_ms` en un día; M1 con data-api `/activity` de 3 perdedoras).
6. Red-team independiente (ola 3) antes de cualquier etiqueta distinta de EXPLORATORY; nada pasa a fase 2 sin prereg de fase 2.
7. Libro de suma: añadir como POTENCIAL con solapes (MECANICAS_NUEVAS §3), nunca como ingreso.

## 6. Qué cambia la decisión
- M2 PASA fase 1 → fase 2 de capturabilidad (es la única que, con EV ≈+0,3 y cuota ≥30 %, se acerca sola a 200 k€); REFUTADA → se cierra el mecanismo «paridad» y la pista de W queda sin explicar (no reabrir S1).
- M1 PASA → fase 2 (cola en ~0,80) y conflicto con B (B compra el barato en los mismos mercados: definir prioridad); REFUTADA → el valor de las perdedoras no es anticipable, cerrar R7/R8.
- V4 on-chain: si <70 % de los ejecutables son CONFIRMADO o el EV de los confirmados por cierre cruza 0 sin el mejor día → V4 no merece F3.
