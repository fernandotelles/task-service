from config import db
from src.models.task import Task

class TaskRepository:

    def all(self):
        return Task.query.all()