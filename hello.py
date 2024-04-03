from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='HelloWorld API',
          description='A helloworld API',
          )


@api.route('/hello/<name>')
@api.doc(params={'name': 'Your name'})
class HelloWorld(Resource):
    def get(self, name):
        return {'message': "hello, " + name}

    @api.response(403, 'Not Authorized')
    def post(self, name):
        api.abort(403)
