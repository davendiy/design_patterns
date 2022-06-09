#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .base import BaseHandler, HandlingError


class FileHandler(BaseHandler):
    expected_ext = "__DEFAULT"

    def handle(self, obj: str) -> int:
        split = obj.split(".")
        ext = split[-1] if split else None

        if ext == self.expected_ext:
            print(f"Handled file {obj} by {self.__class__.__name__}")
            return 0
        else:
            if self.next is not None:
                return self.next.handle(obj)
            else:
                raise HandlingError("Unable to find handler")


class ExeFileHandler(FileHandler):
    expected_ext = "exe"


class JpegFileHandler(FileHandler):
    expected_ext = "jpg"


class BmpFileHandler(FileHandler):
    expected_ext = "bmp"


def build_file_handler_chain() -> FileHandler:
    exe = ExeFileHandler()
    jpeg = JpegFileHandler(next_=exe)
    bmp = BmpFileHandler(next_=jpeg)

    return bmp
