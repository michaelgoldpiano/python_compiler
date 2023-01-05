import os

# (Optional) Activate the venv:
#     . venv/Scripts/activate

test_commands = [
    # "python -m tests.test_tokenizer",
    # "python -m tests.test_lexer",
    # "python -m tests.test_parser",
    "python -m tests.test_normalizer",
    # "python -m tests.test_assembler",
    # "python -m tests.test_unparser(att)",
]

for command in test_commands:
    os.system(command)
