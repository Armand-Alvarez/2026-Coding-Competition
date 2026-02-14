# This file is used to run automated tests against the functions in each problem

# **WARNING**: This file should **NOT** be edited. It has been specially crafted to run specific assertions against problem functions. Editing this file could break the competition.

# Note: Find a backup of this file in the Backups directory

from tests.test_1 import test as t1


all_tests = [t1]

def run_tests(problem_number: int = None) -> None:
    """
    Run automated tests aginst the problem suite. 

    Prints if you have a problem correct or not. 

    Args:
        problem_number(int): Only run tests against this problem number
    
    Return: 
        None
    """

    match problem_number:
        
        case 1:
            t1()

        case _:
            run_all_tests()


def run_all_tests() -> None:
    """
    Run all tests. Print the correct / total tests

    Args:
        None
    Returns:
        None
    """
    correct = 0
    total = 0
    for test in all_tests:
        c, t = test()
        correct += c
        total += t
    
    print(f"You got {correct} tests passing out of {total}")


if __name__ == "__main__":
    run_all_tests()


