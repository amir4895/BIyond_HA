import requests
from tests.tests_functions import generate_files
from BIyond import app


def test_sanity(server_url):
    files = generate_files(number_of_files=5, length=5)
    data = {"filenames": files}
    post_status = requests.post(url=server_url, json=data)
    assert post_status.status_code == 202
    post_status = requests.post(url=server_url, json={})
    assert post_status.status_code == 400
