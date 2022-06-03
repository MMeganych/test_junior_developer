def order_even_before_odd(numbers):
    for num in numbers:
        if num % 2 != 0:
            numbers.remove(num)
            numbers.append(num)
    return numbers


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(order_even_before_odd(numbers_list))

