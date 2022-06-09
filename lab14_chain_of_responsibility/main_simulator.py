#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from src import Binary, Unary, Plus, Minus, \
    Mul, Neg, HandlingError

ops = [
    Binary("+", "2", "5"),
    Binary("*", "3", "4"),
    Unary("-", "7"),
    Binary("-", "1", "1"),
]

h = Plus()
h = Minus().set_next(h)
h = Mul().set_next(h)
h = Neg().set_next(h)

for op in ops:
    try:
        print(f"{op=} {h.handle(op)=}")
    except HandlingError:
        print(f"Unable to handle {op}")
