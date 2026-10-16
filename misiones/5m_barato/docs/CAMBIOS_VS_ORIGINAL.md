# Cambios respecto al paquete original de Javi (16-Oct-2026)

Originales: `misiones/5m_barato/original_drive_16oct.tar.gz` (20 ficheros, verificados 20/20 contra su `SHA256SUM.txt`; hash del
tar en `original_drive_16oct.tar.gz.sha256`). Aprobado por Javi el 16-Oct: «Sí, con todas».

| # | Cambio | Dónde | Motivo |
|---|---|---|---|
| 1 | F1: «taker-in-book ~50 ms» → MAKER en el libro ~50 ms; TOMADOR casado ≈215 ms del envío | CLAUDE.md, ESTADO, agente event-causality, bloque común | Error de hecho (medido 15-Oct con órdenes reales) |
| 2 | Instalación en `misiones/5m_barato/` + agentes en `.claude/agents/cheap5m-*.md`; el CLAUDE.md raíz NO se sustituye (solo una línea que apunta aquí) | estructura | Exclusividad pedida por Javi y no perder las reglas del proyecto |
| 3 | `cheap5m-chief` pasa a `docs/ROL_CHIEF.md` y lo ejerce la sesión principal | ROL_CHIEF, CLAUDE.md §5, FLUJO | Un subagente no puede lanzar subagentes |
| 4 | Restricción de capital real (34,59 $, stake 2 €, sin recargas) + capacidad V7 y pastel de la caja | CLAUDE.md §1, agente risk-economics, MAPA §7 | Sin ella el plan a 200 k€ partía de un supuesto imposible |
| 5 | alpha-researcher puede proponer a diario (máx. 5) desde los resultados; el chief filtra; decide Javi | CLAUDE.md §5, agente alpha-researcher | Decisión de Javi 16-Oct (mezcla de las dos opciones) |
| 6 | `MAPA_ARTEFACTOS.md` nuevo con rutas verificadas | docs | Evitar que los agentes busquen lo que ya sabemos (cuota y tiempo) |
| 7 | `TRAMPAS_5M_BARATO.md` nuevo | docs | Errores ya cazados que afectan a la misión |
| 8 | Universo: diseño en BTC; v4/V2/V3/V5 multimoneda tal como se congelaron | CLAUDE.md §1, MAPA §0, bloque común | Evitar que "corrijan" v4 a solo BTC |
| 9 | Definición de "barato" = pata 5m barata respecto a bid15(s), distinta de "precio < 0,10" | MAPA §0 | Ambigüedad del paquete |
| 10 | Reglas de código para execution-engineer (dev, vigías hasheados, ejecutor compartido con órdenes reales, watchdog, F2 reservado) | agente execution-engineer, CLAUDE.md §7 | Reglas del repo que el paquete no conocía |
| 11 | Datos truncados rellenados: placebo −0,003; @mo-money 22,6 % vs 17,1 %; «−0,002»; «n=40» = G1 ejecutables | CLAUDE.md, ESTADO, REGISTRO H12, agentes | Existían en los informes |
| 12 | Estado posterior a 07:40Z (decisión→envío 5,45 ms, envío inline, ref5) | CLAUDE.md §3.5 | Actualización |
| — | Bloque común en los 9 agentes: ámbito exclusivo, lecturas obligatorias, Bash solo lectura, no tocar F2/screens/cron, trabajo pesado con nice/ulimit fuera de 06-09Z, castellano | `.claude/agents/cheap5m-*.md` | Seguridad operativa y cuota |
| — | Descripciones de los agentes empiezan por «SOLO misión 5m barato» | frontmatter | Que no se invoquen fuera de la misión |

Sin cambios: modelos, esfuerzo, herramientas, principios, prioridades P0-P7, etiquetas, cementerio y el resto del texto.
Nota: los subagentes solo aparecen tras reiniciar la sesión de Claude Code; sin cuota de subagentes hasta el 19-Oct 13:00 UTC.
