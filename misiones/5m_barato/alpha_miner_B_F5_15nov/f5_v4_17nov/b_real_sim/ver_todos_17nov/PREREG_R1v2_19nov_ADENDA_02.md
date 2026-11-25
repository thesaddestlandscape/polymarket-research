# PREREG R1v2 — ADENDA 02 (19-Nov ~10:20Z, chief). Antes de ver ningún dato de V5.
Base: PREREG_R1v2_19nov.md (48fe638e…) + ADENDA_01 (efd19654…). No se editan.

## Motivo (detectado por Javi)
La variante V5 de ADENDA_01 («cancelar ante movimiento adverso de Binance, 3 bps / 3000 ms») DUPLICA una regla ya
preregistrada en la familia Q11: **CXJ150** (docs/reverse-engineering/casos/RE-THRU1/PREREG_Q11_THRU1_FWD.md,
sha 68ca25a0…, línea 14): G0 que (i) no arma si hubo salto adverso de Binance ≥3 bps en 1 s en (t−3300, t−300] y
(ii) da por cancelada la orden viva para todo relleno con t ≥ salto + 150 ms; salto = definición de passT.py
(bnr(coin, t, 1000), hora = RECEPCIÓN del tick; adverso = contra el lado de la puja). Emparentadas: H-DB1/DB1_150
(PREREG_DB1.md), H-DB3, CXB_l. No se inventan umbrales nuevos.

## Cambio
1. V5 := **CXJ150 aplicada sobre la política REAL de B** (DEEP_PEG top−k con repegado, F5_t al colocar), motor
   passT_v4, latencia L_cancel de paquete_l 13-Nov (la «+150 ms» de CXJ150 se mantiene como primaria; 74/111 ms
   como sensibilidad). Se anulan X=3 bps / W=3000 ms de ADENDA_01 §1.
2. Antecedente declarado, sin valor confirmatorio: CXJ150 se eligió post hoc entre 12 variantes sobre G0 en días
   quemados (dPnL +128 sobre G0 26-Oct..04-Nov) con sello anterior a passT_v4 → «no validado» por la regla de
   sello vigente; por eso aquí cuenta como variante de la familia con max-statistic, no como dato previo.
3. Cortafuegos CXB: medir V5 en R1v2 no cambia ningún parámetro de CXB60 ni de Q11 (R-CXB-1..6).
4. El exploratorio de ADENDA_01 §2 sobre los 202 rellenos usa la definición CXJ150 (salto ≥3 bps en 1 s, recepción).
5. Rebate 0 primario (ADENDA_01 §3) se mantiene. Familia = 5 variantes, max-statistic. Nada más cambia.
