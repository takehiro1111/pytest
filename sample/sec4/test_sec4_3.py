# fixtureを使ってクラスに対する前処理＆後処理
import pytest

# scopeはフィクスチャ関数が実行される粒度を指定
# classに対する処理の場合は必要。
# デフォルトはscope="function"と暗黙的に設定されている。
@pytest.fixture(scope="class") 
def setup_processing(request):
    print("setup_processing")
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)

class TestExample():
    def test_example1(self, setup_processing):
        print("hello world!")

    def test_example2(self, setup_processing):
        print("pytest!")
