from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class TaskService(Resource):
    def get(self):
        return {'hello': 'tasks'}

api.add_resource(TaskService, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')