from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from supporting_code.security import authenticate, identity
from supporting_code.user import UserRegister
from supporting_code.item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'chris'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/student/Chris
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)