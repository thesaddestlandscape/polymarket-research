# PREREG BR1 — CONMUTADOR-VOL: ¿el hueco volatilidad prevista − implícita decide CUÁNDO cobra el maker del lado barato? (5m, 6 monedas, banda 0,05-0,30)
Congelado 26-Oct-2026 (polymarket-quantum-alpha-miner, programa BANDA-0-0,30). Escrito ANTES de calcular ningún σ implícito, σ previsto o VG, y antes de que exista ningún día de medida decisiva (≥27-Oct). Lo ya visto está en §7. Cualquier cambio posterior = BR1b con días frescos nuevos. Este fichero no se edita; las aclaraciones van en ADENDA con su sha.

## 1. Decisión que se evalúa
Conmutador por moneda c y hora UTC h. Al empezar h, con información RECIBIDA antes de h, se clasifica (c,h) en ON / MEDIO / OFF:
- ON → maker LARGO en el lado barato (pujar el token de precio 0,05-0,30 o pedir en su complementario);
- OFF → no estar largo barato (lectura de inversión: maker largo en el lado caro 0,70-0,95);
- MEDIO → política base.
Se evalúa sobre la POBLACIÓN de rellenos maker on-chain: mide si el conmutador separa el EV. La captura con cola propia NO se mide aquí (BR2 + arnés); un PASA de BR1 no es € nuestros.

## 2. Mecanismo, pagador y predicción diferencial
El token barato a T s del cierre vale ≈ Φ(−|d|/(σ·√τ_eff)). Si la volatilidad que descuenta el mid (σ_imp) va por detrás de la que viene (la volatilidad es persistente y se prevé con Binance), el lado barato queda mal valorado de forma sistemática durante horas: barato cuando σ_prev > σ_imp, caro cuando σ_prev < σ_imp. Pagador del ON: tomadores que compran el lado caro (persiguen al favorito) cuando el mercado infravalora la cola. Persiste mientras los makers anclen σ al régimen anterior.
Predicciones frente a H0 (ningún rasgo ex ante desplaza el EV del maker barato más allá de moneda/hora/día):
(a) Δ = EV(ON) − EV(OFF) > 0 en días frescos; (b) inversión: en el lado caro el signo se invierte, EV_caro(OFF) − EV_caro(ON) > 0; (c) VG barajado entre días dentro de moneda × bloque de hora no reproduce (a); (d) VG bate a la línea base AR2h (conmutar por el EV realizado reciente).
No es rebautizo: FV v1-v4 / BTC5M-FV-LONGSHOT valoraban CADA mercado como tomador (comisión 4,9-6,7 %/€ en la banda) y no batían al mid; aquí el rasgo se AGREGA por hora y moneda y solo decide si estar como maker (sin comisión). R-TEND, W1 y b_regimen probaron tendencia/eficiencia/coherencia/z240/AR2h como lado CON/CONTRA o nivel diario; «volatilidad realizada vs implícita» quedó declarada NO probada (`b_perdidas_22oct/detector_regimen/INFORME.md` §2).

## 3. Datos y definiciones (todo por RECEPCIÓN ≤ instante de decisión)
- Rellenos: `/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_D.csv.gz`, maker = filas F con `taker` ≠ exchange 0xe111…, dedup tx+log_index; mapa token→(moneda, mercado, lado, cierre) = tokmap `*.k.json` ∪ filas k de m5/m15_registro (nunca `mapa_escala/tokens.json`, truncado desde 23-Oct 01:50Z). Unidad económica = compra equivalente del lado comprado (venta a q = compra del contrario a 1−q). Banda pc ∈ [0,05; 0,30); T = cierre − ts_est ∈ (60; 300] s (misma convención que `mapa_escala`). Se excluyen los rellenos de la wallet dedicada 0x659a…297F.
- Desenlace OFICIAL: `maker_ms_desenlaces_cache.json` ∪ gamma `closed=true`; cobertura ≥99 % del € por moneda × día o se excluye ese (moneda, día) y se declara.
- EV_{c,h} = Σpnl/Σcoste de los rellenos con ts_est en la hora h; pnl por acción = 1{gana} − pc; maker sin comisión; rebate aparte = 0,014·pc·(1−pc) por acción (no entra en el gate).
- σ_imp (por mercado 5m de la moneda c, fotos cada 10 s con T ∈ [90; 240] s): mid_up = (bid+ask)/2 del token Up en la última fila q de `m5_registro` recibida ≤ t (ordenar por recepción: el fichero NO es cronológico), exige ask − bid ≤ 0,03 y libro no cruzado; S_t = último tick Chainlink RTDS (`data/prices/chainlink_D.csv`, solo `source=chainlink`, por recepción); ref5 = twap60 oficial de apertura (`polybolt_D` canal twap60, `source=chainlink`, recibido ≤ t); d = ln(S_t/ref5); τ_eff = (T − 62) + 59/3 s; z = Φ⁻¹(mid_up), foto válida si 0,10 ≤ mid_up ≤ 0,90, |z| ≥ 0,15 y signo(d) = signo(z); σ_imp = d/(z·√τ_eff). Si no, missing (se reporta la tasa por moneda y hora).
- σ_prev: log-HAR por moneda ajustado SOLO con klines 1m de Binance de 2025 (`/root/polymarket-research-datalogs/regimen_5m/barras_y2025.npz`; si falta una moneda, GET público de klines 1m 2025 sin clave): ln RV_{siguientes 5 min} = a + b1·ln RV5 + b2·ln RV30 + b3·ln RV240 (barras cerradas). Coeficientes congelados (con su sha) ANTES de leer octubre. En octubre: barras 1m de bookTicker (`regimen_lib.py`) cerradas ≤ t; hueco >5 min ⇒ missing.
- VG_{c,h−1} = mediana de ln(σ_prev/σ_imp) en las fotos válidas de c en la hora h−1 (≥30 fotos; si no, MEDIO).
- Clases: cortes por moneda = terciles de VG en CAL (05..21-Oct) calculados SOLO con valores de VG (sin mirar EV): VG ≤ q33 → OFF; VG ≥ q67 → ON; resto MEDIO. En WF-ALL los cortes se recalculan cada día con días anteriores.
- Línea base AR2h_{c,h} = EV poblacional largo barato (misma banda y T) de los mercados con cierre ≤ inicio(h) − 60 s y cierre ≥ inicio(h) − 2 h; terciles en CAL igual que VG.

## 4. Periodos
CAL 05..21-Oct (ya visto a nivel de EV por banda y día: solo sirve para cortes; el HAR no se toca). WF-ALL 05-Oct..fin (descriptivo; ≥30 días el 04-Nov). FRESCO = días UTC completos ≥ 27-Oct con m5_onchain del día y del siguiente: DECIDE. Miradas a 10, 20 y 30 días frescos (≈06-Nov, 16-Nov, 26-Nov); entre miradas solo se mira n y cobertura.

## 5. Métrica y gate (FRESCO, en cada mirada)
Δ = EV(ON) − EV(OFF), ponderado por €, todas las monedas juntas (ponderación por €). IC90 bootstrap por DÍA (2.000, semilla 20261026) y por cierre (1.000).
PASA si TODO: G1 ≥10 días frescos y ≥30 días en WF-ALL; G2 Δ ≥ +0,04 e IC90 por días inferior > 0; G3 placebo (clases permutadas entre días dentro de moneda × bloque de 6 h, 2.000) p < 0,01 (3 miradas, K=2); G4 Δ sin los 2 mejores días > 0; G5 Δ > 0 (punto) en ≥4 de las monedas con ≥100 unidades mercado-lado en ON y en OFF, y en ambas mitades del tramo fresco; G6 inversión EV_caro(OFF) − EV_caro(ON) > 0 (punto) en la banda 0,70-0,95; G7 EV(ON) ≥ +0,03; G8 Δ_VG ≥ Δ_AR2h (punto).
REFUTADA si Δ ≤ 0 o IC90 por días superior < +0,02 (en cualquier mirada ≥10 días). INSUFICIENTE en otro caso (se dice qué G falla y la fecha de la siguiente mirada; nada se reajusta).
Potencia declarada: con sd diaria de Δ ≈0,12 (supuesta desde `mapa_escala`), el efecto mínimo detectable a 10 días es ≈+0,07; un efecto real de +0,04 necesita ~30 días.
Descriptivos (NO deciden, BH-FDR entre ellos): VG diario (d−1 → d); ACF y semivida de EV_{c,h} y de VG (retardo de identificación); clase TREND/REVERT/MIXTO de `regimen_lib.py`; DAYT/VOLR; mediana de spread y tamaño del top por (c,h); cuota del € tomador de perdedoras persistentes en las 2 h previas; sub-bandas 0,05-0,10/0,10-0,20/0,20-0,30; BTC solo y sin BTC; con rebate; cruce con la clase C3 de BR2.

## 6. Salvaguardas
Ninguna fila con recepción > inicio(h) entra en VG_{h−1} ni en AR2h_h; los rellenos de h no entran en sus propios rasgos; libros cruzados fuera; filtrar `source` siempre; IC por día y por cierre (racimos entre monedas); EV ponderado por € y también por unidad mercado-lado; sin 2 mejores días; cobertura y missing declarados; un resultado espectacular se trata primero como bug.

## 7. Ya visto (declarado)
EV poblacional por banda × moneda 06..21-Oct (`mapa_escala`), 17..22-Oct (`cola_vs_cruce`, W1), 20..22-Oct (−0,045), 24..25-Oct (vidas virtuales RE-AS-B); detector_regimen / b_regimen (tendencia, AR2h, H-N2). Nunca se ha calculado σ_imp ni VG. Ningún dato ≥27-Oct.

## 8. Recursos y entregable
Un trabajo pesado a la vez; `nice -n 19 ionice -c3`, `ulimit -v 3000000`; nunca 06:00-09:30Z ni con load5>4; checkpoint por día. Código en `experimentos/5m_barato/banda_0_30/br1/` (diff y sha de cada script en el informe). Entregable: `alpha_miner/banda_0_30/RESULTADO_BR1.md` con PASA/REFUTADA/INSUFICIENTE por mirada.
