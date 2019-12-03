from BIyond import db
from datetime import datetime


class File(db.Model):
    """
    ORM class for File table in SQLite via SQLAlchemy


    filename - the full_path for file
    date - upload time , if file was reloaded will set the new time
    """

    filename = db.Column(db.String(120), primary_key=True, unique=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<file {self.filename} last update {self.date}>'


class Heartbeat(db.Model):
    """
    ORM class for Heartbeat table in SQLite via SQLAlchemy

    date - Heartbeat time
    """
    date = db.Column(db.DateTime, primary_key=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Heartbeat {self.date}>'


class TimeoutRequests(db.Model):

    """
    ORM class for TimeoutRequests table in SQLite via SQLAlchemy

    id  - timout index
    file_list -  the files paths that was sent in the original request
    """

    id = db.Column(db.Integer, primary_key=True)
    file_list = db.Column(db.String(120))

    def __repr__(self):
        return f'<TimeoutRequests {self.id}>'


