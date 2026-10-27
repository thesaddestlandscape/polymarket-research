# PREREG E-AM-M2 — COLCHÓN-PARIDAD (fase 1: población on-chain, fuera de muestra)
Autor: polymarket-quantum-alpha-miner, 26-Oct-2026 (escrito ANTES de mirar ningún dato de 24-Oct en adelante; manda mtime + sha256 del fichero, no esta línea).
Mecanismo (MECANICAS_NUEVAS.md M2): vendedores ocasionales liquidan el token barato por debajo de la paridad con el token opuesto; un bid profundo solo rellenado en ese estado cobra a quien vende bajo paridad.

## Definiciones (congeladas; se reutiliza el código de descubrimiento SIN cambiar la lógica)
- Fuente: `/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_D.csv.gz` (maker y tomador explícitos, fee real). Mapa token→(mercado, lado, moneda, cierre) y desenlace OFICIAL (gamma `closed=true` / `maker_ms_desenlaces_cache.json`); cobertura de desenlace en € ≥99 % por moneda y día o el día se excluye y se declara.
- Universo de eventos: rellenos maker de COMPRA (pasivos) en mercados Up/Down 5m de BTC, ETH, SOL, precio p<0,10, excluida la wallet 0xb0f85baa… (W), igual que f25.
- Estado G: gap = (1 − último precio operado del token opuesto en un bloque ANTERIOR al del relleno) − p ≥ 0,05. Cálculo idéntico a `wallet_pspspsps5/senales_externas/scripts/f24_otro_lado.py` (sha256 16 bb15385e171f5362) y f25 (fb16d8512e85a2cd); solo se cambia la lista de días. Rellenos sin opuesto previo en el mismo mercado: fuera (se reporta su número).
- Unidad de inferencia: mercado-lado (Σ de los rellenos en G del mismo (m,s)); EV ponderado por € = Σpnl/Σcoste (pnl maker sin fee, rebate aparte y NO incluido en la métrica primaria). IC90 bootstrap por DÍA de cierre (2.000 réplicas, semilla 20261026) y, como secundario, por cierre.

## Periodo
- OOS: días de cierre desde **2026-10-24** (incluido) — nunca mirados por f24/f25 (05-23 Oct). Primera lectura decisoria cuando haya **≥10 días completos** (previsto 2026-11-03). Lecturas intermedias solo de cobertura (n por día), sin EV.

## Métricas
- Primaria: EV_G (BTC+ETH+SOL, p<0,10).
- Secundarias: Δ = EV_G − EV_resto (rellenos maker de compra p<0,10 sin G, mismo día×moneda×tramo de precio de 0,01, reponderado al mix de G); EV_G por moneda; EV_G sin los 2 mejores días; acierto/precio por cuenta y por €; placebo: gap permutado dentro de día×moneda×tramo (como f25, 200 permutaciones); descriptivo: EV_G con vendedores no repetidores vs repetidores (definición f23, sin decidir nada).

## Criterios (K=1 hipótesis primaria; α=0,05 unilateral)
- **PASA fase 1** si TODO: ≥10 días; n_G ≥ 800 unidades mercado-lado; EV_G ≥ +0,10; IC90 por días de EV_G > 0; EV_G sin 2 mejores días > 0; IC90 por días de Δ > 0; EV_G real > percentil 99 del placebo; BTC con EV_G > 0.
- **REFUTADA** si con ≥10 días y n_G ≥ 800: EV_G ≤ 0, o IC90 de Δ contiene 0.
- **INSUFICIENTE** en cualquier otro caso (se sigue acumulando sin cambiar nada; segunda lectura a ≥20 días).
- Cualquier cambio de umbral, banda o moneda tras ver datos = versión nueva con su propio OOS.

## Lo que NO decide esta fase
Capturabilidad. Si PASA, fase 2 (prereg aparte, antes de mirarla): con libro WS/registro ms y la etiqueta [pes, opt] calibrada contra rellenos reales de B, fracción del flujo G que se llevaría una puja de 5 acc colocada en el nivel ≤ (1 − opuesto) − 0,05, y EV de ESOS rellenos. Sin fase 2, 0 €.

## Coste y recursos
Lectura de 1 fichero diario (~cientos de MB gz) por día con zcat en streaming; <5 min CPU/día; `nice -n 19 ionice -c3`, `ulimit -v 3000000`; nunca 06:00-09:30Z ni con load5>4. Sin órdenes, sin crons, sin tocar B.
