#!/bin/bash
# uso: mkrun.sh nombre
S=/root/pm_ram_test
R=$S/run_$1; rm -rf $R; mkdir -p $R/data/shadow $R/logs
cd $S/snap/data/shadow
for f in *; do
  if [ -d "$f" ]; then cp -a "$f" $R/data/shadow/;
  elif [ "$f" = results.csv ] || [[ "$f" == predictions_*.csv* ]]; then ln -s $S/snap/data/shadow/$f $R/data/shadow/$f;
  else cp -p "$f" $R/data/shadow/; fi
done
cp -a $S/snap/data/live $R/data/live
for d in markets prices alerts backfill binance funding reports sports trades wallets; do ln -s /root/polymarket-research/data/$d $R/data/$d; done
cp -p /root/polymarket-research/data/funding_rates_cache.json $R/data/ 2>/dev/null
echo '{"ultimo_run_utc": "2026-11-01T00:00:00+00:00"}' > $R/data/shadow/patrones_causales_ultimo_run.json
echo '{"ultimo_run_utc": "2026-11-01T00:00:00+00:00"}' > $R/data/shadow/hipotesis_tracker_ultimo_run.json
# codigo: modulos de main (HEAD) + el postmortem pedido
cd /root/polymarket-research; for f in $(git ls-files '*.py' | grep -v /); do git show HEAD:$f > $R/$f 2>/dev/null; done
