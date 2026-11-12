# SPEC de prerregistro MULTIVARIANTE B-CXB (BORRADOR del execution-engineer, 12-Nov-2026) — para que el statistical-validator lo corrija y lo congele
**Estado: NO congelado, NO desplegado. Nada de esto es resultado ni alfa; no autoriza ningún envío (el dry-run solo simula).** Amplía `PREREG_CXB60_FORWARD.md` (borrador v1, hipótesis única CXB60 ETH/SOL/XRP). Código: `dryrun/cxb60_dryrun_fase0.py` (VERSION `cxb60_dryrun_v3`), `cxb60_core.py`, `cxb60_io.py`, `l_pool_emp.json`, `frozen/*` (9 ficheros hasheados en `dryrun/HASHES_CONGELADOS.json`; el runner aborta con exit 3 si difieren). Informe: `dryrun/cxb60_informe.py`.

## 1. Poblaciones y variantes (mismos datos, un proceso)
- **Primaria**: ETH, SOL, XRP (5m, cada token YES/NO = unidad de mercado). **Subvariante BTC**: población APARTE (`--coins BTC --clave-valido dia_valido_btc`); nunca se mezcla con la primaria (el agregado primario excluye BTC por construcción).
- **Colocación** (idéntica a v1): L ∈ {0,10; 0,13; 0,16; 0,19}, 5 acciones, GTC post-only maker virtual; entrada = gate G0 [b15 finito, vol30 ≥ 26, hora UTC ≥ 4, b15−L ≤ 0,03] ∧ ask_rx > L ∧ bid_rx(t−300 ms) ≥ L+0,01; salida por gate falso (+60 ms), T ≤ 61 s o cancelación; re-armado con la regla de entrada.
- **Variantes** (todas con el mismo disparo `bid_otros_rx < L`, cancelación efectiva = rx del disparo + l):
  | Variante | l | Papel |
  |---|---|---|
  | `GEO1` | sin cancelar | CONTROL de igual colocación |
  | `G0` | sin cancelar, sin armado | referencia descriptiva |
  | `CXB35`, `CXB45` | 35 / 45 ms | dosis-respuesta (descriptivas) |
  | **`CXB60`** | 60 ms | **primaria** (H-CXB60-FWD, ya descrita en v1) |
  | `CXB100`, `CXB150` | 100 / 150 ms | **solo control** de dosis-respuesta (G8) |
  | **`CXBEMP`** | l realista: 3 ms (d_proc declarado, NO medido) + valor del pool de 1.453 anclas propias (`l_pool_emp.json`: p50 40,9 ms, p90 96 ms, máx 1.750 ms), un sorteo determinista por segmento (`default_rng([clave_token, round(L·100), n_segmento, 7919])`) | secundaria (H-CXBEMP-FWD) |
  | `PLC60_s` (s = 1..100) | cancelación en instante uniforme del segmento si el disparo de CXB60 existiría | placebo de igual cobertura (≥ 100 semillas) |
- Escenario `c19` (sello de cinta WS = ex−19−1, primario) y `c59` (pesimista, G7) en el MISMO proceso (sin placebo en c59).
- Fuera de cualquier puerta: CXB35/45/100/150, G0, desglose por L.

## 2. Hipótesis (jerarquía propuesta; la fija el validador)
1. **H-CXB60-FWD** (primaria, población primaria): EV ponderado por € (Σpnl/Σcoste, rebate maker 0,2·0,07·L(1−L) incluido) de CXB60 > 0 y mayor que GEO1.
2. **H-CXBEMP-FWD** (secundaria, solo si la 1 pasa; si no, descriptiva): ídem con CXBEMP (el l que un ejecutor real tendría si d_proc ≈ 3 ms y la red como las anclas).
3. **H-CXB60-BTC-FWD** (subvariante, población BTC; **sin evidencia TRAIN**: BTC no está en el npz TRAIN ni en `CX_v3dd`; todo dato BTC es exploratorio hasta el forward). Mismas puertas que la 1 sobre la población BTC. Propuesta: control de multiplicidad por *gatekeeping* jerárquico (1 → 2 → 3, α_IC90 en cada eslabón) o Bonferroni ×3; decisión del validador.
- **Dosis-respuesta en l** (descriptiva): EV(CXB35..150) y Δpnl diario vs GEO1 con IC90 por días + Spearman EV~l (5 puntos). Expectativa pre-declarada: EV no creciente con l; si CXB60 pasa pero solo CXB35/45 → «condicionado a l», no apto para ejecutar sin medir d_proc (G8).

## 3. Métricas C5 (las que sale `informe_cxb60*.json`; TODAS con desenlace OFICIAL, cobertura ≥ 99 % de rellenos; relleno sin desenlace = excluido y contado, missing ≠ 0)
P(fill) por colocaciones y por cantidad · EV incondicional (Σpnl/Σcoste potencial) · EV|fill ponderado por € (métrica de puertas) y por unidad · pnl por mercado procesado · n de cierres con relleno · IC90 bootstrap por CIERRE y por DÍA (razón, 2.000 réplicas, semilla fija) · EV sin los 2 mejores días y cuota del mejor día · desglose por moneda y por L · placebo p = (1+#{EV_placebo ≥ EV})/(1+S) con S ≥ 100 · c59 por variante · `dosis_respuesta_l` · cobertura por día/moneda (`coverage_<D>.json`) y motivos de no colocación (`nof`) · calidad del feed (`mkt`: huecos ≥ 5 s, edad de W) · `cpu_advance_us` del heartbeat.

## 4. Puertas (heredan G1–G8 de v1, ahora POR POBLACIÓN y por variante)
G1 n ≥ 40 rellenos resueltos y ≥ 10 días UTC válidos (dia_valido: cobertura ≥ 0,95 en cada moneda de la población; el día no completo no cuenta). **«Forward limpio» = ≥ 10 días válidos consecutivos o no, tras congelación Y despliegue**; los días previos son exploratorios.
G2 EV ponderado > 0 con IC90 por días y por cierres con extremo inferior > 0. G3 Δ pnl diario vs GEO1 > 0, IC90 por días > 0. G4 EV sin los 2 mejores días > 0. G5 placebo p ≤ 0,05 con S ≥ 100 (y PLC60 no ≈ CXB60). G6 ninguna moneda > 60 % del coste (en BTC: n/a, una moneda; se sustituye por «ningún día > 25 % del pnl positivo») y ningún día > 25 % del pnl positivo. G7 signo de c59 = signo de c19. G8 EV(CXB100) ≥ −0,05 si CXB60 pasa.
Resultado: PASS / FAIL (G2 o G3 con IC90 superior < 0, o G5 refutado con n ≥ 40) / INSUFFICIENT. **PASS ≠ rentable: solo habilita proponer a Javi un micro-ensayo real con tope**, tras auditoría independiente (red team) y medición de d_proc real.

## 5. Operativa y límites declarados (para el validador)
- Un único contraste primario; el resto son descriptivos o van tras la puerta jerárquica. Sin ventanas de tuning: L, size, TMIN, LAT_POST, SETTLE (2 s), c_print, gate, pool y PROC_MS son fijos = manifiesto.
- Recursos: `--max-rss-mb 3000` (exit 4), RSS medido y `cpu_advance_us` del benchmark en el informe de ingeniería; 108 especificaciones × 4 L × 4 monedas con features compartidas por token.
- Debilidades heredadas de v1 §6 (l real con n pequeño; nivel de EV = índice, no previsión en euros; cinta WS sin firma exacta; «bid sin nosotros» no modelado porque no hay orden propia; cola BASE) + nuevas: (a) el pool de l mezcla anclas de Sonda (30-Oct..04-Nov) y B (22-23-Oct) y PROC_MS = 3 es un supuesto; (b) CXBEMP usa otra secuencia pseudoaleatoria que `passT_cxb_l.py` (misma distribución, no reproduce bit a bit sus números TRAIN); (c) BTC sin TRAIN; (d) 4 monedas del mismo cierre = un clúster (IC por cierre y por día, no por mercado).
- Decisiones abiertas para el validador: jerarquía/α entre las 3 hipótesis; si G6 se aplica en BTC; mínimo de semillas del placebo en BTC (100 por defecto); si el criterio «≥ 10 días» se exige también por variante secundaria.
