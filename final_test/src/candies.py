#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 10.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .base import CandyBase, CandyWrapper
from typing import Iterable


class CandiesForm(CandyWrapper):

    def _own_sugar_amount(self):
        return 0

    def _own_price_delta(self):
        return 0


class Chocolate(CandyWrapper):

    rate = 2
    sugar = 0.7

    def __init__(self, candies: Iterable[CandyBase], amount):
        self.amount = amount
        super(Chocolate, self).__init__(candies)

    def _own_price_delta(self):
        return self.amount * self.rate

    def _own_sugar_amount(self):
        return self.sugar


class SimpleCandy(CandyBase):

    rate: float = ...
    sugar: float = 1

    def __init__(self, amount):
        self.amount = amount

    def get_sugar_amount(self):
        return self.sugar

    def get_price_delta(self):
        return self.amount * self.rate


class Sweet(SimpleCandy):
    rate = 3
    sugar = 1


class Goody(SimpleCandy):

    rate = 2
    sugar = 0.8


class Honey(CandyWrapper):

    rate = 5
    sugar = 0.9

    def __init__(self, candies: Iterable[CandyBase], amount):
        self.amount = amount
        super(CandyWrapper, self).__init__(candies)

    def _own_price_delta(self):
        return self.amount * self.rate

    def _own_sugar_amount(self):
        return self.sugar
