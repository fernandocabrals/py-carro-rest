from flask import Flask
from flask_restful import Api
from carro import Carros, Carro

app = Flask(__name__)
api = Api(app)

api.add_resource(Carros, '/carros/')
api.add_resource(Carro, '/carros/<int:codigo>')

if __name__ == '__main__':
    app.run()