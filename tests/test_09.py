# Test file for problem 09
from problems.problem_09.problem import answer

tests = [
    ["abc", "nop"],
    ["Tony Soprano", "Gbal Fbcenab"],
    ["The Best Field Engineering Team", "Gur Orfg Svryq Ratvarrevat Grnz"],
    ["DFAS", "QSNF"],
    ["hello, there!", "uryyb, gurer!"],
    ["12345", "12345"],
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
