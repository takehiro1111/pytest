# テストのスキップ
import pytest

@pytest.mark.hello
def test_hello():
    print("hello")

@pytest.mark.morning
def test_goodmorning():
    print("goodmorning")

@pytest.mark.afternoon(reason="test-reason")
def test_goodafternoon():
    print("goodafternoon")
