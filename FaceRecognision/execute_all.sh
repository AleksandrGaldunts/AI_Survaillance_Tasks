#!/bin/bash

set -e

cleanup() {
    echo "Script interrupted. Stopping further execution."
    exit 1
}

trap cleanup SIGINT
ARGUMENT="$1"


echo "Running capturing_10_photos.py with argument..."
python3 capturing_10_photos.py "$ARGUMENT"

echo "Running organizing_in_folders.py..."
python3 organizing_in_folders.py

echo "Running detect_faces.py..."
python3 detect_faces.py

echo "Running recognise_faces.py..."
python3 recognise_faces.py

echo "All modules executed successfully."
