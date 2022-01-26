import pytest

"""тест"""
class Class_Test:

    def test_dz2_Str1_test(self):
        a = "Py"
        b = "thon"
        assert a + b == "Python"

    def test_dz2_Str2_test(self):
        a = "Py"
        assert a in "Python"

    def test_dz2_Str3_test(self):
        a = "2"
        assert int(a) == 2

    def test_dz2_Str4_test(self):
        a = "abc"
        b = "rtg"
        assert len(a+b) == 6

    @pytest.mark.parametrize ("a, b, c", [("run", "test", "fumble"), ("roll","tor","fresh")])
    def test_firsts_Str5_test(self, a, b, c):
        assert a[0] + b[0] + c[0] == "rtf"