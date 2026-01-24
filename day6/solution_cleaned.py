import operator
import sys
from functools import reduce
from itertools import groupby
from typing import List, Callable, Dict, Any, Iterable

import numpy as np
import numpy.typing as npt

# Define available operators
OPERATORS: Dict[str, Callable[[Any, Any], Any]] = {
    "*": operator.mul,
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
}


def parse_as_numbers(filename: str) -> npt.NDArray[Any]:
    """
    Parses the input file as a matrix of numbers and operators (for horizontal reading).
    Uses numpy.genfromtxt which handles whitespace-separated values.
    """
    return np.genfromtxt(filename, dtype=str)


def parse_as_grid(filename: str) -> npt.NDArray[Any]:
    """
    Parses the input file as a character grid (for vertical reading).
    Preserves exact character positions.
    """
    with open(filename, "r") as file:
        lines = [list(line.strip("\n")) for line in file]
    return np.array(lines)


def solve_horizontal(data: npt.NDArray[Any]) -> int:
    """
    Solves Part 1: Numbers are read horizontally as provided in the input.
    """
    # Data is expected to be [rows of numbers..., row of operators]

    # Extract operand columns (all rows except the last)
    # Transpose so each row in 'operand_columns' corresponds to a column in input
    operand_columns = data[:-1, :].T.astype(int)

    # Extract operators (last row)
    operators = data[-1, :]

    results = []
    for operands, op_symbol in zip(operand_columns, operators):
        if op_symbol in OPERATORS:
            res = reduce(OPERATORS[op_symbol], operands)
            results.append(res)

    return sum(results)


def solve_vertical(data: npt.NDArray[Any]) -> int:
    """
    Solves Part 2: Numbers are formed by reading characters vertically down columns.
    """
    # Transpose to work with columns as rows
    # data.T shape: (cols, rows)
    # The last column of the transposed data (bottom row of original) contains operators
    operators_col = data.T[:, -1]

    # The rest are the characters forming numbers
    number_grid = data.T[:, :-1]

    # Join characters in each column to form strings.
    # We strip spaces because the numbers are formed by digits in the column,
    # and "   " (empty space) is a separator or padding.
    column_strings = ["".join(row).strip() for row in number_grid]

    # Group non-empty strings.
    # An empty string in 'column_strings' means that column was blank (separator).
    # groupby will group consecutive non-empty strings together.
    operand_groups = [
        list(group)
        for is_empty, group in groupby(column_strings, lambda x: x == "")
        if not is_empty
    ]

    # Filter operators, ignoring empty spaces
    valid_operators = [str(op) for op in operators_col if op.strip() != ""]

    results = []
    # Zip the groups of numbers with their corresponding operator
    for operands, op_symbol in zip(operand_groups, valid_operators):
        # Convert the string operands ("1", "24", "356") to integers
        int_operands = map(int, operands)

        if op_symbol in OPERATORS:
            res = reduce(OPERATORS[op_symbol], int_operands)
            results.append(res)

    return sum(results)


def solve(filename: str) -> None:
    data_numbers = parse_as_numbers(filename)
    data_grid = parse_as_grid(filename)

    p1 = solve_horizontal(data_numbers)
    print(f"Part 1: {p1}")

    p2 = solve_vertical(data_grid)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    solve(filename)

