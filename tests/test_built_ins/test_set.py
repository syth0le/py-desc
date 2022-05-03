import pytest

from py_desc.built_in.set import SimpleSet, SetOfFloats, SetOfIntegers, SetOfNumbers, SetOfStrings, CustomSet


class SimpleSetTesting:
    var = SimpleSet()


class SetOfIntegersTesting:
    var = SetOfIntegers()


class SetOfFloatsTesting:
    var = SetOfFloats()


class SetOfNumbersTesting:
    var = SetOfNumbers()


class SetOfStringsTesting:
    var = SetOfStrings()


class CustomSetTesting:
    var_bool = CustomSet(bool)
    var_str = CustomSet(str)
    var_float = CustomSet(float)
    var_int = CustomSet(int)

    def __init__(self, bl, st, fl, it):
        self.var_bool = bl
        self.var_str = st
        self.var_float = fl
        self.var_int = it


@pytest.mark.parametrize('value', [{'fff'}, {'4', 5}, {True, False}])
def test_simple_set(value):
    cls = SimpleSetTesting()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [True, 5, 7.6, (), ])
def test_simple_set_error(value):
    cls = SimpleSetTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_integer_set():
    temp_set = {5, 6, 7}
    cls = SetOfIntegersTesting()
    cls.var = temp_set

    assert cls.var == temp_set


@pytest.mark.parametrize('value', [{'fff'}, {'4', 5}, {5.6}])
def test_integer_set_error(value):
    cls = SetOfIntegersTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_float_set():
    temp_set = {5.1, 6.3, 7.0}
    cls = SetOfFloatsTesting()
    cls.var = temp_set

    assert cls.var == temp_set


@pytest.mark.parametrize('value', [['fff'], ['4', 5], [[[]]], [5, 6, 7], [True, False]])
def test_float_set_error(value):
    cls = SetOfFloatsTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_strings_set():
    temp_set = {'one', 'two', 'three'}
    cls = SetOfStringsTesting()
    cls.var = temp_set

    assert cls.var == temp_set


@pytest.mark.parametrize('value', [[5.4, 5.6], ['4', 5], [[[]]], [5, 6, 7], [True, False]])
def test_strings_set_error(value):
    cls = SetOfStringsTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_numbers_set():
    temp_set = {5, 6.3, 7.6, 0}
    cls = SetOfNumbersTesting()
    cls.var = temp_set

    assert cls.var == temp_set


@pytest.mark.parametrize('value', [[5.4, '3', 5.6], [[[]]], (5, 6)])
def test_numbers_set_error(value):
    cls = SetOfNumbersTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_custom_set():
    cls = CustomSetTesting(
        bl={True}, st={''}, fl={3.4}, it={5}
    )

    assert cls.var_bool == {True}
    assert cls.var_str == {''}
    assert cls.var_float == {3.4}
    assert cls.var_int == {5}


@pytest.mark.parametrize('type,value', [(int, {5.6}), (float, {6}), (bool, {'True'}), (str, {5})])
def test_custom_set_error(type, value):
    class CustomSetLocalTesting:
        var = CustomSet(type)

    cls = CustomSetLocalTesting()
    with pytest.raises(ValueError):
        cls.var = value
