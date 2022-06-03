def is_palindrome(text: str) -> bool:
    text = str(text).upper()
    return text == text[::-1]


print(is_palindrome("ABCXcba"))
