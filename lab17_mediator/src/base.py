#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from abc import ABC, abstractmethod
from typing import Optional

from enum import Enum


class BaseComponent(ABC):
    def __init__(self, mediator: Optional["Mediator"] = None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Optional['Mediator']):
        self._mediator = mediator


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: BaseComponent, event):
        pass


class Event(Enum):
    TAKING_OFF: str = "taking off"
    IN_AIR: str = "in the air"
    LANDING: str = "landing"
    ON_GROUND: str = "on the ground"
