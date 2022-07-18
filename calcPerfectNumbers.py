def calc_perfect_numbers(max_value: int) -> list:
    if max_value <= 10000:
        result_list = []
        for num in range(2, max_value + 1):
            if is_perfect_number(num):        # True
                result_list.append(num)
        return result_list


def is_perfect_number(num) -> bool:
    result_sum_numbers = 1
    for n in range(2, (num // 2) + 1):
        if num % n == 0:
            result_sum_numbers += n
    return result_sum_numbers == num


print(calc_perfect_numbers(100))

