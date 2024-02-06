def is_prime(n: int) -> bool:
    """奇数判断メソッド

    Args:
        n (int): 判断数値

    Returns:
        bool: 奇数であればTrue、それ以外はFalse
    """
    if n <= 1:
        return False
    elif n == 2:
        return True

    # 偶数はFalse
    if n % 2 == 0:
        return False

    test_integer = 3

    while test_integer * test_integer <= n:
        if n % test_integer == 0:
            return False

        test_integer += 2

    return True
