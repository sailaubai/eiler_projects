def sum_fib(n_max=4000000):
    """
    Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
    :param n_max:
    :return: int
    """
    a = 0
    b = 1
    f_sum = 0
    while b <= n_max:
        a, b = b, a+b
        f_sum += a
    return f_sum
