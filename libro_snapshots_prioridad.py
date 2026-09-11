"""libro_snapshots_prioridad.py — orden de prioridad de `motivo` para
colapsar `data/live/libro_snapshots.csv` por señal (una señal genera una
fila por cada reintento mientras el libro no la deje pasar -- ver
CLAUDE.md pt.3b, "contar filas subestima la fill-ability 4-8x").

18-Ago (/code-review, hallazgo real): esta lista vivía duplicada casi
verbatim en 5 scripts de análisis distintos (analisis_fills.py y 4
hermanos) -- cada motivo nuevo (como abort_gate_bucket_postrequote, del
mismo día) exigía recordar editar los 5 a mano; olvidar uno deja ese
motivo mal clasificado (cae al final, prioridad mínima) SOLO en ese
script, produciendo conclusiones inconsistentes entre scripts que
analizan el mismo dataset. Fuente única de verdad desde ahora.
"""

PRIORIDAD = ["ejecutada", "fok_kill",
             # 01-Sep: orden REALMENTE enviada y aceptada por la API (a
             # diferencia de todo lo que sigue en esta lista, que nunca
             # llegó a intentarse) pero sin evidencia de fill real tras el
             # poll de _verificar_fill_real() -- estado ambiguo (puede ser
             # un fill real con indexado lento de get_trades(), o una orden
             # que de verdad nunca casó), deliberadamente NO tratado como
             # "ejecutada" (fail-closed) ni mezclado con los vetos/abortos
             # de más abajo (esos nunca llegaron a la API). Debería ser muy
             # raro -- si no lo es, es señal de que el poll de 3×1.5s se
             # queda corto.
             "sin_fill_confirmado",
             "post_only_mode", "abort_requote",
             "abort_gate_bucket_postrequote",
             "veto_profundidad", "veto_sin_datos", "veto_ballenas_debil",
             "no_viable_stake", "veto_discrepancia_tuplas", "fuera_ventana",
             "senal_caducada", "maker_colocada"]


def prio(motivo: str) -> int:
    """Índice de prioridad tolerante a motivos nuevos no listados (al final)."""
    try:
        return PRIORIDAD.index(motivo)
    except ValueError:
        return len(PRIORIDAD)
