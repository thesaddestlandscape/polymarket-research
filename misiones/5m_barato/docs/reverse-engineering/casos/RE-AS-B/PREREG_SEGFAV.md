# PREREG E-RE-AS-B-SEGFAV (27-Oct-2026 ~13:45Z) — cheap5m-reverse-engineer, fase 3 — escrito ANTES de calcular ninguna cifra
Origen (hallazgos 1+2 de RESULTADO_FRENTE_27oct.md, convertidos en señal): el 94 % de los rellenos baratos los provoca un TOMADOR que compra el FAVORITO (tipo B, −0,264 para el que se llena) y la toxicidad crece al acercarse el cierre (240-300 s −0,106; <180 s −0,35). Si ese flujo está informado y el ask del favorito no se ajusta del todo en nuestra latencia, COMPRAR EL FAVORITO tras el print, como tomador, debería dar EV>0, sobre todo con T<180 s.
## Relación con lo ya refutado (no es la misma hipótesis renombrada)
- Palanca 1 (PREREG_PALANCA1, REFUTADA −0,057, OOS −0,072) compraba el complementario tras un BARRIDO L2 de una puja virtual, PRIMER evento por mercado-lado y día → T p50 260 s (casi todo temprano). Diferencias: (a) disparo = print tomador BUY del favorito (no caída del bid en L2); (b) una unidad por Tbucket → mide T<180 s, donde la toxicidad dice que está la información; (c) placebo NO condicionado al futuro (la adenda 2 de palanca 1 mostró que su placebo "mismas unidades" estaba contaminado), estratificado por moneda×Tbucket×ask. Predicción nueva: EVw>0 en T<180 s. Si sale ≤0, (1)+(2) quedan refutados como señal tomadora.
- Trampas aplicables: tras un evento público el ask se mueve en <300 ms (A3, valor tras salto); copiar tarde no captura; un print es un evento público. Se mide al ASK real del libro en td+L por orden de RECEPCIÓN, nunca al precio del print.
## Datos y código
- m5_registro 2026-10-19..26 (/mnt/HC_Volume_106538179/m5_registro/, filas k/q/t; q: bb,ba,bs,as,recv=c[7]; t: p,side,size,recv=c[6]). Desenlace maker_ms_desenlaces_cache.json (missing excluido y contado). DESC = 19..25 (días 24-25 ya usados por palanca 1 para OTRA regla), OOS = 26.
- scripts/segfav_extraer.py y scripts/segfav_eval.py (sha256 en PREREG_SEGFAV.sha256 / HASHES.txt). Prueba de humo: 1,5 M líneas del 26-Oct, solo se miraron conteos y ausencia de errores (no EV).
- Salidas: experimentos/5m_barato/re_as_b_segfav/sf_D.csv.gz; segfav_salida.txt.
## Regla ÚNICA congelada (PRIMARIA)
- Señal: fila t con side=BUY (lado tomador) sobre el token F de un mercado 5min, p∈[0,70;0,90], T=(cierre−recv)/1000 ∈ [20;180). Decisión td = recepción del print.
- Unidad: primer print por (mercado, lado F, Tbucket), Tbuckets [20,60) [60,120) [120,180) (secundarios [180,240) [240,300)).
- Acción: comprar 5 acc de F al ask NIVEL 1 del último q válido (bb<ba) de F con recepción ≤ td+250 ms (resuelto con la primera fila del mercado con recepción > td+250). Ejecutable si as≥5, edad del estado ≤30 s, 0<ask<1. Coste = 5·ask + 5·0,07·ask·(1−ask); pnl = 5·gana − coste.
- Métricas: EVw=Σpnl/Σcoste y EVu; IC90 bootstrap por CIERRE (2000, semilla 2711); por día; DESC/OOS; sin los 2 mejores días; Δ vs placebo estratificado (celdas moneda×Tbucket×ask 0,05, pesos = coste de la señal, bootstrap conjunto por cierre).
- PLACEBO: por (mercado, lado F, Tbucket) la primera fila q de F con ba∈[0,70;0,90] en el Tbucket, sin condicionar a prints; misma ejecución.
## Criterios (fijados antes de calcular)
- PROMISING (candidata a forward, NO validada) si TODO: EVw TODO IC90 inferior >0; DESC >0 y OOS 26 >0; sin 2 mejores días >0; ≥6/8 días >0; Δ vs placebo IC90 inferior >0.
- REFUTED si EVw TODO IC90 superior <0, o (OOS 26 ≤0 y DESC ≤0). En otro caso INCONCLUSO.
- Secundarias informativas (no cambian el veredicto): L=100 (cota inalcanzable) y L=400; cada Tbucket; INVERSA (comprar C tras el print, "el tomador no acierta"); EV del tomador a su precio de print (descriptivo, no ejecutable); movimiento del ask pre→td+250; moneda×Tbucket n≥40 con BH-FDR 10 % (exploratorio, no gate).
- Supuestos explícitos: sin redondeo de CLOB; as≥5 a nivel 1 basta (sin barrer); el orden del fichero ≈ orden de recepción (si una q con recv≤td+L aparece después de la fila que resuelve, se pierde: sesgo pequeño y de signo desconocido).
