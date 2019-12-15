from flask_restful import Resource

class TaskList(Resource):
    def get(self):
        return '', 200