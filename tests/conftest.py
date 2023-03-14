import pytest
from dotenv import load_dotenv

from framework.demo_qa import DemoQaWithEnv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="prod")


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def reqres(env):
    return DemoQaWithEnv(env).reqres
