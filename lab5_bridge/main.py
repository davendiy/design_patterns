#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from src import Tea, BlackDrink, Milk, ConsumeInside

beverage = Tea(
    sugar=0,
    color=BlackDrink(),
    additions=[Milk()],
    consumption=ConsumeInside()
)

beverage.prepare()
print("Price: ", beverage.cost(), " ГРН")
