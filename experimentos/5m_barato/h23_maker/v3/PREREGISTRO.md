# H69 — H23-MAKER-V3 (RE-PUJA-150) · PREREGISTRO (21-Oct-2026, escrito ANTES de ver ningún resultado OOS 19-20 Oct ni del replay v3)
Estado: EXPLORATORY · solo replay/dry-run · NADA real · paquete H23 v1 congelado (sha 602d5a2debb42cc0, regla 46eff95337902549) INTACTO.
Origen: v2/informe_21oct.md (H62-H66). El efecto de r150 sobre r1500 salió de ~5-7 rellenos «recuperados» en 13 días ya vistos: es una hipótesis, no un hallazgo.

## 1. Qué es V3 (y qué NO cambia)
- Regla de entrada/cancelación = H23 v1 (`h23_regla.py`, umbrales A 0,05 / B 0,02, mq, p_limite, cola, cota bid15): **idéntica** (test `test_regla_v3_solo_difiere_en_lo_declarado`).
- Único cambio de regla: **re-puja 150 ms después de la DECISIÓN de cancelar** (`repuja_ms=150`; v1: el arnés real espera `ASENTAR_S`=1,5 s). Y el replay v3 mide con el **tamaño real** del
  arnés (5 acc o ceil(1 USD/p), tope 10; universo p∈[0,10;0,60], sin puja nueva con T≤12 s) y con «un relleno, aunque parcial, cierra la puja» (modo `primer`), no con los 2 € del replay v1/v2.
- Código: `h23_regla_v3.py` (hash `3eeff503cf0a75c9`), `h23_sim_v3.py`, `paquete_real_v3/experimento_maker_h23_v3.py` (diff vs v1 en `diff_harness_v1_v3.patch`: +104/−16 líneas; 97 tests, 75 heredados + 22 nuevos).
  Ledgers/escalones propios `H23V3`/`H23V3B`, OK propio `H23V3_OK_JAVI.txt`: el n y el kill de v1 y v3 no se mezclan.

## 2. Hipótesis y mecanismo
H69: sobre la misma regla v1, re-pujar a ≤150 ms (en vez de 1,5 s) tras cada cancelación conserva rellenos que el arnés v1 pierde, sin degradar el EV ponderado por €.
Mecanismo: la cancelación es el edge (v1 sin cancelar: +0,06; con cancelar: +0,6-0,8 en replay); tras cancelar, el bid vuelve a ser elegible en ms, y el arnés v1 se pierde esa ventana.
Falsación: si en días NO vistos (OOS) r150 no conserva ≥1,4× los rellenos de r1500 o su PnL total es menor, o el EV ponderado sin 2 mejores días ≤0, H69 se rechaza.
Riesgo R1 (no medible en replay): un casado de ms ANTES del cancel puede verse en `get_order` ~1 s tarde (9.ª review de ASENTAR_S). Re-pujar a 150 ms puede dejar DOBLE exposición (≤2 órdenes ≤3 USD cada una, dentro del presupuesto útil de 5 USD).
Riesgo R2: la latencia REAL decisión→envío de la re-puja (cancelar + `get_order` + firmar + POST) puede ser >300 ms; el replay r300/r500 pierde casi todo el beneficio.
Riesgo R3: el WS puede seguir mostrando la propia orden cancelada como bid unas decenas de ms (la re-puja se unirá a un nivel «fantasma»); mitigado solo en parte: no se libera sin un mensaje del libro de ese token posterior a la decisión de cancelar. Medible en el ensayo en seco/real (`puja_post` vs libro ajeno).

## 3. Celda primaria, multiplicidad y lectura (fijadas ahora)
- PRIMARIA: BTC, cola base, alta 79 ms, cancelación 60 ms, sizing `real`, cierre `primer`, 1 relleno por cierre, desenlace oficial (sin desenlace = missing, nunca 0), hora de RECEPCIÓN, rebate 20 %, fee 0,07.
  Contraste primario = **r150 − r1500 emparejado por cierre** (PnL total, comunes / solo-r150 / solo-r1500), brazos A y B por separado (2 contrastes).
- DESCRIPTIVAS (sin elegir la mejor): r0, r50, r300, r500; sizing `2eur`; cierre `acum`; colas opt/cons; latencias 254/150. Familia mirada: 6 reps × 2 brazos × 2 sizings × 2 cierres = 48 celdas centrales → ninguna se declara significativa.
- Periodos: **DISC** 06-18 Oct (13 días, ya vistos por v1/v2) · **OOS** ≥19-Oct (no vistos al fijar r150). Las cifras DISC no cuentan para el gate. El OOS del replay se actualiza a medida que haya `m5/m15_registro` de más días (mismo comando, solo añade días).
- IC90 por DÍAS (bootstrap de días, 3000, semilla 7) solo con ≥5 días con relleno; si no: «no estimable». Se reporta siempre EV ponderado por € (Σpnl/Σcoste) Y por unidad, y sin los 2 mejores días.
- **Etiqueta del replay OOS**: «INSUFICIENTE» mientras haya <5 días OOS o <5 rellenos «recuperados» (esperado ≈0,4-0,5 por día entre A y B: 2 días ≈1). No decide nada; sirve para detectar un bug o un cambio de signo grosero.

## 4. Gate para pasar de EXPLORATORY a DRY_RUN_VALIDATED (solo observación; NO autoriza real)
Sobre rellenos FORWARD (shadow `h23shadow` + ensayo en seco v3; mismo cálculo que la celda primaria): por brazo, **n ≥ 40 posiciones, ≥10 días, EV ponderado por € ≥ +0,05, IC90 por días > 0, sin 2 mejores días > 0**, y además:
(i) latencia real de re-puja medida (`h23v3_repuja.ms_desde_decision_cancel` y `puja_post.ms_desde_decision_cancel`) con p50 ≤ 300 ms sobre ≥10 re-pujas; (ii) cero `h23v3_fill_tardio` con `doble_exposicion=true`;
(iii) cobertura de desenlace oficial = 100 % de las posiciones del gate. Ritmo esperado (replay DISC, IC Poisson 90 % en el informe): A r150 ≈1,15 rellenos/día → ~35 días a n=40; ambos brazos por tandas alternas (misma wallet) ≈2× más.

## 5. Kill / paradas (heredadas + nuevas)
- Heredados de v1: kill V3 por brazo (fórmula σ acumulada, n≥3; hash `kill=59437e2037321aed`), tope de tanda 5,0 USD (no persistente), suelo de saldo H47 (**suelo duro 12 pUSD**), kill_brazo por ledger hermano ilegible (fail-closed).
- Nuevo: `h23v3_fill_tardio` con orden propia posterior a la cancelación en el mismo token = **doble exposición → kill de brazo PERSISTENTE** (rearme a mano).
- Nuevo: tras ≥10 re-pujas, p50 de `ms_desde_decision_cancel` > 300 ms → se PARA la lectura «r150» (la premisa del replay no se cumple); no es una pérdida, es invalidez: se reevalúa con la latencia real (r300/r500).
- Fail-closed a v1: sin lectura de `get_order` terminal posterior a la cancelación, con `ya_terminal`, con relleno/cierre, o con kill/parada → NO hay re-puja temprana (espera de 1,5 s como v1).

## 6. Dinero real — NADA hasta cumplir TODO
Solo wallet DEDICADA 0x659a40…297F, tanda de 5 USD de presupuesto útil, suelo duro 12 pUSD, ≤3 USD por orden, stake de la misma regla (5 acc / ceil(1 USD/p)); sin recargas. Orden obligatorio:
1. Replay/forward cumplen §4 como mínimo en su parte observable; el ensayo en seco v3 (`experimento_maker_h23_v3.py` SIN `--confirmo-dinero-real`, estado `real=False`) corre ≥1 día sin kill ni `h23v3_fill_tardio`.
2. `/code-review` del diff `diff_harness_v1_v3.patch` (+ sim) — toca el camino de cancelación/re-puja de un arnés con dinero real; sin él no se firma nada.
3. H47-B terminado sin kill (puerta heredada), `--imprimir-sha` y OK de Javi ligado a `sha=… regla=… kill=…` en `/root/polymarket-research-datalogs/H23V3_OK_JAVI.txt`. **El OK de v1 no vale.**
4. Los hashes `h47=` y `pares=` del OK cambian si se edita H47/pares (hoy `h47=08e08d7a65ce10f7`, ya distinto del 439a70e9262ef38c del OK de v1 por la rotación de tanda): reemitir.
Este fichero no autoriza ni lanza nada. Quien lance V3 en real es la sesión principal con el OK expreso de Javi.
