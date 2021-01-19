"""
This part should write down a simpy introduction to this file
"""


def my_function(var1: int, var2: int) -> int:
    """
    Brief description of the goal of this function

    Args:
        To give the statement or explain the meaning of arguments
        - var1: explain meaning of var1
        - var2: explain meaning of var2 ...

    Returns:
        To describe what would return after use of this function

    Example:
        my_function(1, 2) = 3
    """
    return var1 + var2

if __name__ == '__main__':
    print('the annotations of my_function is :')
    print(my_function.__annotations__)
    print('\n')
    print('the docstring of my_function is:')
    print(my_function.__doc__)
