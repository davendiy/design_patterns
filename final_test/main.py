#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 10.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi
from src import Pie, Dessert
from typing import Dict


class Confectionery:

    def __init__(self, makers: Dict):
        self.makers = makers

    def meny(self):
        return self.makers.keys()

    def cook(self, meal):
        maker = self.makers[meal]   # type: Dessert
        return maker.make_candy()


menu = {
    'pie': Pie(3, 2, 3)
}


test = Confectionery(menu)

print(test.cook('pie').get_price_delta())
print(test.cook('pie').get_sugar_amount())
