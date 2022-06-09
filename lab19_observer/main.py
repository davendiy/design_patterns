#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from src import FileReader, MaxWordEventListener, \
    MaxLineEventListener, LineWithMaxWordEventListener, Event

reader = FileReader('anthem.txt')

word_listener = MaxWordEventListener()
line_listener = MaxLineEventListener()
line_with_max_word_listener = LineWithMaxWordEventListener()

reader.subscribe(Event.WORD, word_listener)
reader.subscribe(Event.LINE, line_listener)
reader.subscribe(Event.WORD_IN_LINE, line_with_max_word_listener)

reader.read()

print(f'Max word: {word_listener.val}')
print(f'Max line: {line_listener.val}')
print(f'Line with max word: "{line_with_max_word_listener.row}" where "{line_with_max_word_listener.word}" is longest')
