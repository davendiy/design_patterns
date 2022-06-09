#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from abc import abstractmethod, ABC
from dataclasses import dataclass

MAX_AGE = 20


@dataclass
class Vehicle:
    model:  str = None
    age:    int = None
    damage: float = None
    milage: int = None


class Car(Vehicle):
    milage = 0


class Truck(Vehicle):
    model = 'truck'
    damage = 0


class VehicleCalculator(ABC):
    def __init__(self, v: Vehicle = None) -> None:
        self.vehicle = v

    def set_vehicle(self, v: Vehicle):
        self.vehicle = v

    @abstractmethod
    def calculate_price(self) -> str:
        pass


class TruckCalculator(VehicleCalculator):
    avg_truck_price = 10_000

    def calculate_price(self) -> str:
        res_price = max(
            self.avg_truck_price
            - 100 * (self.vehicle.age / MAX_AGE)
            - 0.01 * self.vehicle.milage,
            0,
        )
        return f"{res_price} USD"


class CarCalculator(VehicleCalculator):
    avg_car_price = 10_000
    car_prices = {
        'bmw': 15_000,
        'audi': 18_000,
        'mercedes': 30_000,
        'tesla': 45_000,
        'volkswagen': 20_000,
    }

    def calculate_price(self) -> str:
        retail_price = self.car_prices.get(
            self.vehicle.model,
            self.avg_car_price    # if model hasn't been added to the database
        )
        res_price = self.vehicle.damage * max(
            retail_price - 100 * self.vehicle.damage, 0
        )
        return f"{res_price} USD"

__all__ = [
    'Vehicle',
    'Car',
    'Truck',
    'VehicleCalculator',
    'TruckCalculator',
    'CarCalculator'
]