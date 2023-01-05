

class Token:
    # Primitives
    class String:
        def __init__(self, string):
            self.string = string  # type: str

        def __str__(self):
            return f"Token.String({self.string})"

        def __eq__(self, other):
            return (
                isinstance(other, Token.String)
                and self.string == other.string)

    class Boolean:
        def __init__(self, boolean):
            self.boolean = boolean  # type: str

        def __str__(self):
            return f"Token.Boolean({self.boolean})"

        def __eq__(self, other):
            return (
                isinstance(other, Token.Boolean)
                and self.boolean == other.boolean)

    class Integer:
        def __init__(self, integer):
            self.integer = integer  # type: str

        def __str__(self):
            return f"Token.Integer({self.integer})"

        def __eq__(self, other):
            return (
                isinstance(other, Token.Integer)
                and self.integer == other.integer)

    # Variable
    class Variable:
        def __init__(self, variable):
            self.variable = variable  # type: str

        def __str__(self):
            return f"Token.Variable({self.variable})"

        def __eq__(self, other):
            return (
                isinstance(other, Token.Variable)
                and self.variable == other.variable)

    # Reserved Symbols/Words
    class Newline:
        def __str__(self):
            return f"Token.Newline()"

        def __eq__(self, other):
            return isinstance(other, Token.Newline)

    class Indent:
        def __str__(self):
            return f"Token.Indent()"

        def __eq__(self, other):
            return isinstance(other, Token.Indent)

    class Dedent:
        def __str__(self):
            return f"Token.Dedent()"

        def __eq__(self, other):
            return isinstance(other, Token.Dedent)

    class Def:
        def __str__(self):
            return f"Token.Def()"

        def __eq__(self, other):
            return isinstance(other, Token.Def)

    class Comma:
        def __str__(self):
            return f"Token.Comma()"

        def __eq__(self, other):
            return isinstance(other, Token.Comma)

    class Colon:
        def __str__(self):
            return f"Token.Colon()"

        def __eq__(self, other):
            return isinstance(other, Token.Colon)

    class OpenParens:
        def __str__(self):
            return f"Token.OpenParens()"

        def __eq__(self, other):
            return isinstance(other, Token.OpenParens)

    class CloseParens:
        def __str__(self):
            return f"Token.CloseParens()"

        def __eq__(self, other):
            return isinstance(other, Token.CloseParens)

    class Equals:
        def __str__(self):
            return f"Token.Equals()"

        def __eq__(self, other):
            return isinstance(other, Token.Equals)

    # Operator
    class Operator:
        def __init__(self, op):
            self.op = op  # type: str

        def __str__(self):
            return f"Token.Operator({self.op})"

        def __eq__(self, other):
            return (
                isinstance(other, Token.Operator)
                and self.op == other.op)
