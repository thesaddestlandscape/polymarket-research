# H47 — suelo de saldo dinámico + redención (19-Oct 14:50Z)
Repo dev `/root/polymarket-research-dev`, rama dev, commit `0798fc068c` (sobre `0445be4e4f`). Sin órdenes ni cliente CLOB; nada lanzado; no se leyó .env.

## 1. Suelo dinámico (opción b)
- SUELO = saldo verificado en el arranque − PRESUPUESTO_UTIL (12 USD, `--presupuesto-util`; en real nunca > 12; `--saldo-min` eliminado).
- «Verificado» = dos lecturas on-chain seguidas que coinciden (≤0,05) en hasta 3 rondas; se usa la mayor. Si no se verifica: `saldo_min=None`, `puede_enviar` NO envía, `vigilar_saldo`/`run()` paran (fail-closed).
- Cada arranque real escribe `suelo_fijado` (wallet, saldo, suelo, suelos previos). DECISIÓN DE DISEÑO A REVISAR: el suelo = max(saldo−12, suelos previos de esa wallet en todos los ledgers reales H47): un reinicio con acciones aún sin redimir NO amplía el presupuesto (con saldo−12 literal, 15,59 tras 4 $ en posiciones daría suelo 3,59 y 16 $ gastables en total). Si el saldo sube (redención/depósito) el suelo sube. Quitar el `max` = literal (1 línea, `fijar_suelo`).
- Con 19,59 pUSD: suelo 7,59, gasto máximo 12 (el tope de pruebas de 5 € quedó superado por la decisión de Javi). Seco: sin suelo ni lectura de saldo.
- Tests: `/root/polymarket-research/.venv/bin/python -m pytest -q test_experimento_maker_h47.py` -> 55 passed (48 previos + 7 nuevos; 4 previos adaptados). 7 mutaciones (sin guardia None, suelo fijo, sin max previo, 1 sola lectura, min en vez de max, sin tope 12 en real, wallet ajena) -> todas hacen fallar algún test.

## 2. ¿Vuelve sola a pUSD la posición ganadora? SÍ (evidencia, wallet principal; la dedicada no se pudo leer directamente)
- data-api `/activity` de 0xB6eD…028b (1.185 eventos): 80 mercados up/down 5m/15m cerrados >1 h, outcome oficial por gamma `closed=true`. Ganadoras mantenidas hasta resolver: 32/32 con evento REDEEM; retraso REDEEM−fin de mercado min 63 s, p50 69 s, p90 102 s, máx 162 s. 47 perdedoras sin REDEEM; 1 ganadora «sin REDEEM» fue vendida a 0,99 antes (no aplica). `/positions` redeemable=true con valor>0: 0 de 347.
- Nuestro código no redime (0 apariciones de redeemPositions en el repo ni cron): lo hace un lote de terceros (EntryPoint ERC-4337): tx `0x1a98b226…8e814` redime a decenas de wallets a la vez, CTF -> USDC.e -> pUSD, y mint de pUSD a la wallet (3,125 = 0x2faf08 ✓).
- Límite: la dedicada usa el mismo tipo de wallet de depósito (signature_type 3), pero su dirección está solo en el .env (no leído) y tiene 0 posiciones: sin evidencia propia. Control en escalón B: `acciones_onchain` ya detecta acciones sin redimir y el cuadre las admite (`capital_mercado`); si tras ~5 min de un mercado ganado hay acciones y no pUSD, parar y avisar.
- Implicación: un relleno ganador devuelve el pUSD en ~1-3 min; un perdedor lo consume (acciones a 0); el suelo no se ve afectado por ganancias pendientes.

## 3. Para la 2ª /code-review medium
`cd /root/polymarket-research-dev && git diff 0445be4e4f HEAD -- experimento_maker_h47.py test_experimento_maker_h47.py` (231+/24−). Foco: `leer_saldo_verificado`, `fijar_suelo` (max con previos), `puede_enviar` (guardia None), `vigilar_saldo`/`run()` (paradas), `_suelos_previos` (glob de ledgers reales, wallet exacta, ignora seco).
Pendiente: OK de Javi sobre el `max` con suelos previos y sobre gastar 12 USD (no 5 €). NO lanzado: ni escalón A/B ni ensayo en seco.
