#!/bin/bash

# Digital Clock App Runner Script
# This script activates the virtual environment and runs the digital clock app

set -e  # Exit on any error

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "🕐 Starting Digital Clock App..."

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "⚠️  Virtual environment not found. Creating one..."
    python3 -m venv .venv
    echo "✅ Virtual environment created."
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source .venv/bin/activate

# Install requirements if they exist and packages aren't installed
if [ -f "requirements.txt" ]; then
    echo "📦 Installing/checking requirements..."
    pip install -q -r requirements.txt
fi

# Run the application
echo "🚀 Launching Digital Clock..."
python digital_clock_app.py

echo "👋 Digital Clock app closed."