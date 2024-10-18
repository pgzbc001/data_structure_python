class Stack:
    """定义栈"""

    class Empty(Exception):
        """对于空的栈，在调用pop或peek方法时抛出的异常"""
        pass

    class Full(Exception):
        """对于满的栈，在调用push方法时抛出的异常"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """初始化"""
        self.capacity = capacity         # 栈主体
        self.stk = [None] * capacity     # 栈的容量
        self.ptr = 0                     # 栈指针


    def length(self) -> int:
        """返回以及进栈的数据的个数"""
        return self.ptr
    
    def is_empty(self) -> bool:
        """栈是否为空"""
        return self.ptr == 0

    def is_full(self) -> bool:
        """栈是否为满"""
        return self.ptr >= self.capacity
    
    def push(self, value) -> None:
        """将value入栈"""
        if self.is_full():
            raise Stack.Full
        
        self.stk[self.ptr] = value
        self.ptr += 1

    
    def pop(self):
        """让数据出栈"""
        if self.is_empty():
            raise Stack.Empty

        self.ptr -= 1
        return self.stk[self.ptr]
    
    def clear(self) -> None:
        """清空栈"""
        self.ptr = 0

    def search(self, value):
        """从栈中查找value并返回下标，未找到返回-1"""
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1
    
    def peek(self):
        """查看栈顶数据"""
        if self.is_empty():
            raise Stack.Empty
        return self.stk[self.ptr - 1]
    
    def dump(self) -> None:
        """打印所有数据"""
        if self.is_empty():
            print('is empty')
        else:
            print(self.stk[:self.ptr])


s = Stack(64)
s.push(56)
s.push(52)
s.push(55)
print(s.pop())
print(s.length())
print(s.peek())
s.dump()