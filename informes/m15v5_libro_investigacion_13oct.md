# Libro de investigación 15m v5 — pares, maker, tomador, híbridos (Javi 13-Oct, prompt "200.000 € netos/año")
Regla: cada hipótesis entra con estado, evidencia (fichero/comando) y siguiente prueba. Nada a dinero sin gates +
/code-review + OK explícito de Javi. Las cifras de este libro salen de comandos de esta sesión o de informes citados;
las de "comunicado" se marcan como tales hasta reproducirlas.

## Estados de partida (verificados contra informes del repo, 13-Oct)
| Vía | Estado | Evidencia | Qué la reabriría |
|---|---|---|---|
| A tomador Φ(z)−ask | REFUTED | `informes/m15v4_superficie_resolucion_08oct.txt` (T>60 s calibrado; M1-M6 OOS −5/−11 %/€); trampa "Φ(z) peor que el mid" en CLAUDE.md | mecanismo causal nuevo, no umbrales |
| B certeza terminal tomador | REFUTED | `m15v4_certeza_terminal_regla_mes_08oct.txt` n=1.451, +0,04c/acc IC cruza 0 | — |
| C certeza terminal maker | CLOSED_CAPACITY | `m15v4_certeza_maker_0506_08oct.txt`, techo ~240 $/día grupo | fuente de valor o capacidad nueva |
| D pares maker ambos lados | OPEN_BLOCKED_BY_QUEUE | sim v4 coste/par 1,030 vs bot 0,995; descubrimiento 09-10 −18,54 $; validación crear 12-13 −0,10 $/merc | medición REAL de la cola (wallet dedicada) |
| E completar como tomador | REFUTED_BY_EXECUTION_ECONOMICS | bid+ask+fee ≥1 en 75/77 (`pares15_mision_12oct.md`) | ejecución/información distinta |
| F cerrar la pata suelta | REFUTED_FOR_CURRENT_POLICIES | B −15,8 $, C τ −16…−25 | (cancelar ANTES del relleno es otra vía: H/I) |
| G híbrido 0xb970fb5c | **degradado a REFUTED_OOS como copia** | `m15_hibrido_cuando_0xb970fb5c_13oct.txt`: 05-07 +5.095 $ → **08-12 −858 $** (210 merc.); REFUERZA 30-120 s +0,55 (n=18) → −0,06 (n=43); H-C todo el mercado 2/38 celdas repiten (= azar) | mecanismo propio (H-A, H-B) |
| H maker que cancela (A3 BTC) | PROMISING_LOW_N | `idea_a3_maker_cancela_btc15m_rastreable_07oct`: VALID +0,36 / FINAL +0,24 $/merc, n 25-40 | n con archivo m15_registro (60 d en volumen) |
| I anticipar vol/liquidez | RISK_TOOL_PROMISING | Spearman |mov|→|mov 60 s| +0,125, spread→spread +0,36, 6/6 días | política de cancelación medida |
| PAIR15_DEFENSA_V1 | FORWARD (congelada sha ddab68ea5f19a4d1) | ensayo crear 40 BTC+40 SOL desde 13-Oct 11:08Z | evaluar 14-Oct >03:45Z |

## Corrección de lectura del prompt (Fail Loud)
- La tabla del prompt dice "pérdidas brutas atribuidas a tomadores ~25k/día". On-chain es AL REVÉS: los tomadores
  GANAN ~25k $/día brutos a los makers y pagan ~38k $/día de comisión → neto tomador ≈ −12,6k $/día; makers −25k $/día
  antes de reembolso (≈ +7,6k $/día estimado, 20 % de la comisión). Suma maker + tomador = −comisión (cuadre exacto).
- El "+1.300 $/día" de 0xcfddfb6e es PnL comercial (~890 $/día) + reembolso ESTIMADO (~410 $/día).
- La pista "+82 %/€ n=36" del híbrido NO replicó fuera de muestra (ver G).

## Iteraciones
(se añaden abajo con fecha, comando, resultado y siguiente paso)

### Iteración 1 (13-Oct ~16:30Z) — `analisis_15m_v5_pares_cola_onchain.py` → `informes/m15v5_pares_cola_onchain_13oct.txt`
On-chain 05-12 Oct, 3,46 M rellenos, 4.225 mercados 15m, desenlace oficial 100 %.
- **Reconciliación** OBSERVED_FACT: PnL maker + PnL tomador + comisión = 0,0 $ los 8 días. Makers 8 días −198 k$
  (reembolso est. +78 k$); el signo del bruto tomador cambia por día (05/06/09/10/11 tomadores ganan, 07/08/12 pierden).
- **Cosechadores** (32 wallets elegidas SOLO con 05-07, ≥80 % emparejado): DESC +2.289 $/día comercial → **FORWARD 08-12
  −253 $/día comercial** (pares +72,9 k, residual −74,1 k), +3.391 $/día SOLO con reembolso estimado (5/5 días).
  OBSERVED_FACT: fuera de muestra el negocio de pares del grupo es un negocio de REEMBOLSO (≈0,51 % del volumen).
- **0xcfddfb6e NO persiste**: forward −667 $/día comercial (0/5 días +), −151 con reembolso. Su coste/par 0,953 (no 0,995)
  y sus sueltas (−26,0 k) se comen los pares (+22,6 k).
- **0x2903c7dc SÍ persiste**: 8/8 días positivo comercial; forward +789 $/día (+1.006 con reembolso), coste/par 0,967,
  residual −3,5 k frente a pares +7,5 k (ratio −0,47; cfd −1,15; grupo −1,02).
- **COLA medida directamente** (orden de log_index dentro de cada nivel de precio de una tx = prioridad precio-tiempo;
  STRONG_INFERENCE): cosechadores P(1º)=0,264-0,279 vs azar 0,280-0,291; cfd 0,317-0,338 vs 0,350; **0x2903c7dc 0,18-0,19
  vs 0,29-0,30 (va DETRÁS más que el azar)**. La hipótesis "el bot crea el mejor bid y se ejecuta primero" NO se sostiene;
  la cola no explica el coste/par ni el resultado del único ganador persistente.
- Selección adversa por posición: el ÚLTIMO de un nivel con ≥5 makers pierde −1,8c/acc (barridos grandes = informados);
  el 1º −0,04c. Ser primero no gana dinero: evita lo peor de los barridos grandes.
- **Consecuencia para Vía D**: la prueba real de cola sigue midiendo algo útil (nuestro P(relleno), espera, selección), pero
  ya NO es la incógnita que decide la estrategia. Lo que separa a 0x2903c7dc es SELECCIÓN/GESTIÓN (residual pequeño), no
  prioridad. Siguiente: diseccionar 0x2903c7dc (qué mercados salta, cuándo entra, cómo limita la suelta).
- Capacidad (cota): aun replicando el grupo a reembolso, 548 €/día ≈ 640 $/día exigirían ~125 k$/día de volumen maker
  con PnL comercial ≥0 (≈ 2,5× el volumen diario de cfd) y un reembolso que hoy es ESTIMADO (verificar pagos reales).

### Iteración 2 (13-Oct ~17:10Z) — disección de cosechadores → `informes/m15v5_disecar_cosechador_13oct.txt`, `m15v5_politica_planos_13oct.txt`
- Ganadores persistentes BTC 15m: 0x2903c7dc (8/8 días +), 0x98b84283 (8/8), 0x86b9a88a (7/8). Perfil común (OBSERVED_FACT):
  acaban PLANOS (desequilibrio final P50 0), 1er relleno tarde (T P50 520-850 s), 0 órdenes tomadoras, 0 ventas, menos
  rellenos en el mejor bid (0,61-0,74 vs 0,87-0,88 de los perdedores). Perdedores (cfd, b945): entran a T≈900, ~80
  rellenos/merc, acaban con ~200 acc sueltas (P50), residual −56 $/merc FWD.
- NO cierran el par con tope: el coste marginal del par al completar es >1,00 en 39-46 % (igual que los perdedores).
- 0x2903c7dc salta el 32 % de mercados; en los que salta, los demás cosechadores pierden −6,20 $/merc-wallet FWD vs +0,38
  donde entra (en DESC no había diferencia) → WEAK_INFERENCE de selección (sin variable previa identificada).
- 0x2903c7dc: 41 % de sus rellenos a T<120 s; FWD lado barato a T 60-120 s: [0-0,2) +0,096 $/acc, [0,2-0,4) +0,233 $/acc;
  lado caro [0,6-0,8) −0,19. Lado barato total +5,4c/acc vs caro −4,1c.
- 2903 elegida entre 32 → riesgo de multiplicidad (P(8/8 días) bajo nulo ≈1/256 por wallet, ×32 ≈ 0,125).

### HIPÓTESIS CONGELADA H15-BARATO-MAKER-V1 (13-Oct 17:15Z, ANTES de mirar 08-12 con esta definición)
Origen: tabla de PnL maker por fase×banda de `m15v4_quien_gana_08oct.txt` (05-07, todos los makers) + 2903c7dc.
Regla: rellenos maker de COMPRA en 15m (todos los makers, todas las monedas) con precio p ∈ [0,10-0,40) y T restante ∈
(60, 600] s. Métrica: PnL a resolución por acción y por € (sin comisión; reembolso aparte), colapsado también a
(mercado, lado). Periodos: DESC 05-07 (visto) / FORWARD 08-12 (no visto con esta definición). Gate: FWD EV/€ ≥ +0,05,
IC90 por días > 0, ≥4/5 días +, ninguna moneda negativa con n≥500 acc, sin el mejor día > 0. Controles: misma banda a
T>600 y caro [0,60-0,90) mismo T. Si pasa: sigue siendo SOLO el precio de los rellenos de OTROS; la incógnita para
nosotros es P(relleno) y selección de NUESTRA orden → experimento real/en seco en esa celda.

### Iteración 3 (13-Oct ~17:40Z) — H15-BARATO-MAKER-V1 → `informes/m15v5_barato_maker_13oct.txt`
- Gate congelado: **FALLA**. FWD 08-12 ponderado por volumen +0,227/€ (5/5 días, IC90 días (+0,195,+0,254)), pero por
  (mercado, lado) +0,015/€ (DESC −0,015) y ETH −0,173 / SOL −0,064. Trampa conocida: contar rellenos ≠ mercados.
- Controles: lado caro [0,60-0,90) mismo T −0,089/€ FWD (0/5 días), −0,124 DESC → los makers que compran el FAVORITO
  entre T 60-600 pierden de forma sistemática (OBSERVED_FACT, ambos periodos).
- Exploración (vista, no cuenta): bootstrap por (mercado, lado) FWD +0,227 IC90 (+0,016,+0,445); BTC +0,263
  (+0,024,+0,483); ETH −0,173 (−0,304,−0,041). Mecanismo candidato: en BTC hay más volumen barato en los mercados donde
  el barato acaba ganando (1.483 vs 1.188 $/unidad) → solo lo cobra una puja que SE REPONE.
- **Congelada H15-BARATO-REPOSICION-V1** (`informes/m15v5_hipotesis_congelada_barato_reposicion_13oct.json`, sha256
  d007dcbf…): BTC, compras maker [0,10-0,40), T (60,600], EV ponderado por volumen, forward desde 13-Oct.
  Vigía `vigia_15m_barato_reposicion_forward.py` (cron 05:35, Telegram, caché en datalogs/vigia_15m_barato_reposicion/),
  validado sobre 09 y 12-Oct (+0,272 / +0,232; cola FINAL 12-Oct +0,285 → estar al final de la cola no lo anula).

### Estado al GUARDAR (13-Oct ~18:05Z, Javi: "guarda exactamente ahora")
- Simulación de capturabilidad `analisis_15m_v5_sim_barato_reposicion.py` (puja propia de 5 acc que se repone, cotas
  conservadora/optimista, topes inf/100/25) ESCRITA y compilada, SIN CORRER: la caché BTC del registro 11-12 Oct la paró
  el guardián de RAM (MemAvailable 1.241 MB). Siguiente intento: 1 solo día (M15_CACHE_GLOB=m15_registro/m15_registro_2026-10-12.csv.gz,
  M15_CACHE_ACTIVOS=BTC, M15_CACHE_DIR=datalogs/m15_ms_cache_v5_btc, con guardián) y fuera del racimo 06-09Z.
- Gate 1 del experimento real (dev 44eba08867): fichero = commit (diff vacío), 19 tests + 8 flujos OK, fórmula de peor
  caso revisada a mano. /code-review medium NO lanzada: RECOMENDACIÓN a decidir con Javi → la iteración 1 dice que la cola
  no es la incógnita decisiva; antes de gastar otra revisión, decidir si la prueba real sigue siendo pares ambos lados
  (mide P(relleno)/selección) o se rediseña a UNA puja barata que se repone en BTC (H15-BARATO-REPOSICION, más simple,
  un solo lado). Sin OK formal de Javi no se envía ninguna orden real.
- Pendiente 14-Oct: >03:45Z DEFENSA_V1 (`analisis_pares15_defensa_v1_forward.py`), 05:20 veredicto H5M (5m), 05:35
  primer día forward H15-BARATO-REPOSICION (13-Oct), cron gates 07:03/07:12/07:24 + invariantes, ≥11:32Z WM SEGUIR BTC15.
- Pendiente misión v5: verificar reembolsos REALES (pagos on-chain no identificados: las entradas de pUSD a 0x2903c7dc
  pasan por el proxy 0x84ba…, sin pago diario distinguible → BLOCKED_BY_DATA); A3 re-corrible desde m15_registro con la
  misma caché; WALLET_PRECURSOR_ENGINE para 0xb970fb5c = NO_INCREMENTAL_EDGE como copia (validación 08-12 −858 $), queda
  diseccionar qué precede a las entradas de los 3 cosechadores persistentes (0x2903c7dc, 0x98b84283, 0x86b9a88a) y su
  selección de mercados (2903 salta el 32 %).
- Capacidad honesta hoy: los 3 cosechadores persistentes suman ≈1,3 k$/día comercial en BTC 15m (+≈0,7 k reembolso est.);
  548 €/día exigiría capturar ~la mitad de lo que hoy gana el mejor grupo del mercado. Ninguna vía tiene aún PnL propio
  demostrado.
