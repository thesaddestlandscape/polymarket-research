# Dashboard 5m barato (21-Oct-2026) -- SOLO LECTURA, no lanzado, sin commits

Fichero: `experimentos/5m_barato/dashboard/dashboard_5m_barato.py` (stdlib, sin CDN, RSS ~26 MB). Puerto 8892 (8888/8890/8891 ocupados).
Auth HTTP Basic con DASHBOARD_USER/DASHBOARD_PASS (env o solo esas 2 claves de data/live/.env; nunca se envían a la página).
Sin credenciales: fuerza escucha en 127.0.0.1 (fail-closed). Solo GET y un POST `/api/refrescar` (relanza la contabilidad; mín. 60 s).

## Arranque (NO ejecutado; registrado en watchdog y verify_deploy)
`cd /root/polymarket-research && screen -dmS dash5m bash -c 'nice -n 10 .venv/bin/python experimentos/5m_barato/dashboard/dashboard_5m_barato.py >> logs/dashboard_5m_barato.log 2>&1'`
Prueba manual: `... dashboard_5m_barato.py 8892 --host 127.0.0.1` y `curl -u user:pass 127.0.0.1:8892/api/datos`.
AVISO: el `pipeline_watchdog.py` en memoria (desde 24-Sep) no ve el cambio; cuando se reinicie, el watchdog lanzará `dash5m` solo.

## Pestañas
1. CONTABILIDAD: lee `contabilidad_wallet_dedicada/estado_dashboard.json` (exige schema_version 1). Cuadre (rojo si no cuadra),
   saldo/hora, capital, PnL por experimento y por tanda de B, abiertas, cobertura, 50 movimientos, serie diaria en SVG.
   Aviso fijo de concentración (PnL global sin las 2 mejores posiciones, de posiciones.csv) y de rol maker/tomador inferido.
   Hilo: `nice -n 19 ionice -c3 python3 actualizar.py` (RLIMIT_AS 2,5 GB) como máx. cada 5 min, flock en `dashboard/.actualizar.lock`,
   nunca en 06:00-09:15Z salvo botón; no corre si el JSON tiene <5 min.
2. B REAL: tanda actual, suelo (lógica del supervisor: máx. de suelo_* hasta suelo_reiniciado), saldo, margen, KILL (ficheros + ledger),
   screens h47B/h47sup, pausa/STOP, últimas líneas del supervisor, rellenos y eventos de la ejecución actual. Ledger leído en bloques
   desde el final (tope 8 MB, nunca entero, caché por mtime/size).
3. VIGÍAS/H23/H59: mtime y últimas 3 líneas de cada log (V4, V2, V3, H5M, R5K, V5-V7, H23, A6) y screens; sin análisis. H59: sin logs aún.

## Verificado (127.0.0.1:8892, subproceso ya matado, puerto libre)
401 sin/mal auth; 200 HTML; /api/datos 0,9 s con load 37; POST con flock ocupado no ejecuta actualizar.py (202) y el 2º da 429; 404 ok.
py_compile OK de los 3 ficheros. NO hay motor JS en el VPS: el JS solo se comprobó por balance de llaves, no se ha renderizado.
Registro: `pipeline_watchdog.py` (SCREEN_RESTART + check_screens) y `verify_deploy.py::SCREENS` (probe http:8892; 401 = vivo).
Cadena de observadores: ninguno de los dos los importa (grep); no se tocó ningún módulo de esa cadena.
