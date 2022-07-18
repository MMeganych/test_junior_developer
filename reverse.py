def reverse_text(text):
    index_counter = (len(text) - 1)
    inverted_string = ''
    for _ in text:
        inverted_string += text[index_counter]
        index_counter -= 1
    return inverted_string


def reverse_text_2(text):
    inverted_string = ''
    for i in text:
        inverted_string = i + inverted_string
    return inverted_string


def reverse_text_3(text):
    inverted_string = ''
    for i in range(len(text)-1, -1, -1):
        inverted_string += text[i]
    return inverted_string


def reverse_4(text):
    reversed_text = ""
    for current_char in reversed(text):
        reversed_text += current_char
    return reversed_text


def reverse_5(text):
    reversed_text = ""
    return reversed_text.join(reversed(text))


print(reverse_text('message'))
print(reverse_text_2('message'))
print(reverse_text_3('message'))
print(reverse_4('message'))
print(reverse_5('message'))
