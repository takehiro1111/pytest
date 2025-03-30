# テストのスキップ
# pytest {ファイル名} -k "hello" 
# pytest {ファイル名} -k "not hello" 
# 関数名の指定で特定の関数のテストをスキップしたり実行できる。
def test_hello1():
    print("hello1")

def test_hello2():
    print("hello2")

def test_afternoon1():
    print("afternoon1")
