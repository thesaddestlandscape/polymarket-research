# ADENDA 1 a PREREG.md (sha 658e2719…) — 25-Oct ~11:40Z, ANTES de cargar HOLD (12-21)
Motivo: la corrida de depuración (PRUEBA=1, solo días DESC 06-09) mostró que el CONTROL «flujo neto de TODAS las tomadoras contra s en [tf−33, tf−3]» separaba
mucho (08-09: EV bandera +0,149 vs no bandera −0,111, 86 % del €). Visto en DESC ⇒ es descubrimiento; se promueve a contraste confirmatorio:
- H4: regla «mantener la puja solo si F_all > 0; cancelar si F_all ≤ 0». Métrica primaria = EV€(F_all>0) − EV€(todo P) en HOLD 12-21, con los mismos criterios de H1
  (n≥40 unidades, ≥10 días, IC90 días y cierre >0, sin 2 mejores días >0, BTC y ALT mismo signo). Además desagregar F_all<0 / =0 (sin operaciones) / >0.
  Placebo: permutar el signo de F_all dentro de (día × moneda) 200 veces. Precedente: detector_ex_ante M3 (flujo/identidad, alts 0,10-0,30, primeras 5 acc) AUC 0,511 ⇒ prior bajo.
- K confirmatorio = 4 ⇒ α = 0,0125. Fuente en tiempo real requerida: dirección del tomador por WS CLOB (last_trade_price side) — inferido, por verificar.
