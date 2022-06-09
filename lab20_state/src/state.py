#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .base import StateBase


class PlayState(StateBase):
    def play(self):
        pass

    def pause(self):
        print("Paused.")
        self.player.set_state(PauseState(self.player))

    def next(self):
        current = self.player.get_current_track_num()
        self.player.set_current_track_num(current + 1)
        print(f"Playing next track: {self.player.get_current_track()}")

    def prev(self):
        current = self.player.get_current_track_num()
        self.player.set_current_track_num(current - 1)
        print(f"Playing prev track: {self.player.get_current_track()}")

    def stop(self):
        print("Stopped.")
        self.player.set_state(StopState(self.player))


class PauseState(StateBase):
    def play(self):
        print(f"Resumed playing : {self.player.get_current_track()}")
        self.player.set_state(PlayState(self.player))

    def next(self):
        current = self.player.get_current_track_num()
        self.player.set_current_track_num(current + 1)
        print(f"Next track: {self.player.get_current_track()}")
        self.player.set_state(StopState(self.player))

    def prev(self):
        current = self.player.get_current_track_num()
        self.player.set_current_track_num(current - 1)
        print(f"Prev track: {self.player.get_current_track()}")
        self.player.set_state(StopState(self.player))

    def stop(self):
        pass

    def pause(self):
        pass


class StopState(StateBase):
    def play(self):
        self.player.set_state(PlayState(self.player))
        print(f"Playing from the beginning: {self.player.get_current_track()}")

    def next(self):
        current = self.player.get_current_track_num()
        self.player.set_current_track_num(current + 1)
        print(f"Next track: {self.player.get_current_track()}")

    def prev(self):
        current = self.player.get_current_track_num()
        self.player.set_current_track_num(current - 1)
        print(f"Prev track: {self.player.get_current_track()}")

    def stop(self):
        pass

    def pause(self):
        pass
