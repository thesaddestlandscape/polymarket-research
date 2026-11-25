# PREREG R1v2 — ADENDA 07 (FIRMADA por el chief 19-Nov ~13:10Z, OK Javi a la fase B). Antes de cualquier lectura de EV de la horquilla.
Base NO editada: PREREG_R1v2_19nov.md (48fe638e…), ADENDA_01..06, CONTRATO_R1v2_19nov_v2.md (6bda3605…). Todo lo no mencionado no cambia.

## 1. Qué fija
La **horquilla de bloqueo** {0, Δ, nivel entero} del canal BLOQUEO del replay (DISEÑO sec. 7a). «EV válido solo si mantiene signo en los tres.» Hoy el código tiene dos extremos: bloq0 (canal apagado = 0) y bloq1 (q = min(restante de la orden, tamaño del nivel visible) = «nivel entero»). Falta Δ.

## 2. Definición propuesta de Δ (unidades: ACCIONES, no USDC)
Δ = cantidad que un relleno por bloqueo puede tomar de nuestra orden: **q_bloqueo = min(restante_de_nuestra_orden, Δ)** (y, como en bloq1, nunca más que el nivel visible). Δ es la mediana del **resto real del tomador a su límite**, en acciones, de los rellenos reales de octubre (20-23 Oct, datos de DISEÑO: ningún dato de noviembre, ningún resultado de EV).
- Fuente: bloqueo_re_19nov/out/l3_reverif_v2.csv, sha256 49e0453125f94e07bd66d47722e0db636771862f0849019e055ebc1e0be838ee (202 filas; calldata on-chain por tx; `estado = ok` en las 202).
- Columna: `rem_sh_limite` = (makerAmount − takerFillAmount) / (makerAmount/takerAmount) = presupuesto USDC sin gastar al límite = `tk_rem·tk_sz` (definición verificada en calldata 19-Nov, ADENDA_SO_A1c; «acciones originales − recibidas» es ERRÓNEA) y `rem_new_descartado`.
- Universo U: `tk_tipo == compra_comp` (la mecánica del bloqueo: el tomador deja su resto como orden en reposo en el complementario) Y `estado == ok` Y `rem_sh_limite >= u`, con **u = 1,0 acción** (umbral fijado a priori: por debajo de 1 acción el «resto» es polvo de redondeo y no hay orden en reposo observable).
- **Δ_central = mediana de `rem_sh_limite` en U, redondeada a 0,01 acciones.** Con los datos de octubre: n(U) = 89, Δ_central = **9.07** acciones (cuartiles 4.13–19.0).
- Sensibilidad por umbral u (descriptiva, NO entra en la horquilla):

| u (acciones) | n | mediana | p25 | p75 |
|---|---|---|---|---|
| 1e-09 | 162 | 1.873 | 0.0 | 10.0 |
| 0.1 | 103 | 5.128 | 2.071 | 16.221 |
| 0.5 | 89 | 9.069 | 4.128 | 19.0 |
| 1 | 89 | 9.069 | 4.128 | 19.0 |
| 2 | 80 | 10.0 | 5.0 | 20.045 |
| 5 | 65 | 14.0 | 6.0 | 23.0 |

## 3. Regla de lectura (exacta)
1. Se miden tres celdas por variante y por estrato: **H0** = bloq0; **HΔ** = canal bloqueo con q = min(restante, Δ_central); **HN** = bloq1 (nivel entero).
2. «Mantiene signo» (`variantes_b.mantiene_signo`): el EV (Σpnl/Σcoste, incondicional, rebate 0) de la variante en H0, HΔ y HN es no nulo y del mismo signo en las tres. Si el signo cambia en cualquiera, el EV de esa variante se publica como **NO ROBUSTO AL BLOQUEO** y no puede ser PASA/éxito.
3. La Puerta 0 ya firmada (ADENDA_06) sigue leyendo bloq0 (primaria) + bloq1 (mismo signo); HΔ se añade como tercera comprobación de signo en FASE B, no cambia la Puerta 0.
4. Δ se fija UNA vez con esta ADENDA; cualquier otro Δ (cuartiles, otro umbral u) es versión nueva y cuenta.

## 4. Implementación (para el review; no editar el motor)
Subclase de `sec7_core.EngineBloqueo` en un fichero nuevo que recorta `q` a Δ solo en los rellenos de canal «bloqueo» (key en `fills`), con Δ como argumento OBLIGATORIO (sin default). b_policy_sim y sec7_core no se tocan.

## 5. Límites declarados
n(U) pequeño (octubre, 4 días, 94 % clase de suelo hi, 11/11 sin L2 el 23-Oct): Δ es una cota de orden de magnitud, no un parámetro estimado con IC. El resto observado es el del tomador REAL, no el de B simulado. No prueba que el bloqueo sea el canal de la AS (prohibido afirmarlo, CONTRATO sec. 10e).
