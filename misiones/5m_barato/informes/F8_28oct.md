# F8 (estructura) con etiqueta calibrada, 28-Oct. Veredicto: REJECTED como fuente de EV>0 (y NO VALIDABLE en la parte «calibrada»). Beneficio validado: 0 EUR.
Código: experimentos/5m_barato/f8_28oct/contrib_f8.py (+contrib_f8.json). Solo lectura, sin tocar data/ ni producción. EXPLORATORY.

## Hechos
- No existe etiqueta calibrada para POBLACIONES: la calibración (calibracion_etiqueta/INFORME.md, v2) dio CALIBRADA=False (P_puja 27 % vs 50 % real; la generativa no calibra, solo las ventanas reales de B). Las ventanas reales solo existen para las 364 pujas de B (20-23 Oct, 4 días): sin potencia (rellenos en flag 43-45 vs fuera 136-138). Por tanto «F8 con ventanas reales sobre 22 días» no es construible.
- Datos F8 disponibles: 05-24 Oct (20 días, 387.073 vidas; evaluación walk-forward 08-24). 25-26 Oct NO procesados (requiere regenerar vpv+on-chain, ~25 min de carga con MemAvailable 1,8 GB < 2,5 GB: no ejecutado). Son 17 días de evaluación, no 22.
- Re-medido previo con etiqueta variante-0 (la mejor de TUNE) reentrenando: contribución retenida por EUR GATE 16-24 −0,026/−0,024/−0,002 (todas −0,123); LIMPIO 22-24 +0,001/+0,013/+0,025 (3 días).
- Nuevo (contrib_f8.py): políticas F8 congeladas (P0/P1/P2, retiene 30 % del EUR, ETH/SOL/XRP) evaluadas por EV ponderado por EUR (Σy/Σc). Etiqueta pesimista (ORIG), 08-24, 17 días: P0 −0,103 (IC90 días −0,120/−0,083; sin 2 mejores −0,115; 1/17 días +), P1 −0,084 (−0,096/−0,071), P2 −0,087; todas −0,192; placebo −0,19, inversión −0,32..−0,34. Pierde menos, nunca gana. Con etiqueta variante-0 (optimista): P0 −0,125, P1 −0,109, P2 −0,096 frente a todas −0,099, placebo p=0,66-0,99, inversión ≈ −0,00..−0,04: la política NO supera al placebo ni a «todas» (la ventaja de ORIG depende de la etiqueta que premia «rellenarse menos»).
- IC90 por días > 0: en ningún caso (techo superior −0,07).

## Límites
Etiqueta virtual no calibrada para poblaciones; transferencia política-pesimista→etiqueta-optimista (no reentrenada) es un contraste, no el reentrenado de B1; 3 días limpios 22-24 con n=3.

## Siguiente paso / qué reabriría
Ninguna inversión adicional en F8. Reabrir solo con ≥750 pujas tipo B reales nuevas (PREREG_TRANSFERENCIA, requiere micro-órdenes con OK Javi) y contribución retenida >0 con IC90 por días >0.
