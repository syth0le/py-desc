import pytest

from py_desc.built_in.float import PositiveFloat, NegativeFloat, CustomFloat


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


@pytest.mark.parametrize(
    'min_value, max_value, test_value',
    [
        (5.3, 10, 7.6),
        (-4.3, 4, 0.0),
        (-3, -2.1, -3.0),
        (234.4, 301.0, 278.7),
        (None, None, -3.1),
        (-3.2, None, -3.1),
        (None, -3.2, -5.1),
    ],
)
def test_custom_float(min_value, max_value, test_value):
    class CustomTest:
        var = CustomFloat(min_value, max_value)

    cls = CustomTest()
    cls.var = test_value

    assert cls.var == test_value


@pytest.mark.parametrize(
    'min_value, max_value, test_value',
    [
        (5.3, 10, 7),
        (-4.3, -2, 0.1),
        (-3, -2.1, -3.1),
        (234.4, 235.0, 278.7),
        (-3, None, -3.1),
        (None, -3.3, -3.1),
        (-4.3, 1, 'str'),
    ],
)
def test_custom_float_value_error(min_value, max_value, test_value):
    class CustomTest:
        var = CustomFloat(min_value, max_value)

    cls = CustomTest()
    with pytest.raises(ValueError):
        cls.var = test_value


@pytest.mark.parametrize(
    'min_value, max_value, test_value',
    [
        ('str', 10, 7),
        (-4.3, 'str', 0.1),
        (234.4, 211.0, 278.7),
    ],
)
def test_custom_float_attribute_error(min_value, max_value, test_value):

    with pytest.raises(AttributeError):

        class CustomTest:
            var = CustomFloat(min_value, max_value)

        test_cls = CustomTest()
        test_cls.var = test_value
