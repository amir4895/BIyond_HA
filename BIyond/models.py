from BIyond import db
from datetime import datetime


class File(db.Model):
    filename = db.Column(db.String(120), primary_key=True, unique=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<file {} last update {}>'.format(self.filename, self.date)


class Heartbeat(db.Model):
    date = db.Column(db.DateTime, primary_key=True, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.date)


class TimeoutRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_list = db.Column(db.String(120))

    def __repr__(self):
        return '<TimeoutRequests {}>'.format(self.id)


