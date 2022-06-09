#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .listeners import Event, EventListener
from collections import defaultdict


class FileReader:
    def __init__(self, path):
        self.path = path
        self.listeners = defaultdict(list)
        self._file = None

    def subscribe(self, event_type: Event, listener: EventListener):
        self.listeners[event_type].append(listener)

    def unsubscribe(self, event_type: Event, listener: EventListener):
        self.listeners[event_type].remove(listener)

    def publish(self, event_type: Event, data: str):
        for listener in self.listeners.get(event_type, []):
            listener: EventListener
            listener.update(data)

    def __enter__(self):
        self._file = open(self.path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

    def read(self):
        with self:
            lines = self._file.readlines()
            for line in lines:
                for word in line.split():
                    self.publish(Event.WORD, word)
                self.publish(Event.LINE, line)
                self.publish(Event.WORD_IN_LINE, line)
