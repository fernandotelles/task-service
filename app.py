from config import app
from flask_restful import Resource, Api

api = Api(app)

class TaskService(Resource):
    def get(self):
        return '', 200
    
api.add_resource(TaskService, '/v1/tasks/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')