#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from abc import ABC, abstractmethod


class DrinkAddition(ABC):
    @abstractmethod
    def get_price(self) -> int:
        pass


class Milk(DrinkAddition):
    def get_price(self) -> int:
        return 2


class Chocolate(DrinkAddition):
    def get_price(self) -> int:
        return 10
