# Validación independiente ALPHA-B (27-Oct, 22 días m5_registro, IS 05-22 / OOS 23-26)
- Hashes/orden temporal OK (sin commit git; prueba por mtime). Reimplementación propia: 50.154 unidades, campos idénticos; cifras = informe.
- R1 (bb+0,01 recotizada + TD Binance, mantener): IS +0,0004 (8/18 días), OOS −0,032. NO CONFIRMADO: cota optimista. Cola estricta IS −0,015 / OOS −0,046; con regla C IS −0,025 / OOS −0,067. 35,9 % de rellenos con ask actual <= b' (puja rancia 130 ms).
- R2 REJECTED (−0,224, 0/18). R3 REJECTED (−0,066 IS, −0,133 OOS).
- Placebo +0,061/+0,083 = ARTEFACTO: al bid +0,10, bb+0,01 +0,061, mid +0,002, ask −0,081 (−0,123 con comisión). Nadie rellena a bb+0,01 sin estar informado.
- API: no es el cuello (mediana 5 recotizaciones/unidad, p99 global 13/s, máx 47/s; límites oficiales sin comprobar).
- BNB+DOGE IS +0,050 / OOS +0,052 (n=1.116): 1 de 17 cortes post-hoc, no base de forward.
- Reparación mínima antes de cualquier forward de R1: resultado principal = cota pesimista (cola estricta + regla C); validar rellenos de cola con on-chain/log_index.
Código: experimentos/5m_barato/validador_alpha_b_27oct/
