class Queue:
    def __init__(self):
        self.queue = []

    def display(self):
        print(str(self.queue))

    def is_empty(self):
        return len(self.queue) <= 0

    def is_full(self):
        return len(self.queue) == 3

    def enqueue(self, item):
        return None if self.is_full() else self.queue.insert(0, item)

    def dequeue(self):
        return None if self.is_empty() else self.queue.pop()

    def peek(self):
        print(None) if self.is_empty() else print(str(self.queue[-1]))


if __name__ == '__main__':
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.peek()
    q.display()

    q.dequeue()
    q.peek()
    q.display()
