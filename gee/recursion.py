def sum_array(array):

    """

    """
    if array:
        return array[0] + sum_array(array[1:])
    else:
        return 0



def fibonacci(n):

    """
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms


    """

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def reversed_string(a_string):
    new_strings = []
    index = len(a_string)
    while index:
        index -= 1
        new_strings.append(a_string[index])
    return ''.join(new_strings)
