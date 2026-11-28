# Anexo de desviación al PREREG_SIML_26nov (27-Nov-2026) — sin versión nueva del PREREG

Ancla: `PREREG_SIML_26nov.md` (sha256 `052d42a391a306171e8d688e7c3690be32baead7401c1f3c17b75bcf7419b404`, intacto; este anexo va aparte para no romper su `.sha256`). Se suma a las desalineaciones residuales del §5.

**Desviación declarada.** SIM-L NO veta libros cruzados ni bloqueados (`bid_rx >= ask_rx`). El ejecutor B-K sí los veta (implícito: `experimento_maker_bk.py::_post_real` y `experimento_maker_h47.py::en_banda` exigen b<a) y desde el 27-Nov los nombra y cuenta (`libro_cruzado`, `libro_sin_dato`; dev-bk b-k-ejecutor, sin commitear por git roto). Regla de referencia: `alpha_miner_B_F5_15nov/PREREG_REPLAY_BRECHA_B_16nov.md` §4.4.

**Magnitud (dato de la autoridad de datos, no medido en este anexo).** ~0,02 % de las filas en banda el 25-Nov están cruzadas/bloqueadas.

**Contrafactual no modelado.** SIM-L puede colocar/rellenar donde el vivo no coloca; el efecto sobre órdenes, rellenos y EV no se ha simulado. No se reajusta ninguna cifra ya reportada de SIM-L; todo informe de SIM-L declara esta limitación.

**Código de SIM-L: no se toca** (KS 27-Nov 14:00Z). Cualquier cambio posterior de SIM-L requiere prereg/versión propia.
