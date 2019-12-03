import pytest
from .test_params import generic_tests_params


@pytest.fixture(scope="session", autouse=True)
def server_url():
    return generic_tests_params["api_end_point"]+generic_tests_params["post_file_route"]
