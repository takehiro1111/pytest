# fixtureの利用
import pytest

@pytest.fixture()
# setup_processingとしてるが、任意の名称で良い。
def setup_processing(request):
    print("\nsetup_processing")
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)

def test_hello(setup_processing):
    print("hello")

def test_goodmorning():
    print("goodmorning")

def test_goodafternoon(setup_processing):
    print("goodafternoon")
