from flask_restful import Resource, fields, marshal_with, abort, reqparse
from src.repository.task_repository import TaskRepository

repository = TaskRepository()

task_fields = {
    'id': fields.String,
    'description': fields.String,
    'state': fields.String,
    'user_id': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('task_id', location='json')
parser.add_argument('task_description', location='json')
parser.add_argument('task_state', location='json')
parser.add_argument('task_user_id', location='json')

def abort_if_dont_exists(task_id):
    task = repository.get_by_id(task_id)
    if task == None:
        abort(404, message="Task {} doesn't exist".format(task_id))

def argsToDict(args):
    task = {}
    task['id'] = args['task_id']
    task['description'] = args['task_description']
    task['state'] = args['task_state']
    task['user_id'] = args['task_user_id']
    return task

class TaskList(Resource):
    @marshal_with(task_fields)
    def get(self):
        tasks = repository.all()
        return tasks, 200

class TaskService(Resource):
    def put(self, task_id):
        abort_if_dont_exists(task_id)
        args = parser.parse_args()
        task = argsToDict(args)
        repository.update(task)
        return '', 204
