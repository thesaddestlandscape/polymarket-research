# Sesión 20-Oct TARDE (14:50-18:10Z) — dónde estamos (complementa SESION_20OCT_STATUS_Y_RELANZAR.md)

## 1. B real (H47 escalón B, wallet dedicada 0x659a40FF9920fEBc5a66836213040924343d297F)
- Javi autorizó (explícito) tandas sucesivas de 5 $ de riesgo con reinversión, suelo duro 12 pUSD. Regla vigente hasta que haya algo acumulado para subir stake.
- Saldo inicial 19,587 pUSD. A las 18:09Z: saldo 29,57 → **+9,98 $ de saldo bruto**; 0 posiciones abiertas marcadas. ~14 rellenos en 5 tandas: es una racha con pocos rellenos, NO prueba edge.
- Tandas: 1 (+0,08) · 2 (+5,00) · 3 (agotada, saldo 20,21) · 4 (pico 34,28, cerró en 29,57, suelo se quedó en 29,28 → agotada) · **5 en curso desde 18:09Z (suelo 24,57)**. Reseteos de suelo hechos: 4 (3 con confirmación reforzada «VEZ n» y segundo motivo).
- **KILL falso (2 veces)** «ya casada» en orden joven: arreglado en dev, commit `0b0eede035` (`ack` del POST + estado terminal leído tras ASENTAR_S); 2 /code-review; confirmado en real (cancel_ya_terminal_ack con MATCHED, sin kill).
- **Supervisor** `h47sup` (`experimentos/5m_barato/h47_tandas_supervisor.py`, autorización expresa de Javi): relanza B si cae sin KILL, reinicia B al ganar (saldo ≥ suelo+6, sin pujas 90 s) para subir el suelo, NO resetea suelos (guarda humana), no relanza si hay `parada` sin reseteo (bug de bucle corregido 18:09Z) ni con KILL ni con saldo < 12. Log `datalogs/h47_tandas_supervisor.log`. Parar: fichero `h47_tandas_supervisor.STOP` o `screen -S h47sup -X quit`.
- Cuando una tanda se agota por pérdida el reseteo lo hace la sesión principal: `echo "REINICIAR SUELO 3d297F VEZ n" | python experimento_maker_h47.py --escalon B --confirmo-dinero-real --reiniciar-suelo "motivo" --segundo-motivo "motivo2"` (n = reseteos previos+1), luego relanzar B. Parar B: `.KILL` o `screen -S h47B -X quit`.

## 2. H23 maker (paquete real, NO en real)
- 3 /code-review: 1ª (8 hallazgos) → arreglos 1-7; 2ª (8) → ronda 2; 3ª (9) → **ronda 3 final en curso** (agente a39e85c1f1c62f407): fallo de gamma apaga el kill acumulado, evaluar kill antes de la 1ª orden de tanda, dedupe por oid entre ledgers, puerta H47-B (escalón B, n_max≥230, sha), `_libro_fresco` con conexión sana, honestidad del kill sigma (inalcanzable <~10 posiciones; protección real = suelo de saldo H47), peor caso (hi), fsync del kill_brazo, sha de pares_contabilidad, recuperación de ledger truncado. Después el paquete se CONGELA hasta n≥40.
- Kill V3 (decisión Javi): acumulado entre tandas, tope 5,0 $ por tanda no persistente (lo acota el suelo de H47), fórmula 1,645·σ1·s·√n − 0,05·s·n con n≥3.
- Datos replay (13 días BTC): variante A n=16 EV +0,99 → +0,393 con 5 acc, **≈0 sin los 2 mejores días**; B n=26 +0,74 (sin 2 mejores −0,168). Gate n≥40 NO cumplido.
- Para real faltan: ronda 3 + congelar, ensayo en seco extremo a extremo (desplegar `h23_maker/` en dev), H47-B terminado (230 pujas, sin kill), n≥40, **OK de Javi con el sha del OK** (`--imprimir-sha`; el último dado: `sha=c394037e5e6656bd regla=46eff95337902549 h47=439a70e9262ef38c pares=5e116f619887345d shadow=43373dd4affe3181 kill=ffcf92552ead5dc1`, cambiará con la ronda 3).

## 3. Resto de la misión
- Colas de calibración (hecho): c≈0,97 ETH/SOL/XRP/DOGE/BNB, BTC 0,90, cola base; parte B sin rellenos reales entonces (ahora hay ~14 de B real).
- H5M maker: CONFIRMADA como población (11 días, 22.031 unidades, EV +0,116 IC90 (+0,082,+0,146)); captura propia vía B. Agente de captura H5M NO lanzado: esperar más rellenos de B.
- V4/V3: agente alpha-researcher (ad9f26c81eec1292d) esperando a sus cálculos (vía maker, H56+ preregistradas). Tomador V4 no capturable (latencia).
- H55/H53: agente event-causality (a190a2f8eed50b9a8) esperando a sus cálculos (6 monedas, 15m/60m, brazo sombra F2 dry-run, propuesta de cron). Vigías: n=1, pendientes.
- R5K: H48 el 24-Oct. Revisión semanal ~27-Oct. PRECIERRE 5m (n=24, +5,72 $) y 15m (n=11, +5,57 $) en 2 €, sin gate.
- `verify_deploy`: arreglado el falso CAÍDO de h23shadow (commit d44769e0cf). vigiasfreq reiniciado.
- Dashboard 5m barato: PENDIENTE para más adelante (Javi), solo anotado (`PENDIENTES_5M_BARATO.md`, memoria `project_dashboard_5m_barato_pendiente_20oct`). Puerto 8891 ocupado por otro servicio: elegir otro.
- Decisiones abiertas de Javi: VPS / parar multivenue (no se recomienda parar: ~12 % de un core, solo captura), capital por peldaño (tandas de 5 $ mientras no haya más acumulado), OK final H23.

## 4. Al retomar, en este orden
1. B: `tail h47_tandas_supervisor.log`, KILL, saldo vs suelo, ¿tanda agotada (necesita reseteo)? PnL realizado = saldo − 19,587 con posiciones resueltas.
2. Informes de los agentes H55/H53, V4/V3 y ronda 3 de H23 (si llegaron); /code-review 4º del paquete H23 solo si la ronda 3 cambió lógica.
3. Lanzar el agente de captura H5M cuando B tenga ≥30 rellenos.
4. Pendientes de Javi (arriba).
