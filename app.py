from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/nivel_basico')
def nivel_basico():
    return render_template('nivel_basico.html')


@app.route('/nivel_intermedio')
def nivel_intermedio():
    return render_template('nivel_intermedio.html')


@app.route('/nivel_avanzado')
def nivel_avanzado():
    return render_template('nivel_avanzado.html')


@app.route('/conceptos_reforzar')
def conceptos_reforzar():
    return render_template('conceptos_reforzar.html')


if __name__ == '__main__':
    # Ejecuta en modo debug localmente
    app.run(host='127.0.0.1', port=5000, debug=True)
