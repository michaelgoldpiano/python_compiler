

from typing import List


class Snake:
    binary_operators = [
        "+",
        "-",
        "*",
        "/",
        "%",
    ]
    unary_operators = [
        "+",
        "-",
    ]

    class String:
        def __init__(self, string):
            self.string = string  # type: str

        def __str__(self):
            return f"Snake.String({self.string})"

        def __eq__(self, other):
            return (
                isinstance(other, Snake.String)
                and self.string == other.string)

        __match_args__ = ("string",)

    class Boolean:
        def __init__(self, boolean):
            self.boolean = boolean  # type: str

        def __str__(self):
            return f"Snake.Boolean({self.boolean})"

        def __eq__(self, other):
            return (
                isinstance(other, Snake.Boolean)
                and self.boolean == other.boolean)

        __match_args__ = ("boolean",)

    class Integer:
        def __init__(self, integer):
            self.integer = integer  # type: str

        def __str__(self):
            return f"Snake.Integer({self.integer})"

        def __eq__(self, other):
            return (
                isinstance(other, Snake.Integer)
                and self.integer == other.integer)

        __match_args__ = ("integer",)

    class Variable:
        def __init__(self, variable):
            self.variable = variable  # type: str

        def __str__(self):
            return f"Snake.Variable({self.variable})"

        def __eq__(self, other):
            return (
                isinstance(other, Snake.Variable)
                and self.variable == other.variable)

        __match_args__ = ("variable",)

    class Call:
        def __init__(self, name, params):
            self.name = name  # type: str
            self.params = params  # type: List[Snake]

        def __str__(self):
            return f"Snake.Call({self.name}, {self.params})"

        def __eq__(self, other):
            return (
                isinstance(other, Snake.Call)
                and self.name == other.name
                and self.params == other.params)

        __match_args__ = ("name", "params")

    class BinaryOp:
        def __init__(self, op, value1, value2):
            self.op = op  # type: str
            self.value1 = value1  # type: Snake
            self.value2 = value2  # type: Snake

        def __str__(self):
            return f"Snake.BinaryOp({self.op}, {self.value1}, {self.value2})"

        def __eq__(self, other):
            return (
                isinstance(other, Snake.BinaryOp)
                and self.op == other.op
                and self.value1 == other.value1
                and self.value2 == other.value2)

        __match_args__ = ("op", "value1", "value2")

    class UnaryOp:
        def __init__(self, op, value):
            self.op = op  # type: str
            self.value = value  # type: Snake

        def __str__(self):
            return f"Snake.UnaryOp({self.op}, {self.value})"

        def __eq__(self, other):
            return (
                isinstance(other, Snake.UnaryOp)
                and self.op == other.op
                and self.value == other.value)

        __match_args__ = ("op", "value")

    class FunDef:
        def __init__(self, name, params, inner_instrs):
            self.name = name  # type: str
            self.params = params  # type: List[Snake]
            self.inner_instrs = inner_instrs  # type: List[Snake]

        def __str__(self):
            return f"Snake.FunDef({self.name}, {self.params}, {self.inner_instrs})"

        def __eq__(self, other):
            return (
                isinstance(other, Snake.FunDef)
                and self.name == other.name
                and self.params == other.params
                and self.inner_instrs == other.inner_instrs)

        __match_args__ = ("name", "params", "inner_instrs")

    class Assign:
        def __init__(self, variable, value):
            self.variable = variable  # type: Snake.Variable
            self.value = value  # type: Snake

        def __str__(self):
            return f"Snake.Assign({self.variable}, {self.value})"

        def __eq__(self, other):
            return (
                isinstance(other, Snake.Assign)
                and self.variable == other.variable
                and self.value == other.value)

        __match_args__ = ("variable", "value")
