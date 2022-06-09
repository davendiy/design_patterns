#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from src import SalesPerson, Manager, ITSupport, StaffList


staff_list = [
    SalesPerson('Dav', 1233),
    Manager("Man", 23132),
    ITSupport('Kind', 23234),
]

StaffList(staff_list).give_raise(123, 231, 12313123)
