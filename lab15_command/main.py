#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

import src as s

test_lamp = s.Lamp(name="foo")
command1 = s.LightCommandOn(test_lamp)
command2 = s.LightCommandOff(test_lamp)
controller_foo = s.Controller(command1, command2)

test_lamp2 = s.Lamp(name="bar")
command1 = s.LightCommandOn(test_lamp2)
command2 = s.LightCommandOff(test_lamp2)
controller_bar = s.Controller(command1, command2)

command_iters_1 = s.LightCommandOnIters([test_lamp, test_lamp2])
command_iters_2 = s.LightCommandOffIters([test_lamp, test_lamp2])
iters_controller = s.Controller(
    command_iters_1, command_iters_2
)

controller_foo.on()
controller_foo.off()

controller_bar.on()
controller_bar.off()

iters_controller.on()
iters_controller.off()
