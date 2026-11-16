#!/bin/bash
# 11-Nov (Javi): copia diaria de datalogs forward que rotan (dia completo, nunca hoy).
# 16-Nov (Javi): TODO se vuelca COMPRIMIDO (gzip) en su destino; los ficheros sin .gz se comprimen al copiar y los
# crudos ya copiados se migran (verificados con cmp antes de borrar). Familias ampliadas (hl_*, perps_*, jump, requote...).
S=/root/polymarket-research-datalogs; D=/mnt/HC_Volume_106538179/protegido_forward_11nov; mkdir -p $D
hoy=$(date -u +%F); n=0; mal=0; cz=0; mig=0
cd $S
for f in $(ls | grep -E "^(maker_ms_2026-11|onchain_fills_|anticipo_perp_|anticipo_liq_|libro_book_ws_|libro_ambos_lados_|polymarket_activity_|binance_movimiento_ask_|precierre_libro_ms_2026-1[01]|penny_clipper_ws_2026-1[01]|valor_relativo_anidado_v2_|tomadores_persistentes_fase0_|colas_escaleras_ws_|arbitraje_anidado_dryrun_2026-1[01]|binance_bookticker_2026-1[01]|hl_posiciones_|hl_ctx_|perps_tickers_|binance_jump_cruzado_|binance_integridad_|binance_huecos_|requote_mejora_sombra_|leadlag_venues_|sondeo_hueco_|puja_fin_).*(gz|csv)$"); do
  case "$f" in *"$hoy"*) continue;; esac
  case "$f" in *.gz) dest="$f";; *) dest="$f.gz";; esac
  [ -e "$D/$dest" ] && continue
  if [ "$dest" = "$f" ]; then
    nice -n 19 ionice -c3 cp -p "$f" "$D/$dest.tmp" || continue
  else
    nice -n 19 ionice -c3 gzip -6 -c "$f" > "$D/$dest.tmp" || { rm -f "$D/$dest.tmp"; continue; }
    touch -r "$f" "$D/$dest.tmp"; cz=$((cz+1))
  fi
  mv "$D/$dest.tmp" "$D/$dest" && n=$((n+1))
  gzip -t "$D/$dest" 2>/dev/null || { echo "GZIP MAL: $f"; mal=$((mal+1)); }
done
# migracion de crudos ya copiados (idempotente): comprimir, verificar con cmp, borrar el crudo
cd $D
for r in $(ls | grep -vE '\.(gz|tmp)$'); do
  if [ ! -e "$r.gz" ]; then
    nice -n 19 ionice -c3 gzip -6 -c "$r" > "$r.gz.tmp" && touch -r "$r" "$r.gz.tmp" && mv "$r.gz.tmp" "$r.gz" || { rm -f "$r.gz.tmp"; continue; }
  fi
  if gzip -t "$r.gz" 2>/dev/null && cmp -s <(gzip -dc "$r.gz") "$r"; then rm -f "$r"; mig=$((mig+1)); else echo "MIGRACION NO VERIFICADA: $r"; fi
done
echo "$(date -u +%FT%TZ) copiados=$n comprimidos_al_copiar=$cz migrados=$mig gzip_mal=$mal total=$(du -sh $D | cut -f1) ficheros=$(ls $D | wc -l)"
# Retencion 30 dias por mtime de origen (cp -p / touch -r conservan mtime); maker_ms ~1 GB/dia domina. 11-Nov (Javi).
find "$D" -maxdepth 1 -type f -mtime +30 -delete
