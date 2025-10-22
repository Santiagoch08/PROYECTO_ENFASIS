from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import mysql
from MySQLdb._exceptions import IntegrityError

emphasis = Blueprint('emphasis', __name__, template_folder='../../templates', static_folder='../../static')


# Mostrar las cartas de los énfasis
@emphasis.route('/enfasis')
def enfasis():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM enfasis")
    data = cur.fetchall()
    cur.close()
    return render_template('/enfasis/enfasis.html', enfasis=data)


# Mostrar usuarios de un énfasis
@emphasis.route('/enfasis/<int:id>', methods=['GET'])
def users_enfasis(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE enfasis_id = %s ORDER BY name ASC", (id,))
    users = cur.fetchall()
    cur.execute("SELECT nombre FROM enfasis WHERE id=%s", (id,))
    enfasis_nombre = cur.fetchone()[0]
    cur.close()
    return render_template('/enfasis/crud_enfasis.html', users=users, enfasis_nombre=enfasis_nombre, enfasis_id=id)


# Agregar énfasis (solo en add_enfasis.html)
@emphasis.route('/add_enfasis', methods=['GET', 'POST'])
def add_enfasis():
    cur = mysql.connection.cursor()

    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        try:
            cur.execute("INSERT INTO enfasis (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
            mysql.connection.commit()
            flash('Énfasis agregado correctamente', 'success')
        except IntegrityError:
            flash('Ese énfasis ya existe. Intenta con otro nombre.', 'danger')
        cur.close()
        return redirect(url_for('emphasis.enfasis'))

    cur.execute("SELECT * FROM enfasis")
    data = cur.fetchall()
    cur.close()
    return render_template('/enfasis/add_enfasis.html', enfasis=data)


# Editar usuario
@emphasis.route('/edit_user/<int:id>', methods=['POST'])
def edit_user(id):
    nombre = request.form['nombre']
    email = request.form['email']

    try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (nombre, email, id))
        mysql.connection.commit()
        cur.close()
        flash('Usuario actualizado correctamente', 'success')
    except IntegrityError:
        flash('Error al actualizar el usuario', 'danger')

    cur = mysql.connection.cursor()
    cur.execute("SELECT enfasis_id FROM users WHERE id=%s", (id,))
    enfasis_id = cur.fetchone()[0]
    cur.close()
    return redirect(url_for('emphasis.users_enfasis', id=enfasis_id))


# Eliminar usuario
@emphasis.route('/delete_user/<int:id>', methods=['POST'])
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT enfasis_id FROM users WHERE id=%s", (id,))
    enfasis_id = cur.fetchone()[0]

    cur.execute("DELETE FROM users WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()

    flash('Usuario eliminado correctamente', 'success')
    return redirect(url_for('emphasis.users_enfasis', id=enfasis_id))
