## ESTADO 18-Nov ~21:30Z (más reciente)
- ADENDA_06 (contrato confirmatorio, 25 checks H, sha b797b7f5…) · ADENDA_07 (5 decisiones Javi; bins p5 dt 555/1.839, vida 354/997) · ADENDA_08 (desviaciones de implementación, ~12: validador debe revisarlas) · código v8 congelado.
- Día DISEÑO 12-Nov completo (out/p1_btc_2026-11-12_DISENO.pkl, 36.164 ev): balance E FALLA (E3 small propio-vs-vecino 0,23; E1 normal dist_ticks 0,166; E2 KS 0,125). Sin tasas vistas.
- EN CURSO (Javi OK): execution-engineer ADENDA_09 = rango EXACTO desde el top (bins 0,1,2,3,4-5,6-8,9-12,>12), vecinos solo mismo rango, small solo nivel propio si E3>0,10; revertir NaN-excluidos y restaurar cláusula NO SOPORTADA; balance en 12 y 16-Nov completos; checks H; hashes v9.
- Si se corta: comprobar si existe ADENDA_09_18nov.md/.sha256 y out/p1_btc_2026-11-16_DISENO.pkl; relanzar engineer desde ahí (no rehacer 12-Nov).
- Después: statistical-validator (ADENDA_06..09 + desviaciones 08 + 25 checks) → run_p1 días 13,14,15,17 (+18,19 cuando completos) → p3 → veredicto ~20-Nov → rediseño R1 (predictive-alpha-engine) → red-team → wallet-intel/event-causality → juez Calma v4.

## ESTADO 18-Nov ~18:30Z (sesión de tarde) — LEER ESTO PRIMERO
Commit 74795f57028. ⚠ CORRECCIÓN (validador 18-Nov): SÍ existían tasas evento−placebo previas: out/obsoletos_preD1/p3_btc_act.json (12:56, regla pre-D-1, 12 y 16-Nov: V1 +0,181, V4 +0,200, V5 +0,048) + FV1 de emparejados/sin pareja leído en 02-b. 12 y 16-Nov = SOLO DISEÑO; veredicto con 13,14,15,17,18,19-Nov (ADENDA_06). run_p1 NO relanzado (pkl 12/16-Nov obsoletos en out/obsoletos_preD1/).
Adendas firmadas (todas antes de mirar tasas): ADENDA_01 (D-1 + 7 menores) · 02 (placebo mismo mercado+nivel, p5 v2, own wallet probada 40/40) · 03 (IPW+EB, covariables PRE-ventana) · 04 (estratos de cola z0/small/normal, recorte de pesos tras EB, Mahalanobis) · 05 (p7_ipw_balance.py: simple 1:1 Mahalanobis mismo token+estrato, tope 2 % masa/control, soporte por token).
Resultado de balance fxK3h (12-Nov 03:40-06:40Z, 4.929 eventos): simple 14,75 % sin pareja, SMD máx 0,110 (small/normal 0,147 justo); primario SMD ≤0,025, n_eff pooled 1.027 (small 77,5), masa máx 1,73 %, exclusión 5,0 %.
HECHOS ACEPTADOS POR JAVI (valen para todo): ≥80 % de la masa caída del nivel en (t−1000,t−50) = retiradas reales, no fills. No hay L2 BTC 20-23 Oct (B no operó BTC).
Control p5 (B ETH/SOL/XRP, post-estratificado): R1 rellenos 0,705 vs no rellenos 0,495 (LR 1,42; F90 1,27; SOL 0,97) → R1 discrimina poco frente a M2≥3. Javi: R1 debe cancelar SOLO las malas y explotar las buenas → rediseño.
Diagnósticos punto 1: diag_punto1/ (entradas en /root/polymarket-research-datalogs/pista_cola_18nov/diag_punto1/, cmp OK).

COLA (uno a uno, Javi da feedback a cada salida):
1. statistical-validator: revisar ADENDA_01..05 + p7 + p5. Comprobar supuesto niveles vecinos ±0,02 (70-79 % del peso en z0/small), estratos a 0,147, IC por días/cierres vs n_eff, semiancho gate de small, z0 no predice desenlace (gate de p3).
2. Rediseño R1 (polymarket-predictive-alpha-engine: P(relleno malo | info ≤t)) → red-team.
3. p3 con pesos por estrato → relanzar run_p1 6 días (12-17 Nov, ~25-40 min/día, prio_pista.sh) → veredicto prereg.
4. wallet-intelligence (quién cancela) → event-causality (cancelación −300..−160 ms ex ante).
5. Juez Calma v4 passT_v4 (cron v3 retirado 18-Nov) → CALMA-T1 / E1b tras F5.

# REANUDAR AQUÍ — RE-B-COLA-CANCELA (parado por Javi 18-Nov ~13:45Z)

Estado: agente cheap5m-reverse-engineer DETENIDO a mitad. Nada corriendo (runner, p1 y prio_pista parados).
Contrato vinculante: ../CONTRATO_PISTA_COLA_18nov.md. Prereg congelado: PREREG_PISTA_COLA_18nov.md (+.sha256), NO editar.
Etiqueta MECANISMO; datos 10-14 Nov y >=15-Nov liberados por Javi solo para mecanismo (no EV, no forward CXB).

Hecho:
- p2_b98.py → out/p2_b98.json (cola delante de los 202 rellenos de B 20-23 Oct; clase 1 n=98, cola>0 73).
  ⚠ REVISAR: los bloques lo y hi salen IDÉNTICOS en todas las clases → posible bug en el corte por clase de suelo.
- p4_m3_b.py → out/p4_m3_b.json (M3 sobre B, cobertura 147/202; F50 evita 83 %, dPnL +3,78, pero buenos perdidos 106,8 frente a malos evitados 110,6; signo por día mixto). Provisional, sin veredicto.
- p1_dia.py (corregido: salta líneas malas y baja memoria) → out/p1_btc_2026-11-12.pkl y out/p1_btc_2026-11-16.pkl HECHOS.

Pendiente (en orden):
1. Relanzar `./run_p1.sh` (idempotente: salta días con pkl). Faltan 14, 17, 13 y 15-Nov (14-Nov se cortó a medias, sin pkl). ~20 min/día.
   Prioridad (Javi la pidió): `nohup ./prio_pista.sh &` (nice 5 + ionice best-effort 6; el live sigue por encima). El runner para solo en la franja 06-09Z.
2. p3_agrega.py: evento vs placebo EMPAREJADO por ventana [−1000,−300) [−300,−150) [−150,−50), C1/C2, por clase de suelo, IC90 por días y por cierre, permutación por mercado.
3. Veredicto del prereg (R1, M1/M2/M3, latencia p50/p90 paquete_l): SOPORTADA / NO SOPORTADA / INSUFFICIENT (nunca «cerrada»).
4. Huecos de Javi: (a) unión on-chain↔libro 49 % → mejorar y medir falsos emparejamientos; (b) quién cancela → huella de makers, grupos y medida en días distintos; (c) llegada del tomador → cota casado − taker delay + señales previas ≤t. Para cada uno: cuánto se resolvió y qué especialista sigue.
5. Expediente docs/reverse-engineering/casos/RE-B-COLA-CANCELA + ledgers.

## ACTUALIZACIÓN 18-Nov ~15:20Z (cheap5m-execution-engineer): ADENDA_01 aplicada
Ver ADENDA_01_18nov.md (+.sha256), VERIFICACION_ADENDA01.md y HASHES_CODIGO.txt (v3). pkl 12/16-Nov invalidados en out/obsoletos_preD1/. p1_dia.py v2 (D-1, semilla, sg estructural, placebos uniformes, wallet propia), p3 v2 (NaN excluidos, sens a/b/c y e250), p2 renombrado + control, p5_control_sin_relleno.py nuevo. Pendiente: ./run_p1.sh (6 días, ahora ~25-40 min/día) y luego p3.
