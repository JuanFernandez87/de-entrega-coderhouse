# de-entrega-coderhouse

Este script extrae datos de la API pública **criptoya** y crea una tabla nombrada **coins** en Redshift para posterior carga de información diaria de los precios de criptomonedas.

### https://criptoya.com/api

**Endpoint:** /api/{exchange}/{coin}/{fiat}/{volumen}

**exchange:** {str} Proveedor a consultar.

**coin:** (str) Cripto a operar.

Valores posibles:
BTC, ETH, USDT, USDC, DAI, UXD, USDP, WLD, BNB, SOL, XRP, ADA, AVAX, DOGE, TRX, LINK, DOT, MATIC, SHIB, LTC, BCH, EOS, XLM, FTM, AAVE, UNI, ALGO, BAT, PAXG, CAKE, AXS, SLP, MANA, SAND, CHZ

**fiat:** (str) Moneda contra la que se opera, puede ser fiat o stablecoin.

Valores posibles:
ARS, BRL, CLP, COP, MXN, PEN, VES, BOB, UYU, DOP, PYG, USD, EUR

**volumen:** (float) Volumen a operar, utilizar el punto como separador decimal.

La api permite obtener las cotizaciones de los exchanges, la cual devuelve como respuesta:

**ask:** (float) Precio de compra reportado por el exchange, sin sumar comisiones.

**totalAsk:** (float) Precio de compra final incluyendo las comisiones de transferencia y trade.

**bid:** (float) Precio de venta reportado por el exchange, sin restar comisiones.

**totalBid:** (float) Precio de venta final incluyendo las comisiones de transferencia y trade.

**time:** (int) Timestamp del momento en que fue actualizada esta cotización.

La idea es ir guardando los precios de las distintas criptomonedas diariamente y poder realizar un reporte con la variación de los valores.

### Instalación
----
#### 1er Paso
- ***1 forma***. Dar clic en Code y luego en Donwload Zip 
- ***2 forma***. Crear una carpeta, ingresar a git bash y ejecutar

```css
  git clone https://github.com/JuanFernandez87/de-entrega-coderhouse.git
```

#### 2do Paso
- Configurar el archivo env y renombrarlo como .env

#### 3er Paso
- Instalar virtualenv
```css
pip install virtualenv
```
- Dentro de la carpeta del proyecto iniciar el entorno virtual
```css
virtualenv venv
```
- Activar el entorno virtual
```css
source venv/bin/activate
```
- Instalar las librerias utilizadas
```css
pip install -r requirements.txt
```
#### 4to Paso
- Ejecutar el archivo main.py