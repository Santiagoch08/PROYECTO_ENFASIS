from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db

from app.models.Enfasis import Enfasis
from app.models.Usuario import Usuario

emphasis = Blueprint('emphasis', __name__,
                     template_folder='../../templates',
                     static_folder='../../static')

# Mostrar todos los énfasis
@emphasis.route('/enfasis')
def enfasis():
    enfasis_list = Enfasis.query.order_by(Enfasis.nombre.asc()).all()
    return render_template('/enfasis/enfasis.html', enfasis=enfasis_list)

# Lista de usuarios de un énfasis específico
@emphasis.route('/enfasis/<int:id>')
def users_enfasis(id):
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM users u WHERE u.enfasis_id = %s ORDER BY u.name ASC", (id,))
    # data = cur.fetchall()
    # cur.close()
    users = Usuario.query.filter_by(enfasis_id=id).order_by(Usuario.name.asc()).all()
    return render_template('/enfasis/crud_enfasis.html', users=users)

# # Crear nuevo énfasis
@emphasis.route('/add_enfasis', methods=['GET', 'POST'])
def add_enfasis():
    # cur = mysql.connection.cursor()
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        new_enfasis = Enfasis(nombre=nombre, descripcion=descripcion)
        try:
            db.session.add(new_enfasis)
            db.session.commit()
            flash('Énfasis agregado correctamente', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error al agregar el énfasis: {}'.format(str(e)), 'danger')

    enfasis_list = Enfasis.query.order_by(Enfasis.nombre.asc()).all()
    data = enfasis_list
    return render_template('/enfasis/add_enfasis.html', enfasis=data)

# Editar énfasis
@emphasis.route('/edit_enfasis/<int:id>', methods=['POST'])
def edit_enfasis(id):
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    enfasis = Enfasis.query.get(id)
    enfasis.nombre = nombre
    enfasis.descripcion = descripcion
    try:
        db.session.commit()
        flash('Énfasis actualizado correctamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error al actualizar el énfasis: {}'.format(str(e)), 'danger')
    return redirect(url_for('emphasis.add_enfasis'))

# Eliminar énfasis
@emphasis.route('/delete_enfasis/<int:id>', methods=['POST'])
def delete_enfasis(id):
    enfasis = Enfasis.query.get(id)
    try:
        db.session.delete(enfasis)
        db.session.commit()
        flash('Énfasis eliminado correctamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error al eliminar el énfasis: {}'.format(str(e)), 'danger')
    return redirect(url_for('emphasis.add_enfasis'))
