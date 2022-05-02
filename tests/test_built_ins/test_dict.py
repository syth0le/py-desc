import pytest

from py_desc.built_in.dict import SimpleDict


class TestingSimpleDict:
    var = SimpleDict()


@pytest.mark.parametrize('value', [{}, {'f': 5}, {'key': {'key2': 'value'}}])
def test_dict(value):
    cls = TestingSimpleDict()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [True, 5, 7.6, []])
def test_dict_error(value):
    cls = TestingSimpleDict()
    with pytest.raises(ValueError):
        cls.var = value
