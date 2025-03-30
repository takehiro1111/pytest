# 例外処理の実行
from translator import GoogleTranslator
import pytest

def test_convert(mocker):
    mock_obj = mocker.patch("translator.GoogleTranslator.get_language_id")
    mock_obj.side_effect = KeyError("ConvertException(Free Name)")
    
    with pytest.raises(KeyError) as e:
        trans = GoogleTranslator()
        text_translated = trans.convert("私の名前は佐藤です。", "日本語", "ポルトガル語")
        print(text_translated)
    
    print(e.value.args[0])
