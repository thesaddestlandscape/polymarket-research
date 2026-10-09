# experimento_pares_cola_15m.py — 12ª pasada de /code-review (09-Oct ~06:50Z), hallazgos SIN APLICAR

Fichero: `/root/polymarket-research-dev/experimento_pares_cola_15m.py`, commit de dev `feb09b531b` (aplica los 10 de la 11ª).
Ensayo en seco: NO hecho (parado por Javi, "céntrate solo en el review"). Copia de la versión 11: scratchpad de la sesión del 09-Oct.

| # | Línea | Dinero | Hallazgo | Corrección propuesta | Origen |
|---|---|---|---|---|---|
| 1 | 472 | SÍ | orderID ≠ hash: h queda `sin_coste`, nunca se cancela ni se cuenta; si h sí está en el libro, queda sin control y fuera del presupuesto | cancelar h y oid; h sigue contando completa (sin `sin_coste`) | regresión del #4 de la 11ª (antes success:false sí cancelaba h) |
| 6 | 481 | SÍ | en el descuadre se cancela y sigue un orderID de la respuesta, que no es un hash propio: en la wallet compartida podría ser de un ejecutor live | tocar oid solo si get_order(oid) confirma que es nuestra (dirección, token, precio y tamaño iguales); si no, kill sin tocarla | ya existía; choca con el #1: resolver los dos juntos |
| 2 | 685 | SÍ | resolver_inciertas cierra con la suma de /trades aunque el ledger tenga un relleno MAYOR leído de get_order | presupuesto = máximo de todos los rellenos conocidos, nunca el último | ya existía |
| 5 | 667 | SÍ | un solo `verif_trades_maker ok` abre para siempre el cierre por /trades, también con suma 0 cuando no hay filas | cerrar por /trades solo si la suma = tamaño completo; si no, sigue incierta | debilidad del #3 de la 11ª |
| 3 | 725 | SÍ | MATCHED/FILLED con size_matched retrasado pasa por "cancelada por el exchange" y se cierra con un relleno menor | MATCHED/FILLED = relleno completo, max(size, size_matched) | el #2 de la 11ª lo hereda (antes era peor: cerraba al momento) |
| 10 | 483 | SÍ | success:false con orderID = hash solo marca incierta en memoria; si el proceso muere, el reinicio la trata como normal y puede cerrarla con 0 | escribir `incierta_presupuesto` en el ledger en ese camino | ya existía |
| 4 | 640 | bloqueo | caída entre `relleno` y `liquidada` de una incierta: el presupuesto la cuenta llena para siempre (~2,5 USDC bloqueados) y nadie la resuelve | misma regla en presupuesto y resolver: solo `liquidada`/`orden_llena` quitan la incertidumbre | ya existía (gemelo del #8) |
| 7 | 891 | robustez | TERMINAL detectado en el `finally` del mercado: queda en `canceladas` hasta la salida del programa | tras el `finally`, asentar y cerrar las canceladas de los tokens del mercado | nuevo con el #2 |
| 8 | 648 | latente | resolver_inciertas mete en `vivas` órdenes con size=0/precio=0: subestima el saldo reservado y `liquidar` las daría por llenas | guardar size/precio/lado/slug reales de la intención | ya existía (hoy lo tapa el kill) |
| 9 | 375 | limpieza | `excluir_slug` ya siempre es None | quitar el parámetro | nuevo con el #10 |
