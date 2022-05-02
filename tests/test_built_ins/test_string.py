import pytest

from py_desc.built_in.string import String


class TestingString:
    var = String()


@pytest.mark.parametrize('value', ['string', 'another string', '7.6', '\n\n\n',])
def test_string(value):
    cls = TestingString()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [True, 5, 7.6, [],])
def test_string_error(value):
    cls = TestingString()
    with pytest.raises(ValueError):
        cls.var = value
