#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from typing import Tuple
from .foreign_customs import CustomsVehicle

from .vehicles import Car, CarCalculator, Truck, TruckCalculator, \
    Vehicle, VehicleCalculator


class CalculatorAdapter:
    def __init__(self, v: CustomsVehicle = None) -> None:
        self.vehicle = v

    def _get_calculator(self) -> Tuple[Vehicle, type(VehicleCalculator)]:
        if self.vehicle.model == "truck":
            return (
                Truck(age=self.vehicle.age,
                      milage=self.vehicle.milage),
                TruckCalculator,
            )
        return (
            Car(age=self.vehicle.age,
                model=self.vehicle.model,
                damage=self.vehicle.damage),
            CarCalculator,
        )

    def price(self):
        vehicle, calc = self._get_calculator()

        # returned in form of string "N USD"
        p = calc(vehicle).calculate_price()
        return p.strip("USD") + "ГРН"
