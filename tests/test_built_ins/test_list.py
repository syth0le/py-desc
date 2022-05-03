import pytest

from py_desc.built_in.list import SimpleList, ListOfFloats, ListOfIntegers, ListOfNumbers, ListOfStrings, CustomList


class SimpleListTesting:
    var = SimpleList()


class ListOfIntegersTesting:
    var = ListOfIntegers()


class ListOfFloatsTesting:
    var = ListOfFloats()


class ListOfNumbersTesting:
    var = ListOfNumbers()


class ListOfStringsTesting:
    var = ListOfStrings()


class CustomListTesting:
    var_bool = CustomList(bool)
    var_str = CustomList(str)
    var_float = CustomList(float)
    var_list = CustomList(list)
    var_int = CustomList(int)

    def __init__(self, bl, st, fl, li, it):
        self.var_bool = bl
        self.var_str = st
        self.var_float = fl
        self.var_list = li
        self.var_int = it


@pytest.mark.parametrize('value', [[], ['fff'], ['4', 5], [True, False], [[[]]], ])
def test_simple_list(value):
    cls = SimpleListTesting()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [True, 5, 7.6, (), ])
def test_simple_list_error(value):
    cls = SimpleListTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_integer_list():
    temp_list = [5, 6, 7]
    cls = ListOfIntegersTesting()
    cls.var = temp_list

    assert cls.var == temp_list


@pytest.mark.parametrize('value', [['fff'], ['4', 5], [[[]]], [5.6]])
def test_integer_list_error(value):
    cls = ListOfIntegersTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_float_list():
    temp_list = [5.1, 6.3, 7.0]
    cls = ListOfFloatsTesting()
    cls.var = temp_list

    assert cls.var == temp_list


@pytest.mark.parametrize('value', [['fff'], ['4', 5], [[[]]], [5, 6, 7], [True, False]])
def test_float_list_error(value):
    cls = ListOfFloatsTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_strings_list():
    temp_list = ['one', 'two', 'three']
    cls = ListOfStringsTesting()
    cls.var = temp_list

    assert cls.var == temp_list


@pytest.mark.parametrize('value', [[5.4, 5.6], ['4', 5], [[[]]], [5, 6, 7], [True, False]])
def test_strings_list_error(value):
    cls = ListOfStringsTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_numbers_list():
    temp_list = [5, 6.3, 7.6, 0]
    cls = ListOfNumbersTesting()
    cls.var = temp_list

    assert cls.var == temp_list


@pytest.mark.parametrize('value', [[5.4, '3', 5.6], [[[]]], (5, 6)])
def test_numbers_list_error(value):
    cls = ListOfNumbersTesting()
    with pytest.raises(ValueError):
        cls.var = value


def test_custom_list():
    cls = CustomListTesting(
        bl=[True], st=[''], fl=[3.4], li=[[5], [4]], it=[5]
    )

    assert cls.var_bool == [True]
    assert cls.var_str == ['']
    assert cls.var_float == [3.4]
    assert cls.var_list == [[5], [4]]
    assert cls.var_int == [5]


@pytest.mark.parametrize('type,value', [(int, [5.6]), (float, [6]), (bool, ['True']), (str, [5])])
def test_custom_list_error(type, value):
    class CustomListLocalTesting:
        var = CustomList(type)

    cls = CustomListLocalTesting()
    with pytest.raises(ValueError):
        cls.var = value
