import datetime

import pytest

from py_desc.date_time import Date, Time, Datetime, Timedelta, TzInfo, Timezone


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


@pytest.mark.parametrize(
    'value',
    [
        datetime.date.today(),
        datetime.date(2005, 7, 14),
        datetime.date(2072, 3, 24)
    ]
)
def test_date(value):
    cls = TestingDate()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-5.4, -234.123])
def test_date_error(value):
    cls = TestingDate()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize(
    'value',
    [
        datetime.time(12, 10, 30),
        datetime.time(22, 45, 15),
        datetime.time.fromisoformat('04:23:01'),
        datetime.time.fromisoformat('04:23:01.000384')
    ]
)
def test_time(value):
    cls = TestingTime()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-5.4, -234.123])
def test_time_error(value):
    cls = TestingTime()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize(
    'value',
    [
        datetime.datetime.now(),
        datetime.datetime(2005, 7, 14, 12, 30),
        datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")

    ]
)
def test_datetime(value):
    cls = TestingDatetime()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-5.4, -234.123])
def test_datetime_error(value):
    cls = TestingDatetime()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize(
    'value',
    [
        datetime.timedelta(days=365),
        datetime.timedelta(days=64, seconds=29156, microseconds=10),
        datetime.timedelta(microseconds=-1)
    ]
)
def test_timedelta(value):
    cls = TestingTimedelta()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-5.4, -234.123])
def test_timedelta_error(value):
    cls = TestingTimedelta()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize(
    'value',
    [
        datetime.timezone(datetime.timedelta(hours=5, minutes=3)),
        datetime.timezone(datetime.timedelta(hours=-5, minutes=-23))
    ]
)
def test_tzinfo(value):
    cls = TestingTzInfo()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-5.4, -234.123])
def test_tzinfo_error(value):
    cls = TestingTzInfo()
    with pytest.raises(ValueError):
        cls.var = value


@pytest.mark.parametrize(
    'value',
    [
        datetime.timezone.utc,
        datetime.timezone(datetime.timedelta(hours=3)),
        datetime.timezone(datetime.timedelta(hours=-12))
    ]
)
def test_timezone(value):
    cls = TestingTimezone()
    cls.var = value

    assert cls.var == value


@pytest.mark.parametrize('value', [-5.4, -234.123])
def test_timezone_error(value):
    cls = TestingTimezone()
    with pytest.raises(ValueError):
        cls.var = value
