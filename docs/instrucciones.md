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



## Instalación
```bash
pip install flask
```

## Lanzar el servidor
```bash
cd server
python app.py
```

El servidor estará disponible en: http://localhost:5000

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
├── app.py          # Servidor Flask principal
├── database.py     # Manejo de base de datos SQLite
├── build.py        # Script para empaquetar juegos
└── analytics.db    # Base de datos (se crea automáticamente)
```
