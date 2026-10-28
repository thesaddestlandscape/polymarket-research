# FORMULA_R1_B (28-Oct-2026) — fórmula de reserva para VENDER / CANCELAR en B (5m, 6 monedas). VEREDICTO: REJECTED (beneficio validado 0 €)
Agente: polymarket-quantum-alpha-miner (1 agente, 20 llamadas). Sin órdenes, sin tocar data/live ni producción. Artefactos: `experimentos/5m_barato/formula_r1_28oct/` (PREREG_FORMULA_R1.md sha256 116f5c420d702fb875b2241e12c00a85e3632f84c98c45fde5c38861380fe086, escrito y hasheado 08:55Z ANTES de extraer; ADENDA1 10c4eabc…; ADENDA2 faae031c…; extract.py v2 6f4896d0…; analysis.py 2e51110d…; HASHES.txt 09:33:52Z, antes de analizar; salida íntegra `analysis_salida.txt`, 145 líneas).

## 1. Resumen
- Población = la de ESCALERA_PATAS_B: 26.802 patas P (1 por mercado+lado; IS 05-22 Oct = 21.875 en 18 días; OOS 23-26 = 4.927 en 4 días), 319.316 estados (pata × instante). HOLD EVw IS +0,0003, OOS −0,0329 (idéntico al de la escalera: comprobado). Coste desplegado 1.386 €/día IS, 1.424 €/día OOS.
- Ninguna regla de la familia (18 variantes de VENDER, 6 de CANCELAR) bate a mantener: VENDER elegida en IS (clase L, κ=0,05 = la menos agresiva) Δ OOS −0,0046 por € (IC90 por días −0,0083/+0,0012; sin los 2 mejores días −0,0082; 40 ventas de 4.927), −2.367 €/año a volumen simulado; placebo p=0,71. CANCELAR: retenidas EVw OOS −0,0359 (IC90 −0,168/+0,100) frente a HOLD −0,0329; placebo p=0,71. Criterios CANDIDATE: 0 cumplidos.
- Causa medida: tras el relleno el mid está calibrado (win − mid = +0,09 pp IS en t1+250 ms; |win−mid| ≤0,4 pp en todos los instantes IS) y la información añadida (15m, desequilibrio L1, Binance) mueve q̂ ≈1 pp rms, frente a un coste de salir de 1,6-3,1 pp por acción. La selección adversa del relleno se realiza ANTES del relleno (win − mid = −2,0 pp a t1−250 ms, −0,8 pp a t1−100 ms; OOS −3,0/−1,9 pp): el relleno es el final del movimiento.
- Cota teórica (sec. 2.2): para ganar +38 % del coste (548 €/día con este volumen) con una salida, el desplazamiento rms de q̂ frente al mid tendría que ser ≈25 pp (hoy ≈1,3 pp). Evidencia estructural de imposibilidad para la SALIDA con nivel-1 + 15m + Binance; no cierra la entrada (sec. 7).

## 2. Derivación
Notación: token propio A, X∈{0,1} su desenlace, F_t la información nuestra, q_t=P(X=1|F_t), m_t mid, b_t bid, f(p)=0,07·p(1−p) comisión tomadora, ρ(p)=0,2·f(p) rebate maker, sh acciones, p0 precio de relleno, τ=T−t.
### 2.1 Parada óptima del tenedor
Instantes de decisión k. Vender como tomador paga S_k=b_k−f(b_k) (ejecución a t_d+250 ms, lote entero, bid con edad ≤2 s, tamaño ≥sh, sh·b≥1 $). V_k=max{S_k, E[V_{k+1}|F_k]}, V_final=X. Como siempre se puede mantener, E[V_{k+1}|F_k]=q_k+O_k con O_k≥0 (valor de opción de vender después). Región de venta: S_k−q_k ≥ O_k (+γ, ver 2.4). Descomposición: S_k−q_k = −h_k − ε_k, con h_k=(m_k−b_k)+f(b_k) el coste de salir (semiespread+comisión) y ε_k=q_k−m_k la información que tenemos y el mercado no.
### 2.2 Cota de valor de la información (la «fórmula» de límite)
Δ(regla)=E[Σ 1{venta en k}(S_k−X)] = E[Σ 1{venta en k}(S_k−q_k)] ≤ E[(−ε−h)^+] por instante. Con ε~N(0,σ²): G(σ,h)=σ·φ(h/σ)−h·(1−Φ(h/σ)) por acción. Medido: h≈2,2 pp, σ≈1,3 pp (de ΔLL≈5·10⁻⁴ nats/fila: σ=√(2·ΔLL·q(1−q))) ⇒ G=0,024 pp/acción = 0,1 % del coste por instante (×1,5-2 con 10 instantes). Con σ=2,6 pp: 1,3 %. Para G=38 % del coste (8,7 pp/acción a p≈0,23) hace falta σ≈25 pp (ΔLL≈0,03 nats/fila, 60 veces lo medido). Una salida sobre un precio que es martingala solo crea valor si se sabe más que el mid en más que el coste de salir.
### 2.3 Coste de selección adversa del relleno
La pata existe porque hubo relleno (evento Φ). EV de la unidad = (m_pre − p0) − AS + ρ, con AS = m_pre − E[X|Φ]. q̂ se calibra SOBRE las patas rellenadas, así que la AS entra como término a0 (log-odds) y como pendiente del precio. Medido: AS(t1−250 ms)=2,0 pp IS/3,0 pp OOS; AS(t1−100 ms)=0,8/1,9 pp; AS(t1+250 ms)=−0,1/+0,9 pp: el relleno es el final de un movimiento de ~1,2 pp en 150 ms y después el mid está en p0.
### 2.4 Inventario (Avellaneda-Stoikov binario)
A-S continuo: r=s−qγσ²(T−t). En una binaria la varianza restante del pago dado m es m(1−m), independiente de τ (el mid converge a 0/1; el ritmo de varianza φ(Φ⁻¹(m))²/τ diverge al cierre). Reserva: R=m−γ·n·m(1−m)−AS+ρ. Con objetivo EV (el de todos los gates) γ=0; γ>0 solo aparece con crecimiento logarítmico (≈½·(n/W)²·m(1−m)); no es calibrable por EV.
### 2.5 Precio de cotización
Con λ(δ)=A·e^{−kδ} (δ=m−x) y AS(δ), maximizar λ(δ)·(q̂−x−AS(δ)+ρ) da x*=R_in−1/k_eff si el máximo es interior; si AS(δ)≥δ+ρ para todo δ (medido: 2,0 pp frente a semiespread 0,5-1,0 + ρ 0,25) la solución es de esquina («no cotizar»). Falta la curva AS(δ) por profundidad en el rango 0,10-0,30 (solo medimos x=bb+0,01 fijo): es la ronda 2.
### 2.6 Fórmula calibrable (≤5 parámetros por clase; pendiente fijada a 1; γ=0)
q̂=σ( logit m_A + a0 + a2·ΔC + a3·ΔQ + a4·zB ).
- ΔC=logit Φ(w)−logit m_A, w=[√(T15−t)·Φ⁻¹(m15(t)) − 1{j≥2}·√(T15−t0)·Φ⁻¹(m15(t0))]/√(T5−t): FV del 5m implicado por el 15m del mismo lado (j=subventana 1-3; σ se cancela; m15 de m15_registro, edad ≤15 s / ≤30 s).
- ΔQ=(bs−as)/(bs+as) nivel 1 (profundidad/cola visible). zB=±ln(S/refB)/(σ60·√max(τ−12,3)) (Binance, reloj de recepción; refB=media [t0−62 s,t0−3 s]).
- Paridad ΔP (token complementario): DEGENERADA (libros YES/NO espejo; |ΔP|>0,02 en 0,01 % de filas) → sustituida por ΔQ en la ADENDA1 antes de ver datos reales.
- VENDER ⇔ S−q̂ ≥ κ (κ∈{0;0,005;0,01;0,02;0,03;0,05}) en clases E (t1+0,25/2/10/30 s) y/o L (T−90/−60/−45/−30/−20/−10 s). CANCELAR ⇔ q̂_N+ρ(p0)−p0 < κ_in (estado a t1−100 ms; t1−250 ms sensibilidad).

## 3. Diseño pre-registrado y desviaciones
Rejilla y criterios en PREREG (18 variantes VENDER, 6 CANCELAR, max-statistic por bootstrap de días estudentizado, placebo = covariables permutadas dentro de moneda×clase×decil de m_A, 200 permutaciones; inversión = q̂=σ(logit m − términos); IS con q̂ leave-one-day-out; OOS con ajuste en todo IS, mirado una vez). Adendas (antes de analizar): ΔP→ΔQ; criterio CANCELAR exige además EVw de retenidas >0 con IC90 por días >0 (Δ_total premia cancelar si HOLD<0); extractor v2 por MemoryError de v1 (regresión v1=v2: 0 valores distintos en 3.478 filas comunes); mawk idéntico a gawk (md5). Desviación declarada: extracción 09:10-09:33Z dentro de la ventana 06:00-09:30Z, nice 19/ionice idle, load1 hasta ~11 (el load5<7 se disparaba por mis propios procesos), MemAvailable ≥1,7 GB.

## 4. Resultados (EVw=Σpnl/Σcoste; Δ=(Σpnl_regla−Σpnl_HOLD)/Σcoste; IC90 por días; 4 días OOS ⇒ IC anchos)
### 4.1 Calibración (ajuste en IS; SE de modelo, anticonservador) — n filas: N 21.875, E 86.671, L 44.976
- N: a0 −0,037(0,024) a2 +0,020(0,026) a3 +0,099(0,030) a4 +0,006(0,021). E: a0 −0,001(0,012) a2 +0,026(0,013) a3 +0,085(0,014) a4 −0,004(0,011). L: a0 +0,015(0,015) a2 +0,043(0,011) a3 +0,154(0,026) a4 +0,038(0,011).
- win − mid por instante (IS | OOS): t1−250 ms −2,0 | −3,0 pp; t1−100 ms −0,8 | −1,9; t1+0,25/2/10/30 s +0,1/+0,1/+0,1/0,0 | −0,9/−0,9/−1,0/−0,9; T−90…T−10 s −0,0…+0,4 | −0,0…+1,0.
### 4.2 Contenido informativo (ΔlogLoss completo−a0; IC90 por días)
E: IS −0,00010 (−0,00022/+0,00003), OOS −0,00053 (−0,00084/−0,00024). L: IS −0,00051 (−0,00095/−0,00005), OOS −0,00074 (−0,00179/+0,00033). N: IS −0,00004, OOS +0,00026. Término a término, OOS: ΔC (15m) E −0,00031 (−0,00044/−0,00020), L −0,00029 (−0,00045/−0,00014); ΔQ E −0,00023 (−0,00045/−0,00000), L −0,00026 (−0,00100/+0,00040), N +0,00044 (peor; coef IS +0,100, OOS −0,035); zB ≈0 (E −0,00000, L −0,00011 cruza 0). Aportan información medible pero minúscula: ΔC y ΔQ (cola L1); Binance zB y paridad no. rms de q̂ ≈1,0-1,3 pp.
### 4.3 Coste de salir (venta total al bid de t_d+250 ms, solo filas ejecutables; IS|OOS)
S − tasa de acierto = −1,6…−3,1 pp (IS) y −0,3…−3,4 pp (OOS) en las 10 ventanas. EVw vender frente a mantener (IS): e1 −0,066/+0,025, e2 −0,027/+0,051, e3 +0,109/+0,190, e4 +0,406/+0,496, l1 1,176/1,306, l3 2,202/2,330, l6 2,977/3,046 (L está condicionado a bid ≥0,20 por el mínimo de 1 $, por eso EVw alto; lo comparable es la diferencia: vender pierde 0,07-0,13 por € en las 10 ventanas IS y 0,01-0,14 OOS).
### 4.4 VENDER
- 18 variantes: Δ IS entre −0,0246 y −0,0017 (todas <0); Δ OOS <0 en 17/18 (+0,0011 E κ=0,03, 72 ventas). p max-statistic IS = 0,999.
- Elegida en IS (L, κ=0,05): IS Δ −0,0017 (−0,0040/+0,0006), sin 2 mejores días −0,0027, EVw −0,0014 (HOLD +0,0003). OOS Δ −0,0046 (−0,0083/+0,0012), por día −0,0099/+0,0050/−0,0065/−0,0066, sin 2 mejores −0,0082, EVw −0,0375 (HOLD −0,0329), 40 ventas de 4.927 (0,8 %); −6,5 €/día (IC90 −12,0/−1,0) = −2.367 €/año a 5 acc por pata.
- Placebo OOS p(≥obs)=0,706 (media −0,0035); inversión OOS −0,0035 (92 ventas), IS −0,0060 (468); sin mínimo de 1 $: IS −0,0027 (257), OOS −0,0042 (43). Monedas con Δ OOS>0: 1 de 6 (DOGE +0,6 €); Δ€ OOS por moneda: BNB −1,4, BTC −3,5, DOGE +0,6, ETH −6,5, SOL −14,6, XRP −0,5; IS: BNB +5,1, BTC −8,6, DOGE +3,4, ETH −30,7, SOL −19,3, XRP +7,8 (30 celdas moneda×bucket en analysis_salida.txt: ruido de ±1-15 €). Criterios i-v: todos falsos.
### 4.5 CANCELAR
- n0, κ_in=0 (elegida): IS Δ_total +0,0027 (−0,0141/+0,0201; sin 2 mejores −0,0056; p max-stat 0,50), canceladas 12.541/21.875 (57 %). OOS +0,0155 (−0,0330/+0,0632; sin 2 mejores −0,0330), canceladas 2.460/4.927 (50 %), +88 € en 4 días SOLO porque HOLD OOS<0; EVw retenidas −0,0359 (−0,168/+0,100) frente a HOLD −0,0329. Placebo OOS media +0,0207, p95 +0,0394, p(≥obs)=0,706; inversión +0,0001 (715 canceladas). κ_in ≥0,01 cancela 79-99 % (política degenerada). Criterios: i F, ii F, iii F, v V → REJECTED.
### 4.6 Contra la escalera fija (mismas unidades; IS | OOS)
HOLD +0,0003 | −0,0329; +10c −0,185 | −0,198; +20c −0,147 | −0,178; +45c −0,078 | −0,116. La fórmula no los rescata ni los supera: la mejor regla (VENDER L κ=0,05) queda en −0,0375 OOS.

## 5. Red team
- «Cancelar mejora €»: artefacto de HOLD<0 (cancelar todo da 0); el placebo con el mismo desplazamiento medio saca más (+0,0207). - «ΔC y ΔQ aportan»: ΔLL de 2-5·10⁻⁴ nats; igual de pequeño en IS; el coeficiente de ΔC IS (+0,03) y OOS (+0,07…+0,21) difieren 3-8×: inestable. - Binance zB sin σ calibrada (σ60 realizada): su nulo es condicional a esa construcción. - SE de la tabla 4.1 anticonservadores (filas correlacionadas por mercado). - Heredado de P: relleno sin cola (Q0=0) y sin L2; ventas con ejecución a nivel 1 con edad ≤2 s; 4 días OOS. - Coincidencia de dos p de placebo idénticas (0,706) = 141/200 en ambos: dos permutaciones distintas, verosímil; no verificado a mano.
- Lo que sí replica: HOLD calibrado tras el relleno, AS previa al relleno, y que todo escalón/venta tomadora empeora mantener (ESCALERA_PATAS_B, SALIDA_DINAMICA_28oct, ENTRADAS_BAJO_010_B).

## 6. Términos no calibrables hoy y logger mínimo
- Rewards de liquidez (r: mi 50, ma 4,5) y rebate de mercado: 5 acc no puntúa; falta el pool por mercado. Logger: gamma (rewards min_size, max_spread, rate diaria) al registrar cada mercado 5m (KB/día).
- Profundidad L2/cola real e identidad del barrendero: L1 solo. Logger: top-5 niveles por lado de los tokens 5m cada 250 ms en [apertura−30 s, cierre+5 s], gz por hora, ~200 MB/día, retención 5 d, en datalogs fuera de git; identidad vía onchain_fills (maker/taker explícitos; copiar a keep_ antes de la rotación de 4 d).
- γ de inventario: preferencia, no identificable por EV.

## 7. Ronda 2 (hipótesis rival / variable)
1. Decisiva y barata (datos existentes, ~10 min con mawk): curva AS(δ) de la puja por profundidad respecto al touch (bb−0,02…bb+0,01) en 0,10-0,30, relleno estricto + reloj de recepción, 22 días, resolver x*=R_in−1/k_eff. Éxito: algún δ con E[win−x+ρ | relleno] ≥ +0,02/acc, n≥750, ≥10 días con IC90 por días >0, placebo p<0,05 (sin max-statistic sobre δ no se acepta). Fracaso: AS(δ)≥δ+ρ en todo δ ⇒ cotizar pasivo en 5m no tiene EV con información L1; B solo se reabre con subsidio (rewards) o L2/identidad.
2. Variable a añadir si hay logger: desequilibrio multi-nivel (ΔQ fue el término más estable) y rewards.
3. Hipótesis rival ya apuntada por los datos: el valor no está en la regla de salida sino en la selección de la entrada (BNB hold +0,054 IS/+0,108 OOS) y en el subsidio; las wallets que «lo hacen» no ganan por una regla de parada (Prop. 2.2).

## 8. Reproducibilidad
`cd experimentos/5m_barato/formula_r1_28oct; bash run_all2.sh` (22 días, idempotente, nice 19, mawk) y `bash run_analysis.sh` (30 s) → analysis_salida.txt. HASHES.txt con sha256 de PREREG, ADENDA1/2, extract.py/extract_v1.py, analysis.py y lanzadores. Datos: units/ (alpha_miner_b_27oct), m5_registro y m15_registro (22 días), maker_ms_desenlaces_cache.json. Estado: COMPLETO (22/22 días).


## Actualizacion 28-Oct (ronda 2)
Ver FORMULA_R2_B.md: la curva de profundidad de la puja pasiva es plana (EV/acc ~0, esquina en +1 tick) y la compuerta dC/dQ solo recupera la cota analitica (+0,2-0,8 pp/acc); el precio de cotizacion x* de la sec. 7 queda cerrado con informacion L1+15m.
