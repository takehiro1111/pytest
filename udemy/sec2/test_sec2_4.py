# メソッドのテスト
# クラス名の先頭にTestを書く必要がある。
# メソッドは関数同様にtest_が先頭に必要。
    # エラーは出ないが、テスト対象から外れる。
class TestExample():
    def test_example1(self):
        assert True

    def test_example2(self):
        assert True
