#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .base import Mediator, Event
from .airport import PlanesInFlight, \
    PlanesOnGround, Runway, Plane


class Watchtower(Mediator):
    def __init__(
        self,
        planes_in_flight: PlanesInFlight,
        planes_on_ground: PlanesOnGround,
        runway: Runway,
    ):
        self.planes_in_flight = planes_in_flight
        self.planes_in_flight.mediator = self
        self.planes_on_ground = planes_on_ground
        self.planes_on_ground.mediator = self
        self.runway = runway
        self.runway.mediator = self

    def notify(self, plane: Plane, event: Event):
        if event == Event.TAKING_OFF:
            self.runway.reserve()
            self.planes_in_flight.add_plane(plane)
            self.planes_on_ground.remove_plane(plane)

        if event == Event.LANDING:
            self.runway.reserve()
            self.planes_on_ground.add_plane(plane)
            self.planes_in_flight.remove_plane(plane)

        if event in (Event.IN_AIR, Event.ON_GROUND):
            self.runway.free()
