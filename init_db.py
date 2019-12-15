from config import db
from src.models.task import Task

if __name__ == '__main__':
    db.create_all()
    db.session.add(Task(description="wash cars", state=0, user_id=1))
    db.session.add(Task(description="wash clothes", state=1, user_id=1))
    db.session.add(Task(description="run", state=1, user_id=1))
    db.session.add(Task(description="wash cars", state=0, user_id=2))
    db.session.add(Task(description="run", state=1, user_id=2))
    db.session.commit()