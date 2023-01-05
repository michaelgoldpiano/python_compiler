# Author: Michael Gold
# Created: 11/03/2022
# Purpose: Turn tokenized input into a lexed stream of Tokens.

# Tokenizer breaks a stream of text into tokens.
# Lexer is a Tokenizer, but also attaches extra content to the tokens.
# Eg. '5' is a number, 'hello' is a string literal, etc.
# This also turns tabs into indents/dedents

# Types of data to be lexed:
# Reserved Words/Symbols (\n, \t, def, :, (, ), =)
# Infix Operators (+, -, *, /, %)
# Primitive Data Types (booleans, strings, integers)
# Variables (eg. x)

from languages.Token import Token


operators = ["+", "-", "*", "/", "%"]


def match_newline(words, num_indents):
    tokens = [Token.Newline()]

    # Count Indent/Dedent
    curr_num_indents = 0
    while len(words) > 0:
        match words:
            case ["\n", *tail]:
                words = tail
                curr_num_indents = 0
            case [("\t" | "    "), *tail]:
                words = tail
                curr_num_indents += 1
            case [" ", *_]:
                raise SyntaxError("Snake syntax cannot have leading spaces in a line")
            case [*_]:
                break

    # Append Indent/Dedent
    while curr_num_indents != num_indents:
        if curr_num_indents > num_indents:
            num_indents += 1
            tokens.append(Token.Indent())
        elif curr_num_indents < num_indents:
            num_indents -= 1
            tokens.append(Token.Dedent())

    return tokens, words, num_indents


# Params: An array of strings to tokenize.
# Returns: The matched string from the input,
#          The remained of the string.
# Purpose: Partitions the string into a tokenizable part and remainder.
def match_word(words):
    match words:
        # Loose tab error
        case["\t", *_]: raise SyntaxError("Cannot have a tab in the middle of a statement")

        # Primitives
        case ["\"", string, "\"", *tail] | ["\'", string, "\'", *tail]: return Token.String(string), tail
        case [("True" | "False") as boolean, *tail]: return Token.Boolean(boolean), tail
        case [integer, *tail] if integer.isnumeric(): return Token.Integer(integer), tail

        # Reserved words
        case ["def", *tail]: return Token.Def(), tail
        case [",", *tail]: return Token.Comma(), tail
        case [":", *tail]: return Token.Colon(), tail
        case ["(", *tail]: return Token.OpenParens(), tail
        case [")", *tail]: return Token.CloseParens(), tail
        case ["=", *tail]: return Token.Equals(), tail

        # Operator
        case [("+" | "-" | "*" | "/" | "%") as operator, *tail]: return Token.Operator(operator), tail

        # Catch-all
        case [variable, *tail]: return Token.Variable(variable), tail


def lex(words):
    tokens = []
    num_indents = 0

    while len(words) > 0:
        match words:
            # Newline and Indent/Dedent
            case ["\n", *tail]:
                new_tokens, words, num_indents = match_newline(tail, num_indents)
                tokens.extend(new_tokens)

            case [*tail]:
                new_token, words = match_word(tail)
                tokens.append(new_token)

    return tokens
