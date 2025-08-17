# DO-OB Games

Este proyecto es una aplicación web que sirve una colección de juegos arcade clásicos. El backend es un servidor Flask de Python que proporciona una página de destino con enlaces a los juegos y sirve los archivos del juego. El frontend consta de varios juegos de una sola página, cada uno implementado en JavaScript vanilla con CSS incrustado.

**Repositorio de GitHub:** [https://github.com/Gabo-araya/do-ob.games](https://github.com/Gabo-araya/do-ob.games)

## Juegos Incluidos

- Breakout
- Flappy Bird
- Frogger
- Memory Match
- Pacman
- Pong
- Snake
- Space Invaders
- Tetris
- Whack-a-Mole

## Tecnologías Utilizadas

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript (Canvas API)
- **Base de Datos:** SQLite para analíticas
- **Despliegue:** Podman, Caddy (Recomendado)

## Configuración y Ejecución Local

### 1. Configurar el entorno

```bash
# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r server/requirements.txt
```

### 3. Ejecutar el servidor

```bash
python server/app.py
```

El servidor estará disponible en `http://localhost:5500`.

## Despliegue en Servidor (VPS con Podman)

Esta aplicación está configurada para un despliegue sencillo usando contenedores Podman. Se incluye un `Dockerfile` y un archivo `compose.yaml` para facilitar el proceso.

### Prerrequisitos

- Un servidor VPS (ej. Hostinger) con acceso root/sudo.
- **Podman** y **git** instalados en el VPS.
- Un dominio o subdominio (ej. `games.do-ob.cl`) apuntando a la IP de tu VPS.

### Pasos para el Despliegue

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Gabo-araya/do-ob.games.git
    cd do-ob.games
    ```

2.  **Construir y ejecutar con Podman Compose:**
    ```bash
    podman-compose up -d --build
    ```

3.  **Configurar un Reverse Proxy (Recomendado):**
    Para manejar HTTPS y acceder a la aplicación a través de tu dominio, se recomienda usar un reverse proxy como Caddy o Nginx.

Para instrucciones detalladas, incluyendo la configuración del reverse proxy, consulta el archivo [docs/server-instrucciones.md](docs/server-instrucciones.md).

## Estructura del Proyecto
```
/
├── breakout/
├── ... (más juegos)
├── server/
│   ├── app.py
│   └── templates/
│       └── index.html
├── compose.yaml
├── Dockerfile
└── README.md
```