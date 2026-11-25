---
name: reference-paridad-contra-json-original-no-md
description: Trampa de paridad 16-Nov - las cifras de los .md estan redondeadas dos veces; comparar contra el JSON original que las genero (p.ej. out_v3/paso0_v3dd/ev.json), con tolerancia = media unidad del decimal publicado.
metadata:
  type: reference
---
En la paridad de lectura de la Etapa 0 (BF5-REPLAY-COLOC-v1, 16-Nov) el EV de ETH en PASS_T_V3_RESULTADOS_11nov.md s.4 figura como -0,056, pero el artefacto original `experimentos/5m_barato/l2_carrera_10nov/out_v3/paso0_v3dd/ev.json` (sha16 de18a23e8ccd9257) da -0,0555 (ya redondeado a 4 decimales): comparar con +-0,0005 contra el md dio un falso NO_PASA. Contra el JSON, G0 y ETH/SOL/XRP cuadran exactos a su precision.
**Why:** un falso negativo de paridad para un programa entero (stop rule); un falso positivo igual de facil con tolerancias holgadas.
**How to apply:** toda paridad/reproduccion se hace contra el JSON/pkl que produjo la cifra publicada (localizar la "Fuente:" del md), tolerancia = media unidad del ultimo decimal del JSON; el md solo como puerta preregistrada si asi lo dice el prereg. Evidencia: etapa0/identidades_SEGT_CX_E0_run1.json (falso negativo) vs identidades_SEGT_CX_E0.json (OK).
