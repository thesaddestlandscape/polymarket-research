# Enmienda banda lo (D1, abierta por abajo) — registro de decisiones, 26-Nov-2026
Fuente para el prereg/firma de la enmienda. Ficheros: dev-bk `experimentos/5m_barato/b_k_ejecutor/enmienda_lo/` (p3_p5_real.json, p2_no_danar.json, regla_par/). PREREG_SIML (firmado 11:08Z) NO se edita: esta nota es su anexo de desviaciones.

## Resultados
- P3 (13-14 Nov, 12 moneda-días): v3.4-D1 PASA 12/12 (100 %). **Desviación declarada:** v3.4b FALLA la letra en 8/12 (94,9-99,4 %), todos lo→mixta por la regla del par. La resolución «P3 se juzga sobre D1; el par es un subconjunto fail-closed» se tomó DESPUÉS de ver el resultado (apoyada en CONTRATO_D3_SIML_P1_25nov §7: «v3.3 evalúa lo sin la regla; el vivo opera un subconjunto; declararlo»). Nunca citar «v3.4b PASA P3».
- P5 PASA (cobertura 100 % con 0/−1/−2/−3 ms; escalón +20 ms ≤1 ventana). Estrato-lo definido por el agente: p5∈[5,28] ms y n≥100. Detector ≤2 s, deriva +1 ms/h y oscilación lo/hi: solo sintético → con datos reales en P4(iii).
- P2 INSUFFICIENT (58/59 pujas nuevas < 200); todas las métricas dentro de la banda placebo.

## Regla del par v3.4b: MANTENER (alpha-miner + red-team «sostenible: sí», 26-Nov)
- Coste. **Denominador citado:** ventanas 5m de frontera ETH+SOL+XRP 13-25 Nov: 11.142 → 11.086 (−0,50 %); 18-25 Nov −0,03 %; 21-25 Nov 0. (CONTRATO §7 usa 322.532 ventanas: −0,56 %). Ambos ≤1 % (§7(j)). P2: −20 pujas (1,0 %), 0 rellenos.
- Beneficio: solo indicio (4/56 = 7,1 % vs 31/11.086 = 0,28 % con hi dentro de [w0,w0+5 min); ~2 episodios, 15-16 Nov). Sin look-ahead (bandera ≤B−1, resultado [B,B+30)).
- **No válida para BTC sin reevaluar:** BTC tiene 5-17 pares hi/día aislados (17-25 Nov) y la regla le costaría 3,62 % (incumple §7(j)). Hoy BTC está fuera de alcance; si entra, se reabre.
- Pendiente BLOQUEANTE para cualquier afirmación de protección intraventana (31/35 hi-dentro sin bandera) y NO bloqueante para la regla del par: DetectorRapidoLive (experimento_maker_bk.py:551, hoy solo log). Se mide con datos reales en P4(iii).

## Pruebas que retiran o mantienen la regla (fijadas ANTES de mirar)
- (a) RTT durante pares hi (P1a: ping WS + TCP a clob) vs ±5 min. n mínimo: ≥10 episodios en ≥2 días. Si |Δp50| ≤3 ms en ≥80 % → artefacto: v3.5 sin el par (re-firma). Si Δp50 ≥ +10 ms en ≥50 % → retraso real: se mantiene. Otro caso o n insuficiente → se mantiene. Disparador: veredicto de P1a (≥29-Nov) y cada mirada; recuento con `regla_par/par_coste.py`.
- (b) Si vuelven los episodios (>1 % de ventanas lo perdidas durante ≥2 días): SIM-L marcadas vs no marcadas, P(relleno) y markout|relleno, placebo = marca desplazada dentro de moneda-día (≥1.000), ≥200 pujas marcadas. Se relaja solo si las marcadas no salen peor que la banda 90 % del placebo. Disparador: el mismo recuento diario de (a).
