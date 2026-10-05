#!/bin/bash
# live_preview.sh - Start Sphinx autobuild with live reload
# Usage: ./live_preview.sh

PROJECT_DIR="$HOME/Documents/VSCodiumFiles/LatticeLang"

cd "$PROJECT_DIR" || { echo "❌ Project directory not found"; exit 1; }

# Verify Poetry environment exists
echo "🔍 Locating Poetry environment..."
VENV_PATH=$(poetry env info --path 2>/dev/null)

if [ -z "$VENV_PATH" ]; then
    echo "❌ No Poetry environment found. Run 'poetry install --extras docs' first."
    exit 1
fi

echo "✅ Using: $(basename "$VENV_PATH")"
echo ""
echo "📚 Starting Sphinx autobuild..."
echo "   Open your browser to: http://127.0.0.1:8000"
echo "   Press Ctrl+C to stop."
echo ""

poetry run sphinx-autobuild docs/source docs/_build/html --host 127.0.0.1