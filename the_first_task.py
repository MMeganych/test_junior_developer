# Здоров висилаю тобі першу задачку
#
# Є дане ціле число(integer) 'x', написати функцію 'def reverse(x):' - котра повертає поданне ціле число 'x' з відзеркалиними числами у ньому.
#
# Приклад: print(reverse(345)) --> Output: 543
#
# Увага: ціле число подаване до функції може бути від'ємним: print(reverse(-231)) --> Output: -132
# чт 18:43
#
# Раз таке діло то ще одна задачка, дуже популярна і люблять давати для джуніорів, колись самому така попалася.
#
# Поданий масив цілих чисел 'nums', написати функцію 'def moveZero(nums)'  - котра переміщює всі нулі данного масиву в його кінець.
# Приклад:
# array1 = [0,1,0,4,10]
# array2 = [1,5,0,0,7,0,2,0,1,12,0,4]
#
# moveZero(array1) - - > 1,4,10,0,0
# moveZero(array2) - - > 1,5,7,2,1,12,4,0,0,0,0,0


def reverse(number):
    num = number
    if number < 0:
        number = abs(number)

    inverted_number = 0
    while number > 0:
        remainder = number % 10
        number = number // 10
        inverted_number = inverted_number * 10 + remainder

    if num < 0:
        return -abs(inverted_number)
    else:
        return inverted_number


def reverse_2(number):
    number_string = str(number)
    if number_string[0] == '-':
        inverted_number = '-' + number_string[:0:-1]
    else:
        inverted_number = number_string[::-1]
    return int(inverted_number)


# ---------------------------------------------------------

def move_zero(nums):
    list_of_zeros = []
    new_list = []
    for x in nums:
        if x == 0:
            list_of_zeros.append(x)
        else:
            new_list.append(x)
    return new_list + list_of_zeros


def move_zero_2(nums):
    for x in nums:
        if x == 0:
            nums.remove(x)
            nums.append(x)
    return nums



array1 = [0, 1, 0, 4, 10]
array2 = [1, 5, 0, 0, 7, 0, 2, 0, 1, 12, 0, 4]

print(move_zero(array2))  # [1, 5, 7, 2, 1, 12, 4, 0, 0, 0, 0, 0]
print(move_zero_2(array2))
print(array2)


