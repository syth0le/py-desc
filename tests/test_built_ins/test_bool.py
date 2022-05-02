import pytest

from py_desc.built_in.bool import TrueBoolean, FalseBoolean


class TestingTrueBoolean:
    var = TrueBoolean()


class TestingFalseBoolean:
    var = FalseBoolean()


def test_true_boolean():
    cls = TestingTrueBoolean()
    cls.var = True

    assert cls.var


def test_true_boolean_error():
    cls = TestingTrueBoolean()
    with pytest.raises(ValueError):
        cls.var = False


def test_false_boolean():
    cls = TestingFalseBoolean()
    cls.var = False

    assert not cls.var


def test_false_boolean_error():
    cls = TestingFalseBoolean()
    with pytest.raises(ValueError):
        cls.var = True
