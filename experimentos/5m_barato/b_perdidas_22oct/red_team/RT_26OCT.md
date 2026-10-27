# RT 26-Oct — red-team de mitigar_as (F5/A1) y F8 (agente cheap5m-red-team-auditor, transcrito por el chief)
Scripts: scratchpad de sesión rt2-rt5.py (no versionados). Datos: datalogs/mitigar_as_25oct/r_*.pkl, m5_registro_2026-10-15, f8_estructura/tabla.parquet.

## 1. mitigar_as F5 (tamaño en ask propio 100 ms antes del print) → EXPLORATORY (autor: PROMISING)
- Recomputado: +11.445 $, IC90 días (+411,+1.115), inversión −9.701, p 0,0009. Sin look-ahead ni lío de relojes (bid del pickle = registro 98,4 %).
- Controles: moneda×hora +9.690; moneda×hora×q +8.955; decil F2×moneda×hora +5.254 (p 0,0076, NO pasa Bonferroni 0,00625; 11/15 días; sin 2 mejores +2.948); sin 3 mejores días +6.260.
- Por moneda: ETH +11.304; SOL +2.081; XRP +234 (cruza 0). Primeros prints de ráfaga +10.029; no primeros +989 (cruza 0).
- Rellenos bajo el mejor bid (los de B): +2.639, IC90 cruza 0, 8/15 días, sin 3 mejores −26.
- τ=250 ms: +2.255 (cruza 0). K real ≥25-30.
- Unidad = print de toda la población de makers (99 % del exceso en ETH), no € de B. €/año validado: 0.
- Reparación: forward pasivo ≥10 días nuevos (≥24-Oct) con base F2×moneda×hora + réplica BTC/DOGE/BNB + prueba al nivel real de B.

## 2. F8 → REJECTED como ganancia (solo pérdida evitada)
- Regla trivial «armar con más T restante» +2.952 (9/9 días) vs modelo P0 +2.909 (mismas 88.572 vidas); placebo +1.
- Vidas retenidas −0,101 €/€; contribución negativa en todos los buckets de b (−0,335..−0,131). La mejor política es no armar.
- Etiqueta virtual rellena 52,8 % vs 5,1 % real de B → no se transfiere. (La calibración está en curso.)
