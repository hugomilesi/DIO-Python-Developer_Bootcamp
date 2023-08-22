from flask_restful import Resource
from flask import request
import json

lista_habilidades = ['Python', 'Data Visualization', 'Flask', 'Tensorflow']

class Habilidades(Resource):
    def get(self, id):
        """Mostra a habilidade especifica no id"""
        try:
            return {'Habilidade escolhida: ' :lista_habilidades[id]}
        except IndexError:
            return {"Error": "id da habilidade não encontrado"}


    def put(self, id):
        """Altera a habilidade escolhida"""
        dados = json.loads(request.data)
        lista_habilidades[id] = dados # troca ovalor do indice especificado
        return dados


    def delete(self, id):
        """Deleta a habilidade escolhida"""
        try:
            lista_habilidades.pop(id)
            return {"Sucesso": f"Habilidade removida"}
        except IndexError:
            return {"Error": "ID não encontrado na lista de habilidades"}


class ListaHabilidades(Resource):
    def get(self):
        """Mostra todas as habilidades"""
        return {"Lista de Habilidades ": lista_habilidades}

    def post(self):
        """Adciona uma nova habilidade"""
        dados = json.loads(request.data)
        lista_habilidades.append(dados)
        return {'Habilidade adicionada': dados}

