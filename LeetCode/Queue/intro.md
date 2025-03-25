2.3.1 循环队列的顺序存储基本描述
下面我们以「方式 3」中特意空出来一个位置的处理方式为例，对循环队列的顺序存储做一下基本描述。

循环队列的顺序存储

我们约定：
 为循环队列的最大元素个数。队头指针 
 指向队头元素所在位置的前一个位置，而队尾指针 
 指向队尾元素所在位置。

初始化空队列：创建一个空队列，定义队列大小为 
。令队头指针 
 和队尾指针 
 都指向 
。即 
。
判断队列是否为空：根据 
 和 
 的指向位置进行判断。根据约定，如果队头指针 
 和队尾指针 
 相等，则说明队列为空。否则，队列不为空。
判断队列是否已满：队头指针在队尾指针的下一位置，即 
，则说明队列已满。否则，队列未满。
插入元素（入队）：先判断队列是否已满，已满直接抛出异常。如果不满，则将队尾指针 
 向右循环移动一位，并进行赋值操作。此时 
 指向队尾元素。
删除元素（出队）：先判断队列是否为空，为空直接抛出异常。如果不为空，则将队头指针 
 指向元素赋值为 
，并将 
 向右循环移动一位。
获取队头元素：先判断队列是否为空，为空直接抛出异常。如果不为空，因为 
 指向队头元素所在位置的前一个位置，所以队头元素在 
 后一个位置上，返回 
。
获取队尾元素：先判断队列是否为空，为空直接抛出异常。如果不为空，因为 
 指向队尾元素所在位置，所以直接返回 
。
2.3.2 循环队列的顺序存储实现代码
```
class Queue:
    # 初始化空队列
    def __init__(self, size=100):
        self.size = size + 1
        self.queue = [None for _ in range(size + 1)]
        self.front = 0
        self.rear = 0
        
    # 判断队列是否为空
    def is_empty(self):
        return self.front == self.rear
    
    # 判断队列是否已满
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    # 入队操作
    def enqueue(self, value):
        if self.is_full():
            raise Exception('Queue is full')
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            
    # 出队操作
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        
    # 获取队头元素
    def front_value(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            value = self.queue[(self.front + 1) % self.size]
            return value
        
    # 获取队尾元素
    def rear_value(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            value = self.queue[self.rear]
            return value
```