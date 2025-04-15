#!/bin/bash

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing required Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Starting CM TruckEst API..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

