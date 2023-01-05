# Author: Michael Gold
# Created: 11/03/2022
# Purpose: Turn raw Snake input into tokenized stream.

# Tokenizer breaks a stream of text into tokens.
# Lexer is a Tokenizer, but also attaches extra content to the tokens.
# E.g. '5' is a number, 'hello' is a string literal, etc.

# Types of data to be tokenized:
# Spacing (" ", "\n", "\t")
# Reserved Symbols ("=", ",", ":", "(", ")", "\"", "\'")
# Infix Operators ("+", "-", "*", "/", "%")
# Comments ("#")


# Params:
# Returns:
# Purpose: Split a string by space, newline, tab, and reserved word.
def split(text):
    reserved_words = {
        " ", "\n", "\t",
        "=", ",", ":", "(", ")", "\"", "\'",
        "+", "-", "*", "/", "%",
        "#",
    }

    match text:
        # Transform 4 spaces into tab
        case [" ", " ", " ", " ", *tail]:
            return "\t", tail

        # Remove spaces
        case [" ", *tail]:
            return None, tail

        # Remove comments
        case ["#", *tail]:
            while len(tail) > 0:
                t = tail[0]
                if t == "\n":
                    break
                tail.pop(0)
            return None, tail

        # Capture symbol
        case [char, *tail] if char in reserved_words:
            return char, tail

        # Capture word
        case [word, *tail]:
            while len(tail) > 0:
                t = tail[0]
                if t in reserved_words:
                    break
                tail.pop(0)
                word += t
            return word, tail


# Params:
# Returns:
# Purpose: Aggregate string tokens.
def tokenize(text):
    text = [*text]

    words = []
    while len(text) > 0:
        curr_word, text = split(text)
        if curr_word is not None:
            words.append(curr_word)

    return words
