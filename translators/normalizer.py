"""
This file converts Snake instructions into Normal form instructions.
"""


from typing import List, Dict, Tuple
from languages.Snake import Snake
from languages.Normal import Normal
from copy import deepcopy


class Environment:
    def __init__(self):
        self.mem_map = {}  # type: Dict[str, Normal.VarMemory]
        self.mem_counter = 0  # type: int

        # Note: mem_counter is necessary (instead of finding size of mem_map), since
        #       in a larger scope a variable can have data stored in a memory slot
        #       that cannot be overwritten in the local scope.

    def new_mem(self, var_name: str) -> Normal.VarMemory:
        """
        Generates a new Normal form memory for a variable.

        Args:
            :param var_name: Str name of the variable to generate memory for and store.

        Returns:
            :return: Normal form of the newly generated memory for the variable.

        Raises:
            Nothing.
        """
        # TODO: Check if var_name already contains value... if so, skip update.

        new_memory = Normal.VarMemory(self.mem_counter)
        self.mem_counter += 1
        self.mem_map[var_name] = new_memory
        return self.mem_map[var_name]

    def get_mem(self, var_name: str) -> None | Normal.VarMemory:
        """
        Finds the Normal form memory associated with a variable.

        Args:
            :param var_name: Str name of the variable to find within scope.

        Returns:
            :return: Normal form memory associated with the input variable if that variable is in scope,
                     None otherwise.

        Raises:
            Nothing.
        """
        if var_name not in self.mem_map:
            return None
        return self.mem_map[var_name]


def normalize_variable(variable: str, env: Environment) -> Normal.VarMemory:
    """
    Transforms a Variable instruction from Snake to Normal form.

    Args:
        :param variable:
        :param env:

    Returns:
        :return: Normal form of the variable's memory within scope.

    Raises:
        SyntaxError for uninitialized input variable
    """
    new_variable = env.get_mem(variable)

    # Error, uninitialized variable
    if new_variable is None:
        raise SyntaxError("Uninitialized variable \"" + variable + "\" was found.")

    # Find memory associated with the variable name
    return new_variable


def normalize_call(name: str, params: List[Snake], env: Environment) -> Tuple[Normal, List[Normal]]:
    """
    Transforms a Call instruction from Snake to Normal form.

    Args:
        :param name: Str name of the function.
        :param params: List of Snake expressions that are parameters to the function.
        :param env: Environment with the scope's available variable names.

    Returns:
        :return: Normal form of the normalized Call instruction.
        :return: List of Normal form intermediate instructions for setting up the call.

    Raises:
        Nothing.
    """
    new_intermediate_instrs = []
    new_params = []

    # Normalize parameters (can be any expression)
    for i, p in enumerate(params):
        # TODO: Store old values of the params to be replaced (used in the current function)

        curr_destination = Normal.ParamMemory(i)
        curr_instrs, _ = normalize_expression([p], env, curr_destination)

        # Save intermediate instructions and param memory
        new_intermediate_instrs += curr_instrs
        new_params += [curr_destination]

    # Create the call
    new_call = Normal.Call(name, new_params)
    return new_call, new_intermediate_instrs  # type: ignore


def normalize_expression(snake_list: List[Snake], env: Environment, destination: Normal) -> Tuple[List[Normal], List[Snake]]:
    """
    Turns a Snake expression into Normal form expressions.
    An expression resolves to a value, while a statement does not resolve to a value.
    (e.g. addition and function calls are considered expressions).
    (e.g. assignment and function definitions are considered statements).

    Args:
        :param snake_list: List of Snake instructions to normalize.
        :param env: Environment with the scope's available variable names.
        :param destination: Normal Memory where the result of the expression is to be stored.

    Returns:
        :return: List of normalized instructions.
        :return: List of remaining Snake instructions.

    Raises:
        SyntaxError when matching a statement where an expression is expected.
        SyntaxError when matching an unknown instruction.
    """
    match snake_list:
        # String
        case [Snake.String(string), *tail]:
            new_assign = Normal.Assign(destination, Normal.String(string))
            return [new_assign], tail  # type: ignore

        # Boolean
        case [Snake.Boolean(boolean), *tail]:
            # Convert boolean to integer
            new_int = {
                "False": "0",
                "True": "1",
            }[boolean]

            new_assign = Normal.Assign(destination, Normal.Integer(new_int))
            return [new_assign], tail  # type: ignore

        # Integer
        case [Snake.Integer(integer), *tail]:
            new_assign = Normal.Assign(destination, Normal.Integer(integer))
            return [new_assign], tail  # type: ignore

        # Variable
        case [Snake.Variable(variable), *tail]:
            new_variable = normalize_variable(variable, env)
            new_assign = Normal.Assign(destination, new_variable)
            return [new_assign], tail  # type: ignore

        # Call
        case [Snake.Call(name, params), *tail]:
            new_call, new_intermediate_instrs = normalize_call(name, params, env)
            new_assign = Normal.Assign(destination, new_call)
            return [*new_intermediate_instrs, new_assign], tail

        # Binary Operation
        case [Snake.BinaryOp(op, value1, value2), *tail]:
            curr_destination1 = Normal.TempMemory(0)
            curr_destination2 = Normal.TempMemory(1)

            # Normalize values
            new_intermediate_instrs1, _ = normalize_expression([value1], env, curr_destination1)
            new_intermediate_instrs2, _ = normalize_expression([value2], env, curr_destination2)

            # Assign the binary operation to the destination
            new_assign = Normal.Assign(destination, Normal.BinaryOp(op, curr_destination1, curr_destination2))
            return [*new_intermediate_instrs1, *new_intermediate_instrs2, new_assign], tail

        # Unary Operation
        case [Snake.UnaryOp(op, value), *tail]:
            curr_destination = Normal.TempMemory(0)

            # Normalize value
            new_intermediate_instrs, _ = normalize_expression([value], env, curr_destination)

            # Assign the unary operation to the destination
            new_assign = Normal.Assign(destination, Normal.UnaryOp(op, curr_destination))
            return [*new_intermediate_instrs, new_assign], tail

        # Statement
        case [_, *tail]:
            raise SyntaxError("Found a statement where there can only be expressions.")

        # Error
        case _:
            raise SyntaxError("Found an unknown instruction where a Normal form expression is expected.")


def normalize_statement(snake_list: List[Snake], env: Environment) -> Tuple[List[Normal], List[Snake], Environment]:
    """
    Turns a Snake statement into a Normal form statement.
    An expression resolves to a value, while a statement does not resolve to a value.
    (e.g. addition and function calls are considered expressions).
    (e.g. assignment and function definitions are considered statements).

    Args:
        :param snake_list: List of Snake instructions to normalize.
        :param env: Environment with the scope's available variable names.

    Returns:
        :return: List of normalized instructions.
        :return: List of remaining Snake instructions.
        :return: List of str variable names that are stored in the current environment.

    Raises:
        SyntaxError if a non-variable is found in the parameters of a function definition.
        SyntaxError when matching an unknown expression.
    """
    match snake_list:
        # Function Definition
        case [Snake.FunDef(name, params, inner_instrs), *tail]:
            inner_env = deepcopy(env)
            new_intermediate_instrs = []
            new_inner_instrs = []
            new_params = []

            # Normalize parameters (can only be a variable)
            for i, p in enumerate(params):
                match p:
                    # Must be a variable
                    case Snake.Variable(variable):

                        # Normalize param
                        new_param = Normal.ParamMemory(i)
                        new_params += [new_param]

                        # Update inner environment with new variable
                        new_variable = inner_env.new_mem(variable)

                        # Move param into persistent memory
                        new_assign = Normal.Assign(new_variable, new_param)
                        new_intermediate_instrs += [new_assign]

                    # Non-variable Error
                    case other if isinstance(other, Snake):
                        raise SyntaxError("Non-variable in function definition.")

                    # Error
                    case _:
                        raise SyntaxError("Found an unknown instruction where a Normal form variable parameter is expected.")

            # Normalize inner scope
            new_inner_instrs = normalize_all(inner_instrs, inner_env)

            # Normalize function definition
            new_fundef = Normal.FunDef(name, new_params, [*new_intermediate_instrs, *new_inner_instrs])
            return [new_fundef], tail, env  # type: ignore

        # Assign
        case [Snake.Assign(Snake.Variable(variable), value), *tail]:
            new_env = deepcopy(env)

            # Get memory location for assign
            curr_destination = new_env.get_mem(variable)
            if curr_destination is None:
                curr_destination = new_env.new_mem(variable)

            # Normalize left-hand side of the assign (expression normalization already does assignment)
            new_instrs, _ = normalize_expression([value], new_env, curr_destination)

            return new_instrs, tail, new_env

        # Call, as a statement
        case [Snake.Call(name, params), *tail]:
            new_call, new_intermediate_instrs = normalize_call(name, params, env)
            return [*new_intermediate_instrs, new_call], tail, env

        # Expression
        case [_, *tail]:
            return [], tail, env

        # Error
        case _:
            raise SyntaxError("Found an unknown instruction where a Normal form statement is expected.")


def normalize_all(snake_list: List[Snake], env: Environment) -> List[Normal]:
    """
    Helper function that normalizes Snake instructions into Normal form instructions.

    Args:
        :param snake_list: List of Snake instructions to normalize.
        :param env: Environment with the scope's available variable names.

    Returns:
        :return: List of normalized instructions.

    Raises:
        Nothing.
    """
    normal_list = []

    while snake_list:
        new_instrs, snake_list, env = normalize_statement(snake_list, env)
        normal_list += new_instrs

    return normal_list


def normalize(snake_list: List[Snake]) -> List[Normal]:
    """
    Converts Snake instructions into Normal form instructions.

    Args:
        :param snake_list: List of Snake instructions to normalize.

    Returns:
        :return: List of all normalized instructions.

    Raises:
        Nothing.
    """

    return normalize_all(snake_list, Environment())
