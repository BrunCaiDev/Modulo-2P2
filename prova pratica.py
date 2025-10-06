from flask import Flask, request, render_template
import json


# parte do json incompleta pq eu nn lembro e nem tenho consulta suficiente pra conseguir fazer, perdão kkkk
ARQUIVO = "prova pratica.json"

# with open(ARQUIVO, "a+") as arquivo:
#     arquivo.seek(0)
#     try:
#         json.load(arquivo)
#     except:
        # arquivo.write("[]")

# ------------------------------------


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/soma/valor1=<int:n1>/valor2=<int:n2>")
def soma(n1,n2):

    return f'Resultado da soma entre {n1} e {n2} = {n1 + n2}'


@app.route('/subtrair/valor1=<int:n1>/valor2=<int:n2>') 
def subtracao(n1,n2):
    
    return f'Resultado da subtração entre {n1} e {n2} = {n1 - n2}'



@app.route('/multiplicar/valor1=<int:n1>/valor2=<int:n2>') 
def multiplicacao(n1,n2):
    
    return f'Resultado da multiplicação entre {n1} e {n2} = {n1 * n2}'



@app.route('/divisao/valor1=<int:n1>/valor2=<int:n2>') 
def divisao(n1,n2):
   
    if n1 == 0:     
        return f'Esta invalido'
    else:
        return f'Resultado da divisão entre {n1} e {n2} = {n1 / n2}'



if __name__ == "__main__":
    app.run(debug=True)

