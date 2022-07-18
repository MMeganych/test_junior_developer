def calc_primes(max_value: int) -> list:
    result_list = []
    for num in range(2, max_value + 1):
        if is_prime_number(num):       # True
            result_list.append(num)
    return result_list


def is_prime_number(num) -> bool:
    if num < 2:
        return False
    for n in range(2, (num // 2) + 1):
        if num % n == 0:
            return False
    return True


print(calc_primes(15))
print(is_prime_number(4))
