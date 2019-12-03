import requests
import pytest
from random import randrange
from tests.tests_functions import generate_files
from tests.test_params import stress_test_params


@pytest.mark.repeat(stress_test_params["stress_repeat"])
def test_stress(server_url):
    """
    test send x (define in test parms) post requests, file name size and number of files defined in tests_params.py

    :param server_url: url for file upload post
    :return: assert on fail
    """
    try:
        random_size = randrange(1, stress_test_params["max_word_size"])
        random_number_of_files = randrange(1, stress_test_params["max_number_of_files"])
        files = generate_files(number_of_files=random_number_of_files, length=random_size)
        data = {"filenames": files}
        response = requests.post(server_url, json=data, timeout=60)
        response.raise_for_status()
        print(f'Sent {random_number_of_files} files response time was {response.elapsed.total_seconds()}')
        return response.elapsed.total_seconds()
    except Exception as e:
        print(f'got an exception {e} \n Data was {data}')
        raise
