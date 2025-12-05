def add_numbers(num1: int, num2: int) -> int:
    """ Add two numbers
    :param num1: first number (int)
    :param num2: second number (int)
    :return: Sum of two numbers (int)
    """
    return num1 + num2

print(add_numbers.__doc__)

def help(f):
    print(f.__doc__)

help(add_numbers)
help(print)
