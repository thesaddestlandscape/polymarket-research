#!/usr/bin/env bash
# vps_setup.sh — Configura un VPS Ubuntu 22.04 para el bot Polymarket 24/7
#
# Uso:
#   chmod +x vps_setup.sh
#   sudo ./vps_setup.sh

set -euo pipefail

GITHUB_USER="thesaddestlandscape"
REPO_URL="https://github.com/${GITHUB_USER}/polymarket-research.git"
REPO_DIR="/home/ubuntu/polymarket-research"
PYTHON="python3"

echo "=== Polymarket Bot VPS Setup ==="

# ── 1. Paquetes del sistema ───────────────────────────────────────────────────
echo "[1/5] Actualizando apt e instalando paquetes..."
apt-get update -qq
apt-get install -y python3-pip python3-venv git screen

# ── 2. Clonar repositorio ─────────────────────────────────────────────────────
echo "[2/5] Clonando repositorio..."
if [ -d "$REPO_DIR" ]; then
    echo "  Ya existe — actualizando..."
    git -C "$REPO_DIR" pull --ff-only
else
    git clone "$REPO_URL" "$REPO_DIR"
fi

# ── 3. Entorno virtual Python ─────────────────────────────────────────────────
echo "[3/5] Creando entorno virtual Python..."
$PYTHON -m venv "$REPO_DIR/.venv"
"$REPO_DIR/.venv/bin/pip" install --quiet --upgrade pip
"$REPO_DIR/.venv/bin/pip" install --quiet -r "$REPO_DIR/requirements.txt"

# ── 4. Directorios de logs ────────────────────────────────────────────────────
echo "[4/5] Creando directorios de logs..."
mkdir -p "$REPO_DIR/logs"

# ── 5. Scripts de control ─────────────────────────────────────────────────────
echo "[5/5] Instalando scripts de control..."

# ─────────────────────────────────────────────────────────────────────────────
# PROCESO A — FAST: klines + predict + resolve cada ~60 segundos
# ─────────────────────────────────────────────────────────────────────────────
cat > "$REPO_DIR/run_fast.sh" << 'FASTSCRIPT'
#!/usr/bin/env bash
# run_fast.sh — Bucle rápido: klines → predict → resolve cada 60s
# Arrancar con: screen -S fast bash run_fast.sh

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="$REPO_DIR/.venv/bin/python"
LOG="$REPO_DIR/logs/fast.log"

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" | tee -a "$LOG"; }

log "=== Proceso FAST arrancado ==="

CICLO=0
while true; do
    CICLO=$((CICLO + 1))

    $PYTHON "$REPO_DIR/fetch_binance_klines.py" >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/shadow_predict.py"        >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/shadow_resolve.py"        >> "$LOG" 2>&1 || true

    # Push de resultados
    cd "$REPO_DIR"
    git add data/shadow/ data/binance/ >> "$LOG" 2>&1 || true
    if ! git diff --cached --quiet 2>/dev/null; then
        git commit -m "fast: ciclo $CICLO $(date -u +%Y-%m-%dT%H:%MZ)" >> "$LOG" 2>&1 || true
        git pull --rebase --autostash >> "$LOG" 2>&1 || true
        git push >> "$LOG" 2>&1 || true
    fi

    sleep 60
done
FASTSCRIPT
chmod +x "$REPO_DIR/run_fast.sh"

# ─────────────────────────────────────────────────────────────────────────────
# PROCESO B — SLOW: captura de mercados, wallets y trades cada ~15 minutos
# ─────────────────────────────────────────────────────────────────────────────
cat > "$REPO_DIR/run_slow.sh" << 'SLOWSCRIPT'
#!/usr/bin/env bash
# run_slow.sh — Bucle lento: markets + wallets + trades cada ~15 min
# Arrancar con: screen -S slow bash run_slow.sh

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="$REPO_DIR/.venv/bin/python"
LOG="$REPO_DIR/logs/slow.log"

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" | tee -a "$LOG"; }

log "=== Proceso SLOW arrancado ==="

CICLO=0
while true; do
    CICLO=$((CICLO + 1))
    log "--- Ciclo slow $CICLO ---"

    # capture_markets tiene su propio bucle interno de 10 capturas × 60s ≈ 10 min
    $PYTHON "$REPO_DIR/capture_markets.py"  >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/capture_wallets.py"  >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/capture_trades.py"   >> "$LOG" 2>&1 || true

    # Push de datos capturados
    cd "$REPO_DIR"
    git add data/markets/ data/wallets/ data/trades/ data/prices/ >> "$LOG" 2>&1 || true
    if ! git diff --cached --quiet 2>/dev/null; then
        git commit -m "slow: ciclo $CICLO $(date -u +%Y-%m-%dT%H:%MZ)" >> "$LOG" 2>&1 || true
        git pull --rebase --autostash >> "$LOG" 2>&1 || true
        git push >> "$LOG" 2>&1 || true
        log "  Push OK"
    fi

    log "--- Ciclo slow $CICLO completado ---"
    # Sin sleep extra: capture_markets ya tarda ~10 min
done
SLOWSCRIPT
chmod +x "$REPO_DIR/run_slow.sh"

# ─────────────────────────────────────────────────────────────────────────────
# Script de estado rápido
# ─────────────────────────────────────────────────────────────────────────────
cat > "$REPO_DIR/status.sh" << 'STATUSSCRIPT'
#!/usr/bin/env bash
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
echo "=== Estado del bot ==="
echo "Screen sessions activas:"
screen -ls 2>/dev/null || echo "  (ninguna)"
echo ""
echo "--- Log FAST (últimas 15 líneas) ---"
tail -15 "$REPO_DIR/logs/fast.log" 2>/dev/null || echo "  (sin log aún)"
echo ""
echo "--- Log SLOW (últimas 10 líneas) ---"
tail -10 "$REPO_DIR/logs/slow.log" 2>/dev/null || echo "  (sin log aún)"
STATUSSCRIPT
chmod +x "$REPO_DIR/status.sh"

# Configurar git en el repo
git -C "$REPO_DIR" config user.name  "vps-bot"
git -C "$REPO_DIR" config user.email "bot@polymarket-vps"

echo ""
echo "=== Setup completado ==="
echo ""
echo "ARRANCAR el bot (dos procesos paralelos):"
echo ""
echo "  # Terminal 1 — proceso rápido (predict cada 60s):"
echo "  screen -S fast bash $REPO_DIR/run_fast.sh"
echo "  # Ctrl+A, D para salir sin parar"
echo ""
echo "  # Terminal 2 — proceso lento (captura de datos):"
echo "  screen -S slow bash $REPO_DIR/run_slow.sh"
echo "  # Ctrl+A, D para salir sin parar"
echo ""
echo "VER estado:"
echo "  bash $REPO_DIR/status.sh"
echo ""
echo "RECONECTAR a un proceso:"
echo "  screen -r fast"
echo "  screen -r slow"
echo ""
echo "VER logs en tiempo real:"
echo "  tail -f $REPO_DIR/logs/fast.log"
echo "  tail -f $REPO_DIR/logs/slow.log"
