#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .base import Command
from .lamp import Lamp

from typing import Iterable


class LightCommandOn(Command):
    def __init__(self, lamp: Lamp):
        self.lamp = lamp

    def exec(self):
        self.lamp.light_on()


class LightCommandOff(Command):
    def __init__(self, lamp: Lamp):
        self.lamp = lamp

    def exec(self):
        self.lamp.light_off()


class LightCommandOnIters(Command):
    def __init__(self, lamps: Iterable[Lamp]):
        self.lamps = lamps

    def exec(self):
        for l in self.lamps:
            l.light_on()


class LightCommandOffIters(Command):
    def __init__(self, lamps: Iterable[Lamp]):
        self.lamps = lamps

    def exec(self):
        for l in self.lamps:
            l.light_off()
