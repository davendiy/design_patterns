#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .base import Visitor, AcceptsVisitors, Employee
from .staff import Manager, SalesPerson, ITSupport

from typing import Iterable, Union


class GiveRaise(Visitor):

    def __init__(self, manager_delta, sales_delta, it_delta):
        self.manager_delta = manager_delta
        self.sales_delta = sales_delta
        self.it_delta = it_delta

    def visit_manager(self, p: "Manager"):
        p.salary += self.manager_delta

    def visit_sales(self, p: "SalesPerson"):
        p.salary += self.sales_delta

    def visit_it_support(self, p: "ITSupport"):
        p.salary += self.it_delta


class StaffList:

    def __init__(self, staff: Iterable[Union[AcceptsVisitors, Employee]]):
        self.staff = staff

    def give_raise(self, manager_delta, sales_delta, it_delta):
        visitor = GiveRaise(manager_delta, sales_delta, it_delta)
        for employee in self.staff:
            employee.accept(visitor)
