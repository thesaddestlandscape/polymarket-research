#!/bin/bash
# deploy_tokens_cache_once.sh -- SUPERADO (14-Nov): wrapper fino. v3 ya contiene la cache de tokens (y la siembra en P2b) y es el UNICO despliegue vigente
# (cobertura_5m_13nov/v3/deploy/deploy_deltas_libro_ws_once.sh). Este wrapper NUNCA ejecuta un despliegue: rechaza --ejecutar y, sin el, redirige al script v3 en dry-run.
echo "SUPERADO: deploy_tokens_cache_once.sh (v5) ya no despliega nada; se usa SOLO deploy_deltas_libro_ws_once.sh (v3, que incluye la cache de tokens)" >&2
for a in "$@"; do [ "$a" = "--ejecutar" ] && { echo "rechazado: este wrapper nunca ejecuta; lanzar el script v3 explicitamente" >&2; exit 2; }; done
exec bash "$(cd "$(dirname "$0")" && pwd)/../../cobertura_5m_13nov/v3/deploy/deploy_deltas_libro_ws_once.sh" "$@"
