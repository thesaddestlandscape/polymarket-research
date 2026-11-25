---
name: project-q11-barrido-corregido-05nov
description: Q11 barrido corregido (05-Nov-2026, escalera G ETH/SOL/XRP 5m, 26-Oct..04-Nov): los precursores no anticipan el barrido más allá de la geometría (T, L, bid-L); colocarse delante del barrido pierde; puerta geométrica de colocación = EXPLORATORIA post hoc
metadata:
  type: project
---
Hechos verificados el 05-Nov (informe misiones/5m_barato/informes/Q11_barrido_corregido_05nov.md; expediente experimentos/5m_barato/q11/barrido_corr/, HASHES.txt):
- G0 de la escalera G reproduce dec2 exacto 10/10 días (2.938 rellenos). Cruce de cotización en el 55,3 % de los rellenos (S_nivel 98,6 %, cola en L 37 %).
- S_nivel (precios>=2 y pmin<L) EV +0,206 (IC90 cierre −0,12..+0,55); S_wallet +0,458; la pérdida de G0 viene de los rellenos «thru1» (un solo precio bajo L: mejoramos el bid) −0,123, n=2.308.
- Oráculos con reposición: ON60 −0,24, OYD60 (diana del hazard AUC .77) −0,52 0/10 días, ON1 +0,27 no robusto, ANTI60 +0,061 (Δ +245 € en 10 d). El estimando correcto es EVITAR, no colocarse delante (igual que R9-E1 en BTC, oráculo −0,43).
- g_* a tf−300 ms: HGB OOS 0,570 (placebo máx 0,536); solo rellenos con cruce 0,542 ≈ placebo. Binance/cross/Chainlink/fase ≈0,5. Hazard de rejilla: AUC 0,80-0,89 pero un modelo con SOLO T, L, bid-L, moneda, lado da lo mismo (dentro de estratos de bid-L, libro+actividad −0,014..−0,002).
- Evitación continua (cancelar al subir el hazard) = no operar (AVO_B70 206 de 1.630 rellenos). Puerta de colocación (solo decide armar) PG_O50: +129,5 € EV +0,282 frente a G0 −71,5 € en 7 días OOS, pero POST HOC y las reglas simples bid-L>=6/8c solo llevan el EV a ~0.
**Why:** el mandato de Javi «anticipar el barrido» exige saber qué NO funciona y dónde está el dinero (geometría, no precursores).
**How to apply:** no reabrir precursores de barrido sin una fuente nueva (L2 a 5 niveles del logger del 05-Nov, perp/liq 1 s) y un control OWN-only; la puerta geométrica necesita prerregistro forward antes de cualquier uso. Ver [[project-trampas-politicas-hazard]] y [[reference-harness-escalera-g]].
