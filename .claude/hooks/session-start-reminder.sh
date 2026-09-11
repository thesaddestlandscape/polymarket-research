#!/usr/bin/env bash
# SessionStart hook — recuerda recitar el checklist pendiente al abrir sesion.
# Peticion del usuario 2026-07-05: el 08-Jul lo primero debe ser recitar el pendiente.
CHECKLIST="/root/.claude/projects/-root-polymarket-research/memory/project_revision_pendiente_08jul.md"

# Si el checklist ya no existe (revisado/borrado), no inyectar nada.
[[ -f "$CHECKLIST" ]] || exit 0

d=$(date -u +%Y-%m-%d)
if [[ "$d" > "2026-07-07" ]]; then
  msg="ARRANQUE DE SESION (fecha >= 08-Jul): antes de responder a nada mas, y SIN que el usuario lo pida, lo PRIMERO es recitarle el checklist pendiente (leer ${CHECKLIST} y resumirle los items). Peticion explicita del usuario del 05-Jul."
else
  msg="Recordatorio de arranque: hay un checklist pendiente para ~08-Jul en ${CHECKLIST}. A partir del 08-Jul, recitarlo lo primero al abrir sesion (peticion del usuario)."
fi

printf '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"%s"}}' "$msg"
