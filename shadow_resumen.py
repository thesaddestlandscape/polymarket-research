"""
shadow_resumen.py — genera data/shadow/estado_actual.md tras cada ciclo fast.

Visible en GitHub en tiempo real. Muestra:
  - Bankroll actual vs inicial (20€ operativo / 30€ depósito)
  - P&L del día y acumulado por estrategia con IC, Kelly, apuesta actual
  - Últimas 5 resoluciones
  - Señales abiertas pendientes

También envía un resumen compacto por Telegram cada TELEGRAM_INTERVALO_MIN minutos.
"""
import csv
import json
import glob
import os
import requests as _requests
from datetime import datetime, timezone
from pathlib import Path

from data_quality import leer_estado_calidad

DIR_SHADOW   = Path("data/shadow")
RESULTS_PATH = DIR_SHADOW / "results.csv"
PARAMS_PATH  = DIR_SHADOW / "strategy_params.json"
OUTPUT_MD    = DIR_SHADOW / "estado_actual.md"
LAST_TG_PATH = DIR_SHADOW / "_last_telegram_update.ts"

TELEGRAM_INTERVALO_MIN = 60   # enviar resumen cada N minutos

CAPITAL_OPERATIVO = 25.44   # depósito real operativo (actualizado 2026-06-30)
DEPOSITO_TOTAL    = 30.0
RESERVA           = 4.56


def cargar_csv(path):
    if not Path(path).exists():
        return []
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def cargar_params():
    if not PARAMS_PATH.exists():
        return {}
    with open(PARAMS_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("estrategias", {})


def main():
    ahora = datetime.now(timezone.utc)
    hoy   = ahora.strftime("%Y-%m-%d")

    resultados = cargar_csv(RESULTS_PATH)
    params     = cargar_params()

    # ── Bankroll ──────────────────────────────────────────────────────────────
    pnl_total = sum(float(r.get("pnl_neto", 0)) for r in resultados)
    bankroll  = CAPITAL_OPERATIVO + pnl_total
    roi_op    = pnl_total / CAPITAL_OPERATIVO * 100
    roi_dep   = pnl_total / DEPOSITO_TOTAL    * 100

    # P&L del día de hoy
    pnl_hoy = sum(
        float(r.get("pnl_neto", 0)) for r in resultados
        if (r.get("resolution_timestamp", "") or "")[:10] == hoy
    )

    # ── Stats por estrategia (subtipo más específico disponible) ──────────────
    from collections import defaultdict
    por_strat = defaultdict(lambda: {"n": 0, "win": 0, "pnl": 0.0})
    for r in resultados:
        key = r.get("strategy", "?")
        sub = r.get("subtype", "")
        if sub:
            key = f"{key}#{sub}"
        por_strat[key]["n"]   += 1
        por_strat[key]["win"] += int(r.get("acierto", 0))
        por_strat[key]["pnl"] += float(r.get("pnl_neto", 0))

    # Agrupar también a nivel estrategia base
    por_base = defaultdict(lambda: {"n": 0, "win": 0, "pnl": 0.0, "cronologico": []})
    for r in resultados:
        key = r.get("strategy", "?")
        por_base[key]["n"]   += 1
        por_base[key]["win"] += int(r.get("acierto", 0))
        por_base[key]["pnl"] += float(r.get("pnl_neto", 0))
        por_base[key]["cronologico"].append(
            (r.get("resolution_timestamp", ""), int(r.get("acierto", 0)))
        )

    # ── Últimas 5 resoluciones ────────────────────────────────────────────────
    ultimas = resultados[-5:] if resultados else []

    # ── Señales abiertas (predicciones no resueltas) ──────────────────────────
    resueltos_ids = set(
        (r.get("prediction_timestamp",""), r.get("strategy",""), r.get("market_id",""))
        for r in resultados
    )
    archivos_pred = sorted(glob.glob(str(DIR_SHADOW / "predictions_*.csv")))[-2:]
    abiertas = 0
    for arch in archivos_pred:
        with open(arch, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("decision","") not in ("BUY_YES","BUY_NO"):
                    continue
                clave = (row.get("timestamp_utc",""), row.get("strategy",""), row.get("market_id",""))
                if clave not in resueltos_ids:
                    abiertas += 1

    # ── Construir Markdown ────────────────────────────────────────────────────
    ts = ahora.strftime("%Y-%m-%d %H:%M UTC")
    n_total = len(resultados)
    n_win   = sum(int(r.get("acierto", 0)) for r in resultados)
    wr_g    = n_win / n_total * 100 if n_total else 0

    signo_pnl    = "+" if pnl_total >= 0 else ""
    signo_hoy    = "+" if pnl_hoy   >= 0 else ""
    emoji_roi    = "🟢" if pnl_total >= 0 else "🔴"
    emoji_hoy    = "🟢" if pnl_hoy   >= 0 else "🔴"

    # ── Live real on-chain (mismo origen que dashboard/digest/Telegram) ──────
    try:
        from live_balance import cargar_balance_real
        snap = cargar_balance_real(max_edad_s=3600)
    except Exception:
        snap = None
    if snap and not snap.get("_rancio"):
        em_live = "🟢" if snap["pnl_real"] >= 0 else "🔴"
        hoy_r = snap.get("pnl_hoy_real")
        d7_r  = snap.get("pnl_7d_real")
        live_rows = [
            f"| Total depositado | {snap['deposito_inicial']:.2f} $ |",
            f"| Balance on-chain | **{snap['total']:.2f} $** |",
            f"| P&L real total | {em_live} **{snap['pnl_real']:+.2f} $** |",
        ]
        if hoy_r is not None:
            live_rows.append(f"| P&L real hoy | {hoy_r:+.2f} $ |")
        if d7_r is not None:
            live_rows.append(f"| P&L real 7 días | {d7_r:+.2f} $ |")
    else:
        live_rows = ["| ⚠️ | Sin snapshot on-chain fresco (live_balance.py, cron 15min) |"]

    # Fees reales pagados (fix 08-Jul) -- coste de Polymarket antes invisible,
    # cobrado solo al comprar. Mismo trades.csv que dashboard/Telegram.
    try:
        trades_csv_md = Path("data/live/trades.csv")
        if trades_csv_md.exists() and trades_csv_md.stat().st_size > 100:
            cerrados_md = [r for r in csv.DictReader(open(trades_csv_md, encoding="utf-8"))
                          if r.get("status") == "CLOSED"]
            fees_md = sum(float(r.get("fee_eur") or 0) for r in cerrados_md)
            live_rows.append(f"| Fees pagados (real) | {fees_md:.2f} $ |")
    except Exception:
        pass

    # PnL fiel: stake fijo 1$ + slippage, sin compounding — misma función que el
    # dashboard. Cota superior: no modela fill-ability (~8%, selección adversa).
    try:
        from dashboard_server import _pnl_realista
        pnl_fiel = sum(v for v in (_pnl_realista(r) for r in resultados)
                       if v is not None)
        fiel_row = f"| P&L fiel (stake fijo 1$) | {pnl_fiel:+.2f} $ |"
    except Exception:
        fiel_row = "| P&L fiel (stake fijo 1$) | ⚠️ error |"

    lines = [
        f"# Estado del bot — {ts}",
        "",
        "## Live — dinero real (on-chain)",
        f"| | |",
        f"|---|---|",
    ] + live_rows + [
        "",
        "## Shadow — MODELO SIMULADO (no cobrable)",
        f"| | |",
        f"|---|---|",
        fiel_row,
        f"| P&L sim compuesto | {emoji_roi} {signo_pnl}{pnl_total:.2f} $ (ficción Kelly: {signo_pnl}{roi_op:.0f}% s/ operativo) |",
        f"| P&L sim hoy ({hoy}) | {emoji_hoy} {signo_hoy}{pnl_hoy:.2f} $ |",
        f"| Operaciones resueltas | {n_total} ({n_win} WIN / {n_total-n_win} LOSS) — {wr_g:.1f}% |",
        f"| Señales abiertas | {abiertas} |",
        "",
        "## Estrategias (visión global)",
        "",
        "| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |",
        "|---|---|---|---|---|---|---|---|",
    ]

    # Estrategias base ordenadas por PNL
    for s, d in sorted(por_base.items(), key=lambda x: x[1]["pnl"], reverse=True):
        n   = d["n"]
        wr  = d["win"] / n * 100 if n else 0
        pnl = d["pnl"]
        ic  = (d["win"] + 1) / (n + 2) - 0.5
        confianza = min(1.0, n / 20)
        ic_ef = ic * confianza
        tendencia = _tendencia(d["cronologico"])

        sp = params.get(s, {})
        activa = sp.get("activa", True)
        apuesta = sp.get("apuesta_kelly", 0.90)

        est_str = "✅ activa" if activa else "🚫 desactivada"
        if activa and n < 8:
            est_str = "⏳ acumulando"
        elif activa and ic_ef < 0:
            est_str = "⚠️ IC negativo"

        signo = "+" if pnl >= 0 else ""
        lines.append(
            f"| {s} | {n} | {wr:.1f}% | {ic_ef:+.3f} | {tendencia} | {signo}{pnl:.2f}$ | {apuesta:.2f}$ | {est_str} |"
        )

    lines += [
        "",
        "## Últimas 5 resoluciones",
        "",
        "| Timestamp | Estrategia | Mercado | Resultado | PNL |",
        "|---|---|---|---|---|",
    ]

    for r in reversed(ultimas):
        ts_r   = (r.get("resolution_timestamp","") or "")[:16]
        strat  = r.get("strategy","")
        sub    = r.get("subtype","")
        label  = f"{strat}#{sub}" if sub else strat
        q      = (r.get("question","") or "")[:50]
        acierto = r.get("acierto","0")
        emoji  = "✅ WIN" if acierto == "1" else "❌ LOSS"
        pnl_r  = float(r.get("pnl_neto", 0))
        signo_r = "+" if pnl_r >= 0 else ""
        lines.append(f"| {ts_r} | {label} | {q}… | {emoji} | {signo_r}{pnl_r:.2f}$ |")

    # ─── Sección calidad de datos ──────────────────────────────────────────
    dq = leer_estado_calidad()
    dq_ts   = dq.get("timestamp_utc", "")[:16]
    dq_glob = dq.get("estado_global", "DESCONOCIDO")
    dq_icon = {"OK": "✅", "DEGRADED": "⚠️", "CRITICAL": "🚨"}.get(dq_glob, "❓")
    rechazos = dq.get("rechazos_1h", {})

    dq_rows = []
    for sym, info in dq.get("assets", {}).items():
        ic_sym = {"OK": "✅", "DEGRADED": "⚠️", "CRITICAL": "🚨"}.get(info.get("estado"), "❓")
        age_s  = info.get("age_seconds")
        age_str = f"{age_s/60:.1f}min" if age_s is not None else "N/A"
        px     = info.get("ultimo_precio")
        px_str = f"${px:,.2f}" if px else "N/A"
        alertas = " ".join(info.get("alertas", []))
        dq_rows.append(f"| {ic_sym} {sym} | {px_str} | {age_str} | {alertas} |")

    lines += [
        "",
        "## Calidad de datos",
        "",
        f"{dq_icon} **{dq_glob}** — última verificación {dq_ts} UTC"
        + (f" | rechazos 1h: {rechazos.get('total',0)}"
           f" (rango={rechazos.get('rango',0)}, spike={rechazos.get('spike',0)})"
           if rechazos.get("total", 0) > 0 else ""),
    ]
    if dq_rows:
        lines += [
            "",
            "| Asset | Precio | Age | Alertas |",
            "|---|---|---|---|",
        ] + dq_rows

    # Cross-source si está disponible
    cross = dq.get("cross_source", {})
    if cross.get("fuentes_activas"):
        fuentes = ", ".join(cross["fuentes_activas"])
        consenso = cross.get("consenso", {})
        fe = cross.get("fuente_elegida", {}) if "fuente_elegida" in cross else {}
        cross_rows = []
        for sym, px in consenso.items():
            src = fe.get(sym, "consenso")
            div_str = ""
            for a in cross.get("alertas", []):
                if a["sym"] == sym:
                    div_str = f"⚠️ div {a['max_div_pct']:.2f}%"
            blk = "🚨 BLOQUEADO" if sym in cross.get("bloqueados", []) else ""
            cross_rows.append(f"| {sym} | ${px:,.2f} | {src} | {div_str}{blk} |")
        if cross_rows:
            lines += [
                "",
                f"**Cross-source** ({fuentes}):",
                "",
                "| Asset | Consenso | Fuente | Estado |",
                "|---|---|---|---|",
            ] + cross_rows

    alertas_dq = dq.get("alertas", [])
    if alertas_dq:
        lines.append("")
        lines.append("**Alertas activas:**")
        for a in alertas_dq[:5]:
            lines.append(f"- ⚠ {a}")

    lines += [
        "",
        "---",
        f"*Actualizado automáticamente cada ~60s por el fast loop*",
    ]

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"  [resumen] Bankroll={bankroll:.2f}€ PNL={signo_pnl}{pnl_total:.2f}€ "
          f"({signo_pnl}{roi_op:.1f}% op) | Hoy={signo_hoy}{pnl_hoy:.2f}€ | "
          f"n={n_total} wr={wr_g:.1f}% | abiertas={abiertas}")

    # Telegram periódico (solo LIVE, ver _telegram_periodico)
    _telegram_periodico(ahora)


def _ic_bayes(win, n):
    return ((win + 1) / (n + 2) - 0.5) * min(1.0, n / 20)


def _tendencia(cronologico):
    """Propuesta #5 (artículo breakout, 09-Jul, ver ic_rolling.py): split-half
    cronológico para ver si el edge MADURA o se AGOTA sin correr el script a
    mano. n<30 (o <15 por mitad) no concluye nada — mismo umbral que el resto
    del proyecto."""
    n = len(cronologico)
    if n < 30:
        return "—"
    ordenado = sorted(cronologico, key=lambda x: x[0])
    mid = n // 2
    primera, segunda = ordenado[:mid], ordenado[mid:]

    def ic(rows):
        wins = sum(a for _, a in rows)
        return (wins + 1) / (len(rows) + 2) - 0.5

    gap = ic(segunda) - ic(primera)
    if abs(gap) < 0.03:
        return "➡️ estable"
    return f"📈 madura ({gap:+.2f})" if gap > 0 else f"📉 agota ({gap:+.2f})"


def _esc(s):
    """Escapa _ y * para Markdown v1 de Telegram."""
    return s.replace('_', '\\_').replace('*', '\\*')


def _stats_directas(resultados):
    """Calcula stats curadas directamente de results.csv, sin ruido de params."""
    from collections import defaultdict

    PAIR_BL   = {'Ethereum', 'XRP', 'Dogecoin', 'BNB', 'Binance'}
    GBM_KEYS  = {
        'BTC#15min':  ('UPDOWN_GBM', '15min', 'BTC'),
        'SOL#15min':  ('UPDOWN_GBM', '15min', 'SOL'),
        'ETH#15min':  ('UPDOWN_GBM', '15min', 'ETH'),
        'BTC#60min':  ('UPDOWN_GBM', '60min', 'BTC'),
        'ETH#60min':  ('UPDOWN_GBM', '60min', 'ETH'),
        'SOL#60min':  ('UPDOWN_GBM', '60min', 'SOL'),
    }

    gbm = defaultdict(lambda: {'n': 0, 'win': 0, 'pnl': 0.0})
    of_btc_sol = {'n': 0, 'win': 0, 'pnl': 0.0}
    buyno_15min = {'n': 0, 'win': 0, 'pnl': 0.0}
    buyyes_60min = {'n': 0, 'win': 0, 'pnl': 0.0}

    for r in resultados:
        strat = r.get('strategy', '')
        sub   = r.get('subtype', '')
        dec   = r.get('decision', '')
        q     = r.get('question', '')
        w     = int(r.get('acierto', 0))
        pnl   = float(r.get('pnl_neto', 0))

        if strat == 'UPDOWN_GBM':
            parts = sub.split('#')  # e.g. BTC#15min
            if len(parts) == 2:
                pair, window = parts[0], parts[1]
                key = f'{pair}#{window}'
                if key in GBM_KEYS:
                    gbm[key]['n']   += 1
                    gbm[key]['win'] += w
                    gbm[key]['pnl'] += pnl
                    # Split BUY_NO / BUY_YES
                    if window == '15min' and dec == 'BUY_NO':
                        buyno_15min['n'] += 1; buyno_15min['win'] += w; buyno_15min['pnl'] += pnl
                    if window == '60min' and dec == 'BUY_YES':
                        buyyes_60min['n'] += 1; buyyes_60min['win'] += w; buyyes_60min['pnl'] += pnl

        elif strat == 'ORDER_FLOW_5M':
            if not any(p in q for p in PAIR_BL):
                of_btc_sol['n']   += 1
                of_btc_sol['win'] += w
                of_btc_sol['pnl'] += pnl

    return gbm, of_btc_sol, buyno_15min, buyyes_60min


def _telegram_periodico(ahora):
    tok = os.environ.get("TELEGRAM_TOKEN", "")
    cid = os.environ.get("TELEGRAM_CHAT_ID", "")
    if not tok or not cid:
        return

    # Comprobar si toca enviar
    ahora_ts = ahora.timestamp()
    if LAST_TG_PATH.exists():
        try:
            ultimo = float(LAST_TG_PATH.read_text().strip())
            if ahora_ts - ultimo < TELEGRAM_INTERVALO_MIN * 60:
                return
        except Exception:
            pass

    # ── Estado live (switch + ventana) ───────────────────────────────────────
    try:
        from live_guard import estado_live
        est       = estado_live()
        switch_on = est["switch"]
        en_ventana = est["en_ventana"]
        # estado_live no expone 'proxima_ventana'; la próxima va dentro de motivo,
        # p.ej. "fuera_de_ventana (proxima: hoy 08:30)"
        if en_ventana:
            live_estado = f"✅ ON — en ventana"
        elif switch_on:
            live_estado = f"🟡 ON — {_esc(est.get('motivo', ''))}"
        else:
            live_estado = f"❌ OFF — {_esc(est.get('motivo', ''))}"
    except Exception as e:
        print(f"[shadow_resumen] excepción en estado_live(): {type(e).__name__}: {e}")
        live_estado = "? (error)"

    # ── Stats live: balance real on-chain (mismo origen que dashboard/digest) ─
    try:
        from live_balance import cargar_balance_real
        snap = cargar_balance_real(max_edad_s=3600)
    except Exception as e:
        print(f"[shadow_resumen] excepción cargando balance real: {type(e).__name__}: {e}")
        snap = None

    # WR y nº de trades reales desde trades.csv (métricas de actividad, no de saldo)
    trades_csv = Path("data/live/trades.csv")
    hoy = ahora.strftime("%Y-%m-%d")
    n_live_hoy = n_live_total = w_live_total = 0
    fees_total_live = 0.0
    try:
        if trades_csv.exists() and trades_csv.stat().st_size > 100:
            cerrados = [r for r in csv.DictReader(open(trades_csv, encoding="utf-8"))
                        if r.get("status") == "CLOSED"]
            n_live_total = len(cerrados)
            n_live_hoy   = sum(1 for r in cerrados
                               if (r.get("close_timestamp", "") or "").startswith(hoy))
            w_live_total = sum(1 for r in cerrados
                               if float(r.get("pnl_neto_eur") or 0) > 0)
            # fees reales pagados (fix 08-Jul) -- coste de verdad, antes invisible
            fees_total_live = sum(float(r.get("fee_eur") or 0) for r in cerrados)
    except Exception as e:
        print(f"[shadow_resumen] excepción leyendo trades.csv: {type(e).__name__}: {e}")

    def _post(msg):
        _requests.post(
            f"https://api.telegram.org/bot{tok}/sendMessage",
            json={"chat_id": cid, "text": msg, "parse_mode": "Markdown"},
            timeout=10,
        )

    # ════════════════════════════════════════════════════════════════════════
    # MENSAJE 1 — LIVE (dinero real, verdad de suelo on-chain)
    # ════════════════════════════════════════════════════════════════════════
    if snap and not snap.get("_rancio"):
        pnl_t_real = snap["pnl_real"]
        deposito = snap["deposito_inicial"]
        bkr_em = "📈" if pnl_t_real >= 0 else "📉"
        pct_total = (pnl_t_real / deposito * 100) if deposito else None
        pct_hoy = (snap["pnl_hoy_real"] / deposito * 100
                   if deposito and snap.get("pnl_hoy_real") is not None else None)
        hoy_str = (f"{snap['pnl_hoy_real']:+.2f}$ ({pct_hoy:+.1f}%)"
                   if snap.get("pnl_hoy_real") is not None and pct_hoy is not None else "—")
        d7_str  = (f"{snap['pnl_7d_real']:+.2f}$"
                   if snap.get("pnl_7d_real") is not None else "—")
        if n_live_total:
            wr_live = w_live_total / n_live_total * 100
            live_perf = (
                f"Trades: {n_live_total}  |  WR {wr_live:.0f}%  |  hoy {n_live_hoy} cerrados\n"
                f"PnL hoy: {hoy_str}  ·  7 días: {d7_str}\n"
                f"Fees pagados (real): {fees_total_live:.2f}$"
            )
        else:
            live_perf = "Sin trades cerrados aún — esperando primera ventana"
        pct_str = f" ({pct_total:+.1f}% sobre depósito)" if pct_total is not None else ""
        msg_live = (
            f"💰 *BOT LIVE — dinero real* — {ahora.strftime('%H:%M UTC')}\n"
            f"\n"
            f"{bkr_em} Balance: *{snap['total']:.2f}$*  "
            f"(depósito {deposito:.2f}$ → {pnl_t_real:+.2f}${pct_str})\n"
            f"{live_perf}\n"
            f"\n"
            f"Estado: {live_estado}"
        )
    else:
        # Fail loud: sin snapshot on-chain fresco no se inventan saldos.
        msg_live = (
            f"💰 *BOT LIVE* — {ahora.strftime('%H:%M UTC')}\n"
            f"\n"
            f"⚠️ Sin balance on-chain fresco (live\\_balance.py corre por cron cada "
            f"15min) — no muestro saldo hasta recuperarlo.\n"
            f"\n"
            f"Estado: {live_estado}"
        )

    # Solo se envía el mensaje LIVE por Telegram (petición Javi 09-Jul: las
    # simulaciones (shadow) ya se consultan en el dashboard — Telegram queda
    # reservado a lo que está pasando de verdad, dinero real). El resumen
    # shadow completo (GBM en observación, whitelist, PnL fiel) sigue
    # generándose en data/shadow/estado_actual.md y en el dashboard, solo
    # dejó de duplicarse por Telegram.
    try:
        _post(msg_live)
        LAST_TG_PATH.write_text(str(ahora_ts))
        print(f"  [telegram] Mensaje live enviado ({ahora.strftime('%H:%M UTC')})")
    except Exception as e:
        print(f"  [telegram] Error: {e}")


if __name__ == "__main__":
    main()
