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
