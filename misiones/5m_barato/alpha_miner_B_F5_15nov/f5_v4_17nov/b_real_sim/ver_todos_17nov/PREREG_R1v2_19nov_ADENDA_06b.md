# PREREG R1v2 — ADENDA_06b (23-Nov-2026, chief; OK de Javi en sesión 23-Nov)
Enmienda SOLO recursos de ADENDA_06 §5. No cambia lógica, días, criterios ni veredictos.
1. Tope de memoria por proceso de la Puerta 0 y de run_v12_post: `ulimit -v` 3 GB → 5 GB (los días 04/05/06/09-Nov murieron por MemoryError con 3 GB; inputs presentes).
2. Precondición de arranque: MemAvailable ≥ 5,5 GB (antes 5 GB). La condición «≥2 GB de swap libre» del PLAN_RERUN_PUERTA0_23nov §2 se SUSTITUYE por esta (opción a de Javi): el swap lo ocupan páginas frías de procesos permanentes (ejecutor live, libro_estado_ws, observadores); vaciarlo arriesgaría OOM del dinero real. El job corre en cgroup pesados.slice (MemorySwapMax=0) vía cron_pesado.sh: si excede, muere solo él.
3. Orden: 05 → 06 → 09 → 04 → 03 (07 y 08 COMPLETE se saltan). Pico por día con /usr/bin/time -v en out_p0/pico_D.txt. 03 huérfano (RUNNING, PID 2980683 muerto) movido a out_p0/huerfanos_20261123/ sin borrar.
4. run_puerta0.sh copia previa en out_p0/run_puerta0.sh.pre_06b; su sha nuevo se registra en HASHES_r1v2_eval.txt.
