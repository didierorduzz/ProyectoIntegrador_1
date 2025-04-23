from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Necesaria para flash y sesión

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']
    
    if usuario == 'admin' and contrasena == '1234':
        session['usuario'] = usuario
        flash('Inicio de sesión exitoso.', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Credenciales incorrectas. Inténtalo de nuevo.', 'error')
        return redirect(url_for('inicio'))

@app.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return render_template('dashboard.html')
    else:
        flash('Debes iniciar sesión primero.', 'error')
        return redirect(url_for('inicio'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Has cerrado sesión exitosamente.', 'success')
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)