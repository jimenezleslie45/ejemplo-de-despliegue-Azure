from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>¡Bienvenido a mi App Automatizada leslie Garcia!</h1><p>Despliegue inicial exitoso.</p>'

if __name__ == '__main__':
    app.run()