#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .drink_color import DrinkColorBase
from .additions import DrinkAddition
from .consumption import ConsumptionBase

from typing import Iterable


SUGAR_PRICE = 0.4

class Beverage:
    base_price = 10

    def __init__(
        self,
        sugar,
        color: DrinkColorBase,
        additions: Iterable[DrinkAddition],
        consumption: ConsumptionBase,
    ):
        self.sugar = sugar
        self.color = color
        self.additions = additions
        self.consumption = consumption

    def prepare(self):
        drink_name = self.__class__.__name__
        color_name = self.color.__class__.__name__
        additions = (
            ", ".join(add.__class__.__name__ for add in self.additions)
        )
        consumption_type = self.consumption.__class__.__name__

        res = f"Making drink <{color_name} {drink_name}> to {consumption_type}"
        if additions:
            res +=  f"with adds: {additions}"
        print(res)

    def drink(self):
        print("Drinking...")

    def cost(self):
        return (
            self.base_price
            + SUGAR_PRICE * self.sugar
            + self.color.get_price()
            + sum(add.get_price() for add in self.additions)
        )


class Coffe(Beverage):
    base_price = 15


class Tea(Beverage):
    base_price = 12
