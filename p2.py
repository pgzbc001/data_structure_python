class Node():
    """node"""
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next


class linkedList:
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def lengh(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def add_first(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def add_larst(self, item):
        if self.is_empty():
            self.add_first(item)
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            
            temp = Node(item)
            current.setNext(temp)
            temp.setNext(None)

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.data == item:
                found = True
                break
            else:
                current = current.getNext()
        return found

    def print_all(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.getNext()




l = linkedList()
# l.add_first(5)
# l.add_first(4)
# l.add_first(3)
# l.add_first(2)
# l.add_first(1)

l.add_larst(1)
l.remove(1)

# print(l.is_empty())
print(l.lengh())

l.print_all()

# print(l.search(3))
# print(l.search(6))



    
    

