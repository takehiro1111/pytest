# 前処理＆後処理の関数の作成
# テストの前処理
def setup_function(function):
    print("setup_function")

# テストの後処理(以下のテスト用関数の実行が先)
def teardown_function(function):
    print("teardown_function")

def test_hello_world():
    print("hello world!")

def test_pytest():
    print("pytest")
