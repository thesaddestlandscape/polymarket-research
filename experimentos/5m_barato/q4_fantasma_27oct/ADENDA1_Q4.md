# ADENDA 1 a PREREG_Q4 (27-Oct ~15:05Z), escrita DESPUES de ver la salida v1 (q4_salida_v1_literal.txt) y ANTES de calcular lo de abajo. Declarada post-hoc.
Lo visto en v1 (regla literal): cobertura on-chain del primer print en <1 s = 81 % 'ok' + 15 % 'ambiguo' (mismo token/tamano/precio con >1 tx en la ventana); IQR reloj on-chain 782-799 ms (<=1500: FC informativa). Con la regla literal (cobertura 'ok' <90 %) el veredicto formal seria NO VALIDABLE.
Se anade, solo informativo (no cambia el veredicto literal salvo que se diga):
 (a) Ambiguos: cotas NO circulares: FC_cota_sup = algun candidato da casado_est < t0+85; FC_cota_inf = todos los candidatos; FC_resuelta = candidato mas cercano a t_exch+OFF (circular: sesga a 'no fantasma'; solo como referencia).
 (b) Calibracion nula de FC: con el ECDF empirico del ruido (ts_chain - t_exch - OFF, prints frescos casados, el mismo dia), tasa esperada de FC en unidades con t_exch >= t0+85 (no fantasma por reloj de exchange) = media de ECDF(t0+85-t_exch); comparar con la observada. Si coinciden, FC no aporta mas que ruido de reloj.
 (c) Sensibilidad de FX al sesgo de sello de lote (el sello de exchange puede ser 190-470 ms ANTERIOR al evento real): FX_d = t_exch + d < t0+85 con d en {0,100,200,300,500} ms. Fantasma "robusto" = FX_300.
 (d) Subtramos de <1 s: [85,200), [200,400), [400,1000) ms: fraccion FX_d y EVw.
 (e) delay recv - t_exch de los primeros prints (p50/p90/p99).
Veredicto final: se emite el literal Y, aparte, la lectura con (a)-(d). Nada de esto se usa para retocar la regla primaria.
