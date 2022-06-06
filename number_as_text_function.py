def number_as_text(numeric: int):
    string_tuple_list_for_digits = (
        'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR',
        'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE'
    )
    result_func = ''
    for num in str(numeric):
        result_func += string_tuple_list_for_digits[int(num)] + ' '
    return str(result_func)


print(number_as_text(148239))
