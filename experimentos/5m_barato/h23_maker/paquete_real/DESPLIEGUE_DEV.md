# Despliegue MINIMO de H23 real en /root/polymarket-research-dev (20-Oct-2026)

Estado: HECHO el 20-Oct 18:14Z (solo copia de ficheros NUEVOS; nada reiniciado; sin commits).

## Que hace falta y por que
`experimento_maker_h23.py` hace `sys.path.insert(AQUI)` (AQUI = su carpeta) e importa `experimento_maker_h47` (que importa `experimento_pares_cola_15m` y
`pares_contabilidad`) y `h23_regla` desde `AQUI/experimentos/5m_barato/h23_maker/`. `h23_shadow` (Refs) se importa en `main()` desde esa misma carpeta.
Por eso el ejecutable va en la RAIZ de dev (junto a H47) y la regla/shadow en `experimentos/5m_barato/h23_maker/` de dev.
NO se necesita nada de `a6_detector_vivo`, `h43_unidades` ni `v4_comprar_lo_bueno` (comprobado: `grep` de imports y 75 tests + ensayo en seco sin ellos;
solo `h23_sim_dia.py`, el replay, los usa y NO se despliega). `h23_shadow` lee `data/prices` de PRODUCCION en solo lectura (ruta absoluta).

## Ficheros desplegados (todos NUEVOS en dev; los de H47 no se tocan)
| origen (/root/polymarket-research/experimentos/5m_barato/h23_maker/) | destino (/root/polymarket-research-dev/) | sha256[:16] |
|---|---|---|
| paquete_real/experimento_maker_h23.py | experimento_maker_h23.py | 602d5a2debb42cc0 |
| h23_regla.py | experimentos/5m_barato/h23_maker/h23_regla.py | 8f4ddaffa0a16b99 (hash_config regla 46eff95337902549) |
| h23_shadow.py | experimentos/5m_barato/h23_maker/h23_shadow.py | 43373dd4affe3181 |
| paquete_real/test_experimento_maker_h23.py, sim_kill_v2.py, sim_kill_v3.py | experimentos/5m_barato/h23_maker/paquete_real/ | (el test apunta a /root/polymarket-research-dev) |
NO tocados: `experimento_maker_h47.py` (sha 439a70e9262ef38c), `experimento_pares_cola_15m.py` (5e116f619887345d), `pares_contabilidad.py` (0a41bc39108cdf82): son
dependencias ligadas al OK, y H47-B real corre con ellos (screen `h47B`).

## Procedimiento reproducible (idempotente)
```
bash /root/polymarket-research/experimentos/5m_barato/h23_maker/paquete_real/desplegar_dev.sh     # cp -p + verifica sha origen == destino
cd /root/polymarket-research-dev
/root/polymarket-research/.venv/bin/python experimento_maker_h23.py --imprimir-sha
   # esperado: sha=602d5a2debb42cc0 regla=46eff95337902549 h47=439a70e9262ef38c pares=5e116f619887345d contabilidad=0a41bc39108cdf82 shadow=43373dd4affe3181 kill=59437e2037321aed
nice -n 19 ionice -c3 bash -c 'ulimit -v 3000000; /root/polymarket-research/.venv/bin/python -m pytest -q -p no:cacheprovider experimentos/5m_barato/h23_maker/paquete_real/test_experimento_maker_h23.py'   # 75 passed
```
Interprete: `/root/polymarket-research/.venv/bin/python` (dev no tiene `.venv`).

## Por que no rompe nada
- `experimento_maker_h23.py` es un nombre nuevo: el watchdog solo redespliega ejecutores live cuyo .py cambia; H47-B no cambia (sha h47 igual).
- No hay symlinks (la ruta de `__file__` y los sha son los de los ficheros copiados; una edicion en el origen NO llega a dev hasta volver a ejecutar el script).
- Si el sha de dev difiere del origen tras editar el paquete: el OK de Javi deja de valer (vuelve a emitirse), y hay que re-ejecutar el script.
- Las dependencias H47/pares de dev NO estan versionadas en el paquete: si alguien edita `experimento_maker_h47.py` o `experimento_pares_cola_15m.py` en dev (p. ej.
  parches al B real), cambia `h47=`/`pares=` y el OK deja de valer (es el comportamiento buscado).

## Deshacer
`rm /root/polymarket-research-dev/experimento_maker_h23.py; rm -r /root/polymarket-research-dev/experimentos/5m_barato/h23_maker` (la carpeta `experimentos/5m_barato/h45_escala_19oct`
de dev es de otra pieza y no se toca). No hay estado persistente que limpiar salvo los ledgers de seco en datalogs (ver ENSAYO_SECO_20OCT.md).
