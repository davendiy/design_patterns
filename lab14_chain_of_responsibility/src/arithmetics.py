#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

import abc
import dataclasses
from typing import Union

from .base import BaseHandler, HandlingError


@dataclasses.dataclass
class Unary:
    op: str
    operand: str
    op_type = "unary"


@dataclasses.dataclass
class Binary:
    op: str
    left: str
    right: str
    op_type = "binary"


Op = Union[Unary, Binary]


class ArithmeticHandler(BaseHandler):
    target_op = "__DEFAULT"
    target_op_type = "__DEFAULT"

    @abc.abstractmethod
    def _handle(self, obj: Op):
        pass

    def handle(self, obj: Op):
        if obj.op == self.target_op and obj.op_type == self.target_op_type:
            return self._handle(obj)
        if self.next is not None:
            return self.next.handle(obj)
        else:
            raise HandlingError(f"Unable to handle op: {obj}")


class Plus(ArithmeticHandler):
    target_op = "+"
    target_op_type = "binary"

    def _handle(self, obj: Op):
        assert isinstance(obj, Binary)
        return int(obj.left) + int(obj.right)

class Minus(ArithmeticHandler):
    target_op = "-"
    target_op_type = "binary"

    def _handle(self, obj: Op):
        assert isinstance(obj, Binary)
        return int(obj.left) - int(obj.right)


class Neg(ArithmeticHandler):
    target_op = "-"
    target_op_type = "unary"

    def _handle(self, obj: Op):
        assert isinstance(obj, Unary)
        return -int(obj.operand)


class Mul(ArithmeticHandler):
    target_op = "*"
    target_op_type = "binary"

    def _handle(self, obj: Op):
        assert isinstance(obj, Binary)
        return int(obj.left) * int(obj.right)
