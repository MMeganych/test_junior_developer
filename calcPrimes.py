def calc_primes(max_value: int) -> list:
    return [num for num in range(2, max_value + 1) if is_prime_number(num)]


def is_prime_number(num) -> bool:
    if num < 2:
        return False
    for n in range(2, (num // 2) + 1):
        if num % n == 0:
            return False
    return True


print(calc_primes(15))  # [2, 3, 5, 7, 11, 13]
print(is_prime_number(4))
