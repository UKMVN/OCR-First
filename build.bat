@echo off
pyinstaller --noconfirm  --onefile --console --add-data "models;models/" "run.py"