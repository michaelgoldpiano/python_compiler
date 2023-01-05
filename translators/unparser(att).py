"""
Unparser from Assembly to string output assembly.
"""

from typing import List, Tuple
from languages.Assembly import Assembly


def unparse_all(assembly_list: List[Assembly]) -> Tuple[str, List[Assembly]]:
    """
    Recursive helper function that unparses Assembly instructions into string assembly instructions.

    Args:
        assembly_list: List of Assembly instructions to unparse.

    Returns:
        List of string machine code instructions.
        List of remaining Assembly instructions to be unparsed.

    Raises:
        Nothing.
    """
    match assembly_list:
        # Register
        case [Assembly.Register(register), tail]:
            return "%" + register, [tail]
        # RegisterValue
        case [Assembly.RegisterValue(register), tail]:
            return "(%" + register + ")", [tail]
        # ScaledIndexed
        case [Assembly.ScaledIndexed(base, index, scale), tail]:
            return "(%" + base + ", %" + index + ", " + scale + ")", [tail]

        # Integer
        case [Assembly.Integer(integer), tail]:
            return "$" + integer, [tail]
        # String
        case [Assembly.String(string), tail]:
            return "$_str_" + string, [tail]
        # StringDeclare
        case [Assembly.StringDeclare(string), tail]:
            return ".string \"" + string + "\"", [tail]

        # Add
        case [Assembly.Add(destination, source), tail]:
            dst, _ = unparse_all([destination])
            src, _ = unparse_all([source])
            return "addq " + src + ", " + dst, [tail]
        # Sub
        case [Assembly.Sub(destination, source), tail]:
            dst, _ = unparse_all([destination])
            src, _ = unparse_all([source])
            return "subq " + src + ", " + dst, [tail]
        # Mul
        case [Assembly.Mul(source), tail]:
            src, _ = unparse_all([source])
            return "mulq " + src, [tail]
        # Div
        case [Assembly.Div(source), tail]:
            src, _ = unparse_all([source])
            return "divq " + src, [tail]
        # Neg
        case [Assembly.Neg(destination), tail]:
            dst, _ = unparse_all([destination])
            return "negq " + dst, tail

        # Mov
        case [Assembly.Mov(destination, source), tail]:
            dst, _ = unparse_all([destination])
            src, _ = unparse_all([source])
            return "movq " + src + ", " + dst, tail
        # Call
        case [Assembly.Call(label), tail]:
            return "call " + label, tail
        # Push
        case [Assembly.Push(source), tail]:
            src, _ = unparse_all([source])
            return "push " + src, tail
        # Pop
        case [Assembly.Pop(destination), tail]:
            dst, _ = unparse_all([destination])
            return "pop " + dst, tail
        # Ret
        case [Assembly.Ret(), tail]:
            return "ret", [tail]
        # Label
        case [Assembly.Label(label, instructions), tail]:
            mc = [label + ":"]
            while instructions:
                new_mc, instructions = unparse_all(instructions)
                mc.extend("\t" + new_mc)
            mc = "\n".join(mc)
            return mc, tail
        # Cmp
        case [Assembly.Cmp(s1, s2), tail]:
            new_s1, _ = unparse_all(s1)
            new_s2, _ = unparse_all(s2)
            return "cmp " + new_s2 + ", " + new_s1, tail
        # Jmp
        case [Assembly.Jmp(label), tail]:
            return "jmp " + label, tail
        # Jne
        case [Assembly.Jne(label), tail]:
            return "jne " + label, tail


def unparse(assembly_list: List[Assembly]) -> str:
    """
    Unparses all assembly instructions into machine code instructions.

    Args:
        assembly_list: List of Assembly instructions to unparse.

    Returns:
        List of string machine code instructions.

    Raises:
        Nothing.
    """
    mc = ""
    while assembly_list:
        new_mc, assembly = unparse_all(assembly_list)
        mc += new_mc
    return mc
