#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CustomsVehicle:
    model:  str
    age:    int
    damage: float
    milage: int


class Customs(ABC):
    @abstractmethod
    def vehicle_price(self, v: CustomsVehicle) -> float:
        pass

    @classmethod
    @abstractmethod
    def tax(cls, v: CustomsVehicle) -> float:
        pass
