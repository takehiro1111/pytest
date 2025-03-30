# モジュールに対する前処理＆後処理
# 前処理
def setup_module(module):
    print("setup_module")

# 後処理
def teardown_module(module):
    print("teardown_module")
    
def setup_function(function):
    print("setup_function")

# テストの後処理(以下のテスト用関数の実行が先)
def teardown_function(function):
    print("teardown_function")

def test_hello_world():
    print("hello world!")

def test_pytest():
    print("pytest")

class TestExample():
    # 前処理
    @classmethod
    def setup_class(cls):
        print("setup_class")

    # 後処理
    @classmethod
    def teardown_class(cls):
        print("teardown_class")
        
        # 前処理の実行
    def setup_method(self, method):
        print("setup_method")

    # 後処理の実行
    def teardown_method(self, method):
        print("teardown_method")
        
    def test_hello_world(self):
        print("hello world!")

    def test_pytest(self):
        print("pytest")
