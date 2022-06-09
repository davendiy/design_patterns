#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from src import MediaPlayer
import random


player = MediaPlayer()

for i in range(1000):
    player.add_track(f'track {i}')

attrs = [player.play, player.next, player.prev, player.pause, player.stop]
for _ in range(100):
    ind = random.randint(0, len(attrs)-1)
    attrs[ind]()
