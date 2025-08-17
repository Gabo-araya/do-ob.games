# Guía de Despliegue en Servidor VPS con Podman

Esta guía detalla los pasos para desplegar la aplicación de juegos en un servidor VPS de Hostinger (o similar) utilizando Podman como motor de contenedores.

**Dominio de ejemplo:** `games.do-ob.cl`

## Paso 1: Configuración del Servidor VPS

1.  **Accede a tu VPS:**
    Conéctate a tu servidor a través de SSH.
    ```bash
    ssh usuario@tu_direccion_ip
    ```

2.  **Actualiza tu sistema:**
    ```bash
    sudo dnf update -y  # Para AlmaLinux/CentOS/Fedora
    # sudo apt update && sudo apt upgrade -y # Para Debian/Ubuntu
    ```

3.  **Instala las herramientas necesarias (Git y Podman):**
    ```bash
    sudo dnf install -y git podman
    # sudo apt install -y git podman # Para Debian/Ubuntu
    ```
    
4.  **Instala `podman-compose`:**
    Esto facilitará la gestión del contenedor definido en `compose.yaml`.
    ```bash
    sudo dnf install -y python3-pip
    pip3 install --user podman-compose
    ```
    Asegúrate de que `~/.local/bin` esté en tu `PATH`. Agrégalo a tu `.bashrc` o `.zshrc`:
    ```bash
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```

## Paso 2: Configuración del DNS

En tu proveedor de dominio (donde registraste `do-ob.cl`), crea un registro **A** para el subdominio `games` que apunte a la dirección IP de tu servidor VPS.

- **Tipo:** A
- **Nombre/Host:** games
- **Valor/Apuntando a:** (La IP de tu VPS)

## Paso 3: Despliegue de la Aplicación

1.  **Clona el repositorio del proyecto:**
    ```bash
    git clone https://github.com/Gabo-araya/do-ob.games.git
    cd do-ob.games
    ```

2.  **Construye la imagen y levanta el contenedor:**
    Usa `podman-compose` para leer el archivo `compose.yaml` y gestionar el contenedor.
    ```bash
    podman-compose up -d --build
    ```
    - `--build`: Construye la imagen a partir del `Dockerfile` la primera vez.
    - `-d`: Ejecuta el contenedor en modo "detached" (en segundo plano).

3.  **Verifica que el contenedor esté en ejecución:**
    ```bash
    podman ps
    ```
    Deberías ver un contenedor llamado `do-ob-games-container` en estado "Up". También puedes revisar los logs:
    ```bash
    podman logs do-ob-games-container
    ```

En este punto, la aplicación ya está corriendo en el puerto `5500` de tu servidor. Sin embargo, no es accesible públicamente a través del dominio ni usa HTTPS. Para ello, necesitas un reverse proxy.

## Paso 4: Configuración de un Reverse Proxy (Caddy)

Usaremos **Caddy** porque es extremadamente fácil de configurar y gestiona automáticamente los certificados SSL/TLS de Let's Encrypt.

1.  **Instala Caddy:**
    Sigue las instrucciones oficiales para tu sistema operativo en [caddyserver.com](https://caddyserver.com/docs/install). Para AlmaLinux 8:
    ```bash
    sudo dnf install 'dnf-command(copr)'
    sudo dnf copr enable @caddy/caddy
    sudo dnf install caddy
    ```

2.  **Configura Caddy:**
    Edita el archivo de configuración de Caddy:
    ```bash
    sudo nano /etc/caddy/Caddyfile
    ```
    Reemplaza todo el contenido con lo siguiente, sustituyendo `games.do-ob.cl` por tu dominio:
    ```
    games.do-ob.cl {
        # Habilita la compresión para un mejor rendimiento
        encode gzip

        # Redirige el tráfico del dominio al puerto donde corre la app
        reverse_proxy localhost:5500
    }
    ```

3.  **Inicia y habilita el servicio de Caddy:**
    ```bash
    sudo systemctl enable --now caddy
    ```
    Caddy se iniciará automáticamente, obtendrá un certificado SSL para `games.do-ob.cl` y redirigirá todo el tráfico de forma segura a tu aplicación en el contenedor.

¡Listo! Ahora deberías poder acceder a tu aplicación en `https://games.do-ob.cl`.

## Mantenimiento y Actualizaciones

Para actualizar la aplicación con los últimos cambios del repositorio de Git:

1.  **Detén el contenedor actual:**
    ```bash
    cd do-ob.games
    podman-compose down
    ```

2.  **Actualiza el código fuente:**
    ```bash
    git pull origin main  # O la rama que corresponda
    ```

3.  **Vuelve a construir y levantar el servicio:**
    ```bash
    podman-compose up -d --build
    ```
