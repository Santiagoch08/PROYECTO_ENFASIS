from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.Rol import Rol
from app.models.Usuario import Usuario

rol_bp = Blueprint('rol', __name__, url_prefix='/rol')

# Listar roles
@rol_bp.route('/')
def list_roles():
    roles = Rol.query.order_by(Rol.nombre).all()
    return render_template('roles.html', roles=roles)

# Agregar rol
@rol_bp.route('/add', methods=['POST'])
def add_rol():
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')

    if not nombre:
        flash('El nombre del rol es obligatorio', 'error')
        return redirect(url_for('rol.list_roles'))

    if Rol.query.filter_by(nombre=nombre).first():
        flash('Ya existe un rol con ese nombre', 'error')
        return redirect(url_for('rol.list_roles'))

    nuevo_rol = Rol(nombre=nombre, descripcion=descripcion)
    db.session.add(nuevo_rol)
    db.session.commit()
    flash('Rol agregado correctamente', 'success')
    return redirect(url_for('rol.list_roles'))

# Editar rol
@rol_bp.route('/edit/<int:id>', methods=['POST'])
def edit_rol(id):
    rol = Rol.query.get_or_404(id)
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')

    if not nombre:
        flash('El nombre del rol es obligatorio', 'error')
        return redirect(url_for('rol.list_roles'))

    rol.nombre = nombre
    rol.descripcion = descripcion
    db.session.commit()
    flash('Rol actualizado correctamente', 'success')
    return redirect(url_for('rol.list_roles'))

# Eliminar rol (reasignando usuarios al rol por defecto)
@rol_bp.route('/delete/<int:id>', methods=['POST'])
def delete_rol(id):
    rol = Rol.query.get_or_404(id)

    # Obtener rol por defecto
    default_rol = Rol.query.filter_by(nombre='Sin rol').first()
    if not default_rol:
        default_rol = Rol(nombre='Sin rol', descripcion='Rol por defecto')
        db.session.add(default_rol)
        db.session.commit()

    # Reasignar usuarios al rol por defecto
    for user in rol.users:
        user.role = default_rol.id

    db.session.delete(rol)
    db.session.commit()
    flash('Rol eliminado y usuarios reasignados al rol por defecto', 'success')
    return redirect(url_for('rol.list_roles'))
