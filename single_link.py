class Node():
    """定义node类"""

    """node属性初始化"""
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    """data, next setter getter实现"""
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next


class linkedList:
    """定义单链表"""

    """单链表属性初始化"""
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self):
        """判断链表是否为空"""
        return self.head == None
    
    def lengh(self):
        """获取链表的长度"""
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def add_first(self, item):
        """头节点处插入节点"""
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def add_larst(self, item):
        """尾节点处插入节点"""
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
        """删除指定节点"""
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
        """查询节点数据"""
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
        """遍历所有节点打印数据"""
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



    
    

