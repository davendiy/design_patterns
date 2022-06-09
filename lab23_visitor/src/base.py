#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def get_salary(self): ...


class Visitor(ABC):

    @abstractmethod
    def visit_sales(self, p: Employee):
        pass

    @abstractmethod
    def visit_manager(self, p: Employee):
        pass

    @abstractmethod
    def visit_it_support(self, p: Employee):
        pass


class AcceptsVisitors(ABC):

    @abstractmethod
    def accept(self, v: Visitor): ...
