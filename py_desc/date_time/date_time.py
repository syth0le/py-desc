import datetime

from build.lib.py_desc.base import Base


class Date(Base):

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, datetime.date):
            raise ValueError('Must be datetime.date')
        setattr(instance, self.name, value)

    def __set_name__(self, owner, name):
        self.name = f'_{name.lower()}'


class Time(Base):

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, datetime.time):
            raise ValueError('Must be datetime.time')
        setattr(instance, self.name, value)

    def __set_name__(self, owner, name):
        self.name = f'_{name.lower()}'


class Datetime(Base):

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, datetime.datetime):
            raise ValueError('Must be datetime.datetime')
        setattr(instance, self.name, value)

    def __set_name__(self, owner, name):
        self.name = f'_{name.lower()}'


class Timedelta(Base):

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, datetime.timedelta):
            raise ValueError('Must be datetime.timedelta')
        setattr(instance, self.name, value)

    def __set_name__(self, owner, name):
        self.name = f'_{name.lower()}'


class TzInfo(Base):

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, datetime.tzinfo):
            raise ValueError('Must be datetime.tzinfo')
        setattr(instance, self.name, value)

    def __set_name__(self, owner, name):
        self.name = f'_{name.lower()}'


class Timezone(Base):

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, datetime.timezone):
            raise ValueError('Must be datetime.timezone')
        setattr(instance, self.name, value)

    def __set_name__(self, owner, name):
        self.name = f'_{name.lower()}'
