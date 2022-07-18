def calc_sum_all_numbers_div_by_2O_r_7(max_value: int) -> int:
    counter = 0
    for num in range(1, max_value):
        if num % 2 or num % 7 == 0:
            counter += 1
    return counter


print(calc_sum_all_numbers_div_by_2O_r_7(8))
