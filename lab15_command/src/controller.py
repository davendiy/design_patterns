#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .base import Command


class Controller:
    def __init__(
        self,
        command_on: Command,
        command_off: Command,
    ):
        self.command_on = command_on
        self.command_off = command_off

    def on(self):
        return self.command_on.exec()

    def off(self):
        return self.command_off.exec()
