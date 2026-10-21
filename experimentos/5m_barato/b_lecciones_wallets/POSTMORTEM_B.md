# POSTMORTEM B (H47-B real) — 21-Oct, agente wallet-intelligence (EXPLORATORY; texto guardado por el chief)
Corte: contabilidad 21-Oct 10:08Z (`posiciones.csv` sha b0014a95d6e82d2c, `movimientos.csv` 20d80e67f0b0ec26), 78 rellenos, 73 posiciones (mercado-lado), desenlace oficial gamma 108/108 pujas. Cuadre con posiciones.csv: +14,089.

**Total**: n=73, 16 ganadas, coste 84,25, PnL +14,09, EV ponderado +0,167. IC90 bootstrap por posición (−0,27,+0,64), por cierre (−0,29,+0,69; 39 cierres). Mejores 3: +8,90/+8,90/+7,92. **Sin las 2 mejores: −3,71 (−0,045).** Solo 2 días (20 y 21-Oct): «sin los 2 mejores días» no calculable. Aciertos 21,9 % frente a precio medio 21,5 %.

Celdas = posiciones / ganadas / PnL $ / EV pond. Casi todas n<15 (EXPLORATORY, sin cortes).
| Dimensión | Celdas |
|---|---|
| Día | 20-Oct 37/8/+3,01/+0,070 · 21-Oct 36/8/+11,08/+0,269 |
| Moneda | ETH 30/6/+3,23/+0,093 · SOL 22/7/+12,79/+0,481 · XRP 21/3/−1,93/−0,084 |
| Banda precio | 0,10-0,15 13/4/+23,00/+1,64 · 0,15-0,20 12/2/−0,58/−0,05 · 0,20-0,25 24/5/−1,28/−0,05 · 0,25-0,30 24/5/−7,05/−0,22 |
| Moneda×banda | ETH 0,15 0/8 · XRP 0,25 0/7 · ETH 0,10 2/5 +12,59 → ruido |
| Tanda (n) | 1 +0,08 (5) · 2 +5,00 (4) · 3 −4,45 (4) · 4 +9,35 (10) · 5 −4,62 (8) · 6 −2,35 (6) · 7 +18,26 (25) · 8 −4,83 (4) · 9 −2,34 (7). La tanda 7 aporta más que el total |
| Hora UTC (n) | 06-09 +18,26 (25) · 09-12 −4,75 (14) · 12-15 −2,34 (2) · 15-18 +9,90 (18) · 18-21 −6,97 (14) |
| T restante al relleno | 60-120 s 7/+8,92 · 120-180 s 19/+15,12/+0,68 · 180-240 s 23/+2,03/+0,07 · 240-300 s 24/−11,97/−0,43 |

**Selección adversa**
- Rellenadas 21,9 % (precio 0,215) vs no rellenadas 37,1 % (último bid 0,203); Fisher p=0,11. No rellenadas con precio ≥0,25: 9/13 ganan (subió y se canceló por banda).
- Markout por € (puja_fin, recepción, n=63): mediana −0,13 a 5 s, −0,19 a 30 s, −0,77 a 120 s (14 missing, probablemente perdedoras).
- Binance en contra antes del casado (bookTicker por recepción): R1 ≥2 bps en contra en [−10,−1,5] s: 20-Oct 11 pos −0,59 (resto +0,33); 21-Oct 7 pos −1,0 (resto +0,52). R2 T>240 s: 20-Oct 15 −0,37 (+0,37); 21-Oct 9 −0,53 (+0,54). R3 cancelación en vuelo: no consistente entre días. R5 precio>0,25: −0,18/−0,19 vs +0,17/+0,47.
- **Población independiente** (makers ETH/SOL/XRP, pc∈(0,10,0,30], T∈(60,300], sin nosotros; 09-21 Oct; on-chain; desenlace 100 %; Binance a bloque −2,4 s ±1,5 s): R1 NO replica (+0,070 vs +0,078; primeras 5 acc +0,052 vs +0,025; n=220.601 rellenos). R2 no concluye. R5 no replica (0,25-0,30 +0,028 primeras 5). **XRP** es la única pista que aguanta: −0,065 IC90 días (−0,124,−0,010), por debajo del resto 9/11 días; primeras 5 acc −0,039 (−0,095,+0,014).
- Nuestros rellenos con Binance ≥2 bps en contra: 24,7 % vs 23,7 % en la población: las contrapartes no están más informadas.

**Regla que lo evitaría: ninguna validada.** Única pista con soporte fuera de muestra: no pujar en XRP; preregistrar y juzgar en forward (≥10 días, EV/€ con primeras 5 acciones y real). Nunca cortar con estos n.
Avisos: 21-Oct parcial (hasta 10:08Z); hora población = bloque −2,4 s (±1,5 s); bookTicker no es tick a tick; 15m no medido; rebates de maker no visibles en la wallet. Scripts en `scripts/` (sha en el informe del agente; `common.py`, `build.py`, `pm.py`…).
