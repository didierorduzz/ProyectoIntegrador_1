@echo off
echo.
echo Cerrando Flask y desactivando el entorno virtual...
echo.

:: Este comando detiene Flask si lo dejaste corriendo con Ctrl+C
echo Si el servidor Flask sigue corriendo, presiona Ctrl+C en la ventana anterior.

:: Desactiva el entorno (solo necesario si estás aún en la terminal activa)
call venv\Scripts\deactivate.bat

pause