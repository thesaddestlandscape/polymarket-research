# Q4 RE-AS-B: fraccion fantasma de los rellenos virtuales <1 s (27-Oct-2026, ~15:10Z)
Codigo, prereg, salidas y hashes: /root/polymarket-research/experimentos/5m_barato/q4_fantasma_27oct/ (PREREG_Q4.md sha 4fdd0436..., ADENDA1_Q4.md sha a8658a1a..., q4.py, q4c.py, q4_salida.txt, q4c_salida.txt, q4_salida_v1_literal.txt, HASHES_Q4.txt). Solo lectura; sin tocar produccion.

## Poblacion
FRENTE-TD primaria (PREREG_FRENTE sha 1528f06b), reproducida con la logica de validador_indep_27oct/ana.py: TODO n=5.086 unidades, 864 cierres, EVw -0,2173 (IC90 cierre -0,261..-0,177) = cifra publicada -0,217. Dias 24, 25, 26-Oct (m5_registro + archivo VOL/m5_onchain; el 26 es lo pedido, 24-25 se anaden porque on-chain existe). 27-Oct NO cubierto: no hay m5_registro_27 (se extrae 03:45Z del 28) ni vidas fr_27; no se ha inventado. El tramo <1 s da aqui EVw -0,0763 (n=1.257, 711 cierres, IC90 -0,147..-0,008), no -0,085 (diferencia de borde de tramo/redondeo; mismo signo).

## Resultados (unidades; entre parentesis por € de coste)
- Cruce on-chain del primer print (token+precio+tamano): <1 s 81 % unico, 15 % ambiguo (>1 tx igual), 1 % sin match, 3 % sin fila t. Regla literal exige >=90 %: NO se cumple.
- Reloj on-chain (ts_chain - t_exch en prints frescos casados, n 300-370 k/dia): p50 2.19-2.22 s, IQR 0,78-0,80 s. A escala <1 s NO discrimina: FC observada 33,1 % vs 34,0 % esperada solo por ruido en unidades sin fantasma de exchange (n=708); FC cota 35,5-41,1 % con ambiguos. FC no aporta informacion.
- Reloj de exchange (FX: t_exch < t0+85 ms): fantasma <1 s = 32,5 % (34,0 % por €); 1-5 s 0,1 % (1/763); 5-20 s 0 %; >=20 s 0 %. Pero es sensible al alineamiento de relojes: el retardo feed (recv - t_exch) es p50 40 ms, p90 91; con margen +100 ms baja a 3,5 % (3,7 % por €), +200 ms 1,3 %, +300 ms 0,7 %. El 65 % del FX_0 esta en dt 85-200 ms (mecanico por el retardo de 40 ms, no prints viejos).
- Union literal (FX o FC) <1 s: 629/1.257 = 50,0 % (51 % por €); parte de FC es ruido. Disputada (bb85>=bp): 26 % en <1 s y 40-42 % en el resto (no distingue tramos).
## EVw (1 obs por mercado-lado, IC90 por cierre) del tramo <1 s
- ANTES -0,0763 (-0,147..-0,008). Sin unidades FX|FC: -0,0785 (-0,180..+0,029; n=628). Sin FX y FC a la vez: -0,0785. Sin FX|FC|disputada: -0,106 (-0,232..+0,011; n=417). Re-simulando sin prints FX|FC (unidad re-asignada): -0,107 (-0,183..-0,026; n=996). Solo los fantasma: -0,074 (n=629). Con FX_100: fantasma -0,116 vs resto -0,079.
- Por dia antes: 24 +0,004 / 25 -0,201 / 26 -0,035; sin los 2 mejores dias -0,201. Subtramos: [85,200) ms -0,101 (n=587), [200,400) +0,038 (n=311, sin IC; exploratorio), [400,1000) -0,158 (n=319).
- Quitar fantasma no cambia el EV (los fantasma no son mas rentables que el resto; en [85,200) quitarlos lo empeora a -0,178). El tramo <1 s sigue negativo (-0,08..-0,11).

## Veredicto
- Literal (PREREG_Q4): NO VALIDABLE (cobertura on-chain 'ok' 81 % < 90 %; el reloj on-chain, IQR 0,78 s, no resuelve el orden a <1 s).
- Lectura sustantiva (Adenda 1, post-hoc declarada): la hipotesis «el -0,085 esta inflado/contaminado por fantasmas» NO se confirma: la fraccion fantasma por reloj de exchange es 3,5 % con 100 ms de margen (32 % solo con margen 0, artefacto de alineamiento), y retirar los fantasmas deja el EVw en -0,08 a -0,11. Consecuencia para Q1: la cifra <1 s es valida como cota (negativa); no hay bolsillo positivo oculto ni optimismo material por prints anteriores. Q1 puede seguir sin esta correccion.
## Limites
Pujas virtuales; t_exch es sello de lote (sesgo 190-470 ms anterior al evento real segun trampas); on-chain da hora de bloque (~2,2 s tras el casado, +/-0,4 s), no hora de casado; no observa identidad de nuestra orden ni reaccion de otros makers; solo 3 dias; el subtramo [200,400) +0,038 no es una candidata (n<400 sin gate). No se ha usado ninguna fuente autenticada ni endpoints de trading.
