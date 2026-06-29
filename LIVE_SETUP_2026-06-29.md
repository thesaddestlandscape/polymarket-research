# Setup Live Trading — Estado 2026-06-29

## ✅ COMPLETADO

### MetaMask
- Wallet creada con seed phrase de 12 palabras (en papel físico)
- Cuenta `Trading Bot` creada — dirección 0x pública anotada
- Cuenta `Ahorro` creada — dirección 0x diferente
- Red Polygon añadida (Chain ID 137)
- Clave privada de `Trading Bot` copiada y guardada (va al VPS en data/live/.env)

### USDC
- ~50 USDC comprados en Coinbase
- Enviados a `Trading Bot` en red Polygon ✅ (notificación de llegada confirmada)

---

## 🔄 EN CURSO — Crear cuenta Polymarket con IP finlandesa

**Problema actual**: fail2ban bloqueó la IP del PC principal por intentos fallidos de SSH.
**Solución**: esperar 10 minutos y volver a intentar.

**Cuando se desbloquee**, en cmd del PC principal:
```
ssh -D 1080 -N root@37.27.249.72
```
Dejar esa ventana abierta → configurar Firefox con proxy SOCKS → crear cuenta Polymarket.

---

## ⏳ PENDIENTE

### Paso 3 — Crear cuenta Polymarket (IP finlandesa)
- [ ] ssh -D 1080 desde PC principal (bloqueado, esperar 10 min)
- [ ] Configurar Firefox: proxy SOCKS localhost:1080
- [ ] Verificar IP en whatismyip.com → debe salir Finlandia
- [ ] Ir a polymarket.com → conectar MetaMask `Trading Bot`
- [ ] Depositar los 50 USDC en Polymarket

### Paso 4 — Credenciales CLOB API (en el VPS)
- [ ] `pip3 install py-clob-client`
- [ ] Ejecutar script para derivar API key con la clave privada de `Trading Bot`
- [ ] Guardar en `data/live/.env`:
  ```
  POLY_PRIVATE_KEY=0x...
  POLY_API_KEY=...
  POLY_API_SECRET=...
  POLY_API_PASSPHRASE=...
  ```

### Paso 5 — Implementar live_trade.py
- [ ] Reemplazar el STUB actual con la integración real py-clob-client
- [ ] Testear que el bot puede leer el .env y conectar a la CLOB API

### Paso 6 — Activar
- [ ] `bash live_switch.sh on`
- [ ] Primer trade real en la próxima ventana horaria

---

## Datos importantes

| Cosa | Dónde está |
|---|---|
| Seed phrase 12 palabras | Papel físico |
| Clave privada Trading Bot | Copiada en PC (va al VPS) |
| Dirección pública Trading Bot | 0x312bc...001eb (completa en MetaMask) |
| USDC | ~50 en MetaMask Trading Bot, Polygon |
| IP del VPS | 37.27.249.72 (Helsinki, Finlandia) |

---

## Estrategias listas para live cuando esté el circuito

| Estrategia | IC | n | Estado |
|---|---|---|---|
| BUY_NO #15min | +0.144 | 43 | 🔥 LISTA |
| BTC#60min | +0.136 | 20 | ⏳ acumulando |
| ETH#60min | +0.100 | 23 | ⏳ acumulando |
