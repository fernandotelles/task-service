from config import app
from flask_restful import Api
from src.services.task_service import TaskList

api = Api(app)

api.add_resource(TaskList, '/v1/tasks/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')