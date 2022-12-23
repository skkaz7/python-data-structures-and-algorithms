class Stack:
    def __init__(self):
        self.stack = []

    def display(self):
        print(str(self.stack))

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == 3

    def push(self, item):
        return None if self.is_full() else self.stack.append(item)

    def pop(self):
        return None if self.is_empty() else self.stack.pop()

    def peek(self):
        print(None) if self.is_empty() else print(str(self.stack[-1]))


if __name__ == '__main__':
    stack = Stack()
    stack.peek()
    print(stack.pop())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.peek()
    stack.pop()
    stack.display()
