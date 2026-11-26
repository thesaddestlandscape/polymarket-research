# PREREG_SIML — simulador v-next de B (SIM-L), 26-Nov-2026 (borrador del chief; firma = OK de Javi + `.sha256` de este fichero)
Base: CONTRATO_D3_SIML_P1_25nov.md §2 + RESOLUCIONES DEL CHIEF; VALIDACION_PAQUETE_P1B_SIML_25nov.md (DATOS, RED-TEAM, /code-review, verificaciones 26-Nov). Código: /root/polymarket-research-dev-bk rama b-k-ejecutor, HEAD del commit que cierre la última pasada del engineer (se anota al firmar) + `b_k_pins.json` vigente. Ningún parámetro de este documento se ha elegido por EV. E2 (EV) sigue PRECINTADO hasta la mirada 1.

## 1. Qué es y qué no es
- SIM-L = replay de B con latencias y reloj vigentes (passT_v4/stamp_v3, latencia de paquete_l 13-Nov, clase de suelo por ventana). Es **secundario precintado**: no rescata a v3.3 ni sustituye a la mirada 1.
- Texto obligatorio: «La corrección de la llegada (88 → 34 ms desde t_envío) se decidió DESPUÉS de ver la sensibilidad de K1 del 17-Nov (3 rellenos de diferencia). El valor sale de paquete_l (`place_ex_menos_envio_ms` p50) y no del EV; el brazo 47 (p90) se reporta siempre. Por eso SIM-L es secundario precintado y no rescata a v3.3.»

## 2. Parámetros congelados (principal; brazos de sensibilidad siempre reportados)
| P | Principal | Brazos | Fuente |
|---|---|---|---|
| L1 llegada | t_envío + 34 ms | 35, 47 | paquete_l B3/B5 `place_ex_menos_envio_ms` |
| L2 ventana de cancelación | desde t_envío | — | código vivo `_post_real` |
| L3a canc_block | 57 ms | — | `latencias.d_red_cancel_ms.p50` B2/B3/B5 |
| L3b post_block | p50 (t_ack − t_envío) de P1b real si P1b sale COMPLETE antes de abrir E2; si no, 59 | 0, 59, 88 | regla del 25-Nov; ledger B3 59,3 |
| L4 DEC | **condicional, ver §3** | 3, A, 50 | seco A 25/26-Nov |
| d_env | 7 ms | 0, 3, 10, 12,5 | seco A: p50 6,88 / p90 12,5, n=699 |
| L5 población | clase GuardaSuelo **v3.4** (`--version-clase v3.4`, = la del ejecutor a desplegar) | v3.3 (lo = p5 14,25-24,25) | suelo_v34.py |
- Congelado además: rf5_cortes.json 4e88fb3c, K1-K4/K6, F5/Calma/V5/V6, t_proc 1,0, modelo de relleno, comisión 0,07·p(1−p) tomador / rebate 0,20 maker, unidad = 1.er relleno (mercado, lado), mismos días válidos que v3.3. `no_armar` se re-llama en t_envío igual que el vivo.
- Redondeo declarado: el simulador firmado trabaja en ms enteros (`int(t+d_alta)`). En el brazo d_env 12,5 la llegada y el bloqueo se redondean hacia arriba al ms siguiente (+47 y +72 ms desde t_dec; `ms_reloj`, conservador). La re-llamada a `no_armar` en el envío va en t_dec + 12,5 exacto, sin redondear; por eso el t_envío derivado (t_llegada − L1) queda en +13. Diferencia declarada de 0,5 ms, solo en ese brazo y no elegida por EV.

## 3. Regla condicional de L4 (fijada ANTES de ver la validación)
- Principal por defecto: **A = U(3,103) + 3 ms** (cadencia 100 ms + proceso), dec='A'.
- Pasa a **R** (A-reinicio, distribución medida) SOLO si la validación KS SIM-L vs seco A (`siml_valida_l4.py`, 27-Nov ≥14:00Z, `ks_sim_vs_seco.json`) da **PASA**: D < 0,05 en los 6 contrastes (moneda ETH/SOL/XRP × estadístico: lag al primer cambio y cambios por lote) con ≥100 lotes, misma población (lotes coincidentes con evaluaciones de `no_armar`), excluido 2026-11-26T00:10-00:20Z (cron contaminante, declarado antes). La KS sin exclusión es solo sensibilidad.
- FALLA, INSUFFICIENT o BLOCKED → se queda A. No se repite la KS con otros días ni otros umbrales para «conseguir» R.

## 4. Medición (cuando se abra E2, tras la mirada 1)
- EV ponderado por € y por unidad; EV incondicional por puja armada (no rellenada = 0 € con capital ocupado) y P(relleno)×EV|relleno; denominador de armables incluye vetadas por F5/Calma/V5/V6.
- IC t por días (n efectivo = días), sin los 2 mejores días, por moneda y por clase de suelo; Δ pareado SIM-L − v3.3 por día.
- E0 identidad (todo apagado = v3.3 en 17-Nov: K1 8.272/26, K6 5.291/20) debe cumplirse antes de abrir E2.
- Trazabilidad: cada brazo con commit, sha de la cadena (`manifest_codigo`), npz/manifest_suelo usados y árbol limpio; sin eso, no cuenta.

## 5. Desalineaciones residuales declaradas
- Binance en SIM-L con reloj del grabador (m5_registro) vs WS propio del vivo.
- P1b: lote 3/3 vs referencia 8/12 y GTD (paquete_l) vs GTC (ejecutor), como supuesto del ancla post_block.
- El seco del 25/26-Nov solo ejercita la clase lo (0 hi, 0 mixta).
- Sensibilidad de L1 sin información el 17-Nov: los brazos 35 y 47 ms dan órdenes, rellenos, tau y cancelaciones idénticos a la base en K1 y K6 (y el 25-Nov igual); desplazar la llegada 1-13 ms no toca ninguno de los 26-32 rellenos del día. Se reporta L1 en cada día nuevo; con un solo día no permite concluir nada sobre la llegada.

## Firma
- [x] OK de Javi (fecha/hora UTC): 2026-11-26T11:08Z  ·  commit: dev-bk b-k-ejecutor e7b00537130 (pins 51) · main 6e86abd1ab0 (cron_pesado e452ecbd) · SIM-L de referencia: out_siml_26nov_v4/siml_2026-11-17.json (COMPLETE, sello RF5 a5161ce9a7df8294) ·  sha256 de este fichero → `PREREG_SIML_26nov.md.sha256`
