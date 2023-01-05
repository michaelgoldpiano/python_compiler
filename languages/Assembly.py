

binary_operators = {
    "+": Assembly.Add(),
}


class Assembly:
    # Addressing Modes
    class Register:
        def __init__(self, register: str):
            self.register = register

    class RegisterValue:
        def __init__(self, register: str):
            self.register = register

    # Scaled-indexed is used for stack base ptr accessed by an offset of a scaled memory size.
    # eg. (base + (index * scale))
    class ScaledIndexed:
        def __init__(self, base: str, index: str, scale: int = 8):
            self.base = base  # register
            self.index = index  # register
            self.scale = scale  # int

    # Immediates
    class Integer:
        def __init__(self, integer):
            self.integer = integer

    class String:
        def __init__(self, string):
            self.string = string

    class StringDeclare:
        def __init__(self, string):
            self.string = string

    # BinaryOp
    class Add:
        def __init__(self, destination, source):
            self.destination = destination
            self.source = source

    class Sub:
        def __init__(self, destination, source):
            self.destination = destination
            self.source = source

    # Result stored in %rax
    class Mul:
        def __init__(self, source):
            self.source = source

    # Quotient stored in %rax, Remainder stored in %rdx
    class Div:
        def __init__(self, source):
            self.source = source

    # UnaryOp
    class Neg:
        def __init__(self, destination):
            self.destination = destination

    # Functionality
    class Mov:
        def __init__(self, destination, source):
            self.destination = destination
            self.source = source

    class Call:
        def __init__(self, label):
            self.label = label

    class Push:
        def __init__(self, source):
            self.source = source

    class Pop:
        def __init__(self, destination):
            self.destination = destination

    class Ret:
        def __init__(self):
            pass

    class Label:
        def __init__(self, label, instructions):
            self.label = label
            self.instructions = instructions

    # Set condition codes according to s1 - s2
    class Cmp:
        def __init__(self, s1, s2):
            self.s1 = s1
            self.s2 = s2

    # Jump
    class Jmp:
        def __init__(self, label):
            self.label = label

    class Jne:
        def __init__(self, label):
            self.label = label
