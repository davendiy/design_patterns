#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from abc import ABC, abstractmethod
from typing import List

from .employee import Employee
from .iterator import EmployeeIterator


class IterableCollection(ABC):
    @abstractmethod
    def __iter__(self):
        pass


class StaffList:
    def __init__(self, employees: List[Employee]):
        self.employees = employees

    def __iter__(self):
        return EmployeeIterator(self.employees)
