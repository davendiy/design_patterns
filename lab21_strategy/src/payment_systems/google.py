#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from .base import PaymentSystemBase


class GooglePay(PaymentSystemBase):

    @staticmethod
    def pay(from_, to):
        print(f'Paying from {from_} to {to} using Google Pay')
