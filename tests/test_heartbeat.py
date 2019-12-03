import pytest
from BIyond import db
from BIyond.models import Heartbeat
from time import sleep


def test_heartbeat():
    """
    test check basic heartbeat mechanism

    :return: assert on fail
    """
    first_sample = db.session.query(Heartbeat).count()
    sleep(11)  # in order to validate Heartbeat
    second_sample = db.session.query(Heartbeat).count()
    assert first_sample <= second_sample
