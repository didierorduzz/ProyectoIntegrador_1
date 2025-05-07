# 🎓 Sistema de Préstamo de Salas Audiovisuales

Aplicación web desarrollada con **Flask + OracleDB** para gestionar reservas de salas audiovisuales y de cómputo en entornos académicos. Administradores pueden gestionar el sistema y docentes realizar solicitudes de préstamo.

---

## 📦 Requisitos

- Python 3.10 o superior
- Oracle Database XE y Oracle Instant Client
- Conexión configurada correctamente en `db.py`
- Entorno virtual (`venv/`) creado y activado

---

## 🔧 Tecnologías utilizadas

- Python 3
- Flask 3.1.0
- HTML, CSS, JavaScript
- Oracle SQL (para las tablas y consultas)
- OracleDB (oracledb 3.1.0)
- HTML5 + CSS3
- Visual Studio Code
- Git y GitHub

## 👥 Tipos de usuario

- **Administrador**: accede al panel completo (dashboard, usuarios, reportes).
- **Profesor**: accede directamente al formulario de solicitud de préstamo.

## 🧪 Funcionalidades
Inicio de sesión con roles (profesor, administrador)

Registro de nuevos usuarios con validación

Dashboard de administración

Solicitud de préstamo para docentes

Manejo de sesiones y autenticación básica

## 📌 Notas Adicionales
El archivo .env puede usarse para guardar variables sensibles como credenciales de la base de datos (no incluido en este repo).
Asegúrate de que las tablas necesarias estén creadas en OracleDB antes de ejecutar el sistema.

## ⚙️ Instalación y ejecución

### 🔹 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/ProyectoIntegrador_1.git
cd Prueba proyecto 1

# Crear archivo y entorno virtual
python -m venv venv
venv\Scripts\activate   # En Windows
source venv/bin/activate  # En Linux/Mac
## En cmd
venv\Scripts\activate

## Instalar dependencias
pip install -r requirements.txt
## Manualmente
pip install flask oracledb

## Comandos de actualizacion en git
git add .
git status
git commit -m "Mensaje descriptivo"
git push origin main

## Ejecutar app
python app.py
http://localhost:5000

## Scripts de ayuda
| Archivo | Función |
|--------|---------|
| `activar_venv.bat` | Activa solo el entorno virtual |
| `iniciar_app.bat` | Activa entorno y ejecuta la app |
| `detener_app.bat` | Te recuerda cerrar Flask y desactiva entorno |

## Regenerar dependencias
pip freeze > requirements.txt
## En otro equipo
pip install -r requirements.txt

## Gitignore
venv/
__pycache__/
*.pyc
.vscode/
*.db
.env

## Ejecutar setup
@sql/setup.sql

### Autor
Didier Orduz – UDI
[Uso académico]
