import pytest

from py_desc.date_time.date_time import *


class TestingDate:
    var = Date()


class TestingTime:
    var = Time()


class TestingDatetime:
    var = Datetime()


class TestingTimedelta:
    var = Timedelta()


class TestingTzInfo:
    var = TzInfo()


class TestingTimezone:
    var = Timezone()


@pytest.mark.parametrize('value', [datetime.date.today()])
def test_date(value):
    cls = TestingDate()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-5.4, -234.123])
def test_date_error(value):
    cls = TestingDate()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize('value', [datetime.time(12, 10, 30)])
def test_time(value):
    cls = TestingTime()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-5.4, -234.123])
def test_time_error(value):
    cls = TestingTime()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize('value', [datetime.datetime.now()])
def test_datetime(value):
    cls = TestingDatetime()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-5.4, -234.123])
def test_datetime_error(value):
    cls = TestingDatetime()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize('value', [datetime.timedelta(days=365)])
def test_timedelta(value):
    cls = TestingTimedelta()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-5.4, -234.123])
def test_timedelta_error(value):
    cls = TestingTimedelta()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize('value', [datetime.timezone(datetime.timedelta(hours=5, minutes=3))])
def test_tzinfo(value):
    cls = TestingTzInfo()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-5.4, -234.123])
def test_tzinfo_error(value):
    cls = TestingTzInfo()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize('value', [datetime.timezone.utc])
def test_timezone(value):
    cls = TestingTimezone()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-5.4, -234.123])
def test_timezone_error(value):
    cls = TestingTimezone()
    with pytest.raises(ValueError):
        cls.var = value
