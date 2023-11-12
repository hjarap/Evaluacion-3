from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        if nota1 > 7.0 or nota2 > 7.0 or nota3 > 7.0:
            return "Error: Las notas no pueden ser mayores que 7.0"

        promedio = (nota1 + nota2 + nota3) / 3
        estado = 'Aprobado' if promedio >= 4.0 and asistencia >= 75 else 'Reprobado'

        return render_template('resultado1.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')

# Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        max_nombre = max(nombres, key=len)
        longitud_max = len(max_nombre)

        return render_template('resultado2.html', max_nombre=max_nombre, longitud_max=longitud_max)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)