

class Error:
    class InvalidSyntax(Exception):
        def __init__(self, instr, function_name, valid_input_description=""):
            self.message = f"""
                Invalid syntax in function \"{function_name}\":\n
                \t{instr}\n
                {valid_input_description}"""
            super().__init__(self.message)

    class UnknownInstruction(Exception):
        def __init__(self, instr, function_name, expected_type, valid_input_description=""):
            self.message = f"""
                Unknown instruction in function \"{function_name}\" of {type(instr)} type, expected {expected_type} type:\n
                \t{instr}\n
                {valid_input_description}"""
            super().__init__(self.message)
