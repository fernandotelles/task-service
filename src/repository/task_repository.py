from config import db
from src.models.task import Task

class TaskRepository:

    def all(self):
        return Task.query.all()

    def get_by_id(self, task_id):
        task = Task.query.filter_by(id=task_id).first()
        return task

    def update(self, a_task):
        task = self.get_by_id(a_task['id'])
        task.description = a_task['description']
        task.state = a_task['state']
        task.user_id = a_task['user_id']
        db.session.commit()