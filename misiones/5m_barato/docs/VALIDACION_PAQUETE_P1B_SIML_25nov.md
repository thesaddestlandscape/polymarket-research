# VALIDACION_PAQUETE_P1B_SIML_25nov — statistical-validator, 25-Nov 17:05-17:40Z (guardado por el chief: el validador es de solo lectura). Solo lectura, 0 órdenes, <0,5 GB.
Repo /root/polymarket-research-dev-bk, rama b-k-ejecutor, def867fc937..4baf998aa91. Manda CONTRATO_D3_SIML_P1_25nov §1-§7 + RESOLUCIONES. Suite: `pytest -q test_*.py` → 418 passed (197 s, RSS máx. 459 MB).
Rutas relativas a experimentos/5m_barato/b_k_ejecutor/ salvo suelo_v34.py (raíz).

## 1. Seco modo A (analiza_seco_a.py) — AMBER
- Bien: KS por bins de 0,25 ms exacta en bordes; D_sup conservadora +0,0025 (masa máx. por bin 0,0056) ⇒ empates no dan PASA en falso; percentil interpolado OK; C5 por media por minuto OK; lag rx→observa ≈0 (p99 1 ms).
- Dependencia: D<0,10 es tamaño de efecto, no p-valor; con n≈10^5 el ruido (~0,01) < variación entre tramos.
- H1 (PASA en falso): sin puerta de duración/cobertura (`duracion_min` leído y no usado l.346-350; bastan 60 min de CPU l.175; falta de k_resumen solo marcada l.325). Arreglo: INSUFFICIENT si no hay k_resumen o minutos_validos < 0,9·duracion_min (216).
- H2 (agregado que engaña): humos 16:02/16:45: D agrupada 0,092/0,103; SOL 0,127/0,143; XRP 0,083/0,106; p50 44/43 vs 53 esperado; 2,7-3,1 % de lags <3 ms. Causa: 11-15 % de decisiones despertadas por Binance (lag p50 ~20 ms) reinician la fase; siml.py:8 «no modelado». Arreglo: publicar D/p50/p90 por moneda; SIM-L con brazo «L4 medida» (histograma).
- H3: C1 cuenta cambios; §1(a) dice decisiones. Añadir n_decisiones ≥300 y ≥100/moneda.
- H4: criterio (e) vivo=batch ≥99 % no se calcula: veredicto «PASA (a)-(d); (e) pendiente de P4(iii)».
- H5: seco_modo_a_noche.sh sin commitear (--suelo-v34). [RESUELTO por el chief: commit ccb5e375809, 17:15Z]

## 2. P1b (analiza_p1b.py) — AMBER
- Bootstrap por orden válido DENTRO de cada run (ac1 −0,035..0,014; bloques de 10 misma anchura). DELETE del ledger = d_red_cancel_ms. Regla §6.1 bien (l.164-182).
- H6: p50 de los runs de referencia 63,1/59,3/60,2 ms; dejar-uno-fuera: B2 vs B3+B5 Δ=+3,14 IC90 [1,69;4,78] → FALLA/AMBER sin cambio real; B3 IC90 [−3,33;−0,57] → no PASA. Arreglo: FALLA y PASA(L1) solo si CADA run de hoy por separado cumple la rama (|Δ|>3, IC90 excluye 0, mismo signo); si no, AMBER. Publicar Δ por run y franja y la calibración de la referencia contra sí misma; post_block_ancla_ms por franja.

## 3. P1a (analiza_p1a.py) — AMBER
- H7: correlación sobre NIVELES (l.230-233); el contrato dice Δ. Arreglo: primeras diferencias entre horas consecutivas como criterio; niveles como sensibilidad.
- H8: load5/swap no se controlan. Arreglo: r parcial con load5 o excluir horas con load5/nproc>1,5.
- H9: `abs(rzy)` (l.240) acepta r negativa como «reloj propio». Arreglo: rzy ≥ +0,6.
- H10: cambios de ref_id de chrony no marcan el día. Arreglo: marcarlo.
- Primer día COMPLETE 26-Nov; veredicto con 3 días, como pronto 29-Nov 00:40Z.

## 4. v3.4b (suelo_v34.py, test_suelo_v34.py) — GREEN
- Causal (batch j∈[B−60,B−2] l.92-98; vivo H60 l.77); tests (a)-(j), P4(i) 10^4 y mutación (h) pasan; 7j reproduce 0,56 %/0,03 %.
- Paridad vivo=batch con el día ENTERO: 16, 17 y 24-Nov × ETH/SOL/XRP = 77.760 bins, 0 diferencias, 651 activaciones (16-Nov).
- Declarar: pérdida medida en bins de 10 s, no en w0 operados; par con p5 ≥45 también da mixta (fail-closed); P4(iii) pendiente.

## 5. SIM-L (siml.py, siml_run.py, out_siml_25nov/siml_2026-11-17.json) — AMBER
- E0 OK en conteos (K1 8.272/26, K6 5.291/20); E2 precintado (sin pnl/coste). Parámetros por medición.
- H11: JSON sellado con código previo a v3.4b y sin commitear (sha_siml d14c179c, sha_suelo_v34 9417e83e, git 5177abf); no reproducible desde HEAD. Arreglo: re-correr e0+base en HEAD vía cron_pesado + `git_dirty` en el manifiesto.
- H12: «bit a bit» = solo igualdad de `ordenes` (siml_run.py:152). Arreglo: hash de la tabla de órdenes contra out_paridad_17novordenes_K1_2026-11-17.pkl y rellenos en `ok`.
- H13: L4 omite el reinicio de fase por Binance. Brazo «L4 medida» antes de firmar PREREG_SIML.

## Orden de arreglo
1. Antes de 22:35Z: H1, H3, H2 (decisión del chief). 2. Antes de firmar PREREG_SIML: H11, H12, H13. 3. Antes del run real de P1b: H6. 4. Antes del 29-Nov: H7-H10.

## Decisión del chief sobre H2 (25-Nov ~17:20Z, antes de las 22:35Z y sin ver la noche)
- El criterio C4 se mantiene como estaba fijado (D agrupada < 0,10). D, p50 y p90 por moneda se publican como informativos: hacerlos decisorios ahora sería elegir el criterio tras ver los humos.
- SIM-L: L4 PRINCIPAL = distribución MEDIDA en el seco de esta noche (por moneda, incluido el reinicio de fase por Binance); U(3,103)+3 queda como brazo. Es medición, no EV. Si el seco sale INSUFFICIENT, L4 principal = U(3,103) declarado y el brazo medido se añade en cuanto haya seco válido.

## RE-PASADA 25-Nov (statistical-validator, 17:44-18:00Z; HEAD 19a764c6fb8, árbol limpio; suite 444 passed; solo lectura, 0 órdenes)
- Seco A — GREEN de código, pendiente de dato (at 76, 22:35Z → veredicto 26-Nov ~02:45Z). H1-H5 verificados.
- P1b — AMBER (1 línea): `cumple_rama` hace `dr["delta_p50_ms"]` sobre `dict(delta_run(...) or {}, franja=f)`; el `or None` de l.274-275 nunca se dispara → con un run de <8 altas KeyError en vez de INSUFFICIENT. Arreglo: en `cumple_rama`, False si falta "delta_p50_ms". Residual declarado: B2 vs resto Δ +3,1 IC90 [1,7;4,8] ⇒ el aviso «referencia no estable» saltará siempre. Con el arreglo: GREEN de código, pendiente del run real.
- P1a — GREEN de código, pendiente de dato (días 26-28 Nov; veredicto ≥29-Nov 00:40Z). Residual: con carga 1,1-1,25/núcleo el filtro casi no excluye horas; p5 cuantizado a 1 ms ⇒ probable INDETERMINADA (decide P1b).
- v3.4b — GREEN (sha a385c9e3).
- SIM-L — E0 y H11 GREEN (K1 hash b1f234ac680cfeca = firmado; K6 solo conteos; head_run git_dirty=false; base K1 6.481/32, K6 4.146/18 idénticos). H13 RED: el brazo «M» sortea un retraso por CADA cambio de libro y el vivo decide todos los cambios de un ciclo de 100 ms a la vez (humo 16:45, n=1.546 lotes: primer cambio del lote vivo p50/p90 70,8/98,9 ms vs 25,2/67,4 con M; 5,7 decisiones por lote vs 1) ⇒ sesgo optimista; además cuenta dos veces Binance y pone dec_rx=0. Arreglo: retirar M; L4 «A-reinicio» = rejilla de 100 ms re-anclada en cada evento Binance (+3 ms), monótona y con agrupado; el histograma del seco pasa a objetivo de VALIDACIÓN (KS sim vs seco por moneda, D<0,05, fijado antes de mirar). Hasta entonces, L4 principal = U(3,103)+3 (A) declarado. Ningún corrido ha usado M.
- Para GREEN total: arreglo de P1b + H13 rehecho (antes de firmar PREREG_SIML); luego los datos en sus fechas.

## COMPROBACIÓN FINAL 25-Nov (validador, 18:19-18:28Z; HEAD 18970b505bb limpio; suite 455 passed)
- P1b: GREEN de código, pendiente del run real. dec_r (A-reinicio): mecánica correcta (+3 ms también en extra_events, agrupa por ciclo, monótona, no duplica Binance, anclas = saltos de todas las monedas como el vivo).
- AMBER 1, siml_valida_l4.py: la traza del sim mete TODOS los cambios de top; el seco solo cuenta cambios con bid en BAND_Q (0,03-0,45) atendidos por armado → «cambios por lote» fallaría por construcción. Arreglo: filtrar en lotes_de_traza los x con bid de top en BAND_Q (m.top(k,x)).
- Pasada muerta (pid 880798, 18:01-18:10Z): la mató guard_ram_fase0 (SIGKILL vía cgroup.kill; SIM-L 3,97 GB + shadow_postmortem ~3,2 GB desde 18:08:47). No es OOM del kernel ni timeout. El lanzador NO da por buena una corrida muerta (JSON PARTIAL); la reanudación reutilizó brazos COMPLETE del mismo HEAD limpio: válida.
- AMBER 2, trazabilidad: lanza_siml.sh abre siml.log con `>` (el relanzamiento borró la prueba) y no anota rc; cron_pesado.log no escribe FIN ni rc; la reutilización de brazos compara solo cfg, no el código. Arreglo: git/sha_siml/pid por brazo y no reutilizar si difieren; logs con `>>` y cabecera; rc anotado; lanzar SIM-L fuera de la hora del postmortem.
- Por pieza: Seco A GREEN de código (dato 26-Nov ~02:45Z); P1b GREEN de código; P1a GREEN de código (29-Nov); v3.4b GREEN; SIM-L E0/H11/dec_r GREEN, faltan AMBER 1 y 2.

## DATOS 26-Nov (agente de datos, paso 0; solo lectura)
- Seco A 25-Nov 22:35Z → 26-Nov 02:40Z, HEAD 3d24707cf46, experimento_maker_bk.py sha16 ac7f023fa907552d limpio, v3.4b activo (par_hi 138/138). C0-C5 PASA: n=133.901 cambios / 23.833 decisiones (eth 10.267, sol 6.926, xrp 6.640), 0 duplicados, 245/240 min.
- Relojes: rx local + monotónico; sin E de Binance ni sello de lote. C2 p50 47,97 · C3 p90 90,5 · C4 D 0,053 vs U(3,103) · CPU p95/min 17,3 %. La cadencia real es algo más densa que U(3,103): SIM-L se valida contra lo MEDIDO.
- libro5 activo sin pausa (libro5tx 73-92 % de la mediana, no degradado); HC 33 GB libres.
- Clases: 126 lo, 12 indet (arranque en frío), 0 hi, 0 mixta; p5 15-18 ms. La noche NO ejercita hi/mixta.
- AMBER: episodios_hi marca 97/126 ventanas lo con «nolo» (mezcla hi con tráfico insuficiente) → columna `motivo` antes de aplicar la regla >5 % → v3.5.
- d_env: p50 6,88 ms, p90 12,5, n=699; firma local 6,06 ms (cota inferior). SIM-L usa 3 ms y brazos {0,10} → principal 7, brazos {0,3,10,12,5} (medido, no elegido por EV).
- (e) paridad de clase vivo=batch ≥99 % pendiente del npz del 26-Nov (P4(iii)).
- KS SIM-L vs seco: necesita 25+26-Nov completos y manifest_suelo_2026-11-26 COMPLETE → 27-Nov ≥09:20Z vía cron_pesado (dueño chief). Declarar si el sim modela las 1.286 decisiones de causa binance (5,4 %). Si FALLA: fallback ya declarado U(3,103)+3.
- Pendientes engineer: manifest con sha de suelo_v34.py/siml.py + dirty global de tracked; `motivo` en episodios_hi; d_env principal 7 en SIM-L.

## RED-TEAM 26-Nov (adversarial, solo lectura, 0 órdenes; tests no corridos por franja 06-09:15Z)
- ALTO-1 P1b: `p1b_paquete.py --real` directo + confirmación válida commiteada se salta ok-javi/franja/2 por día/gasto previo/vigilante → total >0,15 $ (hasta saldo 0,51). `--out-base`/`--paquete` en real eluden el recuento y el wrapper_sha16. Reparar antes de cualquier envío.
- MEDIO P1b: corte a 16 min (B2 tardó 28) → PARTIAL → INSUFFICIENT; nunca probado en seco. Lote 3/3 vs ref 8/12 (composición ≈ +0,4 ms) y GTD (P1b) vs GTC (ejecutor) no declarados.
- MEDIO analiza_p1b: no verifica config_sha P1b ni hoy∩ref = ∅ (B3/B5 como hoy = PASA falso); la rama L1 sale como «PASA».
- MEDIO SIM-L KS: `--dias` sin cruzar con el manifest del seco; puerta manifest_suelo sin cobertura horaria (25-Nov: 15,5 M filas q sin mapa).
- MEDIO seco: cron 00:10Z suelo_p5_directo (308 s, sin nice) dentro del seco → C2/C3/CPU/KS contaminados; mover a ≥03:00Z.
- MEDIO trazabilidad: seco con pins_ok=False; manifest_codigo y reutilización sin rf5_core/calma/variantes_b/polygon_rpc ni npz.
- MEDIO v3.5: motivo_episodio con desempate anti-hi; columna `sin_dato` = no evaluable, no «0 hi».
- BAJO: launch muerto sin informe_final bloquea P1b (documentar desbloqueo); Binance del SIM-L con reloj del grabador (declarar); env BINANCE_WS_URL/BK_DATALOGS.
- Limpio: el seco no puede enviar, firmar con clave real ni leer credenciales; v3.4b sin look-ahead y con paridad; E2 precintado; d_env medido.

## RED-TEAM verificación 26-Nov ~08:15Z (0cff86debec..18ecd170b98)
- Cerrados: P1b 30 min + lote/GTD, analiza_p1b INVALID/PASA_L1, KS días+cobertura, v3.5 (esencial). Pins: 10/10 = FICHEROS_PIN, limpios, = paridad K1/K6.
- Parciales/nuevos: NUEVO-1 MEDIO (--out de un run previo se excluye del recuento → salta gasto previo/2 por día; cierra ALTO-1); NUEVO-2 MEDIO (módulos importados por el vivo fuera de pins: eng_v5, ejecutor_puro, engine_v3/v4, engine_clock, relojes, stamp_v3, engine.py/capt.py de dev); NUEVO-3 MEDIO (sello KS solo hashea siml_valida_l4.py); seco 25-Nov coincidió con suelo_p5_directo 00:10Z. BAJO-1..5 (pos −1 en sensibilidad, sin_dato en denominador, marcador de uso por sha del fichero, sin duración máx. en wrapper directo, paquete_vivo con timeout/bash -c). BAJO-6 falso: suelo_p5_directo.sh ya aplica nice/ionice dentro.
- SIM-L: brazos de out_siml_25nov no reutilizables (sin sha por fichero) → re-correr.
- Veredicto: NO listo para /code-review hasta NUEVO-1 (NUEVO-2/3 baratos).

## /code-review medium 26-Nov ~09:00Z (def867fc937..1cd165349e0) — 4 importantes + 6 nits
- IMP-1 experimento_maker_bk.py:839: verifica_pins_cargados tras crear el cliente real → import live_trade de PRODUCCIÓN + ~10 módulos no pinneados → todo run real B-K sale con sys.exit.
- IMP-2 p1b_lanza.py:98: un intento real rechazado por el wrapper (rc 3) deja p1b_real_* solo con meta → cuenta como run + 0,15 $ de gasto → bloquea P1b para siempre.
- IMP-3 p1b_lanza.py:275: inicio_utc se sella antes de dos cadena_subproceso → con carga, >300 s → el wrapper rechaza su propio directorio (y se combina con IMP-2).
- IMP-4 siml_valida_l4.py:157: KS compara poblaciones distintas (sim = todos los cambios en banda; seco = solo en decisiones de armar).
- Nits: franja_ok sin margen de parada (~+6 min); _dec_causa_libro consume pendientes de ambos tokens; HistLag.vuelca en el hilo de decisión; manifest() del seco puede escribir JSON inválido; pins con rutas absolutas (merge a main = re-pin); SIM-L v3.4 por defecto vs ExpBK v3.3 por defecto.

## RED-TEAM verificación fixes /code-review + desacople (26-Nov ~10:00Z, c5f9f3c6348)
- IMP-1..4 y 6 nits CERRADOS; desacople correcto (46 módulos, 0 de producción raíz; parche idéntico a live_trade); pins 50 cubren ejecutor+SIM-L.
- MAJOR: la KS del 27-Nov 09:25Z (at 83) necesita tape_2026-11-26.pkl, que run_rf5.sh genera el 27-Nov 12:30Z → reprogramar ≥14:00Z + puerta BLOCKED si falta cinta. Choca con la firma PREREG_SIML antes de 12:30Z.
- MODERATE: no lanzar P1b real con SIM-L vivo (siml.pid).
- MINOR: comentario desfasado experimento_maker_bk.py:866; docstring manifest_codigo.py:188 (5 pins de l2_carrera en producción); declarar que P1b se protege con VENDOR_HASHES/paquete_sha16, no con los 50 pins. vigia_bk_pins movido a 09:30Z (chief).
- Veredicto: listo para P1b real y firma, con P1b sin solape con SIM-L y at 83 reprogramado.
