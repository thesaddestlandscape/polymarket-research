# Calibración de las colas del shadow A6 (20-Oct 10:00-11:35Z) — solo lectura

**Fuente:** `libro5_ms_*` (feed crudo B/d/T, hora de RECEPCIÓN, orden de seq), no `maker_ms_*` (solo cima del libro). 17-Oct 10:33Z → 20-Oct 10:10Z, 4 días (17 y 20 parciales). Libros cruzados descartados (57), muestras con hueco G descartadas (4). Scripts y tablas: `calib_colas/`.
**Método:** puja virtual de 50 acc al mejor bid en (0,10-0,30], 1 por (token, tramo de T de posteo, tipo); tramos 60-140/140-220/220-270 (A6 no entra >270 s); viva hasta T=60; L=85 ms. Una bajada de nivel se explica por un trade si cae en [-300,+150] ms (el d llega ~100 ms antes que el T; 91-93 % del volumen emparejado). Cancelación = bajada no explicada. Sin ids de orden no se sabe si lo cancelado estaba delante: 3 repartos (lo = detrás primero, prop, hi = delante primero).
**Validación:** el nivel reconstruido coincide con la `cola` leída por REST en 917/932 órdenes reales de H47-A (98,4 %, error mediano 0).

## Parte A — DEFINITIVA para BTC (n=2.248 pujas, 859 mercados, 4 días)
- **c = fracción de lo que hay delante que desaparece por cancelación antes del 1.er relleno** (suma/suma): prop **0,90** (IC90 por días 0,88-0,92); lo 0,84 (0,81-0,88); hi 0,92 (0,90-0,94). Bloque 1 h: prop 0,886-0,900. Estable por día (prop 0,88/0,89/0,91/0,92).
- Por bucket (prop): 0,10-0,15 0,94 (n=349); 0,15-0,20 0,95 (246); 0,20-0,25 0,90 (257); 0,25-0,30 0,83 (1.396). Por tramo: 0,91/0,91/0,88. Subconjunto con disparo A6 (cum≥5000, n=371): 0,85 (0,84-0,87).
- En volumen tomador: basta comerse **0,10×D0** (0,08-0,19) para llegar a nosotros → c≈0,9 ≈ **opt** (c=1), lejos de base (0,5) y cons (0).
- En **tiempo**, el replay no es opt: P(relleno ≤2 s) opt 0,83, hi 0,71, prop 0,64, lo 0,59, base 0,60, cons 0,57; mediana 1.er relleno opt 0,3 s, prop 0,9 s, base 1,05 s, cons 1,3 s. Factor equivalente f* (mejor ajuste de la curva de relleno): prop **0,3**, rango [0,1 (hi) – 0,7 (lo)]. Acuerdo puja a puja ≤2 s con prop: base 0,92, cons 0,91, opt 0,81.
- ETH (parcial: 934 pujas, ~300 de 439 mercados alternos, 3 días): c prop 0,98 (0,97-0,99); f* 0,1-0,9. SOL/XRP: **no medidos** (job parado para ahorrar cuota). Por celda moneda×bucket×tramo ver `tablas_BTC.txt`; celdas T220-270 con n<40 son orientativas.

**Veredicto A:** en cancelación, la cola es mucho más cercana a **opt** (c≈0,9) que a base/cons; en tasa/tiempo de relleno, **base** es la mejor de las tres (opt sobreestima +19 pp a 2 s; cons −7 pp). Adoptar **base como central y reportar siempre el rango [opt, cons]**; no citar EV con una sola cola. Límite no resoluble con estos datos: el reparto delante/detrás (f* 0,1-0,7). Relleno final (≈97 %) casi igual en las tres: no discrimina.

## Parte B — DATA_BLOCKED (n=0 rellenos reales)
Los 932 pedidos reales de H47-A estaban a 0,01-0,03 (sin relleno por diseño; `verificada f=0`); el resto de ledgers (`pares_*`, `seco`) tienen `real:false`, rellenos simulados; la wallet 0x659a no tiene fills on-chain 16-20 Oct. Nada que calibrar. Datos reales útiles: acuse mediano 79 ms, visible en el WS 254 ms tras el envío (p90 573): L=85 ms es optimista con el camino H47. Para ±8 pp de tasa con p≈0,5 harán falta ~100 órdenes B; hasta H47-B no se declara ninguna cola calibrada.



## Parte A — TODAS las monedas (20-Oct ~16:30Z, `calib_colas/final_tabla.py`, tabla completa en `tabla_monedas.txt`/`tabla_monedas_alts.txt`)
Mismo método (libro5, L=85 ms, ventana [-300,+150] ms, 4 días 17-20 Oct, ~852-859 mercados/moneda). c = fracción de la cola delantera que desaparece por cancelación; IC90 por 4 días (pocos días: IC orientativo).
| Moneda | n pujas | c prop (IC90 días) | c lo-hi | f* hi/prop/lo | Cola recomendada (rango) |
|---|---|---|---|---|---|
| BTC | 2248 | 0,900 (0,876-0,923) | 0,844-0,922 | 0,1/0,3/0,7 | base (opt..base) |
| ETH | 2382 | 0,966 (0,937-0,995) | 0,942-0,970 | 0,1/0,2/0,5 | base (opt..base) |
| SOL | 2431 | 0,968 (0,953-0,984) | 0,915-0,973 | 0,2/0,2/0,9 | base (opt..cons) |
| XRP | 2505 | 0,966 (0,959-0,973) | 0,893-0,972 | 0,2/0,3/0,5 | base (opt..base) |
| DOGE | 2508 | 0,974 (0,962-0,987) | 0,914-0,981 | 0,1/0,1/0,4 | base (opt..base) |
| BNB | 2353 | 0,967 (0,948-0,986) | 0,913-0,973 | 0,4/0,4/0,9 | base (base..cons) |
Relleno final (prop): BTC 0,98, ETH 0,93, SOL 0,88, XRP 0,82, DOGE 0,73, BNB 0,70 (las alts tienen menos relleno; la distancia opt/base/cons es pequeña, <0,03, salvo BTC 0,07 a opt). Caveat: ETH/SOL/XRP/DOGE/BNB sin sensibilidades L/ventana; el reparto delante/detrás sigue sin resolverse.
**Sensibilidades BTC (solo día 19, 2 días-bloque, mercados alternos, IC90 muy ancho):** L=79: c prop 0,871 (0,72-1,02); L=254: 0,893 (0,77-1,01); ventana 1000 ms y 150 ms: 0,871 (0,72-1,02) idéntico. Cola recomendada sigue siendo base en todas. Conclusión: c≈0,87-0,90 no depende de L ni de la ventana dentro de lo medible. Parte B sigue DATA_BLOCKED.
