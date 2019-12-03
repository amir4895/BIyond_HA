import requests
from tests.tests_functions import generate_files
from BIyond.models import File
from BIyond import db
from time import sleep


def test_no_file_duplication(server_url):
    """
    :param server_url: pytest fixture with post address
    :return: assert on fail
    """
    files = generate_files(number_of_files=5, length=5)
    data = {"filenames": files}
    post_status = requests.post(url=server_url, json=data)
    sleep(10)  # should be max timeout (40)
    assert post_status.status_code == 202
    number_of_files_first_insert = db.session.query(File).count()
    post_status = requests.post(url=server_url, json=data)
    assert post_status.status_code == 202
    number_of_files_second_insert = db.session.query(File).count()
    sleep(10)  # should be max timeout (40)
    assert number_of_files_first_insert == number_of_files_second_insert

    # insert new batch of files and validate change in file table

    files = generate_files(number_of_files=5, length=5)
    data = {"filenames": files}
    post_status = requests.post(url=server_url, json=data)
    assert post_status.status_code == 202
    number_of_files_third_insert = db.session.query(File).count()
    sleep(10)  # should be max timeout (40)
    assert number_of_files_third_insert != number_of_files_second_insert
