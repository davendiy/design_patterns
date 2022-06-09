#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .base import PlayerBase
from .state import StopState


class MediaPlayer(PlayerBase):
    def __init__(self):
        self.tracks = []
        self.state = StopState(self)
        self._current_track_num = 0

    def get_current_track(self):
        return self.tracks[self._current_track_num]

    def set_current_track_num(self, num):
        if num < 0 or num >= len(self.tracks):
            return
        self._current_track_num = num

    def get_current_track_num(self):
        return self._current_track_num

    def get_tracks(self):
        return self.tracks

    def add_track(self, track):
        self.tracks.append(track)

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def play(self):
        self.state.play()

    def pause(self):
        self.state.pause()

    def next(self):
        self.state.next()

    def prev(self):
        self.state.prev()

    def stop(self):
        self.state.stop()
