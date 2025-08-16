# Instrucciones del Servidor

## Requisitos
- Python 3.7+
- Flask

### Paso 1: Clonar y Preparar

```bash
# Clonar repositorio
git clone https://github.com/Gabo-araya/do-ob.games.git
cd do-ob.games

# Verificar Python
python3 --version  # Debe ser 3.10+

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate
```

### Paso 2: Instalar Dependencias

```bash
# Actualizar pip
pip install --upgrade pip

# Instalar dependencias del proyecto
pip install -r requirements.txt

```

## Lanzar el servidor
```bash
cd server
python app.py
```

El servidor estará disponible en: http://localhost:5000

## Despliegue con Podman

Estas instrucciones son para desplegar la aplicación en un servidor Ubuntu con Podman.

### 1. Instalar Podman

```bash
sudo apt-get update
sudo apt-get -y install podman
```

### 2. Instalar Podman Compose

`podman-compose` se puede instalar usando `pip`.

```bash
sudo apt-get -y install python3-pip
pip install podman-compose
```

### 3. Construir y correr la aplicación

Desde el directorio raíz del proyecto, donde se encuentra el archivo `compose.yaml`, ejecuta el siguiente comando:

```bash
podman-compose up -d
```

La aplicación estará disponible en el puerto 5500 de tu servidor.

Para detener la aplicación, ejecuta:

```bash
podman-compose down
```

## Endpoints disponibles

### GET /
Lista todos los juegos disponibles
```json
{
  "games": ["snake", "tetris", "pong", ...]
}
```

### GET /games/<game_name>
Sirve el archivo HTML del juego especificado

### POST /analytics/event
Endpoint para tracking de eventos de juego

## Base de datos
- Se crea automáticamente `analytics.db` en el directorio server
- Tablas: `game_events` y `game_stats`

## Build de juegos
Para empaquetar todos los juegos en archivos HTML únicos:
```bash
cd server
python build.py
```

Los archivos empaquetados se guardan en el directorio `dist/`

## Estructura de archivos
```
server/
├── app.py              # Servidor Flask principal
├── database.py         # Manejo de base de datos SQLite
├── build.py            # Script para empaquetar juegos
├── requirements.txt    # Dependencias Python
└── analytics.db        # Base de datos (se crea automáticamente)
```