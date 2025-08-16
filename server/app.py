from flask import Flask, send_from_directory, jsonify
import os
import sqlite3

app = Flask(__name__)

# Configuración de la base de datos
DATABASE = 'analytics.db'

def init_db():
    """Inicializa la base de datos SQLite para analytics"""
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS game_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                game_name TEXT NOT NULL,
                event_type TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                user_agent TEXT,
                session_id TEXT
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    """Página principal que lista todos los juegos"""
    games = [d for d in os.listdir('.') if os.path.isdir(d) and d not in ['docs', 'server']]
    return jsonify({"games": games})

@app.route('/games/<game_name>')
def serve_game(game_name):
    """Sirve un juego específico"""
    if os.path.exists(f'{game_name}/index.html'):
        return send_from_directory(game_name, 'index.html')
    return jsonify({"error": "Game not found"}), 404

@app.route('/analytics/event', methods=['POST'])
def track_event():
    """Endpoint para tracking de eventos de juego"""
    # Implementar tracking de eventos
    return jsonify({"status": "tracked"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5500)
