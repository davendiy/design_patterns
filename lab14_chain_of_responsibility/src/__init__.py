#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .arithmetics import Unary, Binary, Op, \
    ArithmeticHandler, Plus, Mul, \
    Minus, Neg

from .file_openers import FileHandler, ExeFileHandler, JpegFileHandler, \
    BmpFileHandler, HandlingError


_exe = ExeFileHandler()
_jpeg =JpegFileHandler().set_next(_exe)
file_handler = BmpFileHandler().set_next(_jpeg)
