from flask import Blueprint, render_template, request, redirect, url_for, flash

main = Blueprint('main', __name__, template_folder='../../templates', static_folder='../../static')

# @main.route('/')
# def index():
#     cur = mysql.connection.cursor()
#     cur.execute("""
#         SELECT u.id, u.name, u.email, r.name AS rol, e.nombre AS enfasis
#         FROM users u
#         INNER JOIN roles r ON u.role = r.id
#         INNER JOIN enfasis e ON u.enfasis_id = e.id
#     """)
#     users = cur.fetchall()

#     cur.execute("SELECT id, nombre FROM enfasis")
#     enfasis = cur.fetchall()
#     cur.close()

#     return render_template('index.html', users=users, enfasis=enfasis)

# from MySQLdb import IntegrityError

# @main.route('/add', methods=['POST'])
# def add_user():
#     name = request.form["name"]
#     email = request.form["email"]
#     role = request.form["rol"]
#     enfasis_id = request.form['enfasis']

#     try:
#         cur = mysql.connection.cursor()
#         cur.execute(
#             "INSERT INTO users(name, email, role, enfasis_id) VALUES(%s, %s, %s, %s)",
#             (name, email, role, enfasis_id)
#         )
#         mysql.connection.commit()
#         cur.close()

#         flash('Usuario agregado correctamente', 'success')
#     except IntegrityError:
#         flash('El correo ya está registrado. Usa uno diferente.', 'danger')

#     return redirect(url_for('main.index'))


# @main.route('/delete/<int:id>', methods=['POST'])
# def delete_user(id):
#     cur = mysql.connection.cursor()
#     cur.execute("DELETE FROM users WHERE id=%s", (id,))
#     mysql.connection.commit()
#     cur.close()

#     flash('Usuario eliminado correctamente', 'success')
#     return redirect(url_for('main.index'))


# @main.route('/edit/<int:id>', methods=['GET', 'POST'])
# def edit_user(id):
#     cur = mysql.connection.cursor()

#     if request.method == 'POST':
#         name = request.form["name"]
#         email = request.form["email"]
#         role = request.form["rol"]        # este es el id del rol que llega del select
#         enfasis_id = request.form['enfasis']

#         # Verificar si email existe en otro usuario
#         cur.execute("SELECT id FROM users WHERE email = %s AND id != %s", (email, id))
#         existing_user = cur.fetchone()

#         if existing_user:
#             flash('El correo ya está registrado en otro usuario. Usa uno diferente.', 'danger')
#         else:
#             try:
#                 cur.execute(
#                     "UPDATE users SET name=%s, email=%s, role=%s, enfasis_id=%s WHERE id=%s",
#                     (name, email, role, enfasis_id, id)
#                 )
#                 mysql.connection.commit()
#                 flash('Usuario actualizado correctamente', 'success')
#                 cur.close()
#                 return redirect(url_for('main.index'))
#             except Exception as e:
#                 flash('Error al actualizar el usuario: ' + str(e), 'danger')

#     # Para GET: Obtener datos del usuario para llenar el formulario
#     cur.execute("SELECT id, name, email, role, enfasis_id FROM users WHERE id = %s", (id,))
#     user = cur.fetchone()

#     # También trae lista de énfasis para el select
#     cur.execute("SELECT id, nombre FROM enfasis")
#     enfasis = cur.fetchall()

#     cur.close()
#     return render_template('edit_user.html', user=user, roles=role, enfasis=enfasis)

# @main.route('/register')
# def register():
#     return render_template('register.html')