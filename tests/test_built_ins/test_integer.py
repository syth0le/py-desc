import pytest

from py_desc.built_in.integer import PositiveInteger, NegativeInteger, CustomInteger


class PositiveIntegerTesting:
    var = PositiveInteger()


class NegativeIntegerTesting:
    var = NegativeInteger()


@pytest.mark.parametrize("value", [5, 0, 3942, True])
def test_positive_int(value):
    cls = PositiveIntegerTesting()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize("value", [-2, "23", 7.6, -231])
def test_positive_int_error(value):
    cls = PositiveIntegerTesting()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize("value", [-5, -234])
def test_negative_int(value):
    cls = NegativeIntegerTesting()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize("value", [2, "23", 7.6, 231])
def test_negative_int_error(value):
    cls = NegativeIntegerTesting()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize(
    "min_value, max_value, test_value",
    [
        (5, 10, 7),
        (-4, 4, 0),
        (-3, -2, -3),
        (234, 301, 278),
        (None, None, -3),
        (-3, None, -3),
        (None, -3, -5),
    ],
)
def test_custom_float(min_value, max_value, test_value):
    class CustomTest:
        var = CustomInteger(min_value, max_value)

    cls = CustomTest()
    cls.var = test_value

    assert cls.var == test_value


@pytest.mark.parametrize(
    "min_value, max_value, test_value",
    [
        (-4, -2, 1),
        (-3, -2, -3.1),
        (234, 235, 278),
        (-3, None, -4),
        (None, -3, -2),
        (-4, 1, "str"),
    ],
)
def test_custom_float_value_error(min_value, max_value, test_value):
    class CustomTest:
        var = CustomInteger(min_value, max_value)

    cls = CustomTest()
    with pytest.raises(ValueError):
        cls.var = test_value


@pytest.mark.parametrize(
    "min_value, max_value, test_value",
    [
        ("str", 10, 7),
        (-4, "str", 0.1),
        (234, 211, 278.7),
        (5.3, 10, 7),
        (-4.3, -2, 0.1),
        (-3, -2.1, -3.1),
    ],
)
def test_custom_float_attribute_error(min_value, max_value, test_value):

    with pytest.raises(AttributeError):

        class CustomTest:
            var = CustomInteger(min_value, max_value)

        test_cls = CustomTest()
        test_cls.var = test_value
