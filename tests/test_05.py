# Test file for problem 05
from problems.problem_05.problem import answer

tests = [
    [49, True],
    [97, True],
    [1234, False],
    [11, False],
    [55, False],
    [54, False],
    [13, True],
    [19, True],
    [23, True],
    [28, True],
    [4, False],
    [5, False],
    [6, False],
    [2, False]
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
        assert answer(input) == output
        return True
    except AssertionError, Exception:
        return False


if __name__ == "__main__":
    test()
