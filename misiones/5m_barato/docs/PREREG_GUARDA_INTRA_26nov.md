# PREREG guarda intraventana (N1/N2) + regla del par para BTC — 26-Nov-2026 (borrador del chief; firma = OK Javi + .sha256)
Diseño: alpha-miner 26-Nov (dev-bk enmienda_lo/regla_par/intra/, commit en dev-bk; memoria project_guarda_intraventana_n1_n2_btc_26nov). Nada elegido por EV; parámetros = ParamsDetector firmados 17-Nov. Fijado ANTES de mirar a 1 s.

## Piezas (módulo nuevo `guarda_intra.py`, flag `--guarda-intra` apagado por defecto; NO toca suelo_v34.py a385c9e3 ni suelo_causal.py → L5 del PREREG_SIML intacto)
- N1 (≤2 s): por moneda, filas q (bid 0,03-0,45, tokens 5m) de los 2 s completos previos; alarma si n≥20 y <5 % con d=rx−ex ≤29 ms. Acción: cancelar todas las órdenes B de la moneda (quien=INTRA) y no armar; re-armar solo con DetectorRapidoLive.estado=='lo'; sin tráfico sigue suspendido; excepción ⇒ bloquea y cancela.
- N2: `suelo_v34.pares_hi` evaluada en continuo dentro de la ventana (pares j≥B−1) ⇒ bloqueo hasta la siguiente clasificación.
- BTC: clase v3.4 sin par + par (previo y N2) SOLO si el par hi de BTC coincide ±1 bin con uno de ETH/SOL/XRP; estimador de otra moneda ausente ⇒ par completo (fail-closed); pares solo-BTC → N1.

## Validación (datos reales, npz de bandas por segundo 13-26 Nov vía cron_pesado; market-data-engineer en P4(iii) desde 27-Nov 03:10Z)
- V1 coste: N1 ≤0,5 % y par+N1+N2 ≤1 % del tiempo lo, por moneda, ≥3 días, IC90 por días.
- V2 detección: N1 dispara dentro de los 20 s de ≥90 % de los pares hi, latencia mediana ≤10 s (episodios reales 13-16 Nov en registro ms crudo + picos breves de BTC).
- V3 paridad: vivo == batch sobre el QLog (0 diferencias con entradas idénticas).
- Respaldo: falla V1 o V2 ⇒ solo N2. BTC: si falla V1 de BTC a 1 s con días nuevos, NO se deja fuera sin más (Javi 26-Nov): se mitiga todo lo posible (variantes fijadas antes de mirar, p.ej. N1 con re-armado más exigente, par común ampliado, suspensión por franja con más picos) y BTC queda fuera solo si ninguna mitigación cumple ≤1 % y fail-closed. Nada se re-ajusta con los mismos días.
- Cable a cerrar por el engineer (T10, OK Javi «solucionalo»): la guarda FEED solo cubre Binance muerto (experimento_maker_bk.py:288-296). El engineer verifica si existe guarda de caída del WS de Polymarket y, si no, la AÑADE fail-closed (WS sin mensajes/latido > umbral ⇒ cancelar todo y no armar; distinguir de «sin filas q en banda»).

## Tests T1-T10
T1 lo→hi sintético a 10/20/50 filas/s detectado ≤2 s (+1 s alineación) · T2 n<20 nunca dispara · T3 hueco de tráfico mantiene bloqueo · T4 N2 bloquea hasta w0+300 s · T5 excepción bloquea · T6 flag apagado ⇒ E0 (K1 8.272/26, K6 5.291/20) y shas firmados iguales · T7 paridad vivo/batch con QLog 25-Nov · T8 BTC par común/aislado/moneda ausente · T9 INTRA cancela todo y no re-publica · T10 caída del WS de Polymarket.

## SIM-L
Brazo G de sensibilidad (solo N2 desde npz), declarado antes de E2; N1 no simulable con bins de 10 s. Anexo de desviaciones del PREREG_SIML.

## Orden
1 firma de este prereg (Javi) → 2 market-data-engineer V1/V2 (P4(iii)) → 3 engineer guarda_intra.py + T1-T10 → 4 seco con --guarda-intra --registrar-q (V3) → 5 validador + red-team → /code-review medium (único, al cierre) → OK Javi para encender en ETH/SOL/XRP → 6 BTC con la subvariante.

Firma (OK Javi): OK en sesión con 2 cambios (BTC mitigar antes de excluir; T10 solucionar)  Fecha: 2026-11-26T16:00Z
