import pytest

@pytest.fixture()
def setup_processing(request):
    print("\nsetup_processing")
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)

class TestExample():
    def test_hello(self, setup_processing):
        print("hello")

    def test_goodmorning(self):
        print("goodmorning")

    def test_goodafternoon(self, setup_processing):
        print("goodafternoon")
