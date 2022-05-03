import pytest

from py_desc.built_in.string import String


class StringTesting:
    var = String()


@pytest.mark.parametrize('value', ['string', 'another string', '7.6', '\n\n\n'])
def test_string(value):
    cls = StringTesting()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [True, 5, 7.6, []])
def test_string_error(value):
    cls = StringTesting()
    with pytest.raises(ValueError):
        cls.var = value
