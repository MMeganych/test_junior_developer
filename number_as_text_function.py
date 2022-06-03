def number_as_text(numeric: int):
    string_tuple_list_for_digits = (
        'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR',
        'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE'
    )
    for num in str(numeric):
        print(string_tuple_list_for_digits[int(num)], end=' ')


number_as_text(148239)
