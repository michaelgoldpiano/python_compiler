

# Compiler *"In Python For Python"*


## Purpose
This is a personal project for compiling Python code into Assembly code.
The project is written in Python, leveraging the new Python feature of structural pattern matching.
This does not compile all of Python, as Python is enormous and beyond the
scope of a personal project.  I have named the generalized subset of Python
that is compiled here "Snake."


## Supported Instructions and Types
- strings
- booleans
- integers
- variables
- calls
- binary operations (+, -, *, / %)
- unary operations (+, -)
- function definitions
- assignments


## Steps Overview

### Raw Python String Input
The input is a string of valid Python code.
```python
"""
x = 1 + 2
print(x)
"""
```

### Tokenizing
The tokenizer turns the string input into a list of strings.
Strings are broken by spaces, newlines, keywords, and special characters.
```python
[
    "x", "=", "1", "+", "2", "\n",
    "print", "(", "x", ")",
]
```

### Lexing
The lexer labels each string by its intended purpose.
```python
[
    Variable("x"), Equals(), Integer("1"), Operator("+"), Integer("2"), Newline(),
    Variable("print"), OpenParens(), Variable("x"), CloseParens(),
]
```

### Parsing
The parser creates an instruction tree, where instructions contain other instructions.
Mathematical order of operations is determined here.
```python
[
    Assign(Variable("x"), BinaryOp(Operator("+"), Integer("1"), Integer("2"))),
    Call(Variable("print"), [Variable("x")]),
]
```

### Normalizing
The normalizer replaces variables with memory slots, in preparation for assembly memory management.
All literal values (integers, strings, booleans, etc) are moved to memory before being used.
```python
[
    Assign(TempMemory(0), Integer("1")),
    Assign(TempMemory(1), Integer("2")),
    Assign(VarMemory(0), BinaryOp(Operator("+"), TempMemory(0), TempMemory(1))),
]
```

### Assembling
The assembler turns generalized memory addresses into specific addresses used in Assembly.
All instructions are one-to-one with actual assembly.
```Python
[
    Mov(Rax(), Literal("1")),
    Mov(Rcx(), Literal("2")),
    Add(Rax(), Rcx()),
    Mov(Rbx(), Rax()),
]
```

### Raw Assembly String Output
The output is a string of valid Assembly code.
```
"""
mov %rax $1
mov %rcx $2
add %rax %rcx
mov %rbx %rax
"""
```