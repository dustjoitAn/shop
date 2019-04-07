import json

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)



class User(Resource):
    def post(self):
        with open('controller/admin.json', 'r') as outfile:
            admins = json.load(outfile)
        parser = reqparse.RequestParser()
        parser.add_argument("_login")
        parser.add_argument("_password")
        args = parser.parse_args()

        for admin in admins:
            if args["_login"] == admin["_login"] and args["_password"] == admin["_password"]:
                return "Ok", 200
            return "Wrong inputs", 404


api.add_resource(User, "/login")
app.run(debug=True)