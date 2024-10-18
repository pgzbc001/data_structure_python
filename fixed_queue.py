class FixedQueue():
    """定义环形队列"""

    class Empty(Exception):
        """对于空的队列，在调用deque或peek方法时抛出的异常"""
        pass

    class Full(Exception):
        """对于满的队列，在调用enque方法时抛出的异常"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """初始化"""
        self.no = 0                      # 当前数据个数
        self.front = 0                   # 队头元素游标
        self.rear = 0                    # 队尾元素游标
        self.capacity = capacity         # 队列容量
        self.que = [None] * capacity     # 队列主体

    
    def length(self) -> int:
        """返回已经入队的数据的个数"""
        return self.no

    def is_empty(self) -> bool:
        """队列是否为空"""
        return self.no <= 0

    def is_full(self) -> bool:
        """队列是否已满"""
        return self.no >= self.capacity
    
    def enque(self, x)-> None:
        """让数据x入队"""
        if self.is_full():
            raise FixedQueue.Full
        
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1

        if self.rear == self.capacity:
            self.rear = 0

    
    def deque(self):
        """让数据出队"""
        if self.is_empty():
            raise FixedQueue.Empty
        
        x = self.que[self.front]
        self.front += 1
        self.no -= 1

        if self.front == self.capacity:
            self.front = 0

    def peek(self):
        """查看队头元素"""
        if self.is_empty():
            raise FixedQueue.Empty
        
        return self.que[self.front]
    
    def find(self, value):
        """从队列中查找value并返回下标，未找到返回-1"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
            
        return -1
    
    def clear(self):
        """清空队列"""
        self.no = self.front = self.rear = 0
    
    def dump(self):
        """打印所有数据"""
        if self.is_empty():
            print('que is empty')
        else:
            for i in range(self.no):
                idx = (i + self.front) % self.capacity
                print(self.que[idx], end=' ')
            print()


q = FixedQueue()
q.enque(1)
q.enque(2)
q.enque(3)

q.deque()

print(q.length())
print(q.peek())

q.dump()