from flask import Flask
from BIyond.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from BIyond.request_queue import RequestQueueObject
from typing import List

ETL_REQUEST_TIMEOUT = 20

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
db.drop_all()
db.create_all()
migrate = Migrate(app, db)
requests_queue = []  # type: List[RequestQueueObject]




