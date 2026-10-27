# PREREG BR2 — TECHO DE LA COLA: ¿los rellenos de COLA (C3) del maker largo barato ganan fuera de muestra en BTC o en el agregado? (5m, 6 monedas, banda 0,05-0,30)
Congelado 26-Oct-2026 (polymarket-quantum-alpha-miner, programa BANDA-0-0,30). Escrito ANTES de calcular clases C1/C2/C3 fuera de ETH/SOL/XRP 17..22-Oct (ya visto, `b_perdidas_22oct/cola_vs_cruce/AVANCE.md`) y antes de ningún día fresco (≥27-Oct). Cambios posteriores = BR2b; aclaraciones en ADENDA con sha.

## 1. Decisión que se evalúa
Si el diseño «maker sentado en cola en el mejor bid del lado barato que cancela antes de que se siga casando por debajo» puede heredar EV positivo. El TECHO de cualquier política de cola/cancelación es el EV de los rellenos C3 (los NO seguidos de casación por debajo). Si EV(C3) ≤ 0, ninguna cola ni cancelación salva al maker largo barato en esa celda; si EV(C3) ≥ +0,04, el arnés debe medir qué fracción de C3 se retiene cancelando a 60-65 ms y con qué cuota.

## 2. Mecanismo, pagador y predicción diferencial
Pagador del maker en cola: tomadores del lado caro (compran el favorito y consumen la cola del barato al precio) + rebate. Lo que lo mata: que se siga casando por debajo en los ~2 s siguientes (C2; población ALT3 17-22: −0,110, IC90 días −0,199..−0,014). Predicción frente a H0 (C3 ≈ población ≈ 0, como en ALT3 17-22: +0,003): EV(C3) > 0 y EV(C3) − EV(C2) > 0 en días frescos, sobre todo en BTC (88 % del flujo maker de la banda).
No es la identidad rellenas − no rellenas: aquí no se compara contra pujas no rellenadas ni se presenta ninguna diferencia como premio de un filtro ex ante; es la cota superior de lo que una cancelación perfecta podría retener. No es rebautizo de «maker de un solo lado» ni de B (B puja 1-2c bajo el bid: mezcla C1 27 % / C2 36 % / C3 37 %): se aísla la clase alcanzable por diseño.

## 3. Datos y definiciones
Exactamente las de P1 de `cola_vs_cruce` (prereg `prereg/PREREG_P1_CLASIFICACION.md`, sha 0552983b…; `scripts/p1_pop.py` y `p1_ev.py` importados SIN cambios de lógica: solo lista de días y de monedas; diff y sha en el informe): cada relleno maker = largo en el lado comprado c a pc. C1 = la misma tx rellena a otro maker más hondo; C2 = no C1 y en una tx posterior del mismo bloque o del siguiente se rellena a alguien más hondo; C3 = ni C1 ni C2. Rellenos de `m5_onchain_D`, mapa tokmap ∪ filas k (nunca `mapa_escala/tokens.json`), compra equivalente, pc ∈ [0,05; 0,30), T ∈ (60; 300] s, unidad mercado-lado-clase, desenlace OFICIAL con cobertura ≥99 % del € por moneda × día (si no, se excluye y se declara), EV ponderado por € (Σpnl/Σcoste) y por unidad, rebate aparte (no entra en el gate). Fuera los rellenos de la dedicada. El último bloque de cada día necesita el fichero del día siguiente; si falta, esos rellenos son missing (no C3).

## 4. Periodos
VISTO: ETH/SOL/XRP 17..22-Oct. DESC 05..25-Oct las 6 monedas (descriptivo, no decide; se publica ANTES de la primera mirada fresca). FRESCO = días UTC completos ≥27-Oct: DECIDE. Miradas a 10, 20 y 30 días frescos (≈06-Nov, 16-Nov, 26-Nov).

## 5. Gate (FRESCO, en cada mirada)
Celdas decisivas (K=2): A = ALL [0,05; 0,30); B = BTC [0,10; 0,30).
PASA (techo abierto) si TODO: ≥10 días frescos; en A y en B, EV(C3) ≥ +0,04 con IC90 bootstrap por DÍA (2.000, semilla 20261026) inferior > 0 y test de signo por días (permutación de signo del EV diario ponderado, 10.000) p < 0,01; EV(C3) − EV(C2) con IC90 por días inferior > 0 en A; EV(C3) sin los 2 mejores días > 0 en A y en B; EV(C3) > 0 (punto) en ≥4 de las monedas con ≥200 unidades C3; IC por cierre reportado (racimos).
REFUTADA (techo cerrado) si en A y en B el IC90 por días superior de EV(C3) < +0,02 (en cualquier mirada ≥10 días). INSUFICIENTE en otro caso (se dice qué falla y la fecha de la siguiente mirada).
Descriptivos (no deciden): por sub-banda (0,05-0,10/0,10-0,20/0,20-0,30) y 0,01-0,05; por moneda; T (60,150] vs (150,300]; tamaño del relleno (≤5, 5-25, >25 acc); con rebate; por clase ON/MEDIO/OFF de BR1; cuota de cada clase en el €; perfil por día.

## 6. Salvaguardas
IC por día y por cierre; EV ponderado por €; sin 2 mejores días; cobertura declarada; nada de reloj WS (definición solo on-chain); el resultado NO autoriza dinero ni cambia B: si PASA, el siguiente paso es el arnés (cancelación 60-65 ms sobre libro5 con anclas de B) y luego micro-real solo con /code-review + OK de Javi.

## 7. Ya visto (declarado)
ALT3 17..22-Oct por clase (C3 +0,003; C1 +0,011; C2 −0,110; COLA−CRUCE +0,067, IC90 días −0,003..+0,117); B por clase (C3 +0,097 n=95; C1 −0,033; C2 −0,349); EV poblacional por banda × moneda 06..21-Oct. Nada de BTC/DOGE/BNB por clase. Ningún dato ≥27-Oct.

## 8. Recursos y entregable
Trabajo pesado (BTC ≈ 3/4 de las filas): uno a la vez, por día con checkpoint, `nice -n 19 ionice -c3`, `ulimit -v 3000000`, nunca 06:00-09:30Z ni con load5>4. Código en `experimentos/5m_barato/banda_0_30/br2/`. Entregable: `alpha_miner/banda_0_30/RESULTADO_BR2.md`.
