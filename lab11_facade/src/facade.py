#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .other_library import Ignition, Clutch, Accelerator, \
                            Gear, HandBrake

class CarFacade:
    def drive(self):
        ignition = Ignition()
        clutch = Clutch()
        accelerator = Accelerator()
        gear_stick = Gear()
        hand_brake = HandBrake()

        ignition.turn_on()
        clutch.press()
        gear_stick.change_gear(1)
        accelerator.press()
        clutch.lift()
        hand_brake.push_down()
        accelerator.press()
        clutch.press()
