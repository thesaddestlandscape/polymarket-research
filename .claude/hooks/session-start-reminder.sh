#!/usr/bin/env bash
# SessionStart hook — fuerza el protocolo de arranque de sesion.
# Peticion explicita de Javi, 2026-07-17: en cada conexion, antes de responder
# a nada, seguir el protocolo completo de CLAUDE.md (una sola fuente de
# verdad -- no duplicar el texto aqui, solo apuntar y forzar la lectura).
# Sustituye al recordatorio de un solo checklist (05-Jul/08-Jul), que ahora
# es un caso particular del punto 4 de abajo.

CHECKLIST="/root/.claude/projects/-root-polymarket-research/memory/project_revision_pendiente_08jul.md"
VAULT="/root/second-brain"

# Refresca el vault ANTES de que Claude lea nada -- no depender de que se
# acuerde de hacerlo (ver project_mision_sistema.md: "la correccion correcta
# no es prometer que me acordare mejor, es convertirlo en codigo"). Silencioso
# y no bloqueante: si falla (sin red, conflicto), el protocolo de abajo ya le
# dice a Claude que revise el vault igualmente.
[[ -d "$VAULT/.git" ]] && git -C "$VAULT" pull --rebase --autostash --quiet 2>/dev/null

msg="ARRANQUE DE SESION: antes de responder a nada mas, y SIN que el usuario lo pida, sigue el 'Protocolo de arranque de sesion' de CLAUDE.md completo -- (1) leer la mision y objetivos (vault de Obsidian ${VAULT}/02_projects/polymarket-research.md seccion 'Mision y objetivo', version que Javi lee/edita + project_mision_sistema.md/project_roadmap_150k.md en memoria nativa: este proyecto es el proyecto de vida del usuario, cada decision de la sesion va alineada a esos objetivos sin excepcion); (2) barrido de salud del sistema (bugs, fallos, sangrados silenciosos o evidentes, cables desconectados -- mismo rigor que un barrido de coherencia completo); (3) revisar MEMORY.md entero, cierres/checkpoints recientes, datos reales (estado_actual.md, hipotesis_auto.md, trades.csv) y el vault de Obsidian en ${VAULT} (ya clonado de forma permanente y recien sincronizado por este hook -- empezar por _index/00_INDEX.md, NUNCA volver a clonarlo); (4) retomar y recitar los pendientes sin cerrar de sesiones anteriores, proactivamente."

if [[ -f "$CHECKLIST" ]]; then
  msg+=" Punto de partida conocido para el (4): ${CHECKLIST}."
fi

printf '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"%s"}}' "$msg"
