import pytest

from py_desc.built_in.set import SimpleSet, SetOfFloats, SetOfIntegers, SetOfNumbers, SetOfStrings, CustomSet


class TestingSimpleSet:
    var = SimpleSet()


class TestingSetOfIntegers:
    var = SetOfIntegers()


class TestingSetOfFloats:
    var = SetOfFloats()


class TestingSetOfNumbers:
    var = SetOfNumbers()


class TestingSetOfStrings:
    var = SetOfStrings()


class TestingCustomSet:
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
    cls = TestingSimpleSet()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [True, 5, 7.6, (), ])
def test_simple_set_error(value):
    cls = TestingSimpleSet()
    with pytest.raises(ValueError):
        cls.var = value


def test_integer_set():
    temp_set = {5, 6, 7}
    cls = TestingSetOfIntegers()
    cls.var = temp_set

    assert cls.var == temp_set


@pytest.mark.parametrize('value', [{'fff'}, {'4', 5}, {5.6}])
def test_integer_set_error(value):
    cls = TestingSetOfIntegers()
    with pytest.raises(ValueError):
        cls.var = value


def test_float_set():
    temp_set = {5.1, 6.3, 7.0}
    cls = TestingSetOfFloats()
    cls.var = temp_set

    assert cls.var == temp_set


@pytest.mark.parametrize('value', [['fff'], ['4', 5], [[[]]], [5, 6, 7], [True, False]])
def test_float_set_error(value):
    cls = TestingSetOfFloats()
    with pytest.raises(ValueError):
        cls.var = value


def test_strings_set():
    temp_set = {'one', 'two', 'three'}
    cls = TestingSetOfStrings()
    cls.var = temp_set

    assert cls.var == temp_set


@pytest.mark.parametrize('value', [[5.4, 5.6], ['4', 5], [[[]]], [5, 6, 7], [True, False]])
def test_strings_set_error(value):
    cls = TestingSetOfStrings()
    with pytest.raises(ValueError):
        cls.var = value


def test_numbers_set():
    temp_set = {5, 6.3, 7.6, 0}
    cls = TestingSetOfNumbers()
    cls.var = temp_set

    assert cls.var == temp_set


@pytest.mark.parametrize('value', [[5.4, '3', 5.6], [[[]]], (5, 6)])
def test_numbers_set_error(value):
    cls = TestingSetOfNumbers()
    with pytest.raises(ValueError):
        cls.var = value


def test_custom_set():
    cls = TestingCustomSet(
        bl={True}, st={''}, fl={3.4}, it={5}
    )

    assert cls.var_bool == {True}
    assert cls.var_str == {''}
    assert cls.var_float == {3.4}
    assert cls.var_int == {5}


@pytest.mark.parametrize('type,value', [(int, {5.6}), (float, {6}), (bool, {'True'}), (str, {5})])
def test_custom_set_error(type, value):
    class TestingCustomSetLocal:
        var = CustomSet(type)

    cls = TestingCustomSetLocal()
    with pytest.raises(ValueError):
        cls.var = value
