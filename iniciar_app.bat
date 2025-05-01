@echo off
cd /d "C:\Users\Usuario\Documents\Prueba proyecto 1"

:: Activar entorno virtual
call venv\Scripts\activate.bat

:: Ejecutar aplicación Flask
python app.py

:: (Opcional) abrir el navegador automáticamente
start http://localhost:5000

pause