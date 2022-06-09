#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .base import BaseComponent, Event


class Plane(BaseComponent):
    def __init__(self, id: int):
        self.is_in_the_air = False
        self.id = id
        super(Plane, self).__init__()

    def take_off(self):
        if not self.is_in_the_air:
            print(f"Plane {self.id} is taking off.")
            self.is_in_the_air = True
            self.mediator.notify(self, Event.TAKING_OFF)

    def land(self):
        if self.is_in_the_air:
            print(f"Plane {self.id} is landing.")
            self.is_in_the_air = False
            self.mediator.notify(self, Event.LANDING)


class Runway(BaseComponent):
    def __init__(self):
        self.is_awailable = True
        super(Runway, self).__init__()

    def reserve(self):
        self.is_awailable = False
        print("Runway is reserved.")

    def free(self):
        self.is_awailable = True
        print("Runway is free.")


class PlanesOnGround(BaseComponent):
    def __init__(self):
        self.planes = set()
        super(PlanesOnGround, self).__init__()

    def register_plane(self, plane: Plane):
        self.planes.add(plane)
        plane.mediator = self.mediator

    def add_plane(self, plane: Plane):
        self.planes.add(plane)
        print(f"Plane {plane.id} has landed. Add to planes_on_ground.")
        self.mediator.notify(plane, Event.ON_GROUND)

    def remove_plane(self, plane: Plane):
        self.planes.discard(plane)
        print(f"Plane {plane.id} has flighted. Remove from planes on ground.")


class PlanesInFlight(BaseComponent):
    def __init__(self):
        self.planes = set()
        super(PlanesInFlight, self).__init__()

    def add_plane(self, plane: Plane):
        self.planes.add(plane)
        print(f"Plane {plane.id} has flighted. Add to planes_in_flight")
        self.mediator.notify(plane, Event.IN_AIR)

    def remove_plane(self, plane: Plane):
        self.planes.discard(plane)
        print(f"Plane {plane.id} has landed. Remove from planes_in_flight")
