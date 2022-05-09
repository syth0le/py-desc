import datetime
from typing import TypeVar

from py_desc.base import Base

T = TypeVar('T', bound=list)
C = TypeVar('C')


class Date(Base):

    def __get__(self, instance: 'Date', owner: C) -> T:
        return getattr(instance, self.name)

    def __set__(self, instance: 'Date', value: T) -> None:
        if not isinstance(value, datetime.date):
            raise ValueError('Must be datetime.date')
        setattr(instance, self.name, value)

    def __set_name__(self, owner: C, name: str) -> None:
        self.name = f'_{name.lower()}'


class Time(Base):

    def __get__(self, instance: 'Time', owner: C) -> T:
        return getattr(instance, self.name)

    def __set__(self, instance: 'Time', value: T) -> None:
        if not isinstance(value, datetime.time):
            raise ValueError('Must be datetime.time')
        setattr(instance, self.name, value)

    def __set_name__(self, owner: C, name: str) -> None:
        self.name = f'_{name.lower()}'


class Datetime(Base):

    def __get__(self, instance: 'Datetime', owner: C) -> T:
        return getattr(instance, self.name)

    def __set__(self, instance: 'Datetime', value: T) -> None:
        if not isinstance(value, datetime.datetime):
            raise ValueError('Must be datetime.datetime')
        setattr(instance, self.name, value)

    def __set_name__(self, owner: C, name: str) -> None:
        self.name = f'_{name.lower()}'


class Timedelta(Base):

    def __get__(self, instance: 'Timedelta', owner: C) -> T:
        return getattr(instance, self.name)

    def __set__(self, instance: 'Timedelta', value: T) -> None:
        if not isinstance(value, datetime.timedelta):
            raise ValueError('Must be datetime.timedelta')
        setattr(instance, self.name, value)

    def __set_name__(self, owner: C, name: str) -> None:
        self.name = f'_{name.lower()}'


class TzInfo(Base):

    def __get__(self, instance: 'TzInfo', owner: C) -> T:
        return getattr(instance, self.name)

    def __set__(self, instance: 'TzInfo', value: T) -> None:
        if not isinstance(value, datetime.tzinfo):
            raise ValueError('Must be datetime.tzinfo')
        setattr(instance, self.name, value)

    def __set_name__(self, owner: C, name: str) -> None:
        self.name = f'_{name.lower()}'


class Timezone(Base):

    def __get__(self, instance: 'Timezone', owner: C) -> T:
        return getattr(instance, self.name)

    def __set__(self, instance: 'Timezone', value: T) -> None:
        if not isinstance(value, datetime.timezone):
            raise ValueError('Must be datetime.timezone')
        setattr(instance, self.name, value)

    def __set_name__(self, owner: C, name: str) -> None:
        self.name = f'_{name.lower()}'
