# This is a calculator that takes three values x, y,
# and an a and returns the result according to the a
def Calculator(x, y, a):
    result =x+y if a == '+' else x-y if a== '-' else x/y if a == '/' else x*y
    return result


def addNumbers(a, b):
    """
    Sum up two integers
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two integer arguments
    """
    return a + b

def my_big_function(x, n):
    """
    Powering x to n
    :param x: integer
    :param n: integer
    :return: x to the power n
    """
    return x**n


print(Calculator(2, 4, '*'))
print(addNumbers(2, 4))
print(my_big_function(2, 4))