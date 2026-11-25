# ADDENDUM 1 al PREREG_REPLAY_BRECHA_B_16nov — revisión de integridad (B-1..B-6), reordenación de etapas y decisiones de Javi

- **measurement_id**: `BF5-REPLAY-COLOC-v1` (sin cambio de id: este addendum concreta el contrato antes de calcular nada).
- **Prereg base**: `PREREG_REPLAY_BRECHA_B_16nov.md`, sha256 `f1a7d76664ff4ede03a98b948fe78e43d6e95bf3f4381390df9bb206a82fa562` (`sha256sum -c` OK el 16-Nov 16:08Z). **No se edita.**
- **Fuente de los cambios**: `REVISION_INTEGRIDAD_PREREG_16nov.md` (polymarket-data-integrity-authority, estado AMBER), sha256 `c87d2bed21c88ae3205f163311413504b6e8818ed659a76887d8fb897e1bc099`.
- **Redacción**: 2026-11-16, 16:15-16:30Z aprox., `polymarket-quantum-alpha-miner` por encargo del chief (no autocertifica). El sha256 de este fichero va en `ADDENDUM1_PREREG_REPLAY_BRECHA_B_16nov.sha256`; la hora real del sellado es el mtime de ese `.sha256`. Este fichero no se edita después: cualquier cambio = ADDENDUM 2.
- **Estado al sellar**: 0 cifras de este programa calculadas (la Etapa 0 no se ha lanzado; no se ha abierto ningún EV, relleno ni pnl del programa). Etapa 0 autorizada al sellar; **Etapas 2-3 BLOQUEADAS** hasta ADD3 completo y paridad exacta.
- **Precedencia**: donde este addendum y el prereg choquen, manda el addendum; lo no tocado sigue igual.

## 1. Cambios exigidos por la revisión

### B-1 Validez de día (sustituye en lo que choque a §4.3 «Validez de día» y §6.1-4)
1. Regla sin cambio: día primario válido ⇔ Σ_m N_ok / 720 ≥ 0,50 **y** cov_des ≥ 0,995 (N_ok y cov_des de §6.1-2/3).
2. **La lista de días válidos se fija en la Etapa 0 ANTES de cualquier EV**: `dias_validos_E0.json` se escribe y se hashea (`dias_validos_E0.sha256`) antes de ejecutar cualquier paso que sume pnl o rellenos (identidades §6.1-6, paridad de lectura §6.1-7, Q-C, Etapas 2-3). Un error descubierto después se corrige con un ADDENDUM, nunca reescribiendo la lista.
3. **Misma regla en motor y población**: el mismo conjunto de mercados (act, fin) sanos alimenta el motor y filtra la población; los prints de mercados fuera del conjunto salen y se cuentan.
4. **hole60 = sensibilidad OBLIGATORIA**, con su propia lista de días fijada en la Etapa 0 a la vez que la primaria: huecos = saltos > 60 s entre `recv` únicos de libro5_tx del día con centinelas en 00:00 y 24:00Z (lógica literal de `prep_day2.py:20`, que lee los ficheros de D−1, D y D+1); mercado fuera si [fin−300 s, fin] corta algún (a − 60 s, b + 60 s); misma regla ≥ 50 % y cov_des. Toda cifra de las Etapas 2-3 se publica también con hole60 (G-ROB ya lo exige).
   - Para hole60 del 09-Nov la lógica literal lee los libro5_tx del 10-Nov: se usa **solo la columna `recv`** y solo las filas con recv del 09-Nov (extensión declarada de la excepción de §4.1: mismas columnas; ningún desenlace, EV ni libro del 10-Nov).
   - Control cruzado: para 02..09-Nov los huecos recalculados se comparan con `holes` de `L2/calma_v3/huecos_fix_13nov/out/meta2_<D>.json`; si difieren se publica la diferencia y manda el recálculo.
5. **Publicación**: tabla día × moneda con N_cal, N_ok, % retenido, cov_des y horas malas, para la primaria y para hole60.
6. **Declaración**: la censura por hora mala (y por hole60) es **por reloj/datos del feed** (cobertura tx_ws y huecos de recepción), fijada sin mirar desenlaces ni pnl; no es censura por resultado.

### B-2 Latencia `l = MIX` (concreta §3.3 y §13.3 B-2)
1. **Puerta**: los valores individuales reconstruidos deben reproducir EXACTAMENTE (|Δ| ≤ 1e-9) `n`, `p10`, `p50` y `p90` de `anclas_detalle.cancel_ex_menos_envio` de los tres `informe_final.json` (B2 105 / 29 / 34 / 111,4; B3 104 / 29 / 32 / 46,2; B5 104 / 29 / 32 / 41,0).
2. **Lógica** (precisión respecto al prereg, que decía «del `ledger.jsonl`»): esos campos los produce `paquete_l.py::Paquete._anclas_detalle` llamando a `vendor/plan_paquete_l.analiza` sobre `<tanda>/cancel_evid/cancel_evid_*.jsonl*`; los valores salen de `cancel_evid` y el `ledger.jsonl` solo aporta la moneda de cada oid (`post.oid → clave → intencion.coin`, como `pl_core.anclas_de_eventos`). La reconstrucción usa el vendor cargado con su verificación de sha (`pl_core.cargar_vendor`), sin escribir nada en los directorios de las tandas.
3. **Si la puerta falla en cualquier tanda** → la primaria pasa a `l = 46` fija en Q-C y en las Etapas 2-3, y se declara.
4. Se reproduce también `alta_ex_menos_envio` (control de A = 38). Si no se reproduce, A = 38 se mantiene (es el p50 publicado) pero se etiqueta «no reproducido».
5. **Pool MIX** = lista ordenada (tanda B2 → B3 → B5; dentro de cada tanda, el orden en que `analiza` recorre los oid) escrita en `experimentos/5m_barato/replay_brecha_B_16nov/etapa0/l_pool_vigente_13nov.json` con su sha256; Q-C y las Etapas 2-3 la cargan con `assert` de ese sha. El sorteo de §3.3 indexa esta lista.
6. **Sensibilidad obligatoria sin BTC** (universo del replay = ETH/SOL/XRP): `l = MIX_sinBTC`, solo anclas ETH/SOL/XRP. La revisión escribe n = 188; la aritmética de §3.3 da 313 − 126 = 187. Manda el n reconstruido, que se publica con la errata señalada. Se reporta en la rejilla de §10 y junto a G-LAT; no es condición adicional de G-LAT.
7. Etiqueta obligatoria en toda tabla con `l = MIX`: «latencia de 1 día (13-Nov) y ~2,2 h, solo clase LO; d_proc = 3 ms SUPUESTO, no medido».

### B-3 Clase de suelo (concreta §3.4, §6.1-5 y G-INT)
1. Se mantiene el criterio «día LO-puro» (0 ventanas hi e indet ≤ 5 % de las 120 que gobiernan 04:00-24:00Z) para las métricas incondicionales de variantes que solo tienen agregado diario.
2. **Día con indet > 20 %**: sale de las tablas por clase **y también del conteo de «≥ 10 días primarios válidos en LO» de G-INT**; no se sustituye ni se rellena con otro día.
3. **Días mixtos (hi y lo)**: solo por segmento (clase causal por ventana), cada clase en su tabla, nunca fusionados; nunca cuentan como LO-puros. Aclaración del alpha-miner (no viene de la revisión; la autoridad puede vetarla con un ADDENDUM): un día mixto cuenta para el «≥ 10 días LO» de G-INT solo si ≥ 50 % de sus 120 ventanas gobernantes son lo y su indet ≤ 20 %. Sus segmentos LO entran en las tablas LO aunque el día no cuente.
4. La clase se mide por ventana (nunca por fecha); la primera ventana del día es indet (§3.4).

### B-4 Discriminante (sustituye el criterio de incompatibilidad de §9.3)
1. Celda c = día × moneda (LO, día válido). **Incompatible si |Δ(c)| > 1,645 · √(se_mot(c)² + se_pob(c)²)**, con se_mot y se_pob = desviación típica bootstrap de EV_mot(c) y EV_pob(c) (pond. Σpnl/Σcoste) remuestreando **CIERRES** (`fin`) dentro de la celda, B = 10.000, semilla 20261116.
2. Se mantienen: ≥ 30 rellenos del motor y ≥ 100 prints por celda (si no, «sin potencia», contada); > 50 % de celdas con potencia incompatibles → P-NO; en caso contrario, P-SÍ (consecuencias como en §9.3).
3. Sensibilidad obligatoria: tasa de incompatibilidad con h_m (criterio original de §9.3), publicada al lado.
4. Declaración en cada tabla: motor (orden virtual de 5 acciones en cola) y población (prints) siguen siendo objetos distintos; **P-NO no prueba nada sobre B real**.

### B-5 Placebos y multiplicidad (concreta §8 y §10)
1. **Cribado**: 100 placebos por variante secundaria de la Etapa 2 (semilla 20261116).
2. **Confirmación**, declarada de antemano: solo las variantes con p ≤ 0,05 en el cribado se re-ejecutan con ≥ 1.000 placebos **NUEVOS** (semilla 20261117, sin reutilizar los 100); su p final es el de los 1.000 (p_min = 1/1001). Las que no pasan el cribado conservan su p de 100. Prohibido re-cribar con otra semilla.
3. **BH-FDR q = 0,10 sobre los 18 contrastes secundarios** con esos p; max-statistic dentro de cada familia como en §10. Familias y K sin cambio: P (K = 4, Bonferroni 0,0125, solo el contraste de §7.2), X 3, F 3, T 3, Q 1, R 2, S 2, C 4. No se añaden variantes.

### B-6 Recursos de las Etapas 2-3 (aprobado; §13.3 B-6 y §15)
1. Sin cambio: `ulimit -v 6000000`; guardia propia MemAvailable ≥ 5.500 MB en tres lecturas antes de cada día; corte si < 2.500 MB o RSS > 3,6 GB; un día cada vez; ADD3 primero y nunca a la vez que otro pesado; nunca 06:00-09:30Z; `choom -n 500`.
2. **Añadido**: la guardia propia **prevalece** sobre el semáforo `scripts/cron_pesado.sh`. Si el semáforo «corre igualmente» tras su espera de 10 min sin que la guardia propia se cumpla, el job **aborta** (no espera ni corre) y se reintenta más tarde.
3. Excepción de RAM autorizada por Javi el 16-Nov (§3).

## 2. Reordenación de etapas (sustituye en lo que choque a §6, §7.1, §8 y §8.1)
1. **Etapa 0** (§6.1 con B-1 y B-3): días válidos, primaria y hole60, fijados y hasheados antes de cualquier EV. Después, identidades SEGT↔CX y paridad de lectura, publicando solo booleanos y diferencias más la cifra agregada ya publicada. Clase por día en cuanto ADD3 la produzca. Reproducción de paquete_l (B-2). Si ADD3 no ha producido la clase, la Etapa 0 queda PARTIAL (días fijados, clase pendiente).
2. **Q-C** (§7.3): CPU≈0, con δ vigente (MIX si B-2 pasa; si no, 46) sobre las 3.796 órdenes reales. Explicativo, EXPLORATORY. Su corte por clase necesita ADD3 de 20 y 21-Oct, hoy pendientes (22 y 23-Oct COMPLETE); sin ellos, ese corte queda pendiente y la cifra total no se bloquea.
3. **ADD3 completo**: `pob_add3` COMPLETE para 26-Oct..09-Nov (clase del replay) y 20-21 Oct (clase de Q-C). Requisito previo a la paridad (B-6: nunca a la vez).
4. **Paridad** (§8.5): A = 68, l = 60, 26-29 Oct, reproducción exacta de `R` y `A` de `CX_v3dd`; stop rule sin cambio.
5. **Etapa 2**: A = 38, l = MIX (o 46 según B-2), una pasada por día. Se guarda **cada segmento** con `t_dec, t_arr, t_end, L, q, tf, canc, clase causal, rama de sello` (§8.1). T1 (s = 1 frente a s = 5) sale de esta pasada con SIZE parametrizado.
6. **Etapa 3**: sin cambio.
- **Eliminados**: §7.1 (G0 partido por `kt` con A = 68) y §8.4 (tamaño ≤ 5 desde SEGT), como etapa previa y como criterio de prioridad. La Etapa 1 queda reducida a Q-C. La regla «Uso» de §7.1 queda sin efecto: P2 se calcula en la pasada única de la Etapa 2.
- **Retiradas de §8**: las «variantes ya calculadas (regresión)» con A = 68 (CXB60/100/150, TOP60, CXB60r, F5A, F5B, GEO1_F5A) y sus 20 placebos, salvo como control de paridad (§8.5).
- **Identidades SEGT↔CX** (§6.1-6): pasan de puerta a control descriptivo (SEGT ya no alimenta ninguna cifra). La verificación SEGT ⊆ N_ok (§6.1-2) y la paridad de lectura (§6.1-7) siguen siendo parte de la puerta de la Etapa 0.

## 3. Decisiones de Javi (16-Nov), ya tomadas
1. **HOLD 10-14 Nov**: se mantiene sin usar (§12 sin cambio).
2. **Excepción de RAM de B-6**: autorizada.
3. **Anclas HI con dinero real**: NO por ahora (la wallet dedicada tiene céntimos). Todo lo HI sigue DATA_BLOCKED. Se vuelve a decidir tras la Etapa 2 en LO.
4. **Dry-run nuevo**: se decide conjuntamente con Javi cuando una palanca sea PROMISING (§12 y §13.4-4 quedan así).
- §13.4-5 (conservar los datos de los días ≥ 15-Nov) sigue pendiente del chief.

## 4. Ejecución de la Etapa 0 y de la reproducción de paquete_l
- Por encargo expreso del chief (16-Nov), las ejecuta el alpha-miner con código nuevo de solo lectura que no importa el motor ni lee `ms2`. Las Etapas 2-3 siguen siendo de `cheap5m-execution-engineer` (§15).
- **Recursos** (sustituye, para la Etapa 0 y Q-C, la condición «load5 ≤ 4» de §15): `nice -n 19 ionice -c3`, `ulimit -v 3000000`, < 5 min de CPU, RSS < 0,5 GB, fuera de 06:00-09:30Z, MemAvailable ≥ 2,5 GB, carga medida **por núcleo** (load5/nproc ≤ 3). Motivo: trampa del CLAUDE.md raíz del 04-Nov (con nproc = 8, una puerta absoluta load5 < 4 no se abrió en 9 días). Sin tocar ADD3 ni competir con él.
- **Salidas** en `experimentos/5m_barato/replay_brecha_B_16nov/etapa0/`: el código, `dias_validos_E0.json` + `.sha256`, la tabla día × moneda (primaria y hole60), y `l_pool_vigente_13nov.json` + `.sha256` (oid, tanda, moneda y valores) con el resultado de la puerta B-2.

## 5. Sin cambio
Todo lo demás del prereg: sellos §3.2, latencias derivadas §3.3 (salvo B-2), soporte §4.5, desenlace §4.4, métricas §5, palancas §8 (salvo lo retirado), etiquetas §11, HOLD §12 y fuera de alcance §14.
