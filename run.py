from app import create_app

# Crear la aplicación
app = create_app()

if __name__ == '__main__':
    # Ejecutar la app
    app.run('0.0.0.0', 5200, debug=True)
