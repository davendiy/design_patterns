#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from src import CustomsVehicle, Customs, CalculatorAdapter


class UkrainianCustoms(Customs):
    def vehicle_price(self, v: CustomsVehicle) -> float:
        return CalculatorAdapter(v).price()

    def tax(self, v: CustomsVehicle) -> float:
        price = self.vehicle_price(v)
        return 0.2 * price


if __name__ == "__main__":
    v = CustomsVehicle(model="truck", age=2, damage=0, milage=10_000)
    print(UkrainianCustoms().vehicle_price(v))
