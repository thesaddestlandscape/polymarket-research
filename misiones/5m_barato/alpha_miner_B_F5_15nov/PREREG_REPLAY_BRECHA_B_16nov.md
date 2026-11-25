# PREREG_REPLAY_BRECHA_B_16nov — programa de REPLAY/DIAGNÓSTICO sobre el motor v3 para localizar y cerrar la brecha de B

- **measurement_id**: `BF5-REPLAY-COLOC-v1` (sucede al `BF5-REPLAY-COLOC-v0` que propuso, sin contrato escrito, `INTEGRIDAD_REPLAY_COLOCACION_16nov.md`, sha256 99f6dbff41009aab…).
- **Redacción**: 2026-11-16, 13:00-14:30Z aprox. Autor: `polymarket-quantum-alpha-miner` (no autocertifica). El sha256 de este fichero va en `PREREG_REPLAY_BRECHA_B_16nov.sha256`, escrito al final y sin editar después; la hora real del sellado es el mtime de ese `.sha256`.
- **Estado**: escrito ANTES de calcular ninguna cifra de este programa. **BLOQUEADO** hasta que (i) `polymarket-data-integrity-authority` revise este documento y apruebe los puntos bloqueantes B-1..B-6 (§13.3) y (ii) el chief dé el OK. Cualquier cambio posterior = ADDENDUM con fecha y sha propios; este fichero no se edita.
- **No autoriza**: órdenes, firmas, cancelaciones, movimientos de fondos, lectura de `.env`, tocar el dry-run `cxb60dry`, ficheros congelados (`dryrun/frozen/*`, `HASHES_CONGELADOS.json`, `l_pool_emp.json`, vigías V2-V7/FV/H5M), `/root/polymarket-research-dev` (solo lectura), producción, `data/live/` ni módulos compartidos.
- **Etiqueta de todo resultado**: EXPLORATORY (techo PROMISING). Ninguna cifra de este programa es confirmatoria (§1.4).

## 0. Declaración de lo visto antes de escribir (transparencia)
Solo lectura, 0 procesos lanzados. Miré: (a) estructura y columnas de los pkl de §2; (b) **recuentos de SEGMENTOS** de G0 por distancia al bid (`kt`, §7.1), sin mirar rellenos, `gana` ni pnl por tramo; (c) listas de horas malas `bad_<D>.json` (§4.3); (d) perfil de suelo de ADD3 del 27-Oct (89 lo / 54 hi / 1 indet); (e) al comprobar la paridad existente vi el EV diario de G0 en `dryrun/out_replay/replay_2026-10-2{6,7,8,9}.json` (+0,242; −0,358; −0,246; −0,013), ya contenido en el G0 publicado (−0,154; 3/15 días+). **No se ha calculado ninguna cifra** de colocación relativa al bid, CX con latencia vigente, F5C en el motor, cola, tamaño, salida, régimen ni población con sello tm3.

## 1. Mandato, punto de partida y límites
### 1.1 Mandato (Javi, 16-Nov)
Saber de DÓNDE viene la brecha de B y CERRARLA. «No vale un no»: la población (+0,185 ponderada por el coste de B; −0,180 agrupada) debe hacerse alcanzable por nuestro motor/ejecución. La línea base a mover es el motor G0 (−0,154). Cada negativo es la siguiente variante, no un cierre.

### 1.2 Hechos de partida (verificados hoy en sus ficheros)
| Hecho | Cifra | n / periodo | Fuente |
|---|---|---|---|
| B real, sello tm3 | EV pond. −0,0724 sin comisión ni rebate (PnL −16,02 € / 221,30 €) | 215 fills, 202 unidades (mercado-lado), **112 cierres**, 4 días 20-23 Oct, 100 % R1 por calendario | `exp1/E6_brecha_add2.txt` |
| B real con rebate 0,2·0,07 | EV −0,0615 (la diferencia con −0,0724 ≈ rebate ≈ +0,011/€ a p≈0,22) | 3.796 órdenes, 20-23 Oct | `L_REAL_Y_DRYRUN_CXB60_11nov.md` §5 |
| Población tipo B en las celdas de B | +0,1853 pond. por coste de B / −0,1796 agrupada | 12 celdas día×moneda, 9.269 prints | `exp1/E6_brecha_add2.txt` |
| Concentración de la población | sin 10-21 XRP → +0,076; sin además 10-22 ETH → +0,001; por día −0,222 / +0,510 / +0,157 / −0,152 | 12 celdas, 4 días | aritmética rehecha hoy sobre las celdas publicadas de E6 (coincide con INTEGRIDAD Q3) |
| Motor v3 G0 (virtual, 5 acc., cola BASE, `t_arr = t_dec+68`, tm3) | 47.470 segmentos, 4.601 rellenos, coste 3.422 €, pnl −527,8 €, EV −0,154, IC90 días [−0,259; −0,046], sin 2 mejores −0,223, 3/15 días+ | TRAIN 26-Oct..09-Nov, 15 días | `PASS_T_V3_RESULTADOS_11nov.md` §4 (L_REAL §3 da IC90 (−0,261; −0,048): otro remuestreo, misma cifra puntual) |
| Control GEO1 (G0 y bid(t−300) ≥ L+1 tick) | 4.346 rellenos, EV −0,146 | 15 días | L_REAL §3 |
| CXB60 (l=60 supuesto, `t_arr`+68) | 882 rellenos, EV +0,135, IC90 días (−0,002; +0,282), sin 2 mejores +0,040, 8/15 días+; Δpnl vs GEO1 +552,9 € (13/15) | 15 días, K=10 variantes | PASS_T_V3 §5 |
| Motor sobre las órdenes reales de B | sim −0,222 vs real −0,061; 70 TP (−0,106 vs −0,108), 12 FP (−0,989), 132 FN | 3.796 órdenes 20-23 Oct | L_REAL §5 (δ=40 ms circular, hoy obsoleto) |

### 1.3 Pregunta operativa
En las MISMAS celdas día×moneda×clase de suelo, con el MISMO sello (tm3), la MISMA banda de precio y la MISMA regla de horas malas: (Q-A) ¿es alcanzable la EV de la población por una orden virtual de 5 acciones en cola (discriminante, §9)? (Q-B) ¿qué parte de la distancia motor→población cierra CADA palanca (colocación ex ante, cancelación con latencia vigente, F5 como filtro y como disparador, cola, tamaño, salida tras relleno, régimen, combinaciones)? (Q-C) ¿cuánto de la brecha de NIVEL motor-vs-real de B explica la carrera de cancelación con δ vigente (no circular, §7.3)?

### 1.4 Lo que este programa NO puede dar
Confirmación. El TRAIN 26-Oct..09-Nov ya se usó para elegir CXB60, la curva de l y K=10 variantes (PASS_T_V3 §6); el HOLD 10-14 Nov está reservado al forward CXB (`PREREG_CXB_MULTIVARIANTE_FORWARD.md` línea 3; `replay_train.py:12` asserta `D_ <= '2026-11-09'`); la clase HI no tiene latencia vigente; B real (20-23 Oct, R1/HI) no es reproducible con el motor (no hay `ms2` antes del 26-Oct). La confirmación de cualquier palanca solo vendrá de un dry-run NUEVO con prereg y hash propios (OK de Javi) o de días no vistos (§12).

## 2. Ficheros de entrada (verificados 16-Nov 13:00-13:45Z)
Rutas relativas a `/root/polymarket-research/` salvo las absolutas. `L2` = `experimentos/5m_barato/l2_carrera_10nov/`; `EXP1` = `misiones/5m_barato/alpha_miner_B_F5_15nov/exp1/`; `DL` = `/root/polymarket-research-datalogs/`; `P2` = `/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/` (solo lectura).

| # | Ruta | Qué es | Columnas / claves verificadas | sha256 (16 hex) / mtime | Cómo se verificó |
|---|---|---|---|---|---|
| E1 | `L2/out_v3/CX_v3dd_<D>.pkl` (15: 26-Oct..09-Nov) | dict `{R, A, ramas, c_epoca}` del generador `passT_cxb_v3.py` | `R` (SOLO rellenos): `var,dia,act,lado,fin,k,L,q,tf,gana,seg,t_dec,canc,T,f5_dec,pnl,cost`; `A` (agregado por var×moneda×L, incluye placebos `P_<var>_<s>`, s=1..20): `var,dia,act,L,n_seg,n_canc,n_fill,cost,pnl`; variantes reales: G0, GEO1, GEO1_F5A, CXB60, CXB100, CXB150, TOP60, CXB60r, F5A, F5B, F5A_CXB60/100/150 | Apéndice A; 26-28 Oct con mtime 12-Nov 11:00Z (copias previas en `_pre_fix_tf_12nov/`, difieren byte a byte) | carga con `/usr/bin/python3` (pandas 3.0.3). **El venv `.venv` no abre estos pkl (falta `pyarrow`)**. **Ojo: `k` = índice de mercado del motor, NO ticks** |
| E2 | `L2/out_v3/SEGT_v3dd_<D>.pkl` (15) | TODOS los segmentos de G0 (rellenos y no rellenos) | `dia,act,lado,fin,k,L,seg,t_dec,T,bidL,r3,dbid3,ja3,q,tf,ftype,vida_ms,gana` | Apéndice A | 47.470 filas = Σ `A.n_seg` de G0 en 15/15 días (comprobado); `bidL = bid_rx(t_dec−300 ms) − L` (`passT_v3.py:112,121,154`, vista de conocimiento RX); 3 `bidL` NaN (XRP 26-Oct, PASS_T_V3 §2) |
| E3 | `L2/out_v3/g0_segs_v3dd_<D>.pkl` | = E2 + `token` | ídem + `token` | — | carga (03-Nov) |
| E4 | `L2/dryrun/frozen/{engine.py, capt.py, relojes.py, engine_clock.py, engine_v3.py}` | motor v3 congelado | constantes `engine.py:6-8`: `LAT_POST=68, LAT_CANC=60, GRID=500, TMIN=61, EPS=1e-6, TOLP=0.0049, LEVELS=(0.10,0.13,0.16,0.19), SIZE=5.0, GATE=dict(lvl=0.03, vol=26.0, hora=4)`; variantes de cola `CONS/BASE/OPT` (`engine.py:14-48`) | a7b8431a…, 3fe09524…, 6c89b853…, 4196fbf6…, b1bf34a1… = `HASHES_CONGELADOS.json` (sha del JSON 534b476093a8294b…) | `sha256sum` hoy: los 5 coinciden |
| E5 | `L2/dryrun/cxb60_core.py` | núcleo del dry-run | importa `l_pool_emp.json` con `assert` (`cxb60_core.py:35-37`) | 40b1099fc70276d3 | **NO se importa** en este programa (pool obsoleto) |
| E6 | `L2/passT_cxb_v3.py`, `L2/passT_v3.py`, `L2/stamp_v3.py`, `L2/dryrun/replay_train.py`, `L2/dryrun/brecha_nivel_v3.py` | generadores/referencias | — | 69b178b5bb1f9f3f, eedb28a860102a24, fbf8be964804137a, 46791c3e0d0352c3, 55880cf512c1228d | `sha256sum` |
| E7 | `DL/sa_ms2/ms2_<D>.npz` (+`.manifest.json`) | libro top-of-book con EX y RX | `q_k, q_t_rx, q_v0, q_v3` (leídas en `passT_cxb_v3.py:89`) | — (no hasheados: ~1,5 GB) | `ls`: **solo 26-Oct..09-Nov** |
| E8 | `P2/precursores_barrido/out/tape_<D>.pkl`, `bad_<D>.json` | cinta on-chain de rellenos maker y horas malas | tape: `side,t_ws_ms,tx,log_index,token_id,price,sh` (por el código que la lee: `engine.py:103-107`, `passT_cxb_v3.py:26-27`; el pkl no se abrió); bad: `{"bad": [[día, hora]], "fills", "cob_tx_ws", "side0_sanas"}` | — | `ls`: 26-Oct..14-Nov; contenido de `bad` leído (§4.3) |
| E9 | `/mnt/HC_Volume_106538179/libro5_tx/libro5_tx_<D>_*.csv.gz` | casados WS↔tx | `t_ev, token, tx, recv` (`passT_cxb_v3.py:24`) | — | `ls`: 24-Oct..16-Nov |
| E10 | `/mnt/HC_Volume_106538179/m5_registro/` | registro ms filtrado | filas `q` (col 2 EX, col 8 RX), `t`, `x` (CONTRATO_RELOJES §2) | — | `ls`: 08-Oct..15-Nov (39 ficheros) |
| E11 | `DL/sa_r1/gmap_*.json` | desenlace OFICIAL `{slug: {id, toks, des}}` | `des ∈ {YES, NO}` (`capt.py:9-12`) | — | `ls`: 28 ficheros, 19-Oct..15-Nov; **cobertura por día NO verificada** |
| E12 | `DL/paquete_l/ensayo_real_{B2,B3,B5}/informe_final.json` | latencia VIGENTE (13-Nov) | `cobertura.anclas_directas`, `anclas_detalle.{alta_ex_menos_envio, cancel_ex_menos_envio, cancel_ack_menos_ex}.{n,p10,p50,p50_ic90,p90,p90_ic90}`, `latencias.{d_proc_ms, d_red_cancel_ms}` | 0d12371631930994, 11d1b82ceea5105a, a8cbc57a9a5d062a | lectura JSON (tabla §3.3). Crudos por ancla: `ledger.jsonl` y `cancel_evid/` de cada tanda (**nombres de campo NO verificados**) |
| E13 | `EXP1/suelo_feed_publico_2026-11-13.txt` | suelo del feed público 13-Nov | `ventana n p5` (144 filas) | 33e3433e135773b0 | head/tail: p5 18-21 ms en 144/144 → LO |
| E14 | `EXP1/cache/pob_add3_<D>.json` | mapa de clase por ventana (ADD3) | `C3_suelo_rx_menos_ex.{perfil_p5_10min (144), ventanas_por_clase, prints_por_etiqueta, frac_indet}` | — | 27-Oct: lo 89 / hi 54 / indet 1. Hoy existen COMPLETE: 09, 10, 11, 12, 17, 22, 23 y 27-Oct; el resto lo producirá `EXP1/lanza_add3.sh` (supervisor at; espera MemAvailable ≥5.500 MB) |
| E15 | `EXP1/B_fills_v3.pkl` | 215 fills reales de B con tm3 | 111 columnas, entre ellas `precio, coste, pnl, gana, coin, dia, cierre, mkt_lado, tm3, rama, epoca, bid_p35, bid_p60, F5_p35, F5_p60, cat_p60` | 8a5c7521823c70eb | carga: precio 0,11-0,29 (máx 0,2900001297), mediana 0,22, 135 ≥ 0,20; ramas sig 163 / amb 24 / sinev 17 / nosig 6 / guard 5 |
| E16 | `L2/verif_real/out_v3/V3_2026-10-2{0,1,2,3}.pkl`, `own_2026-10-2{0..3}.pkl` | motor sobre las 3.796 órdenes reales | columnas usadas por `brecha_nivel_v3.py` (`v3d_BASE_f_q`, `v3d_BASE_f_tf`, `real_q`, `tcs`, `gana`, `L`) | — | `ls` (existen los 8); columnas por el docstring/código de `brecha_nivel_v3.py:2-49` |
| E17 | `EXP1/E6_brecha_add2.txt`, `EXP1/cache/<D>_pob.pkl.gz` | población E2 (sello constante) | E6 por celda; E2 37/37 COMPLETE (`STATUS.json::E2agg_add2`) | 72170dd0a221b3d5 (E6) | lectura |
| E18 | `L2/calma_v3/huecos_fix_13nov/{prep_day2.py, esc_v3b.py}` | definición de hole60 | hueco = salto >60 s entre `recv` únicos de libro5_tx (`prep_day2.py:20`); exclusión `(a−60000, b+60000)` (`esc_v3b.py:22`) | — | lectura de código; `meta2_<D>.json` solo 02..12-Nov |
| E19 | `scripts/cron_pesado.sh` | semáforo global de pesados | flock `/tmp/cron_pesado.lock`; espera MemAvailable ≥3 GB máx. 10 min y **luego corre igualmente**; `exec choom -n 500` | — | lectura |
| E20 | `scripts/validate_measurement_contract.py`, `docs/data-governance/` | citados por INTEGRIDAD Q4.1 | **NO EXISTEN** (búsqueda con `find`) | — | el contrato lo valida a mano la autoridad de integridad |

## 3. Relojes, sellos y latencia (contrato de medición)
### 3.1 Dominios (CONTRATO_RELOJES.md R1-R8)
EX = sello del exchange; RX = recepción en nuestro reloj; LOC = nuestras decisiones/envíos (mismo reloj que RX, chrony). Reglas: (R2) toda feature y todo disparo de decisión se lee en RX (última fila con `rx ≤ t`); (R3) la mecánica de relleno (libro a la llegada, cola, prints que consumen el nivel, `tf`) en EX bajo el supuesto etiquetado `loc == ex`; (R4) `tf` siempre EX; nunca se usa RX−EX como duración de nada (solo para clasificar el suelo). Modo del motor: `causal` = (relleno EX, conocimiento RX) (`engine_clock.py:13`). Todo informe declara reloj y modo.

### 3.2 Sello del print (tm3) y reconciliación con la población
- Motor y población del discriminante: **la MISMA cinta** `tape_<D>` (side 0) tras `stamp_v3.stamp_events` (firma única token+precio+tamaño ±1.500 ms EX → `tm = ex(fila) − 1`; si ambigua/sin firma/fuera de guardia → `t_ev − c_día − 1`, c_día = p50 de d_ex de las firmas únicas del día, 18-21 ms; sin `t_ev` → `recv − 63`, rama `sinev`). Cada relleno y cada print lleva su `rama` (sig/amb/nosig/guard/sinev).
- La población de EXP-1/E2 (rama constante `r_v3 = t_ev − 19 − 1` sobre filas `t` de m5_registro, sin firma) **no entra en ninguna cifra decisoria**: se usa solo como descriptiva y en un puente E2↔tape (§9.4) que mide cuánto cambia la EV de celda al pasar del sello constante al tm3.
- Sensibilidad de sello: solo-`sig` (las demás ramas fuera) en el discriminante y en F1/F2.

### 3.3 Latencia: SOLO los ensayos reales vigentes (13-Nov, clase LO confirmada)
| Tanda | anclas directas | alta ex−envío p50 [IC90] / p90 | cancelación efectiva ex−envío p50 [IC90] / p90 | ack−ex cancel p50 | RTT cancel p50 (`d_red_cancel_ms`) | fin (UTC) |
|---|---|---|---|---|---|---|
| B2 | 105 (alta n=107; 2 fills) | 38 [37; 40] / 146,6 | 34 [33; 35] / 111,4 | 24 | 58,7 | 11:33Z |
| B3 | 104 | 34 [33,5; 35] / 46,7 | 32 [32; 32,5] / 46,2 | 24 | 56,6 | 11:50Z |
| B5 | 104 | 35 [34; 36] / 41,7 | 32 [31; 33] / 41,0 | 24 | 56,5 | 12:11Z |
Total 313 anclas (verificado), un solo día (13-Nov) y ~2,2 h; por moneda BTC 126 / ETH 64 / SOL 63 / XRP 60. Clase de suelo del feed público ese día: 144/144 ventanas LO (`EXP1/suelo_feed_publico_2026-11-13.txt`). `d_proc_ms` 0,007 ms es del bucle de sonda, NO del bucle de decisión.

**Parámetros derivados (rejilla declarada; l, A y clase NO son métricas de selección):**
- `d_proc` = 3 ms, SUPUESTO no medido (sensibilidad 10 y 20 ms).
- Alta: `t_arr = t_dec + A`, **A = 38 ms primaria** (= 3 + 35, p50 mediano de las tres tandas); **A = 68 ms** solo para la paridad y como sensibilidad conservadora.
- Cancelación efectiva desde el RX del disparo: `t_canc_ef = t_trig_rx + l`, `l = d_proc + cancel_ex_menos_envío`.
  - **Primaria `l = MIX`**: por segmento, `l_i = 3 + v_j`, con `v_j` uno de los 313 valores individuales de `cancel_ex_menos_envio` (B2 ∪ B3 ∪ B5), índice `j` sorteado de forma determinista con `numpy.random.default_rng([token_key, round(100·L), seg, 20261116])` (mismo patrón que CXBEMP, `cxb60_core.py:41`, pero con el pool vigente). **Condición**: los 313 valores se reconstruyen del `ledger.jsonl` con la misma lógica de `paquete_l.py` y deben reproducir EXACTAMENTE n, p10, p50 y p90 de los tres `informe_final.json`; si no se reproduce, la primaria pasa a `l = 46` fija (se declara cuál se usó).
  - Sensibilidad: `l ∈ {36, 46, 60, 100}` y **111 ms** de estrés (p90 de B2).
- **Clase HI = DATA_BLOCKED**: no hay latencia vigente en HI. Sensibilidad acotada, nunca inferencia: `A + 20,5` y `l + 20,5` ms.
- **Obsoletos** (prohibidos como primarios; solo regresión etiquetada): `l_pool_emp.json`/CXBEMP, `LAT_POST=68` como primario, δ=40 ms de `carrera_cancel_vs_print.py` (n=39, circular), NOTA_A2 §3, anclas Sonda 30-Oct..05-Nov.

### 3.4 Clase de suelo por ventana (nunca por fecha)
- Ventana de 10 min definida en RX; p5 de (rx−ex) de las filas `q` con bid ∈ [0,03; 0,45] y ≥200 filas; **lo** si |p5 − 19,25| ≤ 5 ms, **hi** si |p5 − 39,5| ≤ 5 ms, **indet** en otro caso o sin datos (ADD2 §2 / ADD3 §1).
- Clase CAUSAL (primaria) de un segmento: la de la última ventana cerrada antes de `t_dec − 200 ms`, índice `w = floor((t_dec − 200 − día0)/600000) − 1` (ADD3 §2); de un print de población: igual con `tm3` en lugar de `t_dec`. La primera ventana del día es indet. Clase concurrente: solo descriptiva.
- Fuente: `perfil_p5_10min` de ADD3 (E14). Si 48 h después del sellado ADD3 no lo ha producido para algún día del replay, se mide con el criterio idéntico de `EXP1/suelo_ventanas.sh` (awk en streaming), que antes de usarse debe reproducir ventana a ventana (±0 ms) el perfil ADD3 del 27-Oct; si no lo reproduce, ese día queda DATA_BLOCKED para tablas por clase.
- Tablas SIEMPRE por clase primero (lo / hi / indet por separado). Lo fusionado no decide.

## 4. Días, exclusiones, ventana y soporte de precio
### 4.1 Días
- **Primarios: 28-Oct..09-Nov (13 días)**, segmentos y prints en clase LO causal.
- **26 y 27-Oct**: solo con etiqueta por ventana (hi y lo por separado, jamás fusionados); 27-Oct es mixto (lo 89 / hi 54 ventanas).
- **Excluidos**: HOLD 10-14 Nov (y cualquier día ≥10-Nov mientras el forward CXB no haya cerrado su última mirada, §12); 20-23 Oct del replay (sin `ms2`); cualquier día sin `ms2` o sin tape.
- **Excepción declarada** (precedente PASS_T_V3 línea 1): para sellar tx del 09-Nov se leen los `libro5_tx` del 10-Nov (solo `t_ev, token, tx, recv`); ningún desenlace, EV ni libro del 10-Nov.

### 4.2 Universo y ventana temporal
5m ETH, SOL, XRP (BTC fuera: ver §14). Decisión cada 500 ms en `[fin−300 s, fin−61 s]` (`engine.grid`), hora UTC ≥ 4 (gate G0). La población del discriminante se restringe a la misma ventana (`tm3 ∈ [fin−300 s, fin−61 s]`), mismas horas, mismos mercados `sane == 'ok'` y con desenlace.

### 4.3 Horas malas / huecos: UNA regla
- **Primaria = hora completa de `bad_<D>.json`**, aplicada igual al motor (`engine.sane`: fuera todo mercado cuya hora de inicio o de cierre sea mala) y a la población. Es la regla con la que se calcularon TODOS los números publicados del motor (necesaria para la paridad).
- **Sensibilidad = hole60** (huecos >60 s entre `recv` únicos de libro5_tx, ±60 s; E18), recalculada para los 15 días con la lógica de `prep_day2.py:20` (libro5_tx existe desde el 24-Oct), aplicada igual a motor y población.
- La ventana fija «xx:43..xx+1:08» (brief) / «xx:50..(xx+1):08» (`sondeador_hueco_4h.py:2,20`) **no define ninguna regla**: es la ventana de muestreo del sondeador pasivo y el criterio descriptivo `en4h` de `detector_cortos.py`. hole60 es por datos. Discrepancia resuelta por no-uso (la causa del hueco de 4 h sigue ABIERTA y no afecta a este programa).

Horas malas verificadas (`bad_<D>.json`; entre paréntesis: horas elegibles 04-23Z que conserva el día, aproximación por horas):
| Día | horas malas | conserva | Día | horas malas | conserva |
|---|---|---|---|---|---|
| 26-Oct | — | 20/20 | 03-Nov | 3,7,11,15,19,20,22,23 | 13/20 |
| 27-Oct | — | 20/20 | 04-Nov | 0-11,15,19 | 10/20 |
| 28-Oct | — | 20/20 | 05-Nov | 7,11,15,19,23 | 15/20 |
| 29-Oct | 18 | 19/20 | 06-Nov | 3,7,11,15,19,23 | 15/20 |
| 30-Oct | 10-18 | 11/20 | 07-Nov | 3,7,11,15,19,23 | 15/20 |
| 31-Oct | 17,20,22,23 | 16/20 | 08-Nov | 7,11,23 | 17/20 |
| 01-Nov | 0,3-9,15,19,22,23 | 10/20 | 09-Nov | 3,7,11,15,19,23 | 15/20 |
| 02-Nov | 0,3-17,19,23 | 4/20 | | | |
(`cob_tx_ws` 0,50 el 02-Nov, 0,60 el 04-Nov, 0,67 el 30-Oct, 0,79 el 01-Nov; ≥0,945 el resto.)

- **Validez de día (sustituye a la lectura literal de INTEGRIDAD Q4.8; punto bloqueante B-1)**: un día primario es válido si conserva ≥ 50 % de los mercados 5m ETH/SOL/XRP con cierre en 04:00-24:00Z tras la regla primaria (cómputo exacto por mercados en la Etapa 0). Con las listas de hoy se espera: **02-Nov NO válido** en el primario (sí entra en hole60); 01-Nov y 04-Nov en el límite (decide el cómputo por mercados); resto válidos. Motivo: la regla literal «parar si un día pierde >5 % de segmentos por hora mala» dejaría solo 26, 27, 28 y 29-Oct (11 de 15 días pierden >5 % de horas), lo que no es la intención de la condición; la pérdida por MemoryError, en cambio, nunca se acepta (el día se repite hasta completarse).

### 4.4 Desenlace, libros cruzados, supervivencia
- Cobertura de desenlace oficial (gmap) ≥ 0,995 por día sobre los mercados sanos; un día por debajo queda fuera (listado, nunca relleno con ceros). Población: cobertura por coste (Σp·sh con desenlace / Σp·sh) ≥ 0,995 por día.
- Libros cruzados o bloqueados (`bid_rx ≥ ask_rx` en `t_dec`): no se coloca (motivo `libro_cruzado`, contado por día). Prints de población con estado RX cruzado en su instante de decisión: fuera y contados. En la Etapa 1 no es medible (SEGT no trae ask): limitación declarada.
- Ningún mercado sin desenlace se descarta en silencio: se lista por día y moneda.

### 4.5 Soporte de precio común
- **S = {0,11; 0,12; …; 0,29}** (19 niveles de 1c) = intersección de B real [0,11; 0,29] y población (0,10; 0,30].
- Etapa 1 (motor de 4 niveles): soporte común = **{0,13; 0,16; 0,19}**; L = 0,10 se reporta aparte como «fuera de soporte» (fuera del rango de B y en el borde abierto de la población).
- Etapas 2-3: lo colocado o impreso fuera de S no entra en las cifras de soporte común; se cuenta (motivo `fuera_soporte`) y se reporta aparte. Los prints a 0,30 exactos quedan fuera de S (contados).

## 5. Unidades, métricas y descomposición P(fill) × EV|fill (contrato de métricas)
### 5.1 Unidades y contabilidad
- **Segmento** = vida de una orden virtual de compra (de `t_arr` a `t_end`): unidad de colocación, nocional `N = SIZE·L`. **Unidad económica** = (mercado, lado) = índice `k` del motor (como B). **Cierre** = `fin` (todas las monedas que cierran a la vez forman un clúster).
- PnL idéntico para motor, población y B real: `pnl = q·(gana − p) + q·0,2·0,07·p·(1−p)` (rebate maker = 0,2 de la comisión 0,07·p(1−p); `passT_cxb_v3.py:143`, `brecha_nivel_v3.py::pnl_of`); `coste = q·p`. Sin rebate solo como regresión. La comisión tomadora 0,07·p(1−p) solo aparece en salidas tomadoras (§8, S1).
- No rellenado = 0 € (contrafactual declarado; coste de oportunidad del capital no modelado). Los parciales cuentan por su `q`. Ningún segmento se descarta por no rellenarse.

### 5.2 Métricas obligatorias en TODA tabla (variante × clase × día, y agregadas)
| # | Métrica | Fórmula |
|---|---|---|
| M1 | n_seg, n_fill, **P(fill)** | n_fill / n_seg (segmento con q > 0) |
| M2 | **EV\|fill** | pond. € = Σpnl/Σcoste de los rellenos; por unidad = media sobre (mercado, lado) de Σpnl/Σcoste |
| M3 | **EV incondicional** | por orden = Σpnl/n_seg (€/orden); **por € nocional = Σpnl/ΣN (primaria)** |
| M4 | **Descomposición exacta** | Σpnl/ΣN = P(fill) · ρ · EV\|fill, con ρ = (Σcoste/n_fill)/(ΣN/n_seg) (fracción de tamaño×precio realmente rellenada); se publican los tres factores y el producto; identidad comprobada a 1e-9 |
| M5 | PnL total y **ΔPnL** vs control | emparejado por día × moneda × clase × soporte |
| M6 | Capital-tiempo (descriptivo) | Σ N·vida (€·min en órdenes vivas); Σ coste·T_rem (€·min en posición) |
| M7 | Incertidumbre | IC90 bootstrap percentil, B = 10.000, semilla 20261116, por **día** y por **cierre**; sin los 2 mejores días; días+/días; mitades cronológicas 28-Oct..02-Nov / 03..09-Nov |

Regla (trampa 14-Oct): ninguna palanca se declara mejor por subir EV|fill si baja el EV incondicional por € nocional o el PnL total; siempre se publican ambos.

## 6. Etapas, orden y puertas de paso
| Etapa | Qué | Coste | Entradas | Puerta para pasar |
|---|---|---|---|---|
| 0 | Días válidos, cobertura de desenlace, mapa de clase, sha de entradas, identidades | < 5 min CPU, RSS < 0,5 GB, sin motor ni `ms2` | E1, E2, E8 (`bad`), E11, E14, Apéndice A | ≥ 10 de los 13 días primarios válidos y con clase medida; paridad de lectura exacta |
| 1 | CPU≈0: partición ex ante de G0 (§7.1), tamaño ≤ 5 (§8.4), variantes ya calculadas (§8), Q-C (§7.3) | < 30 min CPU, RSS < 1 GB | E1, E2, `RT_v3dd_<D>`, E16, mapa de clase | no da etiquetas: solo ordena la cola de la Etapa 2 (§7.1) |
| 2 | Réplica pesada: paridad, re-sellado tm3 + población (§9), variantes con latencia vigente y placebos (§7.2, §8) | ≈ 10-25 min/día, RSS 2,1-3,5 GB; 13 días + 4 de paridad | copia del motor (E4) + E7-E11 | G-INT (§11), B-6 aprobado, ADD3 terminado |
| 3 | Combinaciones fijas, salidas, régimen sobre variantes ≠ G0 | como la 2, condicional | salidas de la Etapa 2 | ≥ 1 palanca con G-REL o decisión del chief |
| 4 | Propuesta de dry-run NUEVO (no ejecuta nada) | 0 | INFORME_E2/E3 | PROMISING + validador + red-team + OK de Javi |

### 6.1 Etapa 0 — cómputo exacto de días válidos (antes de abrir ninguna cifra de EV)
1. `N_cal(D, m) = 240` mercados por moneda m ∈ {ETH, SOL, XRP} (cierres 04:05..24:00Z; la puerta `hora ≥ 4` deja fuera el de las 04:00).
2. `N_ok(D, m)` = mercados con hora de inicio y de cierre fuera de `bad_<D>.json` (regla de `engine.sane`, reimplementada sin importar el motor). Verificación obligatoria: todo (act, fin) de `SEGT_v3dd_<D>` pertenece a `N_ok` (100 %); si falla, la reimplementación está mal y el día queda PENDIENTE hasta la lista `sane` del propio motor en la Etapa 2.
3. `cov_des(D)` = fracción de `N_ok` con desenlace en `gmap` (≥ 0,995).
4. **Válido** ⇔ Σ_m N_ok / 720 ≥ 0,50 (B-1) y cov_des ≥ 0,995. Se publica la tabla día × moneda (N_cal, N_ok, cov_des, horas malas) y la lista de días válidos queda fijada antes de la Etapa 1.
5. Clase: por día, nº de las 120 ventanas que gobiernan las decisiones de 04:00-24:00Z (03:50..23:40, regla causal §3.4) en lo / hi / indet. **Día LO-puro** = 0 ventanas hi e indet ≤ 5 %. Día con indet > 20 % → fuera de las tablas por clase (B-3).
6. Identidades SEGT↔CX por día: len(SEGT) = Σ A.n_seg(G0); nº de SEGT con q > 0 = Σ A.n_fill(G0); Σ q·L y Σ pnl (recalculado con §5.1) = A.cost/A.pnl(G0) = Σ R(G0) (tolerancia 1e-6). **SEGT es anterior al arreglo de `tf`** (11-Nov 11:47-12:09Z; `MULTIVARIANTE_GOLD_RIESGOS_12nov.md` §2: el arreglo solo cambió `tf`/`T`, no q/pnl/A) → su `tf` no entra en ninguna cifra. Día que falle → fuera de §7.1 y §8.4 (listado).
7. Paridad de lectura: Σ A(G0) fusionado de los 15 días = 4.601 rellenos / −527,8 € / EV −0,154 (±0,0005). Es una cifra ya publicada; no se abre ninguna otra.

## 7. Colocación ex ante y carrera de cancelación
### 7.1 Etapa 1 — G0 partido por distancia al bid en la decisión (`kt`)
- `kt = round(100·bidL)`, con `bidL` de SEGT = `bid_rx(t_dec − 300 ms) − L` (vista RX: conocido antes de decidir). Grupos: kt ≤ −1 (L mejora el bid), **0 (se une al bid), 1, 2, 3** (primarios, K = 4), ≥ 4; NaN contados aparte. Soporte común {0,13; 0,16; 0,19}; L = 0,10 aparte (§4.5). Clase causal por `t_dec` (§3.4).
- **Qué NO es** (se escribe en cada tabla): no es la política «poner a bid − k». (a) La vida de la orden la fija la puerta de G0, no el bid; no hay re-cotización. (b) Para cada k el bid queda atado a L + k·tick (k = 3 ⇒ bid ∈ {0,16; 0,19; 0,22}). (c) En la cola BASE una orden con L < bid tiene cola infinita hasta que el bid baja a L (`engine.py::fill_segment`, «INF si L está por debajo (solo barridos)»): para k ≥ 1 el motor es **conservador** (cota inferior de P(fill)). (d) Latencias del motor congelado (A = 68; fin por puerta +60 ms), NO vigentes: toda cifra de la Etapa 1 lleva «A=68, sensibilidad conservadora, no primaria» (§3.3) y no puede dar etiqueta de palanca.
- Estandarización (la mezcla moneda×L cambia entre grupos): métrica primaria = EV incondicional por € nocional con estandarización directa, pesos = cuota de nocional de cada estrato moneda×L (9 estratos) en G0-soporte (LO, días válidos). También en bruto. Sensibilidad: estratos moneda×L×tercio de T (300-220 / 220-140 / 140-61 s).
- Estadístico: `T_k = EVinc_std(k) − EVinc_std(G0 soporte)`; max_k T_k unilateral (mejora); p por permutación de las etiquetas kt entre segmentos del mismo día×moneda×hora (B = 10.000); umbral 0,0125 (Bonferroni 0,05/4, Q4.4). Inversión: la regla complementaria (todos los k ≠ k*) no debe mejorar también a G0; si lo hace, la ordenación no informa. Sello solo-`sig`: cruce de cada relleno de G0 con `RT_v3dd_<D>` (columna `rama`) por (k, L, seg) si el cruce es 1:1; si no, «no disponible» ese día.
- **Uso (prioridad, nunca cierre)**: la réplica P2 (§7.2) va PRIMERA en la Etapa 2 si (a) algún k tiene p_adj ≤ 0,0125, o (b) EV|fill sube ≥ 0,05 €/€ de k = 0 a k = 3 con P(fill)·ρ cayendo < 50 %. Si no, P2 va detrás de X-vig (§8) con la etiqueta «INSUFFICIENT: la colocación no se separa con el motor de 4 niveles», nunca REJECTED.

### 7.2 Etapa 2 — colocación relativa al bid (P2), k ∈ {0,1,2,3}, sobre S
- Regla: en cada punto de la rejilla (500 ms) de [fin−300 s, fin−61 s], hora ≥ 4: `L_i = round_tick(bid_rx(t_dec) − k·0,01)`; se coloca si L_i ∈ S, `ask_rx(t_dec) > L_i + EPS` (post-only), libro no cruzado ni bloqueado y puerta G evaluada con L_i. Orden estática (sin re-cotizar), `t_arr = t_dec + A`; fin = puerta falsa + l_i o fin duro + l_i; re-arme al nuevo L_i; `rem = 5` por (mercado, lado, k); una orden viva por (mercado, lado, k).
- Primario: A = 38, l = MIX, cola BASE; CONS/OPT = horquilla del modelo de cola (no selección). Puente con §7.1: misma regla con `bid_rx(t_dec − 300 ms)`.
- Control: P2 k = 0 y G0_vig. Placebo: permutación de k entre los segmentos de las 4 variantes P2 del mismo día×moneda×hora (B = 10.000) + inversión. Multiplicidad: Bonferroni 0,0125.
- Por tercio de precio dentro de S (0,11-0,16 / 0,17-0,22 / 0,23-0,29), descriptivo; 0,20-0,29 (donde vivió B: 135/215 rellenos) aparte.

### 7.3 Q-C — brecha de NIVEL motor-vs-real de B con δ vigente (Etapa 1, CPU≈0)
- Entradas: E16 + `/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv` (`oid`, `t_cancel_int`) + `L2/verif_real/out/T1_tx.pkl`. Se copian literalmente `pnl_of` y `sim_con_delta` de `brecha_nivel_v3.py` a un script nuevo (el original no se importa: crea `out_replay/` al importarse).
- δ (fin efectivo de la orden en EX tras el envío del DELETE) = `d_proc + cancel_ex_menos_envio`: primario LO = MIX (`3 + v_j`, sorteo determinista por `oid`, §3.3); rejilla {36, 46, 60}; estrés 111; HI = δ + 20,5 (sensibilidad). Sustituye al δ = 40 circular.
- Salida: TP/FP/FN, precisión, recall, EV_sim(δ) y fracción de la brecha de nivel cerrada `(EV_sim(δ) − EV_sim(sin corrección)) / (EV_real − EV_sim(sin corrección))` (EV_real −0,061 con rebate), por día (4), LODO y por clase de la ventana de cada orden (ADD3 de 20-23 Oct: hoy COMPLETE 22 y 23-Oct; 20 y 21-Oct pendientes). Órdenes en ventanas hi: solo sensibilidad (DATA_BLOCKED).
- Etiqueta: explicativo, EXPLORATORY (4 días, 100 % R1 por calendario); no decide ninguna palanca.

## 8. Resto de palancas (lista cerrada; prohibido añadir variantes tras ver cifras)
En toda variante de las Etapas 2-3: A = 38, l = MIX (§3.3), rejillas de sensibilidad declaradas. **G0_vig / GEO1_vig** = G0 / GEO1 con A = 38 y fin por puerta (y fin duro) a `+ l_i` en vez de +60 ms. Cortes F5 congelados: C0 = 3,526360511779785, C1 = 4,717426776885986 (PREREG_FWD_V2, TRAIN 06-08 Oct); F5 = log1p(tamaño del ask nivel 1 del token propio, vista RX) (`passT_cxb_v3.py:85,112`).

| Familia | id | Definición exacta | Etapa | Control | Placebo / test | K |
|---|---|---|---|---|---|---|
| X cancelación | CXB60/100/150, TOP60, CXB60r | ya calculadas (A = 68; l = 60/100/150) | 1 (regresión) | GEO1 | 20 placebos de CX: solo rango descriptivo | — |
| X | CXB_vig | armar si bid_rx(t_dec−300) ≥ L + 1 tick; disparo = bid_rx < L − TOLP; cancelación efectiva `t_trig_rx + l_i` | 2 | GEO1_vig | 100 placebos (instante uniforme en el segmento cuando la regla dispararía, como `cfn`) | 3 |
| X | TOP_vig | igual; disparo = bid_rx ≤ L + TOLP | 2 | GEO1_vig | ídem | (3) |
| X | CXBr_vig | CXB_vig y además bid_rx(t_dec) ≥ L + 1 tick | 2 | GEO1_vig | ídem | (3) |
| F F5 | F5A, F5B, GEO1_F5A | ya calculadas (filtro + fin de segmento por rejilla) | 1 (regresión) | G0 / GEO1 | 20 máscaras rodadas: rango descriptivo | — |
| F | F5A_vig | no colocar si F5(t_dec) > C1; la puerta cae si F5 > C1 (rejilla) | 2 | G0_vig | 100 máscaras rodadas | 3 |
| F | F5B_vig | ídem con C0 | 2 | G0_vig | ídem | (3) |
| F | **F5C** (disparador por eventos) | no colocar si F5(rx ≤ t_dec) > C1; cancelar en el primer evento `q` (RX) con F5 > C1 tras `t_arr`, efectiva `t_trig_rx + l_i` | 2 | G0_vig | 100 (instante uniforme, misma cobertura) | (3) |
| T tamaño | T1 | s = 1 frente a s = 5 en G0, exacto (§8.4), + EV por rango de acción 1..5 | 1 | s = 5 | bootstrap emparejado por día | 3 |
| T | T10, T25 | SIZE ∈ {10, 25} en G0_vig y CXB_vig | 2 | s = 5 | ídem | (3) |
| Q cola | CONS/BASE/OPT | horquilla del modelo de cola en toda variante primaria de la Etapa 2 | 2 | — | no es selección | — |
| Q | QTHIN | con L = mejor bid (bid_rx = L), cancelar si el tamaño visible del mejor bid `v2_rx < 2·rem`; efectiva `t_trig_rx + l_i` | 2 | G0_vig | 100 (instante uniforme) | 1 |
| R régimen | R1 | operar solo en bloques UTC de 4 h (por moneda) con D1 = vol. realizada de rendimientos de 1 min de Binance en los 30 min previos al bloque ≤ mediana de los 14 días previos (mín. 10 días) | 2-R (ligera), aplicada a G0 a CPU≈0 | G0 | permutación de máscaras de bloque dentro de moneda (B = 10.000) | 2 |
| R | R2 | ídem con D2 = vol. de las 4 h previas | 2-R | G0 | ídem | (2) |
| S salidas | S1 | venta tomadora a bid_rx en el primer disparo CXB tras el relleno; comisión 0,07·p(1−p) | 3 | mantener a resolución (mismos rellenos) | bootstrap emparejado | 2 |
| S | S2 | venta maker a p_fill + 2 ticks colocada en `tf + A`, rellenada con el modelo de cola en el lado ask | 3 | ídem | ídem | (2) |
| C combinaciones | C1 | CXB_vig ∪ F5C | 3 | GEO1_vig | 100 | 4 |
| C | C2 | CXB_vig + F5A_vig | 3 | GEO1_vig | 100 | (4) |
| C | C3 | P2(k = 1) + CXB_vig | 3 | P2 k = 1 | 100 | (4) |
| C | C4 | CXB_vig + R1 | 3 | GEO1_vig | 100 | (4) |

### 8.1 Orden de la Etapa 2 (una pasada por día que lo calcula todo)
Paridad (§8.5) → re-sellado tm3 + población (§9.1) → G0_vig, GEO1_vig → X → F → P2 (antes, si §7.1 la prioriza) → T10/T25 → QTHIN → CONS/OPT de las primarias. Se guarda **cada segmento** (no solo los rellenos) con `t_dec, t_arr, t_end, L, q, tf, canc, clase, rama`, para que toda métrica por clase sea exacta.

### 8.2 Régimen (R1/R2)
Barras de 1 min con el sello de RECEPCIÓN de las filas `x` de m5_registro (nunca el E de Binance; CONTRATO_RELOJES), reutilizando las funciones de `exp1/e5_regimen.py` sin editarlo; trabajo ligero en streaming, fuera del pase del motor. La máscara de bloque se aplica a G0 por el bloque de `t_dec` (CPU≈0) y, en la Etapa 3, a las demás variantes. D3 (memoria del bloque anterior) no se usa: persistencia nula (lag-1 Spearman +0,038, p 0,27, `regimen_bloques4h.txt`, sello viejo, descriptivo). **La clase LO/HI como filtro de régimen = DATA_BLOCKED** (sin latencia HI).

### 8.3 Salidas (S1/S2), condicionadas
S1: el taker delay NO está en los datos vigentes (las sondas del 13-Nov son órdenes en reposo a 0,01; INTEGRIDAD Q2.2) → **DATA_BLOCKED** como primaria; solo horquilla etiquetada (llegada `t_trig_rx + 38 + {150, 250}` ms). S2 exige que la cinta permita simular una venta en reposo (semántica de `side` de `tape_<D>` por verificar; el motor solo modela compras contra ventas que golpean bids); si no, DATA_BLOCKED, nunca REJECTED.

### 8.4 Tamaño ≤ 5 exacto desde SEGT
En una cadena de segmentos (mismo k, L) el inicio y el fin de cada segmento no dependen de `rem` (`run_var`) y el relleno de un segmento es `min(rem, V)`, con V = volumen tras la cola (∞ con barrido; `fill_segment`). Por inducción, lo rellenado acumulado con tamaño s es `Q_s = min(s, Q_5)` y los segmentos de s son los de 5 hasta que `Q_s = s`. Así, P(fill), EV|fill e incondicional de s ∈ {1..5} salen exactos de SEGT; tamaños > 5 necesitan la Etapa 2 (SIZE parametrizado). Límite declarado: orden virtual; un tamaño visible mayor puede cambiar el comportamiento ajeno (no modelado) → cota superior de capacidad.

### 8.5 Copia del motor y paridad (antes de cualquier variante nueva)
Directorio nuevo `experimentos/5m_barato/replay_brecha_B_16nov/`: copia de los 5 ficheros de E4 con sha256 = `HASHES_CONGELADOS.json`, y copia de `passT_cxb_v3.py` parametrizada en A, l (MIX), SIZE y niveles bid-relativos, **sin importar `cxb60_core` ni `l_pool_emp.json`**. Paridad: con A = 68, l = 60, niveles fijos, SIZE = 5 y cola BASE, reproduce EXACTAMENTE `R` y `A` de `CX_v3dd` en 26, 27, 28 y 29-Oct (mismos rellenos k, L, seg, q, tf, pnl y mismas filas de A; patrón `replay_train.py` modo A). Sin paridad exacta no se calcula nada más (stop rule).

## 9. Discriminante motor-vs-población (Q-A)
### 9.1 Población con el MISMO sello y la MISMA cinta (Etapa 2)
Prints de `tape_<D>` lado 0, re-sellados con `stamp_v3.stamp_events` en la misma pasada que el motor (§3.2), deduplicados por (tx, log_index), con `tm3 ∈ [fin−300 s, fin−61 s]`, mercados sanos con desenlace, horas malas con la regla de §4.3 y clase causal por `tm3`. Dos cortes de precio: exactamente L ∈ {0,13; 0,16; 0,19} (±TOLP) para comparar con G0, y S para P2. EV por celda = Σpnl/Σcoste con §5.1 (q = sh, p = price).

### 9.2 Comparación
Celda c = día × moneda (LO, válido; L agrupado dentro del soporte). EV_mot(c) = G0 con A = 68 (paridad) y con A = 38 (G0_vig); EV_pob(c); Δ(c) = EV_mot(c) − EV_pob(c). También el Δ agregado con IC90 por días y por cierre.

### 9.3 Criterio (concreción de INTEGRIDAD Q4.6; punto bloqueante B-4)
Por moneda m: h_m = semiancho del IC90 por días de EV_pob (bootstrap sobre días LO válidos, B = 10.000). Celda **incompatible** si |Δ(c)| > h_m. Solo cuentan las celdas con ≥ 30 rellenos del motor y ≥ 100 prints (el resto, «sin potencia», se cuenta). Si > 50 % de las celdas con potencia son incompatibles → **P-NO**: «la población no es alcanzable por un relleno virtual de 5 acciones en cola»; la referencia pasa a ser G0 y la brecha se mide como distancia a EV = 0. Si no → **P-SÍ**: motor y población comparables; la distancia B real → población es de ejecución. En ambos casos se publica EV_pob con su IC y, si su IC90 por días queda por debajo de 0, se dice: la población no ofrece EV positivo que alcanzar.

### 9.4 Puente E2↔tape
Para los 13 días primarios: EV por celda con la población E2 (sello constante, `EXP1/cache/<D>_pob.pkl.gz`) frente a la de §9.1, con la misma ventana, precios y celdas → ΔEV_sello por celda, descriptivo; mide cuánto de las cifras tipo «+0,185» depende del sello. Los `pob` de 10-14 Nov no se abren.

### 9.5 «Tipo B» ex post
`bid(t−l−3) − p ≥ 0,0099` se retira como regla (INTEGRIDAD D2: condicionada al relleno); queda solo como partición descriptiva de la población.

### 9.6 Fracción de brecha cerrada
`FC_0(v) = (EV_v − EV_G0) / (0 − EV_G0)` (distancia a EV = 0; siempre) y `FC_pob(v) = (EV_v − EV_G0) / (EV_pob − EV_G0)` (solo con P-SÍ y EV_pob > EV_G0). Ambas con EV incondicional por € nocional y con EV|fill, en LO.

## 10. Estadística y multiplicidad
- Familia primaria P (K = 4): Bonferroni 0,0125 por max-statistic de permutación (§7.1 cribado, §7.2 contraste). Las Etapas 1 y 2 miran el mismo TRAIN: solo la Etapa 2 cuenta para etiquetas.
- Familias secundarias X(3), F(3), T(3), Q(1), R(2), S(2), C(4) = 18 contrastes: p por el placebo de cada variante (100; p mínimo 1/101), permutación (R) o bootstrap emparejado (T, S); max-statistic dentro de cada familia; BH-FDR q = 0,10 sobre las 18 para «pasa multiplicidad». Los 20 placebos de CX (Etapa 1) no pueden bajar de p = 1/21 ≈ 0,048: solo rango descriptivo.
- Sensibilidades (nunca selección): A ∈ {38, 68}; l ∈ {MIX, 36, 46, 60, 100, 111}; d_proc ∈ {3, 10, 20}; cola CONS/OPT; sello solo-`sig`; hole60; HI +20,5 (solo ventanas hi); bid en t_dec frente a t_dec − 300 (P2); tercios de precio de S; mitades cronológicas; sin los 2 mejores días; por moneda.
- Concentración: cuota del PnL positivo del mejor día y de la mejor moneda. IC por cierre siempre (fallos en racimo: varias monedas en el mismo cierre = una apuesta).

## 11. Puertas de decisión y etiquetas (por palanca, clase LO, días válidos)
| Puerta | Condiciones (todas) |
|---|---|
| **G-INT** | paridad exacta (§8.5); identidades (§6.1); cobertura de desenlace ≥ 0,995; ≥ 10 días primarios válidos en LO; indet ≤ 20 % por día; ningún día perdido por MemoryError (se repite) |
| **G-REL** (mejora vs control) | ΔPnL > 0; IC90 por días inf > 0 **y** por cierre inf > 0; ≥ 60 % de días con Δ > 0; Δ sin los 2 mejores días > 0; Δ > 0 en las dos mitades cronológicas; multiplicidad pasada (P: p_adj ≤ 0,0125; secundarias: BH-FDR q ≤ 0,10) |
| **G-ABS** (EV absoluto) | EV\|fill pond. > 0 y EV incondicional por € nocional > 0, ambos con IC90 por días inf > 0; sin los 2 mejores días > 0; ≥ 60 % de días +; n_fill ≥ 200; ninguna moneda > 70 % ni ningún día > 50 % del PnL positivo |
| **G-LAT** (Etapas 2-3) | G-REL se cumple con l = MIX y A = 38 **y** con l = 46; el signo de Δ se mantiene con l = 60 y A = 68; l = 111 y HI +20,5 solo se reportan |
| **G-ROB** | mismo signo de Δ con sello solo-`sig`, con hole60 y con cola CONS (OPT solo se reporta) |

Etiquetas (techo PROMISING; este programa **no emite REJECTED**):
- **PROMISING**: G-INT ∧ G-REL ∧ G-ABS ∧ G-LAT ∧ G-ROB, solo en las Etapas 2-3 → candidata a dry-run nuevo (Etapa 4) tras statistical-validator y red-team.
- **EXPLORATORY-mejora**: G-INT ∧ G-REL ∧ G-LAT sin G-ABS → componente de las combinaciones (Etapa 3) o de tamaño/régimen.
- **INSUFFICIENT**: IC que cruza 0, n_fill < 200, multiplicidad no pasada o días/clase insuficientes → sigue en cola con la n necesaria estimada (días nuevos/forward); nunca se cierra.
- **NEGATIVO-EXPLORATORIO (no priorizada)**: Δ con IC90 sup < 0 por días y por cierre → se registran el dato, el reloj, la latencia y la clase en que se apoya; reabrible con una variante de mecanismo distinto.
- **DATA_BLOCKED**: HI; salida tomadora (taker delay sin dato vigente); S2 si la cinta no lo permite.
- La Etapa 1 no emite etiquetas de palanca: solo ordena la cola de la Etapa 2.

### 11.1 Regla de continuidad («alcanzable, no un no»)
Si tras la Etapa 3 ninguna palanca es PROMISING, el informe entrega obligatoriamente: (i) el mejor camino G0 → palanca → combinación, con FC_0 y la distancia restante a EV > 0 con su IC; (ii) qué restricción limita cada palanca (cola conservadora, HI sin latencia, taker delay, n); (iii) las siguientes variantes de mecanismo distinto, para un ADDENDUM; (iv) los datos que habría que reunir (decisiones de §13.4). Cada negativo es la siguiente variante, no un cierre.

### 11.2 Contribución económica (para el libro del 200 k)
Para cada palanca EXPLORATORY-mejora o PROMISING: €/día en LO por moneda con IC90 por días y su anualización `× 365 × fracción de días LO observada`, con T10/T25 como techo de capacidad virtual. Etiqueta EXPLORATORY; nunca una previsión.

## 12. Confirmación y uso de días
- TRAIN 26-Oct..09-Nov: solo exploratorio. **HOLD 10-14 Nov: no se abre nada de esos días** (`ms2`, `tape`, `bad`, `gmap`, `libro5_tx` salvo la excepción del 10-Nov de §4.1, `pob_add3_*`, `*_pob.pkl.gz`). Los días ≥ 15-Nov no se usan mientras el forward CXB no cierre su última mirada (plazo 17-Dic).
- Confirmación de una palanca PROMISING: (a) dry-run NUEVO con prereg y hash propios (OK de Javi), en proceso aparte, sin tocar `cxb60dry`; o (b) réplica sobre días no vistos tras el cierre del forward CXB, para lo que hay que **conservar** m5_registro, libro5_tx y tape de los días ≥ 15-Nov y extraer su `ms2` (decisión del chief: disco).
- Una palanca confirmada solo llega a B por la sesión principal (/code-review medium + OK de Javi); mientras tanto B sigue tal cual.
- Cualquier cambio tras ver cifras de las Etapas 1-3 = ADDENDUM con fecha y sha; este fichero no se edita.

## 13. Trazabilidad frente a INTEGRIDAD_REPLAY_COLOCACION_16nov.md
### 13.1 Condiciones Q1-Q4
| Ítem | Dónde | Estado |
|---|---|---|
| Q1.1 `ms2` solo 26-Oct..09-Nov; días de B no reproducibles | §1.4, §4.1; Q-C sobre las órdenes reales (§7.3) | cubierto |
| Q1.2 HOLD | §4.1, §12 | cubierto |
| Q1.3 TRAIN ya usado | §1.4, §10, §11 (techo PROMISING; Etapa 1 sin etiquetas) | cubierto |
| Q1.4 clase por ventana | §3.4, §6.1-5 | depende de ADD3 (B-3) |
| Q1.5 días utilizables; MemoryError del 27-Oct | §4.1, §15 | cubierto |
| Q1.6 una sola regla de horas malas | §4.3 | cubierto |
| Q2.1 un día, 2,2 h; cola p90-p99 sin estimar | §3.3 (rejilla, estrés 111 ms), §11 G-LAT | declarado |
| Q2.2 sondas lejos del libro; sin taker delay | §3.3 (A = 68 como sensibilidad), §8.3 | S1 DATA_BLOCKED |
| Q2.3 LO del canal de usuario, no del feed | E13: feed público del 13-Nov, 144/144 LO | resuelto |
| Q2.4 HI sin cubrir | §3.3, §8.2 | DATA_BLOCKED; decisión de Javi (§13.4) |
| Q2.5 datos obsoletos | §3.3, E5, §8.5 | cubierto |
| Q3 población ≠ EV de regla; sellos; banda; censura; cruzados; supervivencia; racimos | §9, §5, §4.4, §4.5, §10 | cubierto; cruzados no medibles en la Etapa 1 (§4.4) |
| Q4.1 contrato (el validador no existe, E20) | este documento; revisión manual de integridad | B-1..B-6 |
| Q4.2 días | §4.1 | cubierto |
| Q4.3 hash + paridad | §8.5 | cubierto |
| Q4.4 variantes y K | §7, §8, §10 | B-5 |
| Q4.5 métricas, placebo, inversión, GEO1, BTC aparte | §5, §7, §8, §10, §14 | cubierto |
| Q4.6 discriminante | §9.3 | B-4 |
| Q4.7 etiquetas | §11 | cubierto |
| Q4.8 stop rules | §15; reinterpretadas en B-1 y B-3 | B-1, B-3 |
| Q4.9 clase antes del primer EV | §6 (puerta de la Etapa 0) | depende de ADD3 |
| Coste y RAM | §15 | B-6 |

### 13.2 Defectos D1-D4, 8 discrepancias y cambios exigidos
| Ítem | Tratamiento |
|---|---|
| D1 soportes de precio | §4.5 (S y {0,13; 0,16; 0,19}); §7.2 bid-relativo sobre S |
| D2 «tipo B» ex post | §9.5: retirado como regla |
| D3 latencia obsoleta | §3.3, §8.5 (sin `cxb60_core` ni `l_pool_emp`) |
| D4 virtual ≠ real | §7.1(c), §8.4: el motor es cota inferior de recall y no reproduce el nivel; §7.3 lo mide sobre las órdenes reales |
| Disc. 1 RESUMEN «36/37» | fuera de este programa (salida de EXP-1); aquí no se cita ni 36 ni 37; la corrección queda pendiente del chief |
| Disc. 2 9 frente a 12 celdas | reconciliado; +0,185 (12 celdas) solo descriptivo |
| Disc. 3 «VALIDADA» R2 p60 | no se cita; la población no decide |
| Disc. 4 MemoryError 26 frente a 27-Oct | corregido (27-Oct); ambos replays exactos; solo afecta a §15 |
| Disc. 5 ventana del hueco WS | resuelta por no uso (§4.3: hole60 por datos) |
| Disc. 6 `l_pool_emp` en `cxb60_core` | no se importa; el dry-run no se toca ni se mezcla |
| Disc. 7 sello de población constante frente a tm3 | §9.1 re-sellado; §9.4 puente |
| Disc. 8 ADD3 parado | supervisor `exp1/lanza_add3.sh` vivo (pid 2193770 a las 15:48Z, esperando RAM); fallback de §3.4 |
| Cambios (a)-(f) | (a) este documento; (b) §7; (c) §5; (d) §9.5; (e) fuera de alcance (EXP-1, chief); (f) §9.1 |

### 13.3 Puntos bloqueantes (aprobación de `polymarket-data-integrity-authority` antes de cualquier cómputo)
- **B-1** Validez de día por ≥ 50 % de mercados retenidos (§4.3, §6.1-4), en lugar de la lectura literal de Q4.8 (> 5 % de segmentos perdidos por hora mala).
- **B-2** Latencia primaria `l = MIX`, reconstruida de `ledger.jsonl` + `cancel_evid/` de B2/B3/B5 con la lógica de `L2/paquete_l/paquete_l.py` (registros con `k` —p. ej. `intencion`, `post`— y `t_ns`; el resto de nombres, por verificar), con reproducción exacta de n/p10/p50/p90 de los tres `informe_final.json`; si no, `l = 46` fija. `A = 38` y `d_proc = 3` (supuesto) como primarios.
- **B-3** Mapa de clase: ADD3 `perfil_p5_10min` (o fallback awk que reproduzca ventana a ventana el ADD3 del 27-Oct); «día LO-puro» (0 hi, indet ≤ 5 %) para las métricas incondicionales de variantes que solo tienen agregado diario (`A`); día con indet > 20 % fuera de las tablas por clase (en vez de parar todo el programa).
- **B-4** Concreción del discriminante (§9.3: h_m, celdas con potencia, umbral del 50 %, P-SÍ/P-NO).
- **B-5** Familias, K y multiplicidad (§8, §10): P con Bonferroni 0,0125; 18 contrastes secundarios con max-statistic por familia + BH-FDR q = 0,10; 100 placebos por variante en la Etapa 2; Etapa 1 sin etiquetas.
- **B-6** Recursos de las Etapas 2-3 (§15): `ulimit -v 6000000` (por encima del tope de 3 GB de la misión; el pase del motor murió con 4 GB virtuales), RSS 2,1-3,5 GB, guardia propia (MemAvailable ≥ 5.500 MB en tres lecturas antes de cada día; corte si < 2.500 MB o RSS > 3,6 GB), nunca a la vez que ADD3 u otro pesado, nunca 06:00-09:30Z; requiere también el OK del chief.

### 13.4 Decisiones de Javi / chief (no bloquean las Etapas 0-1)
1. HI: B real fue 100 % R1/HI y la latencia vigente es LO; sin anclas HI (dinero real, ≤ 0,15 $/tanda, solo cuando el suelo en vivo marque hi) todo lo de HI queda DATA_BLOCKED. Recomendación: decidirlo tras la Etapa 2 en LO.
2. Excepción de RAM de las Etapas 2-3 (B-6) y su orden respecto a ADD3 (ADD3 primero).
3. HOLD 10-14 Nov sin usar (recomendación: mantenerlo).
4. Vía de confirmación de una PROMISING: dry-run nuevo en paralelo a `cxb60dry` o esperar al 17-Dic para días no vistos.
5. Conservación de m5_registro/libro5_tx/tape de los días ≥ 15-Nov (disco), para poder replicar en días no vistos.

## 14. Fuera de alcance
BTC (B no lo operó; ninguna tabla primaria; réplica descriptiva opcional en la Etapa 2 si `ms2` lo contiene, nunca decide); reproducir B real 20-23 Oct con el motor (sin `ms2`; solo Q-C sobre sus órdenes); la clase HI como inferencia; comprar ambos lados y vender (Javi 27-Oct: subestrategia aparte); tocar `cxb60dry`; A3/Calma-T1; estrategias tomadoras.

## 15. Recursos, ejecución, salidas y estado
- Implementa `cheap5m-execution-engineer`. Código y resúmenes (md/json) en `experimentos/5m_barato/replay_brecha_B_16nov/`; salidas pesadas (pkl por día y variante, gz) en `/root/polymarket-research-datalogs/replay_brecha_B_16nov/`. Nada en `out_v3/`, `dryrun/`, dev ni `data/`. Intérprete `/usr/bin/python3` (el `.venv` no abre los pkl).
- Etapas 0-1: `nice -n 19 ionice -c3`, `ulimit -v 3000000`, RSS < 1 GB, fuera de 06:00-09:30Z, con load5 ≤ 4 y MemAvailable ≥ 2,5 GB.
- Etapas 2-3: B-6; un día cada vez; `scripts/cron_pesado.sh` (flock) más la guardia propia, porque el semáforo corre igualmente tras 10 min (E19); `choom -n 500` para que el kernel mate antes la réplica que la producción.
- Idempotencia: un fichero por (etapa, día[, variante]) con `.tmp` + `os.replace`; se salta si existe con el mismo sha de código + parámetros (manifiesto); `STATUS.json` con días ok/fallidos/pendientes; resultado PARTIAL si falta algo; un MemoryError nunca se acepta como pérdida (el día se repite).
- Stop rules: paridad no exacta → parar; desenlace < 0,995 → día fuera; MemAvailable < 2,5 GB → parar el trabajo y reanudar después; indet > 20 % → día fuera de las tablas por clase; < 10 días LO válidos → INSUFFICIENT.
- Manifiesto por etapa: sha del código, de las entradas (Apéndice A), de los parámetros y de este prereg (`PREREG_REPLAY_BRECHA_B_16nov.sha256`).
- Informes `INFORME_E0.md` … `INFORME_E3.md`: cada cifra con n, IC, periodo, fichero, reloj, latencia y clase; por clase primero.
- Revisión: integridad (antes de computar y tras cada etapa) → statistical-validator + red-team (tras las Etapas 2 y 3) → chief → Javi.
- **Estado: BLOQUEADO hasta que B-1..B-6 estén aprobados y haya OK del chief. 0 cifras calculadas por este programa.**

## Apéndice A — sha256 (16 hex) de E1 y E2 (calculados el 16-Nov hacia las 15:45Z)
mtime: `CX_v3dd` 26-28 Oct = 12-Nov 11:00Z (regenerados, `MULTIVARIANTE_GOLD_RIESGOS_12nov.md` §2), resto 11-Nov 12:31-13:03Z; `SEGT_v3dd` 15/15 = 11-Nov 11:47-12:09Z (anteriores al arreglo de `tf`, §6.1-6). E3 (`g0_segs`) no se usa.

| Día | `CX_v3dd_<D>.pkl` | `SEGT_v3dd_<D>.pkl` |
|---|---|---|
| 2026-10-26 | 7a85cdb5c689a5c9 | bcb2928495edc0cc |
| 2026-10-27 | 774ca0666ecf997d | b96caee382a3de27 |
| 2026-10-28 | a66d1ecc375352ef | a3fff3eef8dab3df |
| 2026-10-29 | 0e14cb1b04b5df48 | 1968741ddce2dfc8 |
| 2026-10-30 | 4e500ec40d4c6a90 | cfde4f68146b1b9c |
| 2026-10-31 | 007af78af73b1cfc | b652829447d938d1 |
| 2026-11-01 | 0d6a2a447ae854e6 | a70a05c5ddee6af2 |
| 2026-11-02 | 74c9e95e028127ff | 90a12182d397cfcd |
| 2026-11-03 | 4e1cb1d338f4ae1d | c6b9b4e0a0298312 |
| 2026-11-04 | b1b57697e5d0c2d7 | b7afc381c2c17572 |
| 2026-11-05 | 5cc7b4af954aac9a | 4a791df788fa5942 |
| 2026-11-06 | 9657382cea87ec34 | 4b7e4301bf919bc7 |
| 2026-11-07 | 0b396e0de768257a | 78dace8a127e7937 |
| 2026-11-08 | aa8ae756db1686d6 | f2a64e67a1a429cb |
| 2026-11-09 | 67b436c7c478946e | a66323ad6287cccb |
