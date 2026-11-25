# Logger L2 (logger_anticipo_barrido.py) — informe de piloto/despliegue 05-Nov 13:10Z
Medido por el chief tras el corte de sesión (el informe del execution-engineer no llegó a escribirse).
- Despliegue: screen `logl2` (arranque 11:59Z, pid 2124018), registrado en pipeline_watchdog.py (SCREEN_RESTART + lista) y verify_deploy.py (SCREENS, sonda de log). verify_deploy sin STALE.
- CPU 1,9 % de un núcleo (límite 5 %), RSS 34 MB (límite 600 MB), 1 h 10 min de ejecución, 0 errores/caídas en el log.
- Filas: 4/s (4 símbolos × rejilla 1 s) → 240 filas/min medidas; 19.170 filas a las 13:10Z.
- Volumen: +6.238 B/min gz → ~9 MB/día (perp 1 s) + liquidaciones ~0,4 MB (406 B/9.498 filas aprox. en curso). Retención propia 21 d ≈ 200 MB. Sdb 54 %.
- Perps: CVD (vol_compra/vol_venta) y OI en rejilla de 1 s dentro del logger; cron de 5 min intacto.
- Pendiente: el campo `estado` marca `gap` en reinicios; los análisis deben excluir esos segundos. Lectura gz de un día en curso da "unexpected end of file" (normal, stream abierto): leer tolerando EOF.
