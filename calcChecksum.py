def calc_checksum(digits: str) -> int:
    result_checksum = 0
    for index, value in enumerate(digits):
        calc_sum = int(value) * (index + 1)
        result_checksum += calc_sum
    return result_checksum % 10


print(calc_checksum('87654321'))

