#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from src import PostComa, PostWord, PostSpace, PostExclaim


test = PostWord('', 'Hello')
test = PostComa(test)
test = PostSpace(test)
test = PostWord(test, 'world')
test = PostExclaim(test)

print(test)
