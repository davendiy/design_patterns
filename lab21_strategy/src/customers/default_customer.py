#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

import uuid

from .base import CustomerBase
from ..payment_systems import PaymentSystemBase, PayPal, \
                                GooglePay
from typing import Type


class Customer(CustomerBase):

    def __init__(self, ps: Type[PaymentSystemBase]):
        self.payment_system = ps
        self.account_nums = {
            PayPal: uuid.uuid4(),
            GooglePay: uuid.uuid4()
        }

    # noinspection PyTypeChecker
    def pay(self, to):
        self.payment_system.pay(self.account_nums.get(self.payment_system), to)
