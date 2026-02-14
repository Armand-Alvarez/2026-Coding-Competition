# Test file for problem 001
from problems.problem_1.problem_1 import answer
import sys
from io import StringIO


def test() -> tuple:
    """ 
    Test for problem. 

    Args:
        None

    Returns:
        tuple: The number of passing tests, the total number of tests
    """

    correct = 0
    num_tests = 0
    for test_func in [test_1]:
        if test_func():
            correct += 1
        num_tests += 1

    return (correct, num_tests)
    

def test_1() -> bool:
    try:
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        answer()
        
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        assert output.startswith("Hello Field Engineers")
        return True
    except (AssertionError, Exception):
        sys.stdout = old_stdout
        return False


if __name__ == "__main__":
    test()
