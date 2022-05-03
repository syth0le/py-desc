import pytest

from py_desc.built_in.integer import PositiveInteger, NegativeInteger


class PositiveIntegerTesting:
    var = PositiveInteger()


class NegativeIntegerTesting:
    var = NegativeInteger()


@pytest.mark.parametrize('value', [5, 0, 3942, True])
def test_positive_int(value):
    cls = PositiveIntegerTesting()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-2, '23', 7.6, -231])
def test_positive_int_error(value):
    cls = PositiveIntegerTesting()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize('value', [-5, -234])
def test_negative_int(value):
    cls = NegativeIntegerTesting()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [2, '23', 7.6, 231])
def test_negative_int_error(value):
    cls = NegativeIntegerTesting()
    with pytest.raises(ValueError):
        cls.var = value
