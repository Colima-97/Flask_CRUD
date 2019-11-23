from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo desde Flask'

@app.route('/home')
def home():
    return "<html><head><title>Mi Primer Página</title></head><body><h1>Hola mundo</h1></body></html>"

@app.route('/personaldata')
def personaldata():
    name = "Carlos Alejandro Figueroa Bazán"
    age = 22
    subject = ["Inteligencia Artificial", "Programación", "Redes de computadoras"]
    return render_template('personaldata.html', name = name, age = age, subject = subject)

if __name__ == '__main__':
    app.run()