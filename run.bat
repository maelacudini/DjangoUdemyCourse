@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\activate.bat" (
    echo Could not find .venv\Scripts\activate.bat.
    echo Create the virtual environment first with: python -m venv .venv
    pause
    exit /b 1
)

call ".venv\Scripts\activate.bat"
python manage.py runserver
