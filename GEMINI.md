# GEMINI.md - Games Project

## Project Overview

This project is a web application that serves a collection of classic arcade games. The backend is a Python Flask server that provides a landing page with links to the games and serves the game files. The frontend consists of several single-page games, each implemented in vanilla JavaScript with embedded CSS.

The main technologies used are:
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript (Canvas API)
- **Database:** SQLite for analytics

The project is structured with each game in its own directory, and a central `server` directory for the Flask application.

## Building and Running

### 1. Setup the environment

It is recommended to use a virtual environment to install the dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

### 2. Install dependencies

Install the required Python packages using pip:

```bash
pip install -r server/requirements.txt
```

### 3. Run the server

To start the Flask server, run the following command:

```bash
python server/app.py
```

The server will be available at `http://localhost:5500`.

## Development Conventions

The following development conventions are used in this project, as described in `CRUSH.md`:

- **Code Style:**
    - Vanilla JavaScript is preferred for simplicity.
    - Each game is a single HTML file with embedded CSS and JavaScript.
    - Mobile-first responsive design.
    - Touch and keyboard controls.
    - Canvas API for graphics.
- **Naming Conventions:**
    - `camelCase` for JavaScript variables and functions.
    - `kebab-case` for file names.
    - `UPPERCASE` for constants.
- **Error Handling:**
    - Use `try/catch` blocks for game logic.
    - Provide clear error messages for debugging.
- **Performance:**
    - Efficient Canvas rendering.
    - Minimal DOM manipulation.
    - Use `requestAnimationFrame` for smooth animations.
