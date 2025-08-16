# CRUSH.md - Games Project

## Commands
- Build: `npm run build` (when package.json exists)
- Lint: `npm run lint` (when package.json exists)
- Test: `npm test` (when package.json exists)
- Single test: `npm test -- --testNamePattern="test_name"`

## Code Style
- Vanilla JavaScript preferred for simplicity
- Single HTML file per game with embedded CSS/JS
- Mobile-first responsive design
- Touch and keyboard controls
- Canvas API for graphics
- localStorage for local analytics
- SQLite for server-side storage

## Project Structure
- Each game in its own directory
- Games served by Flask server
- Analytics synced to SQLite DB
- Downloadable single HTML files

## Naming Conventions
- camelCase for JS variables/functions
- kebab-case for file names
- UPPERCASE for constants

## Error Handling
- Try/catch blocks for game logic
- Graceful degradation for unsupported features
- Clear error messages for debugging

## Performance
- Efficient Canvas rendering
- Minimal DOM manipulation
- RequestAnimationFrame for smooth animations