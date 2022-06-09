#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from abc import ABC, abstractmethod


class Creature(ABC):
    def defend_against_attack(self):
        self.pick_up_weapon()
        self.defense_action()
        self.move_to_safety()

    @abstractmethod
    def pick_up_weapon(self):
        pass

    @abstractmethod
    def defense_action(self):
        pass

    @abstractmethod
    def move_to_safety(self):
        pass


class Pirate(Creature):
    def pick_up_weapon(self):
        print("Pick up sword.")

    def defense_action(self):
        print("Defend with sword.")

    def move_to_safety(self):
        print("Return to the ship.")


class Troll(Creature):
    def pick_up_weapon(self):
        print("Pick up club.")

    def defense_action(self):
        print("Defend with club.")

    def move_to_safety(self):
        print("Return to the mountain.")
