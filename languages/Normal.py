

from typing import List


class Normal:
    class VarMemory:
        def __init__(self, number):
            self.number = number  # type: int

        def __str__(self):
            return f"Normal.VarMemory({self.number})"

        def __eq__(self, other):
            return (
                isinstance(other, Normal.VarMemory)
                and self.number == other.number)

        __match_args__ = ("number",)

    class ParamMemory:
        def __init__(self, number):
            self.number = number  # type: int

        def __str__(self):
            return f"Normal.ParamMemory({self.number})"

        def __eq__(self, other):
            return (
                isinstance(other, Normal.ParamMemory)
                and self.number == other.number)

        __match_args__ = ("number",)

    class TempMemory:
        def __init__(self, number):
            self.number = number  # type: int

        def __str__(self):
            return f"Normal.TempMemory({self.number})"

        def __eq__(self, other):
            return (
                isinstance(other, Normal.TempMemory)
                and self.number == other.number)

        __match_args__ = ("number",)

    class ReturnMemory:
        def __init__(self, number):
            self.number = number  # type: int

        def __str__(self):
            return f"Normal.ReturnMemory({self.number})"

        def __eq__(self, other):
            return (
                isinstance(other, Normal.ReturnMemory)
                and self.number == other.number)

        __match_args__ = ("memory",)

    class String:
        def __init__(self, string):
            self.string = string

        def __str__(self):
            return f"Normal.String({self.string})"

        def __eq__(self, other):
            return (
                isinstance(other, Normal.String)
                and self.string == other.string)

        __match_args__ = ("string",)

    class Boolean:
        def __init__(self, boolean):
            self.boolean = boolean

        def __str__(self):
            return f"Normal.Boolean({self.boolean})"

        def __eq__(self, other):
            return (
                isinstance(other, Normal.Boolean)
                and self.boolean == other.boolean)

        __match_args__ = ("boolean",)

    class Integer:
        def __init__(self, integer):
            self.integer = integer

        def __str__(self):
            return f"Normal.Integer({self.integer})"

        def __eq__(self, other):
            return (
                isinstance(other, Normal.Integer)
                and self.integer == other.integer)

        __match_args__ = ("integer",)

    class Call:
        def __init__(self, name, params):
            self.name = name
            self.params = params

        def __str__(self):
            return f"Normal.Call({self.name}, {self.params})"

        def __eq__(self, other):
            return (
                isinstance(other, Normal.Call)
                and self.name == other.name
                and self.params == other.params)

        __match_args__ = ("name", "params")

    class BinaryOp:
        def __init__(self, op, memory1, memory2):
            self.op = op
            self.memory1 = memory1
            self.memory2 = memory2

        def __str__(self):
            return f"Normal.BinaryOp({self.op}, {self.memory1}, {self.memory2})"

        def __eq__(self, other):
            return (
                isinstance(other, Normal.BinaryOp)
                and self.op == other.op
                and self.memory1 == other.memory1
                and self.memory2 == other.memory2)

        __match_args__ = ("op", "memory1", "memory2")

    class UnaryOp:
        def __init__(self, op, memory):
            self.op = op
            self.memory = memory

        def __str__(self):
            return f"Normal.UnaryOp({self.op}, {self.memory})"

        def __eq__(self, other):
            return (
                isinstance(other, Normal.UnaryOp)
                and self.op == other.op
                and self.memory == other.memory)

        __match_args__ = ("op", "memory")

    class FunDef:
        def __init__(self, name, params, inner_instrs):
            self.name = name
            self.params = params
            self.inner_instrs = inner_instrs

        def __str__(self):
            return f"Normal.FunDef({self.name}, {self.params}, {self.inner_instrs})"

        def __eq__(self, other):
            return (
                isinstance(other, Normal.FunDef)
                and self.name == other.name
                and self.params == other.params
                and self.inner_instrs == other.inner_instrs)

        __match_args__ = ("name", "params", "inner_instrs")

    class Assign:
        def __init__(self, destination, source):
            self.destination = destination
            self.source = source

        def __str__(self):
            return f"Normal.Assign({self.destination}, {self.source})"

        def __eq__(self, other):
            return (
                isinstance(other, Normal.Assign)
                and self.destination == other.destination
                and self.source == other.source)

        __match_args__ = ("destination", "source")
