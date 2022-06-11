def reverse_list(values):
    index_counter = len(values) - 1
    inverted_list = []
    for _ in values:
        inverted_list.append(values[index_counter])
        index_counter -= 1
    return inverted_list


def reverse_list_2(values):
    inverted_list = []
    for v in range(len(values)-1, -1, -1):
        inverted_list.append(values[v])
    return inverted_list



my_list = ['hello', 'world', 'message']

print(reverse_list(my_list))
print(reverse_list_2(my_list))



