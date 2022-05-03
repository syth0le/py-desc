import pytest

from py_desc.built_in.tuple import \
    SimpleTuple, TupleOfFloats, TupleOfIntegers, TupleOfNumbers, TupleOfStrings, CustomTuple


class SimpleTupleTesting:
    var = SimpleTuple()


class TupleOfIntegersTesting:
    var = TupleOfIntegers()


class TupleOfFloatsTesting:
    var = TupleOfFloats()


class TupleOfNumbersTesting:
    var = TupleOfNumbers()


class TupleOfStringsTesting:
    var = TupleOfStrings()


class CustomTupleTesting:
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
    cls = SimpleTupleTesting()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', (True, 5, 7.6, [], ))
def test_simple_tuple_error(value):
    cls = SimpleTupleTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_integer_tuple():
    temp_tuple = (5, 6, 7)
    cls = TupleOfIntegersTesting()
    cls.var = temp_tuple

    assert cls.var == temp_tuple


@pytest.mark.parametrize('value', (('fff',), ('4', 5), (5.6,)))
def test_integer_tuple_error(value):
    cls = TupleOfIntegersTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_float_tuple():
    temp_tuple = (5.1, 6.3, 7.0)
    cls = TupleOfFloatsTesting()
    cls.var = temp_tuple

    assert cls.var == temp_tuple


@pytest.mark.parametrize('value', (('fff',), ('4', 5), (5, 6, 7), (True, False)))
def test_float_tuple_error(value):
    cls = TupleOfFloatsTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_strings_tuple():
    temp_tuple = ('one', 'two', 'three')
    cls = TupleOfStringsTesting()
    cls.var = temp_tuple

    assert cls.var == temp_tuple


@pytest.mark.parametrize('value', ((5.4, 5.6), ('4', 5), (5, 6, 7), (True, False)))
def test_strings_tuple_error(value):
    cls = TupleOfStringsTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_numbers_tuple():
    temp_tuple = (5, 6.3, 7.6, 0)
    cls = TupleOfNumbersTesting()
    cls.var = temp_tuple

    assert cls.var == temp_tuple


@pytest.mark.parametrize('value', ((5.4, '3', 5.6), [5, 6]))
def test_numbers_tuple_error(value):
    cls = TupleOfNumbersTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_custom_tuple():
    cls = CustomTupleTesting(
        bl=(True,), st=('',), fl=(3.4,), li=(['', 'f'], ['d', 5]), it=(5,)
    )

    assert cls.var_bool == (True,)
    assert cls.var_str == ('',)
    assert cls.var_float == (3.4,)
    assert cls.var_list == (['', 'f'], ['d', 5])
    assert cls.var_int == (5,)


@pytest.mark.parametrize('type,value', ((int, (5.6,)), (float, (6,)), (bool, ('True',)), (str, (5,))))
def test_custom_tuple_error(type, value):
    class CustomTupleLocalTesting:
        var = CustomTuple(type)

    cls = CustomTupleLocalTesting()
    with pytest.raises(ValueError):
        cls.var = value
