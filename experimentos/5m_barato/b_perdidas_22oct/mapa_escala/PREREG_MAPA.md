# PREREG MAPA-ESCALA (OLA 6) - 23-Oct-2026 ~09:50Z, escrito y hasheado ANTES de calcular ninguna celda
Objetivo: tabla de nichos donde el mecanismo de B (maker que pone pujas baratas) podria tener volumen y EV, y que suma llega a 200 k EUR/anio. No toca B ni ejecutores.

## Datos y unidad (fijados)
- Fuente de volumen/EV: rellenos ON-CHAIN de makers (taker != EXCH 0xe111...) de `m5_onchain_D` y `m15_onchain_D` (D = 05..22-Oct, 18 dias) y, para 60 min, de `onchain_fills_D` (solo los dias que existan, retencion 4 d) filtrado a los tokens 60min. Mapa token->(moneda, mercado, fin, lado) de las filas k de `m15_registro`. Desenlace OFICIAL: `maker_ms_desenlaces_cache.json` + gamma closed=true para lo que falte; se reporta cobertura (mercados y EUR) y los mercados sin desenlace se EXCLUYEN diciendolo (nunca se rellenan).
- Unidad: fila de relleno maker convertida a "compra equivalente" del lado comprado (venta del token a q = compra del contrario a 1-q, igual que `vigia_5m_barato_maker_forward.unidades_dia`). coste = EUR pagados, pnl = acc*gana - coste. Maker paga fee 0.
- Rebate (INFERIDO, pago no observado): 0,2 x fee taker = 0,014 x (1-pc) por EUR de coste. Toda EV se da SIN rebate (cifra principal) y CON rebate (declarada aparte).
- Niche = (marco in {5m, 15m, 60m}) x moneda (6; 60m solo las del registro) x banda de precio del lado comprado {[0.01,0.05),[0.05,0.10),[0.10,0.20),[0.20,0.30),[0.30,0.50),[0.50,0.70),[0.70,0.90),[0.90,0.99]} con T (s al cierre) en (60, L] con L = 300/900/3600 segun marco. Secundarios descriptivos (no rankeados): T<=60, T>L (pre-ventana), y B-core = (5m, ETH+SOL+XRP, 0.10-0.30).
- Agregados pooled: por (marco, banda) sobre todas las monedas; por (marco, coin).
## Metricas por nicho (todas ponderadas por EUR)
vol = coste medio/dia (EUR) y por dia; EV = sum(pnl)/sum(coste); IC90 por bootstrap de DIAS (2000, semilla 20261023) y por CIERRE (cluster por fin_s, 2000); EV sin los 2 mejores dias; EV DESC (05-13) y OOS (14-22) por separado; n mercados-lado, n makers, share del maker top-1 y top-5 de coste; hit vs precio medio; exposicion concurrente p95 (EUR, malla 1 min).
Mejores makers: elegidos SOLO en DESC (>=30 unidades mercado-lado en el nicho, EV>=+0.05, >=5 de 9 dias con pnl>0) y medidos en OOS; placebo = mismo numero de makers aleatorios del nicho (1000 sorteos), inversion = los peores en DESC. Se reporta su EV OOS ponderado y su volumen.
## Clases (fijadas)
- PERSISTENTE: EV pooled (18 d) > 0 sin rebate, EV DESC > 0 y EV OOS > 0, IC90 por dias del pooled con limite inferior > 0, EV sin 2 mejores dias > 0, maker top-1 <= 30 %, >= 10 dias con >= 20 unidades.
- FRAGIL: EV pooled > 0 y EV OOS > 0 pero falla alguna otra condicion.
- NEGATIVO/CERO: resto. Multiplicidad: 144+ nichos -> se reporta cuantos PERSISTENTE salen y cuantos se esperan por azar (5 % x nichos x P(DESC y OOS>0)); BH-FDR sobre p de dias (una cola, bootstrap).
## Capacidad y euros/anio (formulas fijas)
cap = vol medio/dia OOS (EUR) del nicho (poblacion de makers; NO profundidad en reposo).
Anual cons = 1 % x cap x max(0, min(IC90_inf_dias, EV_sin2mejores)) x 365
Anual base = 3 % x cap x max(0, EV_OOS) x 0.28 x 365 (0.28 = retencion forward maxima observada de exploratorias en el LIBRO)
Anual opt = 5 % x cap x max(0, EV_OOS) x 365   [con rebate se suma 0.014(1-pc) a EV, aparte]
Solo cuentan niches PERSISTENTE o FRAGIL en base/opt; cons solo PERSISTENTE. Capital = f x exposicion p95 (f = 1,3,5 %).
Solape: monedas del mismo cierre rho~0,345 (post_25_27) -> las sumas se dan bruta y con dedup por (marco, cierre): las bandas de un mismo marco/moneda se suman (no se solapan en precio) pero se avisa del solape entre monedas y con B.
## Ranking (fijado)
score = cap_OOS x EV_OOS_inf90dias (EV conservador; si <=0 -> 0), desempate por EV_OOS x cap. Facilidad de reutilizar B: 3 = mismo codigo (5m, lado barato, bid por WS ya existente), 2 = cambia marco/moneda (misma libreria libro_estado_ws), 1 = cambia mecanica (nuevo marco de resolucion o mercado). Top-3 = mayor score entre niches con facilidad>=2; si ninguno tiene score>0 se dice y se listan los 3 de mayor EV_OOS puntual como "no ejecutables".
## Limites declarados de antemano
18 dias (5-22 Oct) de un solo regimen; no hay 2025 on-chain por token (Jon-Becker = markets/blocks sin mapa por token 5m); sports/weather/4h/diario sin identidad de maker en mis fuentes -> INFERIDOS/ESPECULATIVOS, no entran en sumas "medidas". EV de poblacion != EV de NUESTRA cola (B: -0,072 vs poblacion -0,019 en 0,10-0,30).
