# Test file for problem 04
from problems.problem_04.problem import answer

tests = [
    (([7, 19, 1, 27], [7, 23, 14, 9, 27]), [1, 9, 14, 19, 23]),
    (([1, 2, 3], [3, 2, 1]), []),
    (([45, 8, 19, 2], [66, 33, 12, 8]), [2, 12, 19, 33, 45, 66]),
    (
        (
            [99, 23, 109, 8932, -87, 123, 13, 0, 3945, 1450],
            [8932, 77, 340, 87, 202, 13, 10, 1450],
        ),
        [-87, 0, 10, 23, 77, 87, 99, 109, 123, 202, 340, 3945],
    ),
    (([2, 4, 8, 6], [9, 7, 5, 3, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9]),
]


def test() -> tuple:
    """
    Test for problem.

    Args:
        None

    Returns:
        tuple: The number of passing tests, the total number of tests
    """

    correct = 0
    num_tests = len(tests)
    for test in tests:
        if test_func(test[0], test[1]):
            correct += 1

    return (correct, num_tests)


def test_func(input, output) -> bool:
    try:
        assert answer(*input) == output
        return True
    except AssertionError, Exception:
        return False


if __name__ == "__main__":
    test()
