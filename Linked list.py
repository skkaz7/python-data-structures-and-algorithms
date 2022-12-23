class Node:
    def __init__(self, data=None, next_value=None):
        self.data = data
        self.next_value = next_value


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def display(self):
        if self.head is None:
            print('Linked list is empty!')
            return

        iterator = self.head
        result = 'HEAD->'
        while iterator:
            result += str(iterator.data) + '->'
            iterator = iterator.next_value

        result += 'NULL'
        print(result)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        iterator = self.head
        while iterator.next_value:
            iterator = iterator.next_value

        iterator.next_value = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        iterator = self.head
        while iterator:
            iterator = iterator.next_value
            count += 1

        return count

    def remove_from_beginning(self):
        self.head = self.head.next_value

    def remove_from_end(self):
        index = 0
        iterator = self.head
        while index < self.get_length() - 2:
            iterator = iterator.next_value
            index += 1

        iterator.next_value = None

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index!')

        if index == 0:
            self.remove_from_beginning()

        iterator = self.head
        count = 0
        while iterator:
            if count == index - 1:
                iterator.next_value = iterator.next_value.next_value
            iterator = iterator.next_value
            count += 1

    def insert_at(self, data, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index!')

        if index == 0:
            self.insert_at_beginning(data)

        iterator = self.head
        count = 0
        while iterator:
            if count == index - 1:
                iterator.next_value = Node(data, iterator.next_value)
            iterator = iterator.next_value
            count += 1


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_beginning(1)
    linked_list.insert_at_beginning(2)
    linked_list.insert_at_beginning(3)
    linked_list.insert_at_beginning(4)
    linked_list.insert_at_end(0)
    # linked_list.remove_from_beginning()
    # linked_list.remove_from_end()
    linked_list.remove_at(2)
    linked_list.insert_at(2, 2)
    linked_list.insert_at(5, 0)
    # linked_list.insert_values(['first', 'second', 'third'])
    print(linked_list.get_length())
    linked_list.display()
