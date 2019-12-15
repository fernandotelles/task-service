from config import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False)
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Task (id=%r, description=%r, state=%r, user_id=%r)>' \
                % (self.id, self.description, self.state, self.user_id)