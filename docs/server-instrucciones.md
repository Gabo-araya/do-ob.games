# Instrucciones del Servidor

## Requisitos
- Python 3.7+
- Flask

## Instalación
```bash
cd server
pip install -r requirements.txt
```

O instalar manualmente:
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
├── app.py              # Servidor Flask principal
├── database.py         # Manejo de base de datos SQLite
├── build.py            # Script para empaquetar juegos
├── requirements.txt    # Dependencias Python
└── analytics.db        # Base de datos (se crea automáticamente)
```