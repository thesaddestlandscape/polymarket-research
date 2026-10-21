# H62 — «B sin XRP» (preregistro 2026-10-21T10:42:45Z, Javi OK 21-Oct). SOLO MEDICIÓN; B real NO se toca.
**Origen**: LECCIONES_B.md nº7. Población makers ETH/SOL/XRP 09-19 Oct: XRP −0,065 €/€, IC90 por días (−0,124,−0,010), por debajo del resto 9/11 días; primeras 5 acciones −0,039 (−0,095,+0,014). B real XRP (20-21 Oct): −0,084 (n=21). Contradice H35 simulado (+0,121, 3 días).
**Hipótesis congelada**: el maker barato 5m de XRP tiene EV ponderado por € < ETH+SOL (misma celda, mismo periodo); excluir XRP mejora el EV de la cartera de B.
**Forward**: solo datos con relleno posterior a 2026-10-21T10:42:45Z (excluye todo lo usado para formularla: 09-21 Oct 10:08Z). Dos medidas, ambas por posición (mercado-lado), desenlace oficial gamma, EV = Σpnl/Σcoste:
 (a) B real: posiciones XRP vs ETH+SOL de las tandas siguientes (contabilidad_wallet_dedicada/posiciones.csv);
 (b) población on-chain (makers ETH/SOL/XRP, pc∈(0,10,0,30], T∈(60,300] s, «primeras 5 acciones» por maker-mercado-lado, sin nosotros).
**Gate (para PROPONER excluir XRP, nunca para aplicarlo solo)**: ≥10 días independientes de forward; en (b) EV(XRP) − EV(ETH+SOL) con IC90 por días < 0 y EV(XRP) < 0; en (a) n≥40 posiciones XRP y consistente en signo (sin los 2 mejores días EV(XRP) ≤ 0). Si falla (b) o (a) no concluye → sin cambio. Si XRP > 0 en forward → REFUTADA.
**Prohibido**: cambiar monedas de B () por esto antes del gate, tocar K_POR_MONEDA o cortar con n<40. Cambiar el set de monedas de B real exige /code-review + OK de Javi.
**Cómo se mide**: tarea diaria del vigía de B (pendiente de implementar por un agente; hasta entonces, re-correr `scripts/pop.py` y `scripts/pm.py` con días nuevos; fills on-chain tienen retención de 4 días: extraer cada ≤3 días).
