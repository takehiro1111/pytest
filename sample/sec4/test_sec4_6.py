# テストのスキップ
import pytest

def test_hello():
    print("\nhello")

# テストしたいが、まだ実装が追いついていなくて部分的にテストしたくないものに設定する。
# 設定するとこの部分だけテストをスキップできる。
@pytest.mark.skip(reason="write reason")
def test_goodmorning():
    print("goodmorning")

def test_goodafternonn():
    print("goodafternoon")
