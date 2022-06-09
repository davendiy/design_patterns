#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 09.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from src import GooglePay, Customer, PayPal

c = Customer(GooglePay)
c.pay("First address")
c.payment_system = PayPal
c.pay("Second address")
