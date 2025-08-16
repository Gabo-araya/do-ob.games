import sqlite3
import json
from datetime import datetime

class AnalyticsDB:
    def __init__(self, db_path='analytics.db'):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Inicializa la base de datos"""
        with sqlite3.connect(self.db_path) as conn:
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
            conn.execute('''
                CREATE TABLE IF NOT EXISTS game_stats (
                    game_name TEXT PRIMARY KEY,
                    play_count INTEGER DEFAULT 0,
                    win_count INTEGER DEFAULT 0,
                    avg_duration REAL DEFAULT 0
                )
            ''')
            conn.commit()
    
    def track_event(self, game_name, event_type, user_agent=None, session_id=None):
        """Registra un evento de juego"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO game_events 
                (game_name, event_type, user_agent, session_id)
                VALUES (?, ?, ?, ?)
            ''', (game_name, event_type, user_agent, session_id))
            conn.commit()
    
    def update_game_stats(self, game_name, won=False, duration=0):
        """Actualiza las estadísticas de un juego"""
        with sqlite3.connect(self.db_path) as conn:
            # Crear entrada si no existe
            conn.execute('''
                INSERT OR IGNORE INTO game_stats (game_name) VALUES (?)
            ''', (game_name,))
            
            # Actualizar estadísticas
            if duration > 0:
                conn.execute('''
                    UPDATE game_stats 
                    SET play_count = play_count + 1,
                        win_count = win_count + ?,
                        avg_duration = ((avg_duration * play_count) + ?) / (play_count + 1)
                    WHERE game_name = ?
                ''', (1 if won else 0, duration, game_name))
            else:
                conn.execute('''
                    UPDATE game_stats 
                    SET play_count = play_count + 1,
                        win_count = win_count + ?
                    WHERE game_name = ?
                ''', (1 if won else 0, game_name))
            
            conn.commit()
    
    def get_game_stats(self, game_name):
        """Obtiene las estadísticas de un juego"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT * FROM game_stats WHERE game_name = ?
            ''', (game_name,))
            return cursor.fetchone()
    
    def get_all_stats(self):
        """Obtiene estadísticas de todos los juegos"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT * FROM game_stats ORDER BY play_count DESC
            ''')
            return cursor.fetchall()

# Para pruebas
if __name__ == '__main__':
    db = AnalyticsDB()
    print("Base de datos inicializada")