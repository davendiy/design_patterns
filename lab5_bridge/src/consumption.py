#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from abc import ABC, abstractmethod


class ConsumptionBase(ABC):
    @abstractmethod
    def consume(self) -> None:
        pass


class ConsumeInside(ConsumptionBase):
    def consume(self) -> None:
        print("Drink consumed in house")


class ConsumeOutside(ConsumptionBase):
    def consume(self) -> None:
        print("Drink consumed outdoors")
