#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 10.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from abc import ABC, abstractmethod
from typing import Iterable


class CandyMakerBase(ABC):

    @abstractmethod
    def make_candy(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_sugar(self):
        pass


class CandyBase(ABC):

    @abstractmethod
    def get_price_delta(self):
        pass

    @abstractmethod
    def get_sugar_amount(self):
        pass


class CandyWrapper(CandyBase):

    def __init__(self, candies: Iterable[CandyBase]):
        self._children = candies

    def get_price_delta(self):
        own = self._own_price_delta()
        return sum(child.get_price_delta() for child in self._children) + own

    def get_sugar_amount(self):
        own = self._own_sugar_amount()
        res = 1
        for child in self._children:
            res *= child.get_sugar_amount()
        return res * own

    @abstractmethod
    def _own_price_delta(self):
        pass

    @abstractmethod
    def _own_sugar_amount(self):
        pass
