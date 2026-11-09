---
name: project_predictor_as_b_28oct
description: 28-Oct-2026 predictor ex-ante de la selección adversa de B (palancas 1 y 3). El nivel/ask SÍ se predice (AUC 0,71-0,75) pero P(gana|relleno) NO (dAUC +0,007) -> REJECTED; techo oráculo ≈0
metadata:
  type: project
---
Resultado (informe misiones/5m_barato/informes/PREDICTOR_AS_B_28oct.md; código y datos en experimentos/5m_barato/predictor_as_b_28oct/, HASHES.txt). Evaluado con 7 días IS (05-10 y 13 Oct; 9.415 rellenos de P) y OOS 23-26 Oct (5.711), NO los 22 días (tope de llamadas); extracción de los demás días en curso con run_pred2.sh.
- HOLD OOS −0,0318 = R1 del alpha miner (valida el pipeline). Techo oráculo (quitar rellenos con barrido, 80-83 % de los rellenos): IS +0,051 / OOS −0,052, IC90 cruzan 0 -> previsión perfecta del barrido ≈0±0,1.
- AUC(gana|relleno) 0,551 vs base estática 0,544: dAUC +0,007 (IC90 −0,005/+0,018) a 100 ms; ninguna familia (L1 propio, espejo, prints, Binance) supera la base. Cancelar/no pujar: retenidos OOS −0,011..−0,029 (pesimista −0,057..−0,075), placebo p≥0,056. Complementario tomador tras marcar: −0,021..−0,048 vs −0,050 incondicional.
- El cuándo SÍ se predice: barrido adverso en (100,2100] ms AUC 0,713 vs 0,676 estática; ask comp +2c en 250 ms AUC 0,753 vs 0,595; AUC 0,67-0,74 para leads 100-3000 ms.
**Why:** el barrido (print a través del nivel) es el caso normal; su timing sale del estado, pero la pérdida depende de información no observable en nivel-1/prints/Binance (E-TD ya está dentro de P).
**How to apply:** no reabrir B como "maker + predictor de cancelación" con estos datos; solo con información nueva (libro 15m alineado, L2 profundo, identidad del tomador) y criterio dAUC(gana|relleno) ≥ +0,03 IC90>0 a L ≥ 100 ms + EVw pesimista >0. Ver [[reference_traps_predictor_harness_28oct]].
