"""
backtest.py — v1. Backtesta señales históricas de shadow_predict contra resoluciones reales.

Flujo:
  1. Carga todas las señales de data/shadow/predictions_*.csv
  2. Filtra mercados ya vencidos y consulta resolución en Gamma API
  3. Simula P&L con Kelly fraccional (0.25) y max 5% por posición
  4. Genera métricas: ROI, Sharpe, drawdown, win rate por estrategia
  5. Guarda equity curve CSV + PNG en data/backtest/
"""
import csv, json, math, time
from datetime import datetime, timezone
from collections import defaultdict
from pathlib import Path
import requests

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    HAS_MPL = True
except ImportError:
    HAS_MPL = False

# ── Parámetros ─────────────────────────────────────────────────────────────
CAPITAL_INICIAL  = 1_000.0   # USDC virtual
KELLY_FRACCION   = 0.25      # Quarter-Kelly conservador
MAX_POS_PCT      = 0.05      # Max 5% capital por trade
EDGE_MINIMO      = 0.03      # Solo señales con edge neto >= 3%
MIN_HORAS_REST   = 0         # Incluir mercados ya vencidos (horas_a_vencimiento < 0)
TIMEOUT          = 30
PAUSA            = 0.25

DIR_DATA    = Path("data")
DIR_SHADOW  = DIR_DATA / "shadow"
DIR_OUT     = DIR_DATA / "backtest"
DIR_OUT.mkdir(parents=True, exist_ok=True)

GAMMA_API   = "https://gamma-api.polymarket.com/markets"
HEADERS_HTTP = {"User-Agent": "polymarket-research/backtest/1.0", "Accept": "application/json"}


# ── 1. Carga de señales ────────────────────────────────────────────────────

def cargar_señales():
    señales = []
    for f in sorted(DIR_SHADOW.glob("predictions_*.csv")):
        with open(f, encoding="utf-8") as fp:
            for row in csv.DictReader(fp):
                señales.append(row)
    print(f"  {len(señales)} señales brutas cargadas")
    return señales


def filtrar_señales(señales):
    """Mantiene solo señales BUY con edge suficiente en mercados ya cerrados."""
    ahora = datetime.now(timezone.utc)
    ok = []
    for s in señales:
        # Solo BUY (señal de entrada)
        if s.get("decision", "") not in ("BUY_YES", "BUY_NO"):
            continue
        # Edge suficiente
        try:
            edge = float(s.get("edge_neto", 0) or 0)
        except ValueError:
            continue
        if edge < EDGE_MINIMO:
            continue
        # Mercado vencido (horas_a_vencimiento < 0) o próximo a vencer
        try:
            end_date = datetime.fromisoformat(s["end_date"].replace("Z", "+00:00"))
            if end_date > ahora:
                continue   # aún no ha resuelto
        except Exception:
            continue
        ok.append(s)
    print(f"  {len(ok)} señales válidas (vencidas, BUY, edge >= {EDGE_MINIMO})")
    return ok


# ── 2. Resoluciones Gamma API ──────────────────────────────────────────────

def fetch_resolucion_batch(market_ids):
    """Consulta Gamma API para un batch de market_ids. Devuelve {market_id: p_yes_final}."""
    resoluciones = {}
    for mid in market_ids:
        try:
            r = requests.get(
                GAMMA_API,
                params={"id": mid},
                headers=HEADERS_HTTP,
                timeout=TIMEOUT,
            )
            if r.status_code != 200:
                continue
            data = r.json()
            if not data:
                continue
            m = data[0] if isinstance(data, list) else data
            # outcomePrices: ["1", "0"] → YES ganó; ["0", "1"] → NO ganó
            prices = m.get("outcomePrices") or m.get("outcome_prices") or []
            if len(prices) >= 2:
                try:
                    resoluciones[str(mid)] = float(prices[0])
                except (ValueError, TypeError):
                    pass
        except Exception as e:
            print(f"    Gamma error {mid}: {type(e).__name__}")
        time.sleep(PAUSA)
    return resoluciones


# ── 3. Kelly sizing ────────────────────────────────────────────────────────

def kelly_stake(p_modelo, p_mercado, capital):
    """
    Kelly fraccional para apuesta binaria.
    b = (1 - precio) / precio  (odds netas)
    f* = (b*p - q) / b
    """
    p = max(0.01, min(0.99, p_modelo))
    precio = max(0.01, min(0.99, p_mercado))
    b = (1 - precio) / precio
    q = 1 - p
    f = (b * p - q) / b
    if f <= 0:
        return 0.0
    f_adj = f * KELLY_FRACCION
    return min(f_adj * capital, capital * MAX_POS_PCT)


# ── 4. Simulación ──────────────────────────────────────────────────────────

def simular(señales, resoluciones):
    capital = CAPITAL_INICIAL
    trades = []
    equity = []

    def parse_ts(s):
        try:
            return datetime.fromisoformat(s.replace("Z", "+00:00"))
        except Exception:
            return datetime.min.replace(tzinfo=timezone.utc)

    señales_ord = sorted(señales, key=lambda x: parse_ts(x.get("timestamp_utc", "")))

    for s in señales_ord:
        mid = str(s.get("market_id", ""))
        if mid not in resoluciones:
            continue

        p_yes_final = resoluciones[mid]
        resolvio_yes = p_yes_final >= 0.95
        resolvio_no  = p_yes_final <= 0.05
        if not (resolvio_yes or resolvio_no):
            continue  # mercado en disputa o sin resolver limpiamente

        decision = s.get("decision", "")
        try:
            p_modelo = float(s["prob_yes_modelo"])
            p_mercado = float(s["precio_yes_mercado"])
            edge_neto = float(s["edge_neto"])
        except (ValueError, KeyError):
            continue

        if decision == "BUY_YES":
            stake = kelly_stake(p_modelo, p_mercado, capital)
            ganamos = resolvio_yes
            odds = (1 - p_mercado) / p_mercado
        elif decision == "BUY_NO":
            p_no_mercado = 1 - p_mercado
            stake = kelly_stake(1 - p_modelo, p_no_mercado, capital)
            ganamos = resolvio_no
            odds = (1 - p_no_mercado) / p_no_mercado
        else:
            continue

        if stake < 0.5:
            continue

        pnl = stake * odds if ganamos else -stake
        capital = max(capital + pnl, 0.01)
        ts = parse_ts(s.get("timestamp_utc", ""))

        trades.append({
            "ts": ts,
            "strategy": s.get("strategy", "?"),
            "decision": decision,
            "p_mercado": p_mercado,
            "p_modelo": p_modelo,
            "edge_neto": edge_neto,
            "stake": stake,
            "pnl": pnl,
            "capital": capital,
            "gano": ganamos,
            "question": s.get("question", "")[:70],
        })
        equity.append((ts, capital))

    return capital, equity, trades


# ── 5. Métricas ────────────────────────────────────────────────────────────

def calcular_metricas(equity, trades):
    if not trades:
        return {}

    caps = [CAPITAL_INICIAL] + [c for _, c in equity]
    retornos = [(caps[i] - caps[i-1]) / caps[i-1] for i in range(1, len(caps))]

    media = sum(retornos) / len(retornos)
    var = sum((r - media)**2 for r in retornos) / max(len(retornos)-1, 1)
    std = math.sqrt(var) if var > 0 else 0
    sharpe = (media / std * math.sqrt(252)) if std > 0 else 0.0

    peak, max_dd = CAPITAL_INICIAL, 0.0
    for c in caps:
        if c > peak:
            peak = c
        dd = (peak - c) / peak
        if dd > max_dd:
            max_dd = dd

    wins = sum(1 for t in trades if t["gano"])

    por_estrategia = defaultdict(lambda: {"n": 0, "wins": 0, "pnl": 0.0})
    for t in trades:
        e = t["strategy"]
        por_estrategia[e]["n"] += 1
        if t["gano"]:
            por_estrategia[e]["wins"] += 1
        por_estrategia[e]["pnl"] += t["pnl"]

    return {
        "n_trades": len(trades),
        "win_rate": wins / len(trades),
        "roi": (caps[-1] - CAPITAL_INICIAL) / CAPITAL_INICIAL,
        "sharpe": sharpe,
        "max_drawdown": max_dd,
        "capital_final": caps[-1],
        "por_estrategia": {k: dict(v) for k, v in por_estrategia.items()},
    }


# ── 6. Chart ───────────────────────────────────────────────────────────────

def generar_chart(equity, trades, metricas, ruta):
    if not HAS_MPL or len(equity) < 2:
        return

    fechas = [ts for ts, _ in equity]
    caps   = [c  for _, c  in equity]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 8),
                                    gridspec_kw={"height_ratios": [3, 1]})
    fig.patch.set_facecolor("#0d1117")
    for ax in (ax1, ax2):
        ax.set_facecolor("#161b22")
        ax.tick_params(colors="white")
        ax.spines["bottom"].set_color("#30363d")
        ax.spines["top"].set_color("#30363d")
        ax.spines["left"].set_color("#30363d")
        ax.spines["right"].set_color("#30363d")
        ax.yaxis.label.set_color("white")
        ax.xaxis.label.set_color("white")

    roi   = metricas.get("roi", 0)
    sh    = metricas.get("sharpe", 0)
    wr    = metricas.get("win_rate", 0)
    dd    = metricas.get("max_drawdown", 0)
    n     = metricas.get("n_trades", 0)

    fig.suptitle(
        f"Shadow Paper Trader — Backtest\n"
        f"ROI {roi*100:+.1f}%  |  Sharpe {sh:.2f}  |  "
        f"Win rate {wr*100:.0f}%  |  Max DD {dd*100:.1f}%  |  N={n}",
        color="white", fontsize=11, y=0.98,
    )

    # Equity curve
    ax1.plot(fechas, caps, color="#58a6ff", linewidth=1.8, label="Capital")
    ax1.axhline(CAPITAL_INICIAL, color="#484f58", linestyle="--", linewidth=0.8)
    ax1.fill_between(fechas, CAPITAL_INICIAL, caps,
                     where=[c >= CAPITAL_INICIAL for c in caps],
                     alpha=0.15, color="#3fb950")
    ax1.fill_between(fechas, CAPITAL_INICIAL, caps,
                     where=[c < CAPITAL_INICIAL for c in caps],
                     alpha=0.15, color="#f85149")
    ax1.set_ylabel("Capital (USDC)", color="white")
    ax1.grid(True, alpha=0.15, color="white")
    ax1.legend(facecolor="#161b22", labelcolor="white", framealpha=0.5)

    # Trade PnL bars
    if trades:
        t_fechas = [t["ts"] for t in trades]
        t_pnls   = [t["pnl"] for t in trades]
        colors   = ["#3fb950" if p > 0 else "#f85149" for p in t_pnls]
        ax2.bar(t_fechas, t_pnls, color=colors, width=0.03, alpha=0.8)
        ax2.axhline(0, color="#484f58", linewidth=0.8)
        ax2.set_ylabel("PnL / trade", color="white")
        ax2.grid(True, alpha=0.1, color="white")

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(ruta, dpi=150, bbox_inches="tight", facecolor="#0d1117")
    plt.close()
    print(f"  Chart → {ruta}")


# ── 7. Main ────────────────────────────────────────────────────────────────

def main():
    ts0 = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts0}] === Backtest v1 ===")

    # Señales
    señales_raw = cargar_señales()
    señales = filtrar_señales(señales_raw)
    if not señales:
        print("  Sin señales válidas para backtest (mercados aún no resueltos).")
        return

    # Resoluciones
    market_ids = list(set(s["market_id"] for s in señales if s.get("market_id")))
    print(f"  Consultando {len(market_ids)} mercados en Gamma API...")
    resoluciones = fetch_resolucion_batch(market_ids)
    n_res = sum(1 for v in resoluciones.values() if v >= 0.95 or v <= 0.05)
    print(f"  {len(resoluciones)} mercados encontrados, {n_res} con resolución limpia")

    if not resoluciones:
        print("  Sin resoluciones disponibles. El backtester necesita mercados cerrados.")
        return

    # Simulación
    capital_final, equity, trades = simular(señales, resoluciones)

    # Métricas
    m = calcular_metricas(equity, trades)
    if not m:
        print("  Sin trades ejecutados.")
        return

    # Output consola
    print("\n══════════════════════════════════════")
    print("  RESULTADOS BACKTEST")
    print("══════════════════════════════════════")
    print(f"  Capital inicial : ${CAPITAL_INICIAL:>10,.2f}")
    print(f"  Capital final   : ${m['capital_final']:>10,.2f}")
    print(f"  ROI             : {m['roi']*100:>+10.2f}%")
    print(f"  Trades          : {m['n_trades']:>10d}")
    print(f"  Win rate        : {m['win_rate']*100:>10.1f}%")
    print(f"  Sharpe ratio    : {m['sharpe']:>10.3f}")
    print(f"  Max drawdown    : {m['max_drawdown']*100:>10.1f}%")
    print("\n  Por estrategia:")
    for est, s in sorted(m["por_estrategia"].items()):
        n = s["n"]
        wr = s["wins"] / n * 100 if n > 0 else 0
        print(f"    {est:<35} n={n:3d}  win={wr:.0f}%  pnl={s['pnl']:+.2f}")

    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # CSV trades
    if trades:
        f_csv = DIR_OUT / f"trades_{fecha}.csv"
        with open(f_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=[
                "ts","strategy","decision","p_mercado","p_modelo",
                "edge_neto","stake","pnl","capital","gano","question"
            ])
            w.writeheader()
            for t in trades:
                w.writerow({**t, "ts": t["ts"].isoformat()})
        print(f"\n  Trades CSV → {f_csv}")

    # Métricas JSON
    f_json = DIR_OUT / f"metrics_{fecha}.json"
    with open(f_json, "w", encoding="utf-8") as f:
        json.dump({**m, "timestamp": ts0, "capital_inicial": CAPITAL_INICIAL}, f, indent=2)
    print(f"  Métricas JSON → {f_json}")

    # Chart
    if HAS_MPL:
        generar_chart(equity, trades, m, DIR_OUT / f"equity_{fecha}.png")

    print(f"\n[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] === Fin ===")


if __name__ == "__main__":
    main()
