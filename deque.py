class Deque:
    def __init__(self):
        self.deque = []

    def display(self):
        print(str(self.deque))

    def size(self):
        print(len(self.deque))

    def check_empty(self):
        return len(self.deque) <= 0

    def check_full(self):
        return len(self.deque) == 5

    def add_front(self, item):
        return None if self.check_full() else self.deque.append(item)

    def add_rear(self, item):
        return None if self.check_full() else self.deque.insert(0, item)

    def remove_front(self):
        return None if self.check_empty() else self.deque.pop()

    def remove_rear(self):
        return None if self.check_empty() else self.deque.pop(0)


if __name__ == '__main__':
    deque = Deque()

    deque.add_rear(1)
    deque.add_rear(2)
    deque.add_rear(3)
    deque.add_rear(4)
    deque.add_front(0)
    deque.add_rear(5)
    deque.size()
    deque.display()

    deque.remove_front()
    deque.remove_rear()
    deque.size()
    deque.display()
