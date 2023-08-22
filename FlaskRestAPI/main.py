import requests
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

#using variables
@app.route('/<int:id>')
def my_api(id):
    return jsonify({'id': id, 'nome': 'Rafael', 'profissao': 'Cientista de Dados'})


# Sending multiples numbers for sum
@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10+10
    return jsonify({'soma':total})





# Extrair elementos ou modificar tabelas ['GET', 'POST']
desenvolvedores = [
    {'nome': 'Hugo',
     'habilidades': ['Python', 'Pandas', 'Flask']
     },
    {'nome': 'Anne',
     'habilidades': ['Vendas', 'Música']}
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):

    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'Erro', 'Mensagem': 'Desenvolvedor Não encontrado na database.'}
        except Exception:
            response = {'status': 'Erro', 'Mensagem': 'Erro Desconhecido.'}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)  # pega a tabela json que foi inserida dentro do postman.
        print('Valor dentro de dados: ', dados)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'Sucesso', 'mensagem': 'Registro Excluido'})

# Registrar Desenvolvedores
@app.route('/dev/', methods = ['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        print(dados)
        desenvolvedores.append(dados)
        return jsonify({'Status':'Sucesso', 'Mensagem': 'Registro Inserido.'})
    if request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)

