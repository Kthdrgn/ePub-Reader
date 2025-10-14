#!/bin/bash

# EPUB Reader PWA - Quick Setup Script
# This script helps you get started quickly

echo "📚 EPUB Reader PWA - Setup"
echo "=========================="
echo ""

# Check if icons exist
if [ ! -f "icon-192.png" ] || [ ! -f "icon-512.png" ]; then
    echo "⚠️  Icons not found!"
    echo "Please create icons:"
    echo "1. Open create-icons.html in a browser"
    echo "2. Download both icon files"
    echo "3. Place them in this directory"
    echo ""
fi

# Function to detect OS and suggest server
start_server() {
    echo "🚀 Starting local server..."
    echo ""
    
    # Try Python 3
    if command -v python3 &> /dev/null; then
        echo "✅ Using Python 3"
        echo "🌐 Open: http://localhost:8000"
        echo ""
        python3 -m http.server 8000
        return
    fi
    
    # Try Python 2
    if command -v python &> /dev/null; then
        echo "✅ Using Python 2"
        echo "🌐 Open: http://localhost:8000"
        echo ""
        python -m SimpleHTTPServer 8000
        return
    fi
    
    # Try PHP
    if command -v php &> /dev/null; then
        echo "✅ Using PHP"
        echo "🌐 Open: http://localhost:8000"
        echo ""
        php -S localhost:8000
        return
    fi
    
    # Try Node.js serve
    if command -v npx &> /dev/null; then
        echo "✅ Using npx serve"
        echo "🌐 URL will be shown below"
        echo ""
        npx serve
        return
    fi
    
    echo "❌ No server found!"
    echo ""
    echo "Please install one of the following:"
    echo "  • Python: https://python.org"
    echo "  • Node.js: https://nodejs.org (includes npx)"
    echo "  • PHP: https://php.net"
    echo ""
    echo "Or deploy to:"
    echo "  • GitHub Pages (free)"
    echo "  • Netlify (free)"
    echo "  • Vercel (free)"
    echo ""
}

# Main menu
echo "Choose an option:"
echo "1. Start local server"
echo "2. View deployment instructions"
echo "3. Exit"
echo ""
read -p "Enter choice [1-3]: " choice

case $choice in
    1)
        start_server
        ;;
    2)
        echo ""
        echo "📦 Deployment Options:"
        echo ""
        echo "GitHub Pages:"
        echo "  git init"
        echo "  git add ."
        echo "  git commit -m 'Initial commit'"
        echo "  git remote add origin YOUR_REPO_URL"
        echo "  git push -u origin main"
        echo "  Then enable Pages in repo settings"
        echo ""
        echo "Netlify:"
        echo "  1. Go to netlify.com"
        echo "  2. Drag and drop this folder"
        echo "  3. Done!"
        echo ""
        echo "Vercel:"
        echo "  npm i -g vercel"
        echo "  vercel"
        echo ""
        ;;
    3)
        echo "Goodbye! 👋"
        exit 0
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac
