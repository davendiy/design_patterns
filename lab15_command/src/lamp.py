#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi


class Lamp:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def light_on(self):
        if self.is_on:
            return
        print(f"{self.name} is on")
        self.is_on = True

    def light_off(self):
        if not self.is_on:
            return
        print(f"{self.name} is off")
        self.is_on = False

