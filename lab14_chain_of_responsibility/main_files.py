#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from src import file_handler, HandlingError

file_names = ["foo.bmp", "bar.exe", "foo.jpg", "foo.txt"]

for name in file_names:
    try:
        file_handler.handle(name)
    except HandlingError:
        print(f"Couldn't handle {name}")
