#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .base import StringWrapperBase


class PostComa(StringWrapperBase):

    def _handle_str(self):
        return str(self._wrapped) + ","


class PostSpace(StringWrapperBase):

    def _handle_str(self):
        return str(self._wrapped) + ' '


class PostWord(StringWrapperBase):

    def __init__(self, wrapped, word):
        self._word = word
        super(PostWord, self).__init__(wrapped)

    def _handle_str(self):
        return str(self._wrapped) + self._word


class PostExclaim(StringWrapperBase):

    def _handle_str(self):
        return str(self._wrapped) + '!'
