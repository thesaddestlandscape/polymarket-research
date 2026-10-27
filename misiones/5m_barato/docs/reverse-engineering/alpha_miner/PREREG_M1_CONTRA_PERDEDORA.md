# PREREG E-AM-M1 — CONTRA-PERDEDORA-VISIBLE (fase 1: población on-chain, fuera de muestra)
Autor: polymarket-quantum-alpha-miner, 26-Oct-2026 (escrito ANTES de mirar ningún dato de 22-Oct en adelante para esta pregunta; manda mtime + sha256).
Mecanismo (MECANICAS_NUEVAS.md M1): las tomadoras perdedoras persistentes compran el lado barato y repiten; quien les vende el barato (maker del complementario) cobra. Pregunta: ¿se puede ANTICIPAR ese flujo desde su primera compra visible on-chain?
Relación: desarrolla la «R8 perdedora visible» propuesta en `experimentos/5m_barato/b_perdidas_22oct/ganadoras_persistentes/INFORME.md` §6; si otro agente ya la prerregistró (carpeta `r8_emparejado`), el chief elige UNA y la otra no se ejecuta (K no se duplica).

## Definiciones (congeladas)
- Fuente: `m5_onchain_D.csv.gz` (5m, 6 monedas, maker/tomador explícitos), desenlace OFICIAL con cobertura en € ≥99 % por moneda×día (si no, día excluido y declarado).
- Perdedoras del día D: definición walk-forward de `ganadoras_persistentes/scripts/a3_perdedoras.py` (sha256 16 f3c20057ade669e2) sobre la ventana D−7..D−1 (z ≤ −2 en banda 0,05-0,30), sin usar nada del día D.
- Disparador: primera compra TOMADORA de una perdedora del día en (m, s) con p∈[0,05, 0,30] y T∈[60, 300] s hasta el cierre; hora t = hora de bloque. Ventana de acción [t+5 s, t+60 s] (≥ bloque + ~3 s: sin look-ahead de identidad).
- Rellenos medidos («tratados»): rellenos maker que compran el complementario ŝ de (m) (o venden s; las ventas se convierten en compra del complementario como en a4) con bloque en la ventana de acción.
- Control: rellenos maker de compra del complementario en banda 0,70-0,95 del MISMO día×moneda×tramo de precio 0,05×tercio de T, en mercados-momento sin ningún disparador en los 60 s previos.
- Placebo: el mismo procedimiento con disparadores de tomadoras NO perdedoras (activas en D−7..D−1 con |z|<1), emparejadas por moneda, precio (0,05) y tercio de T, mismo número de disparadores por día.
- Unidad: mercado (Σ de rellenos tratados por mercado); EV ponderado por € de capital = Σpnl/Σcoste; IC90 bootstrap por DÍA (2.000 réplicas, semilla 20261026) y por cierre como secundario.

## Periodo
OOS: días de cierre desde **2026-10-22** (ganadoras_persistentes midió 06-21 Oct). Lectura decisoria con **≥10 días completos** con cobertura (previsto ~2026-11-01).

## Métricas
- Primaria: Δ = EV_tratados − EV_control (reponderado al mix de celdas de los tratados).
- Secundarias: Δ − Δ_placebo; P(la perdedora vuelve a comprar s en (m) en los 60 s siguientes); EV tratados por moneda (BTC vs alts); sin los 2 mejores días; concentración (perdedora top ≤30 % del € tratado).

## Criterios (K=1 primaria; α=0,05 unilateral)
- **PASA fase 1** si TODO: ≥10 días; ≥400 mercados tratados en total y ≥20 por día de media (y nunca <40 en el periodo); Δ > 0 con IC90 por días > 0; Δ sin 2 mejores días > 0; Δ − Δ_placebo con IC90 por días > 0; BTC y alts con el mismo signo; perdedora top ≤30 %.
- **REFUTADA** si con ≥10 días: Δ ≤ 0, o IC90 de Δ − Δ_placebo contiene 0 (el efecto no es de las perdedoras, es del momento/dirección).
- **INSUFICIENTE** en otro caso (seguir acumulando sin cambios).

## Lo que NO decide
Capturabilidad (cola en el complementario, a ~0,80, con muchos makers) ni €: si PASA, fase 2 con [pes, opt] calibrado y prereg propio.

## Coste
Reutiliza M_/T_ de `VOL/agentes_datos/wallets_ballenas_b/` y scripts de ganadoras_persistentes (≈1-2 min/día); extracción de días nuevos con zcat en streaming. `nice -n 19 ionice -c3`, `ulimit -v 3000000`, fuera de 06:00-09:30Z, load5<4.
