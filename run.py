class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def insert_beginning(self, elem):
        if self.head:
            node = Node(elem)
            node.next = self.head
            self.head = node
        else:
            self.head = Node(elem)
        self._size += 1

    def insert_end(self, elem):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size += 1

    def remove(self, value):
        if self.head:
            pointer = self.head
            while(pointer.next):
                if(pointer.data == value):
                    self.head = pointer.next
                    self._size -= 1
                    return
                if pointer.next.data == value:
                    pointer.next = pointer.next.next
                    self._size -= 1
                    return
                pointer = pointer.next
            raise ValueError("value not found in the list")
        else:
            raise IndexError("list index out of range")

    def search(self, value):
        if self.head:
            pointer = self.head
            while(pointer):
                if pointer.data == value:
                    return pointer
                pointer = pointer.next
            raise ValueError("value not found in the list")
        else:
            raise IndexError("list index out of range")

    def print_list(self):
        if self.head:
            print(self.head.data)
            if self.head.next:
                pointer = self.head
                while(pointer.next):
                    pointer = pointer.next
                    print(pointer.data)
        else:
            raise ValueError('no head')

    def size(self):
        return self._size

    def is_empty(self):
        if self.head:
            return False
        else:
            return True