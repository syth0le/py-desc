import pytest

from py_desc.built_in.tuple import \
    SimpleTuple, TupleOfFloats, TupleOfIntegers, TupleOfNumbers, TupleOfStrings, CustomTuple


class TestingSimpleTuple:
    var = SimpleTuple()


class TestingTupleOfIntegers:
    var = TupleOfIntegers()


class TestingTupleOfFloats:
    var = TupleOfFloats()


class TestingTupleOfNumbers:
    var = TupleOfNumbers()


class TestingTupleOfStrings:
    var = TupleOfStrings()


class TestingCustomTuple:
    var_bool = CustomTuple(bool)
    var_str = CustomTuple(str)
    var_float = CustomTuple(float)
    var_list = CustomTuple(list)
    var_int = CustomTuple(int)

    def __init__(self, bl, st, fl, li, it):
        self.var_bool = bl
        self.var_str = st
        self.var_float = fl
        self.var_list = li
        self.var_int = it


@pytest.mark.parametrize('value', ((), ('fff',), ('4', 5), (True, False), (()), ))
def test_simple_tuple(value):
    cls = TestingSimpleTuple()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', (True, 5, 7.6, [], ))
def test_simple_tuple_error(value):
    cls = TestingSimpleTuple()
    with pytest.raises(ValueError):
        cls.var = value


def test_integer_tuple():
    temp_tuple = (5, 6, 7)
    cls = TestingTupleOfIntegers()
    cls.var = temp_tuple

    assert cls.var == temp_tuple


@pytest.mark.parametrize('value', (('fff',), ('4', 5), (5.6,)))
def test_integer_tuple_error(value):
    cls = TestingTupleOfIntegers()
    with pytest.raises(ValueError):
        cls.var = value


def test_float_tuple():
    temp_tuple = (5.1, 6.3, 7.0)
    cls = TestingTupleOfFloats()
    cls.var = temp_tuple

    assert cls.var == temp_tuple


@pytest.mark.parametrize('value', (('fff',), ('4', 5), (5, 6, 7), (True, False)))
def test_float_tuple_error(value):
    cls = TestingTupleOfFloats()
    with pytest.raises(ValueError):
        cls.var = value


def test_strings_tuple():
    temp_tuple = ('one', 'two', 'three')
    cls = TestingTupleOfStrings()
    cls.var = temp_tuple

    assert cls.var == temp_tuple


@pytest.mark.parametrize('value', ((5.4, 5.6), ('4', 5), (5, 6, 7), (True, False)))
def test_strings_tuple_error(value):
    cls = TestingTupleOfStrings()
    with pytest.raises(ValueError):
        cls.var = value


def test_numbers_tuple():
    temp_tuple = (5, 6.3, 7.6, 0)
    cls = TestingTupleOfNumbers()
    cls.var = temp_tuple

    assert cls.var == temp_tuple


@pytest.mark.parametrize('value', ((5.4, '3', 5.6), [5, 6]))
def test_numbers_tuple_error(value):
    cls = TestingTupleOfNumbers()
    with pytest.raises(ValueError):
        cls.var = value


def test_custom_tuple():
    cls = TestingCustomTuple(
        bl=(True,), st=('',), fl=(3.4,), li=(['', 'f'], ['d', 5]), it=(5,)
    )

    assert cls.var_bool == (True,)
    assert cls.var_str == ('',)
    assert cls.var_float == (3.4,)
    assert cls.var_list == (['', 'f'], ['d', 5])
    assert cls.var_int == (5,)


@pytest.mark.parametrize('type,value', ((int, (5.6,)), (float, (6,)), (bool, ('True',)), (str, (5,))))
def test_custom_tuple_error(type, value):
    class TestingCustomTupleLocal:
        var = CustomTuple(type)

    cls = TestingCustomTupleLocal()
    with pytest.raises(ValueError):
        cls.var = value
