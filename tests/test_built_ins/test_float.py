import pytest

from py_desc.built_in.float import PositiveFloat, NegativeFloat


class PositiveFloatTesting:
    var = PositiveFloat()


class NegativeFloatTesting:
    var = NegativeFloat()


@pytest.mark.parametrize('value', [5.3, 0.0, 3942.3])
def test_positive_float(value):
    cls = PositiveFloatTesting()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-2, '23', 7, -231])
def test_positive_float_error(value):
    cls = PositiveFloatTesting()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize('value', [-5.4, -234.123])
def test_negative_float(value):
    cls = NegativeFloatTesting()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [2, '23', -7, 231])
def test_negative_float_error(value):
    cls = NegativeFloatTesting()
    with pytest.raises(ValueError):
        cls.var = value
