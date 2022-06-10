#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 10.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from abc import abstractmethod

from .base import CandyMakerBase, CandyBase
from .candies import Sweet, Chocolate, Goody, CandiesForm


class Dessert(CandyMakerBase):

    def __init__(self, chocolate_amount,
                 sweet_amount, goody_amount):
        self.sweet = sweet_amount
        self.chocolate = chocolate_amount
        self.goody = goody_amount
        self._dessert: CandyBase = ...

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def prepare_basement(self):
        pass

    @abstractmethod
    def make_form(self):
        pass

    @abstractmethod
    def beautify(self):
        pass

    def make_candy(self):
        self.reset()
        self.prepare_basement()
        self.make_form()
        self.beautify()
        return self._dessert

    def get_price(self):
        return self._dessert.get_price_delta()

    def get_sugar(self):
        return self._dessert.get_sugar_amount()


class HoneyDessert(Dessert):

    def __init__(self, chocolate_amount,
                 sweet_amount, goody_amount,
                 honey_amount):
        self.honey = honey_amount
        super(HoneyDessert, self).__init__(chocolate_amount=chocolate_amount,
                                           sweet_amount=sweet_amount,
                                           goody_amount=goody_amount)


class Pie(Dessert):

    def reset(self):
        self._dessert = CandiesForm([])

    def prepare_basement(self):
        self._dessert = CandiesForm([Sweet(self.sweet), Sweet(self.goody)])

    def make_form(self):
        self._dessert = Chocolate([self._dessert], self.chocolate)

    def beautify(self):
        pass
