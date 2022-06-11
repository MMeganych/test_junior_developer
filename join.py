def join(values, delimiter):
    result_string = ''
    for s in values:
        result_string += delimiter + s
    return result_string[3:]


def join_2(values, delimiter):
    result_string = ''
    for s in values:
        result_string += delimiter + s
    return result_string.replace(delimiter, '', 1)


my_list = ['hello', 'world', 'message']

print(join(my_list, '+++'))
print(join_2(my_list, '+++'))
