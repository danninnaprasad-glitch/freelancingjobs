@echo off
echo Starting Daily Job Update...
python scraper.py
python cleanup.py
echo Daily update completed!
pause
