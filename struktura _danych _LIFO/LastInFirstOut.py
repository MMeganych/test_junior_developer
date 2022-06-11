class Stack:
    def __init__(self):
        self.values = []

    # Is stack empty
    def is_empty(self):
        return len(self.values) == 0

    # Adds an element to the top of the stack
    def push(self, element):
        self.values.append(element)

    # Selects and deletes the top item
    def pop(self):
        if self.is_empty():
            return None
        return self.values.pop()

    # Examines the element at the end of the stack
    def peek(self):
        if self.is_empty():
            return None
        return self.values[-1]


def main():
    stack = Stack()
    stack.push("first")
    stack.push("second")
    print("PEEK: " + stack.peek())
    print("POP: " + stack.pop())
    print("POP: " + stack.pop())
    print("IS EMPTY: " + str(stack.is_empty()))


main()
