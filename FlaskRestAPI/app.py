from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy.orm import sessionmaker
from DataBase.model import Users, Artists

from sqlalchemy import create_engine, MetaData, Table


engine = create_engine("sqlite:///Database/MusicStreaming.db")
Session = sessionmaker(bind=engine)
session = Session()


app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self, nome):
        try:
            user = session.query(Users).filter_by(FirstName=nome).first()
            response = {
                'id': user.UserID,
                'nome': user.FirstName,
                'LastName': user.LastName,
                'Email': user.Email,
                'Address': user.Address
            }
        except AttributeError:
            return {"Error": "Invalid Username"}
        return response


class Artist(Resource):
    def get(self, nome):
        try:
            artist = session.query(Artists).filter_by(Name=nome).first()
            response = {
                #'id': user.UserID,
                'Name': artist.Name,
                'Genre': artist.Genre,
                'Country': artist.Country,
            }
            return response
        except:
            return {"error": "Artist not found"}

    def put(self, nome):
        artist = session.query(Artists).filter_by(Name=nome).first()
        dados = request.json
        if 'Name' in dados:
            artist.Name = dados['Name']
        if 'Genre' in dados:
            artist.Genre = dados['Genre']
        if 'Country' in dados:
            artist.Country = dados['Country']

        response = {
            'Name': artist.Name,
            'Genre': artist.Genre,
            'Country': artist.Country
        }
        return response


    def delete(self, nome):
        artist = session.query(Artists).filter_by(Name=nome).first()
        if artist:
            session.delete(artist)
            #session.commit() i kept this commented for testing purposes
            return{'status': 'Sucesso',
                   'Mensagem': f"Artista {artist.Name} Removido"
                   }
        else:
            return {
                'status': 'Error',
                'message': f"Artist {nome} not found"
            }


class ListArtists(Resource):
    def get(self):
        """Mostra todos os artistas adicionados"""
        artist = session.query(Artists).all()
        response = [{'Name': i.Name, 'Genre': i.Genre, 'Country': i.Country} for i in artist]
        return response

    def post(self):
        dados = request.json
        artist = Artists(Name=dados['Name'], Genre=dados['Genre'], Country=dados['Country'])
        session.add(artist)
        #session.commit()  i kept this commented for testing purposes
        response = {
            'Name': artist.Name,
            'Genre': artist.Genre,
            'Country': artist.Country
        }

        return response


api.add_resource(User,'/user/<string:nome>/')
api.add_resource(Artist,'/artist/<string:nome>/')
api.add_resource(ListArtists, '/artist/')
if __name__ == '__main__':
    app.run(debug=True)
