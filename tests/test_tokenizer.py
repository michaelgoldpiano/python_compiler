

from translators.tokenizer import tokenize


text_inputs = [
    " \n\t    ",
    "=,:()\"\'",
    "+-*/%",

    "    ",
    " ",
    "# comment",
    "word",
    
    "word1 word2",
    "word1 = word2 + # hello world"
]

expected_outputs = [
    ["\n", "\t", "\t"],
    ["=", ",", ":", "(", ")", "\"", "\'"],
    ["+", "-", "*", "/", "%"],

    ["\t"],
    [],
    [],
    ["word"],

    ["word1", "word2"],
    ["word1", "=", "word2", "+"]
]


def test_tokenizer():
    for text, expected in zip(text_inputs, expected_outputs):
        result = tokenize(text)

        if result != expected:
            print(f"result {result} did not equal expected {expected}")


test_tokenizer()
