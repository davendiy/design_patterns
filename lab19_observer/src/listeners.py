#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi
from enum import Enum, auto


class Event(Enum):
    LINE = auto()
    WORD = auto()
    WORD_IN_LINE = auto()


class EventListener:
    def update(self, data: str):
        pass


class MaxLineEventListener(EventListener):
    def __init__(self):
        self.val = ""

    def update(self, data: str):
        if len(data) > len(self.val):
            self.val = data


# same logic, but different word
MaxWordEventListener = MaxLineEventListener

# default
NULL_LISTENER = EventListener()


class LineWithMaxWordEventListener(EventListener):
    def __init__(self):
        self.row = ""
        self.word = ""

    def update(self, data: str):
        words = data.split()
        if not words:
            return
        max_word = max(words, key=len)
        if len(max_word) > len(self.word):
            self.row = data
            self.word = max_word
