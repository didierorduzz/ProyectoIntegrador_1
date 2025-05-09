from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
from db import get_connection

app = Flask(__name__)
app.secret_key = 'clave_secreta'

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')
        confirmar = request.form.get('confirmar')
        rol = request.form.get('rol')

        if contrasena != confirmar:
            flash('Las contraseñas no coinciden.', 'error')
            return redirect(url_for('registro'))

        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO usuario (nombre, correo, contraseña, rol)
                    VALUES (:1, :2, :3, :4)
                """, (nombre, correo, contrasena, rol))
                conn.commit()
                flash('Usuario registrado exitosamente. Ahora puedes iniciar sesión.', 'success')
                return redirect(url_for('inicio'))
        except Exception as e:
            print("Error al registrar usuario:", e)
            flash('Error al registrar el usuario.', 'error')
            return redirect(url_for('registro'))
    else:
        return render_template('register.html')


@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT rol FROM usuario WHERE correo = :1 AND contraseña = :2", (usuario, contrasena))
            result = cursor.fetchone()

            if result:
                session['usuario'] = usuario
                rol = result[0]
                flash('Inicio de sesión exitoso.', 'success')
                if rol == 'administrador':
                    return redirect(url_for('dashboard'))
                else:
                    return redirect(url_for('solicitar_prestamo'))
            else:
                flash('Credenciales incorrectas.', 'error')
                return redirect(url_for('inicio'))
    except Exception as e:
        import traceback
        traceback.print_exc()
        flash('Error en el inicio de sesión.', 'error')
        return redirect(url_for('inicio'))
    
@app.route('/recuperar-contrasena', methods=['GET', 'POST'])
def recuperar_contrasena():
    if request.method == 'POST':
        correo = request.form.get('correo')
        # Aquí podrías buscar en la base de datos y enviar un correo, por ahora simulamos:
        flash(f'Si el correo {correo} está registrado, recibirás instrucciones pronto.', 'success')
        return redirect(url_for('inicio'))

    return render_template('recuperar_contrasena.html')

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        flash('Debes iniciar sesión primero.', 'error')
        return redirect(url_for('inicio'))

    vista = request.args.get('vista', 'prestamos')

    datos = []
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            if vista == 'prestamos':
                cursor.execute("""
                    SELECT sala_solicitada, hora_prestamo, 
                        TO_CHAR(fecha_solicitud, 'YYYY-MM-DD'), observaciones, edificio
                    FROM prestamosala
                    ORDER BY fecha_solicitud DESC, hora_prestamo DESC
                """)
                datos = cursor.fetchall()
            elif vista == 'usuarios':
                cursor.execute("SELECT nombre, correo, rol FROM usuario ORDER BY nombre")
                datos = cursor.fetchall()
            elif vista == 'reportes':
                cursor.execute("""
                    SELECT usuario, sala, TO_CHAR(fecha_reporte, 'YYYY-MM-DD'), descripcion
                    FROM reportes
                    ORDER BY fecha_reporte DESC
                """)
                datos = cursor.fetchall()
            elif vista == 'crear_profesor':
                datos = []  # Puedes cargar algo si deseas mostrar profesores creados
    except Exception as e:
        print("Error en dashboard:", e)
        flash("No se pudieron cargar los datos.", "error")

    return render_template('dashboard.html', vista=vista, datos=datos)

@app.route('/agregar-profesor', methods=['POST'])
def agregar_profesor():
    correo = request.form.get('correo')
    if not correo:
        flash("Debes ingresar un correo.", "error")
        return redirect(url_for('dashboard', vista='usuarios'))

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO profesores_autorizados (correo) VALUES (:1)", (correo,))
            conn.commit()
            flash("Correo de profesor registrado exitosamente.", "success")
    except Exception as e:
        print("Error al agregar profesor:", e)
        flash("Hubo un error al registrar el profesor.", "error")

    return redirect(url_for('dashboard', vista='usuarios'))

@app.route('/prestamo')
def solicitar_prestamo():
    if 'usuario' not in session:
        flash('Debes iniciar sesión primero.', 'error')
        return redirect(url_for('inicio'))
    return render_template('prestamo.html')

@app.route('/solicitar', methods=['POST'])
def solicitar():
    sala = request.form.get('sala')
    edificio = request.form.get('edificio')
    hora = request.form.get('hora')
    fecha = request.form.get('fecha')
    observaciones = request.form.get('observaciones')

    if not sala or not hora or not fecha:
        flash("Todos los campos son obligatorios.", "error")
        return redirect(url_for('solicitar_prestamo'))

    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            # Verifica si ya existe una reserva para esa fecha, hora y sala
            cursor.execute("""
                SELECT COUNT(*) FROM prestamosala
                WHERE sala_solicitada = :1 AND hora_prestamo = :2 AND fecha_solicitud = TO_DATE(:3, 'YYYY-MM-DD')
            """, (sala, hora, fecha))
            count = cursor.fetchone()[0]

            if count > 0:
                flash("La sala ya está reservada para esa fecha y hora.", "error")
                return redirect(url_for('solicitar_prestamo'))

            # Inserta nueva solicitud
            cursor.execute("SELECT correo FROM usuario WHERE correo = :1", (session['usuario'],))
            usuario_id = cursor.fetchone()[0]

            cursor.execute("""
            INSERT INTO prestamosala (sala_solicitada, hora_prestamo, fecha_solicitud, observaciones, edificio)
            VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5)
            """, (sala, hora, fecha, observaciones, usuario_id, edificio))
            conn.commit()
            flash("Solicitud registrada exitosamente.", "success")
    except Exception as e:
        print("Error al guardar en Oracle:", e)
        flash("Hubo un error al registrar la solicitud.", "error")

    return redirect(url_for('solicitar_prestamo'))

@app.route('/usuarios')
def ver_usuarios():
    if 'usuario' not in session:
        flash('Inicia sesión primero.', 'error')
        return redirect(url_for('inicio'))

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, correo, rol FROM usuario ORDER BY nombre")
            usuarios = cursor.fetchall()
    except Exception as e:
        print("Error al cargar usuarios:", e)
        usuarios = []
        flash('Error al mostrar usuarios.', 'error')

    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Has cerrado sesión exitosamente.', 'success')
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)