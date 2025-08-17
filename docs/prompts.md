# Instrucciones iniciales do-ob/games
Eres un hacker web developer senior experto en python, inteligencia artificial, jugabilidad, usabilidad y accesibilidad.
Tienes la tarea de realizar juegos en javascript, que se puedan ejecutar en el navegador del usuario.
Los juegos deben ser jugables tanto en desktop como en móviles.

## 10 juegos simples y entretenidos para móviles y desktop:
1. Snake
2. Tetris
3. Flappy Bird
4. Memory Match
5. Whack-a-Mole
6. Pong
7. Pacman
8. Space Invaders
9. Frogger
10. Breakout

## Sugerencias y decisiones:
1. Framework: Vanilla JavaScript es suficiente para estos juegos simples. No necesitamos frameworks pesados.
2. Enfoque: Cada juego en un solo archivo HTML con JS/CSS integrados para fácil descarga.
3. Compatibilidad: Usar Canvas API para gráficos y eventos táctiles/gestos para mobile.
4. Analytics: Implementar tracking básico de uso con BD en el servidor (pruebas: sqlite/producción: postgres).
5. Servidor: Flask para servir juegos y manejar la API de analytics.
6. Estructura: Directorio por juego con index.html y assets necesarios.
7. Build: Script para empaquetar cada juego en un solo HTML descargable.
8. DB: SQLite para pruebas y PostgreSQL para producción.
9. Testing: Pruebas manuales en múltiples dispositivos y navegadores.
10. Deployment: Podman para fácil deployment del servidor Flask en un VPS.



# Prompts para do-ob/games

Genera una lista de 10 juegos simples en Vanilla JavaScript.
Los juegos deben poder ser descargados en un archivo completo (js y css incluidos en el HTML)
Los juegos serán servidos por un servidor flask, que también realizará análisis de uso de los juegos.
Guarda la información en el archivo 'xat'_timestamp.md

---

Lee instrucciones.md y genera un plan de implementación en formato md en 'docs/'.

---

Lee docs/plan.md y comienza con la fase 1

---

Crea instrucciones de cómo lanzar el servidor en 'docs/instrucciones.md'
Genera un plan de implementación del primer juego en 'snake/readme.md'

---

Comienza con la creación del primer juego: Snake.
Genera instrucciones para el juego (en archivo md y en el juego).

---

Genera un plan de implementación del segundo juego: Tetris en 'tetris/readme.md'.
Comienza con la creación del juego.
Genera instrucciones para el juego (en archivo md y en el juego)

---

Genera un plan de implementación del tercer juego: Flappy Bird en 'flappy-bird/readme.md'.
Comienza con la creación del juego.
Genera instrucciones para el juego (en archivo md y en el juego)

---

Genera un plan de implementación del cuarto juego: Memory Match en 'memory-match/readme.md'
Comienza con la creación del juego.
Genera instrucciones para el juego (en archivo md y en el juego)

---

Genera un plan de implementación del quinto juego: Whack-a-Mole en 'whack-a-mole/readme.md'
Comienza con la creación del juego.
Genera instrucciones para el juego (en archivo md y en el juego)

---


Genera un plan de implementación del sexto juego: Pong en 'pong/readme.md'
Comienza con la creación del juego.
Genera instrucciones para el juego (en archivo md y en el juego)

---


Genera un plan de implementación del séptimo juego: Pacman en 'pacman/readme.md'
Comienza con la creación del juego.
Genera instrucciones para el juego (en archivo md y en el juego)

---


Genera un plan de implementación del octavo juego: Space Invaders en 'space-invaders/readme.md'
Comienza con la creación del juego.
Genera instrucciones para el juego (en archivo md y en el juego)

---


Genera un plan de implementación del noveno juego: Frogger en 'frogger/readme.md'
Comienza con la creación del juego.
Genera instrucciones para el juego (en archivo md y en el juego)

---


Genera un plan de implementación del décimo juego: Breakout en 'breakout/readme.md'
Comienza con la creación del juego.
Genera instrucciones para el juego (en archivo md y en el juego)

---

revisa la app flask y crea un landing page con accesos a cada juego.

---

mejora el estilo de la landing de la app flask que sea un diseño profesional, inspirando en cyberpunk, que tenga una descripción e instrucciones de cada juego, con un espacio para imagen representativa de cada juego (la pondré después).

---

modifica el proyecto para que sea desplegable usando podman en un vps en un ubuntu

---

GEMINI 2.5 flash

vamos a cargar esta app a un VPS que tiene contenedores podman y un nginx entremedio. existe otro subdominio llamado maca.do-ob.cl con un flask y otro flask corriendo en www.do-ob.cl. quiero que me des los pasos para poder identificar las redes podman, los contenedores existentes y los volúmenes asociados y también las ubicaciones de las configuraciones de los subdominios de nginx


---

ya existe un Dockerfile en el proyecto. Recuerda que los contenedores son podman. me conviene tener diferentes redes para los contenedores? no usan servicios comunes. el resultado del comando:
gabo@srv949717:~$ cat /home/gabo/apps/nginx/conf.d/do-ob.cl.conf



---


cat <<'EOF' > /home/gabo/apps/nginx/conf.d/games.do-ob.cl.conf
 Bloque 1: Configuración HTTP para games.do-ob.cl (para retos de Certbot)
server {
    listen 80;
    server_name games.do-ob.cl;

    # Esta sección es importante para que Certbot pueda verificar tu dominio.
    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }
    # Una vez que tengas SSL, todo el tráfico será redirigido a HTTPS.
    location / {
        return 301 https://$host$request_uri;
    }
}
# Bloque 2: Configuración principal para games.do-ob.cl con SSL/TLS (HTTPS)
# Nota: Este bloque no funcionará hasta que generes el certificado SSL.
server {
   listen 443 ssl http2;
   server_name games.do-ob.cl;
   # IMPORTANTE: Debes generar un certificado para games.do-ob.cl
   # La ruta probablemente será la siguiente:
   ssl_certificate /etc/letsencrypt/live/games.do-ob.cl/fullchain.pem;
   ssl_certificate_key /etc/letsencrypt/live/games.do-ob.cl/privkey.pem;
   # Incluir opciones de SSL recomendadas
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        # Apunta al nombre del contenedor de la app de juegos y su puerto
        proxy_pass http://games-app:5500;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
EOF


---



---



---



---


---
