# RESULTADO E-RE-AS-B-REWARDS5M (27-Oct-2026 ~13:25Z) — prereg PREREG_REWARDS5M.md sha cf75e0f3… (antes de calcular)
## Veredicto: pool de rewards 5m ACTIVO = 0 medido -> pool×cuota = 0 < AS. Rewards NO pagan hoy en 5m. (No se toco B/produccion; 23 llamadas publicas.)
## M1 MEDIDO (API publica, 27-Oct ~13:17Z)
- gamma + clob `/markets/{cid}` de 8 mercados 5m vivos (BTC/ETH/SOL/XRP x 2 ventanas): `rewards: {rates: None, min_size: 50, max_spread: 4.5}`; `feeSchedule rate 0,07 takerOnly rebateRate 0,2`.
- clob `/rewards/markets/{cid}`: data=[] en 8/8 (y en 1 mercado 15m BTC). Control positivo en el mismo endpoint: `/rewards/markets/multi?order_by=rate_per_day` devuelve mercados politicos con `rate_per_day` 1.026-2.000 $/dia. Busquedas q="Bitcoin Up or Down"/"updown" no devuelven ningun 5m. => los 5m tienen min_size 50 / max_spread 4,5 (por eso la memoria «r: mi 50, ma 4.5») PERO rate_per_day ausente: sin asignacion.
- Doc (https://docs.polymarket.com/programs/liquidity-rewards, leida hoy): «Crypto TWAP Rewards ... $1M en agosto ... This program has ended. The August allocation is no longer active». Caps de agosto 5m: BTC 300k$, SOL/ETH/HYPE/XRP 200k$ a partes iguales (50k$ c/u), BNB/DOGE 50k$. Coherente con `get_total_earnings_for_user_for_day` = [] los 13 dias del 21-Oct (PENDIENTES 21-Oct).
- Formula (doc, Methodology ec. 1-7): S=((v-s)/v)^2·b; Q_one/Q_two por lado (m y complemento); Q_min=max(min(Q1,Q2), max(Q1,Q2)/c) con c=3,0 si medio en [0,10;0,90] (un solo lado puntua a 1/3), fuera de ese rango hay que cotizar dos lados; muestra 1/min al azar, 1.440/dia UTC; normalizado por muestra y por epoch; pago minimo 1 $. «Punto medio ajustado por tamano»: la doc no define el recorte -> supuesto A1 (medio simple).
## M2-M4 (SUPUESTO: pool = cap de agosto /31 /288; NO es el pool actual, que es 0) — rewards5m_salida.txt
Libro5_ms 24-Oct 00:00 (~1,6 h, 18 mercados/moneda x 5 muestras, 360 muestras/archivo; ~25 % «sin_libro» al inicio) y 26-Oct 22:21-24:00Z (igual). Exploratorio: 2 tramos cortos, n=18 mercados por moneda y archivo. Cotizacion hipotetica: bid 50 acc un solo lado (Q_our=S·50/3), en la mejor puja o a 1c del medio; cuota = Q_our/(Q_our+R), R de la masa rival agregada en [Qtot/6, Qtot/2] (A3, no se ve la composicion por participante); variante b = solo niveles >=50 (A2).
| moneda | Qtot rival med (a/b) | cuota a (bajo-alto) | pool escenario $/mercado | ingreso $/mercado (variante b) | p* = ingreso/2,25 |
|---|---|---|---|---|---|
| BTC | 1.2k-2.1k | 0,02-0,06 | 33,6 | 0,4-2,1 | 0,2-0,9 |
| ETH | 175-228 | 0,08-0,27 | 5,6 | 0,5-1,7 | 0,2-0,7 |
| SOL | 66-72 | 0,21-0,41 (b: 0,4-0,56) | 5,6 | 2,1-3,2 | 0,9-1,4 |
| XRP | 20-59 | 0,23-0,59 (b: 0,5-0,8) | 5,6 | 2,8-4,6 | 1,3-2,1 |
Lectura: SI el pool de agosto volviera, el ingreso por mercado (≈0,4-4 $) cubriria el coste AS de UN relleno (50 acc × 4,5-5 c = 2,25-2,5 $) solo con p(relleno)<~0,2-0,7 en BTC/ETH y casi siempre en SOL/XRP (donde casi nadie cotiza en banda: Qtot 20-70, variante b ≈0 -> cuota ~0,8 es artefacto de «sin rival ≥50»). Con p(relleno) mas alto el EV neto es negativo.
## NO medido / supuesto (Fail Loud)
- p(relleno) de una puja de 50 acc a <=1c del medio NO esta medida (B real: 0,05-0,40, fuera de banda -> B no puntua; las AS medidas -4,5..-5,2 c/acc son de pujas en el frente barato/favorito, no a 1c del medio). Cotizar dentro de banda es cotizar cerca del medio, donde el primer tomador esta informado: AS plausiblemente >= la medida.
- Pool actual: 0 (medido). Si Polymarket reabre un programa, la tabla sirve de escala. Composicion por participante, recorte de «tamano», muestras aleatorias y pagos reales: no observables con datos publicos. El libro agregado se uso SIN duplicar el espejo YES/NO (A5: una orden aparece en ambos libros; se cuenta solo el libro del token YES).
- Vigilar: `GET /rewards/markets/{cid}` de 5m cada semana (1 llamada) y changelog de la doc; si `rate_per_day`>0 en 5m, repetir M2-M4 con el pool real.
