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
