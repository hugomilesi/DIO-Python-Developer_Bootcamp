from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, ListaHabilidades
import json
app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'rafael',
        'habilidades': ['Python', 'Flask']
     },
    {
        'id': '1',
        'nome': 'Anne',
        'habilidades': ['Vendas', 'Música']}
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'Erro', 'Mensagem': 'Desenvolvedor Não encontrado na database.'}
        except Exception:
            response = {'status': 'Erro', 'Mensagem': 'Erro Desconhecido.'}
        return response

    def put(self, id):
        dados = json.loads(request.data)  # pega a tabela json que foi inserida dentro do postman
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'Sucesso', 'mensagem': 'Registro Excluido'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


# controle de classes e rotas
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/<int:id>')
api.add_resource(ListaHabilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug = True)
