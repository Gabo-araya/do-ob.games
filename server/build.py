#!/usr/bin/env python3
"""
Script para empaquetar juegos en un solo archivo HTML descargable.
Combina HTML, CSS y JavaScript en un archivo único.
"""

import os
import re
import base64
from pathlib import Path

def inline_css(html_content, game_dir):
    """Inline CSS files into HTML"""
    def replace_css(match):
        css_file = match.group(1)
        css_path = Path(game_dir) / css_file
        if css_path.exists():
            with open(css_path, 'r') as f:
                return f"<style>\n{f.read()}\n</style>"
        return match.group(0)
    
    return re.sub(r'<link[^>]*href="([^"]*\.css)"[^>]*>', replace_css, html_content)

def inline_js(html_content, game_dir):
    """Inline JavaScript files into HTML"""
    def replace_js(match):
        js_file = match.group(1)
        js_path = Path(game_dir) / js_file
        if js_path.exists():
            with open(js_path, 'r') as f:
                return f"<script>\n{f.read()}\n</script>"
        return match.group(0)
    
    return re.sub(r'<script[^>]*src="([^"]*\.js)"[^>]*>', replace_js, html_content)

def inline_images(html_content, game_dir):
    """Inline images as base64 data URLs"""
    def replace_img(match):
        img_file = match.group(1)
        img_path = Path(game_dir) / img_file
        if img_path.exists():
            with open(img_path, 'rb') as f:
                img_data = f.read()
                ext = img_path.suffix[1:]  # Remove the dot
                data_uri = f"data:image/{ext};base64,{base64.b64encode(img_data).decode()}"
                return f'<img src="{data_uri}"'
        return match.group(0)
    
    return re.sub(r'<img[^>]*src="([^"]*)"', replace_img, html_content)

def package_game(game_name):
    """Empaqueta un juego en un solo archivo HTML"""
    game_dir = Path(game_name)
    index_path = game_dir / 'index.html'
    
    if not index_path.exists():
        print(f"No se encontró index.html en {game_name}")
        return None
    
    with open(index_path, 'r') as f:
        content = f.read()
    
    # Procesar inlining
    content = inline_css(content, game_dir)
    content = inline_js(content, game_dir)
    content = inline_images(content, game_dir)
    
    # Asegurar que el HTML es válido
    if not content.strip().startswith('<!DOCTYPE html>'):
        content = '<!DOCTYPE html>\n' + content
    
    return content

def package_all_games():
    """Empaqueta todos los juegos"""
    games = [d for d in os.listdir('.') if os.path.isdir(d) and d not in ['docs', 'server']]
    
    for game in games:
        print(f"Empaquetando {game}...")
        packaged = package_game(game)
        if packaged:
            output_path = Path('dist') / f'{game}.html'
            output_path.parent.mkdir(exist_ok=True)
            
            with open(output_path, 'w') as f:
                f.write(packaged)
            
            print(f"  Guardado en {output_path}")
        else:
            print(f"  Error al empaquetar {game}")

if __name__ == '__main__':
    package_all_games()