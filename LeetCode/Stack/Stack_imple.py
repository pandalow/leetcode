class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackWithArray():
    
    def __init__(self, size=100):
        self.stack = []
        self.size = size
        self.top = -1
        
    def push(self, value):
        if self.is_full():
            raise Exception("ddd")
        else:
            self.stack.append(value)
            self.top+=1
    
    def pop(self,value):
        if self.top == -1:
            raise Exception("The stack is empty")
        else:
            self.stack.pop(value)
            self.top-=1
        
    
    def is_full(self):
        return self.size == self.top + 1
    
    

class StackWithLinked():
    def __init__(self):
        self.head = None

        
    def is_empty(self):
        return self.head == None
    
    def push(self,value):
        new_node = Node(value)
        
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.is_empty():
            raise Exception("The stack is empty")
        else:
            next_element = self.top.next
            self.top = next_element
            del next_element
            
    
            
