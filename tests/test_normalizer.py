

from translators.normalizer import normalize
from languages.Snake import Snake
from languages.Normal import Normal


tests = [
    # FunDef [def name(x): \n \t x = 0]
    (
        [Snake.FunDef("name", [Snake.Variable("x")], [Snake.Assign(Snake.Variable("x"), Snake.Integer("0"))])],
        [
            Normal.FunDef(
                "name",
                [Normal.ParamMemory(0)],
                [
                    Normal.Assign(Normal.VarMemory(0), Normal.ParamMemory(0)),
                    Normal.Assign(Normal.VarMemory(0), Normal.Integer("0")),
                ]
            ),
        ],
    ),

    # Assign [x = 0]
    (
        [Snake.Assign(Snake.Variable("x"), Snake.Integer("0"))],
        [Normal.Assign(Normal.VarMemory(0), Normal.Integer("0"))],
    ),

    # Call (as a statement) [x = 0 \n name(x)]
    (
        [
            Snake.Assign(Snake.Variable("x"), Snake.Integer("0")),
            Snake.Call("name", [Snake.Variable("x")]),
        ],
        [
            Normal.Assign(Normal.VarMemory(0), Normal.Integer("0")),
            Normal.Assign(Normal.ParamMemory(0), Normal.VarMemory(0)),  # TODO: Can be optimized away
            Normal.Call("name", [Normal.ParamMemory(0)]),
        ],
    ),

    # Call (as an expression) [x = 0 \n y = name(x)]
    (
        [
            Snake.Assign(Snake.Variable("x"), Snake.Integer("0")),
            Snake.Assign(Snake.Variable("y"), Snake.Call("name", [Snake.Variable("x")])),
        ],
        [
            Normal.Assign(Normal.VarMemory(0), Normal.Integer("0")),
            Normal.Assign(Normal.ParamMemory(0), Normal.VarMemory(0)),  # TODO: Can be optimized away
            Normal.Assign(Normal.VarMemory(1), Normal.Call("name", [Normal.ParamMemory(0)])),  # TODO: Can be optimized to reuse memory
        ],
    ),

    # String [x = "hello"]
    (
        [Snake.Assign(Snake.Variable("x"), Snake.String("hello"))],
        [Normal.Assign(Normal.VarMemory(0), Normal.String("hello"))],
    ),

    # Boolean [x = True]
    (
        [Snake.Assign(Snake.Variable("x"), Snake.Boolean("True"))],
        [Normal.Assign(Normal.VarMemory(0), Normal.Integer("1"))],
    ),

    # Integer [x = 0]
    (
        [Snake.Assign(Snake.Variable("x"), Snake.Integer("0"))],
        [Normal.Assign(Normal.VarMemory(0), Normal.Integer("0"))],
    ),

    # Variable [x = 0 \n y = x]
    (
        [
            Snake.Assign(Snake.Variable("x"), Snake.Integer("0")),
            Snake.Assign(Snake.Variable("y"), Snake.Variable("x")),
        ],
        [
            Normal.Assign(Normal.VarMemory(0), Normal.Integer("0")),
            Normal.Assign(Normal.VarMemory(1), Normal.VarMemory(0)),
        ],
    ),

    # BinaryOp [x = 1 + 2]
    (
        [Snake.Assign(Snake.Variable("x"), Snake.BinaryOp("+", Snake.Integer("1"), Snake.Integer("2")))],
        [
            Normal.Assign(Normal.TempMemory(0), Normal.Integer("1")),
            Normal.Assign(Normal.TempMemory(1), Normal.Integer("2")),
            Normal.Assign(Normal.VarMemory(0), Normal.BinaryOp("+", Normal.TempMemory(0), Normal.TempMemory(1))),
        ],
    ),

    # UnaryOp [x = -1]
    (
        [Snake.Assign(Snake.Variable("x"), Snake.UnaryOp("-", Snake.Integer("1")))],
        [
            Normal.Assign(Normal.TempMemory(0), Normal.Integer("1")),
            Normal.Assign(Normal.VarMemory(0), Normal.UnaryOp("-", Normal.TempMemory(0))),
        ],
    ),
]


def test_normalizer():
    for data, expected in tests:
        result = normalize(data)

        for r, e in zip(result, expected):
            if r != e:
                print(f"result {type(r)} did not equal expected type {type(e)}")


test_normalizer()
