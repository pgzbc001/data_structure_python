class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class doubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def append(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp
        self.size += 1

    def prepend(self, item):
        temp = Node(item)
        if self.head == None:
            self.head =  temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        self.size += 1

    def remove(self, item):
        current = self.head
        while current != None:
            if current.data == item:
                if current is self.head:
                    self.head = current.next
                    if self.head != None:
                        self.head.prev = None
                elif current is self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.size -= 1
                return True
            current = current.next
        return False
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
                break
            else:
                current = current.next
        return found
    
    def print_all(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
    
d = doubleLinkedList()
# d.append(1)
# d.append(2)
# d.append(3)
d.append(4)
d.append(5)

# d.prepend(1)
# d.prepend(2)
# d.prepend(3)
# d.prepend(4)
# d.prepend(5)

d.remove(5)
d.print_all()

    