import math


def get_max_prime_divider(n):
    """
    Каков самый большой делитель числа 600851475143, являющийся простым числом?
    :param n:
    :return: int
    """
    max_prime = None
    while n % 2 == 0:
        n = n / 2
        max_prime = n
    while n % 3 == 0:
        max_prime = 3
        n = n / 3
    for i in range(5, int(math.sqrt(n))+1, 6):
        while n % i == 0:
            max_prime = i
            n = n / i

    return max_prime

