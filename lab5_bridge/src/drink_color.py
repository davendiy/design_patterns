#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi
from abc import ABC, abstractmethod


class DrinkColorBase(ABC):
    @abstractmethod
    def get_price(self) -> int:
        pass


class DefaultDrink(DrinkColorBase):
    def get_price(self) -> int:
        return 0


class BlackDrink(DrinkColorBase):
    def get_price(self) -> int:
        return 10
