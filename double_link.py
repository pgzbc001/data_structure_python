class Node:
    """定义node类"""

    """node属性初始化"""
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class doubleLinkedList:
    """定义双链表"""

    """双链表属性初始化"""
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        """判断链表是否为空"""
        return self.size == 0

    def append(self, item):
        """尾节点处插入节点"""
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
        """头节点处插入节点"""
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
        """删除指定节点"""
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
        """查询节点数据"""
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
        """遍历所有节点打印数据"""
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