# Expansión H55 → H56/H57/H58 (agente event-causality, 20-Oct; fuente: datalogs_analisis_caches/h56_h58/{PREREGISTRO.json,stats_out.txt})
Datos: archivo 12-19 Oct (5m dentro de 15m), maker_ms 15-19 Oct (60m). Entrada tomador a +215 ms, desenlace oficial 100 %. Preregistro escrito ANTES de mirar resultados.

| Variante | n (días) | EV pond. | IC90 cierre | Sin 2 mejores días | Entradas/día |
|---|---|---|---|---|---|
| H55 BTC (5m⊂15m) | 19 (8) | +0,061 | (−0,17;+0,27) | −0,22 | 2,4 |
| H56 alts 5m⊂15m | 111 (8) | **−0,082** | (−0,17;+0,01) | −0,16 | 13,9 |
| H57 15m⊂60m (BTC/ETH/SOL) | 31 (5) | +0,014 | (−0,26;+0,28) | −0,56 | 3,9 |
| H58 5m⊂60m (BTC/ETH/SOL) | 33 (5) | +0,031 | (−0,21;+0,26) | −0,15 | 4,1 |
| Unión H56+H57+H58 | 175 | −0,047 | — | — | 21,9 |

- H56 por moneda: ETH −0,164, SOL −0,143, XRP −0,185 negativas; BNB +0,075 y DOGE +0,031 no significativas. Por precio: ask 0,50-0,60 pierde fuerte; ask 0,90-0,95 +0,073 (n=16, 8/8 días) — corte visto DESPUÉS de mirar datos: solo sirve para un forward desde el 21-Oct.
- H57/H58: la regla del «primer instante» dispara al abrir la ventana con ask 0,50-0,55 (moneda al aire, no favorito).
- 60m⊂4h: missing (el registro no tiene 4h). Control fallido: H55 BTC 06-18 no reproduce el descubrimiento (n=18 +0,105 vs n=36 +0,179, faltan días 06-11): pipeline sin verificar.
- Profundidad a 5 acc: no nos comemos el libro (BTC nivel 1 P50 = 18,6× objetivo); a tamaño R1 (147 $) solo el 38 % en BTC y el 5 % en alts. Lo que limita es que el ask sube antes de llegar: se llena el 47 % de los disparos en BTC; OOS 19-20 Oct: 1 de 6.
- Conclusión: ninguna ampliación llega a EV ≥0,08 real. Brazo F2 de H55 (dry-run) pendiente del execution-engineer (ESPECIFICACION_BRAZO_H55_F2.md). Cron propuesto (NO instalado), 10:40Z, flock + ulimit 3 GB + aviso Telegram si falla; falta comprobar `informe` con `-I`.
