#!/bin/bash
# A6: día NUEVO (19-Oct 00:30-13:00Z). Espera a que acabe la evaluación 17-18 y a load5<12; extrae y evalúa.
S=/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/a6
D=$S/d; V=/mnt/HC_Volume_106538179; DL=/root/polymarket-research-datalogs
while ! grep -q FIN $S/eval_17_18.out 2>/dev/null; do sleep 20; done
while true; do L=$(awk '{print int($2)}' /proc/loadavg); [ "$L" -lt 12 ] && break; sleep 15; done
ulimit -v 3000000
for f in $V/libro5_ms/libro5_ms_2026-10-19_*.csv.gz; do
  b=$(basename $f .csv.gz)
  nice -n 19 ionice -c3 bash -c "zcat $f 2>/dev/null | grep -a -E '^(T|G),' | gzip -1 > $D/$b.TG.gz"
  nice -n 19 ionice -c3 bash -c "zcat $f 2>/dev/null | grep -a '^B,' | cut -d, -f1,2,3,7,8 | gzip -1 > $D/$b.B.gz"
done
nice -n 19 ionice -c3 bash -c "for f in $DL/maker_ms_2026-10-19_*.csv.gz; do zcat \$f 2>/dev/null | grep -a '^k,'; done | sort -u > $D/k_2026-10-19.csv"
cd /root/polymarket-research/experimentos/5m_barato/a6_detector_vivo
TG=$(ls $D/libro5_ms_2026-10-19_*.TG.gz | sort -t_ -k3,3 -k4,4 | tr '\n' ' ')
B=$(ls $D/libro5_ms_2026-10-19_*.B.gz | sort -t_ -k3,3 -k4,4 | tr '\n' ' ')
nice -n 19 ionice -c3 python3 -I r5k_eval.py --desde 2026-10-19T00:30:00Z --hasta 2026-10-19T13:00:00Z --tg $TG --b $B \
  --k $D/k_2026-10-18.csv $D/k_2026-10-19.csv --onchain $DL/onchain_fills_2026-10-19.csv.gz \
  --gamma-cache $S/gamma_des_cache.json --out $S/eval_19.json > $S/eval_19.out 2>&1
echo FIN >> $S/eval_19.out
