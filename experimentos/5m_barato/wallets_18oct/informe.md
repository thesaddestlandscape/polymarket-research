# Wallets 17-18 Oct + @flippingsharks (agente 5, wallet-intelligence) — 19-Oct-2026 ~13:50Z

Estado: **COMPLETE** para (1) y (2) dentro del alcance pedido (informe breve). Etiqueta: EXPLORATORY (descriptivo, no es un gate).
Solo lectura; sin órdenes, sin credenciales, sin gastos. APIs públicas usadas: gamma `public-search` y `markets?closed=true`,
data-api `activity` y `v2/user-pnl` (GET sin autenticación).

## 1. ¿Quién tomó contra los makers baratos el 17-18 Oct y cómo?

Universo: celda H5M (makers que compran el lado c a pc (0,10-0,30], T (60-300] s), mercados 5m de las 6 monedas, on-chain
`VOL/m5_onchain` → `fills_D.parquet`, desenlace oficial 100 %. Reproduce al céntimo al validador (17-Oct −16.274,87 $ / 270.339 $;
18-Oct −47.828,80 $ / 274.154 $). Base de comparación 09-16 Oct.

**Respuesta corta: nadie nuevo. Fue el desenlace, no la contraparte.**

| Pregunta | 09-16 Oct | 17 Oct | 18 Oct | Fuente |
|---|---|---|---|---|
| EV maker celda, ponderado por € | −0,019..+0,197 (6/8 días ≈ +0,06) | −0,060 | −0,175 | `resultados_a1.txt` §0 |
| Nº tomadores / top-10 % del coste / HHI | 3.552-4.100 / 22-31 % / 0,008-0,025 | 3.610 / 21,5 % / 0,009 | 3.470 / 22,5 % / 0,009 | §1 |
| Tomadores «nuevos» (sin coste en 09-16) | — | 193 wallets, 12,5 % del coste, +2,0 k$ de +34,4 k$ (17+18) | | §2 |
| Exceso de acierto del tomador por clase de tamaño (<50 $, 50-500, 500-5k, >5k) | casi todos negativos | −2,1 / +1,6 / +2,0 / +0,6 pp | **+2,9 / +4,0 / +2,8 / +4,0 pp** | §5 |
| Persistencia top-20 tomadores (día A → día B, vs placebo 2.000 grupos) | P(placebo ≥ grupo) 0,26-0,86 | 17→18: 0,76 | 18→17: 0,67; 09-16→17+18: 0,96 | §4 |
| Makers activos / makers nuevos | 888-1.067 | 928 | 905; nuevos 0,8 % del coste | §6 |
| Grupos maker fijados con 09-13 (GANADORA / PERDEDORA / RESTO) | 14-15: +0,12..+0,24 | −0,022 / −0,045 / −0,076 | −0,180 / −0,182 / −0,153 | §6 |
| Binance a favor del tomador ANTES del casado (BTC, 5 s / 2 s, bps) | 0,42-0,67 / 0,23-0,27 | 0,26 / 0,16 | 0,32 / 0,21 | `scripts_19oct/b2.py` |
| % rellenos BTC con ≥1 bp a favor del tomador en los 2 s previos | 13,3-18,1 % | 7,9 % | 12,7 % | b2 |

- **Cómo**: igual que siempre — miles de tomadores de todos los tamaños compran el lado caro (0,70-0,90) contra pujas baratas en reposo.
  No hay más «pick-off» rápido por Binance el 17-18 (menos que la base), no hay concentración nueva, ni wallets que persistan.
  Incluso el minorista <50 $ ganó +2,9 pp el 18-Oct: es un efecto de DESENLACE que afecta a todos por igual.
- **El qué**: BTC es el 89-90 % del coste (BTC −18,8 k$ / −46,4 k$). El lado barato de BTC acertó 18,8 % / 16,5 % (ponderado por
  acciones) frente a 20,4 % de precio pagado (base 21-25 %). Menos mercados con giro (ambos lados baratos en algún momento):
  32,8 % / 31,6 % frente a 39-41 % el 14-16 Oct, pero el 10-Oct tuvo 30,0 % y EV +0,070 → el giro no basta para explicarlo (b4).
  Volatilidad realizada BTC (Chainlink, σ 10 s): 0,80 / 1,22 bps vs 1,8-2,5 el 14-16, pero el 10-11 Oct (fin de semana) 0,56 / 0,89
  con EV +0,07 → Spearman σ↔EV 0,44 en 10 días: débil, no causal (b3).
- **Rareza**: remuestreando mercados BTC del resto de días, P(EV ≤ observado) = 0,097 (17-Oct) y 0,010-0,015 (18-Oct); el 15-Oct es
  el espejo (P(≥) = 0,029). Con todos los rellenos de un mercado compartiendo desenlace, la cola diaria es gruesa: un día −0,19 cada
  ~2 meses es compatible con la población (b4). Pérdida repartida: el 18-Oct, 15 de 24 horas negativas (b1).
- Avisos: el reloj causal (a2) solo empareja el 16-17 % de los rellenos (fila `t` del registro ms por token+precio+tamaño) y el
  subconjunto emparejado tiene otro EV (−0,119 / −0,193): los retornos de Binance son descriptivos. `p_fair` = Φ(z) con σ del día
  entero (mira el día completo) y sobreconfiado (0,32-0,35 vs precio 0,20): NO usar como precio justo.
- **Para nuestra política**: no hay contraparte que esquivar. El riesgo de H5M/H44/H43 es la varianza del desenlace por día y por
  BTC → IC por cierre/día, nunca veredicto con 1-2 días. Hipótesis (sin probar, a pre-registrar si el chief quiere): «retirar pujas
  baratas BTC cuando σ realizada de la última hora < umbral fijado en DESC»; el 10-11 Oct la contradice ya en descubrimiento.

## 2. @flippingsharks como referencia de H39

Dirección (gamma public-search, perfil «flippingsharks», seudónimo Ambitious-Membership): **0xc387c2a40d389f17b723b6bba9b18b7dbd2de4f4**.
Ya estaba en el top-25 de makers de la celda H5M (coste medio 2,6 k$/día; EV celda 09-16 +0,060, 17-Oct +0,019, 18-Oct −0,117).

**Las cifras del post son de TODA LA VIDA, no mensuales** (data-api `v2/user-pnl`, 15-Abr → 19-Oct): realized_market_pnl 59.378 $ /
volume 16,94 M = **0,350 %**; fees_paid 71.946 $ = **0,425 %**; fees_refunded 12.987 + maker_rebate 20.632 = **0,198 %**; 0,35 + 0,43 − 0,20
= 0,58 «spread». El «+58,6 K» es el realized ACUMULADO al 01-Oct (58.734 $). PnL económico total +86,5 k$ (incluye rebates).
Por mes (realized, $): may +14,6 k · jun −1,8 k · jul −7,4 k · ago −0,8 k · **sep +50,1 k** (volumen USDC 1,51 M, +3,3 %) · **oct 1-18 +2,6 k**
(0,46 M, +0,57 %), últimos 3 días −1,8 k / −0,7 k / −0,3 k. Ojo: `maker_rebate` de la serie se congela el 12-Sep pero los eventos
MAKER_REBATE siguen llegando (129-230 $/día en las muestras de sep y oct): el PnL económico reciente está infravalorado ~150-200 $/día.

| Dimensión | Hecho (fuente) | Certeza |
|---|---|---|
| Universo | Sep: 100 % BTC/ETH **5m** (09-14: 100 % BTC 5m). Oct: BTC 5m ~64-72 %, BTC 15m ~21-24 %, ETH 5m/15m resto. Nada fuera de up/down (`act_an.py`) | observado (activity; 5m y 15m cuadran con on-chain al dólar el 17-18 Oct) |
| Maker vs tomador | 5m 09-18 Oct on-chain: MAKER 90 % del volumen (117,7 k$; solo COMPRA, nunca vende), tomador 10 % (fee 240 $). 15m 15/17/18: maker 89-99 % | observado |
| Pares vs dirección | Solo 32 % (on-chain 5m) / 36-48 % (activity) de los mercados tienen 2ª pata; equilibrio mediano 0; acciones residuales 2,1-3,2× las de par. Pares +1,5-3,3 k$/día brutos, residuo −0,7..−3,2 k$/día. **No es cosechador de pares: es maker de un lado que a veces completa** | observado |
| De dónde salió septiembre | Residuo en la pata CARA: en las 3 muestras de sep la pata grande a 0,5-0,7 ganó 77 % (precio 0,60) y a 0,7-0,9 el 93 % (0,80): +5,7 k$ en 3 días; en oct 57 % (0,61) y 88 % (0,81). Precio de compra mediano sep 0,70-0,77 → oct 0,48-0,56. Igual que @mo-money: **el dinero era DIRECCIONAL**, y se ha secado en oct | observado en 3+3 días (09-27 truncado a 5.500 filas): EXPLORATORY |
| PnL visible 5m on-chain 09-18 Oct (sin 10-Oct, inactivo) | +207 $ (maker +840, tomador −633); EV maker ponderado +0,007, IC90 días (−0,015,+0,040), 9 días | observado |
| Rebates | Pagados 129-230 $/día (eventos MAKER_REBATE); ≈ todo su beneficio neto de octubre | observado |
| Cola | En niveles con ≥2 makers rellenados en la misma tx, rango relativo medio 0,73 (azar 0,5); primero 20 % vs 37 % al azar: **va DETRÁS** | observado (5.273 niveles) |
| Causalidad de sus rellenos | Rellenos que ABREN/aumentan desequilibrio EV −0,001, IC90 días (−0,068,+0,065); los que CIERRAN par +0,038 (−0,110,+0,201): no discrimina. El «la pata suelta barata pierde» (7,4 % de acierto a 0,148) es selección ex post (la pata queda suelta PORQUE pierde), no un filtro causal | observado / inferido |

**Lectura para H39** (expectativa ≤0 ya registrada): la mejor referencia pública de «maker en ambos lados, detrás en la cola» da
≈0 de trading en octubre y vive de rebates (~0,7 % de su volumen USDC); su septiembre fue dirección en la pata cara, no spread.
Con nuestras órdenes de 5 acciones los rebates serían céntimos/día. No hay mecanismo de pares que copiar ni que mejorar: lo único
diferencial (sept) fue elegir el favorito correcto a 0,5-0,9, y eso no persistió. Propuesta: H39 no merece cola de cómputo antes que
H47; si se reabre, el control debe ser «sus mismos mercados, misma cola», y el criterio de refutación el ya congelado.
Nunca copiar sus rellenos (on-chain llega ~2,4 s después del casado).

## Reproducción
- (1): `nice -n 19 ionice -c3 python3 -I agrega_dia.py D` (09-18) → `a1_tomadores.py` (→ `resultados_a1.txt`, sha f7d0447335768543);
  `a2_reloj.py D` y `a4_estado.py D` (14-18; cachés en `VOL/datalogs_analisis_caches/wallets_18oct/`); `scripts_19oct/b1.py`..`b4.py`.
- (2): `scripts_19oct/act_pull.py DIAS` → `act_res.py` → `act_an.py`/`act_an3.py`; `fs5m.py`, `fs5m_b.py`, `fs_abre.py`, `fs15.py`.
  Los scripts leen del scratchpad de la sesión: los datos están copiados en `datos_flippingsharks/` (activity gz, `fs_pnl.json` sha c919b61e4a73ecda,
  `fs_ledger5m.csv.gz` sha 13ca50b77570b848, `resol.json` sha f773ba90d26dd78f, filas 15m on-chain `m15_D.csv`); cambiar `SP` para reproducir.
- Ledgers de los 3 tomadores destacados del 17-18 (0x6a7447d2 +2,9 k$ visible en 5m, 0x512c1e90 −19,2 k$, 0x2272e77a −6,4 k$; todos
  BTC 5m, ninguno persistente): `ledger_*.csv.gz`.
- Warnings: PnL visible ≠ total (solo 5m/15m; coberturas en otros mercados no vistas, aunque la activity no muestra otros mercados);
  activity 09-27 truncada (tope de offset 5.500); etiqueta de fecha de `v2/user-pnl` = día siguiente (volumen cuadra con un día de
  desfase); rebate «estimado» 0,2·0,07·p(1−p) por acción infraestima el pagado real; extracción on-chain completa 14-19 Oct
  abandonada (carga >12) porque activity+m15_onchain cubren el universo.
