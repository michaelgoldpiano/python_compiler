

from translators.lexer import lex
from languages.Token import Token


# TODO: Order of operations (**, */, +-)

text_inputs = [
    ["\n"],
    ["\n", "\t", "    "],
    ["\n", "\t", "1", "\n", "2"],
    ["\"", "string", "\"", "True", "False", "4"],
    ["def", ",", ":", "(", ")", "="],
    ["+", "-", "*", "/", "%"],
    ["variable"],
]

expected_outputs = [
    [Token.Newline()],
    [Token.Newline(), Token.Indent(), Token.Indent()],
    [Token.Newline(), Token.Indent(), Token.Integer("1"), Token.Newline(), Token.Dedent(), Token.Integer("2")],
    [Token.String("string"), Token.Boolean("True"), Token.Boolean("False"), Token.Integer("4")],
    [Token.Def(), Token.Comma(), Token.Colon(), Token.OpenParens(), Token.CloseParens(), Token.Equals()],
    [Token.Operator("+"), Token.Operator("-"), Token.Operator("*"), Token.Operator("/"), Token.Operator("%")],
    [Token.Variable("variable")],
]


def test_lexer():
    for text, expected in zip(text_inputs, expected_outputs):
        result = lex(text)

        for r, e in zip(result, expected):
            if r != e:
                print(f"result {type(r)} did not equal expected type {type(e)}")


test_lexer()
