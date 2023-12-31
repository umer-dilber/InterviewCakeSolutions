class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

    def getMax(self):
        toatal = len(self.items)
        maximum = self.items[-1]
        for i in range(toatal-2, -1, -1):
            maximum = max(maximum, self.items[i])
        
        return maximum

stack = Stack()
stack.push(20) 
stack.push(10)
stack.push(9)
print(stack.getMax())