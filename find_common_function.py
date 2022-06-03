
def find_common(values1, values2):
    if len(values1) > len(values2):
        values1, values2 = values2, values1

    my_set = set()
    for x in values1:
        if x in values2:
            my_set.add(x)
    return my_set


array1 = [0, 1, 0, 4, 10]
array2 = [1, 5, 0, 0, 7, 0, 2, 0, 1, 12, 0, 4]

print(find_common(array2, array1))
