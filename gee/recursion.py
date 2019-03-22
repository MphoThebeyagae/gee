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


def reverse(word):
    if len(word) == 1:
        return word
    else:
        return word[-1] + reverse(word[:-1])
