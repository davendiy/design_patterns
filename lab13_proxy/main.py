#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from src import ImageGallery
import os

_, _, filenames = next(os.walk('./images'))

filenames = [os.path.join('./images', filename) for filename in filenames]

g = ImageGallery(filenames)
g.show()
