def difference_arithmetic_progress(n):
    """
    Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
    :param n:
    :return: int
    """
    sum_progress = (n*(n+1)/2)**2
    sum_pow = (1/6) * ((2*(n**3)) + (3*(n**2)) + n)
    return int(abs(sum_pow-sum_progress))
