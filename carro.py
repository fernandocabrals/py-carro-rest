import os
from flask import json, request
from flask_restful import Resource

filedb = os.path.join('./', 'data', 'carrodb.json')

class Carros(Resource):
    def get(self):
        with open(filedb) as carrodb:
            return json.load(carrodb)

    def post(self):
        carro = request.get_json()
        with open(filedb) as carrodb:
            listaCarros = json.load(carrodb)
            listaCarros.append(carro)
        with open(filedb, "w") as carrodbrw:
            json.dump(listaCarros, carrodbrw)
        return 'OK'


class Carro(Resource):
    def get(self, codigo):
        with open(filedb) as carrodb:
            listaCarros = json.load(carrodb)
            for carro in listaCarros:
                if carro['codigo'] == codigo:
                    return carro
            return "BOCA MOLE!!"

    def put(self, codigo):
        carro_req = request.get_json()
        with open(filedb) as carrodb:
            listaCarros = json.load(carrodb)
            for carro in listaCarros:
                if carro['codigo'] == codigo:
                    carro_tmp = carro
                    listaCarros.remove(carro)
                    if 'marca' in carro_req:
                        carro_tmp['marca'] = carro_req['marca']
                    if 'modelo' in carro_req:
                        carro_tmp['modelo'] = carro_req['modelo']
                    if 'preco' in carro_req:
                        carro_tmp['preco'] = carro_req['preco']
                    listaCarros.append(carro_tmp)
        with open(filedb, 'w') as carrodbrw:
            json.dump(listaCarros, carrodbrw)
            return 'OK'
