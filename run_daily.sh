#!/bin/bash
echo "Starting Daily Job Update..."
python3 scraper.py
python3 cleanup.py
echo "Daily update completed!"
