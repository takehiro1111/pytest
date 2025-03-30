# テスト関数に様々なデータを渡してテストを実行
from translator import GoogleTranslator
import pytest

# テストで使用したいデータ
input_data = [
    ("私の名前は佐藤です。","日本語","英語", "My name is Sato."),
    ("こんにちは","日本語","英語", "Hello"),
    ("おはよう","日本語","英語", "good morning")
]

# 前処理の設定
@pytest.fixture(scope="module")
def trans():
    t = GoogleTranslator()
    print("create Translator")
    return t

# fixtureの後に記述する必要がある。
@pytest.mark.parametrize("input_a, input_b, input_c, input_d", input_data)

def test_convert(input_a, input_b, input_c, input_d, trans):
    print(f"input_a:{input_a}")
    print(f"input_b:{input_b}")
    print(f"input_c:{input_c}")
    print(f"input_d:{input_d}")

    text_translated = trans.convert(input_a, input_b, input_c)
    assert text_translated == input_d
