# ADDENDUM H-Q11-SOL013 (2026-11-05, vigente desde 2026-11-06 00:00Z; ningun dia forward contado antes). Aclaraciones; NO cambia reglas, umbrales, activo, nivel ni ventana. PREREG_Q11_SOL013.md intacto (sha 38ebc6f8...). Aprobado por Javi.
1. Criterio ">=60 % de los dias" (T1>PLA_T1 y T1>G0): el denominador son los dias VALIDOS (con dec2+dec3s100). Un dia valido sin relleno T1 NO cuenta a favor.
2. Si el comparador PLA_T1 es NaN o tiene <=2 dias con rellenos, el veredicto es INSUFFICIENT, nunca REFUTA, y ese estado no avanza el contador de 20 dias hacia REFUTED. Si al dia 20 sigue sin dato, tambien INSUFFICIENT.
3. Implementacion: forward_sol013/filtro_sol013.py (rama 'plaok'); el resto del script no se toca.
