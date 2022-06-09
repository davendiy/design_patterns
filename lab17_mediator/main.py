#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from src import Plane, PlanesInFlight, PlanesOnGround, Runway, Watchtower


plane_1 = Plane(123113)
plane_2 = Plane(123131)
plane_3 = Plane(123123)

planes_on_ground = PlanesOnGround()
runway = Runway()
planes_in_flight = PlanesInFlight()

watchtower = Watchtower(planes_in_flight, planes_on_ground, runway)

planes_on_ground.register_plane(plane_1)
planes_on_ground.register_plane(plane_2)
planes_on_ground.register_plane(plane_3)

plane_1.take_off()
print()
plane_2.take_off()
print()
plane_1.land()
print()
plane_3.take_off()
print()
plane_2.land()
print()
plane_3.land()
