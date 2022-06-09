#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def has_more(self):
        pass


class EmployeeIterator(Iterator):
    def __init__(self, employee_list):
        self.collection = employee_list
        self.state = 0

    def has_more(self):
        return self.state < len(self.collection)

    def __next__(self):
        if not self.has_more():
            print(f"Stop iteration.")
            raise StopIteration
        print(
            f"Next from Iterator. Current state {self.state}"
        )
        val = self.collection[self.state]
        self.state += 1
        return val
