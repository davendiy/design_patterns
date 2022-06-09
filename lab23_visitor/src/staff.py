#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .base import AcceptsVisitors, Employee, Visitor


class SalesPerson(AcceptsVisitors, Employee):

    def get_salary(self):
        return self.salary + 1000

    def accept(self, v: Visitor):
        v.visit_sales(self)


class Manager(AcceptsVisitors, Employee):

    def get_salary(self):
        return self.salary * 0.2

    def accept(self, v: Visitor):
        v.visit_manager(self)


class ITSupport(AcceptsVisitors, Employee):

    def get_salary(self):
        return self.salary * 35   # salary in dollars

    def accept(self, v: Visitor):
        v.visit_it_support(self)
