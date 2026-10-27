# REGIMEN_PLAN — herramienta de régimen como CONMUTADOR de política (programa BANDA-0-0,30; sirve a B, CARRY-FAV-5M y a todo 5m barato) — 26-Oct-2026
Estado: **DISEÑO / EXPLORATORY. Validado 0 €.** Prereg decisivo: `PREREG_BR1_CONMUTADOR_VOL.md` (sha256 c7f84c24b3ef33e4f7492acb9eb0a7ec447b0675c86d14b3b7fa215d7c4f2955, congelado 26-Oct 10:23Z, antes de calcular nada). Sin dinero, sin crons, sin tocar B ni vigías. Rutas relativas a `experimentos/5m_barato/b_perdidas_22oct/` salvo indicación.

## 0. Respuesta corta
1. **No se repite**: tendencia/eficiencia/coherencia/z240 como DIRECCIÓN o como lado CON/CONTRA (D-FUERTE AUC 0,554; R-TEND; b_regimen; W1), el nivel diario por el día anterior (Spearman −0,03 en 129 d de proxy) ni el detector de rellenos malos (AUC 0,513). R0 (saltar el lado a favor de la tendencia de 15 min, Δ −0,234 al ask real, placebo p=0,000, 16/17 días, ETH/SOL/XRP; BTC signo contrario) sigue en su forward L1/L1b (~02-03 Nov): es una regla de LADO y es compatible con este plan.
2. **Reformulación**: el objeto es el NIVEL del EV del maker por (moneda, hora) y qué política conviene en cada régimen (maker largo barato / corto barato / no jugar; banda; tamaño), no la dirección a 5 min.
3. **Única familia con mecanismo aún sin probar** (declarada así en `detector_regimen/INFORME.md` §2): el hueco σ_prev − σ_imp (prima de volatilidad del binario). σ_prev > σ_imp ⇒ longshots baratos (maker largo barato / B ON; CARRY-FAV en reposo); σ_prev < σ_imp ⇒ longshots caros (CARRY-FAV y M1 ON; B OFF).
4. **Retraso**: conmutador horario por moneda (mediana de ~190 fotos/hora), útil solo si la semivida del régimen es ≥3 h (se mide; si es <1 h se cierra la línea, sin bajar a valoración por mercado = FV v4, cementerio).
5. **Gate** en días frescos ≥27-Oct (10 días ≈06-Nov; WF de 30 días el 04-Nov), placebo dentro de moneda × bloque de hora, inversión en el lado caro (lo que sirve a CARRY-FAV) y línea base AR2h.
6. **€ honesto**: como interruptor de B tal cual ≈0,3-0,5 k€/año; su valor es multiplicar una política escalada (CARRY-FAV o maker en cola): 33-100 k€/año brutos con cuota 1-3 % del flujo del régimen favorable SI el EV propio iguala al de la población; central 5-15 k€; validado 0.

## 1. Antecedentes (no repetir) y lo que dejan abierto
| Pieza | Qué probó | Resultado | Deja abierto |
|---|---|---|---|
| D-FUERTE (`detector_regimen`) | dirección a 5 min con rasgos de régimen, 171 d | AUC 0,554 (M17); exceso explicado a medias por nivel día × moneda | nada (dirección cerrada) |
| R-TEND H1/H2 | CON vs CONTRA (tendencia 15 min previa), S_A 129 d, S_D 2025 349 d, S_B 40 d oficial, bookTicker 28 d, pob. 17-22 | H1 SÍ (Δ −0,08..−0,17, placebo p≤0,002); H2 TREND I_R −0,073 (p2 0,025 sin corregir) | regla de lado R0/R1/R2 (forward) |
| P-REAL R0 / R2 | saltar CON (\|rpre\|≥7,7 bps) al ask real; R2 solo TREND/MIXTO | R0 Δ −0,234, p=0,000, 16/17 d; R2 p=0,044 (no pasa Bonferroni) | forward L1/L1b ~02-03 Nov |
| `b_regimen` | alcista/bajista/lateral (z240), reglas H-R/H-R2/H-N, AR2h | sin dependencia estable; reglas fallan OOS; AR2h/H-N2 ≤+0,04 por € y no pasan K | AR2h = línea base G8 de BR1 |
| R-TEND §0.4 | nivel diario del EV de longshots | Spearman(X_d−1, X_d) = −0,03 (129 d) | nivel HORARIO con rasgo nuevo |
| H50 (E-RE-CM-03) | régimen d−1 del EV de la población | BTC r 0,34 p 0,057; ALT3 r 0,14 p 0,21 (15 pares) | repetir con ≥30 pares (~20-Nov) |
| `detector_ex_ante` | detector de rellenos malos | techo AUC estratificado 0,513; M1F forward desde 25-Oct | — |
| W1 `tendencia_wallets` | rpre/r900/r60/f60; ganadoras ETH | dominado por 17-19 Oct; las ganadoras no leen tendencia | — |
| R1/E1D | cancelación por régimen ms | confusor moneda + hora + sábado | — |

## 2. Pregunta 1 — ¿qué variables ex ante separan horas/días buenos y malos sin confusor?
| Familia | Mecanismo | Fuente (marca de RECEPCIÓN) | Estado | Papel |
|---|---|---|---|---|
| V1 VG = ln(σ_prev/σ_imp) | prima de volatilidad del binario; anclaje de los makers | m5_registro q, Chainlink RTDS (+1,36 s), polybolt twap60, barras 1m Binance | NUEVA | primaria (BR1) |
| V2 tendencia multi-escala (r60, rpre, ER60, VR240, z240, DAYT) | continuación/reversión | `regimen_lib.py` (barras cerradas) | vista | descriptiva / control |
| V3 actividad (vol30, VOLR, prints, € tomador por hora) | más flujo, más informados | m5_onchain (bloque + 3 s), m5_registro | vista en R1 (confusor) | descriptiva con efectos fijos |
| V4 hora, día de la semana, sábado | composición del flujo | reloj | confusor | efectos fijos y estratos del placebo; NUNCA conmutador |
| V5 liquidez (spread mediano, tamaño del top, 3 niveles) | makers retirados ⇒ más selección adversa | m5_registro q / libro5_ms | NUEVA como régimen | descriptiva (candidata a BR1b) |
| V6 composición del flujo tomador (cuota del € de perdedoras persistentes y de tomadores rápidos en las 2 h previas) | quién paga (lotería) frente a quién informa | m5_onchain, identidad a bloque + 3 s, lista D−7..D−1 | NUEVA como régimen | descriptiva; enlaza con M1/CF |
| V7 EV propio reciente (AR2h, EV d−1) | momentum del nivel | m5_onchain + desenlace | vista | línea base (G8) |
Control de confusores: (a) placebo permutado entre días dentro de moneda × bloque de 6 h; (b) regresión del EV por unidad sobre VG con efectos fijos de moneda, bloque horario y día de la semana, IC por día; (c) BH-FDR entre descriptivos; (d) ningún descriptivo cambia el veredicto: un ganador solo entra en un prereg nuevo (BR1b) con días frescos posteriores.

## 3. Pregunta 2 — ¿se identifica con retraso aceptable?
Medidas descriptivas ya prerregistradas en BR1: ACF de EV_{c,h} a 1-24 h y semivida (bootstrap por día); ACF de VG; matriz de transición ON/MEDIO/OFF hora a hora; retraso de detección = horas entre un cambio de régimen definido ex post (EV realizado de 6 h centrado) y el cambio de clase de VG. Criterio fijado ahora: semivida del nivel ≥3 h y retraso mediano ≤1 h. Si la semivida es <1 h, el conmutador horario no puede funcionar y la línea se cierra.

## 4. Pregunta 3 — qué política cambia por régimen y cuánto vale
| Régimen (VG de la hora anterior) | Maker largo barato (B, cola) | Corto barato: CARRY-FAV (profundo) y M1 | M2 (paridad) | Tomador en banda | Tamaño |
|---|---|---|---|---|---|
| ON (σ_prev ≫ σ_imp: longshots baratos) | ON en 0,10-0,30 | en reposo / mínimo | ON | NO (comisión 4,9-6,7 %/€) salvo V4 | K hasta 20 (R3: K≤20) |
| MEDIO | base (B tal cual, K5) | base | ON | NO | base |
| OFF (σ_prev ≪ σ_imp: longshots caros) | OFF (B en pausa) | ON (favorito 0,70-0,99) | ON | NO | CF a su tamaño |
Valor: Δ de BR1 (€/€ con IC por días) y G6 (inversión en el lado caro). Para B en concreto, además (descriptivo, n pequeño): clases aplicadas a sus 202 rellenos on-chain y al forward pasivo L1/L1b.

## 5. Datos y walk-forward ≥30 días
| Fuente | Rango | Uso |
|---|---|---|
| Klines 1m Binance 2025 (`/root/polymarket-research-datalogs/regimen_5m/barras_y2025.npz`, 349 d) y backfill 2026 (26-Mar..17-Ago) | larga | ajuste (2025) y validación fuera de muestra (2026) del HAR: R² de ln RV 5 min |
| bookTicker Binance (24-Sep→) | 1 mes | barras 1m en vivo |
| Chainlink RTDS `data/prices/chainlink_D.csv` (10-Oct→), polybolt twap60 | ~16 d | S_t y ref5 |
| m5_registro (05-Oct→, 60 d) | 21 d | mid para σ_imp |
| m5_onchain (05-Oct→) | 21 d | objetivo (EV maker) |
| libro5_ms (19-Oct→) | 7 d | spread/profundidad (V5) |
| Jon-Becker (dic-ene, desenlace oficial, sin precios) | 40 d | solo validación de la proxy de desenlace |
| prices-history del CLOB (a sondear en la ola 1) | ¿meses? | si existe: σ_imp histórico + desenlace gamma → réplica LARGA de VG sobre el error de calibración del mid (componente de valoración del EV del maker; no sustituye rellenos ni cola; recordar que es precio MEDIO) |
Potencia: el objetivo (EV maker on-chain) solo existe desde el 05-Oct. Por eso: (i) WF-ALL 05-Oct→ llega a 30 días el 04-Nov (descriptivo; la familia se eligió antes); (ii) la decisión se toma en frescos ≥27-Oct (10 d ≈06-Nov; 30 d ≈26-Nov); (iii) réplica larga solo si prices-history da mids (prereg BR1-L aparte, tras la sonda); (iv) la mitad σ_prev se valida ya con 2025→2026. Efecto mínimo detectable ≈+0,07 a 10 días; +0,04 necesita ~30 días.

## 6. Arnés de régimen (lo construye `cheap5m-execution-engineer`)
`experimentos/5m_barato/banda_0_30/regimen/`: importa (no copia) `detector_regimen/scripts/regimen_lib.py`; nuevo `vol_lib.py` (σ_imp por foto, HAR congelado con sha, VG por moneda-hora) importado por el análisis Y por el etiquetador; `etiquetar_vg.py D` (etiquetas por moneda-hora con versión de código; lock, escritura atómica, idempotente, retención 45 d, patrón de `etiquetar_regimen.py`); `evaluar_br1.py` (une etiquetas con la población on-chain, con B y, cuando existan, con CF/M1/M2). Sin cron salvo decisión del chief (proponer `25 0 * * *`). Salida `/root/polymarket-research-datalogs/regimen_vg/etiquetas/vg_D.csv.gz`.

## 7. Olas de agentes (integradas con `INFORME.md` §4.2; ≤3 con tokens a la vez; un solo trabajo pesado)
| Ola | Agente (modelo) | Tarea | Pesado | Cuándo |
|---|---|---|---|---|
| R1 | `cheap5m-market-data-engineer` (sonnet) | contrato de datos (ola 1 del INFORME) + sonda prices-history | ligero | ya |
| R2 | `cheap5m-execution-engineer` (sonnet) | HAR 2025 congelado + validación 2026 + `vol_lib` + VG 05-Oct→ + etiquetador | medio | tras R1, fuera de 06:00-09:30Z, load5<8 |
| R3 | `cheap5m-statistical-validator` (sonnet) | revisión de código vs prereg (sin gates) | ligero | tras R2 |
| R4 | `cheap5m-statistical-validator` + `cheap5m-red-team-auditor` (opus) | gate BR1 en frescos; refutación desde crudos (confusor moneda/hora/sábado, horas extremas) | medio / ligero | ≥06-Nov |
| R5 | `cheap5m-objetivo-200k` | valor del conmutador sobre B, CF, M1, M2 sin solapes (como POTENCIAL) | ligero | tras R4 |
**Prompt R2:** «Misión 5m barato, BANDA-0-0,30, línea de régimen. Verifica `sha256sum -c misiones/5m_barato/docs/reverse-engineering/alpha_miner/banda_0_30/PREREG_BR1_CONMUTADOR_VOL.sha256`. En `experimentos/5m_barato/banda_0_30/regimen/`: (1) ajusta el log-HAR por moneda SOLO con `regimen_5m/barras_y2025.npz` y congela los coeficientes (json + sha + mtime) antes de abrir ningún dato de octubre; (2) valida el HAR en el backfill 2026 (R² de ln RV 5 min) y repórtalo; (3) `vol_lib.py` con σ_imp por foto exactamente como el prereg (m5_registro ordenado por recepción, Chainlink source=chainlink por recepción, twap60 oficial, τ_eff = (T−62)+59/3) y VG por moneda-hora; (4) VG y AR2h 05-Oct→último día; cortes de CAL solo con valores de VG; (5) `etiquetar_vg.py` idempotente, sin cron. NO calcules Δ ni ningún EV por clase. `nice -n 19 ionice -c3`, `ulimit -v 3000000`, fuera de 06:00-09:30Z, load5<8, un trabajo a la vez, checkpoint por día. Entrega `banda_0_30/IMPL_REGIMEN.md` (comandos, hashes, tasa de missing de σ_imp por moneda-hora); respuesta ≤5 líneas.»
Prompts R3/R4: los de las olas 2b y 3 de `INFORME.md` §4.2 (cubren BR1).

## 8. EV potencial honesto
- Como interruptor de B tal cual (55 €/día, EV −0,072): pausar B en OFF ahorraría ≈0,3-0,5 k€/año si Δ ≈ +0,05. Irrelevante para 200 k.
- Como multiplicador de una política escalada: flujo maker largo barato en horas ON ≈114 k€/día (1/3 de 341 k); cuota 1-3 % con EV +0,08 → 33-100 k€/año brutos; con la brecha medida de un diseño tipo B (−0,053) → 0-35 k. Lado caro (CARRY-FAV en OFF): flujo maker favorito ≈2,28 M€/día, 1/3 en OFF; 0,5 % de cuota a +0,034 → ≈47 k€/año, solo si CF1 pasa y la cuota se demuestra.
- Central (retención exploratorio → forward medida en el proyecto 11-28 %): 5-15 k€/año. **Validado: 0.** Coste del test: 0 € y ~1-2 h de CPU.
