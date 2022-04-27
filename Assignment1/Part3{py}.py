class my_stack:
    def __init__(self):
        self.stack = []
        is_empty= True
    
    def push(self, integer):
        self.stack.append(integer)
   
    def pop(self):
        if len(self.stack) <= 0:
            print("Out of range")
        else:
            temp = self.stack[len(self.stack)-1]
            del self.stack[len(self.stack)-1]
            return temp
    
    def top(self):
        if len(self.stack) <= 0:
            print("Stack is Empty")
        return self.stack[len(self.stack)-1]
    
    def isEmpty(self):
        if len(self.stack) > 0:
            self.is_empty = False
        return is_empty
        
    def size(self):
        return len(self.stack)
        
        

        
        
        