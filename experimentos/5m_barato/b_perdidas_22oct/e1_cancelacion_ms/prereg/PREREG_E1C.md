# PREREG E1C — cancelación en ms contra la selección adversa de B (24-Oct-2026 ~10:40Z), escrito ANTES de calcular ningún EV de política
Pregunta: ¿existe una regla de CANCELACIÓN, decidible con información recibida antes del relleno y con latencia real, que mejore el PnL de B?
Ya visto antes (no ciego): as_b_trades (rellenas aciertan ~18 pp menos que no rellenas), cola_posicion/control_b (antes del relleno el nivel se
vacía: EXIT F 0,733 vs R 0,110). La familia DEPTH está por tanto MOTIVADA por un dato ya visto: sus resultados son, como mucho, EXPLORATORY.

## Método (contrafactual SUSTRACTIVO sobre órdenes REALES, no simulador)
El simulador calibrado (simulador_calibrado/INFORME.md) es NO_REPRODUCE puja a puja (kappa 0,46): no se usa para medir palancas.
Se usan las 3.272 órdenes reales de B (DL/cola_posicion/ordenes_b.json, 20-22 Oct, ETH/SOL/XRP 5m), sus 186 rellenos con print localizado en L2
(cola_posicion/datos/b_l2.csv t_arr, t_print; b_cola.csv pnl, coste, gana; desenlace oficial) y el libro L2 por RECEPCIÓN (DL/cola_vs_cruce/mk).
- Vida de cada orden: [t_arr, fin]; t_arr = llegada localizada en L2 (o t_call0+122 ms si no); fin = t_print (rellena) o t_fuera / t_cancel_int+65 ms.
- Decisión en rejilla de 10 ms por RECEPCIÓN; la señal solo usa datos con recepción <= t. Cancelación efectiva = t + 60 ms (ida y vuelta medida).
- Hora del casado = t_print − 30 ms (recepción del print menos lag p50 exchange→recepción ~26 ms). Un relleno se EVITA si t_señal + 60 <= t_print − 30.
- Una política solo QUITA rellenos (sin recolocación): ΔPnL = −Σ pnl de los rellenos evitados. Supuesto declarado: el resto de órdenes de B igual
  que en la realidad (no se modela la recolocación tras cancelar; las cancelaciones de órdenes que no se iban a rellenar cuestan 0).
- Libros cruzados (best bid Y + best bid N > 1000 milésimas) → la señal de libro no se evalúa en ese instante (no dispara).
Sensibilidad (no elige): cancelación 120 ms; casado = t_print − 80 ms.

## Familias y rejilla (K declarado)
F1 BN: retorno Binance (aggTrade, recepción c[7]) en contra del lado en W∈{100,300,1000} ms ≥ X∈{1,2,3,5} bps → 12
F2 KNIFE5: ask propio (1000 − best bid del token opuesto) baja ≥ d∈{1,2,3} ticks en W∈{300,1000} ms → 6; ask − puja ≤ g∈{1,2} ticks → 2
F3 L15: mid 15m de la misma moneda (token YES, q del registro maker_ms) se mueve en contra ≥ c∈{1,2} c en W∈{300,1000} → 4
F4 TRADE: print que golpea bids del token a nivel > puja en los últimos W∈{200,1000} ms → 2
F5 DEPTH: otros en mi nivel caen ≥ f∈{50,80} % en W∈{300,1000} ms con otros(t−W)≥5 → 4; SOLO (otros ≤0,5 y otros(t−1000)≥5) → 1;
   profundidad delante (bids a niveles > puja) cae ≥ f∈{50,80} % en 1000 ms → 2
F6 EDAD: cancelar a edad ≥ A∈{1,2,5,10} s → 4
F7 COMBO: OR de la mejor de F1 y la mejor de F5 (elegidas en TRAIN); OR mejor F2 + mejor F5; OR de las 3 → 3
K_total = 40 configuraciones; K_test = 7 (una por familia).

## Partición, selección y gate
TRAIN = 20-21 Oct (elige por familia la config con mayor ΔPnL); TEST = 22 Oct (no se usa para elegir).
Métricas: ΔPnL, EV€ retenido (Σpnl/Σcoste), EXCESO = EV_ret − EV_base, P(relleno), rellenos ganadores perdidos (n y €), hit−p de evitados vs retenidos,
por moneda × banda de precio (0,10-0,20, 0,20-0,30).
Placebo: quitar al azar la MISMA fracción de rellenos dentro de cada día (5000), p = P(ΔPnL_placebo ≥ ΔPnL_obs).
Gate (todo): ΔPnL_TEST > 0; p_placebo_TEST < 0,10/7 = 0,0143; IC90 por cierre (bootstrap 2000, semilla 7) de ΔPnL_TEST con límite inferior > 0;
ΔPnL (3 días) > 0 sin los 2 mejores días y sin los 2 mejores cierres; retención de € ≥ 40 %.
Potencia: MDE de ΔPnL = (z_{1−0,0143}+z_0,8)·SE_placebo; días necesarios.
