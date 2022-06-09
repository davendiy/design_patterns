#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from abc import ABC, abstractmethod


class PlayerBase(ABC):

    @abstractmethod
    def get_current_track(self):
        pass

    @abstractmethod
    def get_current_track_num(self):
        pass

    @abstractmethod
    def set_current_track_num(self, num: int):
        pass

    @abstractmethod
    def get_tracks(self):
        pass

    @abstractmethod
    def add_track(self, track):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def prev(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state



class StateBase(ABC):
    def __init__(self, player: PlayerBase):
        self.player = player

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def prev(self):
        pass

    @abstractmethod
    def stop(self):
        pass
