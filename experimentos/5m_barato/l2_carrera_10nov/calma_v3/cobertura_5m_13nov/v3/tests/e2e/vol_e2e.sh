#!/bin/bash
# L3: volumen de pruebas para los e2e (el hijo REAL de libro_estado_ws pausa libro5 con < 10 GB libres en el volumen de LIBRO5_DIR y su umbral NO se toca: es el del codigo desplegado).
# tmpfs con tope de 12 GB (size= es solo un TOPE: no reserva RAM; se usa lo que escriben los ensayos, unos MB). Ni el disco raiz ni el volumen de produccion entran.
#   vol_e2e.sh monta            -> imprime el directorio montado (rc 0) o rc 1 sin imprimir nada
#   vol_e2e.sh limpia <dir>     -> mata (por PID explicito, leyendo /proc) los procesos cuyo cmdline contiene <dir>, desmonta (umount, y -l si esta ocupado) y borra <dir>. Solo actua sobre /var/tmp/e2e_vol.*
case "${1:-}" in
  monta)
    d=$(mktemp -d /var/tmp/e2e_vol.XXXXXX) || exit 1
    mount -t tmpfs -o "size=${E2E_VOL_GB:-12}g,mode=1777" tmpfs "$d" 2>/dev/null || { rmdir "$d" 2>/dev/null; exit 1; }
    echo "$d";;
  limpia)
    d=${2:-}; case "$d" in /var/tmp/e2e_vol.*) ;; *) echo "vol_e2e: ruta no valida: $d" >&2; exit 1;; esac
    [ -d "$d" ] || exit 0
    for p in /proc/[0-9]*; do pid=${p#/proc/}; [ "$pid" = "$$" ] || [ "$pid" = "$PPID" ] && continue
      { tr '\0' ' ' < "$p/cmdline" | grep -qF -- "$d/" && kill -9 "$pid"; } 2>/dev/null; done
    sleep 0.5
    if mountpoint -q "$d"; then umount "$d" 2>/dev/null || { sleep 1; umount "$d" 2>/dev/null || umount -l "$d"; }; fi
    rmdir "$d" 2>/dev/null; exit 0;;
  *) echo "uso: vol_e2e.sh monta | limpia <dir>" >&2; exit 2;;
esac
