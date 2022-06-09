#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from abc import ABC, abstractmethod
from PIL import Image


class DisplayObject(ABC):
    @abstractmethod
    def display(self):
        pass


class ImageFile(DisplayObject):
    def __init__(self, path: str):
        self.img = Image.open(path)

    def display(self):
        self.img.show()
