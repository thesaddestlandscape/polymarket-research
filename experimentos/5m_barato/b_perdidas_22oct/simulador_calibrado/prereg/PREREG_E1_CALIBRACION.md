# PREREG E1 — calibración del simulador maker fiel a B (B_FIEL, e1q_sim.py) contra anclas on-chain. 23-Oct-2026 ~06:05Z
Congelado ANTES de ejecutar nada de este directorio. Visto antes (declarado, no es ciego): AVANCE cola_vs_cruce (B_FIEL: tasa 0,58 vs 0,61 en 239
pujas, acuerdo 0,74; EV B_FIEL ELEGIR -0,171 / MEDIR +0,115) y INFORME cola_posicion (B on-chain EV -0,050 n=175; wallets 0xf074 y 0x0ab01745).
Solo se tocó un recuento de unidades por wallet (0xf074: 398 unidades ETH en banda, 0x0ab0: 510; solo ETH) para saber qué datos hay.

## Universo y definiciones
- Pujas reales de B = `puja_fin` del ledger H47-B (20-22 Oct, real=true) con mercado en el mapa de tokens (act, fin) y lado == lado simulado (el sim elige el 1.er lado
  cuyo top bid entra en banda). Se reporta el % de pujas cuyo lado no coincide (criterio B0).
- Relleno real = (a) `rellenos` no vacío en `puja_fin` O (b) fila on-chain de B en (mercado, lado) (b_clase.csv es_b=1) O (c) `relleno_tardio` del ledger. Se reporta (a) solo y la unión.
- Simulador bajo prueba: `e1q_sim.py` (importado SIN modificar, hash del prereg P2 respetado), variante B_FIEL = (settle 0, repost 1500, lat_can 280, lat_post 85, alloc prop).
  Se pasa por MEDIR (20-22 Oct, libro5 en `/root/polymarket-research-datalogs/cola_vs_cruce`).
- Edad al relleno: real = `vida_ms` de cola_posicion/datos/b_cola.csv (print que rellena − llegada de la orden en L2, hora de RECEPCIÓN; faltan los «sin print»);
  sim = r_relleno − t_vivo de la orden que rellena (t_vivo = envío + 85 ms).
- EV = Σpnl/Σcoste ponderado por € (no por unidad). Real: pnl/coste de b_clase.csv; sim: acc·gana − acc·p (maker sin comisión, igual que el real).
## Partición para calibrar (anti-sobreajuste)
TUNE = pujas del 20-Oct. EVAL = pujas del 21 y 22-Oct. Rejilla ÚNICA y cerrada de parámetros del simulador, elegida en TUNE por máx. kappa de relleno puja a puja
(desempate: menor |Δtasa|): lat_can ∈ {65, 150, 280, 450} ms × alloc ∈ {prop, lo, hi} (12 celdas; repost 1500 y settle 0 fijos = código real de B). Nada más se toca.
Se evalúa en EVAL con la celda elegida Y con B_FIEL nominal (280/prop). El veredicto se da sobre EVAL.
## Criterios de fidelidad (todos sobre EVAL; B_FIEL elegido)
B0 lado: coincidencia de lado sim vs real >= 0,90 de las pujas con mercado en el sim.
B1 tasa de relleno: |tasa_sim − tasa_real| <= 0,05 (mismas pujas).
B2 acuerdo puja a puja: exactitud >= 0,80 Y kappa de Cohen >= 0,60 Y recall P(sim relleno | real relleno) >= 0,75 Y precisión P(real relleno | sim relleno) >= 0,75.
B3 edad al relleno: KS D (sim vs real, rellenos de las mismas pujas) <= 0,15 Y |Δ mediana| <= 0,5 s; en pares con relleno en ambos, |t_sim − t_real| <= 1,0 s en >= 70 %.
B4 EV: |EV_sim − EV_real| <= 0,10 (€/€, mismas pujas) Y cuotas de coste por clase (sim X1/X2/X3 vs on-chain C1/C2/C3) cada una a <= 0,10 (abs). Se reporta además el desglose
   EV(ambos), EV(solo sim), EV(solo real) (¿los rellenos que el sim inventa/pierde son adversos o neutros?).
Anclas de wallets (solo ETH; 17-22 Oct; unidades en banda (0,10-0,30]; fuente up_*.csv.gz, oc_*.csv.gz, libro L2 `mk`):
W1 relleno explicado por el replay del libro: fracción de rellenos de cada wallet con un print normalizado en el mismo nivel (±0,005) en [ts_chain−6 s, ts_chain+1 s] (reloj on-chain +2,4±1,5 s)
   >= 0,75 para cada wallet y a <= 0,10 de la fracción de B calculada igual.
W2 volumen: en mercados ETH/SOL/XRP comunes, Σ acciones de prints L2 en banda vs Σ acciones de rellenos maker on-chain (todos los makers, mismo lado/banda), razón agregada en [0,85, 1,15]
   Y Spearman por mercado >= 0,70.
W3 (descriptivo, SIN criterio): mezcla C1/C2/C3, EV, hit, precio y T de las wallets frente a B real y al sim; su política es desconocida, no se puede replicar puja a puja.
## Regla de veredicto (sobre EVAL)
REPRODUCE solo si pasan B0, B1, B2, B3, B4, W1 y W2. REPRODUCE_PARCIAL (agregados B1+B4 pasan pero fallan B2/B3/W): se trata como NO_REPRODUCE para evaluar palancas marginales
(un efecto de ±0,05-0,10 €/€ exige acierto puja a puja, no solo agregados). Cualquier otro caso: NO_REPRODUCE. Intervalos: bootstrap por mercado (y por día si procede), 2.000 réplicas, semilla 20261023.
## Límites previstos
n pujas por día ~80-100 (EVAL ~160-180): potencia baja para B4 (IC EV real ±0,2). No hay política conocida de las wallets: W solo valida el replay del libro, no la política.
