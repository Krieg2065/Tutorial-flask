from flask import Flask , request, jsonify, Response
from flask_restful import Resource , Api ,reqparse
from flask_cors import CORS
from bson import json_util
import pandas as pd

from flask_pymongo import PyMongo

app = Flask(__name__ )

app.config["MONGO_URI"] = "link al tuo database"

mongo = PyMongo(app)

CORS(app)
api = Api(app)


#-------------------------------------------------------------------------------------------------------------------Prova

class UsersApi(Resource):
    def get(self):
        uss = mongo.db.Prova1.find()
        resp = json_util.dumps(uss)
        return Response(resp, mimetype = 'application/json') 
    def post(self):
        user = request.json["user"]
        informatica = request.json["informatica"]
        matematica = request.json["matematica"]
        arte = request.json["arte"]
        if user and informatica and matematica and arte:
            id = mongo.db.Prova1.insert_one(
                {
                'user': user,
                'informatica': informatica,
                'matematica': matematica,
                'arte': arte 
                }
            )
            resp = {
                "id" : str(id),
                'user': user,
                'informatica': informatica,
                'matematica': matematica,
                'arte': arte 
            }
            return resp
        else:
            return {'message': 'received'}

api.add_resource(UsersApi, '/users')



if __name__ == '__main__':
    app.run()