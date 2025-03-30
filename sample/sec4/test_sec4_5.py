import pytest

# 前処理＆後処理の定義
# autouse -> テスト対象のメソッドや関数の引数に前処理を追加しなくても自動的に前処理が実行される。
# 全てのテストに前処理、後処理を加えたい場合に設定しておくのが良い。
@pytest.fixture(autouse=True) # デフォルトはFalse
def setup_processing(request):
    print("setup_processing")
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)

class TestExample():
    def test_hello(self, setup_processing):
        print("hello")

    def test_goodmorning(self):
        print("goodmorning")

    def test_goodafternoon(self):
        print("goodafternoon")
