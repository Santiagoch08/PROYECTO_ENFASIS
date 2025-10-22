from app import create_app

app = create_app()
app.secret_key = "mysecretkey"  # Asignar la clave antes de correr el servidor

if __name__ == '__main__':
    app.run('0.0.0.0', 5200, debug=True)
