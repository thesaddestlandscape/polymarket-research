---
name: verify-deploy
description: Verificar que un cambio de código Python quedó realmente desplegado (los procesos persistentes corren lo que hay en disco) y reiniciar+probar lo que esté obsoleto. Usar SIEMPRE tras editar cualquier .py del repo, antes de dar el cambio por "hecho". Triggers: "verify deploy", "desplegar", "reiniciar screen", "deploy obsoleto", después de editar dashboard_server.py / live_control.py / photo_finish_logger.py o módulos que estos importan.
---

# verify-deploy — el cambio no está hecho hasta que el proceso lo corre

Cicatrices que codifica: 07-Jul se editó `dashboard_server.py` sin reiniciar la
screen (el watchdog alertó "deploy obsoleto"); 08-Jul se descubrió que
`live_control` llevaba una semana con módulos cacheados del 01-Jul.

## Secuencia (en orden, todas)

```bash
# 1. Compila lo editado
python3 -m py_compile <ficheros_editados.py>

# 2. ¿Algún proceso persistente quedó obsoleto? (exit 1 si hay STALE/CAIDO)
python3 verify_deploy.py

# 3. Reinicia SOLO lo obsoleto (hace quit+relanzar+probe automáticamente)
python3 verify_deploy.py --restart dash      # y/o control, pfinish

# 4. Re-verifica
python3 verify_deploy.py
```

## Mapa fichero → runtime (quién necesita restart y quién no)

| Runtime | Código | Restart al editar |
|---|---|---|
| screen `dash` | dashboard_server.py + sus imports locales | SÍ (`--restart dash`, probe HTTP :8888) |
| screen `control` | live_control.py + imports (shadow_resumen, live_stake, live_guard, live_balance, shadow_digest…) | SÍ (`--restart control`, probe log "escuchando comandos") |
| screen `pfinish` | photo_finish_logger.py | SÍ (`--restart pfinish`) |
| fast/slow loop | shadow_predict, live_trade, shadow_resolve, postmortem, resumen, data_quality… | **NO** — proceso fresco cada ciclo; el siguiente ciclo ya usa el código nuevo. Confirmar viendo una línea nueva en `logs/fast.log` |
| crons | nested_arb_scanner, live_balance, reconciliar, watchdog, smart_money, sync_obsidian | **NO** — proceso fresco por invocación |
| screens `fast`/`slow` (el .sh mismo) | run_fast.sh / run_slow.sh | ⚠️ `verify_deploy.py` los detecta pero **se niega a reiniciarlos** (regla #8 del manual: diagnostica primero, watchdog + marker `orden_en_curso.json`). Editar un .sh mientras bash lo ejecuta es peligroso: hacerlo con el loop parado |

## Trampas conocidas

- **Módulos cacheados**: un proceso Python persistente NO recoge cambios en los
  módulos que ya importó (sys.modules). Editar `shadow_resumen.py` exige
  reiniciar `control` aunque no tocaras `live_control.py` — por eso el script
  vigila el cierre de imports, no solo el entrypoint.
- **Credenciales**: `live_control` y `shadow_digest` cargan `TELEGRAM_*` de
  `data/live/.env` vía load_dotenv (añadido 08-Jul), así que un restart desde
  cualquier shell conserva Telegram. Si un probe de Telegram falla, verifica
  que `.env` sigue teniendo las 2 vars.
- **No confundir con el watchdog**: el watchdog reinicia procesos CAÍDOS; este
  skill detecta procesos VIVOS con código viejo — el caso que el watchdog solo
  avisa a veces y nadie ejecuta.

## Cierre

Commit del código (sin mezclar `data/`) solo cuando el paso 4 da todo ✅.
