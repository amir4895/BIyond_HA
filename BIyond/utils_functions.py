import timeout_decorator
from datetime import datetime

from random import randrange
from BIyond import db, requests_queue, ETL_REQUEST_TIMEOUT
from BIyond.models import Heartbeat, TimeoutRequests, File
from timeout_decorator.timeout_decorator import TimeoutError as decTimeout
from sqlalchemy.sql import exists


def send_heartbeat():
    new_heartbeat = Heartbeat()
    db.session.add(new_heartbeat)
    db.session.commit()


def monitor_timout_events():
    for request_obj in requests_queue:
        try:
            request = request_obj.future_ps
            data = request_obj.data
            if request.done() and not request.result():
                requests_queue.remove(request_obj)
        except decTimeout:
            requests_queue.remove(request_obj)
            update_db_with_new_timeout_request(files=str(data))


def update_db_with_new_timeout_request(files="empty_string"):
    new_timeout_request = TimeoutRequests(file_list=files)
    db.session.add(new_timeout_request)
    db.session.commit()


@timeout_decorator.timeout(ETL_REQUEST_TIMEOUT, use_signals=False)
def analyze_json(file_names_list, is_corrupt):
    num_files_in_request = len(file_names_list)-1
    if not num_files_in_request:
        return
    corrupted_index = None
    if is_corrupt:
        corrupted_index = randrange(num_files_in_request)

    for idx, file in enumerate(file_names_list):
        if is_corrupt and idx == corrupted_index:
            continue
        else:
            is_exists = db.session.query(exists().where(File.filename == file)).scalar()
            if is_exists:
                existing_file = File.query.filter_by(filename=file).first()
                existing_file.date = datetime.utcnow()
            else:
                new_file = File(filename=file)
                db.session.add(new_file)
    db.session.commit()


