#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Union


class StringWrapperBase(ABC):

    def __init__(self, wrapped: Union[str, StringWrapperBase]):
        self._wrapped = wrapped

    def __str__(self):
        res = self._handle_str()
        return res

    @abstractmethod
    def _handle_str(self):
        pass

    def raw_str(self):
        if hasattr(self._wrapped, 'raw_str'):
            return self._wrapped.raw_str()
