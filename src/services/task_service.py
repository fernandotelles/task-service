from flask_restful import Resource, fields, marshal_with
from src.repository.task_repository import TaskRepository

repository = TaskRepository()

task_fields = {
    'id': fields.String,
    'description': fields.String,
    'state': fields.String,
    'user_id': fields.String
}

class TaskList(Resource):
    @marshal_with(task_fields)
    def get(self):
        tasks = repository.all()
        return tasks, 200
