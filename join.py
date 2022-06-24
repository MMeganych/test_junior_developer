def join(values, delimiter):
    result_string = ''
    for index, value in enumerate(values):
        if index == len(values) - 1:
            result_string += value
        else:
            result_string += value + delimiter
    return result_string


def join_2(values, delimiter):
    result_string = ''
    for s in values:
        result_string += delimiter + s
    return result_string.replace(delimiter, '', 1)


my_list = ['hello', 'world', 'message']

print(join(my_list, '*******'))
print(join_2(my_list, '+++++'))
