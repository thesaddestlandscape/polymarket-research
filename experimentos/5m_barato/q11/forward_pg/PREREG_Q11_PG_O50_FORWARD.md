# PREREGISTRO FORWARD — PG_O50 (puerta de colocación) · escalera G ETH/SOL/XRP 5m · congelado 05-Nov-2026 ~15:30Z, ANTES del 06-Nov 00:00Z
Estado de partida: EXPLORATORIO (días 29-Oct..04-Nov gastados; regla elegida a posteriori; red-team: INCONCLUSIVE inclinado a desfavorable, p max-t 0,090 sobre 14 políticas). Esto prerregistra SOLO el contraste forward. Validado: 0 €. Dinero real: NINGUNO (dry-run/simulación).
## Regla congelada
- **PG_O50** (= passC5c VARS `('PG_O50','OWN','0.5','avo')`): armar la puja de la escalera G solo si el modelo OWN congelado da p < umbral c=0,5 (evitar los momentos de mayor riesgo de barrido); si no, no armar. Resto de la escalera = G0 sin tocar (engine.py).
- **Modelo OWN**: HGB (rasgos T, L, bidL, act_i, lado_i; hiperparámetros en modelo_own.json), entrenado UNA vez con 26-Oct..04-Nov (263.879 filas), umbral 0,08880918519419896. sha256 modelo_own.pkl = f80d7b573bd74084a8fb6b601af84f0eab7c7d8dd155f1f17d90070d28eb3839 ; modelo_own.json = 35adc359660d8b99f3719d73989d1f9f9dc2ef20a974e159a0ec577cf69ab8dd ; entrenar_own.py = ea9f59056d0e3283bba5bc498a6242093eb20cbf2cbcb4d6e5acf94f49b30a68. No se reentrena ni se retoca el umbral durante el forward.
- Comparadores: **G0** (sin puerta) y **GEO6** (armar solo si bid5−L ≥ 6c). Familia ya mirada y declarada: 14 políticas (RC5, RC5b, RC5c, RC5d, ver Q11_redteam_PG_O50_05nov.md); ninguna otra se añade al contraste.
## Medición (cambios del red-team incorporados)
1. **Cotas del relleno OBLIGATORIAS cada día**: BASE, STRICT, OPT, THIN y CROSS (redteam/rt_sim.py). Contraste ΔPnL(PG_O50−G0) con IC90 pareado **por cierre** (nunca por día solo).
2. **PASA** solo si: Δ>0 con IC90 por cierre >0 en BASE **y** estimación puntual >0 en CROSS. Si falla en CROSS => «no identificado por el relleno».
3. **No atribuir mecanismo con el tf de BASE**: registrar t_below y t_cross de cada relleno; markouts y K3 con ambas fechas.
4. **Régimen**: Δ por lado. Exigir Δ_YES>0 por separado, o ≥3 días forward con G0-NO ≥0 y Δ_NO>0 en ellos. Si no, aunque pase: «no separable del régimen».
5. **Robustez**: EV absoluto sin los 5 mejores cierres >0 (además de sin los 2 mejores días); EV ponderado por € además del medio por unidad.
6. **«Supera a GEO6»**: Δ(PG_O50−GEO6)>0 con IC90 por cierre >0; no declarable fallido antes de ~20 días ni aprobado con 10 si la Δ se encoge (Δ diaria histórica +18,2 €, sd 14,7; ≈23 días si retiene el 28 %).
7. **Duración**: mínimo 10 días forward (desde 06-Nov 00:00Z), revisión a 20. Datos: cinta on-chain + libro5_ms del día; cobertura de desenlace ≈100 % declarada.
8. **Medición decisiva fuera del simulador** (sin ella ninguna Δ pasa de EXPLORATORY): P(relleno | el ask toca L con nuestra puja sola en L, armada a ≥6c) con micro-órdenes reales de la escalera (peldaño micro-real, requiere OK Javi aparte) o L2 (logger_anticipo_barrido, forward ≈16-17 Nov).
## Resultado permitido
PASS (forward) => propuesta de prerregistro de micro-real, nunca promoción directa. Cualquier otro resultado => REJECTED/EXPLORATORY y se cierra sin reabrir sin fuente nueva. Sin retoques a posteriori de umbral, rasgos, moneda o lado.
