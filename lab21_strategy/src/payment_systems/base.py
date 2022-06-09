#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi
from abc import ABC, abstractmethod


class PaymentSystemBase(ABC):

    @staticmethod
    @abstractmethod
    def pay(from_, to):
        pass
