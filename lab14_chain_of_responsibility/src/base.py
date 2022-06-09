#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class BaseHandler(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, next_: BaseHandler = None):
        self._next = next_
        return self

    @property
    def next(self):
        return self._next

    @abstractmethod
    def handle(self, obj: Any):
        pass


class HandlingError(Exception):
    pass
