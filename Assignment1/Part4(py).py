class queue:
    def __init__(self):
        self.queue = []
        is_empty= True
    
    def enqueue(self, integer):
        self.queue.append(integer)
        
    def dequeue(self):
        if len(self.queue) <= 0:
            print("Out of range")
        else:
            del self.queue[0]
        
    def rear(self):
        if len(self.queue) <= 0:
            print("Queue is empty")
        else:
            return self.queue[len(self.queue)-1]
        
    def front(self):
        if len(self.queue) <= 0:
            print("Queue is Empty")
        else:
             return self.queue[0]
        
    def size(self):
        return len(self.queue)
        
    def isEmpty(self):
        if self.size() > 0:
            is_empty = False
        return is_empty
        
        
        

        
        
        