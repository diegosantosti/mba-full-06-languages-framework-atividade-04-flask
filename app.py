from flask import Flask , request

app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello World"

@app.route("/calcular-imc" , methods=['POST'])
def calcularImc():
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        imc = round(peso / altura ** 2,2)
        resultado = calculateDescription(imc)

        print(peso)
        print(altura)
        print(imc)
        print(resultado)

        description = "Peso: " + str(peso) + "Altura: " + str(altura) + "IMC: " + str(imc) + "Resultado: " + resultado
        return description

def calculateDescription(imc):
        description = 'Obesidade'
        if imc < 18.5: description = 'Magreza'
        elif imc < 24.9: description = 'Normal'
        elif imc < 30: description = 'Sobrepeso'
        return description


app.run(host='localhost',port=8080, debug=True)
