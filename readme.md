python -m venv venv
venv\Scripts\activate
venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt

para correr desde la terminal del server
$env:FLASK_ENV="development"
.\venv\Scripts\gunicorn.exe --bind 0.0.0.0:5502 --workers 3 --timeout 120 --log-level info wsgi:application

para correr desde la terminal local en Windows:
python wsgi.py

y

app.run(host="0.0.0.0", port=5502, debug=debug) en la función main