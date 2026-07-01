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
from datetime import datetime, timezone, timedelta
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
    por_base = defaultdict(lambda: {"n": 0, "win": 0, "pnl": 0.0})
    for r in resultados:
        key = r.get("strategy", "?")
        por_base[key]["n"]   += 1
        por_base[key]["win"] += int(r.get("acierto", 0))
        por_base[key]["pnl"] += float(r.get("pnl_neto", 0))

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

    lines = [
        f"# Estado del bot — {ts}",
        "",
        "## Capital",
        f"| | |",
        f"|---|---|",
        f"| Depósito total | **{DEPOSITO_TOTAL:.0f} €** |",
        f"| Capital operativo | **{CAPITAL_OPERATIVO:.0f} €** |",
        f"| Reserva intocable | **{RESERVA:.0f} €** |",
        "",
        "## Bankroll simulado",
        f"| | |",
        f"|---|---|",
        f"| Inicio | {CAPITAL_OPERATIVO:.2f} € |",
        f"| Actual | **{bankroll:.2f} €** |",
        f"| P&L acumulado | {emoji_roi} **{signo_pnl}{pnl_total:.2f} €** |",
        f"| ROI s/ operativo | {signo_pnl}{roi_op:.2f}% |",
        f"| ROI s/ depósito | {signo_pnl}{roi_dep:.2f}% |",
        f"| P&L hoy ({hoy}) | {emoji_hoy} {signo_hoy}{pnl_hoy:.2f} € |",
        f"| Operaciones resueltas | {n_total} ({n_win} WIN / {n_total-n_win} LOSS) — {wr_g:.1f}% |",
        f"| Señales abiertas | {abiertas} |",
        "",
        "## Estrategias (visión global)",
        "",
        "| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |",
        "|---|---|---|---|---|---|---|",
    ]

    # Estrategias base ordenadas por PNL
    for s, d in sorted(por_base.items(), key=lambda x: x[1]["pnl"], reverse=True):
        n   = d["n"]
        wr  = d["win"] / n * 100 if n else 0
        pnl = d["pnl"]
        ic  = (d["win"] + 1) / (n + 2) - 0.5
        confianza = min(1.0, n / 20)
        ic_ef = ic * confianza

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
            f"| {s} | {n} | {wr:.1f}% | {ic_ef:+.3f} | {signo}{pnl:.2f}€ | {apuesta:.2f}€ | {est_str} |"
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
        lines.append(f"| {ts_r} | {label} | {q}… | {emoji} | {signo_r}{pnl_r:.2f}€ |")

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

    # Telegram periódico
    _telegram_periodico(ahora, bankroll, pnl_total, pnl_hoy, n_total, n_win,
                        por_strat, params)


def _ic_bayes(win, n):
    return ((win + 1) / (n + 2) - 0.5) * min(1.0, n / 20)


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


def _telegram_periodico(ahora, bankroll, pnl_total, pnl_hoy,
                         n_total, n_win, por_strat, params):
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
        prox      = est.get("proxima_ventana", "")
        if en_ventana:
            live_estado = f"✅ ON — en ventana"
        elif switch_on:
            live_estado = f"🟡 ON — próx. ventana: {prox}"
        else:
            live_estado = f"❌ OFF — próx. ventana: {prox}"
    except Exception:
        live_estado = "? (error)"

    # ── Stats live reales (dinero real de trades.csv) ────────────────────────
    try:
        from live_stake import bankroll_actual, pnl_live_hoy, CAPITAL_OPERATIVO_INICIAL
        bkr_real   = bankroll_actual()
        pnl_d_real = pnl_live_hoy()
        pnl_t_real = bkr_real - CAPITAL_OPERATIVO_INICIAL
        trades_csv = Path("data/live/trades.csv")
        trades_all = list(csv.reader(open(trades_csv))) if trades_csv.exists() else []
        hoy = ahora.strftime("%Y-%m-%d")
        n_live_hoy = sum(
            1 for row in csv.DictReader(open(trades_csv)) if row.get("status") == "CLOSED"
            and row.get("close_timestamp", "").startswith(hoy)
        ) if trades_csv.exists() and trades_csv.stat().st_size > 100 else 0
        n_live_total = sum(
            1 for row in csv.DictReader(open(trades_csv)) if row.get("status") == "CLOSED"
        ) if trades_csv.exists() and trades_csv.stat().st_size > 100 else 0
        w_live_total = sum(
            1 for row in csv.DictReader(open(trades_csv))
            if row.get("status") == "CLOSED" and float(row.get("pnl_neto_eur", 0) or 0) > 0
        ) if trades_csv.exists() and trades_csv.stat().st_size > 100 else 0
        tiene_live = n_live_total > 0
    except Exception:
        bkr_real = CAPITAL_OPERATIVO_INICIAL = 25.44
        pnl_d_real = pnl_t_real = 0.0
        n_live_hoy = n_live_total = w_live_total = 0
        tiene_live = False

    # ── Stats shadow curadas de results.csv ──────────────────────────────────
    resultados_raw = cargar_csv(RESULTS_PATH)
    gbm, of_bs, buyno, buyyes = _stats_directas(resultados_raw)

    LIVE_IC = 0.08
    LIVE_N  = 40

    def fila(label, d):
        n, win, pnl = d['n'], d['win'], d['pnl']
        if n == 0:
            return None
        ic  = _ic_bayes(win, n)
        sp  = "+" if pnl >= 0 else ""
        prog = f"n={n}/{LIVE_N}" if n < LIVE_N else f"n={n}✓"
        if ic >= LIVE_IC and n >= LIVE_N:
            ico = "🔥"
        elif ic >= LIVE_IC * 0.75 and n >= LIVE_N * 0.75:
            ico = "⏳"
        elif ic < 0:
            ico = "⚠️"
        else:
            ico = "▸ "
        return f"{ico} {_esc(label):<18} {prog:<8} IC={ic:+.3f}  {sp}{pnl:.2f}€"

    def _post(msg):
        _requests.post(
            f"https://api.telegram.org/bot{tok}/sendMessage",
            json={"chat_id": cid, "text": msg, "parse_mode": "Markdown"},
            timeout=10,
        )

    # ════════════════════════════════════════════════════════════════════════
    # MENSAJE 1 — LIVE (dinero real)
    # ════════════════════════════════════════════════════════════════════════
    bkr_em = "📈" if pnl_t_real >= 0 else "📉"
    if tiene_live:
        wr_live = w_live_total / n_live_total * 100 if n_live_total else 0
        live_perf = (
            f"Trades totales: {n_live_total}  |  WR {wr_live:.0f}%\n"
            f"Hoy: {n_live_hoy} trades cerrados  |  PNL hoy: {pnl_d_real:+.2f}€"
        )
    else:
        live_perf = "Sin trades cerrados aún — esperando primera ventana"

    msg_live = (
        f"💰 *BOT LIVE — dinero real* — {ahora.strftime('%H:%M UTC')}\n"
        f"\n"
        f"{bkr_em} Bankroll: *{bkr_real:.2f}€*  ({pnl_t_real:+.2f}€ vs inicio)\n"
        f"{live_perf}\n"
        f"\n"
        f"Estado: {live_estado}"
    )

    # ════════════════════════════════════════════════════════════════════════
    # MENSAJE 2 — SHADOW (simulación, no es dinero real)
    # ════════════════════════════════════════════════════════════════════════
    wr_g  = n_win / n_total * 100 if n_total else 0
    sp_t  = "+" if pnl_total >= 0 else ""
    sp_h  = "+" if pnl_hoy   >= 0 else ""

    lineas_shadow = [
        f"🧪 *SHADOW (simulación)* — {ahora.strftime('%H:%M UTC')}",
        f"_(No es dinero real — incluye BUY\\_YES y estrategias en prueba)_",
        "",
        f"Bankroll sim: {bankroll:.2f}€  ({sp_t}{pnl_total:.2f}€ total | hoy: {sp_h}{pnl_hoy:.2f}€)",
        f"{n_total} ops  |  {wr_g:.1f}% WR global",
        "",
        "*Estrategia live activa* (BUY\\_NO #15min):",
    ]

    f_buyno = fila("BUY\\_NO#15min", buyno)
    if f_buyno:
        lineas_shadow.append(f_buyno)
    else:
        lineas_shadow.append("  (sin datos aún)")

    lineas_shadow += ["", "*Otras GBM en observación:*"]
    ORDER_GBM = ['BTC#15min', 'ETH#15min', 'SOL#15min', 'ETH#60min', 'BTC#60min', 'SOL#60min']
    for key in ORDER_GBM:
        d = gbm.get(key)
        if d:
            f = fila(key, d)
            if f:
                lineas_shadow.append(f)

    n_of, win_of, pnl_of = of_bs['n'], of_bs['win'], of_bs['pnl']
    if n_of > 0:
        ic_of = _ic_bayes(win_of, n_of)
        sp_of = "+" if pnl_of >= 0 else ""
        lineas_shadow += [
            "",
            f"*ORDER FLOW* (BTC+SOL): n={n_of}  IC={ic_of:+.3f}  {sp_of}{pnl_of:.2f}€",
        ]

    msg_shadow = "\n".join(lineas_shadow)

    # Enviar ambos mensajes
    try:
        _post(msg_live)
        _post(msg_shadow)
        LAST_TG_PATH.write_text(str(ahora_ts))
        print(f"  [telegram] Mensajes live+shadow enviados ({ahora.strftime('%H:%M UTC')})")
    except Exception as e:
        print(f"  [telegram] Error: {e}")


if __name__ == "__main__":
    main()
