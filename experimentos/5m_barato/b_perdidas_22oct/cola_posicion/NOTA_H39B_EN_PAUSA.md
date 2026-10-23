# H39b — EN PAUSA (orden de Javi 22-Oct: primero masterizar B; H39b es una estrategia distinta, no sub-estrategia de B)
NO está preregistrada ni diseñada. Se retiró el borrador de preregistro que se había escrito antes de recibir la orden (no se calculó nada con él). Solo se guardan los parámetros ya propuestos por el chief/Javi:
- ETH, SOL y XRP 5m (misma regla en las tres), ambos lados (BUY post-only YES y NO, nunca tomador, nunca mejorar el mejor bid), banda 0,30-0,70, clip 5 acc, tope de inventario |I| ≤ 15 acc,
  T restante 290 → 50 s, reequilibrado como regla (el lado que aumenta |I| se retira al pasar de un umbral).
- Comparar contra 0xf074dc84 y 0x0ab01745. Gate pedido por Javi: ≥10 días, EV ponderado por € con IC90 por días >0, sin los 2 mejores días.
- Aviso de capital ya detectado: el peor caso por mercado (15 acc netas × ~0,5) supera el tope de pruebas de 5 €.
- Hallazgos de INFORME.md relevantes cuando se retome: 0xf074 nunca precede a B en el mismo nivel; en B la cola delante sale casi toda por cancelación (97 %).
Cualquier reactivación requiere nuevo preregistro y /code-review + capital + OK de Javi antes de órdenes reales.
