#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .image import DisplayObject, ImageFile
from typing import List


class ImageProxy(DisplayObject):

    def __init__(self, path):
        self.path = path
        self.src_file: ImageFile = ...

    def display(self):
        if self.src_file is Ellipsis:
            self.src_file = ImageFile(path=self.path)
        self.src_file.display()


class ImageGallery:
    def __init__(self, images: List[str]):
        self.imgs = images

    def show(self):
        for path in self.imgs:
            p = ImageProxy(path)
            p.display()
