#!/bin/bash
cd "$(dirname "$0")"
for f in /mnt/HC_Volume_106538179/libro5_ms/libro5_ms_2026-11-17_3094008.csv.gz /mnt/HC_Volume_106538179/libro5_ms/libro5_ms_2026-11-16_1324947.csv.gz /mnt/HC_Volume_106538179/libro5_ms/libro5_ms_2026-11-17_3198155.csv.gz /mnt/HC_Volume_106538179/archivo_libro5_raw/libro5_ms_2026-10-27_1965189.csv.gz /mnt/HC_Volume_106538179/libro5_ms_prot/libro5_ms_2026-11-08_2714353.csv.gz; do echo "== $(basename $f)"; ionice -c3 nice -n19 ./u2_continuidad.sh $f; done > out/u2_resultados.txt 2>&1; echo FIN >> out/u2_resultados.txt
