import pytest

from rocksteady.data import DATA
from rocksteady.steady_rocking import Villain


@pytest.fixture()
def lunchbox():
    yield 20


@pytest.fixture(scope="session")
def large_load(request):
    yield 10 * request.param


@pytest.fixture
def add_key3():
    DATA["DATA1"]["key3"] = 20
    yield DATA
    del DATA["DATA1"]["key3"]


@pytest.fixture
def villain_factory():
    def _make_villain(name, health):
        return Villain(name, health)

    yield _make_villain
