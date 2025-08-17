# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
# Copiamos el directorio del servidor y todos los directorios de los juegos
COPY server/ /app/server/
COPY breakout/ /app/breakout/
COPY flappy-bird/ /app/flappy-bird/
COPY frogger/ /app/frogger/
COPY memory-match/ /app/memory-match/
COPY pacman/ /app/pacman/
COPY pong/ /app/pong/
COPY snake/ /app/snake/
COPY space-invaders/ /app/space-invaders/
COPY tetris/ /app/tetris/
COPY whack-a-mole/ /app/whack-a-mole/
COPY analytics.db /app/analytics.db

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r server/requirements.txt

# Exponer el puerto en el que se ejecuta la aplicación
EXPOSE 5500

# Comando para ejecutar la aplicación
CMD ["python", "server/app.py"]