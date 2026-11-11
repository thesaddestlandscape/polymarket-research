#!/bin/bash
# 11-Nov (Javi): copia diaria de datalogs forward que rotan (dia completo, nunca hoy). Sin retencion: decidir con Javi. Ficheros truncados (gzip sin cierre) se copian igual (ya truncados en origen).
S=/root/polymarket-research-datalogs; D=/mnt/HC_Volume_106538179/protegido_forward_11nov; mkdir -p $D
hoy=$(date -u +%F); n=0; mal=0
cd $S
for f in $(ls | grep -E "^(maker_ms_2026-11|onchain_fills_|anticipo_perp_|anticipo_liq_|libro_book_ws_|libro_ambos_lados_|polymarket_activity_|binance_movimiento_ask_|precierre_libro_ms_2026-1[01]|penny_clipper_ws_2026-1[01]|valor_relativo_anidado_v2_|tomadores_persistentes_fase0_|colas_escaleras_ws_|arbitraje_anidado_dryrun_2026-1[01]|binance_bookticker_2026-1[01]).*(gz|csv)$"); do
  case "$f" in *"$hoy"*) continue;; esac
  [ -e "$D/$f" ] && continue
  nice -n 19 ionice -c3 cp -p "$f" "$D/$f.tmp" && mv "$D/$f.tmp" "$D/$f" && n=$((n+1))
  case "$f" in *.gz) gzip -t "$D/$f" 2>/dev/null || { echo "GZIP MAL: $f"; mal=$((mal+1)); };; esac
done
echo "copiados=$n gzip_mal=$mal total=$(du -sh $D | cut -f1) ficheros=$(ls $D | wc -l)"
